"""Papildu zīmējumi: 1., 4., 5., 6. nodaļa un starojuma diagrammas 13. nodaļā."""
import math
from xml.sax.saxutils import escape
from lib import (Fig, K, G, LG, MG, chain, tw, RED, RED_T, BLUE, BLUE_T, GREEN, GREEN_T,
                 AMBER, AMBER_T, BRICK, BRICK_T)
from figs_b import _groundline

DARK = "#333333"


def _mono(f, x, y, t, size=72):
    f.add(f'<text x="{x:.1f}" y="{y:.1f}" font-family="DejaVu Sans Mono, Courier New, monospace" '
          f'font-size="{size}" font-weight="bold" fill="{K}">{escape(t)}</text>')


def f01_1():
    f = Fig(760, 330)
    f.box(360, 170, 150, 60, "Transīvers", size=14, bold=True)
    f.box(100, 170, 120, 52, "Barošanas bloks\n13,8 V", size=11)
    f.arrow(160, 170, 285, 170)
    f.text(222, 160, "līdzstrāva", size=11, italic=True)
    f.box(600, 170, 110, 52, "SWR un jaudas\nmērītājs", size=11)
    f.line(435, 170, 545, 170, w=2.4)
    f.text(490, 160, "kabelis", size=11, italic=True)
    f.line(655, 170, 712, 170, w=2.4)
    f.antenna(712, 170, h=80)
    f.text(712, 76, "antena", size=11, italic=True)
    # dators
    f.box(170, 280, 110, 44, "Dators", size=12)
    f.pl([(225, 280), (310, 280), (310, 200)])
    f.text(302, 248, "CAT, audio", anchor="end", size=10, italic=True)
    # mikrofons
    f.box(570, 280, 170, 44, "Mikrofons,\ntelegrāfa atslēga", size=11)
    f.pl([(485, 280), (410, 280)])
    f.arrow(410, 280, 410, 201)
    # zemējums
    f.ground(360, 200, stem=34)
    f.text(360, 278, "zemējums", size=11, italic=True)
    f.save("atteli/01-1-stacija.svg", "Radioamatiera stacijas uzbūve")


def f04_1():
    f = Fig(760, 300)
    x0, y, cw = 200, 120, 43.2
    _mono(f, x0, y, "YL3ABC")
    f.add(f'<text x="{x0 + 6 * cw:.1f}" y="{y:.1f}" font-family="DejaVu Sans Mono, Courier New, monospace" '
          f'font-size="72" font-weight="bold" fill="{MG}">/P</text>')
    parts = [(0, 3, ["Prefikss", "YL un cipars", "YL — Latvija"], None),
             (3, 6, ["Sufikss", "3 burti —", "B kategorija"], None),
             (6, 8, ["Papildzīme", "/P — portatīva", "(nav obligāta)"], "5 4")]
    for a, b, labs, dash in parts:
        xa, xb = x0 + a * cw + 4, x0 + b * cw - 4
        f.pl([(xa, y + 14), (xa, y + 24), (xb, y + 24), (xb, y + 14)], w=1.6, dash=dash)
        xm = (xa + xb) / 2
        f.line(xm, y + 24, xm, y + 34, w=1.6, dash=dash)
        for i, t in enumerate(labs):
            f.text(xm, y + 56 + i * 18, t, size=13 if i == 0 else 12, bold=(i == 0))
    f.text(380, 270, "YL2AB — A kategorija    ·    YL3ABC — B kategorija    ·    YL3ABCD — C kategorija", size=13)
    f.save("atteli/04-1-izsaukuma-signals.svg", "Izsaukuma signāla uzbūve")


