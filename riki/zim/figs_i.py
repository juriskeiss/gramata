"""A pielikuma (formulu lapas) zīmējumi: A-1 … A-10.

Formulu lapas saturs un secība ir YL3RZ oriģināla; šeit tikai pārzīmēti grāmatas stilā
(riki/zim/lib.py palete). Faili: atteli/A-*.svg.
"""
import math
from xml.sax.saxutils import escape
from lib import (Fig, K, MG, RED, BLUE, BLUE_T, GREEN, GREEN_T, AMBER, AMBER_T,
                 BRICK, BRICK_T)
from figs_f import _gate_ansi


def _sub(f, x, y, main, sub, anchor="middle", size=13, italic=True, bold=False, color=K):
    """Teksts ar apakšindeksu (U_s), lai nebūtu atkarības no fonta Unicode apakšindeksiem."""
    st = (' font-style="italic"' if italic else "") + (' font-weight="bold"' if bold else "")
    f.add(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="{size}" fill="{color}"{st}>'
          f'{escape(main)}<tspan dy="{size * 0.28:.1f}" font-size="{size * 0.72:.1f}">{escape(sub)}</tspan></text>')


# ------------------------------------------------------------- 1. rezistori
def a_1_virkne():
    f = Fig(300, 62)
    y = 36
    f.line(20, y, 88, y); f.resistor(110, y, label="R₁")
    f.line(132, y, 168, y); f.resistor(190, y, label="R₂"); f.line(212, y, 280, y)
    f.save("atteli/A-1-rezistori-virkne.svg", "Rezistoru virknes slēgums")


def a_1_paralela():
    f = Fig(300, 122)
    ya, yb = 34, 88
    ym = (ya + yb) / 2
    xa, xb = 90, 210
    f.line(20, ym, xa, ym); f.line(xb, ym, 280, ym)
    for yy, lab, pos in ((ya, "R₁", "above"), (yb, "R₂", "below")):
        f.line(xa, ym, xa, yy); f.line(xb, ym, xb, yy)
        f.line(xa, yy, 128, yy); f.line(172, yy, xb, yy)
        f.resistor(150, yy, label=lab, lpos=pos)
    f.circ(xa, ym, 3, fill=K); f.circ(xb, ym, 3, fill=K)
    f.save("atteli/A-1-rezistori-paralela.svg", "Rezistoru paralēlais slēgums")


# ----------------------------------------------------------- 2. kondensatori
def a_2_virkne():
    f = Fig(300, 62)
    y = 36
    f.line(20, y, 96, y); f.capacitor(100, y); f.line(104, y, 196, y)
    f.capacitor(200, y); f.line(204, y, 280, y)
    f.text(100, y - 22, "C₁", size=13, italic=True)
    f.text(200, y - 22, "C₂", size=13, italic=True)
    f.save("atteli/A-2-kondensatori-virkne.svg", "Kondensatoru virknes slēgums")


def a_2_paralela():
    f = Fig(300, 122)
    ya, yb = 38, 86
    ym = (ya + yb) / 2
    xa, xb = 90, 210
    f.line(20, ym, xa, ym); f.line(xb, ym, 280, ym)
    for yy in (ya, yb):
        f.line(xa, ym, xa, yy); f.line(xb, ym, xb, yy)
        f.line(xa, yy, 146, yy); f.line(154, yy, xb, yy)
        f.capacitor(150, yy)
    f.text(150, ya - 18, "C₁", size=13, italic=True)
    f.text(150, yb + 30, "C₂", size=13, italic=True)
    f.circ(xa, ym, 3, fill=K); f.circ(xb, ym, 3, fill=K)
    f.save("atteli/A-2-kondensatori-paralela.svg", "Kondensatoru paralēlais slēgums")


