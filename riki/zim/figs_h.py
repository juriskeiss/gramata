"""Pamatshēmas no kursa 7. nodarbības slaidiem (2.–10. slaids):
filtri ar shēmām un raksturlīknēm, diožu tilts, sprieguma stabilizators,
platjoslas un rezonanses pastiprinātājs, multivibrators."""
import math
from lib import (Fig, K, MG, RED, BLUE, GREEN, BRICK, BLUE_T, BRICK_T)


# ---------------------------------------------------------------- palīgi
def _dot(f, x, y):
    f.circ(x, y, 3.2, fill=K)


def _term(f, x, y):
    f.circ(x, y, 3.8)


def _cap_v(f, x, y1, y2, plate=22):
    """Vertikāls vads no y1 līdz y2 ar kondensatoru vidū."""
    ym = (y1 + y2) / 2
    f.line(x, y1, x, ym - 4); f.line(x, ym + 4, x, y2)
    f.capacitor(x, ym, horizontal=False, plate=plate)


def _ind_v(f, x, y1, y2, n=4, r=6):
    ym = (y1 + y2) / 2
    h = f.inductor(x, ym, horizontal=False, n=n, r=r)
    f.line(x, y1, x, ym - h); f.line(x, ym + h, x, y2)


def _res_v(f, x, y1, y2, label=None, dash=None, L=40):
    ym = (y1 + y2) / 2
    f.line(x, y1, x, ym - L / 2, dash=dash); f.line(x, ym + L / 2, x, y2, dash=dash)
    f.rect(x - 7, ym - L / 2, 14, L, rx=0, dash=dash)
    if label:
        f.text(x + 12, ym + 5, label, anchor="start", size=12, italic=True)


def _ind_h(f, x1, x2, y, n=4, r=6):
    xm = (x1 + x2) / 2
    h = f.inductor(xm, y, n=n, r=r)
    f.line(x1, y, xm - h, y); f.line(xm + h, y, x2, y)


def _cap_h(f, x1, x2, y, plate=22):
    xm = (x1 + x2) / 2
    f.line(x1, y, xm - 4, y); f.line(xm + 4, y, x2, y)
    f.capacitor(xm, y, plate=plate)


def _curve(f, x0, y0, W, H, kind):
    """Raksturlīkne kā slaidos: sarkana U ass, zaļa f ass, zila līkne."""
    f.arrow(x0, y0, x0, y0 - H - 14, color=RED, w=1.8)
    f.arrow(x0, y0, x0 + W + 14, y0, color=GREEN, w=1.8)
    f.text(x0 + 8, y0 - H - 8, "U", anchor="start", size=12)
    f.text(x0 + W + 12, y0 - 8, "f", italic=True, size=13)
    pts = []
    for k in range(161):
        t = k / 160
        if kind == "lp":
            v = 1 / math.sqrt(1 + (t / 0.55) ** 10)
        elif kind == "hp":
            v = 1 / math.sqrt(1 + (0.4 / max(t, 1e-3)) ** 10)
        elif kind == "bp":
            v = math.exp(-((t - 0.5) / 0.14) ** 4)
        else:
            v = 1 - 0.95 * math.exp(-((t - 0.5) / 0.12) ** 2)
        pts.append((x0 + 2 + W * t, y0 - 3 - (H - 8) * v))
    f.pl(pts, w=2.4, color=BLUE)


def _rails(f, x0, x1, yt, yb):
    f.line(x0, yt, x1, yt); f.line(x0, yb, x1, yb)
    for x in (x0, x1):
        _term(f, x, yt); _term(f, x, yb)


def _band(f, y, name, short, text, color, tint):
    f.rect(30, y, 840, 26, fill=color, rx=4, sw=0, color=color)
    f.text(42, y + 18, short, anchor="start", size=13, bold=True, color="white")
    f.text(92, y + 18, f"{name}: {text}", anchor="start", size=11.5, color="white")


