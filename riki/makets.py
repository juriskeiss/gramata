#!/usr/bin/env python3
"""Uzbūvē grāmatas maketu: Markdown → HTML → PDF (A4).

    python3 riki/makets.py                 # visas nodaļas mapē nodalas/
    python3 riki/makets.py 05 07           # tikai norādītās nodaļas
    python3 riki/makets.py --paraugs 05    # + dizaina elementu lapa beigās

Vajag: pandoc (3.x), Python pakotni playwright ar Chromium (vai sistēmas
Google Chrome), fontu Inter. Rezultāts: izvade/gramata.html un izvade/gramata.pdf.

Dizains ir mapē riki/dizains/: gramata.css (stils), pateiciba.css (pateicības
lapa), filtrs.lua (Markdown bloki → maketa bloki), ikonas.py (nodaļu ikonas),
lral-logo.png (LRAL zīme). Pateicības teksts ir pateicibas.md grāmatas saknē.
Vāks tiek veidots atsevišķi un šeit netiek būvēts; PDF sākas ar titullapu.
"""
import html
import re
import subprocess
import sys
from pathlib import Path

SAKNE = Path(__file__).resolve().parent.parent
DIZ = SAKNE / "riki" / "dizains"
NOD = SAKNE / "nodalas"
IZV = SAKNE / "izvade"
PATEICIBAS = SAKNE / "pateicibas.md"
sys.path.insert(0, str(DIZ))
from ikonas import nodalas_ikona  # noqa: E402
sys.path.insert(0, str(SAKNE / "riki"))
from qr import qr_svg  # noqa: E402

GRAMATA = "No nulles līdz izsaukuma signālam"
APAKSV = "Mācību grāmata radioamatiera B kategorijai"
VERSIJA = "0.1"            # izdotās versijas numurs; pirms nākamās izdošanas palielina
IZDOTS = "20.11.2026."     # versijas izdošanas datums
_LOGO = DIZ / "lral-logo.png"
if not _LOGO.exists() and _LOGO.with_suffix(".png.b64").exists():
    # projektā zīme glabājas kā base64 teksts; atjauno PNG pirms būvēšanas
    import base64
    _LOGO.write_bytes(base64.b64decode(_LOGO.with_suffix(".png.b64").read_text()))
LOGO = _LOGO.as_uri()

VIDEO = SAKNE / "video-saites.md"


def video_saites():
    """Nolasa video-saites.md: atskaņošanas saraksta saite un katras nodarbības saite."""
    saraksts, saites = "", {}
    if VIDEO.exists():
        for rinda in VIDEO.read_text(encoding="utf-8").splitlines():
            m = re.match(r"Saraksts:\s*(\S+)", rinda)
            if m:
                saraksts = m.group(1)
            m = re.match(r"\|\s*(\d+(?:\.\d+)?)\s*\|[^|]*\|\s*(\S*)\s*\|", rinda)
            if m and m.group(2):
                saites[m.group(1)] = m.group(2)
    return saraksts, saites


SARAKSTS, SAITES = video_saites()


def video_qr(meta_html: str) -> str:
    """QR kods nodaļas sākumam: uz nodarbības video, ja saite zināma, citādi uz sarakstu."""
    if not SARAKSTS:
        return ""
    m = re.search(r"((?:\d+\.,?\s*(?:un\s+)?)+)nodarbība(?:,\s*(\d+)\.\s*daļa)?", meta_html)
    if m:
        nums = re.findall(r"\d+", m.group(1))
        key = nums[0] + ("." + m.group(2) if m.group(2) else "")
        url = SAITES.get(key) or SAITES.get(nums[0])
        nos = m.group(0).strip()
        teksts = (f"Video lekcija: {nos}" if url else
                  f"Kursa video saraksts LRAL.lv YouTube kanālā; skaties: {nos}")
    else:
        url, teksts = None, "Kursa video saraksts LRAL.lv YouTube kanālā"
    return (f'<div class="qr-vieta"><div class="qr">{qr_svg(url or SARAKSTS)}</div>'
            f'<div>{teksts}</div></div>')


