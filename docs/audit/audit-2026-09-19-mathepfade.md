# Audit Level-Progression Mathepfade (2026-09-19)

Nur-Lese-Audit aller 90 Trainer. Es ergänzt die bereits behobenen harten
Gate-Fehler um das, was das Gate **nicht** sieht: Stufen, die formal sauber
sind, inhaltlich aber keine Steigerung darstellen.

## Vorgehen und seine Grenzen

Gemessen wird je Stufe die durchschnittliche Fragelänge, der Anteil Multiple
Choice, die Zahl der Aufgaben mit angesagter Rechenart, die Zahl der Aufgaben
mit AFB-III-Merkmal und die Länge des Lösungswegs.

**Kalibrierung.** Dieselbe Messung lief über die beiden Schwesterprojekte,
deren Zustand bekannt ist — die DifferenzierungsEngine und Ref4OHG sind
vollständig überarbeitet. Befunde je Trainer:

| Befund | DiffEngine | Ref4OHG | Mathepfade |
|---|---|---|---|
| KEIN_AFB3 | 0,67 | 0,80 | **1,63** |
| KOLLAPS | 0,27 | 0,30 | **0,78** |
| DÜNNER_WEG (alte Messung) | 0,01 | 0,01 | **0,67** |

Daraus folgt, was man den Zahlen glauben darf:

- **KOLLAPS ist belastbar.** Mathepfade liegt beim Dreifachen der beiden
  überarbeiteten Projekte. Eine Stichprobe hat den Befund bestätigt: In
  `9-raumgeometrie-prisma-zylinder` rechnen Stufe 4 und Stufe 5 beide
  „Volumen oder Oberfläche, nur mit anderer Grundfläche".
- **KEIN_AFB3 ist es nicht.** Der Zähler sucht Schlagwörter (begründe, warum,
  Fehler, prüfe …) und schlägt deshalb auch bei der fertigen
  DifferenzierungsEngine an. Im selben Trainer ist Aufgabe #30 („Schneidet eine
  Ebene parallel zur Grundfläche ein Prisma, ist die Schnittfigur …") eine
  Begründungsaufgabe, die der Zähler übersieht. Die Spalte ist ein Hinweis,
  kein Urteil.

## Der Hauptbefund: die Lösungswege

Ein Lösungsweg soll den Weg zeigen, nicht das Ergebnis wiederholen. Als dünn
gilt hier ein Lösungsweg, der **weder** einen erklärenden Satz (mindestens vier
Wörter) **noch** einen sichtbaren Rechenschritt enthält.

**Das Kriterium musste zweimal nachgeschärft werden** — beide Male, weil es sonst
Lösungswege beanstandet hätte, die in Ordnung sind:

1. Die erste Fassung wertete jede formellastige Zeile als dünn und hätte 42 % der
   bereits überarbeiteten DifferenzierungsEngine getroffen. Reine Formelketten wie
   `$$5x + 3x = (5+3)x = 8x$$` sind aber vollwertige Lösungswege.
2. Die zweite Fassung zählte nur `=` als Rechenschritt. Bei Ungleichungen steht
   dort aber `\leq`, `\geq` oder `\implies` — `$$3x - 2x \leq 5 + 7 \implies x \leq 12$$`
   wurde dadurch fälschlich als dünn geführt. In `7-ungleichungen` waren nach diesem
   Kriterium 20 Aufgaben auffällig, tatsächlich ist es **eine**.

Mit dem endgültigen Kriterium (Rechenschritt = `=`, `\leq`, `\geq`, `\implies`,
`\Rightarrow`, `\approx`, `<`, `>`):

| Projekt | dünne Lösungswege |
|---|---|
| DifferenzierungsEngine | 39 von 3708 (1 %) |
| Ref4OHG | 31 von 2736 (1 %) |
| **Mathepfade** | **rund 1180 von 3240 (36 %)** |

Zum Vergleich, beide aus Stufe 1:

