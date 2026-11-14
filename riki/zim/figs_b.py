"""11.–13. nodaļas zīmējumi."""
import math
from lib import Fig, K, G, LG, MG, chain, tw
from lib import BLUE, BLUE_T, AMBER, AMBER_T, BRICK, BRICK_T


def _below(f, pos, i, y, label, dy=92, bh=44, size=12, note=None):
    """Bloks zem ķēdes i-tā bloka ar bultiņu uz augšu."""
    cx = pos[i][0]
    w = max(70, 18 + max(tw(t, size) for t in label.split("\n")))
    f.box(cx, y + dy, w, bh, label, size=size)
    f.arrow(cx, y + dy - bh / 2, cx, y + 23)
    if note:
        f.text(cx, y + dy + bh / 2 + 16, note, size=11, italic=True)


def _rx(f, labels, y, x0=84, speaker=True, fills=None, gap=28):
    f.antenna(40, y, h=44)
    f.arrow(40, y, x0, y)
    pos = chain(f, labels, x0, y, fills=fills, gap=gap)
    xe = pos[-1][2]
    if speaker:
        f.arrow(xe, y, xe + 28, y)
        f.speaker(xe + 28, y)
        f.w = xe + 70
    else:
        f.w = xe + 30
    return pos


def f11_1():
    f = Fig(600, 170)
    y = 70
    pos = _rx(f, ["Svārstību\nkontūrs", "Detektors\n(diode)", "Austiņas"], y, speaker=False, gap=40)
    f.ground(pos[0][0], y + 23, stem=22)
    f.text(pos[0][0] + 20, y + 62, "zemējums", anchor="start", size=11, italic=True)
    f.text((pos[0][2] + pos[1][1]) / 2, y - 12, "AM", size=11, italic=True)
    f.text((pos[1][2] + pos[2][1]) / 2, y - 12, "skaņa", size=11, italic=True)
    f.text(40, y + 22, "antena", size=11, italic=True)
    f.save("atteli/11-1-detektoruztverejs.svg", "Detektoruztvērēja blokshēma")


def f11_2():
    f = Fig(700, 130)
    y = 70
    pos = _rx(f, ["Ieejas\nkontūrs", "AFP", "Detektors", "ZFP"], y, gap=40)
    f.text(pos[1][0], y + 42, "pastiprina\naugstfrekvenci".split("\n")[0], size=10, italic=True)
    f.text(pos[1][0], y + 54, "augstfrekvenci", size=10, italic=True)
    f.text(pos[3][0], y + 42, "pastiprina", size=10, italic=True)
    f.text(pos[3][0], y + 54, "skaņu", size=10, italic=True)
    f.save("atteli/11-2-tiesa-pastiprinajuma-uztverejs.svg", "Tiešā pastiprinājuma uztvērēja blokshēma")


def f11_3():
    f = Fig(1000, 230)
    y = 70
    pos = _rx(f, ["Ieejas filtrs\nun AFP", "Jaucējs", "SF filtrs", "SFP", "Detektors", "ZFP"], y, gap=56)
    _below(f, pos, 1, y, "Heterodīns", note="ar to noskaņo uztvērēju")
    _below(f, pos, 4, y, "Otrais\nheterodīns", note="SSB un CW uztveršanai")
    f.text((pos[0][2] + pos[1][1]) / 2, y - 12, "f sign", size=11, italic=True)
    f.text((pos[1][2] + pos[2][1]) / 2, y - 12, "f SF", size=11, italic=True)
    f.text((pos[4][2] + pos[5][1]) / 2, y - 12, "skaņa", size=11, italic=True)
    # starpfrekvences trakta iezīmējums
    xa, xb = pos[2][1] - 8, pos[3][2] + 8
    f.rect(xa, y - 36, xb - xa, 72, fill="none", dash="5 4", sw=1, color=MG, rx=8)
    f.text((xa + xb) / 2, y - 44, "nemainīga starpfrekvence", size=11, italic=True)
    f.save("atteli/11-3-superheterodins.svg", "Superheterodīna uztvērēja blokshēma")


