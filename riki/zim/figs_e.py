"""Uztvērēju un raidītāju blokshēmas (11. un 12. nodaļa).

Simboli un bloku secība atbilst LRAL bezmaksas kursa 7. nodarbības slaidiem
("Izmantotie apzīmējumi" un blokshēmas), lai grāmata un slaidi veidotu vienu
mācību komplektu. Zīmējumi ir uzzīmēti no jauna.
"""
from lib import (Fig, K, G, LG, MG, sym_filter, sym_amp, sym_mixer, sym_gen, sym_det, sym_disc,
                 sym_lim, sym_block, sym_key, lab, RED, BLUE, GREEN)

# Trakti superheterodīnā — tās pašas krāsas kā slaidā: FM sarkans, AM zils, CW/SSB zaļš.
C_FM, C_AM, C_SSB = RED, BLUE, GREEN

Y = 0  # palīgs


def _ant_in(f, x_ant, y, x_to):
    f.antenna(x_ant, y, h=46)
    f.arrow(x_ant, y, x_to, y)


def _ant_out(f, x_from, y, x_ant):
    f.arrow(x_from, y, x_ant, y)
    f.antenna(x_ant, y, h=50)


def _spk(f, x_from, y, x_spk):
    f.arrow(x_from, y, x_spk, y)
    f.speaker(x_spk, y)


def f11_0():
    """Apzīmējumi — kā slaidā "Izmantotie apzīmējumi"."""
    f = Fig(900, 460)
    rows = 7
    y0, dy = 40, 58
    left = [("bp", "Joslas filtrs"), ("lp", "Zemo frekvenču filtrs\n(nogriež augstās frekvences)"),
            ("hp", "Augsto frekvenču filtrs"), ("amp", "Pastiprinātājs: AFP — augstfrekvences,\nSFP — starpfrekvences, ZFP — zemfrekvences"),
            ("mix", "Jaucējs (maisītājs, angliski mixer)"), ("mic", "Mikrofons"),
            ("key", "Telegrāfa atslēga")]
    right = [("det", "Detektors (demodulators)"), ("gent", "Ģenerators (pārskaņojams)"),
             ("gen", "Ģenerators (nemainīga frekvence)"), ("disc", "Diskriminators (FM detektors)"),
             ("lim", "Amplitūdas ierobežotājs"), ("ant", "Antena"), ("spk", "Skaļrunis vai austiņas")]
    def draw(kind, cx, cy):
        if kind in ("bp", "lp", "hp"):
            sym_filter(f, cx, cy, kind)
        elif kind == "amp":
            sym_amp(f, cx, cy)
        elif kind == "mix":
            sym_mixer(f, cx, cy)
        elif kind == "mic":
            f.mic(cx + 12, cy)
        elif kind == "key":
            sym_key(f, cx + 8, cy - 26)
        elif kind == "det":
            sym_det(f, cx, cy)
        elif kind == "gent":
            sym_gen(f, cx, cy, tunable=True)
        elif kind == "gen":
            sym_gen(f, cx, cy)
        elif kind == "disc":
            sym_disc(f, cx, cy)
        elif kind == "lim":
            sym_lim(f, cx, cy)
        elif kind == "ant":
            f.antenna(cx, cy + 22, h=44)
        elif kind == "spk":
            f.speaker(cx - 10, cy)
    for col, items in ((60, left), (520, right)):
        for i, (k, t) in enumerate(items):
            cy = y0 + i * dy + 10
            draw(k, col, cy)
            f.mtext(col + 44, cy, t, size=12, anchor="start")
    f.save("atteli/11-1-apzimejumi.svg", "Blokshēmu apzīmējumi")


