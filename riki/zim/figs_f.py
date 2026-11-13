"""Papildu zīmējumi (A prioritāte no recenzijas/trukstosie-atteli.md):
10.4.–10.6., 13.7., 14.1., 15.3., 16.2., 17.2. attēls."""
import math
from lib import (Fig, K, G, LG, MG, tw, RED, RED_T, BLUE, BLUE_T, GREEN, GREEN_T,
                 AMBER, AMBER_T, BRICK, BRICK_T, sym_amp, sym_mixer, sym_filter, sym_gen, lab)
from figs_a import _bjt
from figs_b import _groundline


# ------------------------------------------------------------------ 10.4.
def f10_4():
    f = Fig(760, 384)
    # kreisā puse: ko dara pastiprinātājs
    f.text(185, 24, "Ko dara pastiprinātājs", bold=True, size=14)
    cy = 190
    f.sine(40, cy, 80, 12, 2, w=2, color=BLUE)
    f.text(80, cy + 44, "ieeja: mazs signāls", size=11)
    f.line(124, cy, 162, cy)
    sym_amp(f, 185, cy)
    f.line(206, cy, 236, cy)
    f.sine(240, cy, 100, 44, 2, w=2.4, color=BLUE)
    f.text(290, cy + 70, "izeja: tāds pats, tikai lielāks", size=11)
    f.arrow(185, 90, 185, 168, w=1.6, color=AMBER)
    f.mtext(185, 74, "barošanas avots\n(enerģija)", size=11, color=AMBER)
    f.line(380, 40, 380, 340, dash="3 5", w=1, color=MG)
    # labā puse: pakāpe ar tranzistoru
    f.text(570, 24, "Pakāpe ar tranzistoru (kopējais emiters)", bold=True, size=14)
    yt, yg = 54, 320
    f.line(450, yt, 700, yt, w=2)
    f.text(704, yt + 5, "+U", anchor="start", size=13, bold=True)
    tx, ty = 600, 188                       # tranzistors: B (540,188), C (614,130), E (614,246)
    _bjt(f, tx, ty)
    xr = 500
    # R1 un R2 — bāzes dalītājs
    f.line(xr, yt, xr, 88); f.resistor(xr, 110, horizontal=False, label="R1"); f.line(xr, 132, xr, ty)
    f.line(xr, ty, 540, ty)
    f.line(xr, ty, xr, 238); f.resistor(xr, 260, horizontal=False, label="R2"); f.line(xr, 282, xr, yg)
    f.circ(xr, ty, 3, fill=K)
    # ieejas kondensators
    f.circ(426, ty, 4)
    f.line(430, ty, 460, ty)
    f.capacitor(464, ty)
    f.line(468, ty, xr, ty)
    f.text(426, ty - 14, "ieeja", size=11)
    f.text(464, ty + 30, "C1", size=12, italic=True)
    # RC
    xc = 614
    f.line(xc, yt, xc, 66); f.resistor(xc, 88, horizontal=False, label="RC"); f.line(xc, 110, xc, 130)
    # izejas kondensators
    f.circ(xc, 118, 3, fill=K)
    f.line(xc, 118, 660, 118); f.capacitor(664, 118); f.line(668, 118, 700, 118)
    f.circ(704, 118, 4)
    f.text(704, 104, "izeja", size=11)
    f.text(664, 146, "C2", size=12, italic=True)
    # RE
    f.line(xc, 246, xc, 254); f.resistor(xc, 276, horizontal=False, label="RE"); f.line(xc, 298, xc, yg)
    # zeme
    f.line(xr, yg, xc, yg, w=1.6)
    f.ground(556, yg, stem=6)
    f.mtext(575, 358, "R1 un R2 iestata darba punktu, RC — slodze;\nC1 un C2 nelaiž cauri līdzstrāvu",
            size=10, italic=True)
    f.save("atteli/10-4-pastiprinatajs.svg", "Pastiprinātājs: darbība un pakāpe ar tranzistoru")


