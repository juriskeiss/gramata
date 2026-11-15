"""14.–17. nodaļas zīmējumi."""
import math
from lib import (Fig, K, G, LG, MG, chain, tw, arcpts, RED, RED_T, BLUE, BLUE_T,
                 GREEN, GREEN_T, AMBER, AMBER_T, BRICK, BRICK_T)
from figs_b import _groundline


def _pt(cx, cy, r, a):
    return (cx + r * math.sin(a), cy - r * math.cos(a))


def f14_1():
    f = Fig(760, 340)
    cx, cy, R = 380, 1200, 950
    A = 0.40
    # jonosfēra
    f.pl(arcpts(cx, cy, R + 168, -A, A), w=30, color=BLUE_T)
    f.text(cx, cy - R - 195, "jonosfēra", size=13, bold=True, color=BLUE)
    # Zeme
    earth = arcpts(cx, cy, R, -A, A)
    f.pl(earth + [(earth[-1][0], 340), (earth[0][0], 340)], close=True, fill=GREEN_T, w=0, color=GREEN_T)
    f.pl(earth, w=2)
    f.text(cx, 296, "Zeme", size=13, bold=True)
    # masti
    aT, aD, aR = -0.33, -0.21, 0.33
    for a, lab in ((aT, "raidītājs"), (aD, ""), (aR, "uztvērējs")):
        f.line(*_pt(cx, cy, R, a), *_pt(cx, cy, R + 36, a), w=3)
        if lab:
            x, y = _pt(cx, cy, R - 18, a)
            f.text(x, y + 4, lab, size=11, italic=True)
    T = _pt(cx, cy, R + 36, aT)
    # tiešais vilnis
    D = _pt(cx, cy, R + 36, aD)
    f.arrow(T[0], T[1], D[0], D[1], w=2, color=AMBER)
    f.ltext((T[0] + D[0]) / 2 - 6, (T[1] + D[1]) / 2 - 9, "tiešais vilnis", anchor="start", size=11, color=AMBER, bold=True)
    # zemes vilnis
    gw = arcpts(cx, cy, R + 9, aT + 0.012, 0.02, n=40)
    f.pl(gw[:-2], dash="6 4", w=2, color=GREEN)
    f.arrow(gw[-4][0], gw[-4][1], gw[-1][0], gw[-1][1], w=2, color=GREEN)
    x, y = _pt(cx, cy, R + 26, -0.08)
    f.text(x, y, "zemes vilnis", size=12, color=GREEN, bold=True)
    # telpas vilnis
    I = _pt(cx, cy, R + 153, 0.0)
    Rx = _pt(cx, cy, R + 36, aR)
    f.line(T[0], T[1], I[0], I[1], w=2, color=RED)
    f.arrow(I[0], I[1], Rx[0], Rx[1], w=2, color=RED)
    f.text(I[0] + 150, I[1] + 62, "telpas vilnis", size=12, color=RED, bold=True)
    f.save("atteli/14-2-izplatisanas-veidi.svg", "Trīs radioviļņu izplatīšanās veidi")


def f14_2():
    f = Fig(780, 400)
    yg = 350
    yy = lambda h: yg - 0.72 * h
    xl, xm, xr = 110, 430, 750
    f.text((xl + xm) / 2, 22, "Diena", bold=True, size=15)
    f.text((xm + xr) / 2, 22, "Nakts", bold=True, size=15)
    # slāņi: diena
    for h1, h2, name, fill in ((60, 90, "D", "#f4cf9e"), (95, 130, "E", "#d6e3f4"), (160, 220, "F1", "#bcd1ee"), (250, 400, "F2", "#9fbce6")):
        f.rect(xl, yy(h2), xm - xl - 6, yy(h1) - yy(h2), fill=fill, rx=0, sw=0.6)
        f.text(xm - 14, (yy(h1) + yy(h2)) / 2 + 5, name, anchor="end", size=13, bold=True)
    # nakts
    f.rect(xm + 6, yy(400), xr - xm - 6, yy(200) - yy(400), fill="#9fbce6", rx=0, sw=0.6)
    f.text(xr - 8, (yy(200) + yy(400)) / 2 + 5, "F", anchor="end", size=13, bold=True)
    # zeme un ass
    f.line(xl - 10, yg, xr, yg, w=2)
    f.arrow(xl - 10, yg, xl - 10, 36, w=1.2, head=7)
    for h in (100, 200, 300, 400):
        f.line(xl - 15, yy(h), xl - 5, yy(h), w=1)
        f.text(xl - 20, yy(h) + 4, f"{h} km", anchor="end", size=11)
    f.line(xm, 34, xm, yg, dash="3 5", w=1, color=MG)
    # diena: 80 m absorbēts D slānī
    x0 = xl + 36
    f.arrow(x0, yg, x0 + 34, yy(72), w=2, color=RED)
    f.text(x0 + 34, yy(72) + 6, "×", size=20, bold=True, color=RED)
    f.text(x0 - 8, yg + 18, "80 m", size=12, bold=True, color=RED)
    f.text(x0 + 6, yg + 34, "absorbē D slānis", size=11, italic=True)
    # diena: 15 m atstarojas no F2
    xa = xl + 130
    f.line(xa, yg, xa + 70, yy(300), w=2, color=BLUE)
    f.arrow(xa + 70, yy(300), xa + 140, yg, w=2, color=BLUE)
    f.text(xa + 70, yg + 18, "15 m", size=12, bold=True, color=BLUE)
    f.text(xa + 70, yg + 34, "atstarojas no F2", size=11, italic=True)
    # nakts: 80 m atstarojas no F
    xb = xm + 50
    f.line(xb, yg, xb + 110, yy(260), w=2, color=RED)
    f.arrow(xb + 110, yy(260), xb + 220, yg, w=2, color=RED)
    f.text(xb + 110, yg + 18, "80 m", size=12, bold=True, color=RED)
    f.text(xb + 110, yg + 34, "D slāņa nav; atstarojas no F", size=11, italic=True)
    f.save("atteli/14-3-jonosferas-slani.svg", "Jonosfēras slāņi dienā un naktī")


