#!/usr/bin/env python3
"""Grāmatas zīmējumu ģenerators.

Palaišana:  python3 riki/zimet.py        (no mapes gramata/)
Rezultāts:  SVG faili mapē atteli/

Visi zīmējumi ir oriģināli, veidoti šai grāmatai; licence CC BY-NC-SA 4.0.
Stils: melnbalts, līnijas 1,6 px, fonts DejaVu Sans, shēmu apzīmējumi pēc IEC.
Lai mainītu zīmējumu, labo attiecīgo funkciju un palaid skriptu vēlreiz.
"""
import math, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "atteli")
FONT = "DejaVu Sans, Arial, Helvetica, sans-serif"
G = "#e6e6e6"   # gaiši pelēks aizpildījums
D = "#888"      # tumšāk pelēks


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class S:
    def __init__(s, w, h):
        s.w, s.h, s.e = w, h, []

    def add(s, x):
        s.e.append(x)

    def line(s, x1, y1, x2, y2, dash=None, w=1.6, col="#000", arrow=False):
        a = ' marker-end="url(#a)"' if arrow else ""
        d = f' stroke-dasharray="{dash}"' if dash else ""
        s.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{w}"{d}{a}/>')

    def arrow(s, x1, y1, x2, y2, dash=None, w=1.6, col="#000"):
        s.line(x1, y1, x2, y2, dash, w, col, True)

    def poly(s, pts, dash=None, w=1.6, fill="none", close=False, col="#000", arrow=False):
        p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        d = f' stroke-dasharray="{dash}"' if dash else ""
        a = ' marker-end="url(#a)"' if arrow else ""
        tag = "polygon" if close else "polyline"
        s.add(f'<{tag} points="{p}" fill="{fill}" stroke="{col}" stroke-width="{w}" stroke-linejoin="round"{d}{a}/>')

    def rect(s, x, y, w, h, fill="#fff", r=0, dash=None, sw=1.6, col="#000"):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        s.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}" fill="{fill}" stroke="{col}" stroke-width="{sw}"{d}/>')

    def circ(s, cx, cy, r, fill="#fff", dash=None, sw=1.6, col="#000"):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        s.add(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" stroke="{col}" stroke-width="{sw}"{d}/>')

    def path(s, d, fill="none", dash=None, w=1.6, col="#000", arrow=False):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        a = ' marker-end="url(#a)"' if arrow else ""
        s.add(f'<path d="{d}" fill="{fill}" stroke="{col}" stroke-width="{w}"{da}{a}/>')

    def text(s, x, y, t, size=14, anchor="middle", bold=False, italic=False, col="#000"):
        lines = t.split("\n")
        st = (' font-weight="bold"' if bold else "") + (' font-style="italic"' if italic else "")
        y0 = y - (len(lines) - 1) * size * 0.6
        for i, ln in enumerate(lines):
            s.add(f'<text x="{x:.1f}" y="{y0 + i * size * 1.2:.1f}" font-family="{FONT}" font-size="{size}" '
                  f'text-anchor="{anchor}" fill="{col}"{st}>{esc(ln)}</text>')

    def box(s, cx, cy, w, h, label, size=13, fill="#fff", dash=None):
        s.rect(cx - w / 2, cy - h / 2, w, h, fill=fill, r=3, dash=dash)
        s.text(cx, cy + size * 0.36, label, size)

    def dot(s, x, y):
        s.circ(x, y, 2.6, fill="#000")

    # --- simboli -------------------------------------------------------
    def antenna(s, x, y, h=44):
        s.line(x, y, x, y - h)
        s.poly([(x - 13, y - h), (x, y - h + 20), (x + 13, y - h)])
        s.line(x - 13, y - h, x + 13, y - h)

    def ground(s, x, y):
        s.line(x, y, x, y + 8)
        for i, hw in enumerate((12, 8, 4)):
            s.line(x - hw, y + 8 + i * 5, x + hw, y + 8 + i * 5)

    def speaker(s, x, y):
        s.rect(x, y - 8, 9, 16)
        s.poly([(x + 9, y - 8), (x + 24, y - 20), (x + 24, y + 20), (x + 9, y + 8)], close=True, fill="#fff")

    def mic(s, x, y):
        s.circ(x, y, 10)
        s.line(x - 14, y - 12, x - 14, y + 12, w=2.4)

    def res_h(s, cx, cy, w=46, h=18, label=None):
        s.rect(cx - w / 2, cy - h / 2, w, h)
        if label:
            s.text(cx, cy - h / 2 - 7, label, 13, italic=True)

    def res_v(s, cx, cy, w=18, h=46, label=None):
        s.rect(cx - w / 2, cy - h / 2, w, h)
        if label:
            s.text(cx + w / 2 + 8, cy + 5, label, 13, anchor="start", italic=True)

    def cap_h(s, cx, cy, gap=8, ph=26):
        s.line(cx - gap / 2, cy - ph / 2, cx - gap / 2, cy + ph / 2, w=2.4)
        s.line(cx + gap / 2, cy - ph / 2, cx + gap / 2, cy + ph / 2, w=2.4)

    def cap_v(s, cx, cy, gap=8, pw=26):
        s.line(cx - pw / 2, cy - gap / 2, cx + pw / 2, cy - gap / 2, w=2.4)
        s.line(cx - pw / 2, cy + gap / 2, cx + pw / 2, cy + gap / 2, w=2.4)

    def coil_h(s, x, y, n=4, r=7):
        d = f"M {x} {y} " + " ".join(f"a {r} {r} 0 0 1 {2 * r} 0" for _ in range(n))
        s.path(d)
        return x + 2 * r * n

    def coil_v(s, x, y, n=4, r=7, right=True):
        sw = 1 if right else 0
        d = f"M {x} {y} " + " ".join(f"a {r} {r} 0 0 {sw} 0 {2 * r}" for _ in range(n))
        s.path(d)
        return y + 2 * r * n

    def battery_v(s, x, cy):
        s.line(x - 14, cy - 5, x + 14, cy - 5)
        s.line(x - 7, cy + 5, x + 7, cy + 5, w=3.2)
        s.text(x - 20, cy - 3, "+", 14, anchor="end")
        s.text(x - 20, cy + 14, "−", 14, anchor="end")

    def diode_h(s, cx, cy, kind="d"):
        s.poly([(cx - 10, cy - 11), (cx - 10, cy + 11), (cx + 10, cy)], close=True, fill="#fff")
        if kind == "z":
            s.poly([(cx + 15, cy - 13), (cx + 10, cy - 11), (cx + 10, cy + 11), (cx + 5, cy + 13)])
        else:
            s.line(cx + 10, cy - 11, cx + 10, cy + 11)
        if kind == "led":
            s.arrow(cx - 2, cy - 15, cx + 9, cy - 29, w=1.3)
            s.arrow(cx + 8, cy - 13, cx + 19, cy - 27, w=1.3)

    def meter(s, cx, cy, letter):
        s.circ(cx, cy, 15)
        s.text(cx, cy + 5, letter, 15, bold=True)

    def sine(s, x0, y0, w, amp, cycles, n=240, ph=0.0, dash=None, lw=1.6, fn=None):
        pts = []
        for i in range(n + 1):
            t = i / n
            v = fn(t) if fn else math.sin(2 * math.pi * cycles * t + ph)
            pts.append((x0 + w * t, y0 - amp * v))
        s.poly(pts, dash=dash, w=lw)

    def axes(s, x, y, w, h, xl="", yl="", mid=False):
        """Asis: sākumpunkts (x, y) kreisajā apakšā; mid=True — laika ass pa vidu."""
        s.arrow(x, y, x, y - h - 12, w=1.2)
        ya = y - h / 2 if mid else y
        s.arrow(x, ya, x + w + 14, ya, w=1.2)
        if xl:
            s.text(x + w + 12, ya + 18, xl, 12, anchor="end", italic=True)
        if yl:
            s.text(x - 6, y - h - 4, yl, 12, anchor="end", italic=True)

    def chain(s, x0, y, labels, bw=88, bh=46, gap=24, size=13, fills=None):
        """Bloku virkne ar bultiņām; atgriež bloku centru sarakstu."""
        cs = []
        for i, lb in enumerate(labels):
            cx = x0 + bw / 2 + i * (bw + gap)
            s.box(cx, y, bw, bh, lb, size, fill=(fills[i] if fills else "#fff"))
            if i:
                s.arrow(cx - bw / 2 - gap, y, cx - bw / 2 - 1, y)
            cs.append(cx)
        return cs

    def save(s, name):
        os.makedirs(OUT, exist_ok=True)
        head = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{s.w}" height="{s.h}" viewBox="0 0 {s.w} {s.h}">\n'
                '<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
                'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#000"/></marker></defs>\n'
                f'<rect width="{s.w}" height="{s.h}" fill="#fff"/>\n')
        with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f:
            f.write(head + "\n".join(s.e) + "\n</svg>\n")