def f11_1():
    f = Fig(560, 200)
    y = 90
    a, b = sym_filter(f, 150, y, "bp")
    _ant_in(f, 50, y, a)
    c, d = sym_det(f, 290, y)
    f.arrow(b, y, c, y)
    _spk(f, d, y, 410)
    lab(f, 150, y + 48, "Preselektors", size=11)
    lab(f, 150, y + 76, "(pārskaņojams\njoslas filtrs)", size=10)
    lab(f, 290, y + 48, "Detektors", size=11)
    lab(f, 290, y + 62, "(demodulators)", size=10)
    lab(f, 420, y + 48, "Austiņas", size=11)
    f.save("atteli/11-2-detektoruztverejs.svg", "Detektoruztvērēja blokshēma")


def f11_2():
    f = Fig(680, 200)
    y = 90
    xs = [150, 250, 350, 450]
    a, b = sym_filter(f, xs[0], y, "bp")
    _ant_in(f, 50, y, a)
    c, d = sym_amp(f, xs[1], y); f.arrow(b, y, c, y)
    e, g = sym_det(f, xs[2], y); f.arrow(d, y, e, y)
    h, i = sym_amp(f, xs[3], y); f.arrow(g, y, h, y)
    _spk(f, i, y, 530)
    for x, t in zip(xs + [541], ["Ieejas filtrs", "AFP", "Detektors", "ZFP", "Skaļrunis"]):
        lab(f, x, y + 48, t)
    f.save("atteli/11-3-tiesa-pastiprinajuma-uztverejs.svg", "Tiešā pastiprinājuma uztvērēja blokshēma")


def f11_3():
    f = Fig(830, 440)
    y = 190
    pa, pb = sym_filter(f, 110, y, "bp")
    _ant_in(f, 36, y, pa)
    aa, ab = sym_amp(f, 190, y); f.arrow(pb, y, aa, y)
    ma, mb = sym_mixer(f, 270, y); f.arrow(ab, y, ma, y)
    sym_gen(f, 270, y + 92, tunable=True); f.arrow(270, y + 69, 270, y + 23)
    fa, fb = sym_filter(f, 352, y, "bp"); f.arrow(mb, y, fa, y)
    sa, sb = sym_amp(f, 432, y); f.arrow(fb, y, sa, y)
    xn = 476
    yf, ys = y - 100, y + 90
    # FM zars (sarkans)
    f.pl([(sb - 4, y - 3), (xn, y - 3), (xn, yf)], w=1.8, color=C_FM)
    la, lb = sym_lim(f, 534, yf); f.arrow(xn, yf, la, yf, w=1.8, color=C_FM)
    da, db = sym_disc(f, 614, yf); f.arrow(lb, yf, da, yf, w=1.8, color=C_FM)
    # AM zars (zils)
    ea, eb = sym_det(f, 574, y); f.arrow(sb, y, ea, y, w=1.8, color=C_AM)
    # CW/SSB zars (zaļš)
    f.pl([(sb - 4, y + 3), (xn, y + 3), (xn, ys)], w=1.8, color=C_SSB)
    xa, xb = sym_mixer(f, 574, ys); f.arrow(xn, ys, xa, ys, w=1.8, color=C_SSB)
    sym_gen(f, 574, ys + 92); f.arrow(574, ys + 69, 574, ys + 23)
    # katrs zars atsevišķi uz ZFP
    xj = 690
    za, zb = sym_amp(f, 742, y)
    f.pl([(db, yf), (xj, yf), (xj, y - 12)], w=1.8, color=C_FM)
    f.arrow(xj, y - 12, za, y - 12, w=1.8, color=C_FM)
    f.arrow(eb, y, za, y, w=1.8, color=C_AM)
    f.pl([(xb, ys), (xj + 8, ys), (xj + 8, y + 12)], w=1.8, color=C_SSB)
    f.arrow(xj + 8, y + 12, za, y + 12, w=1.8, color=C_SSB)
    _spk(f, zb, y, 782)
    f.text(xj + 14, yf + 18, "FM", anchor="start", size=12, bold=True, color=C_FM)
    f.text(650, y - 8, "AM", size=12, bold=True, color=C_AM)
    f.text(xj + 16, ys - 10, "CW / SSB", anchor="start", size=12, bold=True, color=C_SSB)
    # paraksti (kā slaidā)
    lab(f, 110, y + 44, "Preselektors", size=10)
    lab(f, 190, y - 32, "AFP")
    f.text(190, y + 44, "lētajos nav", size=10, italic=True)
    lab(f, 270, y - 46, "Jaucējs\n(maisītājs)", size=10)
    lab(f, 352, y + 44, "Pamatselekcijas", size=10)
    lab(f, 352, y + 57, "joslu filtrs", size=10)
    lab(f, 432, y - 32, "SFP")
    lab(f, 534, yf - 44, "Amplitūdas\nierobežotājs", size=10)
    lab(f, 614, yf - 44, "FM detektors\n(diskriminators)", size=10)
    lab(f, 742, y - 32, "ZFP")
    lab(f, 270, y + 132, "Heterodīns")
    lab(f, 270, y + 146, "(oscilators, pārskaņojams)", size=10)
    lab(f, 574, ys + 132, "Papildģenerators")
    lab(f, 574, ys + 146, "(atbalsta ģenerators)", size=10)
    f.save("atteli/11-4-superheterodins.svg", "Superheterodīna uztvērēja blokshēma")