- DifferenzierungsEngine, `7-terme-vereinfachen` #1:
  `$$5x + 3x = (5+3) \cdot x = 8x$$` — zeigt den Schritt.
- Mathepfade, `11-steckbriefaufgaben` #2: `\(f(2)=5\).` — nur das Ergebnis.

Das ist derselbe Befund, der im Statusbericht als „Telegrammstil" steht. Die
zunächst genannte Zahl von 1356 war um rund 15 % zu hoch.

## Arbeitsliste

Vorrang haben die 20 Trainer mit KOLLAPS zwischen den oberen Stufen (L4/L5 oder
L5/L6) — dort ist die Steigerung genau da flach, wo sie am wichtigsten ist:

`11-ableitung-ketten-produkt`, `11-e-funktion-ableitung`, `11-e-funktion`,
`11-tangenten-normalen`, `12-geraden-raum`, `12-lk-stoch-prozesse`,
`12-vektoren-grundlagen`, `7-binomische-formeln`, `7-gleichungen-linear`,
`8-bruchterme-grundlagen`, `8-strahlensatz`, `8-vektoren-2d`,
`9-exponentielles-wachstum`, `9-flaechenberechnung-determinante`,
`9-potenzen-rational`, `9-pythagoras`, `9-raumgeometrie-anwendungen`,
`9-raumgeometrie-prisma-zylinder`, `9-raumgeometrie-pyramide-kegel`,
`9-stoch-haeufigkeiten`.

Weitere 11 Trainer zeigen KOLLAPS zwischen L3 und L4.


## Messwerte je Trainer

Die Zahlen sind die durchschnittlichen Fragelängen je Stufe.