# ------------------------------------------------------------------ 10.5.
def f10_5():
    f = Fig(760, 380)
    # blokshēma
    y = 80
    f.text(40, y + 5, "f₁ = 9 MHz", anchor="start", size=13, bold=True, color=BLUE)
    f.line(132, y, 196, y)
    sym_mixer(f, 220, y)
    lab(f, 220, y - 34, "Jaucējs")
    f.line(220, 140, 220, 104)
    f.arrow(220, 132, 220, 105, w=1.4)
    f.text(220, 156, "f₂ = 2 MHz", size=13, bold=True, color=BLUE)
    f.arrow(244, y, 320, y)
    f.mtext(282, y - 18, "7 un 11 MHz", size=11)
    sym_filter(f, 344, y, "bp")
    lab(f, 344, y - 34, "Joslas filtrs 7 MHz")
    f.arrow(368, y, 450, y)
    f.text(458, y + 5, "7 MHz", anchor="start", size=13, bold=True, color=GREEN)
    # spektrs
    x0, yb, W = 60, 320, 640
    fx = lambda mhz: x0 + W * mhz / 12.5
    # filtra caurlaides josla
    f.rect(fx(6.2), yb - 120, fx(7.8) - fx(6.2), 120, fill=GREEN_T, rx=0, sw=0)
    f.text(fx(7), yb - 126, "filtrs", size=11, italic=True, color=GREEN)
    f.arrow(x0, yb, x0 + W + 20, yb, w=1.3)
    f.text(x0 + W + 20, yb + 38, "f, MHz", anchor="end", size=12, italic=True)
    for k in range(0, 13):
        f.line(fx(k), yb, fx(k), yb + 5, w=1)
        f.text(fx(k), yb + 20, str(k), size=11)
    lines = [(2, 70, BLUE, "f₂"), (9, 70, BLUE, "f₁"), (7, 100, GREEN, "9 − 2 = 7"),
             (11, 100, MG, "9 + 2 = 11")]
    for m, h, c, t in lines:
        f.line(fx(m), yb, fx(m), yb - h, w=4, color=c)
        f.text(fx(m), yb - h - 8, t, size=12, bold=True, color=c)
    for i, (c, t) in enumerate(((BLUE, "ieejas signāli"), (GREEN, "starpība — filtrs to izvēlas"),
                                (MG, "summa — filtrs to aiztur"))):
        f.line(520, 140 + i * 20, 548, 140 + i * 20, w=4, color=c)
        f.text(556, 144 + i * 20, t, anchor="start", size=11)
    f.save("atteli/10-6-jaucejs.svg", "Jaucējs: summa un starpība")


# ------------------------------------------------------------------ 10.6.
def _gate_iec(f, cx, cy, sym, n_in=2, inv=False):
    w, h = 54, 64
    f.rect(cx - w / 2, cy - h / 2, w, h, rx=0, sw=1.8)
    f.text(cx, cy + 6, sym, size=16, bold=True)
    ys = [cy - 16, cy + 16] if n_in == 2 else [cy]
    for yy, name in zip(ys, "AB"):
        f.line(cx - w / 2 - 34, yy, cx - w / 2, yy)
        f.text(cx - w / 2 - 38, yy + 5, name, anchor="end", size=12, italic=True)
    xo = cx + w / 2
    if inv:
        f.circ(xo + 5, cy, 5, sw=1.6)
        xo += 10
    f.line(xo, cy, cx + w / 2 + 40, cy)
    f.text(cx + w / 2 + 44, cy + 5, "Y", anchor="start", size=12, italic=True)