# Saturs pa daļām (nodaļu numuri). Atbilst README.md tabulai.
DALAS = [
    ("Ievads", range(1, 3)),
    ("Noteikumi un ētera prakse", range(3, 7)),
    ("Tehniskie pamati", range(7, 15)),
    ("Stacija praksē", range(15, 18)),
    ("Eksāmens un tālāk", range(18, 20)),
]


def pandoc(md: Path) -> str:
    return subprocess.run(
        ["pandoc", md.name, "-f", "markdown", "-t", "html5", "--mathml",
         "--lua-filter", str(DIZ / "filtrs.lua")],
        cwd=md.parent, check=True, capture_output=True, text=True).stdout


def galva(num: int, title: str, inner: str) -> str:
    """Nodaļas sākums: virsraksts, ievads, informācija un mērķi; teksts turpinās tajā pašā lapā."""
    ievads = re.search(r'<div class="atv-ievads">(.*?)</div>', inner, re.S)
    meta = re.search(r'<dl class="atv-meta">(.*?)</dl>', inner, re.S)
    merki = re.search(r'<ol class="merki-saraksts">.*?</ol>', inner, re.S)
    meta_html = meta.group(1) if meta else ""
    _, ikona = nodalas_ikona(num)
    qr = video_qr(meta_html)
    return f'''
<header class="nod-galva">
  <div>
    <span class="kicker">{num}. nodaļa</span>
    <h1>{html.escape(title)}</h1>
    <p class="nod-ievads">{ievads.group(1).strip() if ievads else ""}</p>
  </div>
  <div class="nod-ikona">{ikona}</div>
</header>
<div class="nod-info">
  <div><h3>Par nodaļu</h3><dl class="atv-meta">{meta_html}</dl>{qr}</div>
  <div class="nod-merki"><h3>Pēc šīs nodaļas tu pratīsi</h3>{merki.group(0) if merki else ""}</div>
</div>'''


def nodala(md: Path):
    frag = pandoc(md)
    m = re.search(r'<template class="atv-dati" data-num="(\d+)" data-title="([^"]*)">(.*?)</template>',
                  frag, re.S)
    if not m:
        raise SystemExit(f"{md.name}: nav atrasts nodaļas virsraksts '# N. nodaļa. Nosaukums'")
    num, title = int(m.group(1)), html.unescape(m.group(2))
    body = frag[m.end():]
    body = re.sub(r"<!--NODALA-ATVERUMS \d+-->", "", body)
    page_css = (f'.nodala-{num} {{ page: nodala{num}; }}\n'
                f'@page nodala{num} {{ @bottom-left {{ content: "{GRAMATA} · LRAL'
                f'   |   {num}. {title.replace(chr(34), "")}"; }} }}\n')
    out = (f'<section class="nodala nodala-{num}" id="nodala-{num}">'
           + galva(num, title, m.group(3))
           + f'\n<div class="nodala-teksts">\n{body}\n</div></section>\n')
    return num, title, out, page_css


PIEL = SAKNE / "pielikumi"
PIELIKUMI_SAR = []


def pielikums(md: Path):
    """Pielikums: '# C pielikums. Nosaukums'; vienkāršs sākums bez mērķiem un QR."""
    frag = pandoc(md)
    m = re.search(r'<template class="atv-dati" data-num="([A-Z])" data-title="([^"]*)">(.*?)</template>',
                  frag, re.S)
    if not m:
        raise SystemExit(f"{md.name}: nav atrasts virsraksts '# X pielikums. Nosaukums'")
    burts, title = m.group(1), html.unescape(m.group(2))
    ievads = re.search(r'<div class="atv-ievads">(.*?)</div>', m.group(3), re.S)
    body = re.sub(r"<!--NODALA-ATVERUMS \w+-->", "", frag[m.end():])
    page_css = (f'.pielikums-{burts} {{ page: piel{burts}; }}\n'
                f'@page piel{burts} {{ @bottom-left {{ content: "{GRAMATA} · LRAL'
                f'   |   {burts} pielikums. {title.replace(chr(34), "")}"; }} }}\n')
    out = (f'<section class="nodala pielikums pielikums-{burts}" id="pielikums-{burts}">'
           f'<header class="nod-galva"><div><span class="kicker">{burts} pielikums</span>'
           f'<h1>{html.escape(title)}</h1>'
           f'<p class="nod-ievads">{ievads.group(1).strip() if ievads else ""}</p></div></header>'
           f'\n<div class="nodala-teksts">\n{body}\n</div></section>\n')
    return burts, title, out, page_css