```
Trainer                                      L1  L2  L3  L4  L5  L6   Befunde
10-exponentialfunktionen.html                51  60  64  68  93  77   KEIN_AFB3 L5; KOLLAPS L1/L2
10-ganzrationale-funktionen.html             45  51  49  54  68  60   KEIN_AFB3 L6; DUENNER_WEG (Stufen 2)
10-graphen-transformationen.html             34  65  64  52  83  67   KEIN_AFB3 L5; KEIN_AFB3 L6
10-kreissektor.html                          71  80  75  93  63 134   KEIN_AFB3 L5; KOLLAPS L2/L3
10-logarithmus.html                          32  34  60  34  57  89   KEIN_AFB3 L5; KEIN_AFB3 L6
10-polynomdivision.html                      54  47  58  56 101  91   KEIN_AFB3 L5; KOLLAPS L2/L3
10-potenzfunktionen.html                     40  49  66  57  55  68   KEIN_AFB3 L5; KEIN_AFB3 L6
10-stoch-bedingte-wsk.html                   60 131 116  74 119  99   KEIN_AFB3 L5; KEIN_AFB3 L6
10-stoch-mehrstufig.html                     66  80  62  78  65  92   KEIN_AFB3 L5; KEIN_AFB3 L6
10-substitution.html                         75  58  76  64  73  79   ok
10-trig-einheitskreis.html                   48  57  57  61  99  97   KEIN_AFB3 L5; KEIN_AFB3 L6
10-trig-gleichungen.html                     63  79  73  76  75 107   KEIN_AFB3 L5; KEIN_AFB3 L6
10-trig-sinusfunktion.html                   57  40  86  86  83 178   KEIN_AFB3 L5; KEIN_AFB3 L6
10-trig-sinussatz-kosinussatz.html           41  88  85  91 144 103   KEIN_AFB3 L6; KOLLAPS L2/L3; KOLLAPS L3/L4
11-ableitung-ketten-produkt.html             42  35  39  43  47  42   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L2/L3; KOLLAPS L5/L6; KURZ (Stufen 1,2,3,4,6); DUENNER_WEG (Stufen 1,2,3)
11-ableitungsregeln.html                     48  63  67  61  70  67   KEIN_AFB3 L5; KOLLAPS L2/L3; DUENNER_WEG (Stufen 1,4)
11-aenderungsrate.html                       68  79  78  68  86  92   KEIN_AFB3 L5; DUENNER_WEG (Stufen 4,5,6)
11-e-funktion-ableitung.html                 25  22  27  41  45  41   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L1/L2; KOLLAPS L4/L5; KOLLAPS L5/L6; KURZ (Stufen 1,2,3,4,6); DUENNER_WEG (Stufen 1,2,3,4,5,6)
11-e-funktion.html                           30  25  22  40  59  60   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L5/L6; KURZ (Stufen 1,2,3,4); DUENNER_WEG (Stufen 1,2,3,4,5,6)
11-extrempunkte-wendepunkte.html             41  44  48  63  49  51   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L1/L2; KOLLAPS L2/L3; DUENNER_WEG (Stufen 1,2,5)
11-extremwertaufgaben.html                   32  50  92  70  78  60   KEIN_AFB3 L5; KEIN_AFB3 L6; DUENNER_WEG (Stufen 1,2,6)
11-kurvendiskussion-ganzrational.html        41  42  47  44  49  57   KEIN_AFB3 L6; DUENNER_WEG (Stufen 1,2,3,4,5)
11-lk-funktionsscharen.html                  39  60  58  63  75  73   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L2/L3; DUENNER_WEG (Stufen 1,2,3,4,5)
11-lk-gebrochen-rational.html                31  46  84  39  61  58   KEIN_AFB3 L5; KEIN_AFB3 L6; DUENNER_WEG (Stufen 1,2,3,4,5,6)
11-lk-kurvendisk-erweitert.html              33  39  37  47  37  37   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L3/L4; KURZ (Stufen 1,2,3,5,6); DUENNER_WEG (Stufen 1,2,3,4,5,6)
11-lk-newton.html                            40  47  54  48  66  44   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L2/L3; DUENNER_WEG (Stufen 1,2,3,4,6)
11-monotonie-kruemmung.html                  38  45  39  44  43  61   KEIN_AFB3 L5; KOLLAPS L2/L3; KOLLAPS L3/L4; KURZ (Stufen 1,3,4,5); DUENNER_WEG (Stufen 1,2,3,5)
11-steckbriefaufgaben.html                   42  62  57  89 104  73   KEIN_AFB3 L5; KEIN_AFB3 L6; DUENNER_WEG (Stufen 1,2,4,5,6)
11-tangenten-normalen.html                   56  58  51  66  57  72   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L2/L3; KOLLAPS L4/L5; DUENNER_WEG (Stufen 3,4)
12-bestimmtes-integral.html                  37  34  37  41  64  75   KEIN_AFB3 L5; KOLLAPS L2/L3; KOLLAPS L3/L4; KURZ (Stufen 1,2,3,4)
12-ebenen.html                               39  45  59 103  89  76   KEIN_AFB3 L5; KEIN_AFB3 L6; DUENNER_WEG (Stufen 2,3)
12-flaechenberechnung.html                   65  51  70  82  73  89   KEIN_AFB3 L5; KEIN_AFB3 L6
12-geraden-raum.html                         85 121  95 140 122 113   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L5/L6
12-lk-dgl.html                               39  54  35  61  80  52   KEIN_AFB3 L5; KEIN_AFB3 L6; DUENNER_WEG (Stufen 1,2)
12-lk-geom-abstaende.html                    69  51  70  70  84 106   KEIN_AFB3 L5; KOLLAPS L3/L4; DUENNER_WEG (Stufen 2)
12-lk-geom-lagebeziehungen.html              53  69  69  88  73 108   KEIN_AFB3 L5; KEIN_AFB3 L6; DUENNER_WEG (Stufen 4)
12-lk-geom-schnittwinkel.html                51  52  62  60  47 112   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L2/L3; KOLLAPS L3/L4; DUENNER_WEG (Stufen 2,3)
12-lk-integral-rotationskoerper.html         59  47  61  69  76  78   KEIN_AFB3 L5; KEIN_AFB3 L6; DUENNER_WEG (Stufen 6)
12-lk-integral-uneigentlich.html             47  48  38  46  54  55   KEIN_AFB3 L5; KEIN_AFB3 L6; DUENNER_WEG (Stufen 2,3,4)
12-lk-stoch-normalverteilung.html            54  46  39  67  80 104   KEIN_AFB3 L5; KEIN_AFB3 L6; DUENNER_WEG (Stufen 1,3,4,5)
12-lk-stoch-prozesse.html                    52 111  93  93  94 129   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L3/L4; KOLLAPS L4/L5; DUENNER_WEG (Stufen 2,3,4,5,6)
12-skalarprodukt.html                        75 113 100  89 130 125   KEIN_AFB3 L5; KEIN_AFB3 L6
12-stammfunktionen.html                      60  46  50  42  50  67   KEIN_AFB3 L5; KEIN_AFB3 L6; DUENNER_WEG (Stufen 2,4)
12-stoch-binomialverteilung.html             48  63  52  56 108  84   KEIN_AFB3 L5; KEIN_AFB3 L6
12-stoch-hypothesentests.html                35  54  85  68  95  73   RUECKFALL L5 (3 gegen L4 4); RUECKFALL L6 (1 gegen L4 4)
12-stoch-sigma-regeln.html                   47  70  76  71 100  79   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L2/L3; KOLLAPS L3/L4; DUENNER_WEG (Stufen 2,6)
12-stoch-zufallsgroessen.html                57  80  64  67  46  68   KEIN_AFB3 L5; KEIN_AFB3 L6; DUENNER_WEG (Stufen 2,4,5)
12-vektoren-grundlagen.html                  62 118  68  99  89  96   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L5/L6; DUENNER_WEG (Stufen 3)
7-binomische-formeln.html                    44  40  42  45  49  71   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L2/L3; KOLLAPS L4/L5; DUENNER_WEG (Stufen 2,3)
7-daten-diagramme.html                       59  73  86  69 120 117   KEIN_AFB3 L5
7-dreiecke-kongruenz.html                    45  86  75  66 103 123   KEIN_AFB3 L5; KEIN_AFB3 L6
7-gleichungen-linear.html                    29  27  30  37  48  88   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L3/L4; KOLLAPS L4/L5; KURZ (Stufen 1,2,3,4); DUENNER_WEG (Stufen 3)
7-konstruktionen.html                        61  76  87  56  85 129   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L2/L3
7-potenzgesetze.html                         24  33  38  32  38  66   KEIN_AFB3 L5; KURZ (Stufen 1,2,3,4,5); DUENNER_WEG (Stufen 2,3)
7-symmetrie.html                             54  34  74  68  83  85   KEIN_AFB3 L5; KEIN_AFB3 L6
7-terme-aufstellen.html                      54  57 109  72 137 136   KEIN_AFB3 L6; DUENNER_WEG (Stufen 2)
7-terme-umformungen.html                     39  47  48  44  56  71   KEIN_AFB3 L5; KOLLAPS L2/L3; DUENNER_WEG (Stufen 2)
7-ungleichungen.html                         36  40  60  40  64 116   KEIN_AFB3 L5; KEIN_AFB3 L6
7-vierecke.html                              62  87  89  72 120  87   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L2/L3; DUENNER_WEG (Stufen 2)
7-winkel-winkelsumme.html                    48  85  98  87 113  83   KEIN_AFB3 L6
8-aehnlichkeit-streckung.html                58  79  86  98 124 106   KEIN_AFB3 L5; DUENNER_WEG (Stufen 2,4)
8-bruchgleichungen.html                      40  45  55  41  55  83   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L2/L3
8-bruchterme-grundlagen.html                 50  55  69  54  56  73   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L4/L5
8-kreise.html                                48  77  86  90 102 120   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L3/L4; DUENNER_WEG (Stufen 1)
8-lgs.html                                   43  52  57  55  73  52   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L3/L4
8-lineare-funktionen-anwendungen.html        60  59  86  69  83  72   KEIN_AFB3 L5; KOLLAPS L1/L2; DUENNER_WEG (Stufen 4)
8-lineare-funktionen-grund.html              44  48  44  50  68  54   KEIN_AFB3 L5; DUENNER_WEG (Stufen 2,5)
8-potenzen-negativ.html                      30  33  30  47  37  67   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L1/L2; KOLLAPS L2/L3; KURZ (Stufen 1,2,3,5); DUENNER_WEG (Stufen 1,2,3,4)
8-proportionalitaet.html                     52  50  52  76  60  72   KEIN_AFB3 L5; KOLLAPS L1/L2; KOLLAPS L2/L3
8-raumgeometrie-grund.html                   37  78  77  94  81 132   KEIN_AFB3 L5; KEIN_AFB3 L6; DUENNER_WEG (Stufen 1,2)
8-stoch-laplace.html                         45  53  53  52  60  76   KEIN_AFB3 L6; KOLLAPS L2/L3; KOLLAPS L3/L4; DUENNER_WEG (Stufen 2,3)
8-stoch-zaehlprinzip.html                    60  44  65  60  77  67   KEIN_AFB3 L5; DUENNER_WEG (Stufen 1,2,3,4,5,6)
8-strahlensatz.html                          50  64  88 103 109 130   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L4/L5
8-vektoren-2d.html                           40  51  64  62  76  67   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L5/L6; DUENNER_WEG (Stufen 1,2,3,4,5,6)
9-exponentielles-wachstum.html               41  61  65  72  75  81   KEIN_AFB3 L5; KOLLAPS L4/L5; DUENNER_WEG (Stufen 1,2,3,5)
9-flaechenberechnung-determinante.html       36  55  54  62  55  71   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L2/L3; KOLLAPS L3/L4; KOLLAPS L4/L5; DUENNER_WEG (Stufen 2,5,6)
9-potenzen-ganzzahlig.html                   23  40  36  37  82  56   KEIN_AFB3 L5; KURZ (Stufen 1,2,3,4); DUENNER_WEG (Stufen 1,3,4)
9-potenzen-rational.html                     23  27  30  42  38  57   KEIN_AFB3 L5; KOLLAPS L1/L2; KOLLAPS L4/L5; KURZ (Stufen 1,2,3,4,5); DUENNER_WEG (Stufen 1,2,3,5)
9-potenzgleichungen.html                     29  33  36  28  46  43   KEIN_AFB3 L6; KOLLAPS L1/L2; KURZ (Stufen 1,2,3,4,6); DUENNER_WEG (Stufen 1,2,3,4,5,6)
9-pythagoras.html                            42  48  74  64  72  94   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L3/L4; KOLLAPS L4/L5; DUENNER_WEG (Stufen 2,3,4,5)
9-quadratische-funktionen.html               46  52  59  56  79  76   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L3/L4; DUENNER_WEG (Stufen 1,2,3,4,6)
9-quadratische-gleichungen.html              37  42  42  57  80  57   KEIN_AFB3 L5; KEIN_AFB3 L6; DUENNER_WEG (Stufen 1)
9-quadratwurzeln.html                        29  39  40  49  83  74   KEIN_AFB3 L5; DUENNER_WEG (Stufen 1,2,3)
9-raumgeometrie-anwendungen.html             52  72  77  71  73  81   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L2/L3; KOLLAPS L3/L4; KOLLAPS L4/L5; DUENNER_WEG (Stufen 1,2,4,5)
9-raumgeometrie-prisma-zylinder.html         37  47  74  69  74  84   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L3/L4; KOLLAPS L4/L5; DUENNER_WEG (Stufen 1,2,3,4,5,6)
9-raumgeometrie-pyramide-kegel.html          31  44  60  74  68  80   KEIN_AFB3 L5; KOLLAPS L4/L5; DUENNER_WEG (Stufen 1,3,5,6)
9-stoch-boxplot.html                         26  29  51  87  57  91   KEIN_AFB3 L5; DUENNER_WEG (Stufen 1,2,3,4,5,6)
9-stoch-haeufigkeiten.html                   41  30  60  57  47  78   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L4/L5; DUENNER_WEG (Stufen 1,2,4,5,6)
9-trig-rechtwinkliges-dreieck.html           39  56  64  69  74  79   KEIN_AFB3 L5; KEIN_AFB3 L6; DUENNER_WEG (Stufen 2,3,4)
9-wurzelgleichungen.html                     28  31  50  59  51  75   KEIN_AFB3 L5; KEIN_AFB3 L6; KOLLAPS L1/L2; DUENNER_WEG (Stufen 1,2,4)

--- Haeufigkeit der Befunde ---
  147  KEIN_AFB3
   70  KOLLAPS
   60  DUENNER_WEG
   12  KURZ
    2  RUECKFALL

89 von 90 Trainern mit Befund
```