def f11_4():
    f = Fig(700, 230)
    y = 70
    pos = _rx(f, ["Ieejas\nfiltrs", "Jaucējs", "ZF filtrs", "ZFP"], y, gap=40)
    _below(f, pos, 1, y, "Heterodīns", note="noskaņots uz signāla frekvenci")
    f.text((pos[0][2] + pos[1][1]) / 2, y - 12, "f sign", size=11, italic=True)
    f.text((pos[1][2] + pos[2][1]) / 2, y - 12, "skaņa", size=11, italic=True)
    f.save("atteli/11-4-tiesas-parveidosanas-uztverejs.svg", "Tiešās pārveidošanas uztvērēja blokshēma")


def f11_5():
    f = Fig(760, 200)
    y = 90
    pos = _rx(f, ["Ieejas\nfiltrs", "Analogciparu\npārveidotājs (ADC)", "Signālu apstrāde\n(programma)"], y,
              fills=["white", "white", LG], gap=40)
    f.text(pos[2][0], y - 36, "filtri · demodulators · AGC · spektra attēls", size=11, italic=True)
    f.text((pos[1][2] + pos[2][1]) / 2, y - 12, "skaitļi", size=11, italic=True)
    for a, b, lab in ((pos[0][1], pos[1][2], "Aparatūra"), (pos[2][1], pos[2][2], "Programma")):
        yb = y + 40
        f.pl([(a, yb - 6), (a, yb), (b, yb), (b, yb - 6)], w=1.1)
        f.text((a + b) / 2, yb + 18, lab, size=12, bold=True)
    f.save("atteli/11-5-sdr.svg", "SDR uztvērēja blokshēma")


def _tx_end(f, pos, y):
    xe = pos[-1][2]
    f.arrow(xe, y, xe + 34, y)
    f.antenna(xe + 34, y, h=44)
    f.w = xe + 70


def f12_1():
    f = Fig(760, 230)
    y = 80
    pos = chain(f, ["Ģenerators", "Starppakāpe\n(reizinātājs)", "Jaudas\npastiprinātājs", "Zemo frekvenču\nfiltrs (LPF)"], 40, y, gap=40)
    _tx_end(f, pos, y)
    _below(f, pos, 1, y, "Telegrāfa\natslēga", note="ieslēdz un izslēdz signālu")
    f.save("atteli/12-1-cw-raiditajs.svg", "CW raidītāja blokshēma")


def f12_2():
    f = Fig(760, 240)
    y = 70
    pos = chain(f, ["Ģenerators", "Starppakāpe", "Jaudas\npastiprinātājs", "Zemo frekvenču\nfiltrs (LPF)"], 40, y, gap=40)
    _tx_end(f, pos, y)
    y2 = y + 100
    cxm = pos[2][0]
    f.box(cxm, y2, 96, 44, "Modulators", size=12)
    f.arrow(cxm, y2 - 22, cxm, y + 23)
    cxz = cxm - 96 / 2 - 40 - 35
    f.box(cxz, y2, 70, 44, "ZFP", size=12)
    f.arrow(cxz + 35, y2, cxm - 48, y2)
    f.mic(cxz - 35 - 34, y2)
    f.arrow(cxz - 35 - 34, y2, cxz - 35, y2)
    f.text(cxz - 35 - 46, y2 + 34, "mikrofons", size=11, italic=True)
    f.text(cxm + 8, (y + y2) / 2 + 6, "maina amplitūdu", anchor="start", size=11, italic=True)
    f.save("atteli/12-2-am-raiditajs.svg", "AM raidītāja blokshēma")


def f12_3():
    f = Fig(900, 150)
    y = 70
    x0 = 80
    f.mic(x0 - 30, y)
    f.arrow(x0 - 30, y, x0, y)
    pos = chain(f, ["ZFP", "Ģenerators ar\nfrekvences modulatoru", "Reizinātāji", "Jaudas\npastiprinātājs",
                    "Zemo frekvenču\nfiltrs (LPF)"], x0, y, gap=34)
    _tx_end(f, pos, y)
    f.text(x0 - 42, y + 34, "mikrofons", size=11, italic=True)
    f.text(pos[1][0], y + 42, "balss maina ģeneratora frekvenci", size=11, italic=True)
    f.save("atteli/12-3-fm-raiditajs.svg", "FM raidītāja blokshēma")


