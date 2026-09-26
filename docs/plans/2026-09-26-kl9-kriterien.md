# Klasse 9 — Überarbeitung je Trainer (Stand 2026-09-26)

Lokale Nachvollziehbarkeit; im Public-HTML stehen die Kriterien bewusst nicht.
Grundlage: Rubrik aus `docs/plans/2026-09-26-lehrplan-th-und-level-progression-plan.md`
(Lesart Kl. 9: L4 = Verfahren/Potenzgesetz selbst wählen, Modell aus Text (Zehnerpotenzen,
Wachstum), Umkehraufgabe (Exponent/Basis gesucht); L5 = zweischrittige Sachaufgabe ohne Weg,
Fehler in vorgelegter Umformungskette, Parameter aus zwei Bedingungen, Wurzelgleichung mit
Probe/Scheinlösung; L6 = Behauptung begründet prüfen, Sonderfall (keine Lösung,
Definitionsmenge), Umkehraufgabe (a und n aus zwei Punkten), Fallunterscheidung nach
Vorzeichen/Parität des Exponenten), Befunde aus `docs/audit/audit-2026-09-19-mathepfade.md`.
Niveau: TH-Lehrplan 2.3.1 (Potenz-/Wurzelschreibweise, Potenzgesetze begründen und anwenden,
ganzzahlige und rationale Exponenten, Potenz- und Wurzelgleichungen, Zehnerpotenzen; Logarithmus
höchstens als Schreibweise).
Jede Lösung mit Wolfram|Alpha nachgerechnet; Bilder L5/L6 per `tests/bild.py` angesehen.

Blöcke: **A1 Potenzen und Wurzeln (7)** → A2 Quadratische Funktionen/Gleichungen, Wachstum,
LGS, Bruchgleichungen → B Geometrie/Stochastik.

## Block A1 — Potenzen und Wurzeln

Abgrenzung der sieben Trainer (gegen Dubletten im Pool):
7-potenzgesetze = natürliche Exponenten, gleiche Basis / gleicher Exponent, Begründung;
8-potenzen-negativ = negative Exponenten, Kehrwert, Zehnerpotenzen, wissenschaftliche Notation;
9-potenzen-ganzzahlig = gemischte Potenzgesetze mit Variablen, Größenvergleiche;
9-potenzen-rational = Wurzel ↔ Potenz, Bruchexponenten; 9-quadratwurzeln = Wurzelwerte,
teilweises Radizieren, Wurzelgesetze, Nenner rational, irrationale Zahlen;
9-potenzgleichungen = x^n = a, Parität, Wachstumsfaktor aus n Perioden;
9-wurzelgleichungen = Quadrieren, Probe, Scheinlösung, Definitionsmenge.

