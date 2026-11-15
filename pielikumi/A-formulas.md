# A pielikums. Formulu lapa

Eksāmenā vajadzīgās formulas, mērvienības un tabulas vienuviet. Lapa
atbilst LRAL bezmaksas kursa formulu lapai.

## Oma likums un jauda

| Formula | Ko aprēķina |
| --- | --- |
| $U = I \cdot R$ | Spriegums |
| $I = U / R$ | Strāva |
| $R = U / I$ | Pretestība |
| $P = U \cdot I$ | Jauda |
| $P = I^2 \cdot R$ | Jauda, ja zināma strāva un pretestība |
| $P = U^2 / R$ | Jauda, ja zināms spriegums un pretestība |

$U$ — spriegums [V], $I$ — strāva [A], $R$ — pretestība [Ω], $P$ — jauda [W].

## Rezistori, kondensatori un spoles

| | Virknes slēgums | Paralēlais slēgums |
| --- | --- | --- |
| Rezistori | $R = R_1 + R_2 + \dots$ | $\frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2} + \dots$ |
| Kondensatori | $\frac{1}{C} = \frac{1}{C_1} + \frac{1}{C_2} + \dots$ | $C = C_1 + C_2 + \dots$ |
| Spoles | $L = L_1 + L_2 + \dots$ | $\frac{1}{L} = \frac{1}{L_1} + \frac{1}{L_2} + \dots$ |

Diviem rezistoriem paralēli: $R = \frac{R_1 \cdot R_2}{R_1 + R_2}$.

> **Atceries:** kondensatori slēgumos uzvedas pretēji rezistoriem un spolēm.

## Maiņstrāva

| Formula | Ko nozīmē |
| --- | --- |
| $U_{RMS} = U_{max} / \sqrt{2} \approx 0{,}707 \cdot U_{max}$ | Efektīvā vērtība no amplitūdas |
| $U_{max} = U_{RMS} \cdot \sqrt{2} \approx 1{,}414 \cdot U_{RMS}$ | Amplitūda no efektīvās vērtības |
| $U_{p\text{-}p} = 2 \cdot U_{max}$ | Spriegums no smailes līdz smailei |
| $f = 1 / T$, $T = 1 / f$ | Frekvence un periods |
| $\omega = 2 \pi f$ | Leņķiskā frekvence |
| $u(t) = U_{max} \cdot \sin(\omega t + \varphi)$ | Momentānais spriegums |

## Reaktīvā pretestība un rezonanse

| Formula | Ko nozīmē |
| --- | --- |
| $X_C = \frac{1}{2 \pi f C}$ | Kondensatora pretestība; frekvencei augot, samazinās |
| $X_L = 2 \pi f L$ | Spoles pretestība; frekvencei augot, pieaug |
| $f = \frac{1}{2 \pi \sqrt{L C}}$ | LC kontūra rezonanses frekvence |

$f$ — frekvence [Hz], $C$ — kapacitāte [F], $L$ — induktivitāte [H],
$\pi \approx 3{,}14$.

## Viļņa garums un antenas

| Formula | Ko nozīmē |
| --- | --- |
| $\lambda = c / f$, $c \approx 3 \cdot 10^8$ m/s | Viļņa garums |
| $\lambda\,[\text{m}] = 300 / f\,[\text{MHz}]$ | Ērtā forma |
| $L\,[\text{m}] \approx 142{,}5 / f\,[\text{MHz}]$ | Pusviļņa dipola garums |

## Transformators

$$\frac{U_2}{U_1} = \frac{N_2}{N_1}$$

$N_1$, $N_2$ — vijumu skaits primārajā un sekundārajā tinumā.

## Kirhofa likumi

- **Strāvu likums:** mezglā ieplūstošo strāvu summa ir vienāda ar izplūstošo
  strāvu summu.
- **Spriegumu likums:** slēgtā kontūrā sprieguma kritumu summa ir vienāda ar
  avota spriegumu.

## Decibeli

$$P_{dB} = 10 \cdot \lg \frac{P}{P_{ref}} \qquad U_{dB} = 20 \cdot \lg \frac{U}{U_{ref}}$$

| dB | Jaudas attiecība | dB | Jaudas attiecība |
| --- | --- | --- | --- |
| 1 | 1,26 | 10 | 10 |
| 2 | 1,58 | 15 | 31,6 |
| 3 | 2 | 20 | 100 |
| 4 | 2,51 | 25 | 316 |
| 6 | 4 | 30 | 1000 |
| 8 | 6,31 | 40 | 10 000 |

Viena S vienība ir 6 dB. Virknē slēgtu pakāpju decibelus saskaita.

## Metriskie prefiksi

| Prefikss | Apzīmējums | Reizinātājs | Piemērs |
| --- | --- | --- | --- |
| tera | T | $10^{12}$ | 1 TΩ |
| giga | G | $10^{9}$ | 1 GHz |
| mega | M | $10^{6}$ | 1 MΩ |
| kilo | k | $10^{3}$ | 1 kΩ |
| mili | m | $10^{-3}$ | 1 mA |
| mikro | µ | $10^{-6}$ | 1 µF |
| nano | n | $10^{-9}$ | 1 nF |
| piko | p | $10^{-12}$ | 1 pF |

## Loģiskie elementi

| A | B | UN (AND) | VAI (OR) |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 |

NE (NOT) pārvērš ieeju pretējā: 0 → 1, 1 → 0.

## Binārā sistēma

**No binārā uz decimālo:** saskaita divnieka pakāpes tajās pozīcijās, kur ir
1. Piemērs: $1011_2 = 8 + 0 + 2 + 1 = 11_{10}$.

**No decimālā uz bināro:** dala ar 2 un pieraksta atlikumus; rezultātu lasa no
apakšas uz augšu. Piemērs: 11 : 2 = 5 (atl. 1), 5 : 2 = 2 (atl. 1),
2 : 2 = 1 (atl. 0), 1 : 2 = 0 (atl. 1) → $1011_2$.

| $2^0$ | $2^1$ | $2^2$ | $2^3$ | $2^4$ | $2^5$ | $2^6$ | $2^7$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 |