def _q(f, x, y, r=21, npn=True, mirror=False):
    """Mazs bipolārais tranzistors; atgriež B, C, E pieslēguma punktus."""
    s = -1 if mirror else 1
    f.circ(x, y, r)
    bx = x - 7 * s
    f.line(bx, y - 12, bx, y + 12, w=2.6)
    B = (x - (r + 12) * s, y)
    f.line(B[0], y, bx, y)
    cx = x + 9 * s
    f.line(bx, y - 6, cx, y - 15); f.line(cx, y - 15, cx, y - r - 12)
    if npn:
        f.arrow(bx, y + 6, cx, y + 15, w=1.5, head=8)
    else:
        f.arrow(cx, y + 15, bx, y + 6, w=1.5, head=8)
    f.line(cx, y + 15, cx, y + r + 12)
    return B, (cx, y - r - 12), (cx, y + r + 12)


def _diode_seg(f, p1, p2, s=9, kind="normal"):
    """Diode uz nogriežņa p1→p2 (anods p1 pusē, katods p2 pusē)."""
    (x1, y1), (x2, y2) = p1, p2
    L = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    px, py = -uy, ux
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    a = (mx - ux * s, my - uy * s)
    c = (mx + ux * s, my + uy * s)
    f.line(x1, y1, a[0], a[1]); f.line(c[0], c[1], x2, y2)
    f.pl([(a[0] + px * s, a[1] + py * s), (a[0] - px * s, a[1] - py * s), c], close=True, fill="white")
    if kind == "zener":
        f.pl([(c[0] + px * s - ux * 5, c[1] + py * s - uy * 5), (c[0] + px * s, c[1] + py * s),
              (c[0] - px * s, c[1] - py * s), (c[0] - px * s + ux * 5, c[1] - py * s + uy * 5)], w=2)
    else:
        f.line(c[0] + px * s, c[1] + py * s, c[0] - px * s, c[1] - py * s, w=2)


# ---------------------------------------------------------------- 10.2.
def f10_2():
    f = Fig(900, 430)
    # LPF
    y = 20
    _band(f, y, "Zemo frekvenču filtrs", "LPF", "laiž cauri zemās frekvences, nomāc augstās", BRICK, BRICK_T)
    yt, yb = y + 70, y + 170
    _rails(f, 90, 400, yt, yb)
    f.line(90, yt, 400, yt, color="white", w=3)
    _ind_h(f, 90, 240, yt); f.line(240, yt, 400, yt)
    _dot(f, 300, yt); _dot(f, 300, yb)
    _cap_v(f, 300, yt, yb, plate=30)
    f.text(165, yt - 16, "L", italic=True, size=13); f.text(322, (yt + yb) / 2 + 5, "C", italic=True, size=13, anchor="start")
    f.text(90, yb + 24, "ieeja", size=11, italic=True); f.text(400, yb + 24, "izeja", size=11, italic=True)
    _curve(f, 560, yb, 260, 100, "lp")
    # HPF
    y = 220
    _band(f, y, "Augsto frekvenču filtrs", "HPF", "laiž cauri frekvences virs robežfrekvences, nomāc zemākās", BLUE, BLUE_T)
    yt, yb = y + 70, y + 170
    _rails(f, 90, 400, yt, yb)
    f.line(90, yt, 400, yt, color="white", w=3)
    _cap_h(f, 90, 240, yt, plate=30); f.line(240, yt, 400, yt)
    _dot(f, 300, yt); _dot(f, 300, yb)
    _ind_v(f, 300, yt, yb)
    f.text(165, yt - 22, "C", italic=True, size=13); f.text(318, (yt + yb) / 2 + 5, "L", italic=True, size=13, anchor="start")
    f.text(90, yb + 24, "ieeja", size=11, italic=True); f.text(400, yb + 24, "izeja", size=11, italic=True)
    _curve(f, 560, yb, 260, 100, "hp")
    f.save("atteli/10-2-lpf-hpf.svg", "Zemo un augsto frekvenču filtrs: shēma un raksturlīkne")