def f04_2():
    f = Fig(800, 445)
    rows = [("80 m", 3500, 3800, 3510, 3750, "3510–3750 kHz", "100 W", ""),
            ("40 m", 7000, 7200, 7010, 7080, "7010–7080 kHz", "100 W", "tikai CW, MGM"),
            ("15 m", 21000, 21450, 21000, 21450, "21 000–21 450 kHz", "100 W", ""),
            ("10 m", 28000, 29700, 28000, 29700, "28 000–29 700 kHz", "100 W", ""),
            ("6 m", 50, 52, 50, 52, "50–52 MHz", "100 W", ""),
            ("2 m", 144, 146, 144, 146, "144–146 MHz", "50 W", ""),
            ("70 cm", 430, 440, 430, 440, "430–440 MHz", "20 W", ""),
            ("23 cm", 1240, 1300, 1240, 1300, "1240–1300 MHz", "10 W", "")]
    X0, W = 110, 440
    f.text(70, 34, "Diapazons", size=12, bold=True)
    f.text(X0 + W / 2, 34, "Radioamatieru josla un B kategorijai atļautā daļa", size=12, bold=True)
    f.text(590, 34, "Atļauts", anchor="start", size=12, bold=True)
    f.text(770, 34, "Jauda", anchor="end", size=12, bold=True)
    for i, (name, lo, hi, blo, bhi, rng, pw, note) in enumerate(rows):
        y = 70 + i * 40
        f.text(90, y + 5, name, anchor="end", size=13, bold=True)
        f.rect(X0, y - 8, W, 16, fill=LG, rx=0, sw=1)
        xa = X0 + W * (blo - lo) / (hi - lo)
        xb = X0 + W * (bhi - lo) / (hi - lo)
        f.rect(xa, y - 8, xb - xa, 16, fill=GREEN, rx=0, sw=1, color=GREEN)
        unit = "kHz" if lo > 1000 and lo < 100000 else "MHz"
        fmt = lambda v: f"{v:,}".replace(",", " ")
        f.text(X0, y + 22, fmt(lo), anchor="start", size=9, color="#555")
        f.text(X0 + W, y + 22, fmt(hi), anchor="end", size=9, color="#555")
        if note:
            f.text(xb + 8, y + 4, note, anchor="start", size=11, italic=True)
        f.text(590, y + 5, rng, anchor="start", size=12)
        f.text(770, y + 5, pw, anchor="end", size=13, bold=True)
    yl = 70 + 8 * 40 + 6
    f.rect(X0, yl - 8, 24, 12, fill=LG, rx=0, sw=1)
    f.text(X0 + 30, yl + 2, "radioamatieru josla", anchor="start", size=11)
    f.rect(X0 + 190, yl - 8, 24, 12, fill=GREEN, rx=0, sw=1, color=GREEN)
    f.text(X0 + 220, yl + 2, "atļauts B kategorijai", anchor="start", size=11)
    f.text(X0, yl + 32, "B kategorijai nav atļauti diapazoni 160 m, 30 m, 20 m, 17 m un 12 m.", anchor="start",
           size=12, italic=True)
    f.save("atteli/04-2-b-kategorijas-joslas.svg", "B kategorijas joslas un jaudas")


def f05_1():
    f = Fig(760, 440)
    xa, xb = 210, 590
    phases = [(75, 125, "1. Izsaukums"), (135, 185, "2. Atbilde"), (195, 295, "3. Apmaiņa"), (305, 405, "4. Noslēgums")]
    for i, (y1, y2, lab) in enumerate(phases):
        f.rect(10, y1, 740, y2 - y1, fill=LG if i % 2 == 0 else "#f6f6f6", rx=0, sw=0)
        f.text(20, (y1 + y2) / 2 + 5, lab, anchor="start", size=12, bold=True)
    for x, name in ((xa, "YL3ABC"), (xb, "ON3DXY")):
        f.box(x, 40, 110, 34, name, size=13, bold=True)
        f.line(x, 57, x, 420, dash="5 4", w=1.2, color=MG)
    msgs = [(108, 1, "CQ CQ CQ, this is YL3ABC"),
            (168, -1, "YL3ABC, this is ON3DXY"),
            (232, 1, "five nine · name Anna · QTH Riga · over"),
            (278, -1, "five seven · name Mark · QTH Brussels · over"),
            (342, 1, "thanks, 73 · ON3DXY this is YL3ABC, clear"),
            (388, -1, "73 · YL3ABC this is ON3DXY, clear")]
    for y, d, t in msgs:
        if d > 0:
            f.arrow(xa, y, xb, y, w=1.6)
        else:
            f.arrow(xb, y, xa, y, w=1.6)
        f.text((xa + xb) / 2, y - 7, t, size=12, italic=True)
    f.text(xb + 70, 254, "signāla ziņojums,", anchor="start", size=10)
    f.text(xb + 70, 267, "vārds, QTH", anchor="start", size=10)
    f.save("atteli/05-2-qso-uzbuve.svg", "QSO četras daļas")


