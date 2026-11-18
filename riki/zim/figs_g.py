"""B prioritātes zīmējumi (recenzijas/trukstosie-atteli.md):
3.1., 5.1., 5.4., 6.2., 6.4., 7.3., 8.2., 10.5., 14.5., 14.7., 17.1., 17.4. attēls."""
import math
from lib import (Fig, K, G, LG, MG, RED, RED_T, BLUE, BLUE_T, GREEN, GREEN_T,
                 AMBER, AMBER_T, BRICK, BRICK_T, sym_amp, lab)
from figs_b import _groundline


def _num(f, x, y, n, color=BRICK):
    f.circ(x, y, 11, fill=color, color=color)
    f.text(x, y + 5, str(n), size=12, bold=True, color="white")


def _rbox(f, cx, cy, w, h, label, fill="white", color=K, size=12, bold=False):
    f.rect(cx - w / 2, cy - h / 2, w, h, rx=8, fill=fill, color=color, sw=1.4)
    f.mtext(cx, cy, label, size=size, bold=bold)


# ------------------------------------------------------------------ 3.1.
def f03_1():
    f = Fig(800, 340)
    rows = [(70, "Pasaule", "ITU", "Radionoteikumi:\nspektra sadale", "IARU"),
            (170, "Eiropa", "CEPT", "eksāmenu programma (ERC 32),\natļauju atzīšana", "IARU 1. reģions"),
            (270, "Latvija", "MK un ES", "MK noteikumi Nr. 257;\neksāmeni, atļaujas", "LRAL")]
    f.text(300, 24, "Regulē (saistoši)", size=13, bold=True, color=BLUE)
    f.text(640, 24, "Pārstāv radioamatierus", size=13, bold=True, color=GREEN)
    for y, lvl, org, what, rep in rows:
        f.rect(20, y - 40, 760, 80, rx=0, fill="#f7f7f8", sw=0, color="#f7f7f8")
        f.text(30, y + 5, lvl, anchor="start", size=13, bold=True, color="#555")
        f.box(220, y, 110, 46, org, size=13, bold=True, color=BLUE, tcolor=BLUE)
        f.mtext(380, y, what, size=11)
        f.box(640, y, 150, 46, rep, size=12, bold=True, color=GREEN, tcolor=GREEN)
        f.arrow(565, y + 8, 482, y + 8, w=1.2, color=GREEN, dash="4 3")
    for y in (93, 193):
        f.arrow(220, y, 220, y + 54, w=1.8, color=BLUE)
    f.text(560, y + 2, "", size=1)
    f.mtext(523, 52, "pārstāv", size=10, italic=True, color=GREEN)
    f.text(220, 334, "↓ radioamatieris ievēro MK noteikumus", size=11, italic=True)
    f.save("atteli/03-1-normativo-aktu-limeni.svg", "Kas regulē radioamatierus un kas tos pārstāv")


