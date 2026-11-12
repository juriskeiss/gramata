"""14.–17. nodaļas zīmējumi."""
import math
from lib import Fig, K, G, LG, MG, chain, tw, arcpts
from figs_b import _groundline


def _pt(cx, cy, r, a):
    return (cx + r * math.sin(a), cy - r * math.cos(a))


def f14_1():
    f = Fig(760, 340)
    cx, cy, R = 380, 1200, 950
    A = 0.40
    # jonosfēra
    f.pl(arcpts(cx, cy, R + 168, -A, A), w=30, color=G)
    f.text(cx, cy - R - 195, "jonosfēra", size=13, bold=True)
    # Zeme
    earth = arcpts(cx, cy, R, -A, A)
    f.pl(earth + [(earth[-1][0], 340), (earth[0][0], 340)], close=True, fill=LG, w=0, color=LG)
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
    f.arrow(T[0], T[1], D[0], D[1], w=1.8)
    f.ltext((T[0] + D[0]) / 2 - 6, (T[1] + D[1]) / 2 - 9, "tiešais vilnis", anchor="start", size=11)
    # zemes vilnis
    gw = arcpts(cx, cy, R + 9, aT + 0.012, 0.02, n=40)
    f.pl(gw[:-2], dash="6 4", w=1.8)
    f.arrow(gw[-4][0], gw[-4][1], gw[-1][0], gw[-1][1], w=1.8)
    x, y = _pt(cx, cy, R + 26, -0.08)
    f.text(x, y, "zemes vilnis", size=12)
    # telpas vilnis
    I = _pt(cx, cy, R + 153, 0.0)
    Rx = _pt(cx, cy, R + 36, aR)
    f.line(T[0], T[1], I[0], I[1], w=1.8)
    f.arrow(I[0], I[1], Rx[0], Rx[1], w=1.8)
    f.text(I[0] + 150, I[1] + 62, "telpas vilnis", size=12)
    f.save("atteli/14-1-izplatisanas-veidi.svg", "Trīs radioviļņu izplatīšanās veidi")


def f14_2():
    f = Fig(780, 400)
    yg = 350
    yy = lambda h: yg - 0.72 * h
    xl, xm, xr = 110, 430, 750
    f.text((xl + xm) / 2, 22, "Diena", bold=True, size=15)
    f.text((xm + xr) / 2, 22, "Nakts", bold=True, size=15)
    # slāņi: diena
    for h1, h2, name, fill in ((60, 90, "D", "#b0b0b0"), (95, 130, "E", G), (160, 220, "F1", LG), (250, 400, "F2", G)):
        f.rect(xl, yy(h2), xm - xl - 6, yy(h1) - yy(h2), fill=fill, rx=0, sw=0.6)
        f.text(xm - 14, (yy(h1) + yy(h2)) / 2 + 5, name, anchor="end", size=13, bold=True)
    # nakts
    f.rect(xm + 6, yy(400), xr - xm - 6, yy(200) - yy(400), fill=G, rx=0, sw=0.6)
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
    f.arrow(x0, yg, x0 + 34, yy(72), w=1.8)
    f.text(x0 + 34, yy(72) + 6, "×", size=20, bold=True)
    f.text(x0 - 8, yg + 18, "80 m", size=12, bold=True)
    f.text(x0 + 6, yg + 34, "absorbē D slānis", size=11, italic=True)
    # diena: 15 m atstarojas no F2
    xa = xl + 130
    f.line(xa, yg, xa + 70, yy(300), w=1.8)
    f.arrow(xa + 70, yy(300), xa + 140, yg, w=1.8)
    f.text(xa + 70, yg + 18, "15 m", size=12, bold=True)
    f.text(xa + 70, yg + 34, "atstarojas no F2", size=11, italic=True)
    # nakts: 80 m atstarojas no F
    xb = xm + 50
    f.line(xb, yg, xb + 110, yy(260), w=1.8)
    f.arrow(xb + 110, yy(260), xb + 220, yg, w=1.8)
    f.text(xb + 110, yg + 18, "80 m", size=12, bold=True)
    f.text(xb + 110, yg + 34, "D slāņa nav; atstarojas no F", size=11, italic=True)
    f.save("atteli/14-2-jonosferas-slani.svg", "Jonosfēras slāņi dienā un naktī")