def tituls() -> str:
    return f'''
<section class="tituls">
  <img class="logo-maz" src="{LOGO}" alt="LRAL">
  <span class="kicker">Latvijas Radioamatieru līga</span>
  <h1>{GRAMATA}</h1>
  <p class="apaksv">{APAKSV}</p>
  <div class="svitra"></div>
  <div class="kolofons">
    <div><b>Izdevējs</b><p>Latvijas Radioamatieru līga (LRAL), lral.lv</p></div>
    <div><b>Versija</b><p>{VERSIJA}, {IZDOTS}</p></div>
    <div><b>Licence</b><p>CC BY-NC-SA 4.0. Grāmatu drīkst lietot, pielāgot un uzlabot, ja norāda
      autoru, nelieto komerciāliem mērķiem un savu versiju izdod ar to pašu licenci.</p></div>
    <div><b>Mākslīgā intelekta izmantošana</b><p>Grāmatas sagatavošanā izmantots mākslīgā
      intelekta modelis Claude Fable 5.2 (Anthropic); saturu pārbaudījuši un rediģējuši LRAL autori.</p></div>
    <div class="kol-qr"><b>Mācību komplekts</b><p>Grāmata papildina LRAL bezmaksas kursa prezentācijas un video
      lekcijas LRAL.lv YouTube kanālā. Video saraksts:</p>{('<div class="qr">' + qr_svg(SARAKSTS) + '</div>') if SARAKSTS else ""}</div>
    <div><b>Zīmējumi</b><p>Oriģināli, uzzīmēti ar kodu; izdoti ar grāmatas licenci.</p></div>
  </div>
</section>'''


def saturs(nodalas, lpp) -> str:
    rindas = []
    for dala, nums in DALAS:
        esosas = [(n, t) for n, t in nodalas if n in nums]
        if not esosas:
            continue
        rindas.append(f'<li class="sadala-grupa">{dala}</li>')
        for n, t in esosas:
            rindas.append(f'<li><span class="nr">{n}</span><span class="nos">'
                          f'<a href="#nodala-{n}">{html.escape(t)}</a></span>'
                          f'<span class="lpp">{lpp.get(n, "")}</span></li>')
    if PIELIKUMI_SAR:
        rindas.append('<li class="sadala-grupa">Pielikumi</li>')
        for b, t in PIELIKUMI_SAR:
            rindas.append(f'<li><span class="nr">{b}</span><span class="nos">'
                          f'<a href="#pielikums-{b}">{html.escape(t)}</a></span>'
                          f'<span class="lpp">{lpp.get(b, "")}</span></li>')
    return (f'<section class="saturs"><h2><span class="kicker">{GRAMATA}</span>'
            f'Saturs</h2><ol>{"".join(rindas)}</ol></section>')


def pateicibas() -> str:
    """Pateicības lapa no pateicibas.md: materiālu autori un redaktori.

    Normatīvie akti šeit netiek minēti. Ja failā palikušas neaizpildītas
    vietas (TODO), būvēšana tos neslēpj, bet brīdina."""
    if not PATEICIBAS.exists():
        return ""
    if "TODO" in PATEICIBAS.read_text(encoding="utf-8"):
        print("BRĪDINĀJUMS: pateicibas.md ir neaizpildītas vietas (TODO): "
              "trūkst autoru vai redaktoru vārdu un izsaukuma signālu.", file=sys.stderr)
    frag = pandoc(PATEICIBAS)
    return (f'<section class="pateiciba"><h2><span class="kicker">{GRAMATA}</span>'
            f'Pateicība</h2>{frag}</section>')


