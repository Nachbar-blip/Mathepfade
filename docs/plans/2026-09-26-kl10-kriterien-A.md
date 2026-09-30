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
| 27 | 5 | L5: zwei Verfahren — Vielfachheit in Produktform, dann \(f(0)\) |
| 28 | 5 | L5: Parameter — Bedingung an \(c\) für keine reelle Nullstelle (MC) |
| 29 | 5 | L5: zweischrittig — Ausklammern und Faktorisieren |
| 30 | 5 | L5: Umkehraufgabe — Parameter aus einem Funktionswert |
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
| 29 | 5 | L5: zweischrittig — Streckfaktor isolieren, dann Wurzel |
| 30 | 5 | L5: zwei Verfahren — Ausklammern und quadratische Ergänzung |
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
