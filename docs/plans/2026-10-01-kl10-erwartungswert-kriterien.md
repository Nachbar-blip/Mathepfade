# Neuer Trainer Kl. 10: Zufallsgrößen und Erwartungswert (TH 2.3.4)

Angelegt 2026-10-01, nach der Prüfung durch einen zweiten Agenten am selben Tag überarbeitet
(Befunde und ihre Behebung sind unten jeweils an Ort und Stelle vermerkt; elf Aufgaben geändert:
#9, #12, #14, #17, #19, #20, #24, #25, #29, #33, #36). Lokale Nachvollziehbarkeit; im Public-HTML stehen die Kriterien bewusst nicht.
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
Transformation, **kein** Additionssatz der Varianz. Diese **Werkzeug**-Abgrenzung ist per
Volltextsuche bestätigt und ist die eigentliche Trennlinie zwischen den beiden Trainern.

Alle 36 Aufgaben wurden gegen die 36 Aufgaben dort gelesen. Vermieden sind alle Aufgaben, die
dort ihren eigenen Kern haben: E(X) und V(X) des fairen Würfels (dort #7, #14, #15), die bare
Drei-Werte-Verteilung mit gesuchtem E(X) (dort #8, #11), die symmetrische Verteilung um null
(dort #9), das Glücksrad mit einer Auszahlung (dort #10), „Einsatz aus der Fairness-Bedingung“
(dort #21), „Verteilung aus Summennormierung und E(X)“ mit drei Werten (dort #25), die
Behauptungen „gleicher Erwartungswert ⇒ gleiche Streuung“ (dort #32) und „faires Spiel ⇒ σ = 0“
(dort #35). Das faire Spiel kommt hier genau einmal vor (#32), und dann als **Nachweis durch
Rechnung** mit anschließender Beurteilung. Der Risikovergleich zweier Angebote bei gleichem
Erwartungswert steht hier als **Rechenaufgabe** (#35: beide σ selbst bestimmen), dort als
MC-Behauptung bzw. mit gegebenen σ-Werten.

**Vier Aufgabenformen sind trotzdem dieselben wie in Kl. 12** (Review-Befund 2026-10-01; der
erste Entwurf dieses Papiers behauptete pauschal, keine Aufgabe wiederhole eine dortige „auch
nicht mit anderen Zahlen" — das war zu weit gegriffen, das Gate prüft nur Wortgleichheit):

| hier | dort | gemeinsame Form | Unterschied |
|---|---|---|---|
| #26 | Kl12 #26 | Fehlersuche „arithmetisches statt gewichtetes Mittel“ | hier MC (Fehler benennen), dort numerisch (Wert korrigieren); andere Zahlen und Gewichte |
| #30 | Kl12 #30 | unbekannter **Wert** a aus E(X) und der Verteilung | hier drei Werte mit negativem Anteil, dort zwei Werte |
| #21 | Kl12 #28 | Anbieter will je Spiel einen festen Betrag verdienen | hier nach der **Auszahlung** aufgelöst, dort nach dem **Einsatz** |
| #15, #16 | Kl12 #13, #16, #18 | V bzw. σ aus barer Verteilung | nur andere Zahlen; identische Form |

Das ist **bewusst so belassen**: Diese Formen sind der Kern dessen, was TH 2.3.4 für Klasse 10
verlangt, und sie fehlen dort nicht, weil Klasse 12 sie ebenfalls braucht. Der Trainer
unterscheidet sich vom Kl.-12-Trainer im Werkzeug und im Anforderungsniveau, nicht darin, dass
jede einzelne Aufgabenform exklusiv wäre.

**Gegen `10-stoch-mehrstufig`** (Pfadregeln, Baumdiagramm): Das Baumdiagramm wird in #14 und #25
als Hilfsmittel benutzt, um die Verteilung zu beschaffen; die Leistung der Aufgabe ist aber
jedes Mal die Verteilung und ihre Kenngrößen. Keine Aufgabe fragt nach einer Pfadwahrscheinlichkeit
als Ergebnis, keine nach „mindestens eins“ über das Gegenereignis, keine Mindestanzahl-Aufgabe,
keine Umkehraufgabe nach der Urnenzusammensetzung.
Der erste Entwurf hatte dort außerdem zwei **Szenarien** wiederverwendet (Review-Befund):
#14 benutzte dieselbe Urne wie dort #14 (3 rot / 2 blau, zweimal ohne Zurücklegen) und rechnete
im Lösungsweg genau dessen Ergebnis 0,6 mit aus; #25 benutzte den Zwei-Würfel-Aufbau von dort
#5/#15. Keine Dublette, aber ein Re-Skin — beide Kontexte sind ersetzt (Kärtchen im Beutel
5 × „1“ und 3 × „4“; Zweifragen-Test mit je fünf Antworten).

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
| 9 | 2 | **erwartete Anzahl** bei 60 Drehungen aus E(X) einer Einzeldrehung (15) |
| 10 | 2 | E(X) mit Brüchen **ohne Hilfsmittel**, Symmetrie als Abkürzung (4) |
| 11 | 2 | E(X) deuten: Durchschnitt auf lange Sicht, nicht Einzeltag/Obergrenze/Modus (MC) |
| 12 | 2 | fehlende Einzelwahrscheinlichkeit mit Bruchangaben, gemeinsamer Nenner (1/3) |
| 13 | 3 | Verteilung aus einem Zufallsversuch **selbst aufstellen** (zwei Münzen), dann E(X) = 1 |
| 14 | 3 | Verteilung aus einer Ziehung ohne Zurücklegen aufstellen (Kärtchen), dann E(X) = 0,75 |
| 15 | 3 | σ über \(V(X)=\sum (x_i-\mu)^2 P(X=x_i)\) aus gegebener Verteilung (0,7) |
| 16 | 3 | V(X) aus gegebener Verteilung mit weit auseinanderliegenden Werten (6,96) |
| 17 | 3 | Verteilung aus den Feldern eines Glücksrads aufstellen, dann σ ≈ 1,27 |
| 18 | 3 | Verteilung eines Zweipunkt-Versuchs aufstellen, dann σ = √5/6 ≈ 0,37 |
| 19 | 4 | Modell aus Sachtext: Zufallsgröße „Rechnungsbetrag“ erst festlegen, dann auf 40 Reparaturen hochrechnen (1140 €) |
| 20 | 4 | Modell aus Sachtext: Zufallsgröße **Fahrtdauer** aus dem Stockwerk erst bilden, Werte stehen nicht im Text (18 s) |
| 21 | 4 | Umkehraufgabe: Auszahlung so wählen, dass die erwartete Einnahme stimmt (g = 10) |
| 22 | 4 | Verfahren wählen: Festpreis gegen Zufallsgröße — vergleichbar erst über E(X); hier gleich (MC) |
| 23 | 4 | Umkehraufgabe andere Richtung: Wahrscheinlichkeit aus vorgegebenem E(X) (0,4) |
| 24 | 4 | Sachtext mit unvollständiger Verteilung: fehlende Wahrscheinlichkeit beschaffen, dann σ = 0,6 |
| 25 | 5 | zwei Verfahren: Verteilung aus zwei Testfragen aufstellen **und** σ berechnen und deuten (0,57) |
| 26 | 5 | **Fehlersuche**: arithmetisches statt gewichtetes Mittel; falsch 5, richtig 2,2 (MC) |
| 27 | 5 | Parameter aus zwei Bedingungen: Verhältnis der Wahrscheinlichkeiten **und** E(X) = 2,2 (0,4) |
| 28 | 5 | Verteilung über alle Augenpaare abzählen, dann E(X) = 70/36 ≈ 1,94 |
| 29 | 5 | **Fehlersuche**: Quadrieren der Abweichungen vergessen; falscher Weg gibt 0, richtig √3 ≈ 1,73 |
| 30 | 5 | Parameter aus zwei Bedingungen: unbekannter **Wert** a aus Summenprobe und E(X) (a = 10) |
| 31 | 6 | **Behauptung prüfen**: E(X) ist stets ein möglicher Wert? Gegenbeispiel 3,5 (MC) |
| 32 | 6 | **faires Spiel begründen**: Nettogewinn-Verteilung aufstellen, E(X) = 0,25 € ⇒ nicht fair |
| 33 | 6 | **Grenzfall**: größtmögliches P(X = 4) bei gegebenem E(X) = 1; Schranke aus \(b \ge 0\) (0,25) |
| 34 | 6 | **Behauptung prüfen**: Gleichverteilung ⇒ E(X) = arithmetisches Mittel? richtig, Σ-Beweis (MC) |
| 35 | 6 | **Vergleich mit Begründung**: zwei Lotterien mit gleichem E(X), σ(A) = √99 ≈ 9,95 gegen σ(B) = 1 |
| 36 | 6 | **Behauptung prüfen, numerisch**: faires Spiel ⇒ Gewinn in der Hälfte? p aus E(X) = 0 ⇒ 1 von 100 |

MC-Anteil: 7 von 36 (L1: 3, L2: 1, L4: 1, L5: 1, L6: 2). Die Obergrenze von 3 MC in Stufe 5
und 6 ist eingehalten.

### Formverteilung je Stufe (höchstens zwei Aufgaben derselben Form)

Der erste Entwurf verletzte diese Regel in vier Stufen; Variation des Zahlentyps (Dezimal /
Prozent / Bruch / negativ) ist keine Formvariation. Jetzt:

| Stufe | Formen |
|---|---|
| 1 | Wertebereich/Begriff (#1, #6) · Verteilung prüfen bzw. lesen (#2, #3) · Σ-Schreibweise (#4, #5) |
| 2 | gewichtete Summe (#7, #10) · fehlende Wahrscheinlichkeit (#8, #12) · Deutung / erwartete Anzahl (#9, #11) |
| 3 | Verteilung aufstellen → E(X) (#13, #14) · Kenngröße aus gegebener Verteilung (#15, #16) · Verteilung aufstellen → σ (#17, #18) |
| 4 | Modell aus Sachtext → E(X) (#19, #20) · Umkehraufgabe (#21, #23) · Verfahren wählen (#22) · Sachtext → σ mit fehlender Wahrscheinlichkeit (#24) |
| 5 | Verteilung aufstellen → σ deuten (#25, #28) · Fehlersuche (#26, #29) · Parameter aus zwei Bedingungen (#27, #30) |
| 6 | Behauptung per MC beurteilen (#31, #34) · Behauptung numerisch widerlegen (#36) · Rechnung mit anschließender Beurteilung (#32, #35) · Grenzfall (#33) |

## Qualitätssicherung

- **Jede Zahl mit dem Wolfram-MCP nachgerechnet**, Verteilungen einzeln auf Summe 1 geprüft und
  jede Standardabweichung gegen die Definition (nicht gegen eine Formel) kontrolliert.
  Nebenrechnung mitgeprüft, wo sie im Lösungsweg steht (etwa die 36 Augenpaare in #28:
  6 + 10 + 8 + 6 + 4 + 2 = 36).
- **Beide Fehlersuchaufgaben führen über den falschen Weg zu einem falschen Ergebnis.**
  #26: arithmetisches Mittel 5 gegen den richtigen Wert 2,2 — die Zahlen sind gerade so gewählt,
  dass die Gewichte stark ungleich sind (0,8 auf dem kleinsten Wert) und beides weit auseinander
  liegt. #29: Der vorgeführte Weg lässt das **Quadrieren** der Abweichungen weg und liefert 0
  gegen die richtige Standardabweichung √3 ≈ 1,73.
  Der erste Entwurf von #29 zeigte stattdessen einen Weg, der Σ xᵢ·P(X=xᵢ) rechnete und mit 1
  **zufällig eine richtig gerechnete Zahl** traf — nämlich μ, nur falsch benannt. Das war zwar
  nicht irreführend (die Toleranz 0,03 schließt die 1 aus, und der Lösungsweg benannte es), aber
  ein vermeidbares Risiko, das sich durch keine Zahlenwahl auflösen ließ, weil der Ausdruck
  definitionsgemäß μ **ist**. Der neue Fehlweg gibt nicht nur eine falsche Zahl, er zeigt
  zugleich, wozu das Quadrieren da ist: Σ (xᵢ − μ)·P = μ − μ = 0 für jede Verteilung.
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

## Review-Nachtrag 2026-10-01

Der Prüf-Agent hat alle 36 Aufgaben nachgerechnet und keinen Zahlenfehler gefunden (alle
Verteilungen summieren sich auf 1, alle Kenngrößen stimmen, keine unmögliche Zahl). Behoben
wurden:

- **#33: Aufgabentext widersprach der eigenen Lösung.** Der Text sagte, X nehme „ausschließlich
  die Werte 0, 1 und 4 an“, der Grenzfall wird aber gerade mit P(X = 1) = 0 erreicht. Unter der
  wörtlichen Prämisse wäre 0,25 ein Supremum, kein größtmöglicher Wert. Jetzt: „keine anderen
  Werte als“. Die Zahl bleibt.
- **Formhäufung in vier Stufen** (siehe Tabelle „Formverteilung je Stufe“): Stufe 2 hatte
  viermal „gewichtete Summe“ (#9 und #12 ersetzt), Stufe 3 dreimal „Verteilung → E(X)“
  (#17 auf σ umgestellt), Stufe 4 dreimal „E(X) aus Sachtext“ (#24 auf σ umgestellt),
  Stufe 6 dreimal „Behauptung per MC“ (#36 numerisch).
- **#20 war auf Stufe 4 kein AFB II**: Werte und Wahrscheinlichkeiten standen fertig im Satz,
  zu leisten war genau das, was #9 auf Stufe 2 verlangte. Ersetzt durch die Aufzugsaufgabe, in
  der die Zufallsgröße (Fahrtdauer) erst aus dem Stockwerk gebildet werden muss und keiner ihrer
  Werte im Text steht. **#19** hatte dieselbe Diagnose in schwächerer Form und verlangt jetzt
  zusätzlich die Hochrechnung auf 40 Reparaturen.
- **#29 Fehlweg ausgetauscht** (Begründung oben unter Qualitätssicherung).
- **Szenario-Re-Skins** aus `10-stoch-mehrstufig` in #14 und #25 ersetzt (siehe Abgrenzung).
- **Abgrenzungs-Aussage richtiggestellt** — die Behauptung, keine Aufgabe wiederhole eine
  Kl.-12-Form, war zu weit gegriffen; die vier tatsächlichen Formgleichheiten stehen jetzt
  in einer eigenen Tabelle.
- Kleinigkeiten: Tipp von #28 nennt nicht mehr die Zahl 36 (grenzte an ein Zwischenergebnis);
  Lösungsweg von #18 begründet σ > μ jetzt mit den ungleichen Gewichten statt mit der
  Spannweite; die Bemerkung „daher der Faktor 2“ in #25 bezieht sich jetzt auf den tatsächlich
  gezeigten Weg über das Gegenereignis; der Verweis auf „Punktzahlen und Fehlerzahlen anderer
  Aufgaben“ ist mit #20 entfallen.

Ausdrücklich **nicht** geändert (vom Prüfer als unproblematisch eingestuft): die drei MC auf
Stufe 1 und die MC-Optionslängen (Abstand 1–6 Zeichen, im Bild kein erkennbares Muster).

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

Insgesamt 19 PNG mit `tests/bild.py --aufgabe <id>` erzeugt und mit dem Read-Tool **angesehen**,
mindestens eines je Stufe, die meisten mit `--loesungsweg`. Erste Runde: #4 (L1, Σ-Schreibweise),
#10 (L2, Brüche), #14 und #18 (L3), #22 (L4, MC mit gemischten Optionen), #25, #26 und #28 (L5),
#31 (L6, MC ohne Lösungsweg), #33 (L6, Grenzfall). Nach dem Review alle elf geänderten Aufgaben
erneut: #9, #12, #14, #17, #19, #20, #24, #25, #29, #33, #36.
Dazu `tests/bild.py index.html` — die neue Zeile steht als dritter und letzter Eintrag im
Abschnitt „C · Stochastik“ der Spalte Klasse 10, Connector `└`, Badge „Neu“.
Kein Layoutfehler: keine abgeschnittenen Zeilen, keine wörtlich gerenderten Markup-Reste,
alle Brüche und das Summenzeichen gesetzt.

## Offen geblieben

- **Stufe 1 enthält drei MC.** Das ist erlaubt (die Grenze von 3 gilt für Stufe 5/6) und hier
  sachlich begründet — Wertebereich, Verteilungsbegriff und Zufallsgrößenbegriff sind
  Entscheidungsfragen, keine Rechnungen. Ein Umbau von #1 oder #2 auf ein numerisches Format
  ginge nur um den Preis einer Dublette zu #8 — kein Handlungsbedarf (Review 2026-10-01).
- **Kein Bild, kein Diagramm — und das ist keine Lehrplanlücke.** Die Trainer-Engine zeigt keine
  Grafiken; Verteilungen stehen als Aufzählung im Text. TH 2.3.4 verlangt Verteilungen
  „bestimmen“, nicht „aus einer Grafik ablesen“; das ist über #13, #14, #17, #25 und #28
  abgedeckt. Wer den Effekt eines Stabdiagramms dennoch will, kann die Säulenhöhen im Text
  angeben — dafür braucht es keine Grafik.
- **Die Verteilungen bleiben klein** (höchstens sechs Werte, #28 ausgenommen). Längere
  Verteilungen wären ohne Tabellendarstellung im Fließtext schlecht lesbar.
- Der Trainer setzt das Baumdiagramm in #14 und #25 als bekannt voraus; im Kl.-10-Pfad steht
  `10-stoch-mehrstufig` davor, die Reihenfolge in der Index-Spalte passt dazu.
