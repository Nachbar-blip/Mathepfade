# Klasse 10, Block A (Analysis) — Überarbeitung je Trainer (Stand 2026-09-30)

Lokale Nachvollziehbarkeit; im Public-HTML stehen die Kriterien bewusst nicht.
Grundlage: Rubrik aus `docs/plans/2026-09-26-lehrplan-th-und-level-progression-plan.md`
(Lesart Kl. 10: L4 = Verfahren selbst wählen, Modell aus Text, Umkehraufgabe (Parameter,
Faktor, Exponent gesucht); L5 = zwei Verfahren kombinieren, Parameter aus zwei Bedingungen,
Fehler in vorgelegter Rechnung; L6 = Behauptung begründet prüfen, Fallunterscheidung nach
Parameter/Grad/Basis, Umkehraufgabe mit zwei Bedingungen), Befunde aus
`docs/audit/audit-2026-09-19-mathepfade.md` (Zeilen 94–107).
Niveau: TH-Lehrplan 2.3.2 (Potenz-, Exponential- und Logarithmusfunktionen, Transformationen,
ganzrationale Funktionen, Grenzwert- und Asymptotenbegriff anschaulich; **keine** Polynomdivision,
**kein** Integral).
Jede Lösung mit Wolfram nachgerechnet; Bilder L5/L6 per `tests/bild.py` angesehen.

Block A umfasst sieben Trainer. Abgrenzung gegen Dubletten im Pool:
10-exponentialfunktionen = Wachstums-/Zerfallsmodelle, Faktor und Anfangswert;
10-logarithmus = Logarithmengesetze, Basiswechsel, Stellenzahl, Definitionsbereich;
10-ganzrationale-funktionen = Nullstellen über Ausklammern und Nullprodukt, Vielfachheit,
Randverhalten; 10-graphen-transformationen = Verschiebung/Streckung/Spiegelung, Scheitelform;
10-potenzfunktionen = \(x^n\) mit ganzzahligem Exponenten, Symmetrie, Monotonie;
10-substitution = biquadratische und substituierbare Gleichungen;
10-polynomdivision (Dateiname historisch) = Grenzwerte und Asymptoten.

