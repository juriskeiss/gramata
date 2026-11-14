"""Kopīga zīmēšanas bibliotēka grāmatas zīmējumiem (SVG; pamatā melnbalts, krāsa — kur tā palīdz).

Visi zīmējumi tiek ģenerēti ar kodu, lai tos varētu labot un pārbūvēt.
Palaišana: python3 riki/zim/build.py
"""
import math
from xml.sax.saxutils import escape

FONT = "DejaVu Sans, Arial, Helvetica, sans-serif"
K = "#111111"      # līnijas un teksts
G = "#cfcfcf"      # pelēks aizpildījums
LG = "#ececec"     # gaiši pelēks
MG = "#9a9a9a"     # vidēji pelēks
# Krāsas — tās pašas, kas grāmatas maketā (riki/dizains/gramata.css). Lieto tikai tur,
# kur krāsa palīdz saprast zīmējumu; melnbaltā izdrukā tās paliek atšķiramas pēc toņa.
RED, RED_T = "#b42318", "#fbe4e1"
BLUE, BLUE_T = "#1e5aa8", "#dde8f6"
GREEN, GREEN_T = "#2f7a4b", "#dcefe2"
AMBER, AMBER_T = "#b45309", "#fbebd3"
BRICK, BRICK_T = "#73281e", "#f3e3e0"
CW = 0.60          # aptuvens rakstzīmes platums pret fonta izmēru


def tw(s, size=13):
    """Aptuvens teksta platums pikseļos."""
    return len(s) * size * CW


