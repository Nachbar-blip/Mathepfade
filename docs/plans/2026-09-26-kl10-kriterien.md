# Klasse 10 — Kriterien je Trainer (Welle Task 7, Stand 2026-09-30)

Lokale Nachvollziehbarkeit; im Public-HTML stehen die Kriterien bewusst nicht.
Grundlage: Rubrik aus `2026-09-26-lehrplan-th-und-level-progression-plan.md`, Befunde aus
`../audit/audit-2026-09-19-mathepfade.md` (Zeilen 94-107). Lesart Kl. 10 durchgaengig:
L4 = Verfahren selbst waehlen / Modell aus Text / Umkehraufgabe; L5 = zwei Verfahren
kombinieren, Parameter aus zwei Bedingungen, Fehler in vorgelegter Rechnung;
L6 = Behauptung begruendet pruefen, Fallunterscheidung, Grenzfall.
Jede Loesung mit Wolfram nachgerechnet; Bilder je geaenderter Stufe per `tests/bild.py`
angesehen. Jeder Block wurde nach der Umsetzung von einem zweiten Agenten geprueft; die
Befunde und ihre Behebung stehen je Block unter "Review-Nachtrag".

Die drei Bloecke der Welle:

| Block | Trainer | Umfang |
|---|---|---|
| A Analysis | 7 | Exponentialfunktionen, ganzrationale Funktionen, Graphentransformationen, Logarithmus, Potenzfunktionen, Substitution, **Ersatz** 10-polynomdivision -> Grenzwerte und Asymptoten |
| B Trigonometrie und Kreis | 5 | Einheitskreis, trig. Gleichungen, Sinusfunktion, Sinus-/Kosinussatz (dort auch L3/L4), Kreissektor |
| C Stochastik | 2 | bedingte Wahrscheinlichkeit (Vierfeldertafel, Unabhaengigkeit), mehrstufige Zufallsversuche |


> **Nachtrag 2026-10-01:** Die in Block C beschriebene Lücke (Verteilung und
> Erwartungswert fehlen in Klasse 10) ist geschlossen — mit dem neuen Trainer
> `10-stoch-erwartungswert`, nicht durch eine Änderung an den beiden Trainern hier.
> Kriterien dort: `2026-10-01-kl10-erwartungswert-kriterien.md`.

---

# Block A — Analysis
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

### Offen (bewusst stehen gelassen, Review 2026-09-30)

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

---

# Block B — Trigonometrie und Kreis
Lokale Nachvollziehbarkeit; im Public-HTML stehen die Kriterien bewusst nicht.
Grundlage: Rubrik aus `2026-09-26-lehrplan-th-und-level-progression-plan.md`
(Lesart Kl. 10: L4 = Verfahren selbst wählen, Modell aus Text, Umkehraufgabe;
L5 = zwei Verfahren kombinieren, Parameter aus zwei Bedingungen, Fehler in vorgelegter
Rechnung; L6 = Fallunterscheidung, Behauptung begründet prüfen, Grenzfall),
Befunde aus `../audit/audit-2026-09-19-mathepfade.md` (Zeilen 94–107).
Niveau: TH-Lehrplan 2.3.3 (Sinus-/Kosinussatz, Kreissektor, Bogenmaß) und 2.3.2
(Sinusfunktion, trigonometrische Gleichungen).
Jede Lösung mit Wolfram nachgerechnet; Bilder L5/L6 per `tests/bild.py` angesehen.

Abgrenzung der vier Trigonometrie-Trainer (gegen sinngleiche Aufgaben):
**10-trig-einheitskreis** = Winkelmaße, Bogenmaß, Symmetrien und Werte am Kreis;
**10-trig-gleichungen** = \(\sin x = a\) lösen, Lösungsmengen im Intervall, alle Lösungen;
**10-trig-sinusfunktion** = Graph, Amplitude/Periode/Verschiebung, Modellierung;
**10-trig-sinussatz-kosinussatz** = allgemeine Dreiecke, Berechnungen, SSW-Fallunterscheidung.
**10-kreissektor** = Bogenlänge, Sektorfläche, Umkehraufgaben, zusammengesetzte Flächen.