# ------------------------------------------------------------------ 5.4.
def f05_4():
    f = Fig(760, 380)
    f.rect(40, 20, 680, 340, rx=10, fill="white", sw=1.6)
    f.rect(40, 20, 680, 80, rx=10, fill=BRICK_T, sw=0, color=BRICK_T)
    f.line(40, 100, 720, 100, w=1, color=BRICK)
    f.text(70, 76, "YL3ABC", anchor="start", size=40, bold=True, color=BRICK)
    f.mtext(560, 60, "Operatore Anna · Rīga, Latvija\nWW lokators KO26 · ITU 29 · CQ 15", size=12)
    f.text(70, 136, "Apstiprinu sakaru ar  ON3DXY", anchor="start", size=15, bold=True)
    heads = ["Datums", "UTC", "MHz", "Veids", "RST"]
    vals = ["2026-03-14", "14:32", "21,285", "SSB", "59"]
    xs = [70, 230, 340, 460, 570, 690]
    y = 170
    f.rect(60, y - 4, 640, 64, rx=0, fill="none", sw=1.2)
    for i, (h, v) in enumerate(zip(heads, vals)):
        f.text((xs[i] + xs[i + 1]) / 2 - 6, y + 18, h, size=12, bold=True, color="#555")
        f.text((xs[i] + xs[i + 1]) / 2 - 6, y + 48, v, size=15)
        if i:
            f.line(xs[i] - 8, y - 4, xs[i] - 8, y + 60, w=1)
    f.line(60, y + 26, 700, y + 26, w=1)
    f.text(70, 270, "☐ PSE QSL   ☒ TNX QSL", anchor="start", size=13)
    f.text(70, 300, "Transīvers 100 W, dipols", anchor="start", size=12, italic=True)
    f.text(690, 300, "73!", anchor="end", size=22, bold=True, color=BRICK)
    f.text(380, 345, "Parauga kartīte 5.5. un 5.6. apakšnodaļas piemēram; stacija ir izdomāta", size=11, italic=True, color="#555")
    f.save("atteli/05-4-qsl-kartite.svg", "QSL kartītes paraugs")


# ------------------------------------------------------------------ 6.2. un 6.4.
def _band(f, fx, segs, yb1=92, yb2=130):
    for a, b, fill, label in segs:
        f.rect(fx(a), yb1, fx(b) - fx(a), yb2 - yb1, fill=fill, rx=0, sw=1.2)
        if label:
            f.mtext((fx(a) + fx(b)) / 2, (yb1 + yb2) / 2, label, size=11, bold=True)


def f06_2():
    f = Fig(800, 280)
    fx = lambda k: 80 + (k - 7000) * 3.3
    yb1, yb2 = 92, 130
    _band(f, fx, [(7000, 7040, BLUE_T, "CW"), (7040, 7060, AMBER_T, ""), (7060, 7200, GREEN_T, "visi veidi, arī SSB")])
    f.line(fx(7010), 66, fx(7080), 66, w=3.5, color=BRICK)
    for x in (fx(7010), fx(7080)):
        f.line(x, 58, x, 74, w=2, color=BRICK)
        f.line(x, 74, x, yb2, dash="3 3", w=1)
    f.text((fx(7010) + fx(7080)) / 2, 52, "B kategorijai: 7010–7080 kHz, tikai CW un MGM", size=12, bold=True,
           color=BRICK)
    for k in range(7000, 7201, 20):
        f.line(fx(k), yb2, fx(k), yb2 + 6, w=1)
        f.text(fx(k), yb2 + 22, str(k), size=11)
    f.text(fx(7200), yb2 + 40, "kHz", anchor="end", size=11, italic=True)
    xd = fx(7050)
    f.line(xd, yb2 + 26, xd, 178, w=0.9, color=AMBER)
    xf = fx(7074)
    f.ltext(xf - 12, 192, "šaurjoslas un ciparu darba veidi", anchor="end", size=11, color=AMBER, bold=True)
    f.line(xf, yb2 + 26, xf, 214, dash="2 3", w=1, color=AMBER)
    f.text(xf, 230, "FT8 7074 kHz", size=11, italic=True, color=AMBER)
    f.mtext(fx(7140), 262, "SSB B kategorijai 40 m diapazonā nav atļauts", size=12, bold=True)
    f.save("atteli/06-2-40m-josla.svg", "40 m diapazons: joslu plāns un B kategorijas robežas")