def _gate_ansi(f, cx, cy, kind):
    x0 = cx - 30
    if kind == "and":
        f.path(f"M {x0} {cy - 30} L {cx} {cy - 30} A 30 30 0 0 1 {cx} {cy + 30} L {x0} {cy + 30} Z",
               fill="white", w=1.8)
        xo = cx + 30
    elif kind == "or":
        f.path(f"M {x0} {cy - 30} Q {cx + 10} {cy - 30} {cx + 32} {cy} Q {cx + 10} {cy + 30} {x0} {cy + 30} "
               f"Q {x0 + 14} {cy} {x0} {cy - 30} Z", fill="white", w=1.8)
        xo = cx + 32
    else:
        f.pl([(x0, cy - 26), (x0, cy + 26), (cx + 20, cy)], close=True, fill="white", w=1.8)
        f.circ(cx + 25, cy, 5, sw=1.6)
        xo = cx + 30
    ys = [cy] if kind == "not" else [cy - 16, cy + 16]
    for yy, name in zip(ys, "AB"):
        xin = x0 + (6 if kind == "or" else 0)
        f.line(x0 - 34, yy, xin, yy)
        f.text(x0 - 38, yy + 5, name, anchor="end", size=12, italic=True)
    f.line(xo, cy, cx + 70, cy)
    f.text(cx + 74, cy + 5, "Y", anchor="start", size=12, italic=True)


def f10_6():
    f = Fig(760, 330)
    cols = [(170, "UN (AND)", "Y = 1, ja A = 1 un B = 1"),
            (400, "VAI (OR)", "Y = 1, ja A = 1 vai B = 1"),
            (620, "NE (NOT)", "Y = pretējs A")]
    for x, t, rule in cols:
        f.text(x, 26, t, size=14, bold=True)
        f.text(x, 312, rule, size=11, italic=True)
    f.text(14, 110, "IEC", anchor="start", size=12, bold=True, color=BRICK)
    f.text(14, 226, "ASV", anchor="start", size=12, bold=True, color=BRICK)
    f.text(14, 242, "(ANSI)", anchor="start", size=10, color=BRICK)
    _gate_iec(f, 170, 105, "&")
    _gate_iec(f, 400, 105, "≥1")
    _gate_iec(f, 620, 105, "1", n_in=1, inv=True)
    _gate_ansi(f, 170, 225, "and")
    _gate_ansi(f, 400, 225, "or")
    _gate_ansi(f, 620, 225, "not")
    f.line(30, 165, 740, 165, dash="3 5", w=1, color=MG)
    f.save("atteli/10-7-logiskie-elementi.svg", "Loģisko elementu UN, VAI, NE apzīmējumi")


# ------------------------------------------------------------------ 13.7.
def f13_7():
    f = Fig(800, 300)
    y = 170
    boxes = [(80, "Transīvers"), (210, "SWR\nmērītājs"), (345, "Antenas\nskaņotājs")]
    for cx, t in boxes:
        f.box(cx, y, 104, 52, t, size=12)
    f.arrow(132, y, 158, y); f.arrow(262, y, 293, y)
    # kabelis līdz balunam
    xb = 640
    f.line(397, y, xb - 34, y, w=3)
    f.text((397 + xb - 34) / 2, y - 12, "koaksiālais kabelis (nesimetrisks)", size=11, italic=True)
    f.box(xb, y, 68, 40, "Baluns\n1:1", size=11)
    # dipols
    f.line(xb, y - 20, xb, 80, w=1.8)
    f.line(xb - 130, 80, xb + 130, 80, w=3)
    f.circ(xb, 80, 4, fill=K)
    f.text(xb, 64, "dipols (simetrisks)", size=11, italic=True)
    # zonas
    f.pl([(28, y + 46), (28, y + 54), (397, y + 54), (397, y + 46)], w=1.6, color=GREEN)
    f.mtext(212, y + 76, "transīvers redz 50 Ω: SWR ≈ 1:1,\nraidītājs dod pilnu jaudu", size=11,
            color=GREEN)
    f.pl([(397, y + 46), (397, y + 54), (xb - 34, y + 54), (xb - 34, y + 46)], w=1.6, color=AMBER)
    f.mtext(505, y + 76, "stāvviļņi un zudumi kabelī paliek —\nskaņotājs antenu nelabo", size=11,
            color=AMBER)
    f.mtext(xb + 90, y + 4, "neļauj strāvai\nplūst pa kabeļa\napvalka ārpusi", size=10, italic=True)
    f.save("atteli/13-7-saskanosana.svg", "SWR mērītāja, antenas skaņotāja un baluna vieta stacijā")