# ---------------------------------------------------------------- 10.3.
def f10_3():
    f = Fig(900, 470)
    # BPF
    y = 20
    _band(f, y, "Joslas filtrs", "BPF", "laiž cauri tikai noteiktu frekvenču joslu, zemākas un augstākas apslāpē", BRICK, BRICK_T)
    yt, yb = y + 70, y + 180
    # a) paralēlais LC pret zemi
    _rails(f, 40, 280, yt, yb)
    _dot(f, 110, yt); _dot(f, 110, yb)
    f.line(110, yt, 110, yt + 18); f.line(110, yb - 18, 110, yb)
    f.line(88, yt + 18, 132, yt + 18); f.line(88, yb - 18, 132, yb - 18)
    _cap_v(f, 88, yt + 18, yb - 18); _ind_v(f, 132, yt + 18, yb - 18, n=3, r=7)
    _dot(f, 220, yt); _dot(f, 220, yb)
    _res_v(f, 220, yt, yb, dash="4 3")
    f.text(160, yb + 24, "paralēlais kontūrs pret zemi", size=10.5, italic=True)
    # b) virknes LC garenvirzienā
    _rails(f, 320, 560, yt, yb)
    f.line(320, yt, 560, yt, color="white", w=3)
    _ind_h(f, 320, 410, yt, n=3); _cap_h(f, 410, 470, yt); f.line(470, yt, 560, yt)
    _dot(f, 510, yt); _dot(f, 510, yb)
    _res_v(f, 510, yt, yb, dash="4 3")
    f.text(440, yb + 24, "virknes kontūrs signāla ceļā", size=10.5, italic=True)
    _curve(f, 620, yb, 220, 100, "bp")
    # BSF
    y = 230
    _band(f, y, "Sprostfiltrs", "BSF", "nomāc noteiktu frekvenču joslu, pārējās izlaiž", BLUE, BLUE_T)
    yt, yb = y + 70, y + 180
    # a) virknes LC pret zemi
    _rails(f, 40, 280, yt, yb)
    _dot(f, 110, yt); _dot(f, 110, yb)
    ym = (yt + yb) / 2
    _cap_v(f, 110, yt, ym); _ind_v(f, 110, ym, yb, n=3, r=6)
    _dot(f, 220, yt); _dot(f, 220, yb)
    _res_v(f, 220, yt, yb, dash="4 3")
    f.text(160, yb + 24, "virknes kontūrs pret zemi", size=10.5, italic=True)
    # b) paralēlais LC signāla ceļā
    _rails(f, 320, 560, yt, yb)
    f.line(320, yt, 560, yt, color="white", w=3)
    f.line(320, yt, 360, yt); _dot(f, 360, yt)
    f.line(360, yt - 20, 360, yt + 20); f.line(450, yt - 20, 450, yt + 20)
    _ind_h(f, 360, 450, yt - 20, n=3); _cap_h(f, 360, 450, yt + 20)
    _dot(f, 450, yt); f.line(450, yt, 560, yt)
    _dot(f, 510, yt); _dot(f, 510, yb)
    _res_v(f, 510, yt, yb, dash="4 3")
    f.text(440, yb + 24, "paralēlais kontūrs signāla ceļā", size=10.5, italic=True)
    _curve(f, 620, yb, 220, 100, "bs")
    f.text(450, 462, "Raustītā līnija — slodze (nākamā pakāpe vai uztvērējs)", size=10.5, italic=True, color=MG)
    f.save("atteli/10-3-bpf-bsf.svg", "Joslas filtrs un sprostfiltrs: shēmas un raksturlīknes")


# ---------------------------------------------------------------- 10.5.
def f10_5():
    f = Fig(640, 320)
    T, R, B, L = (300, 60), (380, 150), (300, 240), (220, 150)
    _diode_seg(f, T, R); _diode_seg(f, B, R)
    _diode_seg(f, L, T); _diode_seg(f, L, B)
    for p in (T, R, B, L):
        _dot(f, *p)
    f.text(352, 92, "D1", size=12, italic=True, anchor="start"); f.text(352, 220, "D2", size=12, italic=True, anchor="start")
    f.text(248, 92, "D3", size=12, italic=True, anchor="end"); f.text(248, 220, "D4", size=12, italic=True, anchor="end")
    # maiņsprieguma avots
    f.circ(100, 150, 24)
    f.sine(84, 150, 32, 7, 1, w=1.8)
    f.pl([(100, 126), (100, 30), (300, 30), T])
    f.pl([(100, 174), (100, 270), (300, 270), B])
    f.mtext(100, 205 + 0, "", size=11)
    f.text(56, 154, "~", size=18, anchor="end")
    f.mtext(60, 300, "maiņspriegums\nno transformatora", size=10.5, italic=True)
    # izeja un slodze
    f.line(R[0], R[1], 520, R[1])
    f.pl([L, (220, 300), (520, 300)])
    _dot(f, 520, 150); _dot(f, 520, 300)
    _res_v(f, 560, 150, 300, label="slodze")
    f.line(520, 150, 560, 150); f.line(520, 300, 560, 300)
    f.text(498, 140, "+", size=16, bold=True); f.text(498, 318, "−", size=16, bold=True)
    # izejas forma
    xw, yw = 420, 205
    pts = [(xw + k * 0.5, yw - 26 * abs(math.sin(math.pi * k / 40))) for k in range(161)]
    f.line(xw, yw, xw + 80, yw, w=0.6, color=MG)
    f.pl(pts, w=1.8, color=BLUE)
    f.mtext(460, 236, "pulsējošs\nlīdzspriegums", size=10.5, italic=True)
    f.save("atteli/10-5-diozu-tilts.svg", "Taisngriezis ar diožu tiltu")