def _minispec(f, cx, yb, kind):
    f.line(cx - 34, yb, cx + 34, yb, w=1)
    if kind in ("dsb", "am"):
        f.pl([(cx - 26, yb), (cx - 26, yb - 12), (cx - 5, yb - 24), (cx - 5, yb)], close=True, fill=G, w=1.1)
        f.pl([(cx + 26, yb), (cx + 26, yb - 12), (cx + 5, yb - 24), (cx + 5, yb)], close=True, fill=G, w=1.1)
        f.line(cx, yb, cx, yb - 34, w=2.2 if kind == "am" else 1.1, dash=None if kind == "am" else "3 3",
               color=K if kind == "am" else MG)
    else:
        f.pl([(cx + 26, yb), (cx + 26, yb - 12), (cx + 5, yb - 24), (cx + 5, yb)], close=True, fill=G, w=1.1)
        f.line(cx, yb, cx, yb - 34, w=1.1, dash="3 3", color=MG)


def f12_4():
    f = Fig(1000, 290)
    y = 130
    x0 = 80
    f.mic(x0 - 30, y)
    f.arrow(x0 - 30, y, x0, y)
    pos = chain(f, ["ZFP", "Balansa\nmodulators", "SSB\nfiltrs", "Jaucējs", "Joslas\nfiltrs",
                    "Lineārais jaudas\npastiprinātājs", "LPF"], x0, y, gap=44, bh=50)
    _tx_end(f, pos, y)
    _below(f, pos, 1, y, "Nesēja\nģenerators", dy=96)
    _below(f, pos, 3, y, "VFO", dy=96)
    f.text(x0 - 42, y + 34, "mikrofons", size=11, italic=True)
    # spektri virs savienojumiem
    for i, kind, cap in ((1, "dsb", "abas sānjoslas,\nnesējs nomākts"), (2, "ssb", "viena\nsānjosla"),
                         (4, "ssb", "darba\nfrekvencē")):
        cx = (pos[i][2] + pos[i + 1][1]) / 2
        _minispec(f, cx, y - 44, kind)
        f.mtext(cx, y - 100, cap, size=10)
    f.save("atteli/12-4-ssb-raiditajs.svg", "SSB raidītāja blokshēma")


def _groundline(f, x1, x2, y):
    f.line(x1, y, x2, y, w=1.8)
    x = x1 + 6
    while x < x2:
        f.line(x, y, x - 8, y + 8, w=0.8, color=MG)
        x += 14


def f13_1():
    f = Fig(720, 290)
    yg, yt = 250, 80
    _groundline(f, 30, 690, yg)
    for xm in (70, 650):
        f.line(xm, yg, xm, yt - 10, w=3)
    xa, xb, xc = 150, 570, 360
    f.line(70, yt - 10, xa, yt, w=1, dash="5 3"); f.line(650, yt - 10, xb, yt, w=1, dash="5 3")
    f.line(xa, yt, xc - 8, yt, w=2.4); f.line(xc + 8, yt, xb, yt, w=2.4)
    for x in (xa, xb):
        f.rect(x - 7, yt - 4, 14, 8, fill="white", rx=2)
    f.circ(xc, yt, 8)
    # koaksiālais kabelis
    f.path(f"M {xc} {yt + 8} C {xc} {yt + 70}, {xc + 40} {yt + 90}, {xc + 40} {yg - 32}", w=2.4)
    f.box(xc + 40, yg - 18, 96, 28, "transīvers", size=12)
    # izmēri
    f.darrow(xa, yt - 36, xb, yt - 36)
    f.line(xa, yt - 44, xa, yt - 8, w=0.7, dash="2 3"); f.line(xb, yt - 44, xb, yt - 8, w=0.7, dash="2 3")
    f.ltext(xc, yt - 32, "kopējais garums ≈ λ/2", size=13)
    f.text((xa + xc) / 2, yt + 22, "plecs", size=12, italic=True); f.text((xb + xc) / 2, yt + 22, "plecs", size=12, italic=True)
    f.text(xa, yt + 22, "izolators", size=11, italic=True); f.text(xb, yt + 22, "izolators", size=11, italic=True)
    f.text(xc - 16, yt + 46, "centra izolators", anchor="end", size=11, italic=True)
    f.text(xc + 56, yt + 110, "koaksiālais", anchor="start", size=11, italic=True)
    f.text(xc + 56, yt + 124, "kabelis", anchor="start", size=11, italic=True)
    f.text(60, yt - 22, "virve", anchor="start", size=11, italic=True)
    f.text(70, yg + 26, "masts", size=11, italic=True); f.text(650, yg + 26, "masts", size=11, italic=True)
    f.save("atteli/13-1-dipols.svg", "Pusviļņa dipols")