def f05_2():
    f = Fig(780, 290)
    y = 190
    fx = lambda k: 100 + (k - 21290) * 30
    f.arrow(60, y, 750, y, w=1.4)
    f.text(750, y + 18, "f", anchor="end", italic=True)
    for k in (21290, 21295, 21300, 21305, 21310):
        f.line(fx(k), y, fx(k), y + 6, w=1.2)
        f.text(fx(k), y + 22, f"{k / 1000:.3f}".replace(".", ","), size=11)
    f.text(405, y + 42, "MHz", size=11, italic=True)
    # DX stacija
    xd = fx(21295)
    f.rect(xd - 10, y - 90, 20, 90, fill=RED, rx=0, sw=1, color=RED)
    f.text(xd - 18, y - 76, "DX stacija raida", anchor="end", size=12, bold=True, color=RED)
    f.text(xd - 18, y - 60, "un saka “up 5”", anchor="end", size=12)
    # saucēji
    for k, h in ((21298.6, 34), (21299.4, 48), (21300.6, 40), (21301.3, 30), (21302.2, 44), (21303.0, 28)):
        f.rect(fx(k) - 5, y - h, 10, h, fill=BLUE_T, rx=0, sw=0.8, color=BLUE)
    xt = fx(21300)
    f.rect(xt - 6, y - 60, 12, 60, fill=GREEN_T, rx=0, sw=1.8, color=GREEN)
    f.pl([(fx(21298.3), y - 70), (fx(21298.3), y - 76), (fx(21303.3), y - 76), (fx(21303.3), y - 70)], w=1.4, color=BLUE)
    f.text(fx(21300.8), y - 84, "šeit DX klausās; šeit sauc visi", size=11, color=BLUE)
    f.path(f"M {xd + 10} {y - 60} C {xd + 60} {y - 150}, {xt - 40} {y - 150}, {xt - 2} {y - 96}", w=1.6, dash="5 4", color=RED)
    f.text((xd + xt) / 2, y - 140, "5 kHz augstāk", size=11, italic=True)
    f.arrow(fx(21305), y - 52, xt + 8, y - 52, w=1.4, head=7, color=GREEN)
    f.text(fx(21305) + 6, y - 48, "tu raidi 21,300 MHz", anchor="start", size=11, bold=True, color=GREEN)
    f.text(xd, y + 62, "Nekad neraidi DX stacijas raidīšanas frekvencē!", size=12, bold=True, color=RED)
    f.save("atteli/05-3-split.svg", "Darbs split režīmā")