FIGS = {}   # numurs -> (faila nosaukums, paraksts)


def fig(num, name, caption):
    def deco(fn):
        FIGS[num] = (name, caption, fn)
        return fn
    return deco


# ======================= 7. nodaļa ====================================
@fig("7.1", "07-1-kede-un-udens", "Elektriskā ķēde un tās salīdzinājums ar ūdens plūsmu caurulē")
def f71():
    s = S(700, 250)
    # elektriskā ķēde
    x1, x2, y1, y2 = 70, 270, 60, 200
    s.poly([(x1, 125), (x1, y1), (x2, y1), (x2, 107)])
    s.poly([(x2, 153), (x2, y2), (x1, y2), (x1, 135)])
    s.battery_v(x1, 130)
    s.res_v(x2, 130, label="R")
    s.text(x1 + 24, 135, "U", 14, anchor="start", italic=True)
    s.arrow(140, y1 - 12, 200, y1 - 12)
    s.text(170, y1 - 20, "I", 14, italic=True)
    s.text(170, 232, "Elektriskā ķēde", 13, bold=True)
    # ūdens analoģija
    a1, a2 = 430, 630
    s.poly([(a1, 112), (a1, y1), (a2, y1), (a2, 110)], w=5, col=D)
    s.poly([(a2, 150), (a2, y2), (a1, y2), (a1, 148)], w=5, col=D)
    s.circ(a1, 130, 18)
    s.text(a1, 135, "S", 14, bold=True)
    s.rect(a2 - 4, 110, 8, 40, fill=D, col=D)
    s.text(a1 - 26, 126, "sūknis", 12, anchor="end")
    s.text(a1 - 26, 142, "(spriegums)", 12, anchor="end")
    s.text(a2 + 14, 126, "sašaurinājums", 12, anchor="start")
    s.text(a2 + 14, 142, "(pretestība)", 12, anchor="start")
    s.arrow(500, y1 - 12, 560, y1 - 12)
    s.text(530, y1 - 20, "plūsma (strāva)", 12)
    s.text(530, 232, "Ūdens caurulē", 13, bold=True)
    return s


@fig("7.2", "07-2-oma-trijsturis", "Oma likuma trijstūris: aizklāj meklējamo lielumu")
def f72():
    s = S(520, 230)
    for i, (cx, hide) in enumerate(((90, None), (260, "U"), (430, "I"))):
        top, bl, br = (cx, 30), (cx - 70, 150), (cx + 70, 150)
        s.poly([top, bl, br], close=True, fill="#fff")
        s.line(cx - 35, 90, cx + 35, 90)
        s.line(cx, 90, cx, 150)
        for lab, (tx, ty) in (("U", (cx, 78)), ("I", (cx - 28, 135)), ("R", (cx + 28, 135))):
            if lab == hide:
                s.circ(tx, ty - 6, 16, fill=G, col=D)
            s.text(tx, ty, lab, 20, bold=True, italic=True, col=(D if lab == hide else "#000"))
    s.text(90, 185, "Trijstūris", 13)
    s.text(260, 185, "U = I · R", 15, bold=True)
    s.text(430, 185, "I = U / R", 15, bold=True)
    s.text(260, 210, "blakus — reizina", 12, col="#444")
    s.text(430, 210, "viens virs otra — dala", 12, col="#444")
    return s


@fig("7.3", "07-3-lidzstrava-mainstrava", "Līdzspriegums un maiņspriegums laikā; amplitūda, efektīvā vērtība un periods")
def f73():
    s = S(720, 270)
    # DC
    s.axes(50, 210, 190, 160, "t", "U", mid=True)
    s.line(50, 85, 240, 85, w=2.2)
    s.text(145, 250, "Līdzspriegums (DC)", 13, bold=True)
    # AC
    x0, ym, w, amp = 340, 130, 300, 70
    s.axes(x0, 210, w, 160, "t", "U", mid=True)
    s.sine(x0, ym, w, amp, 2, lw=2.2)
    s.line(x0, ym - amp * 0.707, x0 + w, ym - amp * 0.707, dash="5,4", w=1.1)
    s.text(x0 + w + 6, ym - amp * 0.707 + 4, "U RMS", 12, anchor="start")
    s.line(x0 + w / 8, ym - amp, x0 + w * 5 / 8 + 30, ym - amp, dash="2,3", w=1)
    s.arrow(x0 + w / 8, ym, x0 + w / 8, ym - amp + 1, w=1.2)
    s.text(x0 + w / 8 + 6, ym - amp / 2 + 14, "U max", 12, anchor="start")
    # periods
    s.line(x0 + w / 8, ym - amp - 6, x0 + w / 8, ym - amp - 24, w=1)
    s.line(x0 + w * 5 / 8, ym - amp - 6, x0 + w * 5 / 8, ym - amp - 24, w=1)
    s.add(f'<line x1="{x0 + w / 8 + 2}" y1="{ym - amp - 16}" x2="{x0 + w * 5 / 8 - 2}" y2="{ym - amp - 16}" stroke="#000" stroke-width="1.2" marker-start="url(#a)" marker-end="url(#a)"/>')
    s.text(x0 + w * 3 / 8, ym - amp - 22, "periods T", 12)
    # Up-p
    xp = x0 + w * 7 / 8
    s.line(xp - 30, ym + amp, xp + 34, ym + amp, dash="2,3", w=1)
    s.line(xp - 30, ym - amp, xp + 34, ym - amp, dash="2,3", w=1)
    s.add(f'<line x1="{xp + 26}" y1="{ym - amp + 2}" x2="{xp + 26}" y2="{ym + amp - 2}" stroke="#000" stroke-width="1.2" marker-start="url(#a)" marker-end="url(#a)"/>')
    s.text(xp + 32, ym + amp - 10, "U p-p", 12, anchor="start")
    s.text(x0 + w / 2, 250, "Maiņspriegums (AC)", 13, bold=True)
    return s


# ======================= 8. nodaļa ====================================
@fig("8.1", "08-1-elektromagnetiskais-vilnis", "Elektromagnētiskais vilnis: elektriskais (E) un magnētiskais (B) lauks ir perpendikulāri viens otram un izplatīšanās virzienam")
def f81():
    s = S(700, 260)
    x0, y0, w = 70, 130, 520
    s.arrow(x0 - 20, y0, x0 + w + 50, y0, w=1.2)
    s.text(x0 + w + 48, y0 + 20, "izplatīšanās virziens", 12, anchor="end", italic=True)
    n = 260
    pe, pb = [], []
    for i in range(n + 1):
        t = i / n
        v = math.sin(2 * math.pi * 2 * t)
        pe.append((x0 + w * t, y0 - 70 * v))
        pb.append((x0 + w * t - 38 * v, y0 + 26 * v))
    s.poly(pb, dash="6,4", w=1.8, col="#555")
    s.poly(pe, w=2.2)
    for k in range(4):
        t = (k + 0.5) / 4
        v = math.sin(2 * math.pi * 2 * t)
        x = x0 + w * t
        s.arrow(x, y0, x, y0 - 68 * v, w=1.1)
        s.arrow(x, y0, x - 36 * v, y0 + 24.5 * v, w=1.1, col="#555")
    s.arrow(x0 - 20, y0 + 40, x0 - 20, y0 - 90, w=1.2)
    s.arrow(x0 + 10, y0 - 20, x0 - 55, y0 + 25, w=1.2)
    s.text(x0 - 30, y0 - 84, "E", 16, bold=True, anchor="end")
    s.text(x0 - 62, y0 + 40, "B", 16, bold=True, col="#555")
    s.text(x0 + w * 0.125 + 12, y0 - 78, "elektriskais lauks", 12, anchor="start")
    s.text(x0 + w * 0.125 - 40, y0 + 62, "magnētiskais lauks", 12, anchor="start", col="#555")
    return s


