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