def f13_2():
    f = Fig(780, 250)
    yg = 190
    # Inverted-V
    cx = 130
    _groundline(f, 20, 240, yg)
    f.line(cx, yg, cx, 50, w=3)
    f.line(cx, 52, 40, 150, w=2.2); f.line(cx, 52, 220, 150, w=2.2)
    f.line(40, 150, 30, yg, w=1, dash="5 3"); f.line(220, 150, 230, yg, w=1, dash="5 3")
    f.circ(cx, 52, 6)
    f.text(cx, 228, "Inverted-V", bold=True, size=13)
    # vairākjoslu dipols
    cx = 390
    _groundline(f, 280, 500, yg)
    for xm in (290, 490):
        f.line(xm, yg, xm, 50, w=3)
    f.line(300, 60, cx - 7, 60, w=2.2); f.line(cx + 7, 60, 480, 60, w=2.2)
    f.line(cx - 6, 64, 330, 100, w=1.8); f.line(cx + 6, 64, 450, 100, w=1.8)
    f.line(cx - 4, 66, 352, 128, w=1.4); f.line(cx + 4, 66, 428, 128, w=1.4)
    f.circ(cx, 60, 6)
    f.line(cx, 66, cx, yg - 20, w=1.6)
    f.text(cx, 228, "Vairākjoslu dipols", bold=True, size=13)
    # OCF
    _groundline(f, 540, 760, yg)
    for xm in (550, 750):
        f.line(xm, yg, xm, 50, w=3)
    xf = 620
    f.line(560, 60, xf - 12, 60, w=2.2); f.line(xf + 12, 60, 740, 60, w=2.2)
    f.rect(xf - 12, 50, 24, 20, rx=2)
    f.text(xf, 64, "4:1", size=9)
    f.line(xf, 70, xf, yg - 20, w=1.6)
    f.darrow(560, 40, xf, 40); f.darrow(xf, 40, 740, 40)
    f.text((560 + xf) / 2, 32, "⅓", size=12); f.text((740 + xf) / 2, 32, "⅔", size=12)
    f.text(650, 228, "OCF dipols", bold=True, size=13)
    f.save("atteli/13-2-dipola-varianti.svg", "Dipola varianti")


def f13_3():
    f = Fig(720, 280)
    # sānskats
    bx, by = 190, 190
    f.text(bx, 22, "Sānskats", bold=True, size=14)
    f.line(bx, by, bx, 50, w=3)
    for dx, dy in ((-130, 40), (130, 40), (-70, 62), (80, 58)):
        f.line(bx, by, bx + dx, by + dy, w=1.8)
    f.circ(bx, by, 6)
    f.path(f"M {bx} {by + 6} C {bx} {by + 40}, {bx + 20} {by + 50}, {bx + 22} {by + 78}", w=2.2)
    f.darrow(bx - 26, 50, bx - 26, by)
    f.text(bx - 34, 124, "λ/4", anchor="end", size=14)
    f.text(bx + 12, 110, "vertikālais", anchor="start", size=11, italic=True)
    f.text(bx + 12, 124, "elements", anchor="start", size=11, italic=True)
    f.text(bx + 110, by + 14, "radiāļi", anchor="start", size=11, italic=True)
    f.text(bx + 30, by + 80, "koaksiālais kabelis", anchor="start", size=11, italic=True)
    # skats no augšas
    cx, cy = 540, 150
    f.text(cx, 22, "Starojums skatā no augšas", bold=True, size=14)
    f.line(cx - 110, cy, cx + 110, cy, w=0.7, color=MG); f.line(cx, cy - 110, cx, cy + 110, w=0.7, color=MG)
    f.circ(cx, cy, 90, fill="none", sw=2.2)
    f.circ(cx, cy, 4, fill=K)
    for a in range(0, 360, 45):
        r = math.radians(a)
        f.arrow(cx + 30 * math.cos(r), cy + 30 * math.sin(r), cx + 78 * math.cos(r), cy + 78 * math.sin(r), w=1, head=6)
    f.text(cx, 268, "vienādi visos virzienos", size=12, italic=True)
    f.line(370, 40, 370, 260, dash="3 5", w=1, color=MG)
    f.save("atteli/13-3-vertikala-antena.svg", "Ceturtdaļviļņa vertikālā antena")


