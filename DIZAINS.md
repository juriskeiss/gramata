# Grāmatas dizains

Grāmatas makets ir veidots vienā stilā ar LRAL bezmaksas kursa 2026
prezentācijām, lai grāmata, slaidi un video lekcijas būtu viens mācību komplekts.
Dizains ir kodā: Markdown pirmavots netiek mainīts, makets no tā tiek uzbūvēts.

## Būvēšana

```
python3 riki/zim/build.py           # zīmējumi (ja mainīti)
python3 riki/makets.py              # visa grāmata
python3 riki/makets.py 05 07        # tikai norādītās nodaļas
python3 riki/makets.py --paraugs 05 # + dizaina elementu lapa recenzentiem
```

Vajag `pandoc` 3.x, Python pakotni `playwright` ar Chromium (vai sistēmas Google
Chrome) un fontu **Inter**. Rezultāts: `izvade/gramata.pdf` (A4) un
`izvade/gramata.html`. Būvēšana notiek divos gājienos: pirmajā nosaka nodaļu
sākumlapas, otrajā tās ieraksta saturā.

| Fails | Ko dara |
| --- | --- |
| `riki/makets.py` | Saliek titullapu, saturu, pateicību un nodaļas; renderē PDF |
| `riki/dizains/gramata.css` | Viss vizuālais stils: krāsas, burti, lapas, lodziņi |
| `riki/dizains/pateiciba.css` | Pateicības lapas stils |
| `riki/dizains/filtrs.lua` | Pārveido VEIDNE.md pierakstu par maketa blokiem |
| `riki/dizains/ikonas.py` | Nodaļu līniju ikonas |
| `riki/dizains/lral-logo.png` | LRAL zīme (no kursa slaidiem); `.png.b64` ir tā pati zīme teksta veidā projektam |
| `riki/dizains/paraugs.md` | Dizaina elementu paraugs (formula, C kategorija, zīmējums) |
| `pateicibas.md` | Pateicības teksts: materiālu autori un redaktori |
| `video-saites.md` | Video lekciju saites; no tām `riki/qr.py` ģenerē QR kodus |

## Stils

Minimālisms, viegli toņi, balta lapa bez pilna krāsojuma. Makets ir kompakts un
draudzīgs izdrukai, arī melnbaltai: krāsa tikai virsrakstu numuros, sīkās zīmēs
un ļoti gaišos lodziņu fonos. Krāsas un burti ir no LRAL kursa prezentācijām, lai
komplekts būtu vienots. **Vāks tiek veidots atsevišķi**; PDF sākas ar titullapu.

## Krāsas

| Nosaukums | Kods | Lietojums |
| --- | --- | --- |
| LRAL ķieģeļsarkanā | `#73281e` | Apakšnodaļu numuri, uzraksti, tabulu galvu teksts, ķeksīši |
| Ķieģeļa gaišais tonis | `#f7efed` | Tabulu galvas fons, nodaļas ikonas aplis |
| Tinte | `#1f2933` | Pamatteksts un virsraksti |
| Zilā / zaļā / sarkanā / dzintara | `#1e5aa8` / `#2f7a4b` / `#b42318` / `#b45309` | Lodziņu "Piemērs", "Praktisks padoms", "Uzmanību!", "Atceries" mala un nosaukums; fonā tikai ļoti gaišs tonis |
| Pelēkā | `#6b7280` | Paraksti, galvene, kājene, avoti |
| Līnija, fons | `#e5e7eb`, `#f7f7f8` | Tabulu līnijas, mācību mērķu bloks |

## Zīmējumi un krāsas

Zīmējumi pamatā ir melnbalti. Krāsu lieto tikai tur, kur tā palīdz saprast
saturu, un tikai tās pašas paletes krāsas (`riki/zim/lib.py`):

| Krāsa | Nozīme zīmējumos |
| --- | --- |
| Sarkanā | Raidītāja signāls, nesējs, telpas vilnis, E lauks, kļūda vai aizliegums |
| Zilā | Informācijas signāls, sānjoslas, B lauks, jonosfēra, starojuma diagramma |
| Zaļā | Atļautā daļa, caurlaides josla, zemes vilnis, pareizs risinājums |
| Dzintara | Troksnis un traucējumi no sadzīves elektronikas, atstarotā jauda, ciparu darba veidi |
| Ķieģeļsarkanā | B kategorijas robežas |

Shēmas un blokshēmas (9.–12. nodaļa) paliek melnbaltas, lai simboli būtu tādi
paši kā kursa slaidos. Rezistoru krāsu kods (9.1. attēls) zīmēts īstajās krāsās.

## Burti

Inter, tāpat kā slaidos. Pamatteksts 9,8 pt, rindstarpa 1,48; nodaļas
virsraksts 24 pt ExtraBold, apakšnodaļas 13,5 pt ar ķieģeļkrāsas numuru.
Formulas: MathML ar Latin Modern Math. Lapas malas 18 mm.

## Lapas elementi

- **Titullapa** — LRAL zīme, nosaukums, īsa ķieģeļkrāsas svītra; apakšā
  izdevējs, versija, licence un MI izmantošanas norāde.
- **Saturs** — vienkāršs saraksts pa daļām ar plānām līnijām.
- **Pateicība** — materiālu autori un redaktori ar izsaukuma signāliem;
  normatīvie akti šeit netiek minēti.
- **Nodaļas sākums** — jaunā lapā, bet bez atsevišķas atvēruma lapas: numurs,
  nosaukums, ievadteikums, maza līniju ikona gaišā aplī; zem tā "Par nodaļu"
  (video lekcija ar QR vietu, eksāmena programma, mācību laiks) un "Pēc šīs
  nodaļas tu pratīsi" gaiši pelēkā blokā. Teksts turpinās tajā pašā lapā.
- **Galvene un kājene** — galvenē pelēkā krāsā nodaļas nosaukums; kājenē maza
  LRAL zīme, grāmatas nosaukums un lapas numurs.
- **Tabulas** — gaišs galvas tonis, plānas horizontālas līnijas, bez rāmjiem.
- **Izceltie lodziņi** — plāna krāsaina kreisā mala, ļoti gaišs fons, maza ikona.
- **Nodaļas beigas** — "Eksāmenā jāzina" gaiši dzintara rāmī, "Pamēģini pats"
  pelēkā rāmī, "Kopsavilkums" ar ķeksīšiem, jautājumi ar apļotiem burtiem A–D
  (īsiem variantiem divās kolonnās). Piespiedu lapu pārtraukumu nav.
- **Zīmējumi** — bez rāmja, paraksts zem plānas līnijas; ja fails vēl nav mapē
  `atteli/`, redzams vietturis ar faila nosaukumu.

## Vēl jāizlemj

- QR kodi video lekcijām: ģenerē `riki/qr.py` no `video-saites.md`. Kamēr
  atsevišķu video saišu nav, kods ved uz kursa atskaņošanas sarakstu un blakus
  ir rakstīts, kuru nodarbību skatīties.
- Vāka dizains (atsevišķs darbs).
- Pielikumu (A–J) noformējums: tie tiks būvēti ar to pašu stilu, kad būs
  uzrakstīti.
- Pateicības lapā trūkst autoru un redaktoru vārdu (`pateicibas.md`, TODO).
