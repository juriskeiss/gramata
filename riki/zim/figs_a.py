"""7.–10. nodaļas zīmējumi."""
import math
from lib import Fig, K, G, LG, MG, chain, tw


def f07_1():
    f = Fig(720, 250)
    # elektriskā ķēde
    f.text(170, 22, "Elektriskā ķēde", bold=True, size=14)
    x1, x2, y1, y2 = 70, 270, 60, 200
    f.line(x1, y1, x2, y1); f.line(x1, y2, x2, y2)
    f.line(x1, y1, x1, 125); f.line(x1, 135, x1, y2)
    f.battery(x1, 130)
    f.line(x2, y1, x2, 108); f.line(x2, 152, x2, y2)
    f.resistor(x2, 130, horizontal=False)
    f.text(x2 + 16, 135, "R", anchor="start", italic=True, size=14)
    f.text(x1 + 22, 135, "U", anchor="start", italic=True, size=14)
    f.arrow(140, y1 - 12, 200, y1 - 12, w=1.3)
    f.text(170, y1 - 20, "I", italic=True, size=14)
    f.text(170, 232, "spriegums U dzen strāvu I caur pretestību R", size=12)
    # ūdens analoģija
    f.text(540, 22, "Ūdens salīdzinājums", bold=True, size=14)
    a1, a2 = 440, 640
    f.line(a1, y1, a2, y1, w=11, color=G); f.line(a1, y2, a2, y2, w=11, color=G)
    f.line(a1, y1, a1, y2, w=11, color=G)
    f.line(a2, y1, a2, 105, w=11, color=G); f.line(a2, 155, a2, y2, w=11, color=G)
    f.line(a2, 105, a2, 155, w=4, color=MG)
    f.circ(a1, 130, 20)
    f.text(a1, 135, "S", bold=True, size=14)
    f.text(a1 - 28, 135, "sūknis", anchor="end", size=12)
    f.text(a2 + 14, 127, "sašauri-", anchor="start", size=12)
    f.text(a2 + 14, 142, "nājums", anchor="start", size=12)
    f.arrow(510, y1 - 14, 570, y1 - 14, w=1.3)
    f.text(540, y1 - 22, "plūsma", size=12)
    f.text(540, 232, "spiediens dzen plūsmu caur sašaurinājumu", size=12)
    f.line(360, 40, 360, 215, dash="3 5", w=1, color=MG)
    f.save("atteli/07-1-kede-un-udens.svg", "Elektriskā ķēde un ūdens salīdzinājums")


def f07_2():
    f = Fig(520, 220)
    ax, ay, bx, by, cx, cy = 130, 30, 30, 190, 230, 190
    f.pl([(ax, ay), (bx, by), (cx, cy)], close=True, fill="white", w=2)
    my = 118
    lx = bx + (ax - bx) * (by - my) / (by - ay)
    rx = cx - (cx - ax) * (cy - my) / (cy - ay)
    f.line(lx, my, rx, my); f.line(130, my, 130, by)
    f.text(130, 96, "U", size=30, bold=True)
    f.text(92, 170, "I", size=30, bold=True)
    f.text(168, 170, "R", size=30, bold=True)
    f.text(300, 70, "U = I · R", anchor="start", size=17)
    f.text(300, 118, "I = U / R", anchor="start", size=17)
    f.text(300, 166, "R = U / I", anchor="start", size=17)
    f.text(300, 200, "aizklāj meklēto lielumu", anchor="start", size=11, italic=True)
    f.save("atteli/07-2-oma-trijsturis.svg", "Oma likuma trijstūris")