## Dünne Lösungswege je Trainer

Stand nach der laufenden Überarbeitung, mit dem endgültigen Kriterium:

```

614 von 3240 Loesungswegen sind duenn (18 %), in 67 Trainern
   27  12-lk-stoch-prozesse.html
   23  12-lk-geom-schnittwinkel.html
   22  12-lk-integral-uneigentlich.html
   21  8-vektoren-2d.html
   20  9-exponentielles-wachstum.html
   19  11-kurvendiskussion-ganzrational.html
   19  12-lk-dgl.html
   17  11-aenderungsrate.html
   17  12-stammfunktionen.html
   16  10-polynomdivision.html
   16  7-terme-umformungen.html
   15  12-ebenen.html
   15  12-stoch-zufallsgroessen.html
   15  9-potenzen-rational.html
   14  10-graphen-transformationen.html
```

## Abschluss Punkt 1 (19.09.2026)

Alle dünnen Lösungswege sind ersetzt.

```
Mathepfade:  0 von 3240 (vorher ~1180, 36 %)
Ref4OHG:     0 von 2736 (vorher 31, 1 %)
```

Jeder neue Lösungsweg nennt den Ansatz, führt die Rechnung in KaTeX vor und
schließt — wo es trägt — mit Probe, Begründung oder dem typischen Fehler ab.
Alle Zahlenwerte sind mit Wolfram geprüft.