@fig("8.2", "08-2-modulacijas-veidi", "Nesējs, amplitūdas modulācija (AM) un frekvences modulācija (FM)")
def f82():
    s = S(700, 420)
    x0, w = 150, 500
    rows = [("Informācijas\nsignāls (balss)", 55), ("Nesējs", 145), ("AM: mainās\namplitūda", 245), ("FM: mainās\nfrekvence", 355)]
    m = lambda t: math.sin(2 * math.pi * 1.5 * t)
    for lab, y in rows:
        s.text(x0 - 14, y + 5, lab, 13, anchor="end")
        s.line(x0, y, x0 + w, y, w=0.8, col="#999")
    s.sine(x0, 55, w, 26, 1.5, lw=2)
    s.sine(x0, 145, w, 30, 24, n=900)
    s.sine(x0, 245, w, 1, 0, n=900, fn=lambda t: 34 * (0.6 + 0.4 * m(t)) * math.sin(2 * math.pi * 24 * t))
    s.sine(x0, 245, w, 1, 0, n=200, dash="4,3", lw=1, fn=lambda t: 34 * (0.6 + 0.4 * m(t)))
    s.sine(x0, 245, w, 1, 0, n=200, dash="4,3", lw=1, fn=lambda t: -34 * (0.6 + 0.4 * m(t)))

    def fm(t):
        # fāze = 2π·(fc·t − β·cos(2π·fm·t)/(2π·fm))
        return math.sin(2 * math.pi * 24 * t - 9 / 1.5 * math.cos(2 * math.pi * 1.5 * t))
    s.sine(x0, 355, w, 30, 0, n=1400, fn=fm)
    s.text(x0 + w, 405, "laiks →", 12, anchor="end", italic=True)
    return s


@fig("8.3", "08-3-spektri", "Signālu spektri: AM, SSB, CW un FM aizņem dažāda platuma joslu")
def f83():
    s = S(720, 330)
    def panel(x, y, title, width):
        s.arrow(x, y, x + 300, y, w=1.2)
        s.text(x + 298, y + 17, "f", 12, anchor="end", italic=True)
        s.text(x + 150, y - 118, title, 13, bold=True)
        s.text(x + 150, y + 32, width, 12)
    # AM
    x, y = 30, 140
    panel(x, y, "AM", "ap 6 kHz")
    s.poly([(x + 80, y), (x + 80, y - 30), (x + 140, y - 50), (x + 140, y)], close=True, fill=G)
    s.poly([(x + 160, y), (x + 160, y - 50), (x + 220, y - 30), (x + 220, y)], close=True, fill=G)
    s.line(x + 150, y, x + 150, y - 95, w=3)
    s.text(x + 110, y - 58, "LSB", 12); s.text(x + 190, y - 58, "USB", 12); s.text(x + 150, y - 100, "nesējs", 12)
    # SSB
    x, y = 390, 140
    panel(x, y, "SSB (USB)", "2,4–3 kHz")
    s.poly([(x + 160, y), (x + 160, y - 50), (x + 220, y - 30), (x + 220, y)], close=True, fill=G)
    s.line(x + 150, y, x + 150, y - 95, w=1.4, dash="4,4", col=D)
    s.poly([(x + 80, y), (x + 80, y - 30), (x + 140, y - 50), (x + 140, y)], dash="4,4", col=D, w=1.1)
    s.text(x + 190, y - 58, "USB", 12); s.text(x + 150, y - 100, "nesējs nomākts", 12, col="#555")
    # CW
    x, y = 30, 300
    panel(x, y, "CW", "ap 100–500 Hz")
    s.rect(x + 146, y - 90, 8, 90, fill=G)
    # FM
    x, y = 390, 300
    panel(x, y, "FM", "ap 12–16 kHz")
    s.poly([(x + 30, y), (x + 50, y - 55), (x + 250, y - 55), (x + 270, y)], close=True, fill=G)
    return s


# ======================= 9. nodaļa ====================================
@fig("9.1", "09-1-rezistors", "Rezistora apzīmējums shēmā un rezistors ar krāsu joslām (4,7 kΩ ±5 %)")
def f91():
    s = S(700, 200)
    s.line(60, 80, 110, 80); s.line(156, 80, 206, 80)
    s.res_h(133, 80, label="R")
    s.text(133, 150, "Apzīmējums shēmā", 13, bold=True)
    # rezistors ar joslām
    cx = 480
    s.line(cx - 150, 80, cx - 80, 80, w=2.2, col=D); s.line(cx + 80, 80, cx + 150, 80, w=2.2, col=D)
    s.rect(cx - 80, 58, 160, 44, fill="#f4f4f4", r=14)
    bands = [(-55, "#bbb", "dzeltena\n4"), (-30, "#666", "violeta\n7"), (-5, "#999", "sarkana\n× 100"), (45, "#ddd", "zelta\n±5 %")]
    for dx, col, lab in bands:
        s.rect(cx + dx - 6, 58, 12, 44, fill=col, sw=1)
        s.line(cx + dx, 102, cx + dx, 122, w=0.9)
        s.text(cx + dx, 146, lab, 11)
    s.text(cx, 190, "Rezistors ar krāsu kodu", 13, bold=True)
    return s


@fig("9.2", "09-2-rezistoru-slegumi", "Rezistoru virknes un paralēlais slēgums")
def f92():
    s = S(700, 230)
    y = 90
    s.line(40, y, 90, y); s.res_h(113, y, label="R₁"); s.line(136, y, 190, y); s.res_h(213, y, label="R₂"); s.line(236, y, 290, y)
    s.dot(40, y); s.dot(290, y)
    s.arrow(52, y + 22, 84, y + 22, w=1.2); s.text(68, y + 40, "I", 13, italic=True)
    s.text(165, 185, "Virknē: viena strāva caur abiem", 13, bold=True)
    s.text(165, 208, "R = R₁ + R₂", 14)
    # paralēli
    xl, xr = 430, 630
    s.line(390, y, xl, y); s.line(xr, y, 670, y); s.dot(390, y); s.dot(670, y)
    for yy, lab, il in ((y - 35, "R₁", "I₁"), (y + 35, "R₂", "I₂")):
        s.poly([(xl, y), (xl, yy), (507, yy)]); s.poly([(553, yy), (xr, yy), (xr, y)])
        s.res_h(530, yy, label=lab)
        s.arrow(445, yy + (16 if yy > y else -16) + 5, 480, yy + (16 if yy > y else -16) + 5, w=1.2)
        s.text(462, yy + (38 if yy > y else -17), il, 13, italic=True)
    s.dot(xl, y); s.dot(xr, y)
    s.text(530, 185, "Paralēli: vienāds spriegums uz abiem", 13, bold=True)
    s.text(530, 208, "R = R₁ · R₂ / (R₁ + R₂)", 14)
    return s


@fig("9.3", "09-3-kondensatori", "Kondensatoru apzīmējumi shēmā")
def f93():
    s = S(700, 170)
    for cx, lab, kind in ((120, "Kondensators", 0), (350, "Elektrolītiskais\n(ar polaritāti)", 1), (580, "Maināmais", 2)):
        y = 65
        s.line(cx - 60, y, cx - 4, y); s.line(cx + 4, y, cx + 60, y)
        if kind == 1:
            s.rect(cx - 8, y - 14, 5, 28, fill="#fff", sw=1.8)
            s.line(cx + 4, y - 14, cx + 4, y + 14, w=2.4)
            s.text(cx - 20, y - 12, "+", 16, bold=True)
        else:
            s.cap_h(cx, y)
        if kind == 2:
            s.arrow(cx - 22, y + 24, cx + 22, y - 24, w=1.4)
        s.text(cx, 135, lab, 13)
    return s


@fig("9.4", "09-4-spoles", "Spoles apzīmējumi shēmā")
def f94():
    s = S(520, 160)
    for cx, lab, core in ((130, "Spole", False), (390, "Spole ar serdi", True)):
        y = 70
        s.line(cx - 70, y, cx - 28, y)
        e = s.coil_h(cx - 28, y, 4, 7)
        s.line(e, y, cx + 70, y)
        if core:
            s.line(cx - 28, y - 16, cx + 28, y - 16, w=2.2)
        s.text(cx, 125, lab, 13)
    return s


@fig("9.5", "09-5-transformators", "Transformators: primārais tinums N₁, serde un sekundārais tinums N₂")
def f95():
    s = S(520, 230)
    cx, y0 = 260, 55
    s.coil_v(cx - 14, y0, 6, 9, right=True)
    s.coil_v(cx + 14, y0, 6, 9, right=False)
    s.line(cx - 3, y0 - 6, cx - 3, y0 + 114, w=2); s.line(cx + 3, y0 - 6, cx + 3, y0 + 114, w=2)
    for sx, sign in ((cx - 14, -1), (cx + 14, 1)):
        s.line(sx, y0, sx + sign * 80, y0); s.line(sx, y0 + 108, sx + sign * 80, y0 + 108)
        s.circ(sx + sign * 80, y0, 3.5); s.circ(sx + sign * 80, y0 + 108, 3.5)
    s.text(cx - 115, y0 + 60, "U₁", 15, italic=True); s.text(cx + 115, y0 + 60, "U₂", 15, italic=True)
    s.text(cx - 50, y0 + 60, "N₁", 14, italic=True); s.text(cx + 50, y0 + 60, "N₂", 14, italic=True)
    s.text(cx - 80, 205, "primārais tinums", 12); s.text(cx + 80, 205, "sekundārais tinums", 12)
    s.text(cx, 30, "serde", 12)
    return s