def f07_3():
    f = Fig(740, 290)
    # līdzstrāva
    f.text(150, 22, "Līdzspriegums", bold=True, size=14)
    f.axes(50, 150, 220, 100, xl="t", yl="U", neg=80)
    f.line(50, 95, 250, 95, w=2.2)
    f.text(255, 90, "U", anchor="start", italic=True)
    # maiņstrāva
    f.text(530, 22, "Maiņspriegums", bold=True, size=14)
    x0, y0, W, A = 370, 150, 300, 80
    f.axes(x0, y0, W + 40, 110, xl="t", yl="u", neg=95)
    f.sine(x0, y0, W, A, 2, w=2.2)
    # Umax
    xp = x0 + W / 8
    f.darrow(xp, y0, xp, y0 - A)
    f.ltext(xp + 8, y0 - 10, "Umax", anchor="start", size=12, italic=True)
    # URMS
    yr = y0 - 0.707 * A
    f.line(x0, yr, x0 + W, yr, dash="5 4", w=1.1)
    f.text(x0 + W + 4, yr + 4, "URMS", anchor="start", size=12, italic=True)
    # Up-p
    xq = x0 + W * 5 / 8 + 36
    f.line(x0 + W * 5 / 8, y0 - A, xq + 6, y0 - A, w=0.8, dash="2 3")
    f.line(x0 + W * 7 / 8, y0 + A, xq - 30, y0 + A, w=0.8, dash="2 3")
    xs = x0 + W * 6 / 8
    f.darrow(xs, y0 - A, xs, y0 + A)
    f.ltext(xs + 8, y0 + 40, "Up-p", anchor="start", size=12, italic=True)
    # periods
    yt = y0 + A + 22
    f.darrow(x0 + W / 8, yt, x0 + W * 5 / 8, yt)
    f.text(x0 + W * 3 / 8, yt + 16, "T (periods)", size=12, italic=True)
    f.line(x0 + W / 8, y0 - A, x0 + W / 8, yt, w=0.7, dash="2 3")
    f.line(x0 + W * 5 / 8, y0 - A, x0 + W * 5 / 8, yt, w=0.7, dash="2 3")
    f.save("atteli/07-3-lidzstrava-mainstrava.svg", "Līdzspriegums un maiņspriegums")


def f08_1():
    f = Fig(720, 260)
    x0, y0, W = 70, 130, 520
    f.arrow(x0 - 20, y0, x0 + W + 50, y0, w=1.3)
    f.text(700, y0 + 96, "izplatīšanās", anchor="end", size=12, italic=True)
    f.text(700, y0 + 111, "virziens", anchor="end", size=12, italic=True)
    n = 240
    A = 70
    # B lauks (slīpā projekcijā), zīmē vispirms
    pts = []
    for i in range(n + 1):
        t = i / n
        v = math.sin(2 * math.pi * 2 * t)
        pts.append((x0 + W * t - 0.62 * A * v, y0 + 0.42 * A * v))
    f.pl(pts, w=1.6, color=MG)
    for k in range(1, 16):
        t = k / 16
        v = math.sin(2 * math.pi * 2 * t)
        if abs(v) > 0.3:
            f.line(x0 + W * t, y0, x0 + W * t - 0.62 * A * v, y0 + 0.42 * A * v, w=0.8, color=MG)
    # E lauks
    f.sine(x0, y0, W, A, 2, w=2.2)
    for k in range(1, 16):
        t = k / 16
        v = math.sin(2 * math.pi * 2 * t)
        if abs(v) > 0.3:
            f.line(x0 + W * t, y0, x0 + W * t, y0 - A * v, w=0.8)
    f.text(x0 + W / 8, y0 - A - 10, "E — elektriskais lauks", size=13, bold=True)
    f.text(x0, 244, "B — magnētiskais lauks", anchor="start", size=13, bold=True, color="#555")
    # viļņa garums
    yl = y0 - A - 34
    f.darrow(x0 + W / 8, yl + 6, x0 + W * 5 / 8, yl + 6)
    f.text(x0 + W * 3 / 8, yl, "λ — viļņa garums", size=12, italic=True)
    f.save("atteli/08-1-elektromagnetiskais-vilnis.svg", "Elektromagnētiskais vilnis")