# ---------------------------------------------------------------- 10.6.
def f10_6():
    f = Fig(640, 330)
    yt, yg = 80, 280
    # ieeja
    _term(f, 60, yt); _term(f, 60, yg)
    f.rich(52, yt + 5, [("+U", 0), ("ie", 1)], anchor="end", size=12)
    f.line(60, yt, 232, yt)
    # tranzistors virknē (pagriezts): bāze uz leju
    cx, cy = 260, 98
    f.circ(cx, cy, 22)
    f.line(248, 110, 272, 110, w=2.6)
    f.pl([(252, 110), (238, 92), (238, yt)])
    f.arrow(268, 110, 282, 92, w=1.5, head=8)
    f.pl([(282, 92), (282, yt), (470, yt)])
    f.line(232, yt, 238, yt)
    f.text(cx, cy - 30, "Q", size=12, italic=True)
    # bāzes ķēde
    f.line(260, 110, 260, 170)
    _dot(f, 150, yt)
    _res_v(f, 150, yt, 170, label="Rv")
    f.line(150, 170, 260, 170); _dot(f, 260, 170)
    # Zenera diode: katods augšā
    _diode_seg(f, (260, yg), (260, 170), kind="zener")
    f.text(278, 230, "Dz", size=12, italic=True, anchor="start")
    f.arrow(222, 186, 222, 262, w=1.4, color=BLUE, head=7)
    f.rich(214, 228, [("U", 0), ("z", 1)], anchor="end", size=12, color=BLUE)
    # izeja un slodze
    _dot(f, 420, yt); _dot(f, 420, yg)
    _term(f, 470, yt); _term(f, 470, yg)
    f.rich(478, yt + 5, [("+U", 0), ("iz", 1)], anchor="start", size=12)
    _res_v(f, 420, yt, yg, label="slodze")
    f.arrow(380, 96, 380, 264, w=1.4, color=BLUE, head=7)
    f.rich(372, 186, [("U", 0), ("iz", 1)], anchor="end", size=12, color=BLUE)
    # zeme
    f.line(60, yg, 470, yg)
    _dot(f, 260, yg)
    f.rich(320, 322, [("U", 0), ("iz", 1), (" ≈ U", 0), ("z", 1),
                      (" − 0,7 V: izejas spriegumu nosaka Zenera diode", 0)], size=11, italic=True)
    f.save("atteli/10-6-stabilizators.svg", "Sprieguma stabilizators ar Zenera diodi un tranzistoru")


# ---------------------------------------------------------------- 10.8.
def _amp_panel(f, ox, title, tank):
    f.text(ox + 200, 24, title, bold=True, size=13)
    yr, yg = 54, 300
    f.line(ox + 110, yr, ox + 330, yr, w=2)
    f.text(ox + 336, yr + 5, "+U", anchor="start", size=12, bold=True)
    Bp, Cp, Ep = _q(f, ox + 220, 180)
    xr = ox + 140
    _res_v(f, xr, yr, 180, label="R1"); _res_v(f, xr, 180, yg, label="R2")
    _dot(f, xr, 180); f.line(xr, 180, Bp[0], 180)
    # ieeja
    _term(f, ox + 40, 180); _cap_h(f, ox + 44, xr, 180)
    f.text(ox + 40, 166, "ieeja", size=11)
    # kolektora slodze
    xc = Cp[0]
    if tank:
        y1, y2 = 72, 120
        f.line(xc, yr, xc, y1); f.line(xc - 16, y1, xc + 16, y1); f.line(xc - 16, y2, xc + 16, y2)
        _ind_v(f, xc - 16, y1, y2, n=3, r=6); _cap_v(f, xc + 16, y1, y2)
        f.line(xc, y2, xc, Cp[1])
        f.text(xc + 30, 100, "LC", anchor="start", size=12, italic=True)
    else:
        _res_v(f, xc, yr, Cp[1] - 6, label="RC", L=36); f.line(xc, Cp[1] - 6, xc, Cp[1])
    _dot(f, xc, 136)
    _cap_h(f, xc, ox + 330, 136); _term(f, ox + 334, 136)
    f.text(ox + 334, 122, "izeja", size=11)
    _res_v(f, xc, Ep[1], yg, label="RE")
    f.line(xr, yg, xc, yg)
    _dot(f, xc, yg)
    f.ground(ox + 190, yg, stem=6)