def f14_3():
    f = Fig(780, 330)
    yg = 240
    f.rect(30, 40, 720, 28, fill=BLUE_T, rx=0, sw=0.6, color=BLUE)
    f.text(690, 59, "jonosfēra", size=12, bold=True, color=BLUE)
    _groundline(f, 30, 750, yg)
    xt = 80
    f.line(xt, yg, xt, yg - 40, w=3)
    f.text(xt - 8, yg - 16, "raidī-", anchor="end", size=11, italic=True)
    f.text(xt - 8, yg - 3, "tājs", anchor="end", size=11, italic=True)
    # zemes vilnis
    f.arrow(xt + 8, yg - 10, 230, yg - 10, dash="6 4", w=2, color=GREEN)
    f.text(160, yg - 18, "zemes vilnis", size=12, color=GREEN, bold=True)
    # telpas vilnis
    f.line(xt, yg - 40, 330, 68, w=2, color=RED)
    f.arrow(330, 68, 590, yg, w=2, color=RED)
    f.text(420, 130, "telpas vilnis", anchor="start", size=12, color=RED, bold=True)
    # zonas
    yb = yg + 26
    for a, b, lab, fill in ((xt, 232, "dzirdams", None), (232, 588, "MIRUSĪ ZONA", "#ececec"), (588, 748, "dzirdams", None)):
        if fill:
            f.rect(a, yb - 8, b - a, 30, fill=fill, rx=0, sw=0.8)
        f.pl([(a, yb - 8), (a, yb + 22)], w=1); f.pl([(b, yb - 8), (b, yb + 22)], w=1)
        f.text((a + b) / 2, yb + 12, lab, size=12, bold=bool(fill))
    f.text(410, yb + 46, "signāls nav dzirdams: zemes vilnis jau izdzisis, telpas vilnis vēl nav nolaidies", size=11, italic=True)
    f.save("atteli/14-4-mirusi-zona.svg", "Mirusī zona")


def f14_4():
    f = Fig(780, 340)
    yg = 260
    f.rect(30, 40, 720, 28, fill=BLUE_T, rx=0, sw=0.6, color=BLUE)
    f.text(700, 59, "F slānis", size=12, bold=True, color=BLUE)
    _groundline(f, 30, 750, yg)
    xc = 300
    # zems dipols
    for xm in (xc - 50, xc + 50):
        f.line(xm, yg, xm, yg - 22, w=2.4)
    f.line(xc - 50, yg - 22, xc + 50, yg - 22, w=2.4)
    f.circ(xc, yg - 22, 4)
    f.text(xc - 60, yg - 6, "zems dipols", anchor="end", size=11, italic=True)
    src = (xc, yg - 22)
    for xu, xd in ((xc - 55, xc - 170), (xc - 100, xc - 250), (xc + 55, xc + 170), (xc + 100, xc + 250)):
        f.line(src[0], src[1], xu, 68, w=1.7, color=RED)
        f.arrow(xu, 68, xd, yg, w=1.7, color=RED)
    # zema leņķa stars salīdzinājumam
    f.arrow(src[0], src[1], 740, 150, dash="6 4", w=1.6, color=BLUE)
    f.text(742, 204, "zema leņķa stars:", anchor="end", size=11, italic=True)
    f.text(742, 218, "tālie sakari", anchor="end", size=11, italic=True)
    yb = yg + 24
    a, b = xc - 250, xc + 250
    f.pl([(a, yb - 6), (a, yb), (b, yb), (b, yb - 6)], w=1.2)
    f.text(xc, yb + 20, "nosegtais apgabals ap raidītāju, bez mirušās zonas", size=12)
    f.text(xc, yb + 38, "līdz dažiem simtiem kilometru", size=11, italic=True)
    f.save("atteli/14-6-nvis.svg", "NVIS izplatīšanās")