| Trainer | Audit-Befund | Geändert |
|---|---|---|
| 10-exponentialfunktionen | KEIN_AFB3 L5; KOLLAPS L1/L2; Warnungen #22 (Tipp mit Lösungswert), #26/#33 (MC-Länge) | L4–L6 neu: Verdopplung bis 6400, Zinseszins über drei Jahre, Modellterm bei 15 % Abnahme (MC), Halbwertszeit 8 Tage, Jahresfaktor aus zwei Zählungen, Abbaufaktor aus \(q^2 = 0{,}49\); \(c\) aus \(f(1)\) und \(f(3)\), Fehler „zweimal 10 % = 20 %" (MC), Kultur A gegen Kultur B als Zweierpotenzen, zwei Zinsphasen hintereinander, Zerfall über fünf Stunden, Wald unter 4000 Bäume; Behauptung „10 Jahre 5 % < einmalig 50 %" (MC), Anzahl Basen mit \(a^x \to 0\) (Fallunterscheidung), \(c\) aus \(f(2)\) und \(f(5)\), Behauptung „Bestand wird null" (MC), Angebotsvergleich A/B über vier Jahre, Behauptung „Verdopplung in 10 Jahren ⇒ Versechsfachung in 30". L1–L3 unverändert (KOLLAPS L1/L2 laut Plan offen) |
| 10-ganzrationale-funktionen | KEIN_AFB3 L6; DUENNER_WEG (Stufen 2); Lehrplan-Gate: #27 nannte „Polynomdivision"; Warnung #28 (MC-Länge) | L5/L6 neu: \(a\) aus drei Nullstellen, Fehler „durch \(x\) teilen" mit Verlust von \(x = 0\) (MC), \(f(0)\) aus doppelter und einfacher Nullstelle (ersetzt die Polynomdivisions-Aufgabe #27), \(c\) mit \(x^4 + c\) ohne reelle Nullstelle (MC), Produkt der Nullstellen nach Ausklammern, \(a\) aus \(f(0) = -6\); Behauptung „ungerader Grad ⇒ Nullstelle" (MC), Anzahl achsensymmetrischer Graphen, \(c\) aus drei Nullstellen, höchstens drei Nullstellen bei \(x^4 + bx^2\) (Fallunterscheidung), Behauptung „gerader Grad ⇒ gerade Anzahl Nullstellen" (MC, Gegenbeispiel \(x^4\)), Leitkoeffizient aus Nullstellen und Punkt |
| 10-graphen-transformationen | KEIN_AFB3 L5; KEIN_AFB3 L6; Warnungen #21 (Tipp mit Lösungswert), #31/#34 (MC-Länge) | L5/L6 neu: \(a\) aus Berührung der \(x\)-Achse und Punkt, Fehler „\(f(x-3)\) verschiebt nach links" (MC), Spiegelung und Verschiebung nacheinander, Scheitel-\(y\) aus zwei Nullstellen, größere Nullstelle von \(3(x+2)^2-27\), Scheitelstelle von \(2x^2+8x+5\); Behauptung „Stauchung in \(x\) = Streckung in \(y\)" (MC, gilt nur für \(x^2\)), kleinstes ganzes \(e\) mit zwei Nullstellen (Fallunterscheidung), \(a\) aus Scheitel und Punkt, Behauptung „Reihenfolge egal" (MC), Nullstelle nach drei Transformationen, Anzahl Funktionen mit zwei Nullstellen. #21 (L4) mit Tipp ohne Lösungswert neu formuliert |
| 10-logarithmus | KEIN_AFB3 L5; KEIN_AFB3 L6; Warnungen #26 (Tipp mit Lösungswert), #29/#34 (MC-Länge) | L5/L6 neu: Fehler „\(\lg(8+2) = \lg 8 + \lg 2\)" (MC), \(\log_2(\sqrt8 \cdot 4)\), Basis \(a\) aus \(f(81) = 4\), \(3 \cdot 2^{x+1} = 96\), \(\log_5(x^3) - 3\log_5 x\) (Wert unabhängig von \(x\)), \(\log_4 32\) über gemeinsame Basis; Behauptung „\(\lg(ab) = \lg a \cdot \lg b\)" (MC, Gegenbeispiel), Anzahl negativer Logarithmuswerte (Fallunterscheidung am Numerus), \(f(32)\) aus \(f(8) = 12\), Wachstumsvergleich mit Potenzfunktionen (MC), kleinste ganze Zahl im Definitionsbereich, Stellenzahl von \(2^{30}\). Die Faustformel-Aufgabe (Verdopplungszeit \(70/p\)) entfällt — sie gehörte thematisch zu 10-exponentialfunktionen und lieferte den Weg im Text mit |

