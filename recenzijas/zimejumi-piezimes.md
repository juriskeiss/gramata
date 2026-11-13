# Zīmējumi — piezīmes recenzentam

Grāmatā šis fails neieiet.

Visi 69 zīmējumi ir uzzīmēti no jauna ar kodu (`riki/zim/`). Tie ir apskatīti
pēc renderēšanas, bet nav salīdzināti ar kursa slaidu attēliem, jo slaidu
attēlu saturs teksta veidā nav pieejams. Katrs zīmējums jāapskata cilvēkam.

## Kopīgi

- [ ] **Apzīmējumu standarts.** Uztvērēju un raidītāju blokshēmās lietoti
  kursa slaidu funkcionālie simboli (`riki/zim/lib.py`, `sym_*`). Shēmās
  9.–10. nodaļā lietoti IEC simboli (rezistors kā
  taisnstūris, spole kā pusloki). Jāsalīdzina ar to, kā shēmas zīmētas ES
  eksāmena jautājumos; ja tur ir citi simboli, jāmaina bibliotēkā
  `riki/zim/lib.py` vienā vietā.
- [x] **Stils.** Pamatā melnbalts. Krāsa ir tur, kur tā palīdz saprast
  zīmējumu (sk. `trukstosie-atteli.md`, "Kas mainīts"). Krāsas ir no grāmatas
  dizaina paletes, un melnbaltā izdrukā tās atšķiras pēc toņa.
- [ ] **Uzraksti.** Visi uzraksti ir latviski un ņemti no nodaļu teksta;
  mainot terminu tekstā, tas jāmaina arī zīmējumā.
- [ ] **Izmēri.** Priekšskatījumā zīmējumi ir mērogoti līdz lapas platumam;
  šauriem zīmējumiem (piemēram, 11.1.) burti tāpēc iznāk lielāki. Jāizlīdzina
  maketēšanas posmā.

## Pa zīmējumiem

- [ ] **1.1.** Stacijas shēma ir vienkāršota: SWR mērītājs rādīts kā atsevišķa
  ierīce, lai gan daudziem transīveriem tas ir iebūvēts.
- [ ] **4.1.** Prefikss attēlots kā "YL un cipars" saskaņā ar MK 257
  33.1. punktu; 1. nodaļas tabulā prefikss ir "YL3". Jāizvēlas viens
  formulējums.
- [ ] **4.2.** Pilno radioamatieru joslu robežas (piemēram, 80 m — 3500–3800 kHz,
  40 m — 7000–7200 kHz) ir no vispārzināmām ziņām; B kategorijas robežas — no
  MK 257 2. pielikuma. 6 m joslas PRIM un sek daļas nav atdalītas.
- [ ] **5.2.** QSO piemērs angliski, tāpat kā 5.5. apakšnodaļas tabulā.
- [ ] **5.3.** Saucēju signāli ir ilustratīvi; frekvences atbilst 5.6. piemēram.
- [ ] **5.5.** Atkārtotāja frekvences (145,050 / 145,650 MHz) ir no kursa slaida;
  virziens joprojām jāpārbauda (sk. `05-piezimes.md`).
- [ ] **6.1.** Segmentu robežas atbilst 6.2. tabulai, kas rakstīta no atmiņas;
  **jāpārbauda pret aktuālo IARU 1. reģiona plānu kopā ar tabulu.**
- [ ] **6.3.** Sānjoslu forma shematiska; ≈ 3 kHz.
- [ ] **7.1.** Ūdens salīdzinājums ir shematisks (sūknis un sašaurinājums).
- [ ] **8.1.** Magnētiskais lauks zīmēts slīpā projekcijā pelēkā krāsā;
  jāpārbauda, vai tas ir saprotams.
- [ ] **8.3.** FM grafikā frekvences izmaiņa ir pārspīlēta uzskatāmībai.
- [ ] **8.4.** Spektru platumi nav mērogā viens pret otru; FM spektrs ir
  shematisks.
- [x] **9.1.** Rezistors zīmēts krāsās (dzeltena, violeta, sarkana, zelta =
  4,7 kΩ, kā 9.1. apakšnodaļas piemērā), zem tā krāsu tabula 0–9.
