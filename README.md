# No nulles līdz izsaukuma signālam

**Mācību grāmata radioamatiera B kategorijai**

Mācību grāmata topošajiem radioamatieriem, kas gatavojas B kategorijas
(iesācēja radioamatiera) eksāmenam. Izdevējs: Latvijas Radioamatieru līga (LRAL).

Šis ir grāmatas **darba pirmavots**. Visus labojumus veic šeit, Markdown failos;
PDF ir tikai no tiem uzbūvēts rezultāts un ar roku netiek labots.

## Statuss

| Nr. | Nodaļa | Fails | Statuss |
| --- | --- | --- | --- |
| 1 | Kas ir radioamatierisms | `nodalas/01-kas-ir-radioamatierisms.md` | Melnraksts |
| 2 | Ceļš līdz licencei | `nodalas/02-cels-lidz-licencei.md` | Melnraksts |
| 3 | Normatīvie akti | `nodalas/03-normativie-akti.md` | Melnraksts |
| 4 | Izsaukuma signāli, joslas un jaudas | `nodalas/04-izsaukuma-signali-joslas-jaudas.md` | Melnraksts |
| 5 | Radiosakaru prakse | `nodalas/05-radiosakaru-prakse.md` | Melnraksts (paraugnodaļa) |
| 6 | Joslu plāni un ētera kultūra | `nodalas/06-joslu-plani-etera-kultura.md` | Melnraksts |
| 7 | Elektronikas pamati | `nodalas/07-elektronikas-pamati.md` | Melnraksts |
| 8 | Radioviļņi, signāli un modulācija | `nodalas/08-radiovilni-signali-modulacija.md` | Melnraksts |
| 9 | Elektronikas komponenti | `nodalas/09-komponenti.md` | Melnraksts |
| 10 | Shēmas | `nodalas/10-shemas.md` | Melnraksts |
| 11 | Uztvērēji | `nodalas/11-uztvereji.md` | Melnraksts |
| 12 | Raidītāji | `nodalas/12-raiditaji.md` | Melnraksts |
| 13 | Antenas un pārvades līnijas | `nodalas/13-antenas-parvades-linijas.md` | Melnraksts |
| 14 | Frekvenču spektrs un izplatīšanās | `nodalas/14-spektrs-izplatisanas.md` | Melnraksts |
| 15 | Mērījumi | `nodalas/15-merijumi.md` | Melnraksts |
| 16 | Traucējumi un elektromagnētiskā saderība | `nodalas/16-traucejumi-ems.md` | Melnraksts |
| 17 | Drošības tehnika | `nodalas/17-drosibas-tehnika.md` | Melnraksts |
| 18 | Gatavošanās eksāmenam | `nodalas/18-gatavosanas-eksamenam.md` | Melnraksts |
| 19 | Licence izsniegta — kas tagad? | `nodalas/19-licence-izsniegta.md` | Melnraksts |

Statusi: Nav sākts → Melnraksts → Recenzēts → Apstiprināts.

## Mapju struktūra

```
gramata/
├── README.md              šis fails
├── VEIDNE.md              nodaļas veidne un pieraksta noteikumi
├── DIZAINS.md             grāmatas dizains: krāsas, burti, lapu elementi
├── avoti.md               avotu saraksts ar lietošanas tiesību statusu
├── pateicibas.md          pateicības lapa: materiālu autori un redaktori
├── video-saites.md        video lekciju saites QR kodiem
├── nodalas/               viena nodaļa = viens fails
├── pielikumi/             A–H pielikumi: formulas, alfabēts un Q kodi, joslas,
│                          joslu plāns, skaitļu lapa, saites, vārdnīca,
│                          lapa pirmajam QSO
├── atteli/                74 zīmējumi SVG formātā (ģenerēti ar riki/zim/)
├── riki/zim/              zīmējumu pirmkods (Python)
├── riki/makets.py         uzbūvē grāmatas maketu (HTML un PDF)
├── riki/dizains/          maketa stils, Pandoc filtrs, ikonas, LRAL zīme
├── riki/priekssatijums.py vienkāršs priekšskatījums recenzēšanai
├── izvade/                uzbūvētie faili (nav pirmavots)
└── recenzijas/            piezīmes recenzentiem; grāmatā neieiet
```

## Zīmējumi

Visi zīmējumi ir oriģināli, uzzīmēti ar kodu vienotā stilā. Pamatā tie ir
melnbalti; krāsa ir tur, kur tā palīdz saprast (viļņi, spektri, joslu plāni,
izplatīšanās, rezistoru krāsu kods, traucējumi). Krāsas ir no grāmatas dizaina
paletes (`DIZAINS.md`). Shēmu apzīmējumi ir pēc IEC (rezistors kā
taisnstūris). Zīmējumi nav pārņemti no slaidiem vai citiem avotiem un tiek
izdoti ar grāmatas licenci. Trūkstošo attēlu saraksts:
`recenzijas/trukstosie-atteli.md`.

Zīmējumu labo tā pirmkodā (`riki/zim/figs_a.py` … `figs_e.py`),
nevis SVG failā, un pārbūvē:

```
python3 riki/zim/build.py
```

## PDF izveide

Grāmata tiek izdota tikai PDF formātā (A4). Makets ir veidots vienā stilā ar
LRAL bezmaksas kursa prezentācijām; sīkāk sk. `DIZAINS.md`. Uzbūvē ar:

```
python3 riki/makets.py              # visa grāmata
python3 riki/makets.py --paraugs 05 # viena nodaļa + dizaina elementu lapa
```

Vajag `pandoc` 3.x, Python pakotni `playwright` ar Chromium un fontu Inter.
Rezultāts ir `izvade/gramata.pdf`.

Grāmatas nosaukums un apakšvirsraksts ir `riki/makets.py` (konstantes
`GRAMATA` un `APAKSV`); no tiem tiek ņemts titullapas, lapu kājenes un PDF
nosaukums. Versijas numurs un izdošanas datums titullapā ir konstantes
`VERSIJA` un `IZDOTS` tajā pašā failā.

## Versijas

| Versija | Datums | Saturs |
| --- | --- | --- |
| 0.1 | 20.11.2026. | Pirmā pilnā versija: 19 nodaļas, A–H pielikums, pateicības; pēc YL2FD, YL2GD, YL3MS, YL3OI un YL2SM recenzijām un divām pilnām pārbaudēm. Git birka `v0.1`, PDF — `no-nulles-lidz-izsaukuma-signalam.pdf`. |

Izdodot jaunu versiju: palielina `VERSIJA`, ieraksta `IZDOTS`, papildina šo
tabulu, uzbūvē PDF, veic commit un pieliek birku `vX.Y`.

## Kā labot

1. Atver nodaļas failu un labo tekstu.
2. Ievēro `VEIDNE.md` noteikumus par izceltajiem lodziņiem, formulām un atsaucēm.
3. Ja pievieno faktu no ārēja avota, ieraksti avotu `avoti.md` un pārbaudi tā
   lietošanas tiesības, **pirms** izmanto tekstu vai attēlu.
4. Pēc labojuma atjauno nodaļas statusu šajā failā.

## Licence

Grāmata tiek izdota ar licenci
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.lv):
to drīkst lietot, pielāgot un uzlabot, ja norāda autoru, nelieto komerciāliem
mērķiem un savu versiju izdod ar to pašu licenci.

## Mākslīgā intelekta izmantošana

Grāmatas sagatavošanā izmantots mākslīgā intelekta modelis Claude Fable 5.2
(Anthropic); saturu pārbaudījuši un rediģējuši LRAL autori.