def f06_4():
    f = Fig(800, 300)
    fx = lambda m: 60 + (m - 144.0) * 340
    yb1, yb2 = 100, 150
    segs = [(144.0, 144.4, BLUE_T, "CW, SSB\nvāji signāli"), (144.4, 144.5, "#d9d9d9", ""),
            (144.5, 145.0, AMBER_T, "visi veidi,\nciparu"), (145.0, 145.2, "#eeeeee", "atkārt.\nieejas"),
            (145.2, 145.6, GREEN_T, "FM tiešie sakari"), (145.6, 145.8, "#eeeeee", "atkārt.\nizejas"),
            (145.8, 146.0, "#e4e4e4", "satelīti")]
    _band(f, fx, segs, yb1, yb2)
    f.text((fx(144.4) + fx(144.5)) / 2, yb1 - 8, "bākas", size=10, italic=True)
    f.line(fx(144.0), 72, fx(146.0), 72, w=3.5, color=BRICK)
    for x in (fx(144.0), fx(146.0)):
        f.line(x, 64, x, 80, w=2, color=BRICK)
    f.text((fx(144) + fx(146)) / 2, 58, "B kategorijai visa josla 144–146 MHz, līdz 50 W", size=12, bold=True,
           color=BRICK)
    for m in (144.0, 144.5, 145.0, 145.5, 146.0):
        f.line(fx(m), yb2, fx(m), yb2 + 6, w=1)
        f.text(fx(m), yb2 + 22, f"{m:.3f}".replace(".", ","), size=11)
    f.text(fx(146.0), yb2 + 40, "MHz", anchor="end", size=11, italic=True)
    marks = [(145.050, "145,050: atkārtotāja ieeja", 196, K), (145.500, "145,500: FM izsaukuma frekvence", 226, GREEN),
             (145.650, "145,650: atkārtotāja izeja", 256, K)]
    for m, t, y, c in marks:
        f.line(fx(m), yb2 + 26, fx(m), y - 14, dash="2 3", w=1, color=c)
        f.text(fx(m), y, t, size=11, bold=(c == GREEN), color=c, anchor="end" if m > 145.4 else "middle")
    f.save("atteli/06-4-2m-josla.svg", "2 m diapazons: vienkāršots joslu plāns")


# ------------------------------------------------------------------ 7.3.
def f07_3():
    f = Fig(520, 220)
    ax, ay, bx, by, cx, cy = 130, 30, 30, 190, 230, 190
    f.pl([(ax, ay), (bx, by), (cx, cy)], close=True, fill=AMBER_T, w=2, color=AMBER)
    my = 118
    lx = bx + (ax - bx) * (by - my) / (by - ay)
    rx = cx - (cx - ax) * (cy - my) / (cy - ay)
    f.line(lx, my, rx, my, color=AMBER); f.line(130, my, 130, by, color=AMBER)
    f.text(130, 96, "P", size=30, bold=True)
    f.text(92, 170, "U", size=30, bold=True)
    f.text(168, 170, "I", size=30, bold=True)
    f.text(300, 70, "P = U · I", anchor="start", size=17)
    f.text(300, 118, "U = P / I", anchor="start", size=17)
    f.text(300, 166, "I = P / U", anchor="start", size=17)
    f.text(300, 200, "tāpat kā Oma likuma trijstūris", anchor="start", size=11, italic=True)
    f.save("atteli/07-3-jaudas-trijsturis.svg", "Jaudas trijstūris")


