"""Uzbūvē visus grāmatas zīmējumus mapē atteli/.

Palaišana no grāmatas saknes mapes:
    python3 riki/zim/build.py            # tikai SVG
    python3 riki/zim/build.py --png DIR  # arī PNG priekšskatījumi mapē DIR (vajag rsvg-convert)
"""
import importlib
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
os.chdir(ROOT)
os.makedirs("atteli", exist_ok=True)

count = 0
for mod in ("figs_a", "figs_b", "figs_c", "figs_d", "figs_e", "figs_f", "figs_g", "figs_h", "figs_i", "figs_j", "figs_k"):
    try:
        m = importlib.import_module(mod)
    except ModuleNotFoundError:
        continue
    for fn in m.ALL:
        fn()
        count += 1
print(f"Uzzīmēti {count} zīmējumi mapē atteli/")

if "--png" in sys.argv:
    out = sys.argv[sys.argv.index("--png") + 1]
    os.makedirs(out, exist_ok=True)
    for name in sorted(os.listdir("atteli")):
        if name.endswith(".svg"):
            subprocess.run(["rsvg-convert", "-z", "1.5", "-o", os.path.join(out, name[:-4] + ".png"),
                            os.path.join("atteli", name)], check=True)
    print(f"PNG priekšskatījumi: {out}")
