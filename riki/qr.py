"""Vienkāršs QR koda ģenerators bez ārējām bibliotēkām (baitu režīms,
kļūdu labošanas līmenis M, versijas 1–6, līdz 106 baitiem).

    from qr import qr_svg
    svg = qr_svg("https://www.youtube.com/playlist?list=...")

Algoritms atbilst ISO/IEC 18004; pārbaudīts ar OpenCV QR dekoderi
(riki/qr.py --test).
"""
import sys

# versija: (datu kodvārdi kopā, EC kodvārdi blokā, bloku skaits) līmenim M
_M = {1: (16, 10, 1), 2: (28, 16, 1), 3: (44, 26, 1), 4: (64, 18, 2), 5: (86, 24, 2), 6: (108, 16, 4)}
_ALIGN = {1: [], 2: [6, 18], 3: [6, 22], 4: [6, 26], 5: [6, 30], 6: [6, 34]}


def _gmul(x, y):
    z = 0
    for i in reversed(range(8)):
        z = (z << 1) ^ ((z >> 7) * 0x11D)
        z ^= ((y >> i) & 1) * x
    return z


def _rs_divisor(degree):
    res = [0] * (degree - 1) + [1]
    root = 1
    for _ in range(degree):
        for j in range(degree):
            res[j] = _gmul(res[j], root)
            if j + 1 < degree:
                res[j] ^= res[j + 1]
        root = _gmul(root, 0x02)
    return res


def _rs_remainder(data, div):
    res = [0] * len(div)
    for b in data:
        f = b ^ res.pop(0)
        res.append(0)
        for i, c in enumerate(div):
            res[i] ^= _gmul(c, f)
    return res


def _codewords(text):
    data = text.encode("utf-8")
    for ver in range(1, 7):
        cap, ec, nb = _M[ver]
        if len(data) + 2 <= cap:
            break
    else:
        raise ValueError("Teksts par garu (vairāk nekā 106 baiti)")
    bits = [0, 1, 0, 0] + [(len(data) >> i) & 1 for i in reversed(range(8))]
    for b in data:
        bits += [(b >> i) & 1 for i in reversed(range(8))]
    bits += [0] * min(4, cap * 8 - len(bits))
    bits += [0] * (-len(bits) % 8)
    cw = [int("".join(map(str, bits[i:i + 8])), 2) for i in range(0, len(bits), 8)]
    k = 0
    while len(cw) < cap:
        cw.append((0xEC, 0x11)[k % 2])
        k += 1
    bl = cap // nb
    blocks = [cw[i * bl:(i + 1) * bl] for i in range(nb)]
    div = _rs_divisor(ec)
    ecs = [_rs_remainder(b, div) for b in blocks]
    out = [b[i] for i in range(bl) for b in blocks] + [e[i] for i in range(ec) for e in ecs]
    return ver, out