def f08_2():
    f = Fig(720, 430)
    x0, W = 150, 520
    rows = [("Informācijas\nsignāls", 60), ("Nesējs", 160), ("AM", 265), ("FM", 370)]
    for lab, y in rows:
        f.mtext(75, y, lab, size=13, bold=True)
        f.line(x0, y, x0 + W, y, w=0.7, color=MG)
    m = lambda t: math.sin(2 * math.pi * 2 * t)
    f.sine(x0, 60, W, 30, 2, w=2)
    f.sine(x0, 160, W, 32, 26, n=900)
    f.sine(x0, 265, W, 26, 26, n=900, env=lambda t: 1 + 0.7 * m(t))
    # apliecēja
    pts = [(x0 + W * i / 200, 265 - 26 * (1 + 0.7 * m(i / 200))) for i in range(201)]
    f.pl(pts, dash="4 4", w=0.9, color=MG)
    pts = [(x0 + W * i / 200, 265 + 26 * (1 + 0.7 * m(i / 200))) for i in range(201)]
    f.pl(pts, dash="4 4", w=0.9, color=MG)
    f.sine(x0, 370, W, 32, 26, n=1200, fm=lambda t: -9.0 * math.cos(2 * math.pi * 2 * t))
    f.text(x0 + W, 312, "mainās amplitūda", anchor="end", size=11, italic=True)
    f.text(x0 + W, 418, "mainās frekvence, amplitūda nemainīga", anchor="end", size=11, italic=True)
    f.save("atteli/08-2-modulacija.svg", "Amplitūdas un frekvences modulācija")


def f08_3():
    f = Fig(760, 230)
    panels = [("AM", "ap 6 kHz"), ("SSB (USB)", "2,4–3 kHz"), ("CW", "100–500 Hz"), ("FM", "12–16 kHz")]
    pw = 170
    for i, (name, bwid) in enumerate(panels):
        x = 20 + i * 185
        cx = x + pw / 2
        yb = 160
        f.text(cx, 24, name, bold=True, size=14)
        f.arrow(x, yb, x + pw, yb, w=1.2, head=7)
        f.text(x + pw, yb + 15, "f", anchor="end", italic=True, size=12)
        if i == 0:
            f.line(cx, yb, cx, 55, w=3)
            f.pl([(cx - 44, yb), (cx - 44, 125), (cx - 6, 95), (cx - 6, yb)], close=True, fill=G)
            f.pl([(cx + 44, yb), (cx + 44, 125), (cx + 6, 95), (cx + 6, yb)], close=True, fill=G)
            f.text(cx - 26, 90, "LSB", size=10); f.text(cx + 28, 90, "USB", size=10)
            f.text(cx, 48, "nesējs", size=10)
            lo, hi = cx - 44, cx + 44
        elif i == 1:
            f.line(cx - 20, yb, cx - 20, 70, w=1.5, dash="4 4", color=MG)
            f.text(cx - 20, 62, "nomākts nesējs", size=10)
            f.pl([(cx + 24, yb), (cx + 24, 125), (cx - 14, 95), (cx - 14, yb)], close=True, fill=G)
            lo, hi = cx - 14, cx + 24
        elif i == 2:
            f.line(cx, yb, cx, 60, w=4)
            lo, hi = cx - 4, cx + 4
        else:
            for k in range(-7, 8):
                h = 80 * math.exp(-(k / 5.5) ** 4) * (0.55 + 0.45 * abs(math.cos(k * 1.3)))
                f.line(cx + k * 10, yb, cx + k * 10, yb - h, w=3, color="#555")
            lo, hi = cx - 74, cx + 74
        f.darrow(lo, yb + 28, hi, yb + 28) if hi - lo > 30 else f.line(lo, yb + 28, hi, yb + 28, w=1.2)
        f.text(cx, yb + 50, bwid, size=12)
    f.save("atteli/08-3-spektri.svg", "AM, SSB, CW un FM signālu spektri")


