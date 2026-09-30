# Klasse 10, Block B (Trigonometrie und Kreis) — Überarbeitung je Trainer (Stand 2026-09-30)

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

## 10-trig-einheitskreis

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | L5: Fehler in vorgelegter Rechnung — Vorzeichen im II. Quadranten (MC) |
| 26 | 5 | L5: zwei Schritte — Kreisgleichung und Quadrantenlage |
| 27 | 5 | L5: Bedingung übersetzen — \(\sin\alpha=\cos\alpha\) plus Quadrant |
| 28 | 5 | L5: zwei Schritte — Bogenmaß in Grad, Quadrant, Referenzwinkel |
| 29 | 5 | L5: Umkehraufgabe — Bogenlänge als Bogenmaß, Umrechnung |
| 30 | 5 | L5: Parameter — Punkt \(P(a\mid 2a)\) auf dem Einheitskreis |
| 31 | 6 | L6: Behauptung prüfen — \(\sin(\alpha+180°)\) (MC, Gegenbeispiel) |
| 32 | 6 | L6: Anzahl über Schnittpunkte mit \(y=x\) |
| 33 | 6 | L6: Behauptung widerlegen — \(\sin^4+\cos^4\) nicht konstant |
| 34 | 6 | L6: Periodizität — kleinster nichtnegativer Winkel zu \(-1000°\) |
| 35 | 6 | L6: Maximum von \(\sin\alpha+\cos\alpha\) über Quadrieren |
| 36 | 6 | L6: Behauptung prüfen — Randfall \(0°/360°\) (MC) |

## 10-trig-gleichungen

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

## 10-trig-sinusfunktion

| id | Level | Kriterium |
|---|---|---|
| 20 | 4 | MC-Optionen auf gleiche Länge gebracht |
| 25 | 5 | L5: Parameter aus zwei Angaben — Höchstwert und Periode |
| 26 | 5 | L5: Amplitude aus Schwankungsbereich (zwei Schritte) |
| 27 | 5 | L5: \(b\) aus halber Periode, dann Umrechnung |
| 28 | 5 | L5: Fehler finden — Periode multipliziert statt dividiert (MC) |
| 29 | 5 | L5: Verschiebung aus steigender Nullstelle |
| 30 | 5 | L5: Anzahl Hochpunkte im Intervall aus der Periode |
| 31 | 6 | L6: Behauptung prüfen — Verdopplung von \(b\) (MC) |
| 32 | 6 | L6: Modellierung — Tag der größten Tageslänge |
| 33 | 6 | L6: Parameter aus zwei Bedingungen (Hoch- und Tiefpunkt) |
| 34 | 6 | L6: Umkehraufgabe — \(a\) aus der Nullstellenanzahl |
| 35 | 6 | L6: Behauptung prüfen — \(\sin(x+\frac{\pi}{2}) = \cos x\) (MC) |
| 36 | 6 | L6: Periode aus dem Abstand Mittellage–Hochpunkt (Viertelperiode) |

## 10-trig-sinussatz-kosinussatz

| id | Level | Kriterium |
|---|---|---|
| 13–18 | 3 | L3 entdoppelt: Kosinussatz mit stumpfem Winkel, Winkel aus drei Seiten, Sinussatz erst nach der Winkelsumme — je ein Zwischenergebnis |
| 19 | 4 | L4: Verfahren wählen und Umfang ergänzen |
| 20 | 4 | L4: fehlenden Gegenwinkel selbst beschaffen |
| 21 | 4 | L4: Umkehraufgabe — Winkel aus zwei Seiten und Gegenwinkel |
| 22 | 4 | L4: Modell aus Text (zwei Wege, eingeschlossener Winkel) |
| 23 | 4 | L4: Satzwahl begründen (MC, Auswahl ist die Leistung) |
| 24 | 4 | L4: Umkehraufgabe SSS — stumpfer Winkel aus drei Seiten |
| 25 | 5 | L5: Fehler finden — Vorzeichen von \(\cos 120°\) (MC) |
| 26 | 5 | L5: zwei Sätze nacheinander (Kosinussatz, dann Winkel) |
| 27 | 5 | L5: Parameter über quadratische Gleichung, zwei Lösungen |
| 28 | 5 | L5: Modell aus Text — Peilung, Winkelsumme, Sinussatz |
| 29 | 5 | L5: SSW mit stumpfer Nebenlösung |
| 30 | 5 | L5: gleichschenkliger Sonderfall erkennen, dann Umfang |
| 31 | 6 | L6: Fallunterscheidung SSW — zwei Dreiecke |
| 32 | 6 | L6: Grenzfall \(a = b\sin\alpha\) — genau ein Dreieck |
| 33 | 6 | L6: Behauptung prüfen — Sinuswert legt Winkel nicht fest (MC) |
| 34 | 6 | L6: eindeutiger Bezug ohne Zeichnung (Winkel zwischen \(a\) und \(b\)) |
| 35 | 6 | L6: Fallunterscheidung SSW — kein Dreieck (\(\sin\beta > 1\)) |
| 36 | 6 | L6: Behauptung prüfen — negativer Kosinuswert und Stumpfwinkligkeit (MC) |

## 10-kreissektor

| id | Level | Kriterium |
|---|---|---|
| 24 | 4 | MC-Optionen auf gleiche Länge gebracht, Tipp ohne Antwort |
| 25 | 5 | L5: Umkehraufgabe — Winkel aus dem Sektorumfang (zwei Schritte) |
| 26 | 5 | L5: Bogen aus Fläche über \(A = \frac12 r b\) |
| 27 | 5 | L5: Fehler finden — Umfangs- statt Flächenanteil (MC) |
| 28 | 5 | L5: Radius aus zwei Angaben (\(A\) und \(b\)) |
| 29 | 5 | L5: zusammengesetzte Figur — Sektor minus Dreieck |
| 30 | 5 | L5: Verhältnisaufgabe — Winkel aus Flächenverhältnis |
| 31 | 6 | L6: Behauptung prüfen — Winkel verdoppeln, Radius halbieren (MC) |
| 32 | 6 | L6: Grenzfall — \(r = 2\) macht Bogen- und Flächenmaßzahl gleich |
| 33 | 6 | L6: Ringsektor als Differenz zweier Sektoren |
| 34 | 6 | L6: Transfer — Kegelabwicklung, Bogen wird Grundkreisumfang |
| 35 | 6 | L6: Behauptung prüfen — Segmentanteil hängt vom Winkel ab (MC) |
| 36 | 6 | L6: Umkehraufgabe — Radius aus Flächengleichheit mit einem Quadrat |