# ------------------------------------------------------------------ 14.1.
def f14_1():
    f = Fig(800, 250)
    segs = [("LF", "garie viļņi", "30–300 kHz", "10–1 km", "#ececec"),
            ("MF", "vidējie viļņi", "300–3000 kHz", "1000–100 m", "#e4e4e4"),
            ("HF", "īsviļņi", "3–30 MHz", "100–10 m", AMBER_T),
            ("VHF", "metru viļņi", "30–300 MHz", "10–1 m", BLUE_T),
            ("UHF", "decimetru viļņi", "300–3000 MHz", "1 m – 10 cm", GREEN_T)]
    x0, W, y1, y2 = 40, 720, 70, 120
    sw = W / 5
    for i, (n, nm, fr, wl, c) in enumerate(segs):
        xa = x0 + i * sw
        f.rect(xa, y1, sw, y2 - y1, fill=c, rx=0, sw=1.2)
        f.text(xa + sw / 2, y1 + 22, n, size=15, bold=True)
        f.text(xa + sw / 2, y1 + 40, nm, size=11)
        f.text(xa + sw / 2, 60, fr, size=11, bold=True)
        f.text(xa + sw / 2, 42, wl, size=11, italic=True, color="#555")
    f.text(x0, 22, "viļņa garums (slīprakstā) un frekvence", anchor="start", size=11, italic=True, color="#555")
    f.text(x0 + W, 24, "frekvence aug →", anchor="end", size=11, italic=True)
    # B kategorijas joslas logaritmiskā mērogā (30 kHz … 3000 MHz = 5 dekādes)
    fx = lambda mhz: x0 + sw * (math.log10(mhz / 0.03))
    bands = [(3.6, "80 m"), (7.05, "40 m"), (21.2, "15 m"), (28.5, "10 m"), (51, "6 m"),
             (145, "2 m"), (435, "70 cm"), (1270, "23 cm")]
    yb = 166
    f.text(x0, yb + 4, "B kategorijas joslas:", anchor="start", size=12, bold=True, color=BRICK)
    for i, (m, n) in enumerate(bands):
        x = fx(m)
        f.line(x, y2, x, yb + 18 + (i % 2) * 22, w=1.4, color=BRICK)
        f.circ(x, y2, 3.5, fill=BRICK, color=BRICK)
        f.text(x, yb + 32 + (i % 2) * 22, n, size=11, bold=True, color=BRICK)
    f.save("atteli/14-1-radiofrekvencu-spektrs.svg", "Radiofrekvenču spektra dalījums un B kategorijas joslas")