def f14_3():
    f = Fig(780, 330)
    yg = 240
    f.rect(30, 40, 720, 28, fill=G, rx=0, sw=0.6)
    f.text(690, 59, "jonosfēra", size=12, bold=True)
    _groundline(f, 30, 750, yg)
    xt = 80
    f.line(xt, yg, xt, yg - 40, w=3)
    f.text(xt - 8, yg - 16, "raidī-", anchor="end", size=11, italic=True)
    f.text(xt - 8, yg - 3, "tājs", anchor="end", size=11, italic=True)
    # zemes vilnis
    f.arrow(xt + 8, yg - 10, 230, yg - 10, dash="6 4", w=1.8)
    f.text(160, yg - 18, "zemes vilnis", size=12)
    # telpas vilnis
    f.line(xt, yg - 40, 330, 68, w=1.8)
    f.arrow(330, 68, 590, yg, w=1.8)
    f.text(420, 130, "telpas vilnis", anchor="start", size=12)
    # zonas
    yb = yg + 26
    for a, b, lab, fill in ((xt, 232, "dzirdams", None), (232, 588, "MIRUSĪ ZONA", LG), (588, 748, "dzirdams", None)):
        if fill:
            f.rect(a, yb - 8, b - a, 30, fill=fill, rx=0, sw=0.8)
        f.pl([(a, yb - 8), (a, yb + 22)], w=1); f.pl([(b, yb - 8), (b, yb + 22)], w=1)
        f.text((a + b) / 2, yb + 12, lab, size=12, bold=bool(fill))
    f.text(410, yb + 46, "signāls nav dzirdams: zemes vilnis jau izdzisis, telpas vilnis vēl nav nolaidies", size=11, italic=True)
    f.save("atteli/14-3-mirusi-zona.svg", "Mirusī zona")


def f14_4():
    f = Fig(780, 340)
    yg = 260
    f.rect(30, 40, 720, 28, fill=G, rx=0, sw=0.6)
    f.text(700, 59, "F slānis", size=12, bold=True)
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
        f.line(src[0], src[1], xu, 68, w=1.5)
        f.arrow(xu, 68, xd, yg, w=1.5)
    # zema leņķa stars salīdzinājumam
    f.arrow(src[0], src[1], 740, 150, dash="6 4", w=1.4)
    f.text(742, 204, "zema leņķa stars:", anchor="end", size=11, italic=True)
    f.text(742, 218, "tālie sakari", anchor="end", size=11, italic=True)
    yb = yg + 24
    a, b = xc - 250, xc + 250
    f.pl([(a, yb - 6), (a, yb), (b, yb), (b, yb - 6)], w=1.2)
    f.text(xc, yb + 20, "nosegtais apgabals ap raidītāju, bez mirušās zonas", size=12)
    f.text(xc, yb + 38, "līdz dažiem simtiem kilometru", size=11, italic=True)
    f.save("atteli/14-4-nvis.svg", "NVIS izplatīšanās")


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
    f.arrow(xe + 30, y - 22, xa - 40, y - 22, w=1.8)
    f.text(xm, y - 32, "tiešā jauda", size=12)
    f.arrow(xa - 40, y + 22, xe + 30, y + 22, w=1.4, dash="6 4")
    f.text(xm, y + 42, "atstarotā jauda", size=12)
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
    f.sine(x, y + h / 2, w, 62, 2.5, w=2.4)
    f.text(190, y + h + 22, "laiks →", size=12, italic=True)
    f.text(190, y + h + 44, "rāda signāla formu: amplitūdu un periodu", size=11)
    f.text(x - 10, y + h / 2 + 4, "U", anchor="end", size=12, italic=True)
    f.text(570, 24, "Spektra analizators", bold=True, size=14)
    x = 430
    _grid(f, x, y, w, h)
    yb = y + h - 8
    for k, hh, lab in ((1, 160, "f"), (2, 70, "2f"), (3, 40, "3f"), (4, 18, "4f")):
        xx = x + w * k / 5
        f.line(xx, yb, xx, yb - hh, w=4)
        f.text(xx, yb - hh - 6, lab, size=11, italic=True)
    f.line(x + 6, yb, x + w - 6, yb, w=1, color=MG)
    f.text(570, y + h + 22, "frekvence →", size=12, italic=True)
    f.text(570, y + h + 44, "rāda sastāvu: pamatfrekvenci un harmonikas", size=11)
    f.text(x - 10, y + h / 2 + 4, "dB", anchor="end", size=12, italic=True)
    f.line(380, 40, 380, 280, dash="3 5", w=1, color=MG)
    f.save("atteli/15-3-osciloskops-spektra-analizators.svg", "Osciloskops un spektra analizators")


def _house(f, x1, x2, yb, yw, apex):
    f.pl([(x1, yb), (x1, yw), ((x1 + x2) / 2, apex), (x2, yw), (x2, yb)], close=True, fill="white", w=2)