# ------------------------------------------------------------------ 8.2.
def f08_2():
    """Viļņa garums mērogā (A) un pusviļņa dipola elektriskais un fiziskais garums (B)."""
    f = Fig(780, 510)
    s = 12.0                      # pikseļi uz metru (abās daļās viens mērogs)
    x0 = 120
    span = 50 * s                 # 0…50 m

    # ---------- A. Viļņa garums ----------
    f.text(20, 24, "A. Viļņa garums — attālums starp diviem blakus maksimumiem",
           anchor="start", size=13, bold=True)
    for fr, band, yc, col in ((7, "40 m diapazons", 82, BLUE), (14, "20 m diapazons", 172, RED)):
        lam = 300 / fr
        lp = lam * s
        f.sine(x0, yc, span, 24, span / lp, phase=math.pi / 2, w=2.2, n=600, color=col)
        f.text(x0 - 14, yc - 2, f"{fr} MHz", anchor="end", size=13, bold=True, color=col)
        f.text(x0 - 14, yc + 14, band, anchor="end", size=10, color=MG)
        yd = yc + 40
        for xc in (x0, x0 + lp):
            f.circ(xc, yc - 24, 3.5, fill=col, color=col)
            f.line(xc, yc - 20, xc, yd + 4, dash="3 3", w=1, color=col)
        f.darrow(x0, yd, x0 + lp, yd, color=col)
        f.ltext(x0 + lp / 2, yd + 5, f"λ ≈ {lam:.0f} m", size=12, bold=True, color=col)
    f.text(x0 + span, 236, "frekvence 2 × augstāka → vilnis 2 × īsāks",
           anchor="end", size=11, italic=True)
    # mērogs metros
    yr = 262
    f.line(x0, yr, x0 + span, yr, w=1.2)
    for m in range(0, 51, 10):
        x = x0 + m * s
        f.line(x, yr - 5, x, yr + 5, w=1.2)
        f.text(x, yr + 20, f"{m} m" if m == 50 else str(m), size=11)
    for m in range(5, 50, 10):
        f.line(x0 + m * s, yr - 3, x0 + m * s, yr + 3, w=1)

    # ---------- B. Antenas garums ----------
    f.line(20, 300, 760, 300, w=0.7, color=MG)
    f.text(20, 326, "B. Pusviļņa dipols 7 MHz frekvencei", anchor="start", size=13, bold=True)
    half = 300 / 7 / 2 * s        # λ/2 pikseļos
    xa = x0
    xb = xa + half
    cx = (xa + xb) / 2
    yw = 382
    # puse viļņa (tas pats 7 MHz vilnis, tikai puse no tā)
    f.sine(xa, yw, half, 26, 0.5, w=2.2, n=200, color=BLUE)
    f.text(cx, yw - 34, "puse viļņa", size=11, italic=True, color=BLUE)
    # elektriskais garums
    ye = yw + 22
    for x in (xa, xb):
        f.line(x, yw, x, 486, dash="3 3", w=1, color=BLUE)
    f.darrow(xa, ye, xb, ye, color=BLUE)
    f.ltext(cx, ye + 5, "λ/2 ≈ 21,4 m", size=12, bold=True, color=BLUE)
    # dipola vads (fiziskais garums = 0,95 · λ/2)
    phys = 0.95 * half
    yd = 470
    gap = 5
    f.line(cx - phys / 2, yd, cx - gap, yd, w=3.2)
    f.line(cx + gap, yd, cx + phys / 2, yd, w=3.2)
    for x in (cx - gap, cx + gap):
        f.circ(x, yd, 2.6, fill=K)
    for x in (cx - phys / 2, cx + phys / 2):
        f.circ(x, yd, 3.2, fill="white")
    f.line(cx - gap, yd, cx - 2, yd + 16, w=1.4)
    f.line(cx + gap, yd, cx + 2, yd + 16, w=1.4)
    f.line(cx, yd + 16, cx, yd + 26, w=2.4)
    f.text(cx + 8, yd + 30, "pievads", anchor="start", size=10, color=MG)
    # fiziskais garums
    yp = yd - 24
    for x in (cx - phys / 2, cx + phys / 2):
        f.line(x, yd - 4, x, yp - 4, w=1, color=K)
    f.darrow(cx - phys / 2, yp, cx + phys / 2, yp, color=K)
    f.ltext(cx, yp + 5, "vads ≈ 20,3 m", size=12, bold=True)
    # skaidrojumi pa labi
    xt = xb + 40
    f.text(xt, ye - 4, "Elektriskais garums", anchor="start", size=12, bold=True, color=BLUE)
    f.text(xt, ye + 12, "cik viļņa garumu antenā ietilpst: λ/2", anchor="start", size=11)
    f.text(xt, yp + 2, "Fiziskais garums", anchor="start", size=12, bold=True)
    f.text(xt, yp + 18, "vada garums metros, ko nomēra ar mērlenti;", anchor="start", size=11)
    f.text(xt, yp + 34, "ap 5 % īsāks: L ≈ 0,95 · λ/2", anchor="start", size=11)
    f.save("atteli/08-2-vilna-garums.svg", "Viļņa garums; antenas elektriskais un fiziskais garums")


