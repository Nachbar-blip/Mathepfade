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
| 26 | 5 | L5: Sachaufgabe zweischrittig — Tunnelprofil, Lkw-Höhe |
| 27 | 5 | L5: Fehler finden — Vorzeichen des Scheitels (MC) |
| 28 | 5 | L5: Parameter aus zwei Bedingungen — a und c |
| 29 | 5 | L5: Sachaufgabe — Zaun an Hauswand, Maximum |
| 30 | 5 | L5: Sachaufgabe — Wasserstrahl, Nullstelle |
| 31 | 6 | L6: Behauptung prüfen — Scheitel unter Achse (MC) |
| 32 | 6 | L6: Fallunterscheidung nach Vorzeichen von a — Nullstellen bei festem Scheitel (MC) |
| 33 | 6 | L6: Umkehraufgabe — Term aus Symmetrieachse und Punkten |
| 34 | 6 | L6: Monotonie — Bereich bestimmen (MC) |
| 35 | 6 | L6: Parabelschar — t, für das der Scheitel auf y = −4 liegt |
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
| 27 | 5 | L5: Sachaufgabe zweischrittig — Rechteck aus Umfang und Fläche |
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
| 35 | 6 | L6: Umkehraufgabe — Faktor aus t = 2 und t = 5, Wert bei t = 7 |
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
| 34 | 6 | L6: Sachaufgabe mit Widerspruch — passender Betrag (Sonderfall) |
| 35 | 6 | L6: Modell aus Text — Altersrätsel mit Zeitverschiebung |
| 36 | 6 | L6: Fallunterscheidung — Anzahl a mit genau einer Lösung (a = ±1 gesondert) |

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
| 35 | 6 | L6: Fallunterscheidung — b für genau eine Lösung (quadratischer Kern) |
| 36 | 6 | L6: Parameter aus zwei Bedingungen — a mit LGS |