# ------------------------------------------------- 3. jauda un Oma likums
def a_3_ritenis():
    W = 364
    cx = cy = W / 2
    R, R_in, r_txt = 172, 60, 141
    f = Fig(W, W)

    def pt(r, deg):
        a = math.radians(deg)
        return cx + r * math.cos(a), cy + r * math.sin(a)

    quads = [  # (leņķis no, tonis, formulas pa 30° sektoriem)
        (180, BLUE_T, ["I = E/R", "I = P/E", "I = √(P/R)"]),
        (270, AMBER_T, ["E = √(P×R)", "E = P/I", "E = I×R"]),
        (0, GREEN_T, ["R = E/I", "R = E²/P", "R = P/I²"]),
        (90, BRICK_T, ["P = I²×R", "P = E²/R", "P = E×I"]),
    ]
    # BL (90–180°) lasa no apakšas uz augšu: sektori 90–120, 120–150, 150–180
    quads[3] = (90, BRICK_T, ["P = E²/R", "P = I²×R", "P = E×I"])
    for a0, tint, forms in quads:
        for i, txt in enumerate(forms):
            s, e = a0 + 30 * i, a0 + 30 * (i + 1)
            x1, y1 = pt(R_in, s); x2, y2 = pt(R, s)
            x3, y3 = pt(R, e); x4, y4 = pt(R_in, e)
            f.path(f"M {x1:.1f} {y1:.1f} L {x2:.1f} {y2:.1f} A {R} {R} 0 0 1 {x3:.1f} {y3:.1f} "
                   f"L {x4:.1f} {y4:.1f} A {R_in} {R_in} 0 0 0 {x1:.1f} {y1:.1f} Z",
                   fill=tint, w=0.9, color=MG)
            tx, ty = pt(r_txt, s + 15)
            f.text(tx, ty + 4, txt, size=10.5)
    # vidus: četri lielumi
    inner = [(180, BLUE_T, BLUE, "I", "strāva"), (270, AMBER_T, AMBER, "E", "spriegums"),
             (0, GREEN_T, GREEN, "R", "pretestība"), (90, BRICK_T, BRICK, "P", "jauda")]
    for a0, tint, col, letter, word in inner:
        x1, y1 = pt(R_in, a0); x2, y2 = pt(R_in, a0 + 90)
        f.path(f"M {cx} {cy} L {x1:.1f} {y1:.1f} A {R_in} {R_in} 0 0 1 {x2:.1f} {y2:.1f} Z",
               fill=tint, w=0.9, color=MG)
        tx, ty = pt(33, a0 + 45)
        f.text(tx, ty + 2, letter, size=22, bold=True, color=col)
        f.text(tx, ty + 14, word, size=7.5, color=col)
    f.circ(cx, cy, R, fill="none", sw=1.8)
    f.circ(cx, cy, R_in, fill="none", sw=1.4)
    f.save("atteli/A-3-oma-likuma-ritenis.svg", "Jaudas un Oma likuma formulu ritenis")


# ------------------------------------------------------- 8. Kirhofa likumi
def a_8_kirhofs():
    f = Fig(300, 178)
    yt, yb = 52, 152
    xs, x1, x2 = 40, 140, 230
    ym = (yt + yb) / 2
    f.line(xs, yt, x2, yt); f.line(xs, yb, x2, yb)
    f.line(xs, yt, xs, ym - 5); f.line(xs, ym + 5, xs, yb)
    f.battery(xs, ym)
    _sub(f, xs + 12, ym + 5, "U", "s", anchor="start", size=14)
    for x, lab in ((x1, "R₁"), (x2, "R₂")):
        f.line(x, yt, x, ym - 22); f.line(x, ym + 22, x, yb)
        f.resistor(x, ym, horizontal=False, label=lab)
    for i, x in enumerate((x1, x2), start=1):
        f.arrow(x - 12, yt + 14, x - 12, yt + 38, w=1.3, head=7)
        _sub(f, x - 18, yt + 30, "I", str(i), anchor="end", size=13)
    f.circ(x1, yt, 3.2, fill=K); f.circ(x1, yb, 3.2, fill=K)
    f.text(x1, 24, "Mezgls", size=12.5, bold=True, color=BRICK)
    f.arrow(x1, 30, x1, yt - 6, w=1.2, head=6, color=BRICK)
    f.save("atteli/A-8-kirhofs.svg", "Shēma Kirhofa likumiem: avots un divi paralēli rezistori")


# -------------------------------------------------------- 9. loģiskie elementi
def _gate(kind, name, title):
    f = Fig(210, 86)
    _gate_ansi(f, 100, 43, kind)
    f.save(f"atteli/A-9-{name}.svg", title)


def a_9_un():
    _gate("and", "un", "Loģiskais elements UN (AND)")


def a_9_vai():
    _gate("or", "vai", "Loģiskais elements VAI (OR)")


def a_9_ne():
    _gate("not", "ne", "Loģiskais elements NE (NOT)")


# ------------------------------------------------------------ 10. binārā sistēma
def a_10_dalisana():
    f = Fig(250, 124)
    rows = [(11, 5, 1), (5, 2, 1), (2, 1, 0), (1, 0, 1)]
    y0, dy = 22, 26
    for i, (a, q, r) in enumerate(rows):
        y = y0 + i * dy
        f.text(46, y, str(a), anchor="end", size=15)
        f.text(56, y, ": 2 =", anchor="start", size=15)
        f.text(122, y, str(q), anchor="end", size=15)
        f.text(140, y, "atl.", anchor="start", size=13, color=MG)
        f.text(176, y, str(r), anchor="start", size=16, bold=True, color=BRICK)
    ytop, ybot = y0 - 5, y0 + 3 * dy - 5
    f.arrow(214, ybot, 214, ytop, w=1.8, head=9, color=BRICK)
    f.save("atteli/A-10-dalisana-ar-2.svg", "Pārveidošana no decimālā uz bināro: dalīšana ar 2")


ALL = [a_1_virkne, a_1_paralela, a_2_virkne, a_2_paralela, a_3_ritenis, a_8_kirhofs,
       a_9_un, a_9_vai, a_9_ne, a_10_dalisana]