class Fig:
    def __init__(self, w, h):
        self.w, self.h, self.e = w, h, []

    def add(self, x):
        self.e.append(x)
        return self

    # --- pamatelementi ---
    def line(self, x1, y1, x2, y2, dash=None, w=1.6, color=K):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                 f'stroke="{color}" stroke-width="{w}"{d} stroke-linecap="round"/>')

    def pl(self, pts, dash=None, w=1.6, color=K, fill="none", close=False):
        p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        d = f' stroke-dasharray="{dash}"' if dash else ""
        tag = "polygon" if close else "polyline"
        self.add(f'<{tag} points="{p}" fill="{fill}" stroke="{color}" stroke-width="{w}"{d} '
                 f'stroke-linejoin="round" stroke-linecap="round"/>')

    def arrow(self, x1, y1, x2, y2, dash=None, w=1.6, color=K, head=9):
        a = math.atan2(y2 - y1, x2 - x1)
        sp = 0.42
        # līnija beidzas nedaudz pirms smailes, lai gals būtu ass
        self.line(x1, y1, x2 - 0.6 * head * math.cos(a), y2 - 0.6 * head * math.sin(a), dash, w, color)
        p = [(x2, y2),
             (x2 - head * math.cos(a - sp), y2 - head * math.sin(a - sp)),
             (x2 - head * math.cos(a + sp), y2 - head * math.sin(a + sp))]
        self.pl(p, w=1, color=color, fill=color, close=True)

    def darrow(self, x1, y1, x2, y2, w=1.2, color=K):
        """Abpusēja bultiņa (izmēru līnija)."""
        self.arrow(x1, y1, x2, y2, w=w, head=7, color=color)
        self.arrow(x2, y2, x1, y1, w=w, head=7, color=color)

    def rect(self, x, y, w, h, fill="white", rx=4, sw=1.6, dash=None, color=K):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
                 f'fill="{fill}" stroke="{color}" stroke-width="{sw}"{d}/>')

    def circ(self, cx, cy, r, fill="white", sw=1.6, dash=None, color=K):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" '
                 f'stroke="{color}" stroke-width="{sw}"{d}/>')

    def path(self, d, fill="none", dash=None, w=1.6, color=K):
        ds = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{w}"{ds} '
                 f'stroke-linecap="round" stroke-linejoin="round"/>')

    def text(self, x, y, t, anchor="middle", size=13, bold=False, italic=False, color=K):
        st = ""
        if bold:
            st += ' font-weight="bold"'
        if italic:
            st += ' font-style="italic"'
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="{size}" '
                 f'fill="{color}"{st}>{escape(t)}</text>')

    def ltext(self, x, y, t, anchor="middle", size=12, italic=False, bold=False, color=K):
        """Teksts ar baltu fonu (lai nepārklātos ar līknēm)."""
        w = len(t) * size * CW + 6
        x0 = x - w / 2 if anchor == "middle" else (x - 3 if anchor == "start" else x - w + 3)
        self.add(f'<rect x="{x0:.1f}" y="{y - size:.1f}" width="{w:.1f}" height="{size + 5:.1f}" fill="white" stroke="none"/>')
        self.text(x, y, t, anchor=anchor, size=size, italic=italic, bold=bold, color=color)

    def mtext(self, cx, cy, label, size=13, bold=False, anchor="middle", lh=1.25, color=K, italic=False):
        lines = label.split("\n")
        y0 = cy - (len(lines) - 1) * size * lh / 2 + size * 0.36
        for i, t in enumerate(lines):
            self.text(cx, y0 + i * size * lh, t, anchor=anchor, size=size, bold=bold, color=color, italic=italic)

    def box(self, cx, cy, w, h, label, fill="white", size=13, bold=False, dash=None, color=K, tcolor=K):
        self.rect(cx - w / 2, cy - h / 2, w, h, fill=fill, dash=dash, color=color)
        self.mtext(cx, cy, label, size=size, bold=bold, color=tcolor)

    def sine(self, x0, y0, width, amp, cycles, phase=0.0, dash=None, w=1.6, n=240,
             env=None, fm=None, rect=False, color=K):
        """Sinusoīda. env(t)->amplitūdas reizinātājs, fm(t)->fāzes piedeva, t no 0 līdz 1."""
        pts = []
        for i in range(n + 1):
            t = i / n
            ph = 2 * math.pi * cycles * t + phase + (fm(t) if fm else 0)
            v = math.sin(ph)
            if rect:
                v = abs(v)
            a = amp * (env(t) if env else 1)
            pts.append((x0 + width * t, y0 - a * v))
        self.pl(pts, dash=dash, w=w, color=color)

    def axes(self, x0, y0, w, h, xl="", yl="", neg=0):
        """Asis: sākums (x0,y0), platums w, augstums h uz augšu, neg uz leju."""
        self.arrow(x0, y0, x0 + w, y0, w=1.2, head=7)
        self.arrow(x0, y0 + neg, x0, y0 - h, w=1.2, head=7)
        if xl:
            self.text(x0 + w - 2, y0 + 16, xl, anchor="end", size=12, italic=True)
        if yl:
            self.text(x0 - 6, y0 - h + 4, yl, anchor="end", size=12, italic=True)

    # --- simboli ---
    def antenna(self, x, y, h=36):
        """Antenas simbols; (x,y) ir pieslēgvieta apakšā."""
        self.line(x, y, x, y - h)
        self.line(x, y - h + 18, x - 12, y - h)
        self.line(x, y - h + 18, x + 12, y - h)

    def ground(self, x, y, stem=10):
        self.line(x, y, x, y + stem)
        for i, hw in enumerate((12, 8, 4)):
            self.line(x - hw, y + stem + i * 5, x + hw, y + stem + i * 5)

    def speaker(self, x, y):
        """Skaļrunis; (x,y) ir pieslēgvieta kreisajā pusē."""
        self.rect(x, y - 8, 9, 16, rx=0)
        self.pl([(x + 9, y - 8), (x + 22, y - 18), (x + 22, y + 18), (x + 9, y + 8)], close=True, fill="white")

    def mic(self, x, y):
        """Mikrofons; (x,y) ir pieslēgvieta labajā pusē."""
        self.circ(x - 12, y, 10)
        self.line(x - 24, y - 12, x - 24, y + 12, w=2.2)
        self.line(x - 2, y, x, y)

    def resistor(self, x, y, horizontal=True, L=44, T=16, label=None, lpos="above"):
        """Rezistors (IEC taisnstūris), centrs (x,y)."""
        if horizontal:
            self.rect(x - L / 2, y - T / 2, L, T, rx=0)
            if label:
                self.text(x, y - T / 2 - 6 if lpos == "above" else y + T / 2 + 16, label, size=13, italic=True)
        else:
            self.rect(x - T / 2, y - L / 2, T, L, rx=0)
            if label:
                self.text(x + T / 2 + 6, y + 5, label, anchor="start", size=13, italic=True)

    def capacitor(self, x, y, horizontal=True, gap=8, plate=24):
        """Kondensators, centrs (x,y); atgriež pusplatumu pieslēgumam."""
        if horizontal:
            self.line(x - gap / 2, y - plate / 2, x - gap / 2, y + plate / 2, w=2.2)
            self.line(x + gap / 2, y - plate / 2, x + gap / 2, y + plate / 2, w=2.2)
        else:
            self.line(x - plate / 2, y - gap / 2, x + plate / 2, y - gap / 2, w=2.2)
            self.line(x - plate / 2, y + gap / 2, x + plate / 2, y + gap / 2, w=2.2)
        return gap / 2

    def inductor(self, x, y, horizontal=True, n=4, r=7):
        """Spole no pusloķiem, centrs (x,y); kopgarums 2*n*r."""
        L = 2 * n * r
        if horizontal:
            d = f"M {x - L / 2:.1f} {y:.1f} "
            for i in range(n):
                d += f"a {r} {r} 0 0 1 {2 * r} 0 "
        else:
            d = f"M {x:.1f} {y - L / 2:.1f} "
            for i in range(n):
                d += f"a {r} {r} 0 0 1 0 {2 * r} "
        self.path(d)
        return L / 2

    def diode(self, x, y, s=11, kind="normal"):
        """Diode horizontāli, anods pa kreisi; centrs (x,y)."""
        self.pl([(x - s, y - s), (x - s, y + s), (x + s, y)], close=True, fill="white")
        if kind == "zener":
            self.pl([(x + s - 5, y - s - 4), (x + s, y - s), (x + s, y + s), (x + s + 5, y + s + 4)], w=2)
        else:
            self.line(x + s, y - s, x + s, y + s, w=2)
        if kind == "led":
            self.arrow(x + 2, y - s - 4, x + 12, y - s - 16, w=1.2, head=6)
            self.arrow(x + 12, y - s - 2, x + 22, y - s - 14, w=1.2, head=6)

    def battery(self, x, y, vertical=True):
        """Baterija, centrs (x,y); garā svītra ir plus."""
        if vertical:
            self.line(x - 14, y - 5, x + 14, y - 5, w=1.6)
            self.line(x - 7, y + 5, x + 7, y + 5, w=3)
            self.text(x - 20, y - 4, "+", anchor="end", size=13)
            self.text(x - 20, y + 12, "−", anchor="end", size=13)

    def meter(self, x, y, letter, r=15):
        self.circ(x, y, r)
        self.text(x, y + 5, letter, size=14, bold=True)

    def save(self, path, title=""):
        head = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w:.0f} {self.h:.0f}" '
                f'width="{self.w:.0f}" height="{self.h:.0f}" font-family="{FONT}">\n')
        t = f"<title>{escape(title)}</title>\n" if title else ""
        bg = f'<rect x="0" y="0" width="{self.w:.0f}" height="{self.h:.0f}" fill="white"/>\n'
        with open(path, "w", encoding="utf-8") as f:
            f.write(head + t + bg + "\n".join(self.e) + "\n</svg>\n")