| Trainer | Audit-Befund | Geändert |
|---|---|---|
| 10-trig-einheitskreis | KEIN_AFB3 L5; KEIN_AFB3 L6 | L5/L6 neu. Alt waren L5 = Grundbeziehung einsetzen (AFB I) und L6 = Standardwinkel ablesen — Letzteres zudem Thema von 10-trig-gleichungen. Neu: Fehlersuche mit Quadrantenvorzeichen, Punkt auf dem Kreis, Winkelhalbierende, Bogenmaß-Umkehr, Parameterpunkt \(P(a\mid 2a)\); L6 mit Symmetrie-Behauptung, Anzahl-Fragen, Widerlegung durch Gegenbeispiel, Periodizität, Maximum von \(\sin\alpha+\cos\alpha\) |
| 10-trig-gleichungen | KEIN_AFB3 L5; KEIN_AFB3 L6; Tipps #7/#9/#12 mit Lösungswert; #34 MC-Länge | L5/L6 neu (Division durch null-werdenden Term, quadratische Form mit Fallausschluss, Grundbeziehung ersetzen, innere Funktion, ganzzahliger Parameter, unvollständige Lösungsmenge; L6 mit Anzahlvergleich, Produktform, Tangensperiode, Parameter aus zwei Bedingungen, Modellierung mit Zeitraum, Fallunterscheidung nach \(c\)). Tipps #7/#9/#12 nennen jetzt den Weg statt \(30°/60°/45°\) |
| 10-trig-sinusfunktion | KEIN_AFB3 L5; KEIN_AFB3 L6; #20/#32 MC-Länge | L5/L6 neu. Alt waren L5 = \(\sin x = a\) lösen (Dublette zu 10-trig-gleichungen) und L6 = Einsetzen in \(h(t)=\sin t\). Neu: Parameter aus Höchstwert und Periode, Amplitude aus Schwankungsbereich, \(b\) aus halber Periode, Fehler „Periode = \(b\cdot 2\pi\)“, Verschiebung aus steigender Nullstelle, Anzahl Hochpunkte; L6 mit Periodenbehauptung, Tag größter Tageslänge, Gleichungssystem aus Hoch- und Tiefpunkt, \(a\) aus Nullstellenzahl, Phasenverschiebung \(\sin(x+\frac{\pi}{2})=\cos x\), Periode aus Viertelabstand. #20 mit vier gleich langen Optionen |
| 10-trig-sinussatz-kosinussatz | KEIN_AFB3 L6; KOLLAPS L2/L3; KOLLAPS L3/L4 | L3–L6 neu. L3 jetzt Klassenarbeits-Standard mit Zwischenschritt (Kosinussatz mit stumpfem Winkel, Winkel aus drei Seiten, Sinussatz nach Winkelsumme) statt Wiederholung von L2; L4 verlangt die Wahl des Satzes, Umfang, Modell aus Text, Umkehraufgaben; L5 kombiniert beide Sätze, Parameter über quadratische Gleichung, Peilaufgabe, stumpfe SSW-Lösung, gleichschenkliger Sonderfall; L6 Fallunterscheidung SSW (zwei / genau ein / kein Dreieck), Grenzfall \(a=b\sin\alpha\), zwei Behauptungen. Alle Tipps ohne fertige Formelzeile |
| 10-kreissektor | KEIN_AFB3 L5; KOLLAPS L2/L3; #24 MC-Länge | L5/L6 neu. Alt war L5 reine Bogenmaß-Umrechnung (AFB I und Dublette zu 10-trig-einheitskreis), L6 Einsetzaufgaben. Neu: Winkel aus Sektorumfang, Bogen aus Fläche, Fehler „Umfang statt Fläche“, Radius aus \(A\) und \(b\), Viertelkreis minus Dreieck, Flächenverhältnis 2 : 3; L6 mit Skalierungsbehauptung, \(r = 2\) als Grenzfall, Ringsektor, Kegelabwicklung, Segment-Behauptung, Radius aus Flächengleichheit. #24 mit vier gleich langen Optionen. KOLLAPS L2/L3 bleibt offen (Stufe 1–3 werden laut Plan nicht neu geschrieben) |

