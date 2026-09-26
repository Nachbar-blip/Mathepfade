# Klasse 7 — Überarbeitung je Trainer (Stand 2026-09-26)

Lokale Nachvollziehbarkeit; im Public-HTML stehen die Kriterien bewusst nicht.
Grundlage: Rubrik aus `docs/plans/2026-09-26-lehrplan-th-und-level-progression-plan.md`
(Lesart Kl. 7: L4 = Rechenart/Verfahren selbst wählen, Modell aus Text, Umkehraufgabe;
L5 = zweischrittige Sachaufgabe ohne Weg, Fehler in vorgelegter Rechnung, Parameter aus zwei
Bedingungen; L6 = Zahlenrätsel/Umkehraufgabe, „Stimmt die Behauptung?" begründet, Sonderfall,
Fallunterscheidung), Befunde aus `docs/audit/audit-2026-09-19-mathepfade.md`.
Jede Lösung mit Wolfram|Alpha nachgerechnet; Bilder L5/L6 per `tests/bild.py` angesehen.

Blöcke: **A Terme/Gleichungen (5)** → **B Geometrie (5)** → **C Daten (1)** = 11 Trainer.

## Block A — Terme und Gleichungen

| Trainer | Audit-Befund | Geändert |
|---|---|---|
| 7-binomische-formeln | KEIN_AFB3 L5/L6; KOLLAPS L4/L5 (L4 = 3. Formel anwenden, L5 = Faktorisieren — beides Standardverfahren) | L4–L6 neu; L3 #16/#18 durch die bisherigen L4-Standardaufgaben zur 3. Formel ersetzt, damit alle drei Formeln in L1–L3 vorkommen |
| 7-gleichungen-linear | KEIN_AFB3 L5/L6; KOLLAPS L3/L4 und L4/L5 (nur mehr Klammern bzw. Brüche); KURZ L1–L4 | L4–L6 neu: Modell aus Text, Parameter aus Lösung, Fehler im Rechenweg, Einholaufgabe, Sonderfälle (unendlich viele / keine Lösung), Grundbereich |
| 7-terme-aufstellen | KEIN_AFB3 L6 (L6 = Termwert-Rechnungen mit Kontext) | L5/L6 neu: Übersetzungsfehler, Streichholzmuster, Kerze (zwei Schritte), Behauptungen über Parität und Flächen, Tarifvergleich |
| 7-terme-umformungen | KEIN_AFB3 L5; KOLLAPS L2/L3 (nicht behoben, L1–L3 bleiben) | L5/L6 neu: Klammerfehler, unvollständiges Ausklammern, Parameter aus Koeffizientenvergleich, konstanter Term, Identität, Zahlenrätsel; binomische Aufgaben (47·53) entfernt — gehören in 7-binomische-formeln |
| 7-ungleichungen | KEIN_AFB3 L5/L6 (L5 = Standardverfahren, L6 = Betragsungleichungen über Kl. 7) | L5/L6 neu: Vorzeichenfehler beim Dividieren, Gewinnschwelle, zwei Bedingungen zählen, Parameter für vorgegebene Lösungsmenge, allgemeingültig/unerfüllbar, Grundbereich ℕ, Behauptung zur Multiplikation |

### 7-binomische-formeln

| id | Level | Kriterium |
|---|---|---|
| 16 | 3 | L3: 3. Formel anwenden (aus altem L4 übernommen, ersetzt Termwert (y−5)² für y=8) |
| 18 | 3 | L3: 48·52 mit 3. Formel (aus altem L4 übernommen, ersetzt 98²) |
| 19 | 4 | L4: Verfahren selbst wählen — 38·42 ohne schriftliche Multiplikation |
| 20 | 4 | L4: Umkehraufgabe — c so, dass x²+16x+c ein Quadrat ist |
| 21 | 4 | L4: Modell aus Text — Quadrat zu Rechteck (a+4)(a−4) |
| 22 | 4 | L4: Umkehraufgabe — b aus (x+b)² = x²+18x+81 |
| 23 | 4 | L4: Verfahren erkennen — welcher Term ist binomisch zerlegbar (MC, Auswahl ist die Leistung) |
| 24 | 4 | L4: Modell aus Text — Flächenzuwachs 23²−20² |
| 25 | 5 | L5: Fehler finden — mittlerer Term bei (2x−3)² (MC) |
| 26 | 5 | L5: Parameter aus zwei Bedingungen — a, b aus (ax+b)² = 9x²+30x+25 |
| 27 | 5 | L5: zweischrittig — zwei Formeln kombinieren, dann einsetzen |
| 28 | 5 | L5: Fehler finden — vergessene 2ab-Terme (MC) |
| 29 | 5 | L5: Sachaufgabe ohne Weg — Seitenlänge aus Flächendifferenz |
| 30 | 5 | L5: Gleichung, in der x² wegfällt |
| 31 | 6 | L6: Behauptung begründen — (n+1)²−n² ungerade (MC) |
| 32 | 6 | L6: Zahlenrätsel — Differenz der Quadrate 45 |
| 33 | 6 | L6: Behauptung prüfen — Fläche bleibt gleich? (MC) |
| 34 | 6 | L6: Sonderfall — c für unendlich viele Lösungen |
| 35 | 6 | L6: Umkehraufgabe — Gleichung mit zwei Quadraten, negative Lösung |
| 36 | 6 | L6: Zahlenrätsel — aufeinanderfolgende ungerade Zahlen |