@fig("9.6", "09-6-diodes", "Diodes, gaismas diodes un Zenera diodes apzīmējumi; strāva plūst no anoda (A) uz katodu (K)")
def f96():
    s = S(700, 180)
    for cx, lab, kind in ((120, "Diode", "d"), (350, "Gaismas diode (LED)", "led"), (580, "Zenera diode", "z")):
        y = 80
        s.line(cx - 60, y, cx - 10, y); s.line(cx + 10, y, cx + 60, y)
        s.diode_h(cx, y, kind)
        s.text(cx - 52, y + 22, "A", 13, bold=True); s.text(cx + 52, y + 22, "K", 13, bold=True)
        s.text(cx, 150, lab, 13)
    s.arrow(85, 40, 155, 40, w=1.2); s.text(120, 32, "strāvas virziens", 11)
    return s


@fig("9.7", "09-7-tranzistori", "Bipolāro tranzistoru (NPN, PNP) un lauktranzistora apzīmējumi")
def f97():
    s = S(700, 230)
    for cx, lab, kind in ((120, "NPN", "npn"), (350, "PNP", "pnp")):
        cy = 100
        s.circ(cx, cy, 30)
        s.line(cx - 10, cy - 18, cx - 10, cy + 18, w=3)
        s.line(cx - 60, cy, cx - 10, cy)
        s.poly([(cx - 10, cy - 8), (cx + 16, cy - 24), (cx + 16, cy - 60)])
        if kind == "npn":
            s.arrow(cx - 10, cy + 8, cx + 16, cy + 24)
        else:
            s.arrow(cx + 16, cy + 24, cx - 8, cy + 9)
        s.line(cx + 16, cy + 24, cx + 16, cy + 60)
        s.text(cx - 66, cy + 5, "B", 14, bold=True, anchor="end")
        s.text(cx + 26, cy - 48, "C", 14, bold=True, anchor="start")
        s.text(cx + 26, cy + 58, "E", 14, bold=True, anchor="start")
        s.text(cx, 205, lab, 13, bold=True)
    cx, cy = 580, 100
    s.circ(cx, cy, 30)
    s.line(cx - 4, cy - 18, cx - 4, cy + 18, w=3)
    s.arrow(cx - 60, cy, cx - 6, cy)
    s.poly([(cx - 4, cy - 12), (cx + 16, cy - 12), (cx + 16, cy - 60)])
    s.poly([(cx - 4, cy + 12), (cx + 16, cy + 12), (cx + 16, cy + 60)])
    s.text(cx - 66, cy + 5, "G", 14, bold=True, anchor="end")
    s.text(cx + 26, cy - 48, "D", 14, bold=True, anchor="start")
    s.text(cx + 26, cy + 58, "S", 14, bold=True, anchor="start")
    s.text(cx, 205, "Lauktranzistors (FET)", 13, bold=True)
    return s


# ======================= 10. nodaļa ===================================
@fig("10.1", "10-1-kontura-rezonanse", "Virknes un paralēlais svārstību kontūrs un to pretestība atkarībā no frekvences")
def f101():
    s = S(720, 330)
    # virknes
    y = 60
    s.line(50, y, 100, y); e = s.coil_h(100, y, 4, 7); s.line(e, y, 206, y); s.cap_h(210, y); s.line(214, y, 290, y)
    s.dot(50, y); s.dot(290, y)
    s.text(128, y - 14, "L", 13, italic=True); s.text(210, y - 20, "C", 13, italic=True)
    s.text(170, 115, "Virknes kontūrs", 13, bold=True)
    gx, gy, gw, gh = 70, 290, 200, 120
    s.axes(gx, gy, gw, gh, "f", "Z")
    s.sine(gx, gy, gw, 1, 0, fn=lambda t: 12 + 100 * min(1, abs(t - 0.5) * 3.2) ** 0.9, lw=2.2)
    s.line(gx + gw / 2, gy, gx + gw / 2, gy - gh, dash="4,4", w=1); s.text(gx + gw / 2, gy + 17, "f₀", 13, italic=True)
    s.text(gx + gw / 2 + 8, gy - 20, "minimums", 12, anchor="start")
    # paralēlais
    xl, xr = 470, 610
    s.line(430, y, xl, y); s.line(xr, y, 650, y); s.dot(430, y); s.dot(650, y); s.dot(xl, y); s.dot(xr, y)
    s.poly([(xl, y), (xl, y - 28), (512, y - 28)]); e = s.coil_h(512, y - 28, 4, 7); s.poly([(e, y - 28), (xr, y - 28), (xr, y)])
    s.poly([(xl, y), (xl, y + 28), (536, y + 28)]); s.cap_h(540, y + 28); s.poly([(544, y + 28), (xr, y + 28), (xr, y)])
    s.text(540, y - 42, "L", 13, italic=True); s.text(563, y + 33, "C", 13, italic=True, anchor="start")
    s.text(540, 130, "Paralēlais kontūrs", 13, bold=True)
    gx = 440
    s.axes(gx, gy, gw, gh, "f", "Z")
    s.sine(gx, gy, gw, 1, 0, fn=lambda t: 10 + 100 / (1 + ((t - 0.5) * 9) ** 2), lw=2.2)
    s.line(gx + gw / 2, gy, gx + gw / 2, gy - gh, dash="4,4", w=1); s.text(gx + gw / 2, gy + 17, "f₀", 13, italic=True)
    s.text(gx + gw / 2 + 10, gy - 104, "maksimums", 12, anchor="start")
    return s


