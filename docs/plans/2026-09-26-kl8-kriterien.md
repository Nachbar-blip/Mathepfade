# Klasse 8 — Überarbeitung je Trainer (Stand 2026-09-26)

Lokale Nachvollziehbarkeit; im Public-HTML stehen die Kriterien bewusst nicht.
Grundlage: Rubrik aus `docs/plans/2026-09-26-lehrplan-th-und-level-progression-plan.md`
(Lesart Kl. 8: L4 = Rechenart/Verfahren selbst wählen, Modell aus Text/Tabelle, Umkehraufgabe;
L5 = zweischrittige Sachaufgabe ohne Weg, Fehler in vorgelegter Rechnung, Parameter aus zwei
Bedingungen; L6 = Behauptung begründet prüfen, Sonderfall (parallel/identisch, keine Lösung,
Definitionslücke), Umkehraufgabe, Fallunterscheidung), Befunde aus
`docs/audit/audit-2026-09-19-mathepfade.md`. Niveau: TH-Lehrplan 2.2.1/2.2.2 (keine LGS als
Verfahren, keine Bruchgleichungen, keine Wurzeln).
Jede Lösung mit Wolfram|Alpha nachgerechnet; Bilder L5/L6 (Ersatz-Trainer zusätzlich L1) per
`tests/bild.py` angesehen.

Blöcke: **A Algebra & Funktionen (5)** → **B Geometrie** → **C Stochastik**.

## Block A — Algebra & Funktionen

| Trainer | Audit-Befund | Geändert |
|---|---|---|
| 8-lineare-funktionen-grund | KEIN_AFB3 L5; DUENNER_WEG L2, L5 (L5/L6 = Gerade aus Punkt + Anstieg bzw. zwei Punkten — Standardverfahren) | L5/L6 neu: Vorzeichenfehler im Differenzenquotienten, n aus zwei Funktionswerten, Nullstelle aus zwei Punkten, Fehler beim Umstellen, Parameter für Punkt auf Gerade; identische Geraden, Parallelität über Parameter, „doppeltes x → doppeltes y?", Schnitt auf der x-Achse, keine Nullstelle (Fallunterscheidung), m aus Schnittstelle. L4 #20/#23/#24 durch die bisherigen Standardaufgaben „Gerade aus zwei Punkten / Punkt + n" ersetzt (Umkehr- und Zweischritt-Aufgaben), damit das Kernverfahren im Trainer bleibt; „Antwort 1 für Ja"-Hack entfernt |
| 8-lineare-funktionen-anwendungen | KEIN_AFB3 L5; KOLLAPS L1/L2 (bleibt); DUENNER_WEG L4 | L5/L6 neu: Vorzeichenfehler beim Leeren, Grundgebühr aus zwei Fahrten, Kerze zweischrittig, m/n vertauscht, Füllstand rückwärts, Radfahrer; Tarifgrenze (Fallunterscheidung), parallele Tarife ohne Schnittpunkt, Gesamtstrecke aus zwei Restwerten, Einholen, zwei Kerzen, „doppelte Zeit = doppelter Preis?". L4 #19, #21–#24 mit ausführlichem Weg (Modell, Umformung, Probe) neu formuliert |
| 8-proportionalitaet | KEIN_AFB3 L5; KOLLAPS L1/L2, L2/L3 (bleiben) | L5/L6 neu: Division statt Multiplikation beim Dreisatz, Vorrat mit Zugang, x = y bei Produkt konstant, Pumpen-Fehlschluss, Drucker mit Pause, Maßstab + Gehzeit; „wächst mit" ≠ proportional (Tabelle), a aus gleichen Quotienten, Durchschnittsgeschwindigkeit 60/120, zusammengesetzter Dreisatz, ausgefallene Arbeiter, „x = 0 → y = 0?". L1 #4/#5 `{,}` außerhalb von KaTeX entfernt, L4 #21 als Modellaufgabe umformuliert |
| 8-bruchterme-grundlagen | KEIN_AFB3 L5/L6; KOLLAPS L4/L5 (beide = Bruchterme addieren/multiplizieren, über Kl.-8-Stoff) | L4–L6 neu, nur Kürzen/Erweitern/Definitionsmenge: kürzbaren Term erkennen, Erweitern rückwärts, a aus Definitionslücke, Modell Rechteckseite, Definitionslücke bei x²−16, Ausklammern + Wert; Kürzen aus Summen, p/q aus Lücke und Wert, gekürzter Term = 12, Definitionsmenge bei Produkt-Nenner, Seitendifferenz, c für Kürzbarkeit; Gleichwertigkeit trotz Lücke, Term aus Lücke + Nullstelle, „Zähler null ⇔ Term null?", Vorzeichen-Fallunterscheidung, k aus gekürztem Term, Term ohne Definitionslücke. L3 #16/#17 ohne vorgegebene Formel |
| 8-vektoren-2d → Prozent- und Zinsrechnung | Thema nicht im TH-Lehrplan Kl. 8 (Vektoren); Prozent/Zins (2.2.2) fehlte | Alle 36 Aufgaben neu, Datei behalten (QR-Links), `THEMA_KEY` unverändert, Index: Abschnitt A, „Prozent & Zinsen" |