def _num(f, x, y, n):
    f.circ(x, y, 10, fill="white", sw=1.4)
    f.text(x, y + 4.5, str(n), size=12, bold=True)


def f16_1():
    f = Fig(820, 430)
    yb = 300
    _groundline(f, 20, 800, yb)
    # radioamatiera māja
    _house(f, 50, 290, yb, 180, 120)
    f.text(126, yb + 22, "radioamatiera māja", anchor="start", size=12, italic=True)
    f.box(130, 250, 110, 40, "Raidītājs", size=12)
    xa = 250
    f.line(xa, 162, xa, 50, w=2.4)
    f.line(xa - 60, 50, xa + 60, 50, w=2.4)
    f.line(185, 250, 215, 250); f.line(215, 250, xa, 200); f.line(xa, 200, xa, 162)
    # kaimiņa māja
    _house(f, 520, 780, yb, 180, 120)
    f.text(650, yb + 22, "kaimiņa māja", size=12, italic=True)
    f.box(585, 250, 90, 40, "TV, radio", size=12)
    f.box(720, 250, 80, 40, "Skaļruņi", size=12)
    f.path("M 630 250 C 645 232, 660 268, 680 250", w=1.4)
    xt = 570
    f.line(xt, 166, xt, 84, w=2)
    for i, hw in enumerate((16, 13, 10)):
        f.line(xt - hw, 90 + i * 9, xt + hw, 90 + i * 9, w=1.6)
    f.line(xt, 166, xt, 230)
    # elektrotīkls
    f.pl([(110, 270), (110, 345), (600, 345), (600, 270)], w=1.6, dash="2 4")
    f.text(355, 362, "elektrotīkls", size=11, italic=True)
    # ceļi
    src = (xa + 60, 50)
    f.arrow(src[0] + 4, src[1] + 2, xt - 20, 96, w=1.8)
    _num(f, 430, 62, 1)
    f.arrow(300, 345, 420, 345, w=2.2)
    _num(f, 355, 330, 2)
    f.arrow(src[0] + 4, src[1] + 10, 652, 244, w=1.8, dash="7 4")
    _num(f, 470, 150, 3)
    f.arrow(src[0] + 4, src[1] + 6, 716, 228, w=1.8, dash="2 4")
    _num(f, 600, 178, 4)
    f.text(xa, 38, "antena", size=11, italic=True)
    # leģenda
    leg = ["1 — caur ierīces antenu", "2 — pa elektrotīkla vadiem", "3 — pa pieslēgtajiem vadiem", "4 — tieši caur ierīces korpusu"]
    for i, t in enumerate(leg):
        f.text(60 + (i % 2) * 390, 392 + (i // 2) * 20, t, anchor="start", size=12)
    f.save("atteli/16-1-traucejumu-celi.svg", "Ceļi, pa kuriem traucējums nonāk ierīcē")


def f17_1():
    f = Fig(800, 320)
    labs = ["Transīvers", "Barošanas\nbloks", "Antenu\nskaņotājs"]
    # pareizi
    f.text(210, 24, "Pareizi: katrai iekārtai savs vads", bold=True, size=13)
    xs = [80, 210, 340]
    for x, l in zip(xs, labs):
        f.box(x, 80, 104, 48, l, size=12)
        f.line(x, 104, x, 176, w=2)
    f.rect(40, 176, 340, 12, fill=MG, rx=2)
    f.text(210, 208, "zemējuma kopne", size=12, italic=True)
    f.line(120, 188, 120, 236, w=2)
    f.ground(120, 236, stem=12)
    f.text(140, 262, "zemētājs, ne vairāk kā 4 Ω", anchor="start", size=12)
    # nepareizi
    f.text(610, 24, "Nepareizi: virknē, viena caur otru", bold=True, size=13)
    xs = [490, 610, 730]
    for x, l in zip(xs, labs):
        f.box(x, 80, 100, 48, l, size=12)
    for i in range(2):
        f.path(f"M {xs[i]} 104 C {xs[i]} 140, {xs[i + 1]} 140, {xs[i + 1]} 104", w=2)
    f.line(730, 104, 730, 190, w=2)
    f.ground(730, 190, stem=12)
    # krusts
    f.line(470, 130, 770, 250, w=5, color=MG); f.line(770, 130, 470, 250, w=5, color=MG)
    f.line(430, 40, 430, 290, dash="3 5", w=1, color=MG)
    f.save("atteli/17-1-stacijas-zemejums.svg", "Stacijas zemējums")


ALL = [f14_1, f14_2, f14_3, f14_4, f15_1, f15_2, f15_3, f16_1, f17_1]