def f05_3():
    f = Fig(780, 330)
    yg = 280
    _groundline(f, 20, 760, yg)
    f.pl([(250, yg), (390, 168), (530, yg)], close=True, fill=GREEN_T, w=1.4, color=GREEN)
    f.line(390, 168, 390, 92, w=3)
    f.antenna(390, 92, h=30)
    f.box(390, 38, 110, 26, "atkārtotājs", size=12)
    for x, lab in ((90, "stacija A"), (690, "stacija B")):
        f.rect(x - 9, yg - 40, 18, 36, fill="white", rx=3)
        f.line(x, yg - 40, x, yg - 66, w=2)
        f.text(x, yg + 22, lab, size=12, bold=True)
    f.arrow(96, yg - 70, 378, 76, w=2.0, color=BLUE)
    f.text(196, 136, "A raida 145,050 MHz", anchor="end", size=12, color=BLUE, bold=True)
    f.arrow(402, 76, 684, yg - 70, w=2.0, color=RED)
    f.mtext(588, 128, "atkārtotājs raida\n145,650 MHz", anchor="start", size=12, color=RED, bold=True)
    # tiešais ceļš, aizsegts
    f.line(100, yg - 58, 322, yg - 58, dash="5 4", w=1.2)
    f.text(330, yg - 52, "×", size=18, bold=True)
    f.text(110, yg - 66, "tiešo sakaru aizsedz pakalns", anchor="start", size=10, italic=True)
    f.text(390, 318, "nobīde 600 kHz: atkārtotājs uztver vienā frekvencē un raida citā", size=12)
    f.save("atteli/05-5-atkartotajs.svg", "Atkārtotāja darbība")


def f06_1():
    f = Fig(800, 300)
    fx = lambda k: 80 + (k - 3500) * 2.2
    yb1, yb2 = 92, 130
    segs = [(3500, 3570, BLUE_T, "CW"), (3570, 3600, AMBER_T, ""), (3600, 3800, GREEN_T, "visi veidi, arī SSB")]
    for a, b, fill, lab in segs:
        f.rect(fx(a), yb1, fx(b) - fx(a), yb2 - yb1, fill=fill, rx=0, sw=1.2)
        if lab:
            f.text((fx(a) + fx(b)) / 2, (yb1 + yb2) / 2 + 5, lab, size=12, bold=True)
    # B robežas
    f.line(fx(3510), 66, fx(3750), 66, w=3.5, color=BRICK)
    f.line(fx(3510), 58, fx(3510), 74, w=2, color=BRICK); f.line(fx(3750), 58, fx(3750), 74, w=2, color=BRICK)
    f.text((fx(3510) + fx(3750)) / 2, 52, "B kategorijai atļauts: 3510–3750 kHz", size=12, bold=True, color=BRICK)
    for x in (fx(3510), fx(3750)):
        f.line(x, 74, x, yb2, dash="3 3", w=1)
    # ass
    for k in range(3500, 3801, 50):
        f.line(fx(k), yb2, fx(k), yb2 + 6, w=1)
        f.text(fx(k), yb2 + 22, str(k), size=11)
    f.text(fx(3800), yb2 + 40, "kHz", anchor="end", size=11, italic=True)
    # šaurjoslas segments
    xd = (fx(3570) + fx(3600)) / 2
    f.line(xd, yb2 + 26, xd, 172, w=0.9, color=AMBER)
    f.ltext(xd, 186, "šaurjoslas un ciparu darba veidi (FT8 3573 kHz)", size=11, color=AMBER, bold=True)
    # YL apaļais galds
    xy = fx(3677)
    f.line(xy, yb2 + 26, xy, 258, dash="2 3", w=1)
    f.text(xy, 274, "YL apaļais galds 3677 kHz", size=11, italic=True)
    # SSB B kategorijai
    ys = 222
    f.pl([(fx(3600), ys - 6), (fx(3600), ys), (fx(3750), ys), (fx(3750), ys - 6)], w=1.8, color=GREEN)
    f.ltext((fx(3600) + fx(3750)) / 2, ys + 18, "SSB B kategorijai: 3600–3750 kHz", size=12, bold=True, color=GREEN)
    f.save("atteli/06-1-80m-josla.svg", "80 m diapazons: joslu plāns un B kategorijas robežas")