def f09_1():
    f = Fig(700, 200)
    f.text(140, 24, "Apzīmējums shēmā", bold=True, size=14)
    f.line(60, 90, 118, 90); f.line(162, 90, 220, 90)
    f.resistor(140, 90, label="R")
    f.text(480, 24, "Rezistors ar krāsu kodu", bold=True, size=14)
    f.line(330, 90, 380, 90, w=2.5, color=MG); f.line(580, 90, 630, 90, w=2.5, color=MG)
    f.rect(380, 66, 200, 48, fill=LG, rx=18)
    bands = [(405, "#444"), (435, "#777"), (465, "#222"), (540, "#aaa")]
    for x, c in bands:
        f.rect(x, 66.8, 14, 46.4, fill=c, rx=0, sw=0.8)
    labs = ["1. cipars", "2. cipars", "nuļļu skaits", "pielaide"]
    xs = [370, 440, 510, 590]
    for (x, c), lab, lx in zip(bands, labs, xs):
        f.line(x + 7, 116, lx, 150, w=0.8)
        f.text(lx, 166, lab, size=12)
    f.save("atteli/09-1-rezistors.svg", "Rezistora apzīmējums un krāsu kods")


def f09_2():
    f = Fig(720, 210)
    f.text(170, 24, "Virknes slēgums", bold=True, size=14)
    y = 100
    f.line(40, y, 88, y); f.resistor(110, y, label="R₁")
    f.line(132, y, 208, y); f.resistor(230, y, label="R₂"); f.line(252, y, 300, y)
    f.arrow(50, y + 26, 100, y + 26, w=1.2); f.text(75, y + 44, "I", italic=True)
    f.arrow(240, y + 26, 290, y + 26, w=1.2); f.text(265, y + 44, "I", italic=True)
    f.text(170, 180, "Rkop = R₁ + R₂", size=13)
    f.text(540, 24, "Paralēlais slēgums", bold=True, size=14)
    xa, xb = 450, 630
    f.line(400, y, xa, y); f.line(xb, y, 680, y)
    for yy, lab in ((y - 34, "R₁"), (y + 34, "R₂")):
        f.line(xa, y, xa, yy); f.line(xb, y, xb, yy)
        f.line(xa, yy, 518, yy); f.line(562, yy, xb, yy)
        f.resistor(540, yy, label=lab, lpos="above" if yy < y else "below")
    f.circ(xa, y, 3, fill=K); f.circ(xb, y, 3, fill=K)
    f.arrow(405, y - 12, 440, y - 12, w=1.2); f.text(420, y - 20, "I", italic=True)
    f.arrow(470, y - 46, 505, y - 46, w=1.2); f.text(486, y - 54, "I₁", italic=True)
    f.arrow(470, y + 22, 505, y + 22, w=1.2); f.text(486, y + 16, "I₂", italic=True)
    f.text(540, 190, "1/Rkop = 1/R₁ + 1/R₂", size=13)
    f.line(350, 40, 350, 190, dash="3 5", w=1, color=MG)
    f.save("atteli/09-2-rezistoru-slegumi.svg", "Rezistoru virknes un paralēlais slēgums")


def f09_3():
    f = Fig(720, 170)
    items = [(120, "Kondensators"), (360, "Elektrolītiskais\nkondensators"), (600, "Maināmais\nkondensators")]
    y = 70
    for x, lab in items:
        f.line(x - 60, y, x - 4, y); f.line(x + 4, y, x + 60, y)
        f.capacitor(x, y)
        f.mtext(x, 138, lab, size=13)
    f.text(360 - 16, y - 12, "+", size=16, bold=True)
    f.arrow(600 - 24, y + 24, 600 + 26, y - 26, w=1.4)
    f.save("atteli/09-3-kondensatori.svg", "Kondensatoru apzīmējumi")


def f09_4():
    f = Fig(560, 160)
    y = 70
    for x, lab, core in ((140, "Spole", False), (420, "Spole ar serdi", True)):
        L = f.inductor(x, y)
        f.line(x - 80, y, x - L, y); f.line(x + L, y, x + 80, y)
        if core:
            f.line(x - L, y - 16, x + L, y - 16, w=1.4)
            f.line(x - L, y - 21, x + L, y - 21, w=1.4)
        f.text(x, 128, lab, size=13)
    f.text(140, y + 28, "L", italic=True, size=14)
    f.save("atteli/09-4-spoles.svg", "Spoles apzīmējumi")