# ------------------------------------------------------------------ 10.5.
def f10_5():
    f = Fig(760, 300)
    y = 120
    sym_amp(f, 330, y)
    lab(f, 330, y - 40, "Pastiprinātājs")
    f.line(352, y, 470, y)
    f.circ(430, y, 3.5, fill=K)
    f.arrow(470, y, 520, y)
    f.sine(530, y, 150, 22, 3, w=2.2, color=BLUE)
    f.text(605, y + 46, "izeja: maiņspriegums", size=11)
    # atgriezeniskā saite
    f.pl([(430, y), (430, 220), (380, 220)], w=1.6, color=GREEN)
    f.box(330, 220, 100, 44, "LC kontūrs\nvai kvarcs", size=11, color=GREEN)
    f.pl([(280, 220), (240, 220), (240, y), (308, y)], w=1.6, color=GREEN)
    f.arrow(250, y, 307, y, w=1.6, color=GREEN)
    f.text(330, 272, "pozitīvā atgriezeniskā saite: daļa izejas atpakaļ uz ieeju", size=11, italic=True,
           color=GREEN)
    f.text(330, 290, "kontūrs vai kvarcs nosaka frekvenci", size=11, italic=True, color=GREEN)
    f.arrow(330, 40, 330, 98, w=1.6, color=AMBER)
    f.text(330, 30, "barošana (līdzspriegums)", size=11, color=AMBER)
    f.save("atteli/10-9-generators.svg", "Ģenerators: pastiprinātājs ar atgriezenisko saiti")


# ------------------------------------------------------------------ 14.5.
def f14_5():
    f = Fig(780, 300)
    x0, y0, W, H = 70, 240, 660, 180
    y1, y2 = 2008, 2032
    fx = lambda yr: x0 + W * (yr - y1) / (y2 - y1)
    f.axes(x0, y0, W + 14, H + 14)
    f.text(x0 - 8, y0 - H - 18, "Saules plankumu skaits", anchor="start", size=11, italic=True)
    for yr in range(2008, 2033, 4):
        f.line(fx(yr), y0, fx(yr), y0 + 5, w=1)
        f.text(fx(yr), y0 + 20, str(yr), size=11)
    def s(t):
        # stilizēts ~11 gadu cikls ar minimumiem 2008,8 un 2019,9
        ph = (t - 2008.8) / 11.1
        return max(0.0, math.sin(math.pi * (ph % 1)) ** 2) * (0.75 if ph < 1 else 1.0)
    pts = [(fx(y1 + (y2 - y1) * i / 300), y0 - H * 0.9 * s(y1 + (y2 - y1) * i / 300)) for i in range(301)]
    f.pl(pts + [(x0 + W, y0), (x0, y0)], close=True, fill=AMBER_T, w=0, color=AMBER_T)
    f.pl(pts, w=2.4, color=AMBER)
    for yr, t in ((2014.3, "maksimums"), (2025.4, "maksimums")):
        f.text(fx(yr), y0 - H * 0.9 * s(yr) - 10, t, size=11, bold=True, color=AMBER)
    for yr in (2008.8, 2019.9, 2031.0):
        f.text(fx(yr), y0 - 10, "minimums", size=10, italic=True)
    f.darrow(fx(2008.8), y0 - H - 4, fx(2019.9), y0 - H - 4, color=K)
    f.text((fx(2008.8) + fx(2019.9)) / 2, y0 - H - 12, "ap 11 gadi", size=11, bold=True)
    f.text(x0 + W, 290, "shematiski, ne mērījumu dati", anchor="end", size=10, italic=True, color="#555")
    f.text(x0, 290, "maksimuma gados atvērti 10 m un 15 m", anchor="start", size=11, color=AMBER)
    f.save("atteli/14-5-saules-cikls.svg", "Saules aktivitātes cikls (shematiski)")