def f11_4():
    f = Fig(680, 290)
    y = 90
    a, b = sym_filter(f, 150, y, "bp")
    _ant_in(f, 50, y, a)
    c, d = sym_mixer(f, 250, y); f.arrow(b, y, c, y)
    sym_gen(f, 250, y + 100, tunable=True); f.arrow(250, y + 77, 250, y + 23)
    e, g = sym_filter(f, 350, y, "lp"); f.arrow(d, y, e, y)
    h, i = sym_amp(f, 450, y); f.arrow(g, y, h, y)
    _spk(f, i, y, 530)
    lab(f, 150, y - 32, "Ieejas filtrs")
    lab(f, 250, y - 32, "Jaucējs")
    lab(f, 350, y - 32, "Zemo frekvenču\nfiltrs", size=10)
    lab(f, 450, y - 32, "ZFP")
    lab(f, 250, y + 142, "Heterodīns")
    lab(f, 250, y + 156, "(noskaņots uz signāla frekvenci)", size=10)
    f.save("atteli/11-5-tiesas-parveidosanas-uztverejs.svg", "Tiešās pārveidošanas uztvērēja blokshēma")


def f11_5():
    f = Fig(780, 320)
    y = 120
    a, b = sym_filter(f, 130, y, "bp")
    _ant_in(f, 50, y, a)
    c, d = sym_mixer(f, 220, y); f.arrow(b, y, c, y)
    sym_gen(f, 220, y + 96, tunable=True); f.arrow(220, y + 73, 220, y + 23)
    e, g = sym_block(f, 320, y, "ADC", w=60, size=12); f.arrow(d, y, e, y)
    h, i = sym_block(f, 470, y, "Programma\ndatu\napstrādei", w=96, size=10)
    f.arrow(g, y - 8, h, y - 8); f.arrow(g, y + 8, h, y + 8)
    f.text((g + h) / 2, y - 16, "I/Q dati", size=10, italic=True)
    j, k = sym_amp(f, 580, y); f.arrow(i, y, j, y)
    _spk(f, k, y, 620)
    lab(f, 130, y - 32, "Ieejas filtrs")
    lab(f, 220, y - 32, "Jaucējs")
    lab(f, 320, y - 32, "Analogciparu\npārveidotājs", size=10)
    lab(f, 580, y - 32, "ZFP")
    lab(f, 220, y + 138, "Ģenerators")
    # daļas
    f.rect(90, 46, 280, 230, fill="none", dash="6 4", sw=1.6, color=GREEN, rx=12)
    f.rect(412, 46, 250, 230, fill="none", dash="6 4", sw=1.6, color=RED, rx=12)
    f.text(230, 300, "„Dzelžu” daļa", size=13, bold=True, color=GREEN)
    f.text(537, 300, "„PC” daļa", size=13, bold=True, color=RED)
    f.save("atteli/11-6-sdr.svg", "SDR uztvērēja blokshēma")