def chain(f, labels, x0, y, bh=46, gap=28, size=12, fills=None, pad=18, minw=62):
    """Bloku ķēde ar bultiņām. Atgriež [(cx, kreisā mala, labā mala)]."""
    x = x0
    out = []
    for i, l in enumerate(labels):
        w = max(minw, pad + max(tw(t, size) for t in l.split("\n")))
        cx = x + w / 2
        f.box(cx, y, w, bh, l, size=size, fill=(fills[i] if fills else "white"))
        out.append((cx, x, x + w))
        if i < len(labels) - 1:
            f.arrow(x + w, y, x + w + gap, y)
        x += w + gap
    return out


def arcpts(cx, cy, R, a1, a2, n=60):
    """Punkti uz loka; leņķis mērīts no vertikāles (radiānos)."""
    return [(cx + R * math.sin(a1 + (a2 - a1) * i / n), cy - R * math.cos(a1 + (a2 - a1) * i / n))
            for i in range(n + 1)]


# --- funkcionālie simboli blokshēmām (kā LRAL kursa 7. nodarbības slaidos) ---
SQ = 46  # bloka izmērs


def _tilde(f, cx, y, w=26, a=4.0, strike=False):
    f.sine(cx - w / 2, y, w, a, 1.0, w=1.4, n=40)
    if strike:
        f.line(cx - 4, y + 6, cx + 4, y - 6, w=1.4)