- [x] **9.7.** Pievienots MOSFET (inducēts N kanāls) blakus JFET; 9.7.
  apakšnodaļā teikums par abiem lauktranzistoru veidiem.
- [ ] **10.1., 10.2.** Līknes ir kvalitatīvas, bez skalām.
- [ ] **10.3.** Sprieguma formas ir shematiskas; pulsāciju lielums pārspīlēts.
- [x] **11.2.–11.6., 12.1.–12.4.** Blokshēmas pārzīmētas ar LRAL kursa
  7. nodarbības simboliem (filtrs kvadrātā ar viļņiem, pastiprinātājs —
  trijstūris, jaucējs — aplis ar krustu, ģenerators — aplis ar vilni,
  pārskaņojamam ar bultu, detektors, diskriminators) un slaidu bloku secību.
- [ ] **12.4.** Mazie spektri virs blokshēmas rāda augšējo sānjoslu.
- [ ] **13.2.** Vairākjoslu dipola un OCF skices ir vienkāršotas; OCF
  pieslēgvieta zīmēta trešdaļā garuma.
- [ ] **13.3.** Radiāļi zīmēti slīpi uz leju (kā antenai uz masta); zemes
  līmeņa antenai tie guļ uz zemes.
- [ ] **13.5.** Starojuma diagrammas ir kvalitatīvas, bez dB skalas; Yagi
  diagramma ir stilizēta, ne konkrētas antenas mērījums.
- [ ] **13.6.** Koaksiālā kabeļa slāņu biezumi nav mērogā.
- [ ] **14.2.** Zemes izliekums un jonosfēras augstums nav mērogā.
- [ ] **14.3.** Slāņu augstumi atbilst nodaļas tabulai (aptuveni skaitļi).
- [ ] **14.6.** NVIS staru leņķi ir shematiski.

### Jaunie zīmējumi (A prioritāte)

14. un 15. nodaļas attēli pārnumurēti: jaunais 14.1. attēls (spektra dalījums)
ir pirms bijušā 14.1., bet 15.3. (SWR līkne) — pirms osciloskopa, kas tagad
ir 15.4.

- [ ] **10.4.** Pastiprinātāja pakāpe ar kopējo emiteru ir tipiska mācību
  shēma; vērtības nav norādītas.
- [ ] **10.6.** Jaucēja piemērs ir tas pats, kas 10.6. apakšnodaļā (9 un 2 MHz).
- [ ] **10.7.** Loģiskie elementi zīmēti abos standartos — IEC (taisnstūris
  ar &, ≥1, 1) un ASV (ANSI). Jāpārbauda, kurš lietots ES eksāmena
  jautājumos; otru var izņemt.
- [ ] **13.7.** Baluns zīmēts pie antenas; skaņotājs — stacijā.
- [ ] **14.1.** Joslu atzīmes logaritmiskā mērogā; LF–UHF robežas kā 14.1.
  tabulā.
- [ ] **15.3.** SWR līkne ir ilustratīva (80 m dipols, rezonanse 3,65 MHz),
  nevis mērījums.
- [ ] **16.2.** Ferīti attēloti kā uzmavas uz vadiem.
- [ ] **17.3.** Krišanas zonas rādiuss = masta augstums; attālums līdz
  elektrolīnijai > h + L, kā 17.7. apakšnodaļā.
- [x] **16.1.** Pārzīmēts: traucējumi abos virzienos. Sarkanā krāsā raidītāja
  signāls, dzintara krāsā sadzīves elektronikas troksnis (invertori, barošanas
  bloki, LED, kondicionieri, siltumsūkņi, arī paša mājās).
- [ ] **17.2.** Labajā pusē rādīts nepareizs slēgums ar krustu; jāpārbauda,
  vai "nepareizi" piemērs atbilst tam, ko domā ES drošības materiāls.

## Kā trūkst

Pilns saraksts: `trukstosie-atteli.md`.

- [ ] 2., 3., 18. un 19. nodaļā zīmējumu nav; tur tie nav obligāti.
- [ ] 5. nodaļā lokatoru karte ar KO26 — nav uzzīmēta, jo vajag precīzu
  kartes pamatni.