def f13_4():
    f = Fig(720, 280)
    y = 140
    f.line(150, y, 480, y, w=4, color=MG)
    els = [(180, 180, "Reflektors", "garākais"), (310, 156, "Aktīvais elements", "≈ λ/2, ar pievadu"),
           (440, 134, "Direktors", "īsākais")]
    for x, L, name, note in els:
        f.line(x, y - L / 2, x, y + L / 2, w=3)
        f.text(x, y + L / 2 + 22, name, size=12, bold=True)
        f.text(x, y + L / 2 + 38, note, size=11, italic=True)
    f.circ(310, y, 6)
    f.arrow(520, y, 660, y, w=3, head=16)
    f.text(590, y - 16, "galvenais", size=12); f.text(590, y + 26, "starojuma virziens", size=12)
    f.text(315, 24, "Skats no augšas", bold=True, size=14)
    f.text(140, y + 5, "nesošā caurule", anchor="end", size=11, italic=True)
    f.save("atteli/13-4-yagi.svg", "Trīs elementu Yagi antena")


def f13_5():
    f = Fig(760, 260)
    cx, cy = 150, 130
    f.text(cx + 60, 22, "Koaksiālais kabelis", bold=True, size=14)
    COPPER = "#c47a3a"
    f.circ(cx, cy, 78, fill="#2f2f2f")                 # apvalks
    f.circ(cx, cy, 66, fill="#d9a066", color=COPPER)   # ekrāns (pinums)
    for k in range(36):
        a = 2 * math.pi * k / 36
        f.line(cx + 57 * math.cos(a), cy + 57 * math.sin(a), cx + 65 * math.cos(a + 0.12),
               cy + 65 * math.sin(a + 0.12), w=0.8, color=COPPER)
    f.circ(cx, cy, 56, fill="#f7f7f2")                 # izolators
    f.circ(cx, cy, 14, fill=COPPER, color="#7a4316")   # centrālais vadītājs
    labs = [(72, -40, "apvalks", 60), (61, -12, "ekrāns", 105), (38, 10, "izolators", 150),
            (13, 45, "centrālais vadītājs", 195)]
    for r, deg, lab, ly in labs:
        a = math.radians(deg)
        px, py = cx + r * math.cos(a), cy + r * math.sin(a)
        f.circ(px, py, 2.2, fill="white", sw=1)
        f.line(px, py, 262, ly, w=0.9)
        f.text(268, ly + 4, lab, anchor="start", size=12)
    f.text(cx + 60, 244, "raksturpretestība 50 Ω vai 75 Ω", size=12, italic=True)
    # simetriskā līnija
    x0 = 600
    f.text(x0, 22, "Simetriskā līnija", bold=True, size=14)
    f.line(x0 - 28, 50, x0 - 28, 220, w=3, color="#c47a3a"); f.line(x0 + 28, 50, x0 + 28, 220, w=3, color="#c47a3a")
    for yy in range(66, 220, 26):
        f.rect(x0 - 28, yy - 3, 56, 6, fill=LG, rx=1, sw=1)
    f.text(x0 + 44, 100, "vadi", anchor="start", size=12)
    f.text(x0 + 44, 150, "starplikas", anchor="start", size=12)
    f.text(x0, 244, "raksturpretestība 240–600 Ω", size=12, italic=True)
    f.line(470, 40, 470, 250, dash="3 5", w=1, color=MG)
    f.save("atteli/13-6-parvades-linijas.svg", "Koaksiālais kabelis un simetriskā līnija")


# 11. un 12. nodaļas blokshēmas ir pārceltas uz figs_e.py (slaidu simboli).
ALL = [f13_1, f13_2, f13_3, f13_4, f13_5]
