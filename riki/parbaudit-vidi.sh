#!/usr/bin/env bash
# Pārbauda, vai šajā datorā var uzbūvēt grāmatu (riki/makets.py).
# Palaid repozitorija saknē:  bash riki/parbaudit-vidi.sh
# Rezultāts: ekrānā un failā izvade/vides-parbaude.txt
cd "$(dirname "$0")/.." || exit 1
mkdir -p izvade
OUT=izvade/vides-parbaude.txt
{
echo "Vides pārbaude $(date '+%Y-%m-%d %H:%M')  ($(uname -srm))"
. /etc/os-release 2>/dev/null && echo "OS: $PRETTY_NAME"
echo

ok(){ echo "[OK]   $*"; }
bad(){ echo "[TRŪKST] $*"; }

# pandoc 3.x
if command -v pandoc >/dev/null; then
  v=$(pandoc --version | head -1 | awk '{print $2}')
  [ "${v%%.*}" -ge 3 ] 2>/dev/null && ok "pandoc $v" || bad "pandoc $v (vajag 3.x)"
else bad "pandoc nav uzinstalēts"; fi

# Python un playwright (sistēmas vai ~/venv/gramata)
PY=python3; [ -x "$HOME/venv/gramata/bin/python" ] && PY="$HOME/venv/gramata/bin/python"
echo "Python: $PY ($($PY --version 2>&1))"
if $PY -c "import playwright" 2>/dev/null; then
  ok "playwright ($($PY -m pip show playwright 2>/dev/null | awk '/^Version/{print $2}'))"
  r=$($PY - <<'PYEOF' 2>&1
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    for how in ("chromium", "chrome"):
        try:
            b = p.chromium.launch() if how == "chromium" else p.chromium.launch(channel="chrome")
            pg = b.new_page(); pg.set_content("<p>x</p>"); pg.pdf(path="/tmp/_tests.pdf"); b.close()
            print("OK " + how); break
        except Exception as e:
            print("NEIZDEVĀS " + how + ": " + str(e).splitlines()[0])
PYEOF
)
  echo "$r" | sed 's/^/       pārlūks: /'
  echo "$r" | grep -q '^OK' && ok "PDF tests ar pārlūku izdevās" || bad "neviens pārlūks nestrādā (python -m playwright install --with-deps chromium)"
else bad "playwright nav ($PY)"; fi
command -v google-chrome >/dev/null && echo "       sistēmas Chrome: $(google-chrome --version 2>/dev/null)"

# Fonti
fc-list | grep -qi "Inter" && ok "fonts Inter" || bad "fonts Inter"
fc-list | grep -qi "Latin Modern Math" && ok "fonts Latin Modern Math" || bad "fonts Latin Modern Math (fonts-lmodern)"

# Pēc izvēles
command -v rsvg-convert >/dev/null && ok "rsvg-convert (nav obligāts)" || echo "[—]    rsvg-convert nav (vajag tikai build.py --png)"
command -v git >/dev/null && echo "git: $(git --version | awk '{print $3}'), zars: $(git branch --show-current 2>/dev/null)"
} 2>&1 | tee "$OUT"
echo; echo "Saglabāts: $OUT"