# ------------------------------------------------------------------ 14.7.
def f14_7():
    f = Fig(780, 260)
    cx, cy, R = 390, 830, 700
    arc = [(cx + R * math.sin(a), cy - R * math.cos(a)) for a in [(-0.56 + 1.12 * i / 200) for i in range(201)]]
    f.pl(arc + [(arc[-1][0], 260), (arc[0][0], 260)], close=True, fill=GREEN_T, w=0, color=GREEN_T)
    f.pl(arc, w=1.8, color=GREEN)
    def surf(a):
        return cx + R * math.sin(a), cy - R * math.cos(a)
    h1, h2 = 90, 45
    th1 = math.acos(R / (R + h1)); th2 = math.acos(R / (R + h2))
    a1 = -0.44
    a2 = a1 + th1 + th2   # abu antenu stari pieskaras Zemei vienā punktā
    (x1, y1), (x2, y2) = surf(a1), surf(a2)
    t1 = (x1 + h1 * math.sin(a1), y1 - h1 * math.cos(a1))
    t2 = (x2 + h2 * math.sin(a2), y2 - h2 * math.cos(a2))
    f.line(x1, y1, *t1, w=3); f.line(x2, y2, *t2, w=3)
    f.text(t1[0], t1[1] - 10, "h₁ = 16 m", size=12, bold=True)
    f.text(t2[0], t2[1] - 10, "h₂ = 4 m", size=12, bold=True)
    # pieskares punkti
    p1 = p2 = surf(a1 + th1)
    f.line(*t1, *t2, w=1.6, color=BLUE, dash="6 4")
    f.circ(p1[0], p1[1], 3.5, fill=BLUE, color=BLUE)
    f.text((t1[0] + p1[0]) / 2, (t1[1] + p1[1]) / 2 - 12, "d₁", size=13, italic=True, color=BLUE)
    f.text((t2[0] + p2[0]) / 2, (t2[1] + p2[1]) / 2 - 12, "d₂", size=13, italic=True, color=BLUE)
    f.text(p1[0], p1[1] - 12, "radio horizonts", size=11, italic=True, color=BLUE)
    f.mtext(cx, 40, "d ≈ 4,12 · (√h₁ + √h₂) = 4,12 · (4 + 2) ≈ 25 km", size=14, bold=True)
    f.text(cx, 64, "augstāka antena redz tālāk; jauda šeit nepalīdz", size=11, italic=True)
    f.save("atteli/14-7-radiohorizonts.svg", "Radio horizonts VHF un UHF sakariem")


# ------------------------------------------------------------------ 17.1.
def _person(f, cx, ytop):
    f.circ(cx, ytop + 20, 18, fill="white", sw=1.8)
    f.path(f"M {cx - 30} {ytop + 52} L {cx + 30} {ytop + 52} L {cx + 26} {ytop + 150} L {cx - 26} {ytop + 150} Z",
           fill="white", w=1.8)
    f.line(cx - 30, ytop + 54, cx - 78, ytop + 120, w=8, color="#cfcfcf")
    f.line(cx + 30, ytop + 54, cx + 78, ytop + 120, w=8, color="#cfcfcf")
    f.line(cx - 14, ytop + 150, cx - 22, ytop + 240, w=9, color="#cfcfcf")
    f.line(cx + 14, ytop + 150, cx + 22, ytop + 240, w=9, color="#cfcfcf")
    # sirds
    hx, hy = cx - 8, ytop + 82
    f.path(f"M {hx} {hy + 10} C {hx - 14} {hy}, {hx - 8} {hy - 12}, {hx} {hy - 4} "
           f"C {hx + 8} {hy - 12}, {hx + 14} {hy}, {hx} {hy + 10} Z", fill=RED, w=1, color=RED)


