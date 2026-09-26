# Kl. 9 Block A1 — Review-Befunde behoben (2026-09-26)

Sieben Trainer (Potenzen/Wurzeln). Alle Zahlen mit Wolfram nachgerechnet; Gates
`level_check --strict` (0 Warnungen), `lehrplan_check --strict`, `katex_check`, `bild.py` L4/L6 grün.

## A. L4 auf AFB II gehoben

| Datei | id | Level | Neues Kriterium |
|---|---|---|---|
| 9-quadratwurzeln | 19 | L4 | Modell aus Text: Seitenlänge eines Quadrats (200 m²) als k√2 — Verfahren (Wurzel + teilweise radizieren) selbst wählen |
| 9-quadratwurzeln | 20 | L4 | Vergleich 2√11 vs. 3√5 ohne Taschenrechner (Vorfaktor unter die Wurzel) — MC, korrekt = 1 |
| 9-quadratwurzeln | 22 | L4 | Umkehraufgabe: Von welcher Zahl ist 4√3 die Wurzel? (48) |
| 9-quadratwurzeln | 23 | L4 | Schätzung: √70 zwischen 8 und 9, mit Begründung über Quadratzahlen — MC, korrekt = 2 |
| 9-quadratwurzeln | 24 | L4 | Modell aus Text: Umfang 8√3 cm → Flächeninhalt 12 cm² (zwei Schritte, Verfahren wählen) |
| 9-potenzen-ganzzahlig | 19 | L4 | Modell aus Text: viermal auf ein Zehntel verdünnt → 10^k, k = −4 |
| 9-potenzen-ganzzahlig | 22 | L4 | Größenvergleich 9^−3 vs. 3^−4 ohne Ausrechnen (gleiche Basis) — MC, korrekt = 1 |

## B. Dubletten / Lösungsverrat

| Datei | id | Level | Änderung |
|---|---|---|---|
| 9-wurzelgleichungen | 21 | L4 | Neue Gleichung √(2x²+7) = 5 (x = 3); Kern √(x²−9)=4 bleibt allein in #31 |
| 9-wurzelgleichungen | 35 | L6 | Parameter b für Scheinlösung x = 2 bei √(x+b) = x−5 (b = 7); Gleichung √(x+3)=x−3 nur noch in #13 |
| 9-wurzelgleichungen | 36 | L6 | Behauptung „positiver Radikand ⇒ Lösung" mit neuem Gegenbeispiel √(x+5) = x−1, x = −1 — MC, korrekt = 2; kein Bezug mehr zu #35 |
| 9-potenzen-rational | 32 | L6 | Neu: Behauptung „a^(1/2) < a für alle a > 0" — Fallunterscheidung a > 1 / a = 1 / 0 < a < 1, MC, korrekt = 1 (Kern 16^r = 8 nur noch in #20) |
| 9-potenzen-rational | 36 | L6 | Neu: Volumen ×27 → Oberfläche ×9 (Exponent 2/3), Behauptung „×27" prüfen; Würfel-„+26 %" bleibt allein in 9-potenzgleichungen #23 |
| 8-potenzen-negativ | 32 | L6 | Neu: Anzahl ganzer x mit x^−2 ≥ 1/9 (6; Sonderfall x = 0 ausschließen); Kern 2^−n = 1/8 nur noch in #30. Damit auch gleicher Tipp-Wortlaut zu potenzen-rational #32 beseitigt |
| 8-potenzen-negativ | 27 | L5 | Parameter-aus-zwei-Bedingungen ersetzt durch zweischrittige Sachaufgabe: Würfel mit Kante 2^−2 m → 15,625 l (Volumen als Zweierpotenz + m³→l). 7-potenzgesetze #26 und 9-potenzen-ganzzahlig #26 bleiben (verschiedene Zahlen/Fragen) |

## C. Tipps ohne Lösung

| Datei | id | Level | Neuer Tipp |
|---|---|---|---|
| 9-wurzelgleichungen | 13 | L3 | Wegbeschreibung (quadrieren, ordnen, lösen, Probe); quadrierte Gleichung und Kandidaten jetzt im Lösungsweg |
| 9-wurzelgleichungen | 14 | L3 | Hinweis auf binomische Formel und Ausklammern; Gleichung im Lösungsweg |
| 9-wurzelgleichungen | 15 | L3 | Hinweis auf zwei Kandidaten + Probe; Gleichung im Lösungsweg |
| 8-potenzen-negativ | 8 | L2 | „Kehrwert der Potenz mit positivem Exponenten" statt „1/16" |
| 9-potenzen-ganzzahlig | 33 | L6 | „Vorzeichen und Betrag getrennt betrachten" statt Nennung beider Kriterien |

## D. MC-Fairness (richtige Option nicht mehr die längste; `korrekt` variiert)

| Datei | id | Level | korrekt alt → neu |
|---|---|---|---|
| 7-potenzgesetze | 28 | L5 | 0 → 1 |
| 7-potenzgesetze | 32 | L6 | 0 → 2 |
| 7-potenzgesetze | 33 | L6 | 0 → 1 |
| 8-potenzen-negativ | 25 | L5 | 0 → 1 |
| 8-potenzen-negativ | 28 | L5 | 0 → 3 |
| 8-potenzen-negativ | 31 | L6 | 0 → 2 |
| 9-quadratwurzeln | 34 | L6 | 0 → 2 |
| 9-potenzen-ganzzahlig | 25 | L5 | 0 → 3 |
| 9-potenzen-ganzzahlig | 29 | L5 | 0 → 2 |
| 9-potenzen-ganzzahlig | 31 | L6 | 0 → 3 |
| 9-potenzen-rational | 25 | L5 | 0 → 2 |
| 9-potenzen-rational | 31 | L6 | 0 → 3 |
| 9-potenzgleichungen | 25 | L5 | 0 → 1 |
| 9-potenzgleichungen | 36 | L6 | 0 → 2 |
| 9-wurzelgleichungen | 25 | L5 | 0 → 2 |
| 9-wurzelgleichungen | 30 | L5 | 0 → 1 |
| 9-wurzelgleichungen | 36 | L6 | 0 → 2 |

Muster: richtige Option auf Kernaussage gekürzt, jeder Distraktor mit einer plausiblen falschen
Begründung auf vergleichbare Länge gebracht; Begründung der richtigen Antwort steht im `loesungsweg`.
Gate-Warnung „richtige MC-Option deutlich laenger" in allen sieben Dateien: 0.