# ------------------------------------------------------------------ 15.3.
def f15_3():
    f = Fig(760, 336)
    x0, y0, W, H = 90, 270, 600, 220
    fmin, fmax, smax = 3.50, 3.80, 4.0
    fx = lambda v: x0 + W * (v - fmin) / (fmax - fmin)
    sy = lambda s: y0 - H * (s - 1) / (smax - 1)
    f0 = 3.65
    swr = lambda v: min(smax, 1.1 + 70 * (v - f0) ** 2)
    # josla ar SWR < 2
    d = math.sqrt((2 - 1.1) / 70)
    f.rect(fx(f0 - d), sy(smax), fx(f0 + d) - fx(f0 - d), y0 - sy(smax), fill=GREEN_T, rx=0, sw=0)
    f.text(fx(f0), sy(smax) + 18, "SWR < 2: ērti strādāt", size=11, color=GREEN, bold=True)
    f.axes(x0, y0, W + 20, H + 14)
    f.text(x0 + W + 20, y0 + 38, "f, MHz", anchor="end", size=12, italic=True)
    f.text(x0 - 10, y0 - H - 18, "SWR", anchor="end", size=12, italic=True)
    for s in (1, 1.5, 2, 3, 4):
        f.line(x0 - 5, sy(s), x0, sy(s), w=1)
        f.text(x0 - 9, sy(s) + 4, f"{s:g}".replace(".", ","), anchor="end", size=11)
    f.line(x0, sy(2), x0 + W, sy(2), dash="5 4", w=1.2, color=AMBER)
    f.text(x0 + 8, sy(2) - 6, "2:1 pieļaujams", anchor="start", size=11, color=AMBER)
    f.line(x0, sy(3), x0 + W, sy(3), dash="5 4", w=1.2, color=RED)
    f.text(x0 + 8, sy(3) - 6, "3:1 robeža", anchor="start", size=11, color=RED)
    for v in (3.50, 3.55, 3.60, 3.65, 3.70, 3.75, 3.80):
        f.line(fx(v), y0, fx(v), y0 + 5, w=1)
        f.text(fx(v), y0 + 20, f"{v:.2f}".replace(".", ","), size=11)
    pts = [(fx(fmin + (fmax - fmin) * i / 200), sy(swr(fmin + (fmax - fmin) * i / 200))) for i in range(201)]
    f.pl(pts, w=2.6, color=BLUE)
    f.line(fx(f0), sy(1.1), fx(f0), y0, dash="3 3", w=1, color=BLUE)
    f.circ(fx(f0), sy(1.1), 4, fill=BLUE, color=BLUE)
    f.text(fx(f0), sy(1.6), "rezonanse: zemākais SWR", size=11, color=BLUE, bold=True)
    f.arrow(fx(f0), sy(1.55), fx(f0), sy(1.1) - 8, w=1.2, color=BLUE, head=7)
    f.save("atteli/15-3-swr-likne.svg", "Antenu analizatora SWR līkne 80 m dipolam")


# ------------------------------------------------------------------ 16.2.
def _ferrite(f, x, y, h=26):
    """Ferīta uzmava uz vada (vads iet horizontāli caur to)."""
    f.rect(x - 14, y - h / 2, 28, h, fill="#4a4a4a", rx=5, color="#222")
    f.text(x, y - h / 2 - 6, "ferīts", size=10, italic=True)