def f09_5():
    f = Fig(560, 230)
    xc, yc = 280, 115
    L = f.inductor(xc - 22, yc, horizontal=False, n=5)
    # labā spole vērsta uz otru pusi
    r, n = 7, 5
    d = f"M {xc + 22:.1f} {yc - L:.1f} " + "".join(f"a {r} {r} 0 0 0 0 {2 * r} " for _ in range(n))
    f.path(d)
    f.line(xc - 4, yc - L, xc - 4, yc + L, w=1.4); f.line(xc + 4, yc - L, xc + 4, yc + L, w=1.4)
    for sx, x in ((-1, xc - 22), (1, xc + 22)):
        f.line(x, yc - L, x + sx * 110, yc - L); f.line(x, yc + L, x + sx * 110, yc + L)
        f.circ(x + sx * 110, yc - L, 3.5); f.circ(x + sx * 110, yc + L, 3.5)
    f.text(xc - 150, yc + 5, "U₁", italic=True, size=15); f.text(xc + 150, yc + 5, "U₂", italic=True, size=15)
    f.text(xc - 62, yc + 5, "N₁", italic=True, size=14); f.text(xc + 62, yc + 5, "N₂", italic=True, size=14)
    f.text(xc - 80, 28, "Primārais tinums", size=13); f.text(xc + 82, 28, "Sekundārais tinums", size=13)
    f.text(xc, 212, "serde", size=12, italic=True)
    f.line(xc, 198, xc, yc + L + 4, w=0.8)
    f.save("atteli/09-5-transformators.svg", "Transformatora apzīmējums")


def f09_6():
    f = Fig(720, 200)
    y = 75
    items = [(120, "Diode", "normal"), (360, "Gaismas diode (LED)", "led"), (600, "Zenera diode", "zener")]
    for x, lab, kind in items:
        f.line(x - 60, y, x - 11, y); f.line(x + 11, y, x + 60, y)
        f.diode(x, y, kind=kind)
        f.text(x, 180, lab, size=13)
    f.text(120 - 58, y - 10, "A", size=13, bold=True); f.text(120 + 58, y - 10, "K", size=13, bold=True)
    f.text(120 - 58, y + 24, "anods", size=11); f.text(120 + 58, y + 24, "katods", size=11)
    f.arrow(120 - 30, y + 46, 120 + 30, y + 46, w=1.2)
    f.text(120, y + 64, "strāvas virziens", size=11, italic=True)
    f.save("atteli/09-6-diodes.svg", "Diožu apzīmējumi")


def _bjt(f, x, y, npn=True):
    f.circ(x, y, 30)
    f.line(x - 12, y - 18, x - 12, y + 18, w=3)
    f.line(x - 60, y, x - 12, y)
    f.line(x - 12, y - 8, x + 14, y - 24); f.line(x + 14, y - 24, x + 14, y - 58)
    if npn:
        f.arrow(x - 12, y + 8, x + 14, y + 24, w=1.6, head=10)
    else:
        f.arrow(x + 14, y + 24, x - 12, y + 8, w=1.6, head=10)
    f.line(x + 14, y + 24, x + 14, y + 58)
    f.text(x - 66, y + 5, "B", anchor="end", bold=True, size=14)
    f.text(x + 22, y - 48, "C", anchor="start", bold=True, size=14)
    f.text(x + 22, y + 56, "E", anchor="start", bold=True, size=14)