def f12_1():
    f = Fig(720, 300)
    y = 110
    ga, gb = sym_gen(f, 60, y, tunable=True)
    xs = [160, 260, 360, 460]
    prev = gb
    for x in xs:
        a, b = sym_amp(f, x, y); f.arrow(prev, y, a, y); prev = b
    fa, fb = sym_filter(f, 560, y, "lp"); f.arrow(prev, y, fa, y)
    _ant_out(f, fb, y, 640)
    labs = ["Atdalošais\npastiprinātājs", "Manipulējamais\npastiprinātājs", "Pastiprinātājs\n(vai ×2, ×3)",
            "Izejas\npastiprinātājs"]
    for x, t in zip(xs, labs):
        lab(f, x, y - 34, t, size=10)
    lab(f, 60, y - 34, "Ģenerators", size=10)
    lab(f, 560, y - 34, "Zemo frekvenču\nfiltrs", size=10)
    f.line(260, y + 12, 260, y + 54)
    sym_key(f, 260, y + 58)
    f.text(282, y + 80, "Telegrāfa atslēga", anchor="start", size=11)
    f.text(360, 285, "pastiprinātāji var būt arī frekvences reizinātāji (×2 vai ×3)", size=10, italic=True)
    f.save("atteli/12-1-cw-raiditajs.svg", "CW raidītāja blokshēma")


def f12_2():
    f = Fig(680, 300)
    y = 100
    ga, gb = sym_gen(f, 60, y, tunable=True)
    a1, b1 = sym_amp(f, 140, y); f.arrow(gb, y, a1, y)
    a2, b2 = sym_amp(f, 210, y); f.arrow(b1, y, a2, y)
    a4, b4 = sym_amp(f, 280, y); f.arrow(b2, y, a4, y)
    a3, b3 = sym_amp(f, 360, y); f.arrow(b4, y, a3, y)
    fa, fb = sym_filter(f, 480, y, "lp"); f.arrow(b3, y, fa, y)
    _ant_out(f, fb, y, 560)
    y2 = y + 110
    f.mic(150, y2)
    za, zb = sym_amp(f, 240, y2); f.arrow(150, y2, za, y2)
    f.line(zb, y2, 360, y2)
    f.arrow(360, y2, 360, y + 13)
    lab(f, 60, y - 34, "Ģenerators", size=10)
    lab(f, 210, y - 34, "Pastiprinātāji (2…3)\nvai reizinātāji", size=10)
    lab(f, 360, y - 34, "Izejas pastiprinātājs\n— arī modulators", size=10)
    lab(f, 485, y - 34, "Zemo frekvenču\nfiltrs", size=10)
    lab(f, 126, y2 + 40, "Mikrofons", size=10)
    lab(f, 240, y2 + 40, "ZFP", size=11)
    f.text(368, y2 - 40, "zemfrekvence maina", anchor="start", size=10, italic=True)
    f.text(368, y2 - 26, "izejas pakāpes pastiprinājumu", anchor="start", size=10, italic=True)
    f.save("atteli/12-2-am-raiditajs.svg", "AM raidītāja blokshēma")


def f12_3():
    f = Fig(760, 220)
    y = 110
    f.mic(60, y)
    za, zb = sym_amp(f, 140, y); f.arrow(60, y, za, y)
    ga, gb = sym_gen(f, 230, y, tunable=True); f.arrow(zb, y, ga, y)
    prev = gb
    for x in (320, 410, 500):
        a, b = sym_amp(f, x, y); f.arrow(prev, y, a, y); prev = b
    fa, fb = sym_filter(f, 590, y, "lp"); f.arrow(prev, y, fa, y)
    _ant_out(f, fb, y, 670)
    lab(f, 36, y + 44, "Mikrofons", size=10)
    lab(f, 140, y + 44, "ZFP")
    lab(f, 230, y - 34, "Ģenerators", size=10)
    lab(f, 365, y - 34, "Starppastiprinātāji", size=10)
    lab(f, 500, y - 34, "Izejas\npastiprinātājs", size=10)
    lab(f, 590, y - 34, "Zemo frekvenču\nfiltrs", size=10)
    f.text(185, y + 64, "zemfrekvence maina ģeneratora frekvenci", size=10, italic=True)
    f.save("atteli/12-3-fm-raiditajs.svg", "FM raidītāja blokshēma")


