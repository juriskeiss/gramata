"""14.8. attēls: vairākkārtēja atstarošanās (HF no F slāņa) un 6 m izplatīšanās (Es, Es + F2).
Papildināts pēc Valta YL3OI recenzijas."""
from lib import Fig, K, MG, RED, BLUE, BLUE_T, GREEN
from figs_b import _groundline


def _cloud(f, cx, cy, rx=46, ry=11):
    f.add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{BLUE_T}" stroke="{BLUE}" stroke-width="1.2"/>')


def _hop(f, pts, dash=None, color=RED, w=2):
    for (x1, y1), (x2, y2) in zip(pts[:-2], pts[1:-1]):
        f.line(x1, y1, x2, y2, dash=dash, w=w, color=color)
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    f.arrow(x1, y1, x2, y2, dash=dash, w=w, color=color)


def _span(f, a, b, y, label):
    f.pl([(a, y - 5), (a, y), (b, y), (b, y - 5)], w=1.1)
    f.text((a + b) / 2, y + 16, label, size=11.5)


def f14_8():
    f = Fig(780, 500)
    # ---------------- HF: divi atstarojumi no F slāņa
    f.text(30, 22, "HF: divi atstarojumi no F slāņa", anchor="start", size=14, bold=True)
    f.rect(30, 38, 720, 22, fill=BLUE_T, rx=0, sw=0.6, color=BLUE)
    f.text(742, 54, "F slānis", anchor="end", size=12, bold=True, color=BLUE)
    yg = 180
    _groundline(f, 30, 750, yg)
    f.line(60, yg, 60, yg - 30, w=3)
    _hop(f, [(60, yg - 30), (230, 60), (400, yg), (570, 60), (740, yg)])
    f.circ(400, yg, 4, fill=K)
    f.ltext(400, yg - 18, "atstarojas no Zemes", size=11, italic=True)
    _span(f, 60, 400, yg + 22, "1. atstarojums: līdz 3000–4000 km")
    _span(f, 400, 740, yg + 22, "2. atstarojums")
    # ---------------- 6 m: Es un Es + F2
    y0 = 262
    f.text(30, y0, "6 m: sporādiskais E, arī kopā ar F2", anchor="start", size=14, bold=True)
    f.rect(30, y0 + 16, 720, 20, fill="white", rx=0, sw=1, dash="5 4", color=BLUE)
    f.text(742, y0 + 31, "F2 slānis (Saules maksimuma gados)", anchor="end", size=11, color=BLUE)
    ye = y0 + 92
    f.line(30, ye, 750, ye, dash="2 5", w=1, color=MG)
    f.text(34, ye - 6, "E slānis", anchor="start", size=11, color=MG)
    _cloud(f, 190, ye); _cloud(f, 420, ye)
    f.text(190, ye - 17, "Es mākonis", size=11, color=BLUE)
    f.text(420, ye - 17, "Es mākonis", size=11, color=BLUE)
    yg2 = y0 + 190
    _groundline(f, 30, 750, yg2)
    f.line(60, yg2, 60, yg2 - 30, w=3)
    _hop(f, [(60, yg2 - 30), (190, ye + 11), (320, yg2), (420, ye + 11), (520, yg2)])
    _hop(f, [(320, yg2), (580, y0 + 36), (740, yg2)], dash="7 5", color=GREEN)
    f.text(500, yg2 - 40, "Es + Es", anchor="start", size=12, bold=True, color=RED)
    f.text(690, y0 + 78, "Es + F2", anchor="start", size=12, bold=True, color=GREEN)
    _span(f, 60, 320, yg2 + 22, "Es atstarojums: līdz ~2000 km")
    f.save("atteli/14-8-vairaki-lecieni.svg", "Vairākkārtēja atstarošanās: HF no F slāņa, 6 m no sporādiskā E un F2")


ALL = [f14_8]