| 10-potenzfunktionen | KEIN_AFB3 L5; KEIN_AFB3 L6; Warnungen #32/#36 (MC-Länge) | L5/L6 neu: \(n\) aus zwei Punkten, Fehler „\(x^4 = 16 \Rightarrow x = 2\)" (MC), \(x\) aus \(3x^{-2} = 12\), \(x\) aus \(x^{2/3} = 16\), Symmetrie und Monotonie von \(x^{-3}\) (MC), \(f(-1)\) nach Punktprobe; Behauptung „\(x^3 > x^2\) für alle \(x > 0\)" (MC), Anzahl punktsymmetrischer Graphen, \(n\) aus \(f(1)\) und \(f(2)\), Behauptung „größerer Exponent, größerer Wert" (MC), Anzahl gemeinsamer Punkte von \(x^2\) und \(x^4\), \(n\) aus einem Punkt mit Wert unter \(1\) |
| 10-substitution | Audit „ok", aber vier sinngleiche Aufgabenpaare (#21/#22, #26/#27, #31/#32, #35/#36) und Substitution im Aufgabentext ab L4 | L5/L6 neu, dazu L4 #19 und #22: Anzahl Lösungen bei geschachteltem Klammerterm, größere Lösung bei \(3^{2x}\), Anzahl Lösungen der biquadratischen Gleichung, Fehler „Rücksubstitution vergessen" (MC), Parameter \(c\) aus gegebener Lösung, Anzahl Lösungen von \(\sin^2 x - 3\sin x + 2 = 0\) (Wertebereich); Behauptung „vier reelle Lösungen" (MC), Summe der Lösungen bei \(u = x^3\), größtes ganzes \(c\) mit genau zwei Lösungen (Fallunterscheidung), Behauptung „jedes \(u\) liefert zwei \(x\)" (MC), positive Lösung mit ausgeschlossenem \(u\), \(p\) aus vier gegebenen Lösungen. Die Substitution wird ab L4 nicht mehr im Text vorgegeben |
| 10-polynomdivision (Dateiname historisch) | Ersatz-Trainer: 6 Lehrplan-Gate-Treffer („Polynomdivision" ist in TH Kl. 10 nicht vorgesehen) | **Alle 36 Aufgaben neu: Thema Grenzwerte und Asymptoten** (TH 2.3.2). `<title>`, `THEMA_CONFIG.name = 'Grenzwerte und Asymptoten'`, Index-Zeilentext „Grenzwerte &amp; Asymptoten" und Kommentar in Zeile 2 der Datei geändert. Aufbau nach Plan: L1 Randverhalten von \(x^2\), \(x^3\), \(1/x\) und Wertetabellen; L2 Glied höchsten Grades, senkrechte Asymptote aus der Nennernullstelle; L3 waagerechte Asymptote von \((ax+b)/(cx+d)\) und verschobene Exponentialfunktionen; L4 Funktionstyp aus Tabelle/Modell erschließen, Grenzwert ohne Verfahrensansage; L5 Parameter aus zwei Bedingungen, Fehler in Grenzwert-Argumentation; L6 Behauptungen prüfen und Fallunterscheidung nach Grad. Vorlage: `../DifferenzierungsEngine/trainer/11-analysis-grenzwerte.html` (GK-Teil, ohne hebbare Lücken) |

### 10-exponentialfunktionen

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | L4: Modell aus Text — Verdopplung, Exponent gesucht |
| 20 | 4 | L4: Verfahren wählen — Zinseszins statt Dreisatz |
| 21 | 4 | L4: Modell aus Text — Zerfallsfaktor erkennen (MC) |
| 22 | 4 | L4: Modell aus Text — Anzahl Halbwertszeiten selbst bestimmen |
| 23 | 4 | L4: Umkehraufgabe — Faktor aus zwei Zählungen |
| 24 | 4 | L4: Umkehraufgabe — Faktor aus \(q^2 = 0{,}49\) |
| 25 | 5 | L5: Parameter aus zwei Bedingungen — \(f(1)\) und \(f(3)\) |
| 26 | 5 | L5: Fehler finden — Prozentsätze addiert statt Faktoren multipliziert (MC) |
| 27 | 5 | L5: zwei Verfahren — gemeinsame Basis und Exponentenvergleich |
| 28 | 5 | L5: zweischrittig — zwei Zinsphasen nacheinander |
| 29 | 5 | L5: zweischrittig — Faktor aus drei Schritten, dann fünfter Schritt |
| 30 | 5 | L5: zweischrittig — Zerfallsfaktor, dann systematisches Probieren |
| 31 | 6 | L6: Behauptung prüfen — Zinseszins gegen einmalige Erhöhung (MC) |
| 32 | 6 | L6: Fallunterscheidung — Basis über oder unter \(1\) |
| 33 | 6 | L6: Parameter aus zwei Bedingungen — \(f(2)\) und \(f(5)\) |
| 34 | 6 | L6: Behauptung prüfen — exponentieller Zerfall erreicht nie null (MC) |
| 35 | 6 | L6: Vergleich zweier Modelle — Startwert gegen Zinssatz |
| 36 | 6 | L6: Behauptung prüfen — Faktoren multiplizieren, nicht addieren (MC) |

### 10-ganzrationale-funktionen

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | L5: Parameter — \(a\) über Produktform aus drei Nullstellen |
| 26 | 5 | L5: Fehler finden — Division durch \(x\) verliert \(x = 0\) (MC) |
| 27 | 5 | L5: zwei Verfahren — Vielfachheit in Produktform, dann \(f(1)\) (Review: Auswertung bei \(x = 0\) verschoben) |
| 28 | 5 | L5: Parameter — Bedingung an \(c\) für keine reelle Nullstelle (MC) |
| 29 | 5 | L5: Parameter aus zwei Nullstellen über Vieta (Review: war reines Faktorisieren) |
| 30 | 5 | L5: Parameter aus Nullstelle und Punkt — zwei Gleichungen (Review: war eine Bedingung bei \(x = 0\)) |
| 31 | 6 | L6: Behauptung prüfen — ungerader Grad und Randverhalten (MC) |
| 32 | 6 | L6: Fallunterscheidung — Symmetrie an vier Funktionen prüfen |
| 33 | 6 | L6: Parameter aus drei Nullstellen — Absolutglied |
| 34 | 6 | L6: Fallunterscheidung nach Vorzeichen von \(b\) |
| 35 | 6 | L6: Behauptung prüfen — Gegenbeispiel \(x^4\) (MC) |
| 36 | 6 | L6: Umkehraufgabe — Leitkoeffizient aus Nullstellen und Punkt |

### 10-graphen-transformationen

| id | Level | Kriterium |
|---|---|---|
| 21 | 4 | L4: Verkettung auswerten; Tipp ohne Lösungswert |
| 25 | 5 | L5: Parameter aus zwei Bedingungen — Berührung und Punkt |
| 26 | 5 | L5: Fehler finden — Richtung der Verschiebung im Argument (MC) |
| 27 | 5 | L5: zwei Transformationen in fester Reihenfolge |
| 28 | 5 | L5: Umkehraufgabe — Scheitel aus zwei Nullstellen |
| 29 | 5 | L5: Umkehraufgabe — Verschiebungswert aus einem Funktionswert, mit Bedingung (Review: war reines Gleichungslösen) |
| 30 | 5 | L5: Parameter aus zwei Bedingungen — Scheitel auf der \(y\)-Achse und Punkt (Review: war L3-Standard) |
| 31 | 6 | L6: Behauptung prüfen — Stauchung in \(x\) gegen Streckung in \(y\) (MC) |
| 32 | 6 | L6: Fallunterscheidung nach Lage des Scheitels |
| 33 | 6 | L6: Parameter aus Scheitel und Punkt |
| 34 | 6 | L6: Behauptung prüfen — Reihenfolge von Streckung und Verschiebung (MC) |
| 35 | 6 | L6: drei Transformationen, dann Nullstelle mit Bedingung |
| 36 | 6 | L6: Fallunterscheidung — Öffnungsrichtung gegen Scheitellage |

### 10-logarithmus

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | L5: Fehler finden — Logarithmengesetz auf Summe angewandt (MC) |
| 26 | 5 | L5: zwei Verfahren — Wurzel als Potenz, dann Produktgesetz |
| 27 | 5 | L5: Umkehraufgabe — Basis aus einem Funktionswert |
| 28 | 5 | L5: zweischrittig — Potenz isolieren, dann Exponenten vergleichen |
| 29 | 5 | L5: Term vereinfachen — Wert unabhängig von \(x\) |
| 30 | 5 | L5: Basiswechsel über gemeinsame Basis \(2\) |
| 31 | 6 | L6: Behauptung prüfen — Produktgesetz mit Gegenbeispiel (MC) |
| 32 | 6 | L6: Fallunterscheidung — Numerus über/unter \(1\) |
| 33 | 6 | L6: Parameter aus einer Bedingung, dann zweite Stelle |
| 34 | 6 | L6: Behauptung prüfen — Wachstum gegen Potenzfunktion (MC) |
| 35 | 6 | L6: Definitionsbereich — kleinste ganze Zahl |
| 36 | 6 | L6: Größenordnung — Stellenzahl aus dem dekadischen Logarithmus |

### 10-potenzfunktionen

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | L5: Parameter aus zwei Punkten — Quotient kürzt den Vorfaktor |
| 26 | 5 | L5: Fehler finden — negative Lösung bei geradem Exponenten fehlt (MC) |
| 27 | 5 | L5: Umkehraufgabe — negativer Exponent als Kehrwert |
| 28 | 5 | L5: Umkehraufgabe — Bruchexponent durch Potenzieren auflösen |
| 29 | 5 | L5: zwei Eigenschaften kombinieren — Symmetrie und Monotonie (MC) |
| 30 | 5 | L5: zweischrittig — Vorfaktor aus Punktprobe, dann Funktionswert |
| 31 | 6 | L6: Behauptung prüfen — \(x^3 > x^2\) nur für \(x > 1\) (MC) |
| 32 | 6 | L6: Fallunterscheidung — Parität des Exponenten bei fünf Funktionen |
| 33 | 6 | L6: Parameter aus zwei Bedingungen — \(f(1)\) und \(f(2)\) |
| 34 | 6 | L6: Fallunterscheidung — Monotonie nach Vorzeichen des Exponenten (Review: war wortgleich mit #31) |
| 35 | 6 | L6: gemeinsame Punkte — Faktorisieren statt Kürzen |
| 36 | 6 | L6: Umkehraufgabe — negativer Exponent aus einem Punkt |

### 10-substitution

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | L4: Substitution selbst finden (nicht mehr im Text genannt) |
| 20 | 4 | L4: biquadratische Gleichung ohne Verfahrensansage (Review: nannte vorher die Substitution für #21) |
| 21 | 4 | L4: geschachtelter Klammerterm als Hilfsvariable; Tipp ohne Zwischenlösungen |
| 22 | 4 | L4: Wurzelsubstitution; ersetzt das sinngleiche Paar mit #21 |
| 23 | 4 | L4: Verfahren wählen — welche Gleichung sich überhaupt zurückführen lässt (MC) |
| 24 | 4 | L4: Ausklammern statt Kürzen; Tipp nennt nur den Weg |
| 25 | 5 | L5: zwei Schritte — Hilfsvariable und Rückrechnung zählen |
| 26 | 5 | L5: Exponentialgleichung ohne Nennung der Substitution |
| 27 | 5 | L5: Anzahl reeller Lösungen nach Rücksubstitution |
| 28 | 5 | L5: Fehler finden — Rücksubstitution vergessen (MC) |
| 29 | 5 | L5: Parameter aus gegebener Lösung (Review: eigene Gleichung statt der dritten Fassung von \(x^4 - 5x^2 + c\)) |
| 30 | 5 | L5: zwei Verfahren — Substitution und Wertebereich des Sinus |
| 31 | 6 | L6: Behauptung prüfen — Anzahl reeller Lösungen (MC, Gegenbeispiel) |
| 32 | 6 | L6: Summe der Lösungen bei ungerader Rückwurzel |
| 33 | 6 | L6: Fallunterscheidung nach Vorzeichen der Zwischenlösungen **und** Grenzfall \(4 - c = 0\) (Review: Lösung war \(-1\), richtig ist \(4\)) |
| 34 | 6 | L6: Behauptung prüfen — \(u \le 0\) als Ausnahme (MC) |
| 35 | 6 | L6: Lösung mit ausgeschlossener Zwischenlösung |
| 36 | 6 | L6: Umkehraufgabe — Parameter aus vier gegebenen Lösungen (Vieta) |

### 10-polynomdivision (Dateiname historisch, Inhalt: Grenzwerte und Asymptoten)

Ersatz-Trainer nach Design 1b: Thema **Grenzwerte und Asymptoten**, TH-Lehrplan Kap. 2.3.2
(Grenzwertbegriff anschaulich, lim-Schreibweise, waagerechte und senkrechte Asymptoten).
Der Dateiname bleibt wegen der gedruckten QR-Codes; Zeile 2 der Datei hält das fest.
Alle 36 Aufgaben sind neu.

| id | Level | Kriterium |
|---|---|---|
| 1 | 1 | L1: Randverhalten von \(x^2\) (MC) |
| 2 | 1 | L1: Randverhalten von \(x^3\) für \(x \to -\infty\) (MC) |
| 3 | 1 | L1: Randverhalten von \(1/x\) (MC) |
| 4 | 1 | L1: ein Funktionswert als Beleg für die Annäherung |
| 5 | 1 | L1: Grenzwert von \(1/x^2\) an Beispielwerten (Review: war dieselbe Wertetabellen-Aufgabe wie #19) |
| 6 | 1 | L1: lim-Schreibweise in die Asymptotengleichung übersetzen |
| 7 | 2 | L2: Glied höchsten Grades entscheidet (MC) |
| 8 | 2 | L2: negativer Leitkoeffizient bei geradem Grad (MC) |
| 9 | 2 | L2: senkrechte Asymptote aus der Nennernullstelle |
| 10 | 2 | L2: negativer Leitkoeffizient bei ungeradem Grad (MC; Review: Stufe entdoppelt) |
| 11 | 2 | L2: Anzahl senkrechter Asymptoten bei einem Produkt im Nenner (Review: Stufe entdoppelt) |
| 12 | 2 | L2: waagerechte Asymptote bei additiver Verschiebung |
| 13 | 3 | L3: waagerechte Asymptote von \((3x+1)/(x-2)\) |
| 14 | 3 | L3: Nennergrad größer — Asymptote \(y = 0\) (Review: Stufe entdoppelt) |
| 15 | 3 | L3: senkrechte Asymptoten nach Ausklammern im Nenner (Review: Stufe entdoppelt) |
| 16 | 3 | L3: verschobene Exponentialfunktion, \(x \to -\infty\) |
| 17 | 3 | L3: Basis unter \(1\), \(x \to \infty\) |
| 18 | 3 | L3: Zählergrad größer als Nennergrad (MC) |
| 19 | 4 | L4: aus Wertetabelle auf den Grenzwert schließen |
| 20 | 4 | L4: Umkehraufgabe — Parameter aus der Asymptotenlage |
| 21 | 4 | L4: Funktion zu zwei vorgegebenen Asymptoten wählen (MC) |
| 22 | 4 | L4: Grenzwert ohne Nennung des Verfahrens |
| 23 | 4 | L4: Nenner zerlegen, Asymptote gegen Definitionslücke prüfen |
| 24 | 4 | L4: Modell aus Text — Sättigung als waagerechte Asymptote (MC) |
| 25 | 5 | L5: Parameter aus zwei Bedingungen — Asymptote und Punkt \(P(2 \mid 7)\) (Review: Auswertung bei \(x = 0\) ersetzt) |
| 26 | 5 | L5: Fehler in Grenzwert-Argumentation — „beide wachsen" (MC) |
| 27 | 5 | L5: drei Bedingungen — beide Asymptoten und eine Nullstelle (Review: war eine einzelne Punktprobe) |
| 28 | 5 | L5: drei Bedingungen — beide Asymptoten und ein Funktionswert (Review: verschärft) |
| 29 | 5 | L5: Fehler finden — Nenner wird nie null (MC) |
| 30 | 5 | L5: Fehler finden — Vorfaktor-Regel bei ungleichem Grad angewandt (MC; Review: war dasselbe Verfahren wie #15 und #22) |
| 31 | 6 | L6: Behauptung prüfen — Graph schneidet seine Asymptote (MC) |
| 32 | 6 | L6: Fallunterscheidung nach Gradvergleich bei vier Funktionen |
| 33 | 6 | L6: Fallunterscheidung nach dem Exponenten \(n\) |
| 34 | 6 | L6: Behauptung prüfen — waagerechte Asymptote gilt nicht beidseitig (MC; Review: ersetzt die Aufgabe mit hebbarer Lücke) |
| 35 | 6 | L6: drei Bedingungen nacheinander auswerten (Review: \(f(0)\) durch \(f(3)\) ersetzt) |
| 36 | 6 | L6: Behauptung prüfen — Exponential- gegen Potenzwachstum (MC) |

## Offen (bewusst stehen gelassen, Review 2026-09-30)

- **Hebbare Lücken bleiben außen vor.** Die frühere Aufgabe #34 des Ersatz-Trainers prüfte die
  Behauptung „Nennernullstelle ⇒ senkrechte Asymptote" am Gegenbeispiel \((x^2-4)/(x-2)\). Task 7
  gibt die Vorlage ausdrücklich „ohne Faktorisierung hebbarer Lücken" vor; die Aufgabe ist deshalb
  ersetzt durch die Behauptung, eine waagerechte Asymptote gelte an beiden Rändern (Gegenbeispiel
  \(2^x + 2\)). Die Lücken-Aufgabe ist didaktisch gut und gehört in Kl. 11 (`11-lk-gebrochen-rational`).
- `10-polynomdivision`: Die sechs MC-Aufgaben #1, #2, #3, #7, #8 und #18 haben denselben
  Optionssatz (→∞, →−∞, →0, →1) und sind nach zwei Begegnungen ratbar. Die Engine mischt zwar die
  Reihenfolge, ein Austausch einzelner Aufgaben durch numerische Formate wäre trotzdem besser.
- `10-polynomdivision`: Stufe 4 deckt „Funktionstyp aus **Graph** schließen" nicht ab — ohne Bild
  im Trainer nur über Wertetabelle und Sachkontext gelöst.
- `10-substitution`: #19 und #26 nutzen denselben Gleichungstyp \(a^{2x} - b \cdot a^x + c = 0\)
  (verschiedene Stufen, verschiedene Basen und Fragerichtungen).
- `10-exponentialfunktionen`: KOLLAPS L1/L2 bleibt — Stufe 1–3 werden laut Plan nicht neu geschrieben.
