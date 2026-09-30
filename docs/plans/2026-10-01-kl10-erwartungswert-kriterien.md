# Neuer Trainer Kl. 10: Zufallsgrößen und Erwartungswert (TH 2.3.4)

Angelegt 2026-10-01. Lokale Nachvollziehbarkeit; im Public-HTML stehen die Kriterien bewusst nicht.
Datei: `trainer/10-stoch-erwartungswert.html`, `THEMA_KEY = '10-stoch-erwartungswert'`,
`THEMA_CONFIG.name = 'Zufallsgrößen & Erwartungswert'`. Index-Zeile: Spalte `.col-10`,
Abschnitt „C · Stochastik“, als dritter und letzter Eintrag (Connector `└`; der bisher letzte
Eintrag `10-stoch-mehrstufig` steht jetzt auf `├`).

Dies ist der **91. Trainer** — kein Ersatz, sondern neu.

## Welche Lücke er schließt

`docs/plans/2026-09-26-kl10-kriterien.md`, Block C, „Offene Punkte“: Die alte Stufe 5 von
`10-stoch-mehrstufig` bestand ausschließlich aus Erwartungswert-Aufgaben und wurde in der Welle
Task 7 der **Trainer-Abgrenzung** wegen entfernt (jener Trainer ist Baumdiagramm und Pfadregeln).
Damit war Wahrscheinlichkeitsverteilung, Erwartungswert und Standardabweichung diskreter
Zufallsgrößen in Klasse 10 nicht mehr abgedeckt, obwohl TH 2.3.4 für Klassenstufe 10 wörtlich
nennt:

- „Wahrscheinlichkeitsverteilungen diskreter Zufallsgrößen bestimmen“
- „Erwartungswert und Standardabweichung diskreter Zufallsgrößen berechnen und interpretieren
  (in einfachen Fällen auch ohne Hilfsmittel)“
- „mit dem Symbol Σ rechnen“

Alle drei Punkte sind abgedeckt: die Σ-Schreibweise in #4, #5 und im Lösungsweg von #34, die
Verteilung in #2, #8, #13, #14, #17, #25, #28, das Rechnen ohne Hilfsmittel ausdrücklich in #10.

## Abgrenzung gegen die Nachbartrainer