def f10_8():
    f = Fig(820, 360)
    _amp_panel(f, 0, "Platjoslas pastiprinātājs", False)
    _amp_panel(f, 420, "Rezonanses (joslas) pastiprinātājs", True)
    f.line(410, 20, 410, 330, dash="3 5", w=1, color=MG)
    f.mtext(200, 345, "kolektorā rezistors: pastiprina plašu joslu", size=10.5, italic=True)
    f.mtext(620, 345, "kolektorā LC kontūrs: pastiprina tikai rezonanses frekvenci", size=10.5, italic=True)
    f.save("atteli/10-9-pastiprinataju-veidi.svg", "Platjoslas un rezonanses pastiprinātājs")


# ---------------------------------------------------------------- 10.10.
def f10_10():
    f = Fig(700, 380)
    yr, yg = 40, 330
    f.line(150, yr, 600, yr, w=2); f.text(606, yr + 5, "+U", anchor="start", size=12, bold=True)
    B1, C1, E1 = _q(f, 200, 262, mirror=True)
    B2, C2, E2 = _q(f, 520, 262)
    # kolektoru rezistori
    _res_v(f, C1[0], yr, C1[1], label="R1")
    _res_v(f, C2[0], yr, C2[1], label="R4")
    # bāzu rezistori
    _res_v(f, 280, yr, 170, label="R2"); f.pl([(280, 170), (280, 262), B1])
    _res_v(f, 440, yr, 170, label="R3"); f.pl([(440, 170), (440, 262), B2])
    for x in (C1[0], C2[0]):
        _dot(f, x, 196)
    for x in (280, 440):
        _dot(f, x, 262)
        _dot(f, x, yr)
    _dot(f, C1[0], yr); _dot(f, C2[0], yr)
    # krusteniskie kondensatori
    f.line(C1[0], 196, 330, 196); f.capacitor(334, 196); f.pl([(338, 196), (350, 196), (440, 262)])
    f.line(C2[0], 196, 390, 196); f.capacitor(386, 196); f.pl([(382, 196), (370, 196), (280, 262)])
    f.text(334, 182, "C1", size=12, italic=True); f.text(386, 182, "C2", size=12, italic=True)
    # zeme
    f.line(150, yg, 600, yg, w=2); f.text(606, yg + 5, "0 V", anchor="start", size=12)
    f.line(E1[0], E1[1], E1[0], yg); f.line(E2[0], E2[1], E2[0], yg)
    _dot(f, E1[0], yg); _dot(f, E2[0], yg)
    f.text(150, 266, "Q1", size=12, italic=True); f.text(566, 266, "Q2", size=12, italic=True, anchor="start")
    # izeja
    f.line(C2[0], 196, 620, 196); _term(f, 624, 196)
    f.text(624, 182, "izeja", size=11)
    xw = 600
    f.pl([(xw, 250), (xw + 12, 250), (xw + 12, 226), (xw + 30, 226), (xw + 30, 250), (xw + 48, 250),
          (xw + 48, 226), (xw + 66, 226), (xw + 66, 250), (xw + 78, 250)], w=1.8, color=BLUE)
    f.mtext(640, 274, "taisnstūra\nimpulsi", size=10.5, italic=True)
    f.save("atteli/10-11-multivibrators.svg", "Multivibrators: divi tranzistori ar krustenisku saiti")


ALL = [f10_2, f10_3, f10_5, f10_6, f10_8, f10_10]