Prüfung Block A2: `level_check --strict` ok ohne Warnung (inkl. neuer MC-Längen-Warnung; Befund
8-bruchgleichungen #21 durch gleich lange Optionen behoben), `lehrplan_check --strict` 0 Befunde,
`katex_check` 0 Fehler, `pytest -k <stem>` je 7 passed, Bilder L5/L6 angesehen, alle Lösungen mit
Wolfram|Alpha nachgerechnet.

Review 2026-09-27 (Block A2): Dubletten entfernt (qf #26 Ballwurf → Tunnel, qf #32 → Vorzeichen-Fallunterscheidung, qg #27 → Rechteck statt Doppel zu #17, lgs #35 → Altersrätsel, bg #35 → b für genau eine Lösung), L6 auf AFB III (qf #35 Parabelschar, lgs #34/#36 Widerspruch bzw. Anzahl a, ew #35 Faktor aus zwei nicht benachbarten Werten), MC-Optionen angeglichen (bg #32, qg #35, lgs #31). Gates erneut grün, Bilder L6 angesehen, neue Zahlen mit Wolfram.

## Block B — Geometrie und Stochastik (Commits bfc611e Geometrie, s. u. Stochastik)

Lesart Kl. 9 Geometrie/Stochastik: L4 = Verfahren selbst wählen (sin/cos/tan; 1./2. Strahlensatz;
Zerlegen oder ½·a·b·sin γ), Modell aus Text- oder Skizzenbeschreibung, Umkehraufgabe (Winkel aus
Seiten, Streckfaktor aus Flächen, Radius aus Volumen); L5 = zweischrittige Sachaufgabe ohne Weg
(Höhe über zwei Winkel, zusammengesetzter Körper), Fehler in vorgelegter Rechnung (sin/cos
vertauscht, Strahlensatz mit AA' statt SA', Quartil falsch, r² statt r³), Größe aus zwei
Bedingungen; L6 = Behauptung begründet prüfen (MC mit Gegenbeispiel), Sonderfall (X-Figur,
k = 1, Median bei gerader Anzahl, Q₁ = Median, Fläche 0), Umkehraufgabe (Daten aus Boxplot,
Streckfaktor aus Flächen), Fallunterscheidung k² gegen k³. Niveau: TH-Lehrplan 2.3.3/2.3.4 —
kein Sinussatz/Kosinussatz, keine Vektoren, keine Standardabweichung/Varianz/Erwartungswert.
Jede Lösung mit Wolfram|Alpha nachgerechnet; Bilder L5/L6 per `tests/bild.py` angesehen.

Abgrenzung: 9-trig-rechtwinkliges-dreieck = Definitionen, Seiten/Winkel im rechtwinkligen
Dreieck, Höhe über zwei Winkel; 9-flaechenberechnung-determinante (jetzt „Flächen im
Koordinatensystem") = Flächen aus Punkten (achsenparallel, Zerlegen), ½·a·b·sin γ, Parameter;
9-raumgeometrie-anwendungen = zusammengesetzte Körper, Einheiten, k³; 8-strahlensatz = 1./2.
Strahlensatz, Umkehrung, X-Figur, Schatten/Fluss; 8-aehnlichkeit-streckung = Streckfaktor,
k/k²-Regeln, Ähnlichkeit von Figuren; 9-stoch-boxplot = Median, Quartile, IQR, Ausreißer;
9-stoch-haeufigkeiten = absolute/relative Häufigkeit als Schätzung, Mittelwert/Median/Modalwert.

| Trainer | Audit-Befund | Geändert |
|---|---|---|
| 9-raumgeometrie-anwendungen | KEIN_AFB3 L5/L6; KOLLAPS L2/L3, L3/L4, L4/L5; DUENNER_WEG L1/L2/L4/L5 | L4–L6 neu: Durchmesser aus 300 l und Höhe (Umkehr), Halle mit Satteldach (Modell aus Text), Würfelkante aus 512 l, Säule streichen ohne Boden (Teilflächen wählen), Trichter leerlaufen (Zeit aus Volumen), Wachsmengen Zylinder gegen Kegel (MC, Vergleich als Leistung); Fehler r² statt r³ (MC), Silo Zylinder + Kegel mit Dichte, Oberfläche aus V = 2a³ (zwei Bedingungen), Fehler Mantel ohne Deckflächen (MC), Aquarium mit Steinen (Verdrängung), Zylinderhöhe bei Kugelvolumen; „doppelter Radius, halbe Höhe" (MC, Behauptung), Tankmodell 1:20 (k³), Lackfläche 1:25 (k²), Kugelradius aus Wasseranstieg (Umkehr), „Kegel größer als Pyramide, weil rund" (MC), ähnliche Kegel k³. L1–L3 unverändert |
| 9-trig-rechtwinkliges-dreieck | KEIN_AFB3 L5/L6; DUENNER_WEG L2–L4; L5 #25–#30 = L2/L3-Muster mit Formel im Tipp, L6 #33/#36 Einschritt | L5/L6 neu: Fehler sin statt cos für Ankathete (MC), Turmhöhe über zwei Höhenwinkel 28°/42°, Rampe 8 % über 25 m (Winkel dann Höhe), Fehler Katheten im Tangens vertauscht (MC), Sparrenlänge aus Hausbreite und Neigung, Dreiecksfläche aus c und α; „sin α = cos β" begründen (MC), tan α = 3 sin α (Gleichung, cos α = 1/3), Ballonhöhe zwischen zwei Beobachtern, Basis des gleichschenkligen Dreiecks aus Schenkel und Spitzenwinkel, „sin α = 1,2 möglich?" (MC, Sonderfall), Drachenhöhe mit Handhöhe. L1–L4 unverändert (L4 bereits Anwendungen) |
| 9-flaechenberechnung-determinante → „Flächen im Koordinatensystem" | KEIN_AFB3 L5/L6; KOLLAPS L2/L3, L3/L4, L4/L5; DUENNER_WEG L2/L5/L6; Bestand war Sinussatz/Kosinussatz/Heron/Umkreis (Kl. 10, TH 2.3.3 nicht Kl. 9) | Alle 36 neu nach Plan: L1 achsenparallele Rechtecke/Dreiecke aus Gitterpunkten; L2 Grundseite auf Achse oder achsenparallel, Höhe ablesen, Parallelogramm, Trapez; L3 Zerlegen (umgebendes Rechteck minus Eckdreiecke), Viereck über Diagonale; L4 ½·a·b·sin γ (spitz und stumpf), b aus Fläche, Trapez aus Punkten erkennen, allgemeines Viereck zerlegen, Parallelogramm mit Winkel (MC); L5 fehlende Koordinate aus Fläche, Fehler „drittes Eckdreieck vergessen" (MC), Seite aus Fläche und Winkel, Trapezparameter c, Fehler „Winkel nicht eingeschlossen" (MC), Viereck mit negativen Koordinaten; L6 „drei Punkte bilden ein Dreieck?" (Fläche 0, MC), t für gleiche Fläche wie Rechteck, x mit Fläche 0 (Punkt auf Gerade), „Koordinaten verdoppeln = Fläche verdoppeln?" (k², MC), Winkel aus Fläche mit Sonderfall 150°, k aus Vierecksfläche. Titel, THEMA_CONFIG.name, Kommentar Zeile 3, Index-Name geändert; Dateiname bleibt |
| 8-strahlensatz (Umzug 8 → 9) | KEIN_AFB3 L5/L6; KOLLAPS L4/L5; L4–L6 = Einsetzen mit Ansatz im Tipp, L4 #23 unlesbar | L4–L6 neu: Schattenlänge bei Laterne (Gleichung mit s auf beiden Seiten), A'B' mit SA' = SA + AA' (Falle AA'), AB aus Streckfaktor (Umkehr), Flussbreite über Peilung (Modell aus Text), Parallele im Dreieck mit Scheitel C, richtiger Ansatz wählen (MC); Fehler AA' statt SA' (MC), Leitersprosse (Scheitel oben), Diagonalenabschnitt im Trapez (zwei Bedingungen), Fehler AA'/SA' im 2. Strahlensatz (MC), Sektglas (Kegelquerschnitt), x aus x/(x+8) = 1/3; dritte Form AA'/BB' = SA/SB begründen (MC), X-Figur (Sonderfall Scheitel zwischen Parallelen), Trapezfläche über k² (Fallunterscheidung), Mittelparallele begründen (MC), Abstand zur Laterne aus Schattenlänge (Umkehr), x für Parallelität (Umkehrung des Strahlensatzes). Für Kl. 9 angehoben: Gleichungen mit Unbekannter auf beiden Seiten, k²-Bezug, Umkehrsatz; L1–L3 unverändert, „schliessen" → „schließen" |
| 8-aehnlichkeit-streckung (Umzug 8 → 9) | KEIN_AFB3 L5; DUENNER_WEG L2/L4; L5/L6 = Einsetzen von k oder k² mit Formel im Tipp | L5/L6 neu: Fehler „Fläche mal k" (MC), Fläche aus zwei Umfängen (zwei Bedingungen), 5-12-13-Dreieck über Umfang zu Fläche, Fehler „Winkel verdoppeln sich" (MC), Posterbreite aus Fläche (k aus k²), dritte Seite für Ähnlichkeit; „gleicher Umfang ⇒ kongruent" (k = 1, MC), Umfang bei vervierfachter Fläche (Umkehr), Bildpunkt bei Streckung vom Ursprung (k aus P und P'), „alle Rechtecke ähnlich?" (MC, Gegenbeispiel), kürzeste Seite aus Flächenverhältnis 18:50, Umfang bei Verkleinerung 48 → 27 (k < 1). Für Kl. 9 angehoben: Rückrechnung k aus k², Ähnlichkeitskriterien, Koordinaten; L1–L4 unverändert bis auf echte Umlaute (Ähnlich, groß, Maßstab, heißt; THEMA_KEY bleibt ASCII) |
| 9-stoch-boxplot | KEIN_AFB3 L5; DUENNER_WEG L1–L6; L5 = L2/L3-Muster mit Hälften im Text, L6 #32/#35 Einschritt; #11 Rückverweis „Gleiche:"; L4 #19/#20 mit Tukey-Formel im Text, #23 Tipp mit Lösungswert | L5/L6 neu: IQR aus ungeordneter Reihe, Fehler „Median zur unteren Hälfte gezählt" (MC), Anzahl Ausreißer aus Rohdaten (Regel nur benannt), x aus Median bei gerader Anzahl, Boxplot-Vergleich zweier Klassen (MC, Auswahl als Leistung), Mittelwert minus Median aus ungeordneter Reihe; „gleicher Boxplot ⇒ gleiche Daten?" (MC, Gegenbeispiel), x mit Median = Mittelwert (Gleichung), Mittelwert aus den fünf Kennwerten eines Boxplots (Umkehr, Rückrechnung der Werte), Q₁ = Median (Sonderfall, MC), Robustheit des Medians gegen Ausreißer (Differenz der Anstiege), „symmetrischer Boxplot ⇒ Median = Mittelwert?" (MC, Gegenbeispiel). #11 mit vollständiger Datenreihe; L4 #19/#20 ohne Formel im Text, #23 Tipp ohne Lösungswert |
| 9-stoch-haeufigkeiten | KEIN_AFB3 L5/L6; KOLLAPS L4/L5; DUENNER_WEG L1/L2/L4–L6; L4 #20/#24, L5 #27/#29, L6 #33 = Standardabweichung/Varianz/Erwartungswert (nicht TH Kl. 9); #16/#17 Rückverweis „wie oben" | L4–L6 neu: n aus H und h (Umkehr), Hochrechnen mit relativer Häufigkeit als Schätzwert, Anzahl Fünfen aus Durchschnitt 3,0 (Gleichung), Kenngröße für „typisches Alter" wählen (MC), Anteil aus Klassen zusammenfassen, Bestehensquote zweier Kurse (nicht mitteln); Fehler 0,4 = 4 % (MC), rote Felder aus 620/2000 (Schätzung → Modell), fehlender Wert aus Mittelwert, Fehler Median ohne Ordnen (MC), Klassengröße aus zwei relativen Häufigkeiten (Gleichung), gewichteter Durchschnitt zweier Klassen; Ausgleichs-Fehlschluss beim Münzwurf (MC), 0 weitere Sechsen für h = 1/6 (Sonderfall), Umfang der zweiten Umfrage aus Gesamtanteil (Gleichung), „Mittelwert ist immer ein Wert der Reihe?" (MC, Gegenbeispiel), Median nach Rückrechnung des sechsten Werts, Anzahl Einsen aus drei Bedingungen. #16/#17 mit vollständiger Notenverteilung |

### 9-raumgeometrie-anwendungen

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | L4: Umkehraufgabe — Durchmesser aus Volumen und Höhe |
| 20 | 4 | L4: Modell aus Text — Quader plus Dreiecksprisma |
| 21 | 4 | L4: Umkehraufgabe — Kante aus Würfelvolumen in Litern |
| 22 | 4 | L4: Verfahren wählen — Mantel plus eine Deckfläche |
| 23 | 4 | L4: Modell aus Text — Kegelvolumen, dann Zeit |
| 24 | 4 | L4: Vergleich Zylinder/Kegel (MC, Auswahl als Leistung) |
| 25 | 5 | L5: Fehler in Rechnung — r² statt r³ (MC) |
| 26 | 5 | L5: zusammengesetzter Körper mit Dichte |
| 27 | 5 | L5: Größe aus zwei Bedingungen — Oberfläche aus V = 2a³ |
| 28 | 5 | L5: Fehler in Rechnung — Deckflächen vergessen (MC) |
| 29 | 5 | L5: zweischrittig — Wasserstand nach Verdrängung |
| 30 | 5 | L5: Größe aus zwei Bedingungen — Zylinderhöhe bei Kugelvolumen |
| 31 | 6 | L6: Behauptung prüfen — 2r und h/2 (MC) |
| 32 | 6 | L6: Fallunterscheidung — Volumen mit k³ |
| 33 | 6 | L6: Fallunterscheidung — Fläche mit k² |
| 34 | 6 | L6: Umkehraufgabe — Kugelradius aus Wasseranstieg |
| 35 | 6 | L6: Behauptung prüfen — Kegel gegen Pyramide (MC) |
| 36 | 6 | L6: ähnliche Körper — Volumen mit k³ aus Höhen |

### 9-trig-rechtwinkliges-dreieck

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | L5: Fehler in Rechnung — sin statt cos (MC) |
| 26 | 5 | L5: Höhe über zwei Winkel |
| 27 | 5 | L5: zweischrittig — Steigung in Winkel, dann Höhe |
| 28 | 5 | L5: Fehler in Rechnung — Katheten im Tangens vertauscht (MC) |
| 29 | 5 | L5: Sachaufgabe ohne Weg — Sparren aus Hausbreite |
| 30 | 5 | L5: zweischrittig — beide Katheten, dann Fläche |
| 31 | 6 | L6: Behauptung begründen — sin α = cos β (MC) |
| 32 | 6 | L6: Gleichung — tan α = 3 sin α |
| 33 | 6 | L6: Höhe zwischen zwei Beobachtern |
| 34 | 6 | L6: Verfahren übertragen — gleichschenkliges Dreieck |
| 35 | 6 | L6: Sonderfall — sin α > 1 unmöglich (MC) |
| 36 | 6 | L6: Sachaufgabe — Schnur plus Handhöhe |

### 9-flaechenberechnung-determinante (Flächen im Koordinatensystem)

| id | Level | Kriterium |
|---|---|---|
| 1–6 | 1 | L1: achsenparallele Figuren aus Gitterpunkten, ein Schritt (2 MC) |
| 7–12 | 2 | L2: Grundseite auf Achse/achsenparallel, Höhe ablesen; Parallelogramm, Trapez (1 MC) |
| 13–18 | 3 | L3: Zerlegen — umgebendes Rechteck minus Eckdreiecke; Viereck über Diagonale (1 MC) |
| 19 | 4 | L4: Verfahren wählen — ½·a·b·sin γ |
| 20 | 4 | L4: Umkehraufgabe — Grundseite aus Fläche |
| 21 | 4 | L4: Trapez aus Punkten erkennen |
| 22 | 4 | L4: allgemeines Viereck zerlegen |
| 23 | 4 | L4: ½·a·b·sin γ mit stumpfem Winkel |
| 24 | 4 | L4: Parallelogramm mit Winkel (MC) |
| 25 | 5 | L5: fehlende Koordinate aus Fläche |
| 26 | 5 | L5: Fehler in vorgelegter Zerlegung (MC) |
| 27 | 5 | L5: Seite aus Fläche und eingeschlossenem Winkel |
| 28 | 5 | L5: Trapezparameter aus Fläche |
| 29 | 5 | L5: Fehler — Winkel nicht eingeschlossen (MC) |
| 30 | 5 | L5: Viereck mit negativen Koordinaten zerlegen |
| 31 | 6 | L6: Behauptung prüfen — Fläche 0, Punkte auf Gerade (MC) |
| 32 | 6 | L6: Parameter für gleiche Flächen |
| 33 | 6 | L6: Punkt auf Gerade ⇔ Fläche 0 |
| 34 | 6 | L6: Behauptung prüfen — Koordinaten verdoppeln, k² (MC) |
| 35 | 6 | L6: Winkel aus Fläche, Sonderfall zweier Lösungen |
| 36 | 6 | L6: Parameter aus Vierecksfläche |

### 8-strahlensatz (Umzug nach Kl. 9)

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | L4: Modell aus Text — Schattenlänge, Unbekannte auf beiden Seiten |
| 20 | 4 | L4: Verfahren wählen — 2. Strahlensatz mit SA' = SA + AA' |
| 21 | 4 | L4: Umkehraufgabe — Urbildstrecke aus Streckfaktor |
| 22 | 4 | L4: Modell aus Text — Flussbreite über Peilung |
| 23 | 4 | L4: Scheitel erkennen — Parallele im Dreieck |
| 24 | 4 | L4: Ansatz wählen (MC, Auswahl als Leistung) |
| 25 | 5 | L5: Fehler in Rechnung — AA' statt SA' (MC) |
| 26 | 5 | L5: Sachaufgabe ohne Weg — Leitersprosse |
| 27 | 5 | L5: Größe aus zwei Bedingungen — Diagonalenabschnitt im Trapez |
| 28 | 5 | L5: Fehler in Rechnung — 2. Strahlensatz falsch angesetzt (MC) |
| 29 | 5 | L5: Sachaufgabe ohne Weg — Sektglas |
| 30 | 5 | L5: Parameter — x/(x+8) = 1/3 |
| 31 | 6 | L6: Behauptung begründen — dritte Form des Strahlensatzes (MC) |
| 32 | 6 | L6: Sonderfall — X-Figur |
| 33 | 6 | L6: Fallunterscheidung — Trapezfläche über k² |
| 34 | 6 | L6: Behauptung begründen — Mittelparallele (MC) |
| 35 | 6 | L6: Umkehraufgabe — Abstand aus Schattenlänge |
| 36 | 6 | L6: Umkehrung des Strahlensatzes — x für Parallelität |

### 8-aehnlichkeit-streckung (Umzug nach Kl. 9)

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | L5: Fehler in Rechnung — Fläche mit k statt k² (MC) |
| 26 | 5 | L5: Größe aus zwei Bedingungen — Fläche aus zwei Umfängen |
| 27 | 5 | L5: zweischrittig — Umfang zu k, Fläche mit k² |
| 28 | 5 | L5: Fehler — Winkel bei Streckung (MC) |
| 29 | 5 | L5: Sachaufgabe ohne Weg — Posterbreite aus Fläche |
| 30 | 5 | L5: Ähnlichkeitsbedingung — dritte Seite |
| 31 | 6 | L6: Sonderfall k = 1 — gleicher Umfang (MC) |
| 32 | 6 | L6: Umkehraufgabe — Umfang aus Flächenfaktor |
| 33 | 6 | L6: Streckung im Koordinatensystem — k aus Punktpaar |
| 34 | 6 | L6: Behauptung prüfen — Rechtecke ähnlich? (MC) |
| 35 | 6 | L6: Umkehraufgabe — Seite aus Flächenverhältnis |
| 36 | 6 | L6: Fallunterscheidung k < 1 — Umfang bei Verkleinerung |

### 9-stoch-boxplot

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | L5: zweischrittig — ordnen, beide Quartile, IQR |
| 26 | 5 | L5: Fehler in Rechnung — Quartil bei ungerader Anzahl (MC) |
| 27 | 5 | L5: Ausreißer aus Rohdaten ohne gelieferte Kenngrößen |
| 28 | 5 | L5: Größe aus Bedingung — x aus Median |
| 29 | 5 | L5: Boxplots vergleichen (MC, Auswahl als Leistung) |
| 30 | 5 | L5: zweischrittig — Mittelwert gegen Median |
| 31 | 6 | L6: Behauptung prüfen — gleicher Boxplot (MC, Gegenbeispiel) |
| 32 | 6 | L6: Sonderfall — Median = Mittelwert, Gleichung |
| 33 | 6 | L6: Umkehraufgabe — Werte aus Boxplot rekonstruieren |
| 34 | 6 | L6: Sonderfall — Q₁ = Median (MC) |
| 35 | 6 | L6: Robustheit des Medians — Differenz der Anstiege |
| 36 | 6 | L6: Behauptung prüfen — symmetrischer Boxplot (MC, Gegenbeispiel) |

### 9-stoch-haeufigkeiten

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | L4: Umkehraufgabe — n aus H und h |
| 20 | 4 | L4: Modell — relative Häufigkeit als Schätzwert, Hochrechnen |
| 21 | 4 | L4: Modell aus Text — Anzahl aus Durchschnitt (Gleichung) |
| 22 | 4 | L4: Kenngröße wählen (MC, Auswahl als Leistung) |
| 23 | 4 | L4: klassierte Daten zusammenfassen |
| 24 | 4 | L4: Häufigkeiten zusammenfassen statt mitteln |
| 25 | 5 | L5: Fehler in Rechnung — 0,4 = 4 % (MC) |
| 26 | 5 | L5: zweischrittig — Schätzung, dann Modell (Felder) |
| 27 | 5 | L5: fehlender Wert aus Mittelwert |
| 28 | 5 | L5: Fehler in Rechnung — Median ohne Ordnen (MC) |
| 29 | 5 | L5: Größe aus zwei Bedingungen — Klassengröße |
| 30 | 5 | L5: gewichteter Durchschnitt |
| 31 | 6 | L6: Behauptung prüfen — Ausgleichs-Fehlschluss (MC) |
| 32 | 6 | L6: Sonderfall — 0 weitere Sechsen |
| 33 | 6 | L6: Umkehraufgabe — Stichprobenumfang aus Gesamtanteil |
| 34 | 6 | L6: Behauptung prüfen — Mittelwert in der Reihe? (MC, Gegenbeispiel) |
| 35 | 6 | L6: zwei Bedingungen — sechster Wert, dann Median |
| 36 | 6 | L6: drei Bedingungen — Anzahl Einsen |

### Prüfung Block B

`level_check.py --strict` je Trainer Exit 0 ohne Warnung; `lehrplan_check.py --strict` 0 Befunde;
`katex_check.py` ok; `pytest tests/test_trainer.py -k <stem>` grün (7 je Trainer); `test_index.py`
grün nach Umbenennung; Bilder L5/L6 je Trainer angesehen (MC-Optionen gleich lang, KaTeX sauber).

Befund beim Umzug 8-aehnlichkeit-streckung: eine pauschale Ersetzung „aehnlich → ähnlich" traf
auch `THEMA_KEY` und ließ den Fortschritt (localStorage, Index-`data-key`) leerlaufen — der
`katex_check` fand die MC-Optionen nicht mehr. THEMA_KEY zurückgesetzt; Regel: THEMA_KEY bleibt ASCII.