def f17_1():
    f = Fig(760, 330)
    for cx, title in ((200, "roka — roka"), (560, "roka — kājas")):
        f.text(cx, 24, title, size=14, bold=True)
        _person(f, cx, 50)
    # roka — roka
    f.path("M 122 170 C 160 120, 180 128, 192 132 C 220 128, 240 120, 278 170", w=3.5, color=RED)
    f.arrow(268, 157, 279, 171, w=3, color=RED)
    # roka — kājas
    f.path("M 482 170 C 520 120, 540 126, 552 132 C 560 170, 558 220, 548 290", w=3.5, color=RED)
    f.path("M 552 200 C 560 230, 568 260, 582 290", w=3.5, color=RED)
    f.arrow(549, 280, 547, 291, w=3, color=RED); f.arrow(578, 280, 582, 291, w=3, color=RED)
    f.mtext(380, 312, "Abos ceļos strāva iet caur krūškurvi un sirdi — tāpēc tie ir visbīstamākie",
            size=12, bold=True, color=RED)
    f.save("atteli/17-1-stravas-cels.svg", "Strāvas ceļš caur cilvēka ķermeni")


# ------------------------------------------------------------------ 17.4.
def f17_4():
    f = Fig(860, 330)
    yg = 280
    _groundline(f, 20, 840, yg)
    # māja
    f.pl([(300, yg), (300, 150), (430, 80), (560, 150), (560, yg)], w=1.8)
    f.box(470, 240, 100, 40, "Transīvers", size=11)
    # antena un masts
    xa = 160
    f.line(xa, yg, xa, 70, w=3)
    f.line(xa - 70, 70, xa + 70, 70, w=2.6)
    # zibens
    f.pl([(110, 10), (96, 40), (112, 40), (98, 66)], w=3, color=AMBER)
    # kabelis ar izlādni pie ieejas mājā
    f.pl([(xa, 90), (250, 90), (250, 200), (300, 200)], w=2.2)
    f.box(250, 214, 46, 26, "", size=10, color=AMBER)
    f.text(250, 219, "Z", size=12, bold=True, color=AMBER)
    f.line(250, 227, 250, yg + 20, w=2, color=GREEN)
    for i, hw in enumerate((14, 9, 4)):
        f.line(250 - hw, yg + 20 + i * 5, 250 + hw, yg + 20 + i * 5, w=2, color=GREEN)
    f.text(250, yg + 46, "zemējums ārpus mājas", size=11, color=GREEN)
    f.mtext(194, 236, "zibens\nizlādnis", size=10, color=AMBER)
    # atvienotais savienotājs
    f.line(300, 200, 380, 200, w=2.2)
    f.line(380, 200, 400, 186, w=2.2)
    f.circ(380, 200, 3, fill=K)
    f.line(412, 200, 470, 200, w=2.2); f.line(470, 200, 470, 220, w=2.2)
    f.circ(412, 200, 3, fill=K)
    f.text(396, 176, "atvienots", size=11, bold=True, color=RED)
    # soļi
    steps = ["1. Beidz raidīt.", "2. Atvieno antenas kabeli no transīvera;",
             "   ja var — savieno ar zemējumu ārpus mājas.", "3. Atvieno iekārtas no elektrotīkla."]
    f.text(590, 110, "Tuvojoties negaisam:", anchor="start", size=12, bold=True)
    for i, t in enumerate(steps):
        f.text(590 + (16 if t.startswith(" ") else 0), 134 + i * 20, t.strip(), anchor="start", size=11)
    f.save("atteli/17-4-zibens.svg", "Antenas aizsardzība pret zibeni")


ALL = [f03_1, f05_4, f06_2, f06_4, f07_3, f08_2, f10_5, f14_5, f14_7, f17_1, f17_4]