def f16_2():
    f = Fig(800, 330)
    f.text(200, 24, "Tavā stacijā", bold=True, size=14)
    f.text(590, 24, "Pie traucētās ierīces", bold=True, size=14)
    f.line(395, 40, 395, 310, dash="3 5", w=1, color=MG)
    # stacija
    y = 150
    f.box(70, y, 96, 46, "Transīvers", size=12)
    f.line(118, y, 150, y)
    sym_filter(f, 173, y, "lp")
    f.text(173, y + 44, "zemo frekvenču", size=11, color=GREEN, bold=True)
    f.text(173, y + 58, "filtrs (LPF)", size=11, color=GREEN, bold=True)
    f.line(196, y, 330, y, w=2.6)
    _ferrite(f, 300, y)
    f.line(330, y, 330, 70, w=2)
    f.line(270, 70, 390, 70, w=2.6)
    f.text(330, 58, "antena", size=11, italic=True)
    f.mtext(230, 250, "LPF aiztur harmonikas raidītāja izejā;\nferīts vai baluns pie antenas aiztur\nstrāvu pa kabeļa apvalka ārpusi",
            size=11)
    # traucētā ierīce
    xt = 690
    f.box(xt, y, 96, 46, "TV, radio", size=12)
    f.line(xt - 48, y, 590, y)
    sym_filter(f, 567, y, "hp")
    f.text(567, y + 44, "augsto frekvenču", size=11, color=BLUE, bold=True)
    f.text(567, y + 58, "filtrs (HPF)", size=11, color=BLUE, bold=True)
    f.line(544, y, 470, y, w=2.6)
    f.line(470, y, 470, 80, w=2)
    for i, hw in enumerate((16, 13, 10)):
        f.line(470 - hw, 84 + i * 9, 470 + hw, 84 + i * 9, w=1.6)
    f.text(470, 70, "TV antena", size=11, italic=True)
    # tīkla un skaļruņu vadi ar ferītiem
    f.line(xt + 20, y + 23, xt + 20, 236); f.line(xt + 20, 236, 760, 236)
    _ferrite(f, xt + 46, 236, h=22)
    f.text(780, 256, "tīkls", anchor="end", size=10, italic=True)
    f.line(xt - 20, y + 23, xt - 20, 270); f.line(xt - 20, 270, 610, 270)
    _ferrite(f, 640, 270, h=22)
    f.text(606, 274, "skaļruņu vads", anchor="end", size=10, italic=True)
    f.mtext(590, 310, "HPF laiž cauri TV signālus, aiztur īsviļņus; ferīti — tuvu ierīcei", size=11)
    f.save("atteli/16-2-filtri-un-feriti.svg", "Kur liek filtrus un ferītus")


# ------------------------------------------------------------------ 17.2.
def f17_2():
    f = Fig(800, 330)
    yg = 270
    _groundline(f, 20, 780, yg)
    xm, hm = 170, 170                        # masts
    # krišanas zona
    f.path(f"M {xm - hm} {yg} A {hm} {hm} 0 0 1 {xm + hm} {yg} Z", fill=RED_T, w=1.2, color=RED, dash="5 4")
    f.text(xm, yg - hm - 14, "krišanas zona: rādiuss = masta augstums", size=11, color=RED, bold=True)
    f.line(xm, yg, xm, yg - hm, w=4)
    for dx in (-90, 90):
        f.line(xm, yg - hm * 0.7, xm + dx, yg, w=1, color=MG)
    f.darrow(xm - 26, yg, xm - 26, yg - hm, color=K)
    f.text(xm - 32, yg - hm / 2, "h", anchor="end", size=14, italic=True, bold=True)
    # antenas vads
    f.line(xm, yg - hm, 420, yg - 110, w=1.6)
    f.circ(420, yg - 110, 3, fill=K)
    f.line(420, yg - 110, 420, yg, w=3, color="#7a5a3a")
    f.text(285, yg - hm + 72, "antenas vads, garums L", size=11, italic=True)
    # elektrolīnija
    xl = 690
    for x in (xl, xl + 60):
        f.line(x, yg, x, yg - 150, w=4, color="#555")
        f.line(x - 20, yg - 140, x + 20, yg - 140, w=2.4, color="#555")
    for dy in (0, 0):
        pass
    f.path(f"M {xl - 120} {yg - 132} Q {xl - 60} {yg - 118} {xl} {yg - 140} Q {xl + 30} {yg - 126} {xl + 60} {yg - 140} "
           f"Q {xl + 80} {yg - 128} {xl + 96} {yg - 134}", w=1.4, color=RED)
    f.text(xl + 30, yg - 160, "elektrolīnija", size=12, bold=True, color=RED)
    # attālums
    f.darrow(xm, yg + 26, xl, yg + 26, color=GREEN)
    f.text((xm + xl) / 2, yg + 48, "attālums līdz līnijai > h + L", size=12, bold=True, color=GREEN)
    f.save("atteli/17-3-masta-drosibas-zona.svg", "Masta krišanas zona un attālums līdz elektrolīnijai")


ALL = [f10_4, f10_5, f10_6, f13_7, f14_1, f15_3, f16_2, f17_2]
