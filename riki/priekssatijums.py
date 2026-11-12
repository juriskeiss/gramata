"""Uzbūvē melnraksta priekšskatījumu: vienu HTML un vienu PDF ar visām nodaļām un zīmējumiem.

Palaišana no grāmatas saknes mapes:
    python3 riki/priekssatijums.py

Vajag: pandoc; PDF izveidei — Python pakotni playwright ar Chromium.
Šis ir tikai priekšskatījums recenzēšanai, nevis grāmatas galīgais makets.
"""
import datetime
import glob
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
os.makedirs("izvade", exist_ok=True)

CSS = """
@page { size: A4; margin: 20mm 18mm 20mm 18mm; }
html { font-size: 10.5pt; }
body { font-family: "DejaVu Serif", Georgia, serif; line-height: 1.45; color: #111; max-width: 46em; margin: 0 auto; padding: 0 1em; }
h1, h2, h3, #TOC, table, figcaption, .title, .subtitle, .date { font-family: "DejaVu Sans", Arial, sans-serif; }
h1 { font-size: 20pt; page-break-before: always; border-bottom: 2px solid #111; padding-bottom: 4pt; margin-top: 0; }
h2 { font-size: 13.5pt; margin-top: 1.5em; page-break-after: avoid; }
h3 { font-size: 11.5pt; page-break-after: avoid; }
header#title-block-header { text-align: center; padding-top: 30vh; page-break-after: always; }
header#title-block-header h1 { page-break-before: avoid; border: none; font-size: 26pt; }
.subtitle { font-size: 14pt; }
.melnraksts { border: 2px solid #111; padding: 8pt 12pt; font-family: "DejaVu Sans", Arial, sans-serif; font-size: 9.5pt; margin: 2em 0; }
#TOC { page-break-after: always; font-size: 9.5pt; }
#TOC ul { list-style: none; padding-left: 1.2em; }
#TOC > ul { padding-left: 0; }
#TOC a { color: #111; text-decoration: none; }
table { border-collapse: collapse; width: 100%; font-size: 9pt; margin: 0.8em 0; page-break-inside: avoid; }
th, td { border: 1px solid #888; padding: 3pt 5pt; vertical-align: top; text-align: left; }
th { background: #e8e8e8; }
blockquote { margin: 0.9em 0; padding: 6pt 10pt; border-left: 4px solid #555; background: #f3f3f3; page-break-inside: avoid; }
blockquote p { margin: 0.3em 0; }
blockquote table { background: white; }
figure { margin: 1.1em 0; text-align: center; page-break-inside: avoid; }
figure img { max-width: 100%; max-height: 105mm; }
figcaption { font-size: 9pt; font-style: italic; margin-top: 3pt; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 9pt; }
ul.task-list { list-style: none; padding-left: 1em; }
math { font-size: 1.05em; }
a { color: #111; }
"""

chapters = sorted(glob.glob("nodalas/*.md"))
today = datetime.date.today().isoformat()
meta = f"""---
title: "Radioamatiera mācību grāmata"
subtitle: "Sagatavošanās B kategorijas eksāmenam"
author: "Latvijas Radioamatieru līga"
date: "Melnraksts, {today}"
lang: lv
toc-title: "Saturs"
---

::: melnraksts
**MELNRAKSTS RECENZĒŠANAI.** Teksts nav recenzēts, un tajā var būt kļūdas. Pārbaudāmās vietas katrai
nodaļai ir uzskaitītas mapē `recenzijas/`. Ievaddaļa un pielikumi vēl nav uzrakstīti. Šis fails ir
priekšskatījums, nevis galīgais makets.

Licence: CC BY-NC-SA 4.0. Grāmatas sagatavošanā izmantots mākslīgā intelekta modelis Claude Fable 5.2
(Anthropic); saturu pārbauda un rediģē LRAL autori.
:::
"""
with open("izvade/_meta.md", "w", encoding="utf-8") as f:
    f.write(meta)
with open("izvade/_stils.css", "w", encoding="utf-8") as f:
    f.write(CSS)

html = "izvade/gramata-melnraksts.html"
cmd = ["pandoc", "izvade/_meta.md", *chapters, "-o", html, "--standalone", "--embed-resources",
       "--resource-path=nodalas:.", "--mathml", "--toc", "--toc-depth=2", "--css=izvade/_stils.css",
       "-f", "markdown+task_lists+pipe_tables+implicit_figures", "--wrap=none"]
subprocess.run(cmd, check=True)
print("HTML:", html, f"({os.path.getsize(html) // 1024} KB)")

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("playwright nav atrasts; PDF netika izveidots")
    sys.exit(0)

pdf = "izvade/gramata-melnraksts.pdf"
foot = ('<div style="font-family: DejaVu Sans, Arial; font-size: 8px; width: 100%; padding: 0 18mm; '
        'display: flex; justify-content: space-between; color: #555;">'
        f'<span>Radioamatiera mācību grāmata · melnraksts {today}</span>'
        '<span class="pageNumber"></span></div>')
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto("file://" + os.path.abspath(html))
    pg.pdf(path=pdf, format="A4", print_background=True, display_header_footer=True,
           header_template="<span></span>", footer_template=foot,
           margin={"top": "20mm", "bottom": "20mm", "left": "18mm", "right": "18mm"})
    b.close()
print("PDF:", pdf, f"({os.path.getsize(pdf) // 1024} KB)")