Nebenbefunde, die dabei aufgefallen und mitbehoben wurden:

| Befund | Umfang |
|---|---|
| ASCII-Umschreibungen statt Umlauten (Flaeche, Hoehe, fuer …) | 205 Stellen in 10 Mathepfade-Trainern, 2 in Ref4OHG |
| Rückverweise auf die Vorgängeraufgabe (die Engine wählt frei) | 6 Aufgaben: 10-stoch-mehrstufig #24/#32, 10-stoch-bedingte-wsk #30/#32, 9-quadratische-funktionen #30, 12-stoch-hypothesentests #27, dazu ein Tipp in 10-substitution #5 |
| Aufgabe auf Stufe 6 inhaltlich identisch mit einer auf Stufe 5 | 12-lk-integral-rotationskoerper #35 — ersetzt durch eine Umkehraufgabe (Volumen gegeben, Integrationsgrenze gesucht) |
| Falscher Zahlwert im Tipp | 12-lk-integral-rotationskoerper #24: 0,0803 → 0,0808 |
| KaTeX-Fehler, den nur das Render-Gate findet | 11-extremwertaufgaben #17: `V_\max` → `V_{\max}` |

Offen (nicht Teil von Punkt 1, zur Entscheidung):

- `11-ableitungsregeln` (Mathepfade): 10 Aufgaben ab Stufe 4 werden an der
  Stelle \(x = 0\) ausgewertet und trivialisieren damit die Produkt- bzw.
  Kettenregel. Das Level-Gate meldet das, die Aufgaben müssten neu gestellt
  werden.
- 18 Doppelungen zwischen Trainern (Level-Gate: „identisch mit …"). Die
  meisten sind unkritisch (Grundwissen in zwei Themen), ein paar Paare auf
  gleicher Stufe wären einen Austausch wert.