def f09_7():
    f = Fig(720, 230)
    _bjt(f, 130, 100, True); f.text(120, 205, "NPN tranzistors", size=13)
    _bjt(f, 360, 100, False); f.text(350, 205, "PNP tranzistors", size=13)
    x, y = 590, 100
    f.circ(x, y, 30)
    f.line(x - 4, y - 20, x - 4, y + 20, w=3)
    f.arrow(x - 60, y, x - 5, y, head=10)
    f.line(x - 4, y - 12, x + 14, y - 12); f.line(x + 14, y - 12, x + 14, y - 58)
    f.line(x - 4, y + 12, x + 14, y + 12); f.line(x + 14, y + 12, x + 14, y + 58)
    f.text(x - 66, y + 5, "G", anchor="end", bold=True, size=14)
    f.text(x + 22, y - 48, "D", anchor="start", bold=True, size=14)
    f.text(x + 22, y + 56, "S", anchor="start", bold=True, size=14)
    f.text(x - 6, 205, "Lauktranzistors (FET)", size=13)
    f.save("atteli/09-7-tranzistori.svg", "Tranzistoru apzīmējumi")


def f10_1():
    f = Fig(720, 380)
    # virknes kontūrs
    f.text(180, 22, "Virknes kontūrs", bold=True, size=14)
    y = 86
    L = f.inductor(140, y)
    f.line(60, y, 140 - L, y); f.line(140 + L, y, 216, y)
    f.capacitor(220, y); f.line(224, y, 300, y)
    f.circ(60, y, 3.5); f.circ(300, y, 3.5)
    f.text(140, y - 16, "L", italic=True, size=14); f.text(220, y - 20, "C", italic=True, size=14)
    # paralēlais kontūrs
    f.text(540, 22, "Paralēlais kontūrs", bold=True, size=14)
    xa, xb = 470, 610
    f.line(420, y, xa, y); f.line(xb, y, 660, y)
    f.circ(420, y, 3.5); f.circ(660, y, 3.5)
    y1, y2 = y - 24, y + 24
    for yy in (y1, y2):
        f.line(xa, y, xa, yy); f.line(xb, y, xb, yy)
    L = f.inductor(540, y1)
    f.line(xa, y1, 540 - L, y1); f.line(540 + L, y1, xb, y1)
    f.line(xa, y2, 536, y2); f.capacitor(540, y2, plate=18); f.line(544, y2, xb, y2)
    f.circ(xa, y, 3, fill=K); f.circ(xb, y, 3, fill=K)
    f.text(540, y1 - 12, "L", italic=True, size=14); f.text(540, y2 + 28, "C", italic=True, size=14)
    # grafiki
    for cx, peak in ((180, False), (540, True)):
        x0, y0, W, H = cx - 120, 345, 240, 150
        f.axes(x0, y0, W + 20, H + 10, xl="f", yl="Z")
        pts = []
        for i in range(201):
            t = i / 200
            v = 1 / (1 + ((t - 0.5) / 0.07) ** 2)
            val = (0.12 + 0.8 * v) if peak else (0.92 - 0.8 * v)
            pts.append((x0 + W * t, y0 - H * val))
        f.pl(pts, w=2.2)
        f.line(x0 + W / 2, y0, x0 + W / 2, y0 - H, dash="3 4", w=0.9, color=MG)
        f.text(x0 + W / 2, y0 + 16, "f₀", italic=True, size=12)
        f.text(cx, 168, "pretestība rezonansē " + ("maksimāla" if peak else "minimāla"), size=12)
    f.line(360, 40, 360, 365, dash="3 5", w=1, color=MG)
    f.save("atteli/10-1-kontura-rezonanse.svg", "Virknes un paralēlais svārstību kontūrs")