def f15_1():
    f = Fig(640, 260)
    x1, x2, y1, y2 = 90, 360, 60, 210
    # kreisā puse ar bateriju
    f.line(x1, y1, x1, 130); f.line(x1, 140, x1, y2)
    f.battery(x1, 135)
    # augša ar ampērmetru
    f.line(x1, y1, 195, y1); f.line(225, y1, x2, y1)
    f.meter(210, y1, "A")
    # labā puse ar rezistoru
    f.line(x2, y1, x2, 113); f.line(x2, 157, x2, y2)
    f.resistor(x2, 135, horizontal=False)
    f.text(x2 - 16, 140, "R", anchor="end", italic=True, size=14)
    f.line(x1, y2, x2, y2)
    # voltmetrs paralēli
    xv = 470
    f.line(x2, y1, xv, y1); f.line(xv, y1, xv, 120)
    f.line(xv, 150, xv, y2); f.line(xv, y2, x2, y2)
    f.meter(xv, 135, "V")
    f.circ(x2, y1, 3, fill=K); f.circ(x2, y2, 3, fill=K)
    f.text(210, y1 - 24, "ampērmetrs — virknē", size=12)
    f.text(xv + 24, 132, "voltmetrs —", anchor="start", size=12)
    f.text(xv + 24, 148, "paralēli", anchor="start", size=12)
    f.arrow(120, y1 + 16, 170, y1 + 16, w=1.2); f.text(145, y1 + 34, "I", italic=True)
    f.save("atteli/15-1-voltmetrs-ampermetrs.svg", "Voltmetra un ampērmetra pieslēgšana")


def f15_2():
    f = Fig(760, 190)
    y = 100
    pos = chain(f, ["Transīvers", "SWR un jaudas\nmērītājs"], 40, y, gap=150, bh=56, size=13, minw=120)
    xe = pos[-1][2]
    xa = xe + 190
    f.line(xe, y, xa, y, w=2.2)
    f.line(pos[0][2], y, pos[1][1], y, w=2.2)
    f.antenna(xa, y, h=60)
    f.text(xa, y + 22, "antena", size=12, italic=True)
    xm = (xe + xa) / 2
    f.arrow(xe + 30, y - 22, xa - 40, y - 22, w=2, color=RED)
    f.text(xm, y - 32, "tiešā jauda", size=12, color=RED, bold=True)
    f.arrow(xa - 40, y + 22, xe + 30, y + 22, w=1.8, dash="6 4", color=AMBER)
    f.text(xm, y + 42, "atstarotā jauda", size=12, color=AMBER, bold=True)
    f.text((pos[0][2] + pos[1][1]) / 2, y - 12, "koaksiālais kabelis", size=11, italic=True)
    f.save("atteli/15-2-swr-meritajs.svg", "SWR mērītāja pieslēgšana")


def _grid(f, x, y, w, h, nx=8, ny=6):
    f.rect(x, y, w, h, fill="white", rx=6, sw=2)
    for i in range(1, nx):
        f.line(x + w * i / nx, y, x + w * i / nx, y + h, w=0.5, color=G)
    for j in range(1, ny):
        f.line(x, y + h * j / ny, x + w, y + h * j / ny, w=0.5, color=G)


def f15_3():
    f = Fig(760, 300)
    f.text(190, 24, "Osciloskops", bold=True, size=14)
    x, y, w, h = 50, 44, 280, 190
    _grid(f, x, y, w, h)
    f.sine(x, y + h / 2, w, 62, 2.5, w=2.4, color=GREEN)
    f.text(190, y + h + 22, "laiks →", size=12, italic=True)
    f.text(190, y + h + 44, "rāda signāla formu: amplitūdu un periodu", size=11)
    f.text(x - 10, y + h / 2 + 4, "U", anchor="end", size=12, italic=True)
    f.text(570, 24, "Spektra analizators", bold=True, size=14)
    x = 430
    _grid(f, x, y, w, h)
    yb = y + h - 8
    for k, hh, lab in ((1, 160, "f"), (2, 70, "2f"), (3, 40, "3f"), (4, 18, "4f")):
        xx = x + w * k / 5
        f.line(xx, yb, xx, yb - hh, w=4, color=(GREEN if k == 1 else RED))
        f.text(xx, yb - hh - 6, lab, size=11, italic=True)
    f.line(x + 6, yb, x + w - 6, yb, w=1, color=MG)
    f.text(570, y + h + 22, "frekvence →", size=12, italic=True)
    f.text(570, y + h + 44, "rāda sastāvu: pamatfrekvenci un harmonikas", size=11)
    f.text(x - 10, y + h / 2 + 4, "dB", anchor="end", size=12, italic=True)
    f.line(380, 40, 380, 280, dash="3 5", w=1, color=MG)
    f.save("atteli/15-4-osciloskops-spektra-analizators.svg", "Osciloskops un spektra analizators")


def _house(f, x1, x2, yb, yw, apex):
    f.pl([(x1, yb), (x1, yw), ((x1 + x2) / 2, apex), (x2, yw), (x2, yb)], close=True, fill="white", w=2)