| Trainer | Audit-Befund | Geändert |
|---|---|---|
| 9-quadratwurzeln | KEIN_AFB3 L5; DUENNER_WEG L1–L3 | L5/L6 neu: Fehler in Kette (√16 = ±4), Zaun um quadratisches Beet (zweischrittig), a aus √a·√18 = 12, Fehler 25√2, Rechteckumfang aus √12 und √27, x aus (√x+3)(√x−3) = 11; „√(a+b) = √a+√b?", √(x²) = −x (Fallunterscheidung), k aus Vielfachen von √5, „Produkt irrationaler Zahlen irrational?", 1/(√5−2) rationalisieren, „doppelte Fläche = doppelte Seite?". L4 #19 von MC auf numerisch (k√2), #21 (√200 dezimal) durch Nenner-rational-machen ersetzt; L1/L2-Tipps ohne Lösungswert |
| 7-potenzgesetze (Umzug 7 → 9) | KEIN_AFB3 L5; KURZ L1–L5; DUENNER_WEG L2/L3; L4 #22 „mit der Potenzregel" (Rechenart-Ansage), L6 #32/#34 mit Rechenweg-Hinweis | L4–L6 neu: Exponent aus Dreifach-Umformung, n aus 3^n·3^4 = 3^10, Koeffizient von (2a³)², 4⁵/2⁷ ohne TR, Quadratfläche als Zweierpotenz, 6⁴/3⁴; Fehler „a⁶·a⁴ = a²⁴", a+n aus zwei Bedingungen, Würfel 3² cm in 3-cm-Würfel, Fehler „2³·3² = 6⁵", 8^x = 2^12, „2^20 ≈ 2000?"; Begründung a^m·a^n = a^{m+n}, „(a^m)^n = a^{(m^n)}?", 2^300 gegen 3^200, 2^n+2^n = 2^{2n} (nur n = 1), Ziffernzahl von 2^10·5^8, Bakterien 2^12 rückwärts. Für Kl. 9 angehoben: Exponentengleichungen, Basiswechsel (4 = 2², 8 = 2³), Parameter aus zwei Bedingungen; L1–L3 unverändert (natürliche Exponenten bleiben Thema des Trainers) |
| 8-potenzen-negativ (Umzug 8 → 9) | KEIN_AFB3 L5/L6; KOLLAPS L1/L2, L2/L3; KURZ L1–L3, L5; DUENNER_WEG L1–L4 | L4–L6 neu: Blattstapel (Modell), wissenschaftliche Notation korrigieren, n aus 5^n = 1/125, Tropfen pro Liter, Haar gegen Bakterium, n aus (1/4)^n = 64; Fehler „2^{-3} = (−2)³", Virus/Bakterium im Modellmaßstab, a·n aus zwei Bedingungen, Fehler „10^{-3}·10^{-2} = 10^6", Molekülanzahl als Exponent, x aus 3·2^{-x} = 0,375; „x^{-2} = −x²?", n aus zwei Wertepaaren, Vorzeichen von x^{-3} (Parität), Anzahl Lösungen x^{-2} = x², Atomkern im Stadionmodell, „kleinerer Exponent = kleinere Potenz?" (Basis < 1). Für Kl. 9 angehoben: Umkehraufgaben, Parameter, Fallunterscheidung nach Basis/Parität; L2/L3-Telegrammfragen („3^{-2} ist gleich …") zu vollständigen Sätzen |
| 9-potenzen-ganzzahlig | KEIN_AFB3 L5 (= wissenschaftliche Notation, jetzt Thema von 8-potenzen-negativ); KURZ L1–L4; DUENNER_WEG L1/L3/L4; L4 ≈ L3 | L4–L6 neu: Exponent von b in a³b⁴/(ab²), (x^{-2})³·x^10, n aus 2^n·2^{-5} = 2^{-1}, 3^{-2}·3⁵·3^{-1}, größte von vier Potenzen (MC), Termwert 6x^{-2}x³/(3x); Fehler „(2a)^{-2} = 2a^{-2}", n aus zwei Bedingungen, Umfang aus Fläche 2^{-4} m², 4^x = 8^{-2}, 2^{-10} gegen 10^{-3} begründet, k für Termwert 1; „(a+b)^{-1} = a^{-1}+b^{-1}?", a aus aq² = 18 und aq⁴ = 162, (−2)^n positiv und < 1 (Parität und Vorzeichen), Anzahl n mit 1 < 2^{-n} < 100, Halbierung rückwärts, Anzahl Werte > 0,2 |
| 9-potenzen-rational | KEIN_AFB3 L5; KOLLAPS L1/L2 (bleibt), KOLLAPS L4/L5; KURZ L1–L5; DUENNER_WEG L1/L2/L3/L5 | L4–L6 neu: √(x³)·∛x als x^k, r aus 16^r = 8, 8^{-2/3}·4^{3/2}, Würfeloberfläche aus Volumen 729, x aus x^{1/3}·x^{1/6} = 8, größte Bruchpotenz (MC); Fehler „8^{2/3} = 8²/3", r aus a^r = 4 und a^{r+1} = 32, Würfelvolumen aus Oberfläche 150, x^{3/4} = 27, Fehler „a^{1/2}·a^{1/3} = a^{1/6}", (x^{2/3})^{3/4}·x^{1/2}; „(−8)^{1/3} = −2 zulässig?" (Definitionsmenge, Widerspruch über 2/6), r aus zwei Wertepaaren, Anzahl Potenzen < √2, √(∛x) = ⁿ√x, x^{1/2} > x nur für 0 < x < 1, Kante bei doppeltem Volumen (+26 %) |
| 9-potenzgleichungen | KEIN_AFB3 L6; KOLLAPS L1/L2 (bleibt); KURZ L1–L4, L6; DUENNER_WEG L1–L6; L4 (x^{1/2} = 6 …) ≈ L3 | L4–L6 neu: n aus Lösung x = −2 von x^n = −32, Zinssatz aus drei Jahren (Faktor aus n Perioden), (x+1)⁴ = 16, Anzahl Lösungen 2x⁶+128 = 0, Kante bei doppeltem Volumen, a aus Lösung von x³ = a; Fehler „x⁴ = 81 ⇒ L = {3}", Bakterien nach 6 h aus Faktor über 4 h, k für genau eine Lösung, (2x−1)³ = −125, Wertverlust pro Jahr aus zwei Jahren, Gleichung mit genau einer Lösung (MC); „gerades n ⇒ immer zwei Lösungen?", Anfangswert aus Jahr 2 und Jahr 5, Anzahl a mit zwei Lösungen (Fallunterscheidung), a aus gemeinsamer Lösung zweier Gleichungen, Anzahl Lösungen x^{-4} = 16, „x⁶ = 64 hat sechs Lösungen?". L1–L3: „Positive Lösung?" → „Gib die positive Lösung an." |
| 9-wurzelgleichungen | KEIN_AFB3 L5/L6; KOLLAPS L1/L2 (bleibt); DUENNER_WEG L1/L2/L4; L3 #13–#15 mit quadrierter Gleichung bzw. „(Quadrieren, Probe!)" im Text, L4 #23 mit Rechenweg | L4–L6 neu: Definitionsmenge √(2x−10), √(x+4) = √(2x−1) ohne Hinweis, √(x²−9) = 4, a aus Lösung x = 11, Fallhöhe aus t = √(h/5) (Modell), 3√(x−2)+4 = 13; Fehler „Quadrieren ohne Isolieren", √(x+12) = x mit Scheinlösung, a aus zwei Lösungen von √(ax+b), Zahlenrätsel mit zwei Wurzeln, Anzahl Lösungen √(x−1) = 3−x, Fehler „√(x−2) = −3 ⇒ x = 11"; „nur eine Lösung möglich?" (Gegenbeispiel ±5), a aus Lösung 9 plus Scheinlösung, √(x+5)−√x = 1, leere Definitionsmenge (keine Lösung), b für Scheinlösung x = 1, „positiver Radikand ⇒ Lösung?". L3 #13–#15 ohne quadrierte Gleichung und ohne Verfahrensansage |

### 9-quadratwurzeln

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | L4: Verfahren wählen — gleichartige Wurzeln zusammenfassen, k eingeben |
| 21 | 4 | L4: Verfahren wählen — Nenner rational machen, 6/√3 = a√3 |
| 25 | 5 | L5: Fehler in Kette — √16 = ±4 (MC) |
| 26 | 5 | L5: zweischrittig — Seite aus Fläche 72, dann Umfang |
| 27 | 5 | L5: Parameter — a aus √a·√18 = 12 |
| 28 | 5 | L5: Fehler finden — √50 = 25√2 (MC) |
| 29 | 5 | L5: zweischrittig — teilweise radizieren, Umfang 10√3 |
| 30 | 5 | L5: Parameter — dritte binomische Formel mit Wurzeln |
| 31 | 6 | L6: Behauptung prüfen — √(a+b) = √a+√b (MC, Gegenbeispiel) |
| 32 | 6 | L6: Fallunterscheidung — √(x²) = −x genau für x ≤ 0 |
| 33 | 6 | L6: Umkehraufgabe — k = m²·5 im Intervall |
| 34 | 6 | L6: Behauptung prüfen — Produkt irrationaler Zahlen (MC) |
| 35 | 6 | L6: Verfahren übertragen — Nenner √5−2 mit dritter binomischer Formel |
| 36 | 6 | L6: Behauptung prüfen — Seite wächst um Faktor √2, nicht 2 |

### 7-potenzgesetze (Umzug nach Kl. 9)

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | L4: Potenzgesetze selbst wählen — drei Gesetze nacheinander |
| 20 | 4 | L4: Umkehraufgabe — Exponent gesucht |
| 21 | 4 | L4: Produkt potenzieren — Koeffizient |
| 22 | 4 | L4: Verfahren wählen — Basiswechsel 4 = 2² |
| 23 | 4 | L4: Modell aus Text — Quadratfläche als Potenz |
| 24 | 4 | L4: Verfahren wählen — gleicher Exponent, Basen dividieren |
| 25 | 5 | L5: Fehler in Kette — Exponenten multipliziert statt addiert (MC) |
| 26 | 5 | L5: Parameter aus zwei Bedingungen — a und n |
| 27 | 5 | L5: zweischrittig — Volumenverhältnis 3⁶/3³ |
| 28 | 5 | L5: Fehler finden — verschiedene Basen und Exponenten (MC) |
| 29 | 5 | L5: Exponentengleichung — 8^x = 2^12 |
| 30 | 5 | L5: Behauptung mit Zahl prüfen — 2^20/2^10 |
| 31 | 6 | L6: Gesetz begründen — Produktregel aus der Definition (MC) |
| 32 | 6 | L6: Behauptung prüfen — (a^m)^n = a^{(m^n)} (MC, Gegenbeispiel) |
| 33 | 6 | L6: Größenvergleich begründen — 2^300 gegen 3^200 (MC) |
| 34 | 6 | L6: Sonderfall — 2^n+2^n = 2^{2n} nur für n = 1 |
| 35 | 6 | L6: Verfahren übertragen — Ziffernzahl über 2^8·5^8 |
| 36 | 6 | L6: Umkehraufgabe im Kontext — Exponent gesucht, Zeit umrechnen |

### 8-potenzen-negativ (Umzug nach Kl. 9)

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | L4: Modell aus Text — Blattdicke, Einheiten umrechnen |
| 20 | 4 | L4: wissenschaftliche Notation prüfen (MC) |
| 21 | 4 | L4: Umkehraufgabe — n aus 5^n = 1/125 |
| 22 | 4 | L4: Modell aus Text — Tropfen pro Liter |
| 23 | 4 | L4: Größenvergleich — Quotient zweier Zehnerpotenz-Angaben |
| 24 | 4 | L4: Umkehraufgabe — n aus (1/4)^n = 64 |
| 25 | 5 | L5: Fehler in Kette — Minus im Exponenten als Vorzeichen (MC) |
| 26 | 5 | L5: zweischrittig — Verhältnis, dann Modellgröße |
| 27 | 5 | L5: Parameter aus zwei Bedingungen — a·n |
| 28 | 5 | L5: Fehler finden — Exponenten multipliziert (MC) |
| 29 | 5 | L5: Sachaufgabe — Molekülanzahl als Exponent |
| 30 | 5 | L5: Gleichung — Potenz isolieren, 0,125 = 2^{-3} |
| 31 | 6 | L6: Behauptung prüfen — x^{-2} = −x² (MC) |
| 32 | 6 | L6: Umkehraufgabe — n aus zwei Wertepaaren |
| 33 | 6 | L6: Fallunterscheidung — Vorzeichen von x^{-3} (MC) |
| 34 | 6 | L6: Sonderfall — Anzahl Lösungen x^{-2} = x² |
| 35 | 6 | L6: Sachaufgabe — Atomkern im Modell, Größenordnungen |
| 36 | 6 | L6: Behauptung prüfen — Monotonie bei Basis < 1 (MC) |

### 9-potenzen-ganzzahlig

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | L4: Term mit Variablen — getrennt kürzen |
| 20 | 4 | L4: Potenzgesetze wählen — Potenz einer Potenz, Produkt |
| 21 | 4 | L4: Umkehraufgabe — n aus 2^n·2^{-5} = 2^{-1} |
| 22 | 4 | L4: drei Faktoren, negative Exponenten |
| 23 | 4 | L4: Größenvergleich (MC) |
| 24 | 4 | L4: Termwert unabhängig von x |
| 25 | 5 | L5: Fehler in Kette — (2a)^{-2} (MC) |
| 26 | 5 | L5: Parameter aus zwei Bedingungen — n |
| 27 | 5 | L5: zweischrittig — Seite aus Fläche 2^{-4}, Umfang in cm |
| 28 | 5 | L5: Exponentengleichung — 4^x = 8^{-2} |
| 29 | 5 | L5: Größenvergleich begründen — 2^{-10} gegen 10^{-3} (MC) |
| 30 | 5 | L5: Parameter — Exponent 0 |
| 31 | 6 | L6: Behauptung prüfen — (a+b)^{-1} (MC, Gegenbeispiel) |
| 32 | 6 | L6: Umkehraufgabe — a aus zwei Bedingungen |
| 33 | 6 | L6: Fallunterscheidung — Parität und Vorzeichen (MC) |
| 34 | 6 | L6: Sonderfall — Anzahl n mit 1 < 2^{-n} < 100 |
| 35 | 6 | L6: Umkehraufgabe im Kontext — Halbierung rückwärts |
| 36 | 6 | L6: Größenvergleich — Basis < 1 gegen Basis > 1 |

### 9-potenzen-rational

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | L4: Schreibweise wählen — Wurzeln als Potenzen, Exponent addieren |
| 20 | 4 | L4: Umkehraufgabe — r aus 16^r = 8 |
| 21 | 4 | L4: zwei Bruchpotenzen auswerten |
| 22 | 4 | L4: Modell aus Text — Oberfläche aus Volumen |
| 23 | 4 | L4: Gleichung — Exponenten zusammenfassen |
| 24 | 4 | L4: Größenvergleich (MC) |
| 25 | 5 | L5: Fehler finden — Nenner als Division (MC) |
| 26 | 5 | L5: Parameter aus zwei Bedingungen — r |
| 27 | 5 | L5: zweischrittig — Volumen aus Oberfläche |
| 28 | 5 | L5: Gleichung — Kehrwert des Exponenten |
| 29 | 5 | L5: Fehler finden — Exponenten multipliziert (MC) |
| 30 | 5 | L5: Term — Potenz einer Potenz und Produkt |
| 31 | 6 | L6: Sonderfall Definitionsmenge — negative Basis (MC) |
| 32 | 6 | L6: Umkehraufgabe — r aus zwei Wertepaaren |
| 33 | 6 | L6: Größenvergleich — Exponenten bei gleicher Basis |
| 34 | 6 | L6: Umkehraufgabe — Wurzelexponent verschachtelter Wurzel |
| 35 | 6 | L6: Fallunterscheidung — x^{1/2} > x (MC) |
| 36 | 6 | L6: Behauptung prüfen — Kante bei doppeltem Volumen |

### 9-potenzgleichungen

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | L4: Umkehraufgabe — Exponent aus Lösung |
| 20 | 4 | L4: Modell aus Text — Zinssatz aus drei Perioden |
| 21 | 4 | L4: Verfahren wählen — Klammer als Ganzes |
| 22 | 4 | L4: Anzahl Lösungen selbst bestimmen |
| 23 | 4 | L4: Modell aus Text — Kante bei doppeltem Volumen |
| 24 | 4 | L4: Umkehraufgabe — a aus Lösung |
| 25 | 5 | L5: Fehler finden — zweite Lösung vergessen (MC) |
| 26 | 5 | L5: zweischrittig — Faktor aus 4 Perioden, dann 6 Perioden |
| 27 | 5 | L5: Parameter — genau eine Lösung |
| 28 | 5 | L5: Gleichung — Klammer, ungerader Exponent |
| 29 | 5 | L5: Sachaufgabe — Wertverlust aus zwei Perioden |
| 30 | 5 | L5: Anzahl Lösungen vergleichen (MC) |
| 31 | 6 | L6: Behauptung prüfen — Fallunterscheidung nach a (MC) |
| 32 | 6 | L6: Umkehraufgabe — Anfangswert aus zwei Zeitpunkten |
| 33 | 6 | L6: Fallunterscheidung — Anzahl a mit zwei Lösungen |
| 34 | 6 | L6: zweischrittig — gemeinsame Lösung zweier Gleichungen |
| 35 | 6 | L6: Sonderfall — negativer Exponent, Anzahl Lösungen |
| 36 | 6 | L6: Behauptung prüfen — Exponent ≠ Lösungsanzahl (MC) |

### 9-wurzelgleichungen

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | L4: Definitionsmenge |
| 20 | 4 | L4: Verfahren wählen — zwei Wurzeln, einmal quadrieren |
| 21 | 4 | L4: Verfahren wählen — Potenzgleichung nach Quadrieren |
| 22 | 4 | L4: Umkehraufgabe — a aus Lösung |
| 23 | 4 | L4: Modell aus Text — Fallhöhe |
| 24 | 4 | L4: Verfahren wählen — Wurzel isolieren |
| 25 | 5 | L5: Fehler in Kette — Quadrieren ohne Isolieren (MC) |
| 26 | 5 | L5: Wurzelgleichung mit Scheinlösung |
| 27 | 5 | L5: Parameter aus zwei Bedingungen — a |
| 28 | 5 | L5: Zahlenrätsel — zwei Wurzeln |
| 29 | 5 | L5: Anzahl Lösungen — Probe entscheidet |
| 30 | 5 | L5: Fehler finden — √ = −3 (MC) |
| 31 | 6 | L6: Behauptung prüfen — Anzahl Lösungen (MC, Gegenbeispiel) |
| 32 | 6 | L6: Umkehraufgabe — a aus Lösung, Scheinlösung nachweisen |
| 33 | 6 | L6: zwei Wurzeln — isolieren, binomische Formel |
| 34 | 6 | L6: Sonderfall — leere Definitionsmenge |
| 35 | 6 | L6: Parameter — b für Scheinlösung |
| 36 | 6 | L6: Behauptung prüfen — Radikand positiv ≠ Lösung (MC) |

## Prüfung

Für alle sieben Trainer: `tests/level_check.py --strict` ok (Duplikat-Warnung 9-potenzen-rational
#24 / 9-potenzen-ganzzahlig #23 „Welche der vier Zahlen ist am größten?" durch Umformulierung
behoben; Tipp-Lösungswert-Warnungen in 9-quadratwurzeln L1/L2 behoben), `tests/lehrplan_check.py
--strict` 0 Befunde, `tests/katex_check.py` 0 Fehler, `pytest tests/test_trainer.py -k <stem>`
je 7 passed, Bilder L5/L6 angesehen.

## Offene Punkte

- KOLLAPS L1/L2 in 8-potenzen-negativ, 9-potenzen-rational, 9-potenzgleichungen und
  9-wurzelgleichungen bleibt laut Auftrag bestehen (Stufe 1–3 nicht neu geschrieben).
- Bei MC-Aufgaben ist die richtige Option meist die längste (Begründung enthalten); die
  Engine mischt die Reihenfolge, aber die Länge bleibt ein Hinweis.

## Block A2 — Quadratische Funktionen/Gleichungen, Wachstum, LGS, Bruchgleichungen

Abgrenzung der fünf Trainer: 9-quadratische-gleichungen = Gleichungen lösen, Lösbarkeit,
Sachaufgaben mit Gleichung; 9-quadratische-funktionen = Graph, Scheitel, Term, Transformation,
Sachfunktion; 8-lgs (Umzug 8 → 9) = 2×2-Systeme, Sonderfälle, Sachaufgaben mit zwei Unbekannten;
8-bruchgleichungen (Umzug 8 → 9) = Definitionsmenge, Scheinlösung, Sachaufgaben
(Geschwindigkeit/Arbeit); 9-exponentielles-wachstum = Faktor, Prozent, Verdopplung/Halbwertszeit
über Tabelle, Vergleich linear/exponentiell (kein Logarithmus, kein e).
Pflicht-Fix Lehrplan-Gate: 9-quadratische-funktionen #22 (alt) machte die „Probe über die
Ableitung f'(x) = 4x − 8“ — die Aufgabe ist mit L4 komplett neu; Scheitel wird überall über
Scheitelpunktform/Symmetrie/Koeffizienten bestimmt.

| Trainer | Audit-Befund | Geändert |
|---|---|---|
| 9-quadratische-funktionen | KEIN_AFB3 L5/L6; KOLLAPS L3/L4; DUENNER_WEG L1–L4/L6; #22 Ableitung; #30 Rückverweis; L3 #16 Formel im Text | L4–L6 neu: a aus Scheitel und Punkt, y-Achsenabschnitt aus Nullstellen, Maximum ohne Verfahrensansage, Term aus Wertetabelle (MC), Nullstellen nach Verschiebung, b aus Scheitelstelle; Brückenbogen 40 m/20 m → Höhe bei 10 m, Wurf von Plattform (Scheitelzeit und Aufprall), Fehler in Scheitelrechnung (Vorzeichen, MC), a und c aus zwei Punkten, Zaun an Hauswand (450 m²), Wasserstrahl trifft Boden; „Scheitel unter Achse ⇒ zwei Nullstellen?“ (MC), kleinstes c ohne Nullstelle (Fallunterscheidung), f(4) aus Symmetrieachse + Nullstelle + Achsenabschnitt, Monotoniebereich (MC), c aus Scheitel, k für Berührung Parabel/Gerade. L1 #5 entdoppelt (x²+1), L3 #16 ohne Formelansage, L3 #17 andere Funktion |
| 9-quadratische-gleichungen | KEIN_AFB3 L5/L6; DUENNER_WEG L1; L3 #13 „mit pq-Formel“, #17 Formel-Abfrage; L4 #21 „Zuerst durch 2 teilen“ | L4–L6 neu: x²−x−12 (Verfahren frei), (x−3)² = 2x−3 (erst ordnen), Produkt aufeinanderfolgender Zahlen 132, p aus Lösung x = 2, 3x²+6x = 0 (MC, Lösung 0 nicht verlieren), Rechteck 5 cm länger; Fehler in pq-Kette (−q bei negativem q, MC), Ball vom Turm eine Sekunde vor Aufprall, p aus Lösungen 2 und −5, Summe 14/Produkt 45, „durch x geteilt — welche Lösung fehlt?“, Bilderrahmen 20×30 → 1200 cm²; „q < 0 ⇒ zwei Lösungen?“ (MC), Anzahl c ∈ [−3; 5] mit zwei Lösungen (Fallunterscheidung), c aus Lösungen −3 und 0,5 bei 2x², (2x−1)² = (x+3)² ohne Ausmultiplizieren, (x+3)² = 0 gegen = 1 (MC), m für genau eine Lösung (Parameter aus Diskriminante). L1 #2 entdoppelt (Textform), L3 #13 ohne Formelansage, #17 Formel-MC → Gleichung x²+3x−10 |
| 9-exponentielles-wachstum | KEIN_AFB3 L5; KOLLAPS L4/L5; DUENNER_WEG L1–L3/L5; L2 #8, L3 #13 Formel im Text; L3 #15 Rückverweis „wie Aufg. 14“; L6 #34/#35 Logarithmus bzw. 72er-Regel | L4–L6 neu: q aus 200 → 288 in 2 Jahren, Term aus Tabelle 5/15/45/135 (MC), Anfangskapital aus 5408 € rückwärts, Prozentsatz aus 1000 → 512 in 3 Jahren, linear 100+30n gegen 100·1,2ⁿ (Tabelle), 96 mg → 12 mg bei HWZ 6 h; Fehler „Wurzel halbiert“ (MC), Medikament 20 % Abbau erstmals unter 200 mg, Anfangswert aus t = 1 und t = 3, Zuwachs im dritten Jahr (2205), Zinseszins gegen einfache Zinsen (5,45 €), Halbwertszeit aus 12,5 % nach 24 Tagen; „100 % in 10 Jahren = 10 % pro Jahr?“ (MC, 1,1¹⁰ ≈ 2,59), Jahresrate bei Verdreifachung in 4 Jahren (31,6 %), Stadt A überholt Stadt B (Tabelle), „4 × 25 % = weg?“ (MC, 0,75⁴), Zinssatz aus 1000 → 1728 in 3 Jahren, q aus N(3) = 27 und erstes t unter 20. L1 #6 → Faktor bei Verdreifachung, L2 #8/#10 und L3 #13 ohne Formel im Text, L3 #15 eigenständig (Motorrad 8000 €, 20 %) |
| 8-lgs (Umzug 8 → 9) | KEIN_AFB3 L5/L6; KOLLAPS L3/L4; L4–L6 nur Rechenroutinen mit Verfahrensansage („Addition liefert“, „Einsetzen x = y+1“), L6 #31/#32 Definitionsfragen | L4–L6 neu: 3x+2y = 16 / 5x−2y = 8 (Verfahren frei), 2x+5y = 1 / 3x−2y = 11 (Vervielfachen), Eiskugeln/Waffeln, a aus Lösung x = 9, LGS aus Zahlenrätsel aufstellen (MC), y = 2x−1 / 3x+2y = 12; Fehler in Additionskette (Vorzeichen, MC), Boot 36 km (Eigengeschwindigkeit), a für keine Lösung, Saftmischung 20 %/60 % → 45 %, zweistellige Zahl mit Quersumme 11, Tarifvergleich 200 Minuten; „immer genau eine Lösung?“ (MC), a mit keiner Lösung bei x+ay = 1 / ax+4y = 2 (Fallunterscheidung a = ±2), identische Geraden grafisch deuten (MC), b aus Lösungspaar, Parabel ax²+bx durch zwei Punkte → f(3), c für unendlich viele Lösungen. Für Kl. 9 angehoben: Parameter-LGS, Lösbarkeit/Lösungsvielfalt, Mischungs- und Bewegungsaufgaben; L1–L3 unverändert |
| 8-bruchgleichungen (Umzug 8 → 9) | KEIN_AFB3 L5/L6; KOLLAPS L2/L3; L2 #7 Verfahrensfrage, L3 #13/#14 gleiche Gleichung; L4 #21 MC-Antwort an Länge erkennbar; L5 nur Routinen, L6 #34/#35 Wurzelausdrücke | L5/L6 neu: Fehler beim Ausmultiplizieren (MC), Scheinlösung → 0 Lösungen, zwei Pumpen (6 h/3 h), Radfahrer 60 km mit 5 km/h mehr (quadratisch), a aus Lösung x = 5, „Mia oder Nils?“ (Probe entscheidet); „höchstens eine Lösung?“ (MC, Gegenbeispiel x/2 = 2/x), (x²−9)/(x−3) = x+3 → Q \ {3} (MC), b für Scheinlösung x = 3, a für unendlich viele Lösungen (Fallunterscheidung), zwei Drucker (12 min / 20 min), a aus Lösung x = 4 und a+b = 6 (LGS). Für Kl. 9 angehoben: Bruchgleichungen mit quadratischem Kern, Definitionslücke als Lösungsfall, Parameter. L2 #7 → Gleichung lösen, L3 #13 → x/4 + x/6 = 5, L4 #21 Optionen gleich lang, #24 Lösungsweg bereinigt |

### 9-quadratische-funktionen

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | L4: Umkehraufgabe — Streckfaktor aus Scheitel und Punkt |
| 20 | 4 | L4: Term aus Nullstellen, y-Achsenabschnitt |
| 21 | 4 | L4: Verfahren wählen — größter Funktionswert |
| 22 | 4 | L4: Modell aus Tabelle — Term erkennen (MC) |
| 23 | 4 | L4: Transformation — Nullstellen nach Verschiebung |
| 24 | 4 | L4: Umkehraufgabe — b aus Scheitelstelle |
| 25 | 5 | L5: Sachaufgabe zweischrittig — Brückenbogen |
| 26 | 5 | L5: Sachaufgabe zweischrittig — Scheitelzeit und Aufprall |
| 27 | 5 | L5: Fehler finden — Vorzeichen des Scheitels (MC) |
| 28 | 5 | L5: Parameter aus zwei Bedingungen — a und c |
| 29 | 5 | L5: Sachaufgabe — Zaun an Hauswand, Maximum |
| 30 | 5 | L5: Sachaufgabe — Wasserstrahl, Nullstelle |
| 31 | 6 | L6: Behauptung prüfen — Scheitel unter Achse (MC) |
| 32 | 6 | L6: Fallunterscheidung — Anzahl Nullstellen je c |
| 33 | 6 | L6: Umkehraufgabe — Term aus Symmetrieachse und Punkten |
| 34 | 6 | L6: Monotonie — Bereich bestimmen (MC) |
| 35 | 6 | L6: Umkehraufgabe — c aus Scheitel |
| 36 | 6 | L6: Sonderfall — Berührung Parabel/Gerade |

### 9-quadratische-gleichungen

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | L4: Verfahren wählen — Faktorisieren oder Formel |
| 20 | 4 | L4: Verfahren wählen — erst ordnen |
| 21 | 4 | L4: Modell aus Text — Produkt aufeinanderfolgender Zahlen |
| 22 | 4 | L4: Umkehraufgabe — p aus Lösung |
| 23 | 4 | L4: Verfahren wählen — Ausklammern (MC) |
| 24 | 4 | L4: Modell aus Text — Rechteckfläche |
| 25 | 5 | L5: Fehler in Kette — −q bei negativem q (MC) |
| 26 | 5 | L5: Sachaufgabe zweischrittig — Aufprall, dann Höhe |
| 27 | 5 | L5: Parameter aus zwei Bedingungen — p aus Lösungen |
| 28 | 5 | L5: Zahlenrätsel — Summe und Produkt |
| 29 | 5 | L5: Fehler finden — Division durch x |
| 30 | 5 | L5: Sachaufgabe — Rahmenbreite |
| 31 | 6 | L6: Behauptung prüfen — q < 0 (MC) |
| 32 | 6 | L6: Fallunterscheidung — Anzahl c mit zwei Lösungen |
| 33 | 6 | L6: Umkehraufgabe — c aus Lösungen bei a = 2 |
| 34 | 6 | L6: Verfahren übertragen — gleiche Quadrate |
| 35 | 6 | L6: Sonderfall — doppelte Lösung gegen zwei (MC) |
| 36 | 6 | L6: Parameter — m für genau eine Lösung |

### 9-exponentielles-wachstum

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | L4: Umkehraufgabe — Faktor aus zwei Werten |
| 20 | 4 | L4: Modell aus Tabelle — Term erkennen (MC) |
| 21 | 4 | L4: Umkehraufgabe — Anfangskapital |
| 22 | 4 | L4: Umkehraufgabe — Prozentsatz aus drei Perioden |
| 23 | 4 | L4: Vergleich linear/exponentiell — Tabelle |
| 24 | 4 | L4: Halbwertszeit — Zeitpunkt aus Halbierungen |
| 25 | 5 | L5: Fehler in Kette — Wurzel statt Hälfte (MC) |
| 26 | 5 | L5: Sachaufgabe zweischrittig — erstmals unter Schwelle |
| 27 | 5 | L5: Parameter aus zwei Bedingungen — Anfangswert |
| 28 | 5 | L5: Sachaufgabe zweischrittig — Zuwachs im dritten Jahr |
| 29 | 5 | L5: Vergleich — Zinseszins gegen einfache Zinsen |
| 30 | 5 | L5: Umkehraufgabe — Halbwertszeit aus Restanteil |
| 31 | 6 | L6: Behauptung prüfen — Prozentsätze addieren (MC) |
| 32 | 6 | L6: Umkehraufgabe — Jahresrate aus Verdreifachung |
| 33 | 6 | L6: Vergleich zweier Bestände — Tabelle |
| 34 | 6 | L6: Behauptung prüfen — Zerfall endet nie (MC) |
| 35 | 6 | L6: Umkehraufgabe — Zinssatz aus drei Perioden |
| 36 | 6 | L6: Parameter, dann Schwelle — q aus N(3) |

### 8-lgs (Umzug nach Kl. 9)

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | L4: Verfahren wählen — Addition |
| 20 | 4 | L4: Verfahren wählen — Vervielfachen |
| 21 | 4 | L4: Modell aus Text — Preise |
| 22 | 4 | L4: Umkehraufgabe — a aus Lösung |
| 23 | 4 | L4: Modell aus Text — LGS aufstellen (MC) |
| 24 | 4 | L4: Verfahren wählen — Einsetzen |
| 25 | 5 | L5: Fehler in Kette — Vorzeichen (MC) |
| 26 | 5 | L5: Sachaufgabe zweischrittig — Boot |
| 27 | 5 | L5: Parameter — a für keine Lösung |
| 28 | 5 | L5: Sachaufgabe — Mischung |
| 29 | 5 | L5: Zahlenrätsel — Ziffern vertauschen |
| 30 | 5 | L5: Sachaufgabe — Tarifvergleich |
| 31 | 6 | L6: Behauptung prüfen — immer genau eine Lösung (MC) |
| 32 | 6 | L6: Fallunterscheidung — a = ±2 |
| 33 | 6 | L6: Sonderfall — identische Geraden grafisch (MC) |
| 34 | 6 | L6: Umkehraufgabe — b aus Lösungspaar |
| 35 | 6 | L6: Transfer — Parabel durch zwei Punkte |
| 36 | 6 | L6: Sonderfall — c für unendlich viele Lösungen |

### 8-bruchgleichungen (Umzug nach Kl. 9)

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | L5: Fehler in Kette — Klammer ausmultiplizieren (MC) |
| 26 | 5 | L5: Scheinlösung — Anzahl Lösungen |
| 27 | 5 | L5: Sachaufgabe — zwei Pumpen |
| 28 | 5 | L5: Sachaufgabe zweischrittig — Radfahrer (quadratisch) |
| 29 | 5 | L5: Umkehraufgabe — a aus Lösung |
| 30 | 5 | L5: Fehler finden — Probe entscheidet |
| 31 | 6 | L6: Behauptung prüfen — höchstens eine Lösung (MC) |
| 32 | 6 | L6: Sonderfall — Definitionslücke, unendlich viele (MC) |
| 33 | 6 | L6: Umkehraufgabe — b für Scheinlösung |
| 34 | 6 | L6: Fallunterscheidung — a für unendlich viele Lösungen |
| 35 | 6 | L6: Sachaufgabe — zwei Drucker, Umkehr |
| 36 | 6 | L6: Parameter aus zwei Bedingungen — a mit LGS |

Prüfung Block A2: `level_check --strict` ok ohne Warnung (inkl. neuer MC-Längen-Warnung; Befund
8-bruchgleichungen #21 durch gleich lange Optionen behoben), `lehrplan_check --strict` 0 Befunde,
`katex_check` 0 Fehler, `pytest -k <stem>` je 7 passed, Bilder L5/L6 angesehen, alle Lösungen mit
Wolfram|Alpha nachgerechnet.