**Gegen `12-stoch-zufallsgroessen` (Kl. 12, Abiturniveau)** — die wichtigste Grenze. Dort:
Binomialverteilung (#12, #33), Verschiebungssatz \(V(X)=E(X^2)-E(X)^2\) (#17, #18, #27, #34),
lineare Transformation und Additionssatz der Varianz (#27, #29, #36), faires Spiel als
durchgehendes Motiv der Stufe 4 (#19–#24), Abi-Format auf Stufe 6.
Hier: **keine** Binomialverteilung, **kein** Verschiebungssatz (die Varianz wird durchgehend
über die Definition \(V(X)=\sum (x_i-\mu)^2 P(X=x_i)\) gerechnet), **keine** lineare
Transformation, **kein** Additionssatz. Alle 36 Aufgaben wurden gegen die 36 Aufgaben dort
gelesen; keine wiederholt eine davon, auch nicht mit anderen Zahlen. Insbesondere vermieden:
E(X) und V(X) des fairen Würfels (dort #7, #14, #15), die bare Drei-Werte-Verteilung mit
gesuchtem E(X) (dort #8, #11), die symmetrische Verteilung um null (dort #9), das Glücksrad
mit einer Auszahlung (dort #10), die Umkehraufgabe „Einsatz aus der Fairness-Bedingung“
(dort #21, #28), „Wert a aus E(X) und einer Wahrscheinlichkeit“ mit zwei Werten (dort #30),
„Verteilung aus Summennormierung und E(X)“ mit drei Werten (dort #25), die Behauptungen
„gleicher Erwartungswert ⇒ gleiche Streuung“ (dort #32) und „faires Spiel ⇒ σ = 0“ (dort #35).
Das faire Spiel kommt hier genau einmal vor (#32) und dann als **Nachweis durch Rechnung**
mit anschließender Beurteilung, nicht als Begriffsabfrage oder Einsatz-Umkehraufgabe.
Der Risikovergleich zweier Angebote bei gleichem Erwartungswert steht hier als **Rechenaufgabe**
(#35: beide σ selbst bestimmen), dort als MC-Behauptung bzw. mit gegebenen σ-Werten.

**Gegen `10-stoch-mehrstufig`** (Pfadregeln, Baumdiagramm): Das Baumdiagramm wird in #14 und #25
als Hilfsmittel benutzt, um die Verteilung zu beschaffen; die Leistung der Aufgabe ist aber
jedes Mal die Verteilung und ihre Kenngrößen. Keine Aufgabe fragt nach einer Pfadwahrscheinlichkeit
als Ergebnis, keine nach „mindestens eins“ über das Gegenereignis, keine Mindestanzahl-Aufgabe,
keine Umkehraufgabe nach der Urnenzusammensetzung.

**Gegen `10-stoch-bedingte-wsk`** (Vierfeldertafel, Unabhängigkeit): Keine Vierfeldertafel,
keine bedingte Wahrscheinlichkeit, kein Produktkriterium. Das Wort „unabhängig“ fällt nur
beschreibend in #25 („die beiden Würfe beeinflussen sich nicht“).

**Gegen `12-stoch-binomialverteilung` und `12-stoch-sigma-regeln`**: keine Bernoulli-Formel,
kein Binomialkoeffizient, keine σ-Regeln, keine σ-Umgebungen.

## Aufbau je Stufe

| id | Level | Kriterium |
|---|---|---|
| 1 | 1 | Wertebereich einer Zufallsgröße ablesen (zwei Münzen, MC) |
| 2 | 1 | Summe aller Wahrscheinlichkeiten = 1 als Entscheidungskriterium (MC) |
| 3 | 1 | Verteilung als Tabelle lesen: \(P(X \ge 4)\) aus drei Einzelwerten |
| 4 | 1 | Σ-Schreibweise deuten: \(\sum P(X=x_i) = 1\) |
| 5 | 1 | Σ-Schreibweise rechnen: Laufindex von 1 bis 4 über die Werte |
| 6 | 1 | Begriff: Zufallsgröße ordnet jedem Ergebnis eine **Zahl** zu (MC) |
| 7 | 2 | E(X) aus vierwertiger Verteilung (Punktzahl), 1,9 |
| 8 | 2 | fehlende Einzelwahrscheinlichkeit über die Summe 1 (0,4) |
| 9 | 2 | E(X) aus Prozentangaben, die erst zu Wahrscheinlichkeiten werden (0,9) |
| 10 | 2 | E(X) mit Brüchen **ohne Hilfsmittel**, Symmetrie als Abkürzung (4) |
| 11 | 2 | E(X) deuten: Durchschnitt auf lange Sicht, nicht Einzeltag/Obergrenze/Modus (MC) |
| 12 | 2 | E(X) mit negativem Wert; Wert mal Wahrscheinlichkeit zählt, nicht die Wahrscheinlichkeit allein (0,2) |
| 13 | 3 | Verteilung aus einem Zufallsversuch **selbst aufstellen** (zwei Münzen), dann E(X) = 1 |
| 14 | 3 | Verteilung aus einer Urnenziehung ohne Zurücklegen aufstellen, dann E(X) = 1,2 |
| 15 | 3 | σ über \(V(X)=\sum (x_i-\mu)^2 P(X=x_i)\) aus gegebener Verteilung (0,7) |
| 16 | 3 | V(X) aus gegebener Verteilung mit weit auseinanderliegenden Werten (6,96) |
| 17 | 3 | Verteilung aus den Feldern eines Glücksrads, dann E(X) = 1,875 |
| 18 | 3 | Verteilung eines Zweipunkt-Versuchs aufstellen, dann σ = √5/6 ≈ 0,37 |
| 19 | 4 | Modell aus Sachtext: Zufallsgröße „Rechnungsbetrag“ erst festlegen (28,50 €) |
| 20 | 4 | Modell aus Sachtext: Wartezeit als Zufallsgröße (5 min) |
| 21 | 4 | Umkehraufgabe: Auszahlung so wählen, dass die erwartete Einnahme stimmt (g = 10) |
| 22 | 4 | Verfahren wählen: Festpreis gegen Zufallsgröße — vergleichbar erst über E(X); hier gleich (MC) |
| 23 | 4 | Umkehraufgabe andere Richtung: Wahrscheinlichkeit aus vorgegebenem E(X) (0,4) |
| 24 | 4 | Modell aus Sachtext mit unvollständiger Verteilung; Sachprobe entlarvt den Fehlweg (1,8) |
| 25 | 5 | zwei Verfahren: Verteilung aus zwei Würfen aufstellen **und** σ berechnen und deuten (0,53) |
| 26 | 5 | **Fehlersuche**: arithmetisches statt gewichtetes Mittel; falsch 5, richtig 2,2 (MC) |
| 27 | 5 | Parameter aus zwei Bedingungen: Verhältnis der Wahrscheinlichkeiten **und** E(X) = 2,2 (0,4) |
| 28 | 5 | Verteilung über 36 Augenpaare abzählen, dann E(X) = 70/36 ≈ 1,94 |
| 29 | 5 | **Fehlersuche**: σ als gewichtete Summe der Werte gerechnet (= μ); richtig √3 ≈ 1,73 |
| 30 | 5 | Parameter aus zwei Bedingungen: unbekannter **Wert** a aus Summenprobe und E(X) (a = 10) |
| 31 | 6 | **Behauptung prüfen**: E(X) ist stets ein möglicher Wert? Gegenbeispiel 3,5 (MC) |
| 32 | 6 | **faires Spiel begründen**: Nettogewinn-Verteilung aufstellen, E(X) = 0,25 € ⇒ nicht fair |
| 33 | 6 | **Grenzfall**: größtmögliches P(X = 4) bei gegebenem E(X) = 1; Schranke aus \(b \ge 0\) (0,25) |
| 34 | 6 | **Behauptung prüfen**: Gleichverteilung ⇒ E(X) = arithmetisches Mittel? richtig, Σ-Beweis (MC) |
| 35 | 6 | **Fallunterscheidung/Vergleich**: zwei Lotterien mit gleichem E(X), σ(A) = √99 ≈ 9,95 gegen σ(B) = 1 |
| 36 | 6 | **Behauptung prüfen**: faires Spiel ⇒ Gewinn in der Hälfte der Spiele? Gegenbeispiel 1/100 (MC) |

MC-Anteil: 9 von 36 (L1: 3, L2: 1, L4: 1, L5: 1, L6: 3). Die Obergrenze von 3 MC in Stufe 5
und 6 ist eingehalten. Keine Aufgabenform kommt in einer Stufe dreimal vor.

## Qualitätssicherung

- **Jede Zahl mit dem Wolfram-MCP nachgerechnet**, Verteilungen einzeln auf Summe 1 geprüft und
  jede Standardabweichung gegen die Definition (nicht gegen eine Formel) kontrolliert.
  Nebenrechnung mitgeprüft, wo sie im Lösungsweg steht (etwa die 36 Augenpaare in #28:
  6 + 10 + 8 + 6 + 4 + 2 = 36).
- **Beide Fehlersuchaufgaben führen über den falschen Weg zu einem falschen Ergebnis.**
  #26: arithmetisches Mittel 5 gegen den richtigen Wert 2,2 — die Zahlen sind gerade so gewählt,
  dass die Gewichte stark ungleich sind (0,8 auf dem kleinsten Wert) und beides weit auseinander
  liegt. #29: Der vorgeführte Ausdruck liefert 1 und trifft damit den **Erwartungswert**, nicht
  die gesuchte Standardabweichung (√3 ≈ 1,73); der Lösungsweg benennt ausdrücklich, dass das
  Ergebnis rechnerisch richtig, aber falsch benannt ist — sonst könnte der Zufallstreffer als
  Bestätigung der falschen Regel gelesen werden.
- **Plausibilisierung, nicht nur Nachrechnen**: In #18 ist σ größer als μ, in #35 ist σ(A)
  zehnmal so groß wie σ(B) — beides im Lösungsweg begründet, damit die Größenordnung nicht als
  Rechenfehler erscheint. In #33 wurde geprüft, dass der Grenzfall im zulässigen Bereich liegt
  (a = 0,75, b = 0, c = 0,25 ist eine gültige Verteilung).
- Tipps nennen ausschließlich den Weg; kein Tipp enthält Lösungswert, Zwischenlösung oder eine
  fertige Gleichung.
- Alle vier MC-Optionen je Aufgabe von ähnlicher Länge; die richtige ist nirgends die längste.
  Keine Option wird über Buchstabe oder Position angesprochen.
- Deutsche Anführung durchgehend `„…“`; echte Umlaute; `<b>…</b>` statt `**`; Mathe-Markup nur
  innerhalb `\(…\)` / `$$…$$`; kein `<` direkt vor einem Buchstaben.
- Datei mit **Write** angelegt (kein Bash-Heredoc), keine Hilfsdateien in `trainer/`.

## Gates und Tests

```
python tests/level_check.py --strict trainer/10-stoch-erwartungswert.html   # Exit 0, ok
python tests/lehrplan_check.py --strict trainer/10-stoch-erwartungswert.html # 0 Befunde
python tests/katex_check.py trainer/10-stoch-erwartungswert.html             # ok
python -m pytest tests/test_trainer.py -k "erwartungswert" -q               # 7 passed
python -m pytest tests/test_index.py -q --override-ini addopts=""            # 3 passed
python tests/level_check.py --strict                                         # alle 91 Trainer:
                                                     # Exit 0, 0 Fehler, 0 Warnungen
```

Der Lauf über den gesamten Bestand ist der eigentliche Dubletten-Test: Er meldet keine Aufgabe
dieses Trainers als wortgleich mit einer Aufgabe eines anderen. Der Bestand steht damit weiter
auf null Warnungen.

## Sichtprüfung (bindend, `schule/CLAUDE.md`)

Neun PNG mit `tests/bild.py --aufgabe <id>` erzeugt und mit dem Read-Tool **angesehen**,
mindestens eines je Stufe, sieben davon mit `--loesungsweg`:
#4 (L1, Σ-Schreibweise), #10 (L2, Brüche), #14 und #18 (L3, Verteilung und σ mit Brüchen),
#22 (L4, MC mit gemischten Optionen), #25, #26 und #28 (L5, lange Lösungswege mit
Verteilungstabellen), #31 (L6, MC ohne Lösungsweg), #33 (L6, Fallunterscheidung).
Dazu `tests/bild.py index.html` — die neue Zeile steht als dritter und letzter Eintrag im
Abschnitt „C · Stochastik“ der Spalte Klasse 10, Connector `└`, Badge „Neu“.
Kein Layoutfehler: keine abgeschnittenen Zeilen, keine wörtlich gerenderten Markup-Reste,
alle Brüche und das Summenzeichen gesetzt.

## Offen geblieben

- **Stufe 1 enthält drei MC.** Das ist erlaubt (die Grenze von 3 gilt für Stufe 5/6) und hier
  sachlich begründet — Wertebereich, Verteilungsbegriff und Zufallsgrößenbegriff sind
  Entscheidungsfragen, keine Rechnungen. Wer später umbaut, sollte #1 oder #2 durch ein
  numerisches Format ersetzen.
- **Kein Bild, kein Diagramm.** Die Trainer-Engine zeigt keine Grafiken; Verteilungen stehen
  deshalb als Aufzählung im Text, nicht als Tabelle oder Stabdiagramm. Das Ablesen aus einem
  Stabdiagramm, das TH 2.3.4 nahelegt, ist so nicht übbar.
- **Die Verteilungen bleiben klein** (höchstens sechs Werte, #28 ausgenommen). Längere
  Verteilungen wären ohne Tabellendarstellung im Fließtext schlecht lesbar.
- Der Trainer setzt das Baumdiagramm in #14 und #25 als bekannt voraus; im Kl.-10-Pfad steht
  `10-stoch-mehrstufig` davor, die Reihenfolge in der Index-Spalte passt dazu.