def _num(f, x, y, n):
    f.circ(x, y, 10, fill="white", sw=1.4)
    f.text(x, y + 4.5, str(n), size=12, bold=True)


def _qarrow(f, p0, c, p1, color, w=2.0, dash=None, n=40):
    """Līkta bultiņa (kvadrātiskā Bezjē līkne) ar smaili galā."""
    pts = [((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * c[0] + t * t * p1[0],
            (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * c[1] + t * t * p1[1])
           for t in (i / n for i in range(n + 1))]
    f.pl(pts[:-3], w=w, color=color, dash=dash)
    f.arrow(pts[-4][0], pts[-4][1], pts[-1][0], pts[-1][1], w=w, color=color)


def _noise(f, x, y, ang=0.0, n=3, color=None):
    """Trokšņa zīme: īsas zigzaga līnijas, kas izplatās virzienā ang (grādi, 0 — pa labi)."""
    color = color or AMBER
    a = math.radians(ang)
    for k in range(n):
        da = math.radians((k - (n - 1) / 2) * 32)
        ux, uy = math.cos(a + da), -math.sin(a + da)
        px, py = -uy, ux
        pts = []
        for i in range(7):
            r = 8 + i * 3.2
            off = (3 if i % 2 else -3)
            pts.append((x + ux * r + px * off, y + uy * r + py * off))
        f.pl(pts, w=1.3, color=color)


def f16_1():
    f = Fig(1010, 500)
    yb = 322
    _groundline(f, 20, 885, yb)
    # --- radioamatiera māja ---
    _house(f, 40, 300, yb, 200, 140)
    f.text(170, yb + 20, "radioamatiera māja", size=12, italic=True)
    f.box(130, 278, 120, 42, "Transīvers", size=12)
    f.box(250, 292, 76, 30, "Lādētājs", size=11)
    _noise(f, 226, 278, ang=135, color=AMBER)
    xa = 272
    f.line(xa, 176, xa, 60, w=2.4)
    f.line(xa - 62, 60, xa + 62, 60, w=2.4)
    f.text(xa - 62, 50, "antena", anchor="start", size=11, italic=True)
    f.pl([(130, 257), (130, 236), (xa, 236), (xa, 176)], w=1.6)          # koaksiālais kabelis
    # --- kaimiņa māja ---
    _house(f, 540, 820, yb, 200, 140)
    f.text(680, yb + 20, "kaimiņa māja", size=12, italic=True)
    # saules paneļi uz labās jumta slīpnes
    for i in range(3):
        x0 = 694 + i * 40
        y0 = 140 + (x0 - 680) * 60 / 140
        x1 = x0 + 36
        y1 = 140 + (x1 - 680) * 60 / 140
        f.pl([(x0, y0 - 6), (x1, y1 - 6), (x1, y1 - 22), (x0, y0 - 22)], close=True,
             fill=BLUE_T, color=BLUE, w=1.3)
    f.text(790, 124, "saules paneļi", size=11, italic=True)
    f.pl([(790, 186), (790, 224)], w=1.2)                     # paneļu vads uz invertoru
    f.box(772, 236, 72, 24, "Invertors", size=11)
    _noise(f, 740, 236, ang=170, n=2)
    # ziemassvētku lampiņas gar jumta kreiso slīpni
    lc = [RED, GREEN, AMBER, BLUE]
    xs_l = [552 + i * 13 for i in range(9)]
    pts = [(x, 200 - (x - 540) * 60 / 140 + 4 + (4 if i % 2 else 0)) for i, x in enumerate(xs_l)]
    f.pl(pts, w=0.9)
    for i, (x, y) in enumerate(pts):
        f.circ(x, y + 3, 3.4, fill=lc[i % 4], color=lc[i % 4], sw=0.8)
    f.mtext(428, 252, "mirgojošas\nlampiņas", size=10, italic=True)
    f.line(456, 242, 546, 200, w=0.8, color=MG)
    _noise(f, 548, 186, ang=140, n=2)
    # TV antena
    xt = 588
    f.line(xt, 180, xt, 96, w=2)
    for i, hw in enumerate((16, 13, 10)):
        f.line(xt - hw, 100 + i * 9, xt + hw, 100 + i * 9, w=1.6)
    f.line(xt, 180, xt, 266)
    f.box(588, 284, 76, 36, "TV, radio", size=11)
    f.box(670, 284, 70, 36, "Skaļruņi", size=11)
    f.path("M 626 284 C 636 270, 642 298, 635 284", w=1.2)
    f.box(768, 284, 76, 36, "Barošanas\nbloks", size=10)
    _noise(f, 732, 272, ang=150, n=2)
    # LED lampa
    f.line(682, 200, 682, 218, w=1.2)
    f.circ(682, 226, 8, fill=AMBER_T, color=K, sw=1.2)
    f.text(698, 230, "LED", anchor="start", size=10)
    _noise(f, 676, 220, ang=150, n=2)
    # kondicionieris / siltumsūknis ārā
    f.rect(832, 274, 50, 46, rx=3, fill="white")
    f.circ(857, 297, 15, fill="white", sw=1.3)
    for k in range(3):
        aa = k * 2 * math.pi / 3
        f.line(857, 297, 857 + 12 * math.cos(aa), 297 + 12 * math.sin(aa), w=1.2)
    f.mtext(857, 344, "kondicionieris,\nsiltumsūknis", size=10, italic=True)
    _noise(f, 857, 270, ang=100)
    # dzirksteļojoša elektrolīnija
    xp = 950
    f.line(xp, yb, xp, 92, w=3)
    f.line(xp - 26, 104, xp + 26, 104, w=2.4)
    for dx in (-20, 20):
        f.rect(xp + dx - 3, 92, 6, 12, fill="white", sw=1.2)
    f.path(f"M {xp - 20} 92 Q 900 120 822 196", w=1.4)          # pievads mājai
    f.line(xp + 20, 92, 1005, 86, w=1.4)
    # dzirkstele pie izolatora
    f.pl([(xp - 26, 86), (xp - 32, 78), (xp - 25, 76), (xp - 34, 64)], w=1.8, color=AMBER)
    f.pl([(xp - 14, 86), (xp - 8, 76), (xp - 15, 74), (xp - 6, 62)], w=1.8, color=AMBER)
    _noise(f, xp - 20, 70, ang=150)
    f.mtext(xp, 344, "dzirksteļojoša\nelektrolīnija", size=10, italic=True)
    # --- elektrotīkls ---
    f.pl([(100, 299), (100, 380), (768, 380), (768, 302)], w=1.6, dash="2 4")
    f.text(225, 395, "elektrotīkls", size=11, italic=True)
    # --- ceļi: sarkans — raidītāja signāls, dzintara — troksnis ---
    f.arrow(338, 62, xt - 22, 98, w=2.2, color=RED)                                  # 1 →
    _qarrow(f, (918, 58), (640, 2), (342, 50), AMBER, w=2.2)                         # 1 ←
    f.arrow(336, 68, 664, 264, w=1.8, color=RED, dash="7 4")                          # 3 →
    f.arrow(336, 66, 588, 264, w=1.8, color=RED, dash="2 4")                          # 4 →
    f.arrow(350, 372, 520, 372, w=2.2, color=RED)                                     # 2 →
    f.arrow(520, 388, 350, 388, w=2.2, color=AMBER)                                   # 2 ←
    f.arrow(272, 277, 272, 244, w=1.8, color=AMBER, dash="7 4")                       # 3 ← (kabeļa apvalks)
    _num(f, 470, 66, 1)
    _num(f, 435, 380, 2)
    _num(f, 520, 205, 3)
    _num(f, 292, 258, 3)
    _num(f, 465, 172, 4)
    # --- leģenda ---
    f.line(60, 428, 96, 428, w=2.4, color=RED)
    f.text(104, 432, "raidītāja signāls traucē sadzīves ierīcēm", anchor="start", size=12)
    f.line(480, 428, 516, 428, w=2.4, color=AMBER)
    f.text(524, 432, "elektroierīču un elektrolīniju troksnis traucē uztvērējam", anchor="start", size=12)
    leg = ["1 — pa gaisu, caur antenām", "2 — pa elektrotīkla vadiem",
           "3 — pa pieslēgtajiem vadiem un kabeļa apvalku", "4 — tieši caur ierīces korpusu"]
    for i, t in enumerate(leg):
        f.text(60 + (i % 2) * 420, 460 + (i // 2) * 20, t, anchor="start", size=12)
    f.save("atteli/16-1-traucejumu-celi.svg",
           "Traucējumi abos virzienos: raidītājs — sadzīves ierīcēm, sadzīves elektronika — uztvērējam")


def f17_1():
    f = Fig(800, 320)
    labs = ["Transīvers", "Barošanas\nbloks", "Antenu\nskaņotājs"]
    # pareizi
    f.text(210, 24, "✓ Pareizi: katrai iekārtai savs vads", bold=True, size=13, color=GREEN)
    xs = [80, 210, 340]
    for x, l in zip(xs, labs):
        f.box(x, 80, 104, 48, l, size=12)
        f.line(x, 104, x, 176, w=2.4, color=GREEN)
    f.rect(40, 176, 340, 12, fill="#c47a3a", rx=2, color="#7a4316")
    f.text(210, 208, "zemējuma kopne", size=12, italic=True)
    f.line(120, 188, 120, 236, w=2)
    f.ground(120, 236, stem=12)
    f.text(140, 262, "zemētājs, ne vairāk kā 4 Ω", anchor="start", size=12)
    # nepareizi
    f.text(610, 24, "✗ Nepareizi: virknē, viena caur otru", bold=True, size=13, color=RED)
    xs = [490, 610, 730]
    for x, l in zip(xs, labs):
        f.box(x, 80, 100, 48, l, size=12)
    for i in range(2):
        f.path(f"M {xs[i]} 104 C {xs[i]} 140, {xs[i + 1]} 140, {xs[i + 1]} 104", w=2)
    f.line(730, 104, 730, 190, w=2)
    f.ground(730, 190, stem=12)
    # krusts
    f.line(470, 130, 770, 250, w=5, color=RED); f.line(770, 130, 470, 250, w=5, color=RED)
    f.line(430, 40, 430, 290, dash="3 5", w=1, color=MG)
    f.save("atteli/17-2-stacijas-zemejums.svg", "Stacijas zemējums")


def _loc(lat, lon):
    """Maidenhead lokators (6 zīmes) pēc platuma un garuma grādos."""
    lo, la = lon + 180, lat + 90
    fl, fa = int(lo // 20), int(la // 10)
    sl, sa = int(lo % 20 // 2), int(la % 10 // 1)
    ul, ua = int(lo % 2 / (2 / 24)), int(la % 1 / (1 / 24))
    return ("ABCDEFGHIJKLMNOPQR"[fl] + "ABCDEFGHIJKLMNOPQR"[fa] + str(sl) + str(sa)
            + "abcdefghijklmnopqrstuvwx"[ul] + "abcdefghijklmnopqrstuvwx"[ua])


# Vienkāršota Baltijas reģiona krasta līnija lauka KO kartei (garums, platums); pašu uzzīmēta.
_KO_LAND = [(20, 50), (20, 54.4), (20.6, 54.95), (21.1, 55.25), (21.05, 55.7), (21.0, 56.5), (21.1, 57.0),
            (21.55, 57.4), (22.0, 57.7), (22.6, 57.75), (22.8, 57.5), (23.2, 57.2), (23.8, 56.97), (24.1, 57.0),
            (24.4, 57.25), (24.35, 57.75), (24.4, 57.87), (24.5, 58.38), (23.85, 58.35), (23.5, 58.7),
            (23.5, 58.95), (23.7, 59.3), (24.5, 59.45), (26, 59.55), (28, 59.45), (29, 59.9), (30.2, 59.9),
            (30.3, 60), (40, 60), (40, 50)]
_KO_SAARE = [(21.9, 58.3), (22.4, 58.6), (23.1, 58.6), (23.3, 58.35), (22.6, 58.1)]
# Daugava kvadrātā KO26 (garums, platums)
_DAUGAVA = [(26, 56.45), (25.7, 56.62), (25.4, 56.64), (24.9, 56.7), (24.6, 56.8), (24.35, 56.87),
            (24.12, 56.97), (24.07, 57.03)]


def f05_1():
    assert _loc(56.95, 24.1) == "KO26bw"  # Rīga
    f = Fig(760, 276)
    y, h = 62, 120
    # 1. lauks: 20° x 10°, 10 x 10 kvadrāti
    x, w = 15, 240
    f.text(x + w / 2, 28, "1. Lauks: KO", bold=True, size=14)
    f.rect(x, y, w, h, rx=0, sw=2)
    f.add(f'<clipPath id="k1"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath><g clip-path="url(#k1)">')
    for poly in (_KO_LAND, _KO_SAARE):
        f.pl([(x + (a - 20) * 12, y + (60 - b) * 12) for a, b in poly], close=True, fill=LG, w=0.9, color=MG)
    f.add("</g>")
    rx_, ry_ = x + (24.1 - 20) * 12, y + (60 - 56.95) * 12
    f.circ(rx_, ry_, 2.2, fill=K, sw=1)
    f.text(rx_ - 5, ry_ - 4, "Rīga", anchor="end", size=10.5)
    for i in range(1, 10):
        f.line(x + w * i / 10, y, x + w * i / 10, y + h, w=0.5, color=MG)
        f.line(x, y + h * i / 10, x + w, y + h * i / 10, w=0.5, color=MG)
    f.rect(x + w * 0.2, y + h * 0.3, w / 10, h / 10, fill="none", rx=0, sw=2.4)
    f.text(x + w * 0.25, y + h * 0.3 + 7, "26", size=10.5, bold=True)
    f.text(x + w / 2, y + h + 32, "20° × 10° = 10 × 10 kvadrāti", size=11)
    f.text(x + w / 2, y + h + 50, "garums 0 → 9 (uz austrumiem)", size=11, italic=True)
    f.text(x + w / 2, y + h + 65, "platums 0 → 9 (uz ziemeļiem)", size=11, italic=True)
    for i in range(10):
        f.text(x + w * (i + 0.5) / 10, y + h + 12, str(i), size=10.5, bold=(i == 2))
        f.text(x - 4, y + h * (9.5 - i) / 10 + 3, str(i), anchor="end", size=10.5, bold=(i == 6))
    # 2. kvadrāts: 2° x 1°, 24 x 24 apakškvadrāti
    x2 = 305
    f.text(x2 + w / 2, 28, "2. Kvadrāts: 26", bold=True, size=14)
    f.rect(x2, y, w, h, fill=LG, rx=0, sw=2)
    f.add(f'<clipPath id="k2"><rect x="{x2}" y="{y}" width="{w}" height="{h}"/></clipPath><g clip-path="url(#k2)">')
    f.pl([(x2 + (a - 24) * 120, y + (57 - b) * 120) for a, b in _DAUGAVA], w=2.4, color=MG)
    f.add("</g>")
    for nm, lo, la in (("Ogre", 24.6, 56.82), ("Koknese", 25.43, 56.64)):
        f.circ(x2 + (lo - 24) * 120, y + (57 - la) * 120, 2, fill=K, sw=1)
        f.text(x2 + (lo - 24) * 120 + 4, y + (57 - la) * 120 - 4, nm, anchor="start", size=10.5)
    f.text(x2 + w - 5, y + 12, "Rīgas līcis (jūra) ↑", anchor="end", size=10.5, italic=True)
    f.text(x2 + w - 5, y + h - 6, "Daugava", anchor="end", size=10.5, italic=True)
    f.circ(x2 + 0.1 * 120, y + (57 - 56.95) * 120, 2.2, fill=K, sw=1)
    f.text(x2 + 0.1 * 120 + 14, y + (57 - 56.95) * 120 + 4, "Rīga", anchor="start", size=10.5)
    for i in range(1, 24):
        f.line(x2 + w * i / 24, y, x2 + w * i / 24, y + h, w=0.4, color=G)
        f.line(x2, y + h * i / 24, x2 + w, y + h * i / 24, w=0.4, color=G)
    cw, ch = w / 24, h / 24
    f.rect(x2 + cw, y + ch, cw, ch, fill="none", rx=0, sw=2.2)
    f.line(x2 + 1.5 * cw, y + 2 * ch + 2, x2 + 1.5 * cw, y + 26, w=1)
    f.text(x2 + 1.5 * cw, y + 38, "bw", size=11, bold=True)
    f.text(x2 + w / 2, y + h + 32, "2° × 1° = 24 × 24 apakškvadrāti", size=11)
    f.text(x2 + w / 2, y + h + 50, "garums a → x (uz austrumiem)", size=11, italic=True)
    f.text(x2 + w / 2, y + h + 65, "platums a → x (uz ziemeļiem)", size=11, italic=True)
    for i, c in enumerate("abcdefghijklmnopqrstuvwx"):
        f.text(x2 + w * (i + 0.5) / 24, y + h + 12, c, size=9.5, bold=(c == "b"))
        if i % 2 == 0:
            f.text(x2 - 4, y + h * (23.5 - i) / 24 + 3, c, anchor="end", size=9.5, bold=(c == "w"))
    # savienojumi
    f.arrow(x + w * 0.3, y + h * 0.5, x2 - 15, y + h * 0.5, dash="4 3")
    f.arrow(x2 + w + 4, y + h / 2, 568, y + h / 2)
    # 3. rezultāts
    f.text(668, 28, "3. Apakškvadrāts: bw", bold=True, size=14)
    f.text(668, y + 50, "KO26bw", size=28, bold=True)
    f.text(668, y + 74, "(Rīga)", size=12, italic=True)
    for k, t in enumerate(("KO — lauks, 20° × 10°", "26 — kvadrāts, 2° × 1°", "bw — apakškvadrāts, 5′ × 2,5′")):
        f.text(575, y + h + 20 + 17 * k, t, anchor="start", size=10.5)
    f.save("atteli/05-2-lokatora-veidosanas.svg", "Lokatora veidošanās: lauks, kvadrāts, apakškvadrāts")


# Vienkāršotas kontinentu kontūras (garums, platums), uzzīmētas pašu spēkiem šai grāmatai;
# neviens ārējs datu kopums vai karte nav izmantota.
_LAND = [
    [(-168, 66), (-156, 71), (-141, 70), (-125, 70), (-110, 68), (-95, 72), (-85, 69), (-82, 63), (-93, 59),
     (-82, 55), (-78, 52), (-78, 60), (-70, 59), (-62, 57), (-56, 52), (-60, 47), (-66, 44), (-70, 42),
     (-75, 38), (-81, 31), (-80, 26), (-83, 29), (-89, 30), (-97, 27), (-97, 22), (-91, 19), (-87, 21),
     (-88, 16), (-83, 15), (-83, 10), (-78, 8), (-80, 7), (-85, 10), (-92, 14), (-97, 16), (-105, 20),
     (-110, 24), (-112, 29), (-115, 30), (-117, 33), (-121, 35), (-124, 40), (-124, 48), (-130, 54),
     (-138, 59), (-150, 60), (-158, 57), (-165, 60)],
    [(-55, 60), (-45, 60), (-20, 70), (-20, 80), (-40, 83), (-65, 80), (-72, 77), (-55, 70)],
    [(-78, 8), (-72, 12), (-62, 10), (-52, 5), (-50, 0), (-40, -3), (-35, -6), (-39, -15), (-41, -22),
     (-48, -26), (-53, -34), (-58, -38), (-65, -41), (-66, -47), (-69, -52), (-72, -54), (-75, -48),
     (-73, -38), (-71, -30), (-70, -18), (-76, -14), (-81, -6), (-80, 0), (-78, 3)],
    [(-9, 37), (-9, 43), (-1, 44), (-4, 48), (2, 51), (8, 54), (9, 57), (14, 54), (21, 55), (24, 58),
     (30, 60), (30, 66), (35, 66), (45, 68), (60, 69), (70, 73), (80, 73), (100, 77), (115, 74),
     (140, 72), (160, 70), (180, 69), (180, 65), (170, 60), (162, 58), (156, 51), (150, 59), (140, 55),
     (135, 43), (130, 42), (127, 39), (129, 35), (126, 35), (122, 40), (121, 31), (120, 23), (108, 21),
     (106, 10), (100, 13), (103, 2), (98, 8), (98, 16), (92, 22), (86, 20), (80, 15), (77, 8), (73, 17),
     (68, 24), (57, 25), (57, 27), (50, 30), (48, 29), (52, 24), (56, 26), (59, 22), (52, 16), (43, 13),
     (39, 22), (35, 28), (34, 31), (36, 36), (28, 37), (26, 40), (23, 40), (20, 40), (16, 38), (12, 42),
     (8, 44), (3, 43), (-1, 37)],
    [(5, 58), (5, 62), (15, 69), (25, 71), (30, 70), (28, 66), (25, 65), (22, 63), (17, 60), (18, 59),
     (12, 56), (8, 58)],
    [(-17, 21), (-10, 30), (-6, 36), (10, 37), (11, 33), (20, 31), (32, 31), (34, 28), (38, 19), (43, 12),
     (51, 12), (41, -2), (40, -15), (35, -24), (32, -29), (27, -34), (20, -35), (17, -30), (12, -17),
     (13, -6), (9, 3), (5, 5), (-8, 4), (-13, 8), (-17, 14)],
    [(114, -22), (122, -18), (130, -12), (137, -12), (142, -11), (146, -19), (153, -26), (150, -37),
     (141, -38), (135, -35), (130, -32), (115, -34), (113, -26)],
    [(-5, 50), (1, 51), (0, 54), (-2, 57), (-5, 58), (-6, 55), (-3, 54)],
    [(-24, 64), (-14, 64), (-14, 66), (-23, 66)],
    [(130, 31), (135, 34), (141, 38), (142, 43), (140, 41), (133, 35)],
    [(44, -25), (47, -25), (50, -15), (49, -12), (44, -17)],
]


def f05_2():
    f = Fig(760, 430)
    s, x0, y0 = 1.95, 42, 52
    mx = lambda lon: x0 + (lon + 180) * s
    my = lambda lat: y0 + (90 - lat) * s
    f.text(380, 24, "Pasaules karte, sadalīta 18 × 18 laukos (shematiska)", bold=True, size=14)
    f.rect(x0, y0, 360 * s, 180 * s, rx=0, sw=2)
    for poly in _LAND:
        f.pl([(mx(a), my(b)) for a, b in poly], close=True, fill=LG, w=0.9, color=MG)
    for i in range(1, 18):
        f.line(x0 + 20 * s * i, y0, x0 + 20 * s * i, y0 + 180 * s, w=0.6, color=MG)
        f.line(x0, y0 + 10 * s * i, x0 + 360 * s, y0 + 10 * s * i, w=0.6, color=MG)
    for i, c in enumerate("ABCDEFGHIJKLMNOPQR"):
        f.text(x0 + 20 * s * (i + 0.5), y0 - 8, c, size=11, bold=(c == "K"))
        f.text(x0 - 8, y0 + 180 * s - 10 * s * (i + 0.5) + 4, c, anchor="end", size=11, bold=(c == "O"))
    # lauks KO: 20°–40° E, 50°–60° N
    f.rect(mx(20), my(60), 20 * s, 10 * s, fill="none", rx=0, sw=3)
    f.circ(mx(24.1), my(56.95), 3, fill=K, sw=1)
    bx, by = mx(-58), my(40)
    f.rect(bx, by, 92, 34, fill="white", rx=4, sw=1.6)
    f.text(bx + 46, by + 15, "KO", bold=True, size=14)
    f.text(bx + 46, by + 28, "Latvija, Rīga", size=10)
    f.arrow(bx + 92, by + 12, mx(20) - 3, my(50) - 4, w=1.2)
    f.text(380, y0 + 180 * s + 26, "Pirmais burts — garums no 180° W (A) uz austrumiem, otrais — platums no 90° S (A) uz ziemeļiem.",
           size=11, italic=True)
    f.text(380, y0 + 180 * s + 44, "Katrs lauks ir 20° plats un 10° augsts.", size=11, italic=True)
    f.save("atteli/05-1-lokatoru-karte.svg", "Pasaules karte ar lokatora laukiem")


ALL = [f05_1, f05_2, f14_1, f14_2, f14_3, f14_4, f15_1, f15_2, f15_3, f16_1, f17_1]