- [ ] Fotogrāfiju nav vispār (QSL kartīte, transīvers, antenas). Tās jāsagādā
  LRAL ar autoru atļauju.

### Jaunie zīmējumi (B prioritāte)

Ievietojot jaunos zīmējumus, pārnumurēti: 5.1.→5.2., 5.2.→5.3., 5.3.→5.5.;
6.2.→6.3.; 7.3.→7.4.; 8.2.→8.3., 8.3.→8.4.; 10.5.→10.6., 10.6.→10.7.;
14.5.→14.6.; 17.1.→17.2., 17.2.→17.3.

- [ ] **3.1.** ITU → CEPT → MK un ES; IARU, IARU 1. reģions un LRAL pārstāv.
- [ ] **5.1.** Lokatora uzbūve shematiski, bez kartes; KO26 kā tekstā.
- [ ] **5.4.** QSL kartīte no izdomātās stacijas YL3ABC (Anna, Rīga, kā 5.5. QSO
  piemērā); dati no 5.6. žurnāla piemēra (ON3DXY, 21,285 MHz, SSB, 59). Jāpārbauda, vai YL3ABC
  nav izsniegts; ja ir, jāizvēlas cits.
- [ ] **6.2.** 40 m plāns pēc 6.2. tabulas (vienkāršots); **jāpārbauda pret
  IARU 1. reģiona plānu kopā ar tabulu.**
- [ ] **6.4.** 2 m plāns vienkāršots un rakstīts no atmiņas (segmentu robežas
  144,4 / 144,5 / 145,0 / 145,2 / 145,6 / 145,8 MHz); **obligāti jāpārbauda
  pret aktuālo IARU 1. reģiona VHF plānu.**
- [ ] **7.3.** Jaudas trijstūris tādā pašā formā kā Oma likuma trijstūris.
- [ ] **8.2.** Viļņu attiecība shematiska; diapazoni kā 8.3. tabulā.
- [ ] **10.5.** Ģenerators kā pastiprinātājs ar pozitīvu atgriezenisko saiti.
- [ ] **14.5.** Saules cikls ir stilizēts, **nav** mērījumu dati (tāpēc nav
  vajadzīga datu lietošanas atļauja); maksimumi ap 2014. un 2025. gadu.
- [ ] **14.7.** Zemes izliekums un antenu augstumi ļoti pārspīlēti; skaitļi
  kā 14.7. piemērā (16 m un 4 m → ap 25 km).
- [ ] **17.1.** Divi strāvas ceļi caur sirdi; cilvēka figūra vienkāršota.
- [ ] **17.4.** Zibens izlādnis pie kabeļa ievada; soļi kā 17.8. apakšnodaļā.

### Saskaņošana ar 7. nodarbības slaidiem

- [x] **11.1.** Jauns attēls: apzīmējumu skaidrojums, kā slaidā "Izmantotie
  apzīmējumi"; papildināts ar augsto frekvenču filtru, amplitūdas
  ierobežotāju, telegrāfa atslēgu un skaļruni, kas lietoti blokshēmās.
  Pārējie 11. nodaļas attēli pārnumurēti (11.1.–11.5. → 11.2.–11.6.).
- [x] **11.4.** Superheterodīna trakti krāsās kā slaidā: FM sarkans, AM zils,
  CW/SSB zaļš; katrs trakts pievienots ZFP atsevišķi. Paraksti kā slaidā
  (maisītājs, oscilators, atbalsta ģenerators, "lētajos nav").
- [x] **11.6.** SDR: „dzelžu” daļa zaļā, „PC” daļa sarkanā rāmī kā slaidā.
- [x] **12.2.** AM raidītājā trīs pastiprinātāji pirms izejas pakāpes, kā slaidā.
- [x] Pārbaudīta bloku secība visās 11. un 12. nodaļas blokshēmās pret
  slaidiem 16.–19. un 21.–24.; tā sakrīt. Vienīgā apzinātā atšķirība: SSB
  raidītājs (12.4.) zīmēts divās rindās, lai ietilptu A4 lapā, un tam
  pievienoti mazi spektri.
