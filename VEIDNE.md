# Nodaļas veidne un pieraksta noteikumi

Visas nodaļas ir būvētas pēc vienas veidnes. Nokopē zemāk doto karkasu jaunā
failā `nodalas/NN-nosaukums.md` un aizpildi.

## Pieraksta noteikumi

- **Virsraksti.** `#` tikai nodaļas nosaukumam, `##` apakšnodaļām (5.1., 5.2.),
  `###` sīkākam dalījumam.
- **Termini.** Jaunu terminu pirmajā lietojumā raksta **treknrakstā** un
  pievieno terminu vārdnīcai (I pielikums).
- **Izceltie lodziņi.** Raksta kā citātu ar treknu nosaukumu pirmajā rindā:

  ```markdown
  > **Praktisks padoms.** Teksts.

  > **Uzmanību!** Teksts.

  > **Piemērs.** Uzdevuma formulējums.
  >
  > 1. Pirmais solis.
  > 2. Otrais solis.
  ```

  Atļautie nosaukumi: `Praktisks padoms.`, `Uzmanību!`, `Piemērs.`,
  `Atceries:`, `Padziļināti.`
- **Formulas.** LaTeX pierakstā: rindā `$U = I \cdot R$`, atsevišķā rindā
  `$$f = \frac{1}{2\pi\sqrt{LC}}$$`.
- **Terminoloģija.** Digitālos darba veidus (FT8, RTTY, PSK31 u.c.) sauc par
  **ciparu darba veidiem**; sinonīms — ciparu režīmi. Vārdu "ciparātie"
  nelieto. MK noteikumu apzīmējums ir MGM. Vārdu "UKV" nelieto: raksta VHF,
  UHF vai konkrētu diapazonu (piemēram, "2 m diapazons"). SSB sadaļās raksta
  "sānjoslas izvēle", nevis "paražas".
- **Skaitļi.** Decimālais komats (21,295 MHz), atstarpe starp skaitli un
  mērvienību (100 W, 50 Ω).
- **Atsauces.** Tekstā numurs kvadrātiekavās, piemēram, `[2]`; numuri atbilst
  sarakstam nodaļas beigās. Normatīvajiem aktiem norāda punktu.
- **Attēli.** Atsevišķā rindā: `![7.1. attēls. Paraksts.](../atteli/07-1-nosaukums.svg)`.
  Teksts kvadrātiekavās kļūst par attēla parakstu. Faila nosaukums sākas ar
  nodaļas un attēla numuru. Zīmējumus ģenerē ar kodu mapē `riki/zim/`;
  svešiem attēliem `avoti.md` norāda autoru un licenci.
- **Zīmējumu vietas.** Kamēr zīmējuma vēl nav, tā vietu atzīmē ar komentāru
  `<!-- ZĪMĒJUMS 7.1: īss apraksts, kas jāuzzīmē -->`.
- **C kategorija.** Apakšnodaļas, kas vajadzīgas arī C kategorijas eksāmenam,
  virsraksta beigās atzīmē ar `{.c-kategorija}`.
- **Piezīmes recenzentam** nodaļas failā neraksta; tās glabā
  `recenzijas/NN-piezimes.md`.

## Karkass

```markdown
# N. nodaļa. Nosaukums

Viens teikums: ko šī nodaļa iemāca.

**Video lekcija:** LRAL bezmaksas kurss, N. nodarbība.
**Eksāmena programma:** sadaļas nosaukums.
**Mācību laiks:** ap N stundām.

## Pēc šīs nodaļas tu pratīsi

- trīs līdz pieci pārbaudāmi mācību mērķi;

## N.1. Apakšnodaļa

Pamatteksts īsās rindkopās, ar zīmējumiem.

> **Piemērs.** Atrisināts uzdevums soli pa solim.

> **Praktisks padoms.** Pieredzējuša operatora ieteikums.

> **Uzmanību!** Drošības brīdinājums vai tipiska kļūda.

## Eksāmenā jāzina

- skaitļi, definīcijas un formulas, ko eksāmenā jautā tieši.

## Pamēģini pats

Viens līdz trīs nelieli praktiski uzdevumi.

## Kopsavilkums

- pieci līdz astoņi punkti.

## Paškontroles jautājumi

10–15 jautājumi: pārsvarā jauni testa jautājumi ar četrām atbildēm,
daži aprēķinu uzdevumi un divi atvērti jautājumi.

## Atbildes

Tabula: numurs, atbilde, skaidrojums. (Grāmatā tiks pārcelta uz G pielikumu.)

## Padziļināti

Neobligāta viela tiem, kas grib zināt vairāk.

## Nodaļas avoti

1. Numurēts saraksts.
```