def _matrix(ver, cws, mask):
    n = 17 + 4 * ver
    m = [[False] * n for _ in range(n)]
    fn = [[False] * n for _ in range(n)]

    def setf(x, y, v):
        m[y][x] = v
        fn[y][x] = True

    for i in range(n):
        setf(6, i, i % 2 == 0)
        setf(i, 6, i % 2 == 0)
    for cx, cy in ((3, 3), (n - 4, 3), (3, n - 4)):
        for dy in range(-4, 5):
            for dx in range(-4, 5):
                x, y = cx + dx, cy + dy
                if 0 <= x < n and 0 <= y < n:
                    setf(x, y, max(abs(dx), abs(dy)) not in (2, 4))
    al = _ALIGN[ver]
    for i, ax in enumerate(al):
        for j, ay in enumerate(al):
            if (i == 0 and j == 0) or (i == 0 and j == len(al) - 1) or (i == len(al) - 1 and j == 0):
                continue
            for dy in range(-2, 3):
                for dx in range(-2, 3):
                    setf(ax + dx, ay + dy, max(abs(dx), abs(dy)) != 1)

    def fmt(mk):
        data = (0 << 3) | mk                       # līmenis M = 00
        rem = data
        for _ in range(10):
            rem = (rem << 1) ^ ((rem >> 9) * 0x537)
        bits = ((data << 10) | rem) ^ 0x5412
        b = lambda i: (bits >> i) & 1 == 1
        for i in range(6):
            setf(8, i, b(i))
        setf(8, 7, b(6)); setf(8, 8, b(7)); setf(7, 8, b(8))
        for i in range(9, 15):
            setf(14 - i, 8, b(i))
        for i in range(8):
            setf(n - 1 - i, 8, b(i))
        for i in range(8, 15):
            setf(8, n - 15 + i, b(i))
        setf(8, n - 8, True)

    fmt(mask)
    i = 0
    total = len(cws) * 8
    right = n - 1
    while right >= 1:
        if right == 6:
            right = 5
        for vert in range(n):
            for j in range(2):
                x = right - j
                up = ((right + 1) & 2) == 0
                y = n - 1 - vert if up else vert
                if not fn[y][x] and i < total:
                    m[y][x] = (cws[i >> 3] >> (7 - (i & 7))) & 1 == 1
                    i += 1
        right -= 2
    masks = [lambda x, y: (x + y) % 2 == 0, lambda x, y: y % 2 == 0, lambda x, y: x % 3 == 0,
             lambda x, y: (x + y) % 3 == 0, lambda x, y: (x // 3 + y // 2) % 2 == 0,
             lambda x, y: x * y % 2 + x * y % 3 == 0, lambda x, y: (x * y % 2 + x * y % 3) % 2 == 0,
             lambda x, y: ((x + y) % 2 + x * y % 3) % 2 == 0]
    f = masks[mask]
    for y in range(n):
        for x in range(n):
            if not fn[y][x] and f(x, y):
                m[y][x] = not m[y][x]
    return m


def _penalty(m):
    n = len(m)
    p = 0
    for rows in (m, [list(c) for c in zip(*m)]):
        for r in rows:
            run = 1
            for k in range(1, n):
                if r[k] == r[k - 1]:
                    run += 1
                else:
                    if run >= 5:
                        p += run - 2
                    run = 1
            if run >= 5:
                p += run - 2
            s = "".join("1" if v else "0" for v in r)
            p += 40 * (s.count("10111010000") + s.count("00001011101"))
    for y in range(n - 1):
        for x in range(n - 1):
            if m[y][x] == m[y][x + 1] == m[y + 1][x] == m[y + 1][x + 1]:
                p += 3
    dark = sum(v for r in m for v in r)
    p += abs(dark * 20 - n * n * 10) // (n * n) * 10
    return p


def qr_matrix(text):
    ver, cws = _codewords(text)
    best = min((_penalty(_matrix(ver, cws, k)), k) for k in range(8))[1]
    return _matrix(ver, cws, best)


def qr_svg(text, module=1, color="#1f2933", quiet=4):
    m = qr_matrix(text)
    n = len(m)
    size = n + 2 * quiet
    d = "".join(f"M{x + quiet} {y + quiet}h1v1h-1z" for y in range(n) for x in range(n) if m[y][x])
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" '
            f'shape-rendering="crispEdges" class="qr-svg"><rect width="{size}" height="{size}" fill="white"/>'
            f'<path d="{d}" fill="{color}"/></svg>')


def _test(texts):
    import numpy as np
    import cv2
    det = cv2.QRCodeDetector()
    ok = True
    for t in texts:
        m = qr_matrix(t)
        n = len(m)
        s = 10
        img = np.full(((n + 8) * s, (n + 8) * s), 255, np.uint8)
        for y in range(n):
            for x in range(n):
                if m[y][x]:
                    img[(y + 4) * s:(y + 5) * s, (x + 4) * s:(x + 5) * s] = 0
        val, _, _ = det.detectAndDecode(img)
        print(("OK  " if val == t else "KĻŪDA ") + f"v{(n - 17) // 4}: {t} -> {val!r}")
        ok &= val == t
    return ok


if __name__ == "__main__":
    if "--test" in sys.argv:
        sys.exit(0 if _test(["LRAL", "https://lral.lv", "https://www.youtube.com/playlist?list=PLYNdYxlVHYrA",
                             "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PLYNdYxlVHYrA&index=12",
                             "x" * 80, "y" * 100]) else 1)