### 7-gleichungen-linear

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | L4: Modell aus Text — Handytarif, Minuten gesucht |
| 20 | 4 | L4: Umkehraufgabe — a aus gegebener Lösung |
| 21 | 4 | L4: Modell aus Text — passende Gleichung wählen (MC, Auswahl ist die Leistung) |
| 22 | 4 | L4: Umkehraufgabe — b aus Lösung x = 6 |
| 23 | 4 | L4: Modell aus Text — Dreiecksseiten aus Umfang, Dezimallösung |
| 24 | 4 | L4: Verfahren wählen — Hauptnenner bei x/4 − x/6 = 2 |
| 25 | 5 | L5: Fehler im Rechenweg finden — Klammer unvollständig aufgelöst (MC) |
| 26 | 5 | L5: Parameter aus zwei Bedingungen — a aus zwei Termwerten |
| 27 | 5 | L5: Sachaufgabe zweischrittig — Alter in 5 Jahren |
| 28 | 5 | L5: Sachaufgabe ohne Weg — Einholen zweier Züge |
| 29 | 5 | L5: Fehler finden — Äquivalenzumformung nur auf einen Summanden (MC) |
| 30 | 5 | L5: Sachaufgabe zweischrittig — Geldwechsel, Verhältnis danach |
| 31 | 6 | L6: Sonderfall — unendlich viele Lösungen (MC) |
| 32 | 6 | L6: Sonderfall — a ohne Lösung |
| 33 | 6 | L6: Zahlenrätsel — Rückwärtsrechnen |
| 34 | 6 | L6: Behauptung begründen — Äquivalenz zweier Gleichungen (MC) |
| 35 | 6 | L6: Fallunterscheidung Grundbereich — 7x = 3 in ℕ / ℚ (MC) |
| 36 | 6 | L6: Umkehraufgabe — Breite aus Umfang und Längenbedingung |

### 7-terme-aufstellen

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | L5: Fehler finden — „Dreifaches der Summe" ohne Klammer (MC) |
| 26 | 5 | L5: zweischrittig — Term aus Muster aufstellen, dann auswerten |
| 27 | 5 | L5: zweischrittig — Anfangslänge bestimmen, dann Zeitpunkt |
| 28 | 5 | L5: Fehler finden — Rabatt nur einmal abgezogen (MC) |
| 29 | 5 | L5: Term aufstellen und Bedingung lösen — vier aufeinanderfolgende Zahlen |
| 30 | 5 | L5: Umfangsterm aufstellen, dann x bestimmen |
| 31 | 6 | L6: Behauptung begründen — n(n+1) gerade (MC) |
| 32 | 6 | L6: Zahlenrätsel — Term vereinfachen, dann lösen |
| 33 | 6 | L6: Behauptung prüfen — 2(x+3) und 2x+3 nie gleich (MC) |
| 34 | 6 | L6: Umkehraufgabe — Alter aus zwei Verhältnissen |
| 35 | 6 | L6: Fallunterscheidung — ab wann Tarif A günstiger |
| 36 | 6 | L6: Behauptung prüfen — Verdopplung der Seite vervierfacht Fläche (MC) |

### 7-terme-umformungen

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | L5: Fehler finden — Minusklammer nur halb gedreht (MC) |
| 26 | 5 | L5: Parameter — a aus vereinfachtem Term |
| 27 | 5 | L5: zweischrittig — vereinfachen, dann negativen Wert einsetzen |
| 28 | 5 | L5: Fehler finden — unvollständiges Ausklammern (MC) |
| 29 | 5 | L5: Parameter aus zwei Bedingungen — Koeffizientenvergleich |
| 30 | 5 | L5: Sachaufgabe — Reststück als Term, dann einsetzen |
| 31 | 6 | L6: Behauptung prüfen — x²+x² = x⁴? (MC) |
| 32 | 6 | L6: Sonderfall — a, für das der Term konstant ist |
| 33 | 6 | L6: Zahlenrätsel — Term reduziert sich auf x−3 |
| 34 | 6 | L6: Sonderfall — Identität, alle x (MC) |
| 35 | 6 | L6: Umkehraufgabe — Rechteck flächengleich zum Quadrat |
| 36 | 6 | L6: Umkehraufgabe — Produktterm vereinfachen, dann x bestimmen |

### 7-ungleichungen

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | L5: Fehler finden — Division durch negative Zahl ohne Umdrehen (MC) |
| 26 | 5 | L5: Sachaufgabe ohne Weg — Gewinnschwelle |
| 27 | 5 | L5: zwei Bedingungen — ganze Zahlen zählen |
| 28 | 5 | L5: Fehler finden — Vorzeichen beim Umstellen (MC) |
| 29 | 5 | L5: Parameter — a für vorgegebene Lösungsmenge |
| 30 | 5 | L5: Sachaufgabe zweischrittig — Notendurchschnitt |
| 31 | 6 | L6: Sonderfall — allgemeingültige Ungleichung (MC) |
| 32 | 6 | L6: Sonderfall — a ohne Lösung |
| 33 | 6 | L6: Umkehraufgabe — b aus Anzahl der Lösungen in ℕ |
| 34 | 6 | L6: Behauptung begründen — Multiplikation mit negativer Zahl (MC) |
| 35 | 6 | L6: Grundbereich ℕ — Lösungen zählen nach Vorzeichenwechsel |
| 36 | 6 | L6: Fallunterscheidung — Lösungsmenge mit Sinnbedingung b > 0 (MC) |