def f06_2():
    f = Fig(780, 250)
    for cx, title, sub, usb in ((200, "LSB — apakšējā sānjosla", "zem 10 MHz: 80 m, 40 m", False),
                                (580, "USB — augšējā sānjosla", "virs 10 MHz: 15 m, 10 m, 2 m, 70 cm", True)):
        y = 170
        f.text(cx, 24, title, size=14, bold=True, color=(AMBER if usb else BLUE))
        f.text(cx, 42, sub, size=11, italic=True)
        f.arrow(cx - 160, y, cx + 160, y, w=1.3)
        f.text(cx + 160, y + 18, "f", anchor="end", italic=True)
        s = 1 if usb else -1
        poly = [(cx + s * 8, y), (cx + s * 8, y - 72), (cx + s * 100, y - 34), (cx + s * 100, y)]
        f.pl(poly, close=True, fill=(AMBER_T if usb else BLUE_T), w=1.6, color=(AMBER if usb else BLUE))
        f.line(cx, y + 4, cx, 66, dash="5 4", w=1.4)
        f.text(cx, 60, "noskaņotā frekvence", size=11)
        a, b = sorted((cx, cx + s * 100))
        f.darrow(a, y + 26, b, y + 26)
        f.text((a + b) / 2, y + 44, "≈ 3 kHz", size=12)
    f.line(390, 30, 390, 230, dash="3 5", w=1, color=MG)
    f.save("atteli/06-3-lsb-usb.svg", "LSB un USB signāls pret noskaņoto frekvenci")


def _polar(f, cx, cy, R, rfun, n=360):
    pts = []
    for i in range(n + 1):
        a = 2 * math.pi * i / n
        r = R * rfun(a)
        pts.append((cx + r * math.cos(a), cy - r * math.sin(a)))
    f.pl(pts, close=True, fill=BLUE_T, w=2.2, color=BLUE)


def f13_6():
    f = Fig(780, 330)
    # dipols
    cx, cy = 190, 175
    f.text(cx, 24, "Dipols (skats no augšas)", size=14, bold=True)
    for r in (40, 80, 120):
        f.circ(cx, cy, r, fill="none", sw=0.6, color=MG, dash="3 4")
    _polar(f, cx, cy, 120, lambda a: abs(math.sin(a)))
    f.line(cx - 60, cy, cx + 60, cy, w=4)
    f.circ(cx, cy, 4, fill=K)
    f.text(cx + 66, cy + 4, "vads", anchor="start", size=11, italic=True)
    f.text(cx, 316, "maksimums perpendikulāri vadam", size=12)
    f.text(cx - 140, cy + 26, "galu", anchor="start", size=11, italic=True)
    f.text(cx - 140, cy + 40, "virzienā", anchor="start", size=11, italic=True)
    f.text(cx - 140, cy + 54, "minimums", anchor="start", size=11, italic=True)
    # Yagi
    cx, cy = 500, 175
    f.text(570, 24, "Yagi (skats no augšas)", size=14, bold=True)
    for r in (42, 84, 125):
        f.circ(cx, cy, r, fill="none", sw=0.6, color=MG, dash="3 4")
    front = lambda a: max(0.0, math.cos(a)) ** 4
    back = lambda a: 0.16 * max(0.0, -math.cos(a)) ** 6
    side = lambda a: 0.05
    _polar(f, cx, cy, 125, lambda a: max(front(a), back(a), side(a)))
    for dx, L in ((-16, 40), (0, 34), (16, 28)):
        f.line(cx + dx, cy - L / 2, cx + dx, cy + L / 2, w=2.4)
    f.line(cx - 16, cy, cx + 16, cy, w=1.4, color=MG)
    f.arrow(cx + 140, cy, cx + 215, cy, w=2.4, head=12)
    f.text(cx + 178, cy - 14, "galvenais", size=11, italic=True)
    f.text(cx + 178, cy + 26, "virziens", size=11, italic=True)
    f.text(cx - 40, cy + 54, "aizmugurē", anchor="end", size=11, italic=True)
    f.text(cx - 40, cy + 68, "vājš", anchor="end", size=11, italic=True)
    f.text(590, 316, "starojums koncentrēts vienā virzienā", size=12)
    f.save("atteli/13-5-starojuma-diagrammas.svg", "Dipola un Yagi starojuma diagrammas")


ALL = [f01_1, f04_1, f04_2, f05_1, f05_2, f05_3, f06_1, f06_2, f13_6]