def paraugs() -> str:
    md = DIZ / "paraugs.md"
    frag = pandoc(md)
    return (f'<section class="nodala-teksts" style="break-before: page">'
            f'<h2 style="display:block"><span class="kicker" style="display:block;font-size:6.8pt;'
            f'letter-spacing:.16em;text-transform:uppercase">Maketa pielikums</span>'
            f'Dizaina elementu paraugs</h2>{frag}</section>')


def lapas_nodalam(pdf: Path) -> dict:
    txt = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True,
                         text=True, check=True).stdout
    lpp = {}
    for i, lapa in enumerate(txt.split("\f"), start=1):
        plakans = re.sub(r"[ \t]", "", lapa)   # retināti burti → "5.NODAĻA"
        for m in re.finditer(r"^(\d+)\.NODAĻA$", plakans, re.M):
            if int(m.group(1)) not in lpp:
                lpp[int(m.group(1))] = i
        for m in re.finditer(r"^([A-Z])PIELIKUMS$", plakans, re.M):
            if m.group(1) not in lpp:
                lpp[m.group(1)] = i
    return lpp


def renderet(doc: str, pdf: Path):
    from playwright.sync_api import sync_playwright
    hfile = IZV / "gramata.html"
    hfile.write_text(doc, encoding="utf-8")
    with sync_playwright() as p:
        try:
            b = p.chromium.launch()
        except Exception:
            b = p.chromium.launch(channel="chrome")
        pg = b.new_page()
        pg.goto(hfile.as_uri(), wait_until="networkidle")
        pg.pdf(path=str(pdf), prefer_css_page_size=True, print_background=True,
               outline=True, tagged=True)
        b.close()


def main(args):
    IZV.mkdir(exist_ok=True)
    ar_paraugu = "--paraugs" in args
    filtri = [a for a in args if not a.startswith("--")]
    faili = sorted(NOD.glob("[0-9][0-9]-*.md"))
    if filtri:
        faili = [f for f in faili if f.name[:2] in filtri]
    nodalas, teksts, css_extra = [], [], []
    for f in faili:
        n, t, h, c = nodala(f)
        nodalas.append((n, t)); teksts.append(h); css_extra.append(c)
    PIELIKUMI_SAR.clear()
    if not filtri or "piel" in filtri:
        for f in sorted(PIEL.glob("[A-Z]-*.md")):
            b, t, h, c = pielikums(f)
            PIELIKUMI_SAR.append((b, t)); teksts.append(h); css_extra.append(c)

    # Lapas kājenes teksts tiek ņemts no GRAMATA, lai nosaukums ir vienā vietā.
    css = (DIZ / "gramata.css").read_text(encoding="utf-8").replace(
        'url("lral-logo.png")', f'url("{LOGO}")').replace(
        'content: "Radioamatiera mācību grāmata · LRAL";',
        f'content: "{GRAMATA} · LRAL";')
    css += "\n" + (DIZ / "pateiciba.css").read_text(encoding="utf-8")
    css += "\n" + "".join(css_extra)
    patcibas_html = pateicibas()

    def salikt(lpp):
        return (f'<!doctype html><html lang="lv"><head><meta charset="utf-8">'
                f'<title>{GRAMATA}</title><style>{css}</style></head><body>'
                f'{tituls()}{saturs(nodalas, lpp)}{patcibas_html}{"".join(teksts)}'
                f'{paraugs() if ar_paraugu else ""}</body></html>')

    pdf = IZV / "gramata.pdf"
    renderet(salikt({**{n: "00" for n, _ in nodalas}, **{b: "00" for b, _ in PIELIKUMI_SAR}}), pdf)   # 1. gājiens: lapu numuri
    lpp = lapas_nodalam(pdf)
    renderet(salikt(lpp), pdf)                              # 2. gājiens: ar saturu
    print(f"{pdf} — nodaļas: {', '.join(str(n) for n, _ in nodalas)}; sākumlapas: {lpp}")


if __name__ == "__main__":
    main(sys.argv[1:])