def sym_filter(f, cx, cy, kind="bp", s=SQ):
    """Filtrs: bp — joslas, lp — zemo frekvenču, hp — augsto frekvenču."""
    f.rect(cx - s / 2, cy - s / 2, s, s, rx=0)
    if kind == "bp":
        _tilde(f, cx, cy - 12, strike=True)
        _tilde(f, cx, cy)
        _tilde(f, cx, cy + 12, strike=True)
    else:
        _tilde(f, cx, cy - 7, strike=(kind == "lp"))
        _tilde(f, cx, cy + 7, strike=(kind == "hp"))
    return cx - s / 2, cx + s / 2


def sym_amp(f, cx, cy, w=42, h=46):
    f.pl([(cx - w / 2, cy - h / 2), (cx - w / 2, cy + h / 2), (cx + w / 2, cy)], close=True, fill="white")
    return cx - w / 2, cx + w / 2


def sym_mixer(f, cx, cy, r=23):
    f.circ(cx, cy, r)
    d = r * 0.707
    f.line(cx - d, cy - d, cx + d, cy + d, w=1.4)
    f.line(cx - d, cy + d, cx + d, cy - d, w=1.4)
    return cx - r, cx + r


def sym_gen(f, cx, cy, r=23, tunable=False):
    f.circ(cx, cy, r)
    _tilde(f, cx, cy, w=24, a=4.5)
    if tunable:
        f.arrow(cx - 11, cy + 9, cx + 11, cy - 11, w=1.4, head=7)
    return cx - r, cx + r


def sym_det(f, cx, cy, s=SQ):
    f.rect(cx - s / 2, cy - s / 2, s, s, rx=0)
    f.line(cx, cy - 16, cx, cy + 16, w=1.4)
    f.pl([(cx - 8, cy - 6), (cx + 8, cy - 6), (cx, cy + 6)], close=True, fill="white", w=1.4)
    f.line(cx - 8, cy + 6, cx + 8, cy + 6, w=1.6)
    return cx - s / 2, cx + s / 2


def sym_disc(f, cx, cy, s=SQ):
    f.rect(cx - s / 2, cy - s / 2, s, s, rx=0)
    f.pl([(cx - s / 2, cy + s / 2), (cx, cy - s / 2), (cx + s / 2, cy + s / 2)], w=1.4)
    return cx - s / 2, cx + s / 2


def sym_lim(f, cx, cy, s=SQ):
    f.rect(cx - s / 2, cy - s / 2, s, s, rx=0)
    pts = []
    for i in range(41):
        t = i / 40
        v = max(-0.55, min(0.55, math.sin(2 * math.pi * t)))
        pts.append((cx - 12 + 24 * t, cy - 14 * v))
    f.pl(pts, w=1.4)
    f.line(cx - 19, cy, cx - 13, cy, w=1.4)
    f.line(cx + 13, cy, cx + 19, cy, w=1.4)
    return cx - s / 2, cx + s / 2


def sym_block(f, cx, cy, label, w=SQ, size=11):
    f.rect(cx - w / 2, cy - SQ / 2, w, SQ, rx=0)
    f.mtext(cx, cy, label, size=size)
    return cx - w / 2, cx + w / 2


def sym_key(f, x, y):
    """Telegrāfa atslēga: augšējais kontakts (x, y), apakšā zemējums."""
    f.circ(x, y, 3.5)
    f.circ(x, y + 34, 3.5)
    f.line(x - 1, y + 31, x - 12, y + 8, w=1.6)
    f.path(f"M {x - 18} {y + 4} L {x - 18} {y + 16} M {x - 18} {y + 4} Q {x - 10} {y + 10} {x - 18} {y + 16}", w=1.4)
    f.line(x, y + 38, x, y + 48, w=1.6)
    f.line(x - 16, y + 48, x + 16, y + 48, w=1.6)
    for k in range(4):
        f.line(x - 14 + k * 9, y + 48, x - 20 + k * 9, y + 58, w=1.2)


def lab(f, cx, y, text, size=11):
    """Paraksts virs vai zem simbola; y ir apakšējās (vai vienīgās) rindas bāzes līnija."""
    lines = text.split("\n")
    for i, t in enumerate(lines):
        f.text(cx, y - (len(lines) - 1 - i) * size * 1.2, t, size=size)