def _minispec(f, cx, yb, both):
    f.line(cx - 30, yb, cx + 30, yb, w=1)
    if both:
        f.pl([(cx - 24, yb), (cx - 24, yb - 10), (cx - 5, yb - 22), (cx - 5, yb)], close=True, fill=G, w=1.1)
    f.pl([(cx + 24, yb), (cx + 24, yb - 10), (cx + 5, yb - 22), (cx + 5, yb)], close=True, fill=G, w=1.1)
    f.line(cx, yb, cx, yb - 30, w=1.1, dash="3 3", color=MG)


def f12_4():
    f = Fig(660, 570)
    y, y2 = 176, 410
    x0 = 56
    f.mic(x0, y)
    za, zb = sym_amp(f, 150, y); f.arrow(x0, y, za, y)
    m1a, m1b = sym_mixer(f, 250, y); f.arrow(zb, y, m1a, y)
    sym_gen(f, 250, y + 90); f.arrow(250, y + 67, 250, y + 23)
    s1a, s1b = sym_filter(f, 350, y, "bp"); f.arrow(m1b, y, s1a, y)
    p1a, p1b = sym_amp(f, 450, y); f.arrow(s1b, y, p1a, y)
    # pāreja uz otro rindu
    ym = y + 152
    f.pl([(p1b, y), (560, y), (560, ym), (70, ym), (70, y2)])
    m2a, m2b = sym_mixer(f, 150, y2); f.arrow(70, y2, m2a, y2)
    sym_gen(f, 150, y2 + 90, tunable=True); f.arrow(150, y2 + 67, 150, y2 + 23)
    s2a, s2b = sym_filter(f, 250, y2, "bp"); f.arrow(m2b, y2, s2a, y2)
    p2a, p2b = sym_amp(f, 350, y2); f.arrow(s2b, y2, p2a, y2)
    p3a, p3b = sym_amp(f, 450, y2); f.arrow(p2b, y2, p3a, y2)
    la, lb = sym_filter(f, 550, y2, "lp"); f.arrow(p3b, y2, la, y2)
    _ant_out(f, lb, y2, 625)
    for x, t in ((150, "ZFP"), (250, "Balansēts\njaucējs"), (350, "SSB filtrs"), (450, "Pastiprinātājs")):
        lab(f, x, y - 34, t)
    for x, t in ((150, "Diapazonu\njaucējs"), (250, "Diapazonu\njoslas filtrs"), (450, "Izejas\npastiprinātājs"),
                 (550, "Zemo frekvenču\nfiltrs")):
        lab(f, x, y2 - 34, t)
    lab(f, x0 - 22, y + 44, "Mikrofons")
    lab(f, 250, y + 132, "SSB atbalsta ģenerators")
    lab(f, 150, y2 + 132, "Diapazonu VFO")
    # mazie spektri
    for cx, yb, both, cap in ((300, 82, True, "abas sānjoslas,\nnesējs nomākts"),
                              (400, 82, False, "viena\nsānjosla")):
        _minispec(f, cx, yb, both)
        lab(f, cx, yb - 36, cap, size=10)
    _minispec(f, 300, y2 + 70, False)
    lab(f, 300, y2 + 88, "darba frekvencē", size=10)
    f.save("atteli/12-4-ssb-raiditajs.svg", "SSB raidītāja blokshēma")


ALL = [f11_0, f11_1, f11_2, f11_3, f11_4, f11_5, f12_1, f12_2, f12_3, f12_4]