### 10-trig-einheitskreis

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | L5: Fehler in vorgelegter Rechnung — Vorzeichen im II. Quadranten (MC) |
| 26 | 5 | L5: drei Schritte — Kreisgleichung, Quadrantenvorzeichen, Summe der Koordinaten |
| 27 | 5 | L5: zwei Bedingungen — aus \(\sin\alpha\cos\alpha = 0{,}48\) über Summen- und Differenzquadrat (ersetzt die Dublette \(\sin\alpha=\cos\alpha\)) |
| 28 | 5 | L5: zwei Winkel getrennt — \(\frac{5\pi}{4}\) und \(\frac{5\pi}{3}\) (früher \(\frac{7\pi}{6}\), enthielt L4 #24 als Teilschritt) |
| 29 | 5 | L5: Bogenlänge als Bogenmaß, Umrechnung, dann Vergleich mit dem Halbkreis |
| 30 | 5 | L5: Parameter — Punkt \(P(a\mid 2a)\) auf dem Einheitskreis |
| 31 | 6 | L6: Behauptung prüfen — \(\sin(\alpha+180°)\) (MC, Gegenbeispiel) |
| 32 | 6 | L6: Produktform \(\sin\alpha\cos\alpha = 0\), zwei Fälle, Achsenlage |
| 33 | 6 | L6: Behauptung widerlegen — \(\sin^4+\cos^4\) nicht konstant (MC, damit die Entscheidung selbst bewertet wird) |
| 34 | 6 | L6: Periodizität — kleinster nichtnegativer Winkel zu \(-1000°\) |
| 35 | 6 | L6: Maximum von \(\sin\alpha+\cos\alpha\) über Quadrieren |
| 36 | 6 | L6: Behauptung prüfen — Randfall \(0°/360°\) (MC) |

### 10-trig-gleichungen

| id | Level | Kriterium |
|---|---|---|
| 7, 9, 12 | 2 | Tipp nennt nur den Weg (vorher stand der Lösungswert darin) |
| 25 | 5 | L5: Fehler finden — Division durch \(\sin x\) verliert Lösungen (MC) |
| 26 | 5 | L5: Substitution mit Fallausschluss (\(\sin x = 2\) unmöglich) |
| 27 | 5 | L5: zwei Verfahren — Grundbeziehung, dann quadratische Gleichung |
| 28 | 5 | L5: innere Funktion — Intervall des Arguments auswerten |
| 29 | 5 | L5: Parameter — ganzzahlige \(k\) mit \(\sin x = k/2\) |
| 30 | 5 | L5: Fehler finden — unvollständige Lösungsmenge bei \(\sin(2x)\) (MC) |
| 31 | 6 | L6: Behauptung prüfen — Anzahlvergleich \(\cos(2x)\) gegen \(\cos x\) (MC) |
| 32 | 6 | L6: Produktform, Fallunterscheidung, halboffenes Intervall |
| 33 | 6 | L6: Umkehraufgabe — Intervallgrenze aus Lösungsanzahl (Tangensperiode) |
| 34 | 6 | L6: Parameter aus zwei Bedingungen (Lösung und \(a+b=1\)) |
| 35 | 6 | L6: Modellierung — Zeitraum mit \(h(t)\ge 11\) über Grenzzeitpunkte |
| 36 | 6 | L6: Fallunterscheidung nach \(c\) — genau zwei Lösungen (MC) |

### 10-trig-sinusfunktion

| id | Level | Kriterium |
|---|---|---|
| 20 | 4 | MC-Optionen auf gleiche Länge gebracht |
| 25 | 5 | L5: Parameter aus zwei Angaben — Hochpunkt liefert \(a\), seine Lage \(b\); gefragt ist \(a+b\) |
| 26 | 5 | L5: Amplitude aus dem Schwankungsbereich und \(b\) aus der halben Periode; gefragt ist \(a\cdot b\) |
| 27 | 5 | L5: senkrechter und waagerechter Abstand Hochpunkt–Tiefpunkt aus Amplitude und Periode |
| 28 | 5 | L5: Fehler finden — Periode multipliziert statt dividiert (MC) |
| 29 | 5 | L5: Verschiebung aus steigender Nullstelle |
| 30 | 5 | L5: Anzahl Hochpunkte im Intervall aus der Periode |
| 31 | 6 | L6: Behauptung prüfen — Verdopplung von \(b\) (MC) |
| 32 | 6 | L6: Modellierung — Tag der größten Tageslänge |
| 33 | 6 | L6: Parameter aus zwei Bedingungen (Hoch- und Tiefpunkt) |
| 34 | 6 | L6: Umkehraufgabe — \(a\) aus der Nullstellenanzahl |
| 35 | 6 | L6: Behauptung prüfen — \(\sin(x+\frac{\pi}{2}) = \cos x\) (MC) |
| 36 | 6 | L6: Periode aus dem Abstand Mittellage–Hochpunkt (Viertelperiode) |

### 10-trig-sinussatz-kosinussatz

| id | Level | Kriterium |
|---|---|---|
| 13–18 | 3 | L3 entdoppelt: Kosinussatz mit stumpfem Winkel, Winkel aus drei Seiten, Sinussatz erst nach der Winkelsumme — je ein Zwischenergebnis |
| 19 | 4 | L4: Verfahren wählen und Umfang ergänzen |
| 20 | 4 | L4: Modell aus Text — Beet, Winkelsumme und Entscheidung, welche Seite die längere ist (ersetzt die zu #16 sinngleiche Rechenaufgabe) |
| 21 | 4 | L4: Umkehraufgabe — Winkel aus zwei Seiten und Gegenwinkel |
| 22 | 4 | L4: Modell aus Text (zwei Wege, eingeschlossener Winkel) |
| 23 | 4 | L4: Satzwahl begründen (MC, Auswahl ist die Leistung) |
| 24 | 4 | L4: dritte Seite erst aus dem Umfang beschaffen, dann Winkel (ersetzt die zu #14/#17 sinngleiche SSS-Aufgabe) |
| 25 | 5 | L5: Fehler finden — Vorzeichen von \(\cos 120°\) (MC) |
| 26 | 5 | L5: zwei Sätze nacheinander (Kosinussatz, dann Winkel) |
| 27 | 5 | L5: Parameter über quadratische Gleichung, zwei Lösungen |
| 28 | 5 | L5: Modell aus Text — Peilung, Winkelsumme, Sinussatz |
| 29 | 5 | L5: SSW mit stumpfer Nebenlösung |
| 30 | 5 | L5: gleichschenkliger Sonderfall erkennen, dann Umfang |
| 31 | 6 | L6: Fallunterscheidung SSW — zwei Dreiecke |
| 32 | 6 | L6: Grenzfall \(a = b\sin\alpha\) — genau ein Dreieck |
| 33 | 6 | L6: Behauptung prüfen — Sinuswert legt Winkel nicht fest (MC) |
| 17 | 3 | L3: kleinsten Winkel selbst identifizieren (vorher sinngleich zu #14) |
| 34 | 6 | L6: eindeutiger Bezug ohne Zeichnung (Winkel zwischen \(a\) und \(b\)) |
| 35 | 6 | L6: Fallunterscheidung SSW — kein Dreieck (\(\sin\beta > 1\)) |
| 36 | 6 | L6: Behauptung prüfen — negativer Kosinuswert und Stumpfwinkligkeit (MC) |

### 10-kreissektor

| id | Level | Kriterium |
|---|---|---|
| 24 | 4 | MC-Optionen auf gleiche Länge gebracht, Tipp ohne Antwort |
| 25 | 5 | L5: Umkehraufgabe — Winkel aus dem Sektorumfang (zwei Schritte) |
| 26 | 5 | L5: Bogen aus der Fläche, danach Umfang des Sektors (zwei Schritte) |
| 27 | 5 | L5: Fehler finden — Umfangs- statt Flächenanteil (MC) |
| 28 | 5 | L5: Radius aus Winkel und Bogen, danach Flächeninhalt (ersetzt das zweite Umstellen von \(A=\frac12 r b\)) |
| 29 | 5 | L5: zusammengesetzte Figur — Sektor minus Dreieck |
| 30 | 5 | L5: Verhältnis in einen Bruchteil übersetzen, dann Kreisfläche und Sektorfläche |
| 31 | 6 | L6: Behauptung prüfen — Winkel verdoppeln, Radius halbieren (MC) |
| 32 | 6 | L6: Grenzfall — \(r = 2\) macht Bogen- und Flächenmaßzahl gleich |
| 33 | 6 | L6: Ringsektor als Differenz zweier Sektoren |
| 34 | 6 | L6: Transfer — Kegelabwicklung, Bogen wird Grundkreisumfang |
| 35 | 6 | L6: Behauptung prüfen — Segmentanteil hängt vom Winkel ab (MC) |
| 36 | 6 | L6: Umkehraufgabe — Radius aus Flächengleichheit mit einem Quadrat |

### Review-Nachtrag 2026-09-30

Behoben nach der Prüfung durch den Review-Agenten:

- **KOLLAPS L3/L4** in `10-trig-sinussatz-kosinussatz` war noch nicht weg: #20 wiederholte
  #16 (Winkelsumme, dann Sinussatz) und #24 wiederholte #14/#17 (SSS über den Kosinussatz).
  Beide ersetzt durch Aufgaben, deren Leistung die Übersetzung aus dem Text bzw. das
  Beschaffen der fehlenden Seite ist. #17 fragt jetzt nach dem kleinsten Winkel statt
  wie #14 nach dem Winkel bei C.
- **Dubletten**: `\(\sin\alpha=\cos\alpha\)` stand in drei Trainern/Stufen — im
  Einheitskreis (#27) ersetzt. Einheitskreis #28 enthielt #24 als Teilschritt
  (\(\frac{7\pi}{6} = 210°\)) — anderes Winkelpaar. Kreissektor #26/#28 waren beide ein
  Umstellen von \(A=\frac12 r b\) — #28 neu.
- **Stufe 5 angehoben**: Einheitskreis #26/#28/#29, Sinusfunktion #25/#26/#27,
  Kreissektor #26/#28/#30 verlangen jetzt zwei Schritte bzw. zwei Bedingungen.
- **Tipps**: gelieferte Formel entfernt in Einheitskreis #26; fertige Gleichung entfernt in
  Kreissektor #19–#23 und in Trig-Gleichungen #20/#21/#23/#24 (Stufe 4).
- **MC-Längen** angeglichen: Einheitskreis #25, Trig-Gleichungen #25, Sinusfunktion #28,
  Kreissektor #24 und #35.
- **Aufgabenformat**: Einheitskreis #33 ist jetzt MC, damit die Entscheidung über die
  Behauptung bewertet wird und nicht nur der Zahlenwert.

### Offen (bewusst nicht in dieser Welle)

- `10-trig-gleichungen`: In 6 von 12 Aufgaben auf L5/L6 wird nach der *Anzahl* der Lösungen
  gefragt — die Formatvielfalt ist zu gering.
- `10-trig-gleichungen`: L3/L4-Kollaps (#17/#18 gegen #23/#24) — Stufe 3 und 4 dort nicht
  im Auftrag dieser Welle.
- Trainerübergreifende L1/L2-Dublette: `10-trig-einheitskreis #3/#6` gegen
  `10-trig-sinusfunktion #7/#11`.
- `10-kreissektor #24` ist eine Begriffsabfrage auf einer AFB-II-Stufe.
- `10-kreissektor`: Stufe 5 setzt \(A = \frac12 r b\) voraus, ohne dass diese Beziehung auf
  L1–L4 vorkommt (nur #18 nennt sie als MC-Begründung).
- `10-kreissektor`: KOLLAPS L2/L3 (Stufe 1–3 werden laut Plan nicht neu geschrieben).

---

# Block C — Stochastik
Lokale Nachvollziehbarkeit; im Public-HTML stehen die Kriterien bewusst nicht.
Grundlage: Rubrik aus `docs/plans/2026-09-26-lehrplan-th-und-level-progression-plan.md`
(Lesart Kl. 10 Stochastik: L4 = Verfahren selbst wählen, Modell aus Text, Bedingung
richtig herum ansetzen; L5 = zwei Verfahren kombinieren (Tafel vervollständigen und dann
bedingen, mit und ohne Zurücklegen vergleichen), Parameter aus zwei Bedingungen,
Fehler in vorgelegter Rechnung; L6 = Behauptung begründet prüfen, Fallunterscheidung
bzw. Grenzfallbetrachtung, Rückwärtsaufgabe über die volle Vierfeldertafel),
Befunde aus `docs/audit/audit-2026-09-19-mathepfade.md` (beide Trainer: KEIN_AFB3 L5 **und** L6).
Niveau: TH-Lehrplan 2.3.4 (Vierfeldertafel, stochastische Unabhängigkeit, mehrstufige
Zufallsversuche, Pfadregeln, Ziehen mit und ohne Zurücklegen, Gegenereignis).
Jede Lösung mit Wolfram nachgerechnet; Bilder L5/L6 per `tests/bild.py` angesehen.

### Abgrenzung der beiden Trainer (gegen Dubletten im Pool)

`10-stoch-bedingte-wsk` = **Vierfeldertafel und stochastische Unabhängigkeit**: Tafel aus
absoluten Zahlen oder Anteilen füllen, bedingte Wahrscheinlichkeit als Einschränkung der
Grundmenge, Produktkriterium \(P(A \cap B) = P(A) \cdot P(B)\), Additionssatz, Gegenereignis
als Merkmalsausprägung. Keine Urnenziehungen ab Stufe 4.

`10-stoch-mehrstufig` = **Baumdiagramm und Pfadregeln**: mehrstufige Versuche, Ziehen mit
und ohne Zurücklegen, Gegenereignis bei „mindestens eins", Pfade zählen und addieren,
Umkehraufgaben nach der Urnenzusammensetzung. Keine Vierfeldertafel, kein Unabhängigkeits-
kriterium als Rechenziel.

| Trainer | Audit-Befund | Geändert |
|---|---|---|
| 10-stoch-bedingte-wsk | KEIN_AFB3 L5; KEIN_AFB3 L6; MC-Längen-Warnung #19/#34; Rückverweise #12/#16/#17 | L5/L6 komplett neu (12 Aufgaben): Tafel vervollständigen und „genau eines" bestimmen, Fehler „Bedingung im Nenner vertauscht", Eckzelle für Unabhängigkeit, Schnitt aus Vereinigung und dann bedingen, \(P(B)\) aus Additionssatz plus Unabhängigkeit, Abweichung von der Unabhängigkeits-Eckzelle; „ausschließend = unabhängig?", kleinstmögliches \(P(A \cup B)\) (Grenzfall \(B \subseteq A\)), Rückwärtsaufgabe über die volle Tafel, „\(P(A\mid B) > P(A) \Rightarrow P(B\mid A) > P(B)\)?", \(P(A\mid \overline B)\) aus drei bedingten Angaben, Unabhängigkeit überträgt sich auf das Gegenereignis. L4 #19 (reine Bayes-Formel-Abfrage, MC-Längen-Warnung) durch eine Modellaufgabe ersetzt. Rückverweise „in obigem Beispiel"/„(Gleiche Situation:)" in #12/#16/#17 durch vollständige Angaben ersetzt |
| 10-stoch-mehrstufig | KEIN_AFB3 L5 (L5 war durchgehend Erwartungswert — nicht lehrplanfremd, aber Thema eines anderen Trainers, siehe Abgrenzung); KEIN_AFB3 L6; Rückverweis im Tipp #32 | L5/L6 komplett neu (12 Aufgaben): Anzahl leerer Batterien aus der Pfadgleichung, Fehler „mit Zurücklegen gerechnet, obwohl die Lose behalten werden", „höchstens ein Ausfall" als zwei Fälle, Vergleich mit/ohne Zurücklegen, Mindestanzahl Drehungen für 90 %, genau zwei Treffer bei drei verschiedenen Wahrscheinlichkeiten; „zweiter Zug ungünstiger?" (bedingt gegen unbedingt), Wartezeit „mehr als zwei Züge", zweistufiger Versuch mit veränderter Urne, „erreicht die 1?", Doppelzählung bei „oder" korrigieren, Raten mit mindestens zwei von drei Treffern. Tipps von #19/#22/#24 (L4) von der fertigen Bernoulli-Gleichung auf den Weg umgestellt |

### 10-stoch-bedingte-wsk

| id | Level | Kriterium |
|---|---|---|
| 12 | 2 | Angaben vollständig im Text (Rückverweis „in obigem Beispiel" entfernt) |
| 16 | 3 | Angaben vollständig im Text (Rückverweis „(Gleiche Situation:)" entfernt) |
| 17 | 3 | Angaben vollständig im Text (Rückverweis „(Gleiche Situation:)" entfernt) |
| 19 | 4 | L4: Bedingung in der ungewohnten Richtung — die Grundmenge (Orchester) steht nicht im Text und muss erst gebildet werden (0,577); ersetzt die reine Formelabfrage zum Satz von Bayes |
| 25 | 5 | L5: zwei Schritte — Tafel füllen, dann „genau eines von beidem" (0,70) |
| 26 | 5 | L5: Fehler finden — Bedingung steht im Nenner, nicht das bedingte Ereignis (MC) |
| 27 | 5 | L5: Parameter aus zwei Randbedingungen — Eckzelle für Unabhängigkeit (100) |
| 28 | 5 | L5: zwei Verfahren — Schnitt aus dem Additionssatz, dann bedingen (0,667) |
| 29 | 5 | L5: Parameter aus zwei Bedingungen — Additionssatz plus Unabhängigkeit (0,4); Tipp nennt nur, dass eine Zusatzinformation im Wort „unabhängig" steckt |
| 30 | 5 | L5: Tafel mit fehlendem Randwert — bedingte Angabe in eine Zelle umrechnen, zwei Randsummen ergänzen, in der anderen Gruppe bedingen (0,30) |
| 31 | 6 | L6: Behauptung prüfen — unvereinbar ist nicht unabhängig, sogar stets abhängig (MC) |
| 32 | 6 | L6: Grenzfallbetrachtung — kleinstmögliches \(P(A \cup B)\) bei \(B \subseteq A\) (0,6) |
| 33 | 6 | L6: Rückwärtsaufgabe über die volle Tafel mit Unabhängigkeit (120) |
| 34 | 6 | L6: Behauptung prüfen — beide Ungleichungen gleichwertig zum Produktkriterium (MC) |
| 35 | 6 | L6: drei bedingte Angaben in die Tafel umrechnen, Bedingung wechseln (0,455) |
| 36 | 6 | L6: Behauptung prüfen — Unabhängigkeit überträgt sich auf das Gegenereignis (MC) |

### 10-stoch-mehrstufig

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | L5: Umkehraufgabe — Anzahl aus der Pfadgleichung, \(k(k-1) = 6\), negative Lösung verwerfen (3) |
| 26 | 5 | L5: Fehler finden — mit Zurücklegen gerechnet, obwohl die Lose behalten werden (MC) |
| 27 | 5 | L5: „höchstens einer" als zwei Fälle, Pfadanzahl beachten (0,9928) |
| 28 | 5 | L5: zwei Verfahren vergleichen — mit gegen ohne Zurücklegen, Differenz (0,027) |
| 29 | 5 | L5: Umkehraufgabe — Mindestanzahl aus Ungleichung mit Gegenereignis (11) |
| 30 | 5 | L5: dreistufiger Baum mit ungleichen Wahrscheinlichkeiten, Pfade addieren (0,38) |
| 31 | 6 | L6: Behauptung prüfen — bedingt gegen unbedingt im zweiten Zug (MC) |
| 32 | 6 | L6: Ereignis umformulieren — „mehr als zwei Züge" ist ein einziger Pfad (0,30) |
| 33 | 6 | L6: zweistufiger Versuch mit veränderter Urne — die zweite Stufe hängt vom Ausgang der ersten ab (0,35) |
| 34 | 6 | L6: Behauptung prüfen — Grenzwert 1 wird nie erreicht (MC) |
| 35 | 6 | L6: vorgelegte Doppelzählung korrigieren, Differenz erklären (0,643) |
| 36 | 6 | L6: „mindestens zwei von drei" als Fallunterscheidung, Pfade zählen (0,1563) |

### Gates nach der Arbeit

```
python tests/level_check.py --strict trainer/10-stoch-bedingte-wsk.html trainer/10-stoch-mehrstufig.html   # Exit 0, 0 Warnungen
python tests/lehrplan_check.py --strict trainer/10-stoch-bedingte-wsk.html trainer/10-stoch-mehrstufig.html # Exit 0, 0 Befunde
python tests/katex_check.py trainer/10-stoch-bedingte-wsk.html trainer/10-stoch-mehrstufig.html             # ok
python -m pytest tests/test_trainer.py -k "bedingte or mehrstufig" -q                                        # 14 passed
python tests/bild.py trainer/<datei>.html --level 5 / --level 6                                              # vier PNG angesehen
```

### Offene Punkte

- **Erwartungswert und Wahrscheinlichkeitsverteilung sind in Kl. 10 jetzt nicht mehr abgedeckt.**
  Die alte Stufe 5 von `10-stoch-mehrstufig` bestand ausschließlich aus Erwartungswert-Aufgaben;
  entfernt wurde sie wegen der **Trainer-Abgrenzung** (dieser Trainer ist Baumdiagramm und
  Pfadregeln), nicht wegen des Lehrplans. TH 2.3.4 nennt für Klassenstufe 10 ausdrücklich
  „Wahrscheinlichkeitsverteilungen diskreter Zufallsgrößen bestimmen" sowie „Erwartungswert und
  Standardabweichung diskreter Zufallsgrößen berechnen und interpretieren"; erst die
  Binomialverteilung mit 2σ-Regel gehört in die Qualifikationsphase. Ein eigener Kl.-10-Trainer
  dafür wäre die saubere Lösung — Entscheidung des Autors, hier bewusst **nicht** angelegt.
- Bernoulli-Ketten auf Stufe 4 (#19/#22/#24 in `10-stoch-mehrstufig`) bleiben: TH 2.3.4 nennt für
  Kl. 10 wörtlich „Bernoulli-Ketten … die Bernoulli-Formel anwenden, dabei Binomialkoeffizienten
  bestimmen und inhaltlich deuten". Ihre Tipps wurden von der fertigen Gleichung auf den Weg
  umgestellt, damit die Deutung und nicht das Eintippen die Leistung ist.
- Nicht behoben, nur notiert: `10-stoch-bedingte-wsk` #12 hat bei einer Ja/Nein-Frage auf L2 vier
  MC-Optionen; `10-stoch-mehrstufig` #27 und #36 nutzen bei verschiedenem Text dasselbe
  Bernoulli-Rechenmuster.

### Beim Einsetzen aufgefallen

`10-stoch-mehrstufig` #23/#24 (Bestand, Stufe 4): Das Dezimalkomma-Markup `0{,}3` stand im
Aufgabentext **ausserhalb** von `\(…\)` und wurde deshalb woertlich als „0{,}3" angezeigt.
Kein Gate sieht das — weder `level_check` (kein KaTeX-Befehlswort) noch `katex_check` (was
nicht in einer Mathe-Umgebung steht, wird gar nicht erst gerendert). Gefunden allein in der
Sichtpruefung am PNG, behoben durch `\\(0{,}3\\)`. Kandidat fuer eine neue Gate-Regel:
`{,}` im Klartext ausserhalb von `\(…\)` und `$$…$$`.

Der erste Reparaturversuch lief ueber ein Bash-Heredoc und verlor je einen Backslash
(`\\(` wurde zu `\(`, vom JS-String verschluckt) — die Regel „nie Bash-Heredoc fuer
Aufgabentexte" aus `CLAUDE.md` gilt auch fuer kleine Korrekturen. Zweiter Versuch per
Scratchpad-Skript war richtig.


Die Zeile der Aufgabe #36 trägt in beiden Dateien den Array-Abschluss `];` am Zeilenende.
Ein zeilenweises Ersetzen nach `id`-Nummer entfernt ihn und macht die Datei unparsbar
(`level_check` meldet „AUFGABEN nicht auswertbar"). Beim Ersetzen der letzten Aufgabe ist
der Abschluss also mitzuschreiben.

---