def f10_2():
    f = Fig(760, 420)
    panels = [("Zemo frekvenču filtrs (LPF)", "lp"), ("Augsto frekvenču filtrs (HPF)", "hp"),
              ("Joslas filtrs (BPF)", "bp"), ("Sprostfiltrs (BSF)", "bs")]
    for i, (name, kind) in enumerate(panels):
        x0 = 60 + (i % 2) * 380
        y0 = 180 + (i // 2) * 205
        W, H = 280, 120
        f.text(x0 + W / 2, y0 - H - 22, name, bold=True, size=13)
        f.axes(x0, y0, W + 20, H + 10, xl="f")
        f.text(x0 + 8, y0 - H - 4, "caurlaidība", anchor="start", size=10, italic=True)
        pts = []
        for k in range(201):
            t = k / 200
            lp = 1 / math.sqrt(1 + (t / 0.45) ** 10)
            hp = 1 / math.sqrt(1 + (0.55 / max(t, 1e-3)) ** 10)
            if kind == "lp":
                v = lp
            elif kind == "hp":
                v = hp
            elif kind == "bp":
                v = 1 / math.sqrt(1 + ((t - 0.5) / 0.13) ** 8)
            else:
                v = 1 - 1 / math.sqrt(1 + ((t - 0.5) / 0.13) ** 8)
            pts.append((x0 + W * t, y0 - H * (0.03 + 0.9 * v)))
        # caurlaides zona iekrāsota
        f.pl(pts + [(x0 + W, y0), (x0, y0)], close=True, fill=LG, w=0, color=LG)
        f.pl(pts, w=2.2)
        marks = {"lp": [0.45], "hp": [0.55], "bp": [0.37, 0.63], "bs": [0.37, 0.63]}[kind]
        for m in marks:
            f.line(x0 + W * m, y0, x0 + W * m, y0 - H, dash="3 4", w=0.9, color=MG)
        lab = "robežfrekvence" if len(marks) == 1 else "josla"
        f.text(x0 + W * sum(marks) / len(marks), y0 + 16, lab, size=11, italic=True)
    f.save("atteli/10-2-filtri.svg", "Četru filtru veidu caurlaidības līknes")


def f10_3():
    f = Fig(800, 250)
    labels = ["Transformators", "Taisngriezis", "Gludinātājs", "Stabilizators"]
    y = 170
    x0 = 100
    pos = chain(f, labels, x0, y, gap=64, size=12, minw=104)
    # ieeja un izeja
    f.arrow(x0 - 64, y, x0, y); f.arrow(pos[-1][2], y, pos[-1][2] + 64, y)
    f.text(x0 - 34, y + 22, "230 V ~", size=12)
    f.text(pos[-1][2] + 34, y + 22, "13,8 V =", size=12)
    # sprieguma formas virs savienojumiem
    xs = [x0 - 34] + [(pos[i][2] + pos[i + 1][1]) / 2 for i in range(3)] + [pos[-1][2] + 34]
    yw, ww = 70, 50
    for i, cx in enumerate(xs):
        f.line(cx - ww / 2, yw, cx + ww / 2, yw, w=0.6, color=MG)
        xa = cx - ww / 2
        if i == 0:
            f.sine(xa, yw, ww, 30, 2, w=1.8)
        elif i == 1:
            f.sine(xa, yw, ww, 13, 2, w=1.8)
        elif i == 2:
            f.sine(xa, yw, ww, 20, 2, w=1.8, rect=True)
        elif i == 3:
            pts = []
            for k in range(121):
                t = k / 120
                ph = (t * 4) % 1.0
                v = 1 - 0.18 * ph if ph > 0.12 else 0.82 + 0.18 * ph / 0.12
                pts.append((xa + ww * t, yw - 20 * v))
            f.pl(pts, w=1.8)
        else:
            f.line(xa, yw - 17, xa + ww, yw - 17, w=1.8)
        f.line(cx, yw + 26, cx, y - 12, w=0.7, dash="2 3", color=MG)
    caps = ["tīkla\nmaiņspriegums", "pazemināts\nmaiņspriegums", "pulsējošs\nlīdzspriegums", "izlīdzināts,\nar pulsācijām", "stabils\nlīdzspriegums"]
    for cx, c in zip(xs, caps):
        f.mtext(cx, 20, c, size=10)
    f.w = xs[-1] + 70
    f.save("atteli/10-3-barosanas-bloks.svg", "Barošanas bloka blokshēma")


ALL = [f07_1, f07_2, f07_3, f08_1, f08_2, f08_3, f09_1, f09_2, f09_3, f09_4, f09_5, f09_6, f09_7,
       f10_1, f10_2, f10_3]