@fig("10.2", "10-2-filtri", "Četru filtru veidu caurlaidības līknes")
def f102():
    s = S(720, 360)
    sig = lambda z: 1 / (1 + math.exp(z))
    defs = [
        ("Zemo frekvenču filtrs (LPF)", lambda t: sig((t - 0.5) * 22), [0.5]),
        ("Augsto frekvenču filtrs (HPF)", lambda t: sig(-(t - 0.5) * 22), [0.5]),
        ("Joslas filtrs (BPF)", lambda t: sig(-(t - 0.33) * 26) * sig((t - 0.67) * 26), [0.33, 0.67]),
        ("Sprostfiltrs (BSF)", lambda t: 1 - sig(-(t - 0.33) * 26) * sig((t - 0.67) * 26), [0.33, 0.67]),
    ]
    for i, (title, fn, marks) in enumerate(defs):
        gx = 60 + (i % 2) * 350
        gy = 150 + (i // 2) * 180
        gw, gh = 240, 90
        s.axes(gx, gy, gw, gh, "f", "")
        s.sine(gx, gy, gw, 1, 0, fn=lambda t, fn=fn: 4 + 80 * fn(t), lw=2.2)
        for m in marks:
            s.line(gx + gw * m, gy, gx + gw * m, gy - gh, dash="4,4", w=1)
            s.text(gx + gw * m, gy + 16, "f r", 12, italic=True)
        s.text(gx + gw / 2, gy - gh - 22, title, 13, bold=True)
        s.text(gx - 8, gy - 78, "laiž", 11, anchor="end"); s.text(gx - 8, gy - 2, "aiztur", 11, anchor="end")
    return s


@fig("10.3", "10-3-barosanas-bloks", "Barošanas bloka četras pakāpes un sprieguma forma pēc katras no tām")
def f103():
    s = S(720, 250)
    labels = ["Transfor-\nmators", "Taisngriezis", "Filtrs", "Stabilizators"]
    cs = s.chain(105, 170, labels, bw=104, bh=48, gap=46, size=13)
    s.arrow(40, 170, 104, 170); s.arrow(cs[-1] + 52, 170, cs[-1] + 110, 170)
    s.text(40, 205, "230 V ~", 12); s.text(cs[-1] + 96, 205, "13,8 V =", 12)
    xs = [58] + [(cs[i] + cs[i + 1]) / 2 for i in range(3)] + [cs[-1] + 86]
    waves = [
        (lambda t: math.sin(2 * math.pi * 2 * t), 26),
        (lambda t: math.sin(2 * math.pi * 2 * t), 11),
        (lambda t: abs(math.sin(2 * math.pi * 2 * t)), 20),
        (lambda t: 0.82 + 0.18 * abs(math.sin(2 * math.pi * 2 * t)) ** 0.5, 20),
        (lambda t: 0.72, 20),
    ]
    for x, (fn, amp) in zip(xs, waves):
        y = 75
        s.line(x - 28, y, x + 28, y, w=0.7, col="#999")
        s.sine(x - 26, y, 52, amp, 0, fn=fn, lw=1.8, n=120)
    s.text(360, 22, "Sprieguma forma", 12, italic=True)
    for x in xs:
        s.line(x, 110, x, 150, dash="2,3", w=0.9, col="#777")
    return s


# ======================= 11. nodaļa ===================================
def _ant_in(s, x, y):
    """Antena ar pievadu līdz punktam (x, y)."""
    s.antenna(x - 28, y - 4)
    s.poly([(x - 28, y - 4), (x - 28, y), (x - 1, y)], arrow=True)


def _spk_out(s, x, y, label="skaļrunis"):
    s.arrow(x, y, x + 24, y)
    s.speaker(x + 26, y)
    s.text(x + 40, y + 40, label, 11)


def _below(s, cx, y, label, bw=88, bh=40, dy=78, dash=None):
    s.box(cx, y + dy, bw, bh, label, 12, dash=dash)
    s.arrow(cx, y + dy - bh / 2, cx, y + 24)


@fig("11.1", "11-1-detektoruztverejs", "Detektoruztvērēja blokshēma")
def f111():
    s = S(620, 190)
    y = 90
    cs = s.chain(90, y, ["Svārstību\nkontūrs", "Detektors\n(diode)", "Austiņas"], bw=110, gap=40)
    _ant_in(s, cs[0] - 55, y)
    s.line(cs[0], y + 23, cs[0], y + 45); s.ground(cs[0], y + 45)
    s.text(cs[0] + 22, y + 62, "zemējums", 11, anchor="start")
    s.text(cs[0] - 83, y + 22, "antena", 11)
    return s


@fig("11.2", "11-2-tiesa-pastiprinajuma-uztverejs", "Tiešā pastiprinājuma uztvērēja blokshēma")
def f112():
    s = S(700, 170)
    y = 85
    cs = s.chain(80, y, ["Ieejas\nkontūrs", "AFP", "Detektors", "ZFP"], bw=104, gap=34)
    _ant_in(s, cs[0] - 52, y)
    _spk_out(s, cs[-1] + 52, y)
    return s


@fig("11.3", "11-3-superheterodins", "Superheterodīna uztvērēja blokshēma")
def f113():
    s = S(740, 250)
    y = 80
    cs = s.chain(64, y, ["AFP", "Jaucējs", "SF\nfiltrs", "SFP", "Detektors", "ZFP"], bw=84, gap=22, size=13)
    _ant_in(s, cs[0] - 42, y)
    _spk_out(s, cs[-1] + 42, y)
    _below(s, cs[1], y, "Heterodīns", bw=96)
    _below(s, cs[4], y, "Otrais\nheterodīns", bw=96, dash="5,3")
    s.text(cs[4] + 54, y + 96, "SSB un CW\nuztveršanai", 11, anchor="start")
    s.line(cs[1] + 42, y + 38, cs[3] + 42, y + 38, w=1); s.line(cs[1] + 42, y + 30, cs[1] + 42, y + 38, w=1); s.line(cs[3] + 42, y + 30, cs[3] + 42, y + 38, w=1)
    s.text((cs[2] + cs[3]) / 2 + 20, y + 54, "starpfrekvence (nemainīga)", 11)
    s.text(cs[0], y - 34, "signāla frekvence", 11)
    s.text(cs[5], y - 34, "skaņas frekvence", 11)
    return s


@fig("11.4", "11-4-tiesas-parveidosanas-uztverejs", "Tiešās pārveidošanas uztvērēja blokshēma")
def f114():
    s = S(700, 230)
    y = 80
    cs = s.chain(80, y, ["Ieejas\nfiltrs", "Jaucējs", "ZF\nfiltrs", "ZFP"], bw=104, gap=34)
    _ant_in(s, cs[0] - 52, y)
    _spk_out(s, cs[-1] + 52, y)
    _below(s, cs[1], y, "Heterodīns", bw=104)
    s.text(cs[1] + 60, y + 82, "noskaņots uz\nsignāla frekvenci", 11, anchor="start")
    return s


@fig("11.5", "11-5-sdr", "SDR uztvērēja blokshēma: aparatūra pārvērš signālu skaitļos, pārējo dara programma")
def f115():
    s = S(720, 230)
    y = 110
    s.rect(52, y - 50, 300, 100, fill="#fafafa", dash="6,4", r=6, sw=1.1)
    s.rect(372, y - 50, 190, 100, fill="#fafafa", dash="6,4", r=6, sw=1.1)
    s.text(202, y - 60, "Aparatūra", 12, italic=True); s.text(467, y - 60, "Programma", 12, italic=True)
    cs = s.chain(72, y, ["Ieejas\nfiltrs", "Pastipri-\nnātājs", "Analogciparu\npārveidotājs"], bw=84, gap=14, size=12)
    s.box(467, y, 150, 56, "Signālu apstrāde", 13, fill=G)
    s.arrow(cs[2] + 42, y, 391, y)
    _ant_in(s, cs[0] - 42, y)
    _spk_out(s, 542, y, "skaņa")
    s.text(467, y + 76, "filtri · demodulators · AGC · spektra attēls", 11)
    return s


# ======================= 12. nodaļa ===================================
def _ant_out(s, x, y):
    s.poly([(x, y), (x + 30, y), (x + 30, y - 4)])
    s.antenna(x + 30, y - 4)


@fig("12.1", "12-1-cw-raiditajs", "CW raidītāja blokshēma")
def f121():
    s = S(720, 230)
    y = 80
    cs = s.chain(40, y, ["Ģenerators", "Starppakāpe /\nreizinātājs", "Jaudas pastip-\nrinātājs", "Zemo frek-\nvenču filtrs"], bw=116, gap=32, size=12)
    _ant_out(s, cs[-1] + 58, y)
    _below(s, cs[1], y, "Telegrāfa\natslēga", bw=104)
    return s


@fig("12.2", "12-2-am-raiditajs", "AM raidītāja blokshēma")
def f122():
    s = S(720, 250)
    y = 70
    cs = s.chain(40, y, ["Ģenerators", "Starppakāpe", "Jaudas pastip-\nrinātājs", "Zemo frek-\nvenču filtrs"], bw=116, gap=32, size=12)
    _ant_out(s, cs[-1] + 58, y)
    y2 = y + 110
    s.mic(cs[0] - 20, y2); s.text(cs[0] - 20, y2 + 30, "mikrofons", 11)
    s.box(cs[1], y2, 116, 44, "ZFP", 13)
    s.box(cs[2], y2, 116, 44, "Modulators", 13)
    s.arrow(cs[0] - 8, y2, cs[1] - 59, y2)
    s.arrow(cs[1] + 58, y2, cs[2] - 59, y2)
    s.arrow(cs[2], y2 - 22, cs[2], y + 24)
    s.text(cs[2] + 10, y + 58, "maina amplitūdu", 11, anchor="start")
    return s


@fig("12.3", "12-3-fm-raiditajs", "FM raidītāja blokshēma")
def f123():
    s = S(740, 190)
    y = 80
    cs = s.chain(70, y, ["ZFP", "Ģenerators ar\nfrekvences\nmodulatoru", "Reizinātāji", "Jaudas pastip-\nrinātājs", "Zemo frek-\nvenču filtrs"], bw=108, bh=58, gap=20, size=12)
    s.mic(34, y); s.text(34, y + 30, "mikrofons", 11); s.arrow(46, y, cs[0] - 55, y)
    _ant_out(s, cs[-1] + 54, y)
    return s


@fig("12.4", "12-4-ssb-raiditajs", "SSB raidītāja blokshēma (filtra metode) un signāla spektrs pēc galvenajiem blokiem")
def f124():
    s = S(720, 440)
    y = 120
    cs = s.chain(96, y, ["ZFP", "Balansa\nmodulators", "SSB filtrs"], bw=112, bh=48, gap=40, size=12)
    s.mic(40, y); s.text(40, y + 30, "mikrofons", 11); s.arrow(52, y, cs[0] - 57, y)
    _below(s, cs[1], y, "Nesēja\nģenerators", bw=104)
    # spektri virs blokiem
    def spec(cx, yy, kind):
        s.line(cx - 34, yy, cx + 34, yy, w=1)
        if kind in ("dsb", "am"):
            s.poly([(cx - 24, yy), (cx - 24, yy - 9), (cx - 5, yy - 18), (cx - 5, yy)], close=True, fill=G, w=1.1)
        s.poly([(cx + 5, yy), (cx + 5, yy - 18), (cx + 24, yy - 9), (cx + 24, yy)], close=True, fill=G, w=1.1)
        s.line(cx, yy, cx, yy - 26, w=(2.2 if kind == "am" else 1), dash=(None if kind == "am" else "2,2"), col=("#000" if kind == "am" else D))
    spec(cs[1], y - 40, "dsb"); s.text(cs[1], y - 76, "abas sānjoslas,\nnesējs nomākts", 11)
    spec(cs[2], y - 40, "ssb"); s.text(cs[2], y - 76, "viena sānjosla", 11)
    # otrā rinda
    y2 = 320
    cs2 = s.chain(40, y2, ["Jaucējs", "Joslas\nfiltrs", "Lineārais\njaudas pastip-\nrinātājs", "Zemo frek-\nvenču filtrs"], bw=112, bh=58, gap=32, size=12)
    # savienojums no SSB filtra uz jaucēju
    s.poly([(cs[2] + 56, y), (cs[2] + 90, y), (cs[2] + 90, y + 132), (20, y + 132), (20, y2), (39, y2)], arrow=True)
    _below(s, cs2[0], y2, "VFO", bw=90, dy=84)
    s.text(cs2[0] + 52, y2 + 88, "nosaka darba\nfrekvenci", 11, anchor="start")
    _ant_out(s, cs2[-1] + 56, y2)
    s.text(cs2[2], y2 + 52, "nedrīkst kropļot signālu", 11)
    s.text(cs2[3], y2 + 52, "aiztur harmonikas", 11)
    return s


# ======================= 13. nodaļa ===================================
@fig("13.1", "13-1-dipols", "Pusviļņa dipols: divi pleci, izolatori un koaksiālais pievads vidū")
def f131():
    s = S(720, 300)
    yg, yw = 270, 80
    s.line(20, yg, 700, yg, w=1.2);
    for x in range(30, 700, 22):
        s.line(x, yg, x - 8, yg + 8, w=0.8, col="#777")
    for mx in (60, 660):
        s.line(mx, yg, mx, 55, w=3.5, col="#555")
    s.line(60, 62, 120, yw, w=1, dash="5,3"); s.line(660, 62, 600, yw, w=1, dash="5,3")
    s.circ(124, yw, 5); s.circ(596, yw, 5)
    s.line(129, yw, 345, yw, w=2.4); s.line(375, yw, 591, yw, w=2.4)
    s.rect(345, yw - 9, 30, 18, fill=G)
    s.line(357, yw + 9, 357, 232, w=1.4); s.line(363, yw + 9, 363, 232, w=1.4)
    s.poly([(357, 232), (357, 244), (420, 244)], w=1.4); s.poly([(363, 232), (363, 238), (420, 238)], w=1.4)
    s.text(428, 246, "uz transīveru", 12, anchor="start")
    s.text(372, 170, "koaksiālais kabelis", 12, anchor="start")
    s.text(360, yw + 30, "", 12)
    s.text(237, yw + 22, "plecs", 12); s.text(483, yw + 22, "plecs", 12)
    s.text(360, yw - 16, "centra izolators\nvai baluns", 11)
    s.text(124, yw - 12, "izolators", 11); s.text(596, yw - 12, "izolators", 11)
    s.text(92, 98, "virve", 11, anchor="end")
    yd = 32
    s.line(124, yd - 6, 124, yd + 6, w=1); s.line(596, yd - 6, 596, yd + 6, w=1)
    s.add(f'<line x1="126" y1="{yd}" x2="594" y2="{yd}" stroke="#000" stroke-width="1.2" marker-start="url(#a)" marker-end="url(#a)"/>')
    s.text(360, yd - 8, "L = λ/2 · 0,95  ≈  142,5 / f [MHz]  metri", 13, bold=True)
    return s


@fig("13.2", "13-2-dipola-varianti", "Dipola varianti: Inverted-V, vairākjoslu dipols un OCF dipols")
def f132():
    s = S(720, 260)
    yg = 200
    # Inverted-V
    cx = 120
    s.line(30, yg, 215, yg, w=1.2)
    s.line(cx, yg, cx, 50, w=3.5, col="#555")
    s.line(cx, 55, 40, 160, w=2.4); s.line(cx, 55, 200, 160, w=2.4)
    s.line(40, 160, 34, yg, w=1, dash="4,3"); s.line(200, 160, 206, yg, w=1, dash="4,3")
    s.rect(cx - 8, 48, 16, 12, fill=G)
    s.line(cx + 4, 60, cx + 4, yg, w=1.2)
    s.text(cx, 235, "Inverted-V", 13, bold=True)
    # fan
    cx = 360
    s.line(255, yg, 465, yg, w=1.2)
    s.line(cx, yg, cx, 50, w=3.5, col="#555")
    for dx, dy in ((100, 20), (75, 55), (50, 85)):
        s.line(cx, 55, cx - dx, 55 + dy, w=2.2); s.line(cx, 55, cx + dx, 55 + dy, w=2.2)
    s.rect(cx - 8, 48, 16, 12, fill=G)
    s.line(cx + 4, 60, cx + 4, yg, w=1.2)
    s.text(cx + 104, 60, "80 m", 11, anchor="start"); s.text(cx + 80, 104, "15 m", 11, anchor="start"); s.text(cx + 56, 150, "10 m", 11, anchor="start")
    s.text(cx, 235, "Vairākjoslu dipols", 13, bold=True)
    # OCF
    x0 = 500
    s.line(x0, yg, 710, yg, w=1.2)
    s.line(x0 + 8, yg, x0 + 8, 50, w=3.5, col="#555"); s.line(702, yg, 702, 50, w=3.5, col="#555")
    s.line(x0 + 8, 60, x0 + 20, 70, w=1, dash="4,3"); s.line(702, 60, 690, 70, w=1, dash="4,3")
    s.line(x0 + 20, 70, x0 + 72, 70, w=2.4); s.line(x0 + 96, 70, 690, 70, w=2.4)
    s.rect(x0 + 72, 60, 24, 20, fill=G); s.text(x0 + 84, 74, "4:1", 10)
    s.line(x0 + 84, 80, x0 + 84, yg, w=1.2)
    s.text(x0 + 46, 56, "⅓", 14); s.text(x0 + 145, 56, "⅔", 14)
    s.text(x0 + 105, 235, "OCF dipols", 13, bold=True)
    return s


@fig("13.3", "13-3-vertikala-antena", "Ceturtdaļviļņa vertikālā antena ar radiāļiem un tās starojums skatā no augšas")
def f133():
    s = S(720, 290)
    bx, by = 200, 190
    s.line(bx, by, bx, 30, w=3)
    for dx, dy in ((-130, 46), (-60, 62), (60, 62), (130, 46)):
        s.line(bx, by, bx + dx, by + dy, w=1.8)
    s.circ(bx, by, 6, fill=G)
    s.line(bx + 2, by + 6, bx + 2, 270, w=1.2); s.line(bx + 7, by + 5, bx + 7, 270, w=1.2)
    s.line(bx + 34, 30, bx + 34, by, w=1)
    s.add(f'<line x1="{bx + 34}" y1="32" x2="{bx + 34}" y2="{by - 2}" stroke="#000" stroke-width="1.2" marker-start="url(#a)" marker-end="url(#a)"/>')
    s.text(bx + 42, 115, "λ/4", 14, anchor="start", bold=True)
    s.text(bx - 110, by + 30, "radiāļi", 12, anchor="end")
    s.text(bx + 16, 266, "koaksiālais kabelis", 12, anchor="start")
    # skats no augšas
    cx, cy = 560, 130
    s.circ(cx, cy, 85, fill="#fafafa", dash="6,4")
    s.circ(cx, cy, 4, fill="#000")
    for a in range(0, 360, 45):
        r = math.radians(a)
        s.arrow(cx + 14 * math.cos(r), cy + 14 * math.sin(r), cx + 78 * math.cos(r), cy + 78 * math.sin(r), w=1.1)
    s.text(cx, 245, "Skats no augšas:", 12, bold=True)
    s.text(cx, 263, "izstaro vienādi visos virzienos", 12)
    return s


@fig("13.4", "13-4-yagi", "Trīs elementu Yagi antena skatā no augšas")
def f134():
    s = S(720, 270)
    y = 135
    s.line(150, y, 470, y, w=5, col="#777")
    for x, hl, lab, lab2 in ((170, 100, "Reflektors", "garākais"), (300, 88, "Aktīvais elements", "ar pievadu"), (450, 76, "Direktors", "īsākais")):
        s.line(x, y - hl, x, y + hl, w=3.2)
        s.text(x, y + hl + 22, lab, 12, bold=True); s.text(x, y + hl + 38, lab2, 11)
    s.rect(293, y - 8, 14, 16, fill=G)
    s.poly([(307, y + 4), (330, y + 4), (330, y + 70)], w=1.2)
    s.text(336, y + 62, "pievads", 11, anchor="start")
    s.arrow(500, y, 650, y, w=3)
    s.text(575, y - 14, "galvenais starojuma virziens", 12)
    s.arrow(130, y, 90, y, w=1.1, dash="4,3"); s.text(86, y - 10, "vājš", 11, anchor="end")
    return s


@fig("13.5", "13-5-parvades-linijas", "Koaksiālā kabeļa uzbūve un simetriskā līnija")
def f135():
    s = S(720, 260)
    cx, cy = 150, 120
    s.circ(cx, cy, 78, fill="#cfcfcf"); s.circ(cx, cy, 66, fill="#fff"); s.circ(cx, cy, 62, fill="#fff", dash="3,2", sw=2.4)
    s.circ(cx, cy, 56, fill="#f1f1f1"); s.circ(cx, cy, 13, fill="#555")
    for (px, py), ty, lab in (((cx + 8, cy), 55, "centrālais vadītājs"), ((cx + 34, cy - 12), 95, "izolators"), ((cx + 58, cy + 20), 135, "ekrāns (pinums)"), ((cx + 70, cy + 30), 175, "ārējais apvalks")):
        s.poly([(px, py), (260, ty), (275, ty)], w=0.9)
        s.text(280, ty + 4, lab, 12, anchor="start")
    s.text(cx, 232, "Koaksiālais kabelis (50 Ω)", 13, bold=True)
    x0 = 480
    s.line(x0, 70, x0 + 210, 70, w=2.6); s.line(x0, 130, x0 + 210, 130, w=2.6)
    for i in range(6):
        x = x0 + 18 + i * 35
        s.rect(x - 4, 70, 8, 60, fill=G, sw=1)
    s.text(x0 + 105, 160, "divi paralēli vadi ar starplikām", 12)
    s.text(x0 + 105, 232, "Simetriskā līnija (240–600 Ω)", 13, bold=True)
    return s


# ======================= 14. nodaļa ===================================
def _earth(s, y=250, x1=20, x2=700, bulge=26):
    pts = [(x1 + (x2 - x1) * i / 60, y - bulge * math.sin(math.pi * i / 60)) for i in range(61)]
    s.poly(pts + [(x2, y + 30), (x1, y + 30)], close=True, fill=G, w=1.4)
    return lambda x: y - bulge * math.sin(math.pi * (x - x1) / (x2 - x1))


def _layer(s, y, h, label, x1=20, x2=700, fill="#f3f3f3", lx=None):
    s.rect(x1, y, x2 - x1, h, fill=fill, sw=0.8, dash="6,4", col="#888")
    s.text((lx if lx else x2 - 8), y + h / 2 + 5, label, 12, anchor=("middle" if lx else "end"), bold=True, col="#444")


@fig("14.1", "14-1-izplatisanas-veidi", "Trīs radioviļņu izplatīšanās veidi: zemes vilnis, tiešais vilnis un telpas vilnis")
def f141():
    s = S(720, 300)
    ey = _earth(s)
    _layer(s, 30, 28, "jonosfēra")
    tx = 90
    s.line(tx, ey(tx), tx, ey(tx) - 46, w=3); s.text(tx, ey(tx) + 22, "raidītājs", 11)
    rx = 250
    s.line(rx, ey(rx), rx, ey(rx) - 40, w=3)
    # tiešais
    s.arrow(tx, ey(tx) - 46, rx - 2, ey(rx) - 40, w=1.6)
    s.text(170, ey(170) - 58, "tiešais vilnis", 12)
    # zemes vilnis
    pts = [(x, ey(x) - 7 - 3 * math.sin((x - tx) / 6)) for x in range(tx + 4, 420, 2)]
    s.poly(pts, w=1.4, arrow=True)
    s.text(350, ey(350) - 16, "zemes vilnis", 12)
    # telpas vilnis
    lx = 640
    s.poly([(tx, ey(tx) - 46), (360, 58), (lx, ey(lx) - 3)], w=1.8, arrow=True)
    s.text(470, 110, "telpas vilnis", 12, anchor="start")
    s.line(lx, ey(lx), lx, ey(lx) - 30, w=3); s.text(lx, ey(lx) + 22, "tāls uztvērējs", 11)
    return s


@fig("14.2", "14-2-jonosferas-slani", "Jonosfēras slāņi dienā un naktī")
def f142():
    s = S(720, 340)
    yg = 300
    s.rect(20, yg, 680, 22, fill=G, sw=1.2)
    s.line(360, 20, 360, yg, w=1, dash="3,4", col="#777")
    s.text(190, 18, "DIENA", 13, bold=True); s.text(530, 18, "NAKTS", 13, bold=True)
    # diena
    _layer(s, 232, 22, "D   60–90 km", 20, 356, lx=None)
    _layer(s, 180, 22, "E   90–130 km", 20, 356)
    _layer(s, 110, 22, "F1", 20, 356)
    _layer(s, 44, 26, "F2   līdz 400 km", 20, 356)
    # nakts
    _layer(s, 60, 34, "F   150–400 km", 364, 700)
    s.text(532, 250, "D slānis izzūd", 12, italic=True, col="#555")
    # stari diena
    s.line(60, yg, 96, 243, w=1.8); s.text(102, 228, "✕", 16, bold=True)
    s.text(60, yg - 34, "80 m", 11, anchor="end"); s.text(120, 268, "absorbē", 11, anchor="start")
    s.poly([(170, yg), (240, 58), (310, yg)], w=1.8, arrow=True); s.text(244, 282, "15 m", 11)
    # stari nakts
    s.poly([(410, yg), (530, 80), (650, yg)], w=1.8, arrow=True); s.text(530, 282, "80 m", 11)
    s.text(360, yg + 16, "Zeme", 12)
    return s


@fig("14.3", "14-3-mirusi-zona", "Mirusī zona starp zemes viļņa beigām un telpas viļņa nolaišanās vietu")
def f143():
    s = S(720, 280)
    yg = 220
    _layer(s, 28, 30, "jonosfēra (F slānis)")
    s.rect(20, yg, 680, 22, fill=G, sw=1.2)
    tx = 70
    s.line(tx, yg, tx, yg - 46, w=3); s.text(tx, yg + 40, "raidītājs", 11)
    s.arrow(tx + 6, yg - 8, 190, yg - 8, w=1.6); s.text(132, yg - 16, "zemes vilnis", 11)
    s.poly([(tx, yg - 46), (290, 58), (510, yg - 2)], w=1.8, arrow=True)
    s.poly([(tx, yg - 46), (360, 58), (650, yg - 2)], w=1.2, dash="5,4", arrow=True)
    s.text(300, 120, "telpas vilnis", 12, anchor="start")
    s.rect(196, yg + 2, 308, 18, fill="#bbb", sw=1)
    s.text(350, yg + 16, "MIRUSĪ ZONA — signāla nav", 12, bold=True)
    s.text(600, yg + 40, "signāls atkal dzirdams", 11)
    s.text(132, yg + 40, "dzirdams tuvumā", 11)
    return s


@fig("14.4", "14-4-nvis", "NVIS: zemu uzkārts dipols izstaro gandrīz vertikāli, un signāls nosedz apgabalu ap raidītāju")
def f144():
    s = S(720, 300)
    yg = 240
    _layer(s, 26, 30, "jonosfēra (F slānis)")
    s.rect(20, yg, 680, 22, fill=G, sw=1.2)
    cx = 330
    s.line(cx - 46, yg, cx - 46, yg - 22, w=2.5, col="#555"); s.line(cx + 46, yg, cx + 46, yg - 22, w=2.5, col="#555")
    s.line(cx - 46, yg - 22, cx + 46, yg - 22, w=2.4)
    s.text(cx, yg + 40, "zems dipols", 11)
    for dx in (-190, -110, -40, 40, 110, 190):
        s.poly([(cx, yg - 22), (cx + dx * 0.5, 58), (cx + dx, yg - 2)], w=1.4, arrow=True)
    s.add(f'<line x1="{cx - 192}" y1="{yg + 52}" x2="{cx + 192}" y2="{yg + 52}" stroke="#000" stroke-width="1.2" marker-start="url(#a)" marker-end="url(#a)"/>')
    s.text(cx, yg + 48, "", 11)
    s.text(cx + 200, yg + 56, "līdz dažiem simtiem km, bez mirušās zonas", 11, anchor="start")
    s.poly([(cx, yg - 22), (640, 60), (700, 78)], w=1.1, dash="5,4")
    s.text(628, 100, "zema leņķa stars\naiziet tālu", 11, anchor="end", col="#555")
    return s


# ======================= 15. nodaļa ===================================
@fig("15.1", "15-1-voltmetrs-ampermetrs", "Voltmetru pieslēdz paralēli, ampērmetru ieslēdz virknē")
def f151():
    s = S(620, 260)
    x1, x2, y1, y2 = 80, 360, 60, 200
    s.poly([(x1, 125), (x1, y1), (195, y1)]); s.poly([(225, y1), (x2, y1), (x2, 107)])
    s.poly([(x2, 153), (x2, y2), (x1, y2), (x1, 135)])
    s.battery_v(x1, 130)
    s.res_v(x2, 130, label="")
    s.text(x2 - 16, 135, "R", 13, italic=True, anchor="end")
    s.meter(210, y1, "A")
    s.text(210, y1 - 24, "ampērmetrs — virknē", 12)
    xv = 480
    s.poly([(x2, y1), (xv, y1), (xv, 115)]); s.poly([(xv, 145), (xv, y2), (x2, y2)])
    s.dot(x2, y1); s.dot(x2, y2)
    s.meter(xv, 130, "V")
    s.text(xv + 24, 126, "voltmetrs —", 12, anchor="start"); s.text(xv + 24, 142, "paralēli", 12, anchor="start")
    return s


@fig("15.2", "15-2-swr-meritajs", "SWR mērītājs starp transīveru un antenu salīdzina tiešo un atstaroto jaudu")
def f152():
    s = S(700, 210)
    y = 120
    s.box(110, y, 130, 56, "Transīvers", 14)
    s.box(350, y, 150, 56, "SWR un jaudas\nmērītājs", 13, fill=G)
    s.line(175, y, 275, y, w=2.2); s.line(425, y, 560, y, w=2.2)
    s.line(560, y, 560, y - 4); s.antenna(560, y - 4, h=56)
    s.text(600, y + 8, "antena", 12, anchor="start")
    s.arrow(250, y - 46, 450, y - 46, w=2); s.text(350, y - 54, "tiešā jauda", 12)
    s.arrow(450, y + 48, 250, y + 48, w=1.4, dash="6,4"); s.text(350, y + 68, "atstarotā jauda", 12)
    s.text(225, y + 16, "koaksiālais kabelis", 10)
    return s


@fig("15.3", "15-3-osciloskops-spektrs", "Viens un tas pats signāls osciloskopā (laikā) un spektra analizatorā (pa frekvencēm)")
def f153():
    s = S(720, 290)
    # osciloskops
    x0, y0, w, h = 40, 40, 280, 180
    s.rect(x0, y0, w, h, fill="#fafafa")
    for i in range(1, 8):
        s.line(x0 + i * w / 8, y0, x0 + i * w / 8, y0 + h, w=0.6, col="#bbb")
    for i in range(1, 6):
        s.line(x0, y0 + i * h / 6, x0 + w, y0 + i * h / 6, w=0.6, col="#bbb")
    s.sine(x0, y0 + h / 2, w, 60, 2, lw=2.2)
    s.add(f'<line x1="{x0 + w / 8 + 2}" y1="{y0 + 18}" x2="{x0 + w * 5 / 8 - 2}" y2="{y0 + 18}" stroke="#000" stroke-width="1.1" marker-start="url(#a)" marker-end="url(#a)"/>')
    s.text(x0 + w * 3 / 8, y0 + 13, "T = 4 iedaļas", 11)
    s.text(x0 + w / 2, y0 + h + 20, "laiks →", 12, italic=True)
    s.text(x0 + w / 2, 272, "Osciloskops: signāla forma", 13, bold=True)
    # spektrs
    gx, gy, gw, gh = 430, 220, 240, 170
    s.axes(gx, gy, gw, gh, "", "")
    for k, (hh, lab) in enumerate(((150, "f"), (48, "2f"), (22, "3f"))):
        x = gx + 50 + k * 70
        s.line(x, gy, x, gy - hh, w=4)
        s.text(x, gy + 18, lab, 13, italic=True)
    s.text(gx + 50, gy - 158, "pamatfrekvence", 11)
    s.text(gx + 155, gy - 62, "harmonikas", 11)
    s.text(gx + gw / 2, gy + 40, "frekvence →", 12, italic=True)
    s.text(gx + gw / 2, 272, "Spektra analizators: sastāvs", 13, bold=True)
    return s


# ======================= 16. nodaļa ===================================
@fig("16.1", "16-1-traucejumu-celi", "Četri ceļi, pa kuriem raidītāja signāls nonāk kaimiņa ierīcē")
def f161():
    s = S(720, 360)
    yg = 270
    s.line(20, yg, 700, yg, w=1.2)
    def house(x, w=170, h=110):
        s.rect(x, yg - h, w, h, fill="#fafafa")
        s.poly([(x - 12, yg - h), (x + w / 2, yg - h - 60), (x + w + 12, yg - h)], close=True, fill=G)
    house(50); house(500)
    s.text(135, yg + 20, "Radioamatieris", 12, bold=True); s.text(585, yg + 20, "Kaimiņš", 12, bold=True)
    # amatiera antena
    s.line(190, yg - 150, 190, yg - 230, w=3, col="#555")
    s.line(130, yg - 228, 250, yg - 228, w=2.4)
    s.box(110, yg - 50, 76, 34, "TRX", 12)
    s.poly([(148, yg - 50), (190, yg - 50), (190, yg - 150)], w=1.2)
    # kaimiņa antena un ierīces
    s.line(560, yg - 150, 560, yg - 205, w=2.5, col="#555")
    for dy in (0, 12, 24):
        s.line(545, yg - 203 + dy, 575, yg - 203 + dy, w=1.6)
    s.box(560, yg - 70, 66, 34, "TV", 12)
    s.line(560, yg - 150, 560, yg - 87, w=1.1)
    s.box(635, yg - 28, 50, 26, "skaļr.", 10)
    s.poly([(593, yg - 62), (635, yg - 62), (635, yg - 41)], w=1.1)
    # elektrotīkls
    s.poly([(110, yg - 33), (110, yg + 46), (540, yg + 46), (540, yg - 53)], w=1.4, dash="7,4")
    s.text(325, yg + 62, "elektrotīkls", 11)
    # ceļi
    def num(x, y, n):
        s.circ(x, y, 11, fill="#000"); s.text(x, y + 5, str(n), 13, bold=True, col="#fff")
    s.arrow(256, yg - 228, 540, yg - 200, w=1.8); num(400, yg - 232, 1)
    s.arrow(240, yg + 46, 420, yg + 46, w=2.4); num(330, yg + 30, 2)
    s.arrow(256, yg - 214, 625, yg - 66, w=1.4, dash="3,3"); num(470, yg - 146, 3)
    s.arrow(256, yg - 200, 524, yg - 76, w=1.4, dash="8,3"); num(380, yg - 118, 4)
    s.text(30, 338, "1 — caur ierīces antenu    2 — pa elektrotīkla vadiem    3 — pa pieslēgtajiem vadiem    4 — tieši caur korpusu", 11, anchor="start")
    return s


# ======================= 17. nodaļa ===================================
@fig("17.1", "17-1-stacijas-zemejums", "Stacijas zemējums: katrai iekārtai savs vads uz kopīgu zemējuma kopni")
def f171():
    s = S(720, 300)
    y = 70
    xs = (140, 330, 520)
    for x, lab in zip(xs, ("Transīvers", "Barošanas\nbloks", "Antenas\nskaņotājs")):
        s.box(x, y, 130, 56, lab, 13)
        s.line(x, y + 28, x, 170, w=2)
        s.dot(x, 170)
    s.rect(70, 164, 520, 12, fill="#999", sw=1.2)
    s.text(600, 175, "zemējuma kopne", 12, anchor="start")
    s.line(330, 176, 330, 232, w=3)
    s.ground(330, 232)
    s.text(350, 250, "zemētājs — pretestība ne vairāk kā 4 Ω", 12, anchor="start")
    s.text(350, 212, "vara vads, vismaz 1,5 mm²", 12, anchor="start")
    s.text(140, 130, "atsevišķs vads", 11, anchor="start")
    s.line(132, 126, 142, 126, w=0)
    s.text(360, 290, "Iekārtas nesaslēdz virknē vienu caur otru.", 12, italic=True)
    return s


def main():
    for num, (name, cap, fn) in FIGS.items():
        fn().save(name)
    print(f"Uzzīmēti {len(FIGS)} attēli -> {os.path.normpath(OUT)}")


if __name__ == "__main__":
    main()
