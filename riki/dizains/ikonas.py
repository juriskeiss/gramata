"""Nodaļu ikonas un uzraksti atvēruma lapām.

Ikonas ir vienkārši līniju zīmējumi tajā pašā valodā kā LRAL kursa
prezentāciju titulslaidos: tumši zila līnija dzintara krāsas kartītē.
viewBox 0 0 64 64, līnijas biezumu un krāsu nosaka CSS (.ikona-svg).
"""

# Katrai nodaļai: (uzraksts kartītē, SVG elementi)
NODALAS = {
    1: ("HOBIJS · KOPIENA",
        '<circle cx="32" cy="34" r="18"/><path d="M14 34h36M32 16c-7 6-7 30 0 36M32 16c7 6 7 30 0 36"/>'
        '<path d="M46 10a12 12 0 0 1 8 8M44 4a20 20 0 0 1 16 14"/>'),
    2: ("CEĻŠ LĪDZ LICENCEI",
        '<path d="M10 54c10-4 8-14 18-16s14-8 10-14"/><circle cx="10" cy="54" r="3"/>'
        '<path d="M38 24V6l14 5-14 5"/>'),
    3: ("LIKUMI · NOTEIKUMI",
        '<path d="M32 8v46M18 54h28M14 16h36"/><path d="M14 16l-7 16h14zM50 16l-7 16h14z"/>'
        '<path d="M7 32a7 4 0 0 0 14 0M43 32a7 4 0 0 0 14 0"/>'),
    4: ("YL · JOSLAS · JAUDAS",
        '<rect x="8" y="20" width="36" height="26" rx="4"/><path d="M16 30h10M16 37h18"/>'
        '<path d="M50 22a8 8 0 0 1 0 12M55 17a15 15 0 0 1 0 22"/>'),
    5: ("CQ · QSO · 73",
        '<rect x="24" y="6" width="16" height="28" rx="8"/><path d="M16 28a16 16 0 0 0 32 0M32 44v10M22 54h20"/>'
        '<path d="M50 10a8 8 0 0 1 0 12M8 10a8 8 0 0 0 0 12" />'),
    6: ("JOSLU PLĀNS",
        '<path d="M6 52h52"/><rect x="10" y="30" width="8" height="22"/><rect x="22" y="18" width="8" height="34"/>'
        '<rect x="34" y="36" width="8" height="16"/><rect x="46" y="24" width="8" height="28"/>'),
    7: ("U = I · R",
        '<path d="M36 6L16 36h14l-4 22 22-32H34z"/>'),
    8: ("AM · FM · SSB",
        '<path d="M4 32c4-14 8-14 12 0s8 14 12 0 8-14 12 0 8 14 12 0 6-10 8-6"/><path d="M4 50h56M4 14h56" stroke-dasharray="3 5"/>'),
    9: ("R · L · C",
        '<path d="M4 20h12M48 20h12"/><rect x="16" y="14" width="32" height="12" rx="2"/>'
        '<path d="M4 46h22M38 46h22M26 36v20M38 36v20"/>'),
    10: ("SHĒMAS",
         '<path d="M8 12h20v14h28M28 26v26H8M44 26v8M40 34h8M42 38h4"/><circle cx="8" cy="12" r="3"/><circle cx="8" cy="52" r="3"/>'
         '<rect x="22" y="34" width="12" height="10" rx="1"/>'),
    11: ("RX · UZTVĒRĒJS",
         '<rect x="6" y="22" width="52" height="32" rx="5"/><circle cx="20" cy="38" r="8"/><path d="M36 32h14M36 40h14M36 48h8"/>'
         '<path d="M20 22L44 8"/>'),
    12: ("TX · RAIDĪTĀJS",
         '<path d="M32 22l-12 36M32 22l12 36M24 46h16M27 36h10"/><circle cx="32" cy="18" r="4"/>'
         '<path d="M20 10a14 14 0 0 0 0 16M44 10a14 14 0 0 1 0 16M13 4a24 24 0 0 0 0 28M51 4a24 24 0 0 1 0 28"/>'),
    13: ("ANTENAS · KABEĻI",
         '<path d="M6 18h22M36 18h22M28 18v8M36 18v8M28 26c0 10 8 10 8 20v12M28 26c0 10 8 10 8 20"/>'
         '<path d="M32 26v32"/>'),
    14: ("SPEKTRS · DX",
         '<path d="M4 58a40 40 0 0 1 56 0"/><path d="M8 50L22 20l14 28 12-24 8 18"/><path d="M4 14c10-6 46-6 56 0" stroke-dasharray="3 5"/>'),
    15: ("SWR · MĒRĪJUMI",
         '<rect x="6" y="10" width="52" height="44" rx="5"/><path d="M14 40a18 18 0 0 1 36 0"/><path d="M32 40l10-14"/>'
         '<circle cx="32" cy="40" r="3"/><path d="M14 48h36"/>'),
    16: ("EMS · TRAUCĒJUMI",
         '<path d="M32 6l20 8v16c0 14-9 22-20 28C21 52 12 44 12 30V14z"/><path d="M20 32l6-8 6 14 6-14 6 8"/>'),
    17: ("DROŠĪBA",
         '<path d="M32 6L4 56h56z"/><path d="M34 22l-8 16h10l-4 12"/>'),
    18: ("EKSĀMENS",
         '<rect x="12" y="6" width="40" height="52" rx="4"/><path d="M22 4h20v8H22z"/>'
         '<path d="M20 26l4 4 7-8M20 40l4 4 7-8M36 27h10M36 41h10"/>'),
    19: ("ĒTERĀ!",
         '<rect x="6" y="14" width="30" height="40" rx="3"/><path d="M12 24h18M12 31h18M12 38h10"/><circle cx="28" cy="45" r="4"/>'
         '<path d="M50 20v36M50 40l-6 16M50 40l6 16"/><path d="M44 16a8 8 0 0 1 12 0M40 11a14 14 0 0 1 20 0"/>'),
}

VAKS = ("B KATEGORIJA",
        '<path d="M6 14c8-4 18-4 26 2v40c-8-6-18-6-26-2zM58 14c-8-4-18-4-26 2v40c8-6 18-6 26-2z"/>'
        '<path d="M44 6a10 10 0 0 1 10 0M41 1a16 16 0 0 1 16 0"/><path d="M49 8v8"/>')


def svg(elements: str, cls: str = "ikona-svg") -> str:
    return (f'<svg class="{cls}" viewBox="0 0 64 64" fill="none" stroke-linecap="round" '
            f'stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg">{elements}</svg>')


def nodalas_ikona(num: int):
    label, el = NODALAS.get(num, ("", '<circle cx="32" cy="32" r="20"/>'))
    return label, svg(el)