### 8-lineare-funktionen-grund

| id | Level | Kriterium |
|---|---|---|
| 20 | 4 | L4: Zweischritt — n aus zwei Punkten (ehem. L6 #33 als numerische Aufgabe) |
| 23 | 4 | L4: Umkehraufgabe — m aus Punkt und n (ehem. L6 #36) |
| 24 | 4 | L4: Zweischritt — f(5) aus zwei Punkten (ehem. L6 #34) |
| 25 | 5 | L5: Fehler finden — Reihenfolge im Differenzenquotienten (MC) |
| 26 | 5 | L5: Parameter aus zwei Bedingungen — n aus f(2), f(6) |
| 27 | 5 | L5: zweischrittig — Nullstelle der Geraden durch zwei Punkte |
| 28 | 5 | L5: Fehler finden — Vorzeichen beim Umstellen der Nullstellengleichung (MC) |
| 29 | 5 | L5: zweischrittig — g(10) aus Nullstelle und Achsenabschnitt |
| 30 | 5 | L5: Parameter — a für P(a\|−3) auf der Geraden durch A, B |
| 31 | 6 | L6: Behauptung prüfen — identische Geraden in verschiedener Form (MC) |
| 32 | 6 | L6: Sonderfall parallel — k aus Anstiegsvergleich |
| 33 | 6 | L6: Behauptung prüfen — Verdopplung nur bei Ursprungsgeraden (MC) |
| 34 | 6 | L6: Umkehraufgabe — n so, dass Schnittpunkt auf der x-Achse liegt |
| 35 | 6 | L6: Fallunterscheidung — c ohne Nullstelle (waagerechte Gerade) |
| 36 | 6 | L6: Umkehraufgabe — m aus vorgegebener Schnittstelle |

### 8-lineare-funktionen-anwendungen

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | L4: Modell aus Text — Fixkosten + Stückkosten (MC, Weg ergänzt) |
| 21 | 4 | L4: Umkehraufgabe — x aus U(x) = 30 (MC, Weg ergänzt) |
| 22 | 4 | L4: Modell aus Text — Pool, Zeit bis 1500 L |
| 23 | 4 | L4: Umkehraufgabe — Gewinnschwelle als Nullstelle |
| 24 | 4 | L4: Umkehraufgabe — Artikelzahl bei Pauschale |
| 25 | 5 | L5: Fehler finden — Vorzeichen beim Leeren des Tanks (MC) |
| 26 | 5 | L5: Parameter aus zwei Bedingungen — Grundgebühr aus zwei Fahrten |
| 27 | 5 | L5: zweischrittig — Abbrandrate, dann Zeitpunkt |
| 28 | 5 | L5: Fehler finden — m und n vertauscht (MC) |
| 29 | 5 | L5: zweischrittig — Zuflussrate, dann rückwärts auf 8:00 Uhr |
| 30 | 5 | L5: zweischrittig — Geschwindigkeit aus zwei Zeitpunkten, dann Prognose |
| 31 | 6 | L6: Behauptung prüfen — Tarifgrenze mit Fallunterscheidung (MC) |
| 32 | 6 | L6: Sonderfall parallel — gleicher kWh-Preis, kein Schnittpunkt (MC) |
| 33 | 6 | L6: Umkehraufgabe — Gesamtstrecke aus zwei Restwerten |
| 34 | 6 | L6: Einholaufgabe — Ort des Einholens |
| 35 | 6 | L6: Lage zweier Geraden — zwei Kerzen gleich lang, danach Wechsel |
| 36 | 6 | L6: Behauptung prüfen — linear ≠ proportional (MC) |

### 8-proportionalitaet

| id | Level | Kriterium |
|---|---|---|
| 21 | 4 | L4: Modell aus Text — Zuordnungsart und Wert bei konstanter Fläche (MC) |
| 25 | 5 | L5: Fehler finden — dividiert statt multipliziert (MC) |
| 26 | 5 | L5: zweischrittig — Vorrat mit Zugang nach 5 Tagen |
| 27 | 5 | L5: Umkehr/Parameter — x = y bei konstantem Produkt |
| 28 | 5 | L5: Fehler finden — mehr Pumpen, längere Zeit? (MC) |
| 29 | 5 | L5: zweischrittig — Druckzeit plus nicht-proportionale Pause |
| 30 | 5 | L5: zweischrittig — Maßstab, dann Gehzeit |
| 31 | 6 | L6: Behauptung prüfen — „wächst mit" ≠ proportional (MC) |
| 32 | 6 | L6: Parameter — a aus gleichen Quotienten |
| 33 | 6 | L6: Behauptung prüfen — Durchschnittsgeschwindigkeit (MC) |
| 34 | 6 | L6: zusammengesetzter Dreisatz — Bagger und Grabenlänge |
| 35 | 6 | L6: Umkehraufgabe — ausgefallene Arbeiter |
| 36 | 6 | L6: Behauptung begründen — y(0) = 0 bei Proportionalität (MC) |

### 8-bruchterme-grundlagen

| id | Level | Kriterium |
|---|---|---|
| 16 | 3 | L3: vollständig kürzen, Nenner angeben (Formel entfernt) |
| 17 | 3 | L3: ausklammern, kürzen, Wert (Formel entfernt) |
| 19 | 4 | L4: Verfahren erkennen — welcher Term ist kürzbar (MC, Auswahl ist die Leistung) |
| 20 | 4 | L4: Umkehraufgabe — Erweitern auf vorgegebenen Nenner |
| 21 | 4 | L4: Umkehraufgabe — a aus Definitionslücke |
| 22 | 4 | L4: Modell aus Text — Rechteckseite als Bruchterm (MC) |
| 23 | 4 | L4: Verfahren wählen — Definitionslücke bei x² − 16 |
| 24 | 4 | L4: Verfahren wählen — ausklammern, kürzen, Wert |
| 25 | 5 | L5: Fehler finden — Kürzen aus Summen (MC) |
| 26 | 5 | L5: Parameter aus zwei Bedingungen — a, b aus Lücke und Wert |
| 27 | 5 | L5: zweischrittig — kürzen, dann Wert 12 rückwärts |
| 28 | 5 | L5: Fehler finden — Faktor x im Nenner übersehen (MC) |
| 29 | 5 | L5: Sachaufgabe zweischrittig — Seitendifferenz bei konstanter Fläche |
| 30 | 5 | L5: Parameter — c für Kürzbarkeit zu x |
| 31 | 6 | L6: Behauptung prüfen — Gleichwertigkeit trotz Definitionslücke (MC) |
| 32 | 6 | L6: Umkehraufgabe — Term aus Lücke und Nullstelle, dann Wert |
| 33 | 6 | L6: Behauptung prüfen — Zähler null ⇔ Term null? (MC) |
| 34 | 6 | L6: Fallunterscheidung — Vorzeichen eines Bruchterms, ganze Zahlen zählen |
| 35 | 6 | L6: Umkehraufgabe — k aus gekürztem Term |
| 36 | 6 | L6: Sonderfall — Nenner x² + 1 ohne Definitionslücke (MC) |

### 8-vektoren-2d (Prozent- und Zinsrechnung)

| id | Level | Kriterium |
|---|---|---|
| 1 | 1 | L1: Prozentwert direkt (25 % von 160) |
| 2 | 1 | L1: Prozent → Bruch (MC) |
| 3 | 1 | L1: Bruch → Prozent |
| 4 | 1 | L1: Prozentsatz direkt (12 von 48) |
| 5 | 1 | L1: Grundwert direkt (10 %) |
| 6 | 1 | L1: Dezimalzahl → Prozent (MC) |
| 7 | 2 | L2: Prozentwert mit Dreisatz |
| 8 | 2 | L2: Grundwert mit Dreisatz |
| 9 | 2 | L2: Prozentsatz mit Dreisatz |
| 10 | 2 | L2: Prozentsatz über 100 % |
| 11 | 2 | L2: Rechenweg für Prozentsatz erkennen (MC) |
| 12 | 2 | L2: Prozentsatz 175 % |
| 13 | 3 | L3: Rabatt |
| 14 | 3 | L3: Mehrwertsteuer |
| 15 | 3 | L3: Jahreszinsen |
| 16 | 3 | L3: Skonto |
| 17 | 3 | L3: Steigerung in Prozent, richtiger Grundwert (MC) |
| 18 | 3 | L3: Steigerung um 20 % |
| 19 | 4 | L4: Grundaufgabe erkennen — alter Preis nach Senkung (verminderter Grundwert) |
| 20 | 4 | L4: Zinsen für Monate |
| 21 | 4 | L4: Ratenzahlung — Aufschlag in Prozent |
| 22 | 4 | L4: Grundaufgabe erkennen — welche Größe ist gesucht (MC) |
| 23 | 4 | L4: Zinsen für Tage |
| 24 | 4 | L4: Grundaufgabe erkennen — Einkaufspreis bei Aufschlag (vermehrter Grundwert) |
| 25 | 5 | L5: zweistufige Änderung +20 % / −20 % |
| 26 | 5 | L5: Fehler finden — Prozentpunkte vs. Prozent (MC) |
| 27 | 5 | L5: Kapital aus Zinsen und Zinssatz |
| 28 | 5 | L5: Fehler finden — falscher Grundwert beim Rückrechnen (MC) |
| 29 | 5 | L5: zweischrittig — zwei Jahre mit mitverzinsten Zinsen |
| 30 | 5 | L5: zweistufige Änderung rückwärts — Neupreis |
| 31 | 6 | L6: Behauptung prüfen — 2 × 10 % = 20 %? (MC) |
| 32 | 6 | L6: Zinssatz aus zwei Kontoständen |
| 33 | 6 | L6: Angebote vergleichen mit Fallunterscheidung — Prozent vs. Festbetrag (MC) |
| 34 | 6 | L6: Umkehraufgabe — Zinsen aus Endkapital |
| 35 | 6 | L6: Umkehraufgabe — p für Rückkehr zum Ausgangspreis |
| 36 | 6 | L6: Angebote vergleichen mit Fallunterscheidung — Zinssatz vs. Gebühr (MC) |

## Block B — Geometrie (inkl. Umzug aus Kl. 9 nach TH 2.2.3)

Kreisteile (Sektor/Bogen) bewusst aus `8-kreise` herausgenommen (eigener Trainer `10-kreissektor`); Halb-/Viertelkreis bleiben. Bei den drei Umzug-Trainern L1–L3 auf Kl.-8-Vorwissen geprüft: √ nur als Taschenrechner-Operation, keine Wurzelgesetze (a√2, a/2·√3, 6√3 entfernt), keine Trigonometrie (Neigungswinkel raus), keine Strahlensätze, keine quadratischen Gleichungen. Kugel nach TH in `9-raumgeometrie-pyramide-kegel` eingebaut (L2 #9, L5 #27, L6 #31/#35).

| Trainer | Audit-Befund | Geändert |
|---|---|---|
| 8-kreise | KEIN_AFB3 L5/L6; KOLLAPS L3/L4; DUENNER_WEG L1 | L4–L6 neu (18): Umfang↔Fläche-Umkehr, Tischdecke, Rechnung wählen (MC), Radumdrehungen, Kiesweg-Ring; Fehler d statt r (MC), Halbkreisrahmen rückwärts, Düngerbeutel, Fehler r² im Umfang (MC), r aus Summe zweier Umfänge, Laufbahn; Flächenaddition 3/4/7 (MC), U = A, halbe Fläche im Ring, Halbkreisumfang (MC), Äquatorseil, Pizzapreis pro cm² (MC). L1 #4 (π-Wert MC) → numerisch, damit MC ≤ 50 %; L3 #16 „Aussenradius" → „Außenradius" |
| 8-raumgeometrie-grund | KEIN_AFB3 L5/L6; DUENNER_WEG L1, L2 | L5/L6 neu (12): Fehler d statt r beim Zylinder (MC), Wasserhöhe im Aquarium, Quader 1:1:3 aus Volumen, Fehler 4 statt 6 Würfelflächen (MC), Regentonne Restvolumen, Volumen aus Mantel; Kanten ×2 → Oberfläche ×4 (MC), Würfeloberfläche aus Quadervolumen, Radienverhältnis bei 1 L / vierfacher Höhe, „2·8 = 4·2"-Begründung (MC), größter Zylinder im Würfel, Firsthöhe aus Dachvolumen. L1 #4 (Einheit MC) → Würfeloberfläche numerisch (MC ≤ 50 %); Wege L1 #5/#6, L2 #7/#8/#9/#10 ausgeführt |
| 9-pythagoras (Umzug) | KEIN_AFB3 L5/L6; KOLLAPS L3/L4, L4/L5; DUENNER_WEG L2–L5 | L4–L6 neu (18). Kl.-8-Vorwissen: L1 #3 (MC „Was ist c") → numerisch 8/15/17; L3 #15 Tipp „d = a√2" → d² = 4²+4²; L3 #17 Tipp „h = a/2·√3" → Höhe halbiert Grundseite; Höhensatz/Kathetensatz (alt L5 #30, L6 #32), Trigonometrie und Koordinatenabstände entfernt; Wege L1/L2/L3 ausgeführt |
| 9-raumgeometrie-prisma-zylinder (Umzug) | KEIN_AFB3 L5/L6; KOLLAPS L3/L4, L4/L5; DUENNER_WEG alle | L4–L6 neu (18). Kl.-8-Vorwissen: L3 #15 Sechseckprisma mit 6√3 → Trapezprisma (168); L1 #6 „π ≈ 3,14" bei exakter Lösung entfernt; gleichseitiges Dreieck (√3, alt L5 #25) und Raumdiagonale-Formel (alt L5 #26) raus; Wege L1 #4/#5, L2 #9/#12, L3 #13 ausgeführt |
| 9-raumgeometrie-pyramide-kegel (Umzug) | KEIN_AFB3 L5; KOLLAPS L4/L5; DUENNER_WEG L1, L3, L5, L6 | L4–L6 neu (18). Kl.-8-Vorwissen: L2 #9 (Höhe über 4√2) → Kugelvolumen r = 4; Neigungswinkel mit tan (alt L6 #33), Kegelstumpf-Formel (alt L5 #27), Sechseckpyramide 24√3 (alt L5 #26), Sektorwinkel des Mantels (alt L6 #34) raus; L3 #14 Cheops-Frage mit Einheiten präzisiert; Wege L1 #4, L2 #11/#12, L3 #17 ausgeführt |

### 8-kreise

| id | Level | Kriterium |
|---|---|---|
| 4 | 1 | L1: Radius aus Durchmesser 9 cm (ersetzt π-Wert-MC) |
| 19 | 4 | L4: Umkehraufgabe — Umfang aus Fläche |
| 20 | 4 | L4: Modell aus Text — Tischdecke, Überhang vergrößert den Radius |
| 21 | 4 | L4: Rechnung wählen — Beeteinfassung, U aus d (MC, Auswahl ist die Leistung) |
| 22 | 4 | L4: Umkehraufgabe — Fläche aus Umfang |
| 23 | 4 | L4: Modell aus Text — vollständige Radumdrehungen auf 100 m |
| 24 | 4 | L4: Modell aus Text — Kiesweg als Kreisring erkennen |
| 25 | 5 | L5: Fehler finden — Durchmesser in die Flächenformel eingesetzt (MC) |
| 26 | 5 | L5: Größe aus Umfang — Halbkreisrahmen (Bogen + Durchmesser) rückwärts |
| 27 | 5 | L5: zweischrittig — Radius aus Umfang, Fläche, Beutel aufrunden |
| 28 | 5 | L5: Fehler finden — Radius im Umfang quadriert (MC) |
| 29 | 5 | L5: Größe aus zwei Bedingungen — r aus Summe der Umfänge und Verhältnis 1:3 |
| 30 | 5 | L5: Sachaufgabe zweischrittig — Laufbahn mit zwei Halbkreisen |
| 31 | 6 | L6: Behauptung prüfen — Flächen addieren sich über r², nicht über r (MC) |
| 32 | 6 | L6: Sonderfall — U = A zahlenmäßig, r = 2 |
| 33 | 6 | L6: Umkehraufgabe — Innenradius für halbe Fläche (√50) |
| 34 | 6 | L6: Behauptung prüfen — Halbkreisumfang ≠ halber Umfang (MC) |
| 35 | 6 | L6: Sonderfall — Äquatorseil, Ergebnis unabhängig vom Radius |
| 36 | 6 | L6: Fallunterscheidung — Pizzapreis pro cm² (MC) |

### 8-raumgeometrie-grund

| id | Level | Kriterium |
|---|---|---|
| 4 | 1 | L1: Würfeloberfläche Kante 2 (ersetzt Einheiten-MC) |
| 25 | 5 | L5: Fehler finden — Durchmesser statt Radius im Zylindervolumen (MC) |
| 26 | 5 | L5: zweischrittig — Wasserhöhe aus Litern und Grundfläche |
| 27 | 5 | L5: Größe aus zwei Bedingungen — Quader a·a·3a = 375 |
| 28 | 5 | L5: Fehler finden — vier statt sechs Würfelflächen (MC) |
| 29 | 5 | L5: Sachaufgabe zweischrittig — Regentonne, Restvolumen |
| 30 | 5 | L5: zweischrittig — Radius aus Mantel, dann Volumen |
| 31 | 6 | L6: Behauptung prüfen — Kanten ×2 → Oberfläche ×4, Volumen ×8 (MC) |
| 32 | 6 | L6: Umkehraufgabe — Würfelkante aus Quadervolumen, dann Oberfläche |
| 33 | 6 | L6: Fallunterscheidung — Radienverhältnis bei gleichem Volumen, vierfacher Höhe |
| 34 | 6 | L6: Behauptung prüfen — gleiche Volumina, falsche Begründung r·h statt r²·h (MC) |
| 35 | 6 | L6: Sonderfall — Abfall beim größten Zylinder im Würfel, unabhängig von a |
| 36 | 6 | L6: Umkehraufgabe — Firsthöhe aus Dachvolumen (zwei Schritte) |

### 9-pythagoras (Umzug)

| id | Level | Kriterium |
|---|---|---|
| 3 | 1 | L1: c aus 8 und 15 (ersetzt MC „Was ist c") |
| 15 | 3 | L3: Quadratdiagonale ohne a√2 (Tipp/Weg umgestellt) |
| 17 | 3 | L3: Höhe im gleichseitigen Dreieck ohne √3-Formel |
| 19 | 4 | L4: Modell aus Text — Drachenhöhe (Kathete) |
| 20 | 4 | L4: Umkehraufgabe — Rechteckfläche aus Diagonale und Breite |
| 21 | 4 | L4: Verfahren wählen — Kathete aus Hypotenuse und Kathete (MC) |
| 22 | 4 | L4: Modell aus Text — Fußballplatz-Diagonale |
| 23 | 4 | L4: Umkehraufgabe — Quadratseite aus Diagonale |
| 24 | 4 | L4: Modell aus Text — Rampenlänge |
| 25 | 5 | L5: Fehler finden — Kathete länger als Hypotenuse (MC) |
| 26 | 5 | L5: Sachaufgabe zweischrittig — geknickter Baum, Höhe = Stumpf + Hypotenuse |
| 27 | 5 | L5: Größe aus zwei Bedingungen — Höhe aus Umfang und Basis |
| 28 | 5 | L5: Fehler finden — „fast gleich" beim Kehrsatz (MC) |
| 29 | 5 | L5: zweischrittig — Kabel über Straße, Höhendifferenz zuerst |
| 30 | 5 | L5: Kathete über Höhe — Umfang eines gleichschenkligen Dreiecks |
| 31 | 6 | L6: Behauptung prüfen — Katheten ×2 → Hypotenuse ×2 (MC) |
| 32 | 6 | L6: Umkehraufgabe — Fläche aus Umfang und Diagonale (binomische Formel) |
| 33 | 6 | L6: Fallunterscheidung — dritte Seite als Hypotenuse oder Kathete |
| 34 | 6 | L6: Behauptung prüfen — a² + b² < c² ⇒ stumpfwinklig (MC) |
| 35 | 6 | L6: Umkehraufgabe — Quaderhöhe aus Raumdiagonale (zweimal Pythagoras) |
| 36 | 6 | L6: Sonderfall — Seite des gleichseitigen Dreiecks aus der Höhe |

### 9-raumgeometrie-prisma-zylinder (Umzug)

| id | Level | Kriterium |
|---|---|---|
| 6 | 1 | L1: Zylindervolumen, „π ≈ 3,14" entfernt (Lösung exakt) |
| 15 | 3 | L3: Trapezprisma (ersetzt Sechseckprisma mit 6√3) |
| 19 | 4 | L4: Rechnung wählen — Zeltdach als Dreiecksprisma (MC) |
| 20 | 4 | L4: Umkehraufgabe — Durchmesser aus Volumen und Höhe |
| 21 | 4 | L4: Modell aus Text — Rohrinhalt in Litern |
| 22 | 4 | L4: Umkehraufgabe — Würfelvolumen aus Oberfläche |
| 23 | 4 | L4: Modell aus Text — Blech für Dreiecksprisma, Hypotenuse via Pythagoras |
| 24 | 4 | L4: Umkehraufgabe — Quaderhöhe aus Oberfläche |
| 25 | 5 | L5: Fehler finden — Mantel als Oberfläche (MC) |
| 26 | 5 | L5: zweischrittig — Steinvolumen aus Wasseranstieg |
| 27 | 5 | L5: Größe aus zwei Bedingungen — h = d und Mantel → Volumen |
| 28 | 5 | L5: Fehler finden — Quaderoberfläche als 2·V (MC) |
| 29 | 5 | L5: Sachaufgabe zweischrittig — Kerzen aus Wachsblock, abrunden |
| 30 | 5 | L5: zweischrittig — Quaderhöhe bei gleichem Volumen wie Würfel |
| 31 | 6 | L6: Behauptung prüfen — r/2 und 2h halbiert das Volumen (MC) |
| 32 | 6 | L6: Sonderfall — Mantel = Boden + Deckel ⇔ h = r |
| 33 | 6 | L6: Fallunterscheidung — Blatt um kurze oder lange Seite rollen |
| 34 | 6 | L6: Behauptung prüfen — O = V nur bei a = 6 (MC) |
| 35 | 6 | L6: Umkehraufgabe — Hypotenuse des Querschnitts aus Volumen |
| 36 | 6 | L6: Sonderfall — Oberfläche beim Zersägen ×4 (+300 %) |

### 9-raumgeometrie-pyramide-kegel (Umzug)

| id | Level | Kriterium |
|---|---|---|
| 9 | 2 | L2: Kugelvolumen r = 4 (TH nennt Kugel explizit; ersetzt Höhe über 4√2) |
| 14 | 3 | L3: Cheops-Pyramide, Einheiten präzisiert |
| 19 | 4 | L4: Umkehraufgabe — Grundkante aus Volumen und Höhe |
| 20 | 4 | L4: Rechnung wählen — Sektglas, d statt r (MC) |
| 21 | 4 | L4: Modell aus Text — Zeltstoff = vier Dreiecke (Seitenhöhe gegeben) |
| 22 | 4 | L4: Umkehraufgabe — Kegelhöhe aus Volumen |
| 23 | 4 | L4: Verfahren wählen — Radius aus Mantellinie und Höhe, dann Volumen |
| 24 | 4 | L4: Modell aus Text — Partyhut nur Mantel |
| 25 | 5 | L5: Fehler finden — Faktor 1/3 vergessen (MC) |
| 26 | 5 | L5: zweischrittig — Kegeloberfläche, s zuerst |
| 27 | 5 | L5: Kugel — Volumen aus Umfang des Großkreises |
| 28 | 5 | L5: Fehler finden — h statt s im Kegelmantel (MC) |
| 29 | 5 | L5: Sachaufgabe zweischrittig — Sandhaufen, Fahrten aufrunden |
| 30 | 5 | L5: Größe aus zwei Bedingungen — Volumen aus Seitenkante und Höhe (a² = d²/2) |
| 31 | 6 | L6: Behauptung prüfen — Kugelradius ×2 → Oberfläche ×4 (MC) |
| 32 | 6 | L6: Umkehraufgabe — Kegelhöhe bei Volumen der Halbkugel |
| 33 | 6 | L6: Sonderfall — Abfall bei Pyramide im Würfel, unabhängig von a |
| 34 | 6 | L6: Behauptung prüfen — größerer Radius bei gleicher Mantellinie, Begründung (MC) |
| 35 | 6 | L6: Kugel — Volumen aus Oberfläche |
| 36 | 6 | L6: Sonderfall — Pyramide mit gleichseitigen Seitenflächen (halbes Oktaeder) |

## Block C — Stochastik (TH 2.2.4)

Kein Binomialkoeffizient als Formel (alt `8-stoch-laplace` L6 #31/#32/#35 mit 6 aus 49 und (n über k) entfernt), keine bedingte Wahrscheinlichkeit; Mengenschreibweise (A ∪ B, A ∩ B) auf L6 eingeführt.

| Trainer | Audit-Befund | Geändert |
|---|---|---|
| 8-stoch-laplace | KEIN_AFB3 L6; KOLLAPS L2/L3 (bleibt), L3/L4; DUENNER_WEG L2, L3 | L4–L6 neu (18): rote Kugeln aus P, Augensumme 9, MISSISSIPPI (MC), Felder aus Gegenereignis, Münze+Würfel, Vielfache von 4; „drei Ergebnisse" bei zwei Münzen (MC), Bonbon gegessen, Urne aus Differenz und P, Summe 5 vs. 10 (MC), Summe ≥ 6 über Gegenereignis, Junge ohne Brille; Summen nicht laplace (MC), Felderzahl aus 3 Gewinnfeldern, P(A ∪ B) mit Mengen, Lotto 1–6 (MC), blaue Kugeln für P = 1/4, P(A ∩ B) = 0 (Pasch und Summe 7). Wege L1 #1/#5, L2 #10/#12, L3 #16/#17 ausgeführt; typografische Anführungszeichen |
| 8-stoch-zaehlprinzip | KEIN_AFB3 L5; DUENNER_WEG alle | L5/L6 neu (12): ohne Zurücklegen wie mit gerechnet (MC), genau einmal grün, Ringziffern aus 512, genau 3 Kopf bei 4 Würfen (MC), höchstens ein Treffer, zweite Kugel rot; 3·½ = 1,5 (MC), blaue Kugeln aus P(rot,rot) = 1/16, gleiche Farbe ohne Zurücklegen, „zwei von vier Pfaden" (MC), p aus (1−p)² = 0,49, Anna neben Ben. Wege L1 #5/#6 ausgeführt; „schiessen" → „schießen", „80%" → „80 %" |

### 8-stoch-laplace

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | L4: Umkehraufgabe — Anzahl aus P und Gesamtzahl |
| 20 | 4 | L4: Modell aus Text — Augensumme 9, Paare zählen |
| 21 | 4 | L4: Verfahren erkennen — MISSISSIPPI, Mehrfachbuchstaben zählen (MC) |
| 22 | 4 | L4: Umkehraufgabe über Gegenereignis — blaue Felder |
| 23 | 4 | L4: Modell aus Text — Münze und Würfel, 12 Paare |
| 24 | 4 | L4: Modell aus Text — Vielfache von 4 bis 30 |
| 25 | 5 | L5: Fehler finden — ungleich wahrscheinliche „Ergebnisse" (MC) |
| 26 | 5 | L5: zweischrittig — Grundgesamtheit nach Entnahme |
| 27 | 5 | L5: Größe aus zwei Bedingungen — Kugelzahl aus Differenz und P (lineare Gleichung) |
| 28 | 5 | L5: Fehler finden — Zerlegungen statt Paare, Pasch zählt einmal (MC) |
| 29 | 5 | L5: zweischrittig — Summe ≥ 6 über Gegenereignis |
| 30 | 5 | L5: Sachaufgabe — Teilgruppe abzählen (Junge ohne Brille) |
| 31 | 6 | L6: Behauptung prüfen — Augensummen sind nicht laplace (MC) |
| 32 | 6 | L6: Umkehraufgabe — Felderzahl aus 3 Gewinnfeldern |
| 33 | 6 | L6: Mengenschreibweise — P(A ∪ B), Doppelzählung vermeiden |
| 34 | 6 | L6: Behauptung prüfen — Lotto 1–6 gleich wahrscheinlich (MC) |
| 35 | 6 | L6: Umkehraufgabe — blaue Kugeln für P(rot) = 1/4 |
| 36 | 6 | L6: Sonderfall — unvereinbare Ereignisse, P(A ∩ B) = 0 |

### 8-stoch-zaehlprinzip

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | L5: Fehler finden — ohne Zurücklegen wie mit gerechnet (MC) |
| 26 | 5 | L5: zweischrittig — zwei Pfade für „genau einmal grün" |
| 27 | 5 | L5: Umkehraufgabe — Ringziffern aus n³ = 512 |
| 28 | 5 | L5: Fehler finden — vierter Wurf im Pfad vergessen, Pfade nicht gezählt (MC) |
| 29 | 5 | L5: Sachaufgabe — „höchstens ein Treffer" über Gegenereignis |
| 30 | 5 | L5: zweischrittig — zweite Kugel rot über zwei Pfade |
| 31 | 6 | L6: Behauptung prüfen — 3·½ = 1,5, Wahrscheinlichkeit > 1 (MC) |
| 32 | 6 | L6: Umkehraufgabe — blaue Kugeln aus p² = 1/16 |
| 33 | 6 | L6: Fallunterscheidung — beide rot oder beide blau |
| 34 | 6 | L6: Behauptung prüfen — Pfade ohne Zurücklegen nicht gleich wahrscheinlich (MC) |
| 35 | 6 | L6: Umkehraufgabe — p aus (1−p)² = 0,49 |
| 36 | 6 | L6: Sonderfall — Nachbarpaar in 4! Sitzordnungen |
