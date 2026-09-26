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

## Block B — Geometrie

| Trainer | Audit-Befund | Geändert |
|---|---|---|
| 7-dreiecke-kongruenz | KEIN_AFB3 L5/L6 (L5 = Verhältnisrechnung, L6 = Außenwinkel-Standard, Pythagoras in #35 — nicht Kl. 7) | L5/L6 neu: Winkel aus zwei Bedingungen, SsW-Fehlschluss, Anzahl ganzzahliger Dreiecke, Basiswinkel-Fehler, Außenwinkel mit Differenz; entarteter SSS-Fall, Winkelhalbierenden-Umkehr, Lösbarkeit SsW, Fallunterscheidung gleichschenklig (100°/50°), Thales begründen |
| 7-konstruktionen | KEIN_AFB3 L5/L6; KOLLAPS L2/L3 (bleibt); L6 #36 mit √3 — nicht Kl. 7 | L5/L6 neu: Radius zu klein für Mittelsenkrechte, zwei gleichseitige Dreiecke, dritter Winkel vor WSW, Umkreis rechtwinklig, Inkreis-Fehler, Schwerpunkt-Umkehr; nicht konstruierbar (SSS), α+β = 180°, Umkreismittelpunkt auf Seite → Thales, Höhenschnittpunkt außen, Kreis berührt Gerade, Winkelhalbierende als Höhe |
| 7-symmetrie | KEIN_AFB3 L5/L6 (L5/L6 = Merkwissen und Ablesen) | L5/L6 neu: Verkettung Drehung+Spiegelung, Achsenverwechslung, Drehwinkel aus Achsenzahl, Achse aus Punkt und Bild, unvollständige Konstruktion, a aus Abstand; kein Dreieck punktsymmetrisch, Punktspiegelung rückwärts, Zacken aus dritter Deckung, doppelter Achsenabstand, zwei Spiegelungen = Drehung 180°, Achse aus Bildpunkt. Negative Koordinaten nach dem Trennstrich in `{…}` gesetzt (KaTeX setzte das Minus binär) |
| 7-vierecke | KEIN_AFB3 L5/L6; KOLLAPS L2/L3 (bleibt); L4 #24 und L5 #26/#28 mit Wurzeln — nicht Kl. 7 | L5/L6 neu: Rechteck aus Umfang und Differenz, Höhe statt Nachbarseite, Trapezhöhe, Parallelogrammwinkel 1:3, Quadrat flächengleich, Dreieck in Trapez; gleich lange Diagonalen ≠ Rechteck, Seiten aus Fläche und Umfang, gleichschenkliges Trapez, genau drei rechte Winkel, Quadrat vs. Rechteck bei gleichem Umfang, Raute aus Eigenschaften. L4 #24 (a√2) durch Umkehraufgabe Grundseite aus Fläche ersetzt |
| 7-winkel-winkelsumme | KEIN_AFB3 L6 (L6 = n-Eck-Formeln im Text) | L5/L6 neu: Nebenwinkel 1:3, Wechselwinkel-Fehler, Winkel aus zwei Bedingungen, Außenwinkel 3:4, Vierecks-Winkelsumme-Fehler, Komplement→Nebenwinkel; zwei stumpfe Winkel, n aus Innenwinkel über Außenwinkel, Hilfsparallele (Zickzack), Stufenwinkel ohne Parallelität, drei Winkel = 290°, größter Winkel aus Termen. L4 #19: Formelansage „Winkelsumme: 180°“ aus dem Text entfernt |

### 7-dreiecke-kongruenz

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | L5: Größe aus zwei Bedingungen — γ aus β = α+20°, γ = 2α |
| 26 | 5 | L5: Fehler finden — Kongruenz aus zwei Seiten und nicht eingeschlossenem Winkel gegenüber der kürzeren Seite (MC) |
| 27 | 5 | L5: zwei Bedingungen — Basis aus Umfang und Schenkel = Basis + 4 |
| 28 | 5 | L5: zweischrittig — Dreiecksungleichung, dann ganzzahlige Werte zählen |
| 29 | 5 | L5: Fehler in Rechnung — Basiswinkel nicht halbiert (MC) |
| 30 | 5 | L5: Außenwinkel und Differenz der Innenwinkel, Weg nicht vorgegeben |
| 31 | 6 | L6: Sonderfall — a + b = c, entartetes Dreieck (MC) |
| 32 | 6 | L6: Umkehraufgabe — α aus Winkel zwischen den Winkelhalbierenden |
| 33 | 6 | L6: Lösbarkeit/Lösungsvielfalt — SsW mit Winkel gegenüber der längeren Seite (MC) |
| 34 | 6 | L6: Fallunterscheidung — 100° kann kein Basiswinkel sein |
| 35 | 6 | L6: Fallunterscheidung — 50° an Spitze oder Basis, beide Fälle rechnen |
| 36 | 6 | L6: Behauptung begründen — Thales über zwei gleichschenklige Dreiecke (MC) |

### 7-konstruktionen

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | L5: Fehler in Konstruktion — Radius kleiner als halbe Strecke (MC) |
| 26 | 5 | L5: Lösungsvielfalt — zwei Lagen für gleichseitiges Dreieck über AB |
| 27 | 5 | L5: zweischrittig — β berechnen, dann WSW (kein Weg vorgegeben) |
| 28 | 5 | L5: zweischrittig — Umkreismittelpunkt auf Hypotenuse, Durchmesser |
| 29 | 5 | L5: Fehler finden — Mittelsenkrechten statt Winkelhalbierende für Inkreis (MC) |
| 30 | 5 | L5: Umkehr über Teilverhältnis 2:1 ohne Nennung im Text |
| 31 | 6 | L6: Lösbarkeit — SSS mit a + b < c, Kreise schneiden sich nicht (MC) |
| 32 | 6 | L6: Sonderfall — α + β = 180°, parallele Schenkel, 0 Dreiecke |
| 33 | 6 | L6: Umkehrung Thales — Umkreismittelpunkt auf c ⇒ γ = 90° |
| 34 | 6 | L6: Behauptung prüfen — Höhenschnittpunkt nach Dreiecksart (MC) |
| 35 | 6 | L6: Sonderfall — Kreis berührt Gerade, genau ein Punkt, mit Fallunterscheidung |
| 36 | 6 | L6: zweischrittig — Winkel im Teildreieck, Winkelhalbierende wird Höhe |

### 7-symmetrie

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | L5: zweischrittig — Drehung 180°, dann Spiegelung an x-Achse |
| 26 | 5 | L5: Fehler finden — Achsen verwechselt (MC) |
| 27 | 5 | L5: zweischrittig — Eckenzahl aus Achsenzahl, dann Drehwinkel |
| 28 | 5 | L5: Umkehr — Achse als Mittelsenkrechte von AA′ |
| 29 | 5 | L5: Fehler in Konstruktion — Abstandsbedingung fehlt (MC) |
| 30 | 5 | L5: Größe aus Bedingung — a aus Abstand zum Spiegelbild |
| 31 | 6 | L6: Behauptung begründen — kein Dreieck punktsymmetrisch (MC) |
| 32 | 6 | L6: Umkehraufgabe — Urbild aus Zentrum und Bildpunkt |
| 33 | 6 | L6: Umkehraufgabe — Zackenzahl aus dritter Deckung bei 216° |
| 34 | 6 | L6: Behauptung prüfen — Verschiebung um doppelten Achsenabstand (MC) |
| 35 | 6 | L6: Begründung — zwei Spiegelungen an senkrechten Achsen = Drehung 180° |
| 36 | 6 | L6: Umkehraufgabe — Achse y = −2 aus Punkt und Bild |

### 7-vierecke

| id | Level | Kriterium |
|---|---|---|
| 24 | 4 | L4: Umkehraufgabe — Grundseite aus Fläche und Höhe (ersetzt a√2) |
| 25 | 5 | L5: zwei Bedingungen — Seiten aus Umfang und Differenz, dann Fläche |
| 26 | 5 | L5: Fehler finden — Nachbarseite statt Höhe (MC) |
| 27 | 5 | L5: Umkehr zweischrittig — Trapezhöhe aus Fläche |
| 28 | 5 | L5: zwei Bedingungen — Nachbarwinkel 1:3 im Parallelogramm |
| 29 | 5 | L5: zweischrittig — Fläche → Quadratseite → Umfang |
| 30 | 5 | L5: zusammengesetzt — Höhe des Teildreiecks erkennen |
| 31 | 6 | L6: Behauptung prüfen — gleich lange Diagonalen, Gegenbeispiel Trapez (MC) |
| 32 | 6 | L6: Umkehraufgabe — Seiten aus Fläche und Umfang |
| 33 | 6 | L6: Fallunterscheidung — Winkel im gleichschenkligen Trapez |
| 34 | 6 | L6: Sonderfall — genau drei rechte Winkel unmöglich (MC) |
| 35 | 6 | L6: Vergleich — Quadrat vs. Rechteck bei gleichem Umfang |
| 36 | 6 | L6: Fallunterscheidung — genaueste Bezeichnung aus Eigenschaften (MC) |

### 7-winkel-winkelsumme

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | L4: Formelansage entfernt, Aufgabe sonst unverändert |
| 25 | 5 | L5: zwei Bedingungen — Nebenwinkel 1:3 |
| 26 | 5 | L5: Fehler finden — Wechselwinkel als Nebenwinkel berechnet (MC) |
| 27 | 5 | L5: Größe aus zwei Bedingungen — α aus β = α+30°, γ = α+β |
| 28 | 5 | L5: Außenwinkel mit Verhältnis 3:4 |
| 29 | 5 | L5: Fehler in Rechnung — Dreieckssumme im Viereck (MC) |
| 30 | 5 | L5: zweischrittig — Komplement, dann Nebenwinkel |
| 31 | 6 | L6: Behauptung begründen — zwei stumpfe Winkel unmöglich (MC) |
| 32 | 6 | L6: Umkehraufgabe — n aus Innenwinkel über Außenwinkelsumme |
| 33 | 6 | L6: Hilfslinie selbst finden — Zickzack zwischen Parallelen |
| 34 | 6 | L6: Sonderfall — Stufenwinkelsatz braucht Parallelität (MC) |
| 35 | 6 | L6: zweischrittig — vierter Winkel aus 360°, Scheitel/Neben |
| 36 | 6 | L6: zweischrittig — x bestimmen, dann größten Winkel vergleichen |

## Block C — Daten und Diagramme

| Trainer | Audit-Befund | Geändert |
|---|---|---|
| 7-daten-diagramme | KEIN_AFB3 L5 (Boxplot/IQR über Kl. 7, sonst Standard); L6 gemischt | L5/L6 neu: gewichteter Mittelwert, Kreisdiagramm-Fehler, gestrichener Wert, x aus Mittelwert, abgeschnittene Achse, Sektorwinkel → Personen; Durchschnitt 2,0 ohne Note 2, fünf Kenngrößen kombinieren, Zielnote, Mittelwert steigt (Begründung), Tippfehler-Korrektur, Median vs. Mittelwert bei Ausreißer. L3 #14: Formel „Anzahl / Gesamtzahl“ aus dem Text entfernt |

### 7-daten-diagramme

| id | Level | Kriterium |
|---|---|---|
| 14 | 3 | L3: Formel im Text entfernt, Aufgabe sonst unverändert |
| 25 | 5 | L5: zweischrittig — Mittelwert zweier ungleich großer Gruppen |
| 26 | 5 | L5: Fehler im Diagramm — Prozent als Grad gezeichnet (MC) |
| 27 | 5 | L5: Umkehr über Summen — gestrichener Wert |
| 28 | 5 | L5: Größe aus Bedingung — x aus Mittelwert |
| 29 | 5 | L5: Fehler im Diagramm — abgeschnittene Achse (MC) |
| 30 | 5 | L5: zweischrittig — Restsektor, Anteil, Anzahl |
| 31 | 6 | L6: Behauptung prüfen — Gegenbeispiel zum Mittelwert (MC) |
| 32 | 6 | L6: Umkehraufgabe — Wert aus Minimum, Spannweite, Median, Mittelwert |
| 33 | 6 | L6: Umkehraufgabe — Note für Zieldurchschnitt |
| 34 | 6 | L6: Behauptung begründen — neuer Wert über Mittelwert (MC) |
| 35 | 6 | L6: Fehlerkorrektur — Summe berichtigen, Mittelwert neu |
| 36 | 6 | L6: Kenngröße beurteilen — Median vs. Mittelwert bei Ausreißer (MC) |
