# Klasse 11, Block A1 (Ableitung und Steigung) — Kriterien je Trainer

Welle Task 8, Stand 2026-09-30. Lokale Nachvollziehbarkeit; im Public-HTML stehen die
Kriterien bewusst nicht.

Grundlage: Rubrik aus `2026-09-26-lehrplan-th-und-level-progression-plan.md`, Befunde aus
`../audit/audit-2026-09-19-mathepfade.md` (Zeilen 108–112, 122 und der offene Punkt in
Zeile 240 ff.). Lesart Kl. 11 durchgängig:

- **L4 (AFB II)**: Verfahren selbst wählen, Modell aus einem Sachtext aufstellen, Umkehraufgabe
  (Parameter oder Stelle gesucht statt Funktionswert).
- **L5 (AFB III)**: zwei Verfahren kombinieren, Parameter aus zwei Bedingungen, Fehler in einer
  vorgelegten Rechnung finden. **Keine** Auswertung an der Stelle \(x = 0\) (Rubrik-Verbot; sie
  trivialisiert Produkt- und Kettenregel).
- **L6 (AFB III, Abi-Format gA)**: mehrschrittige Aufgabe mit Begründungsanteil, Formulierungen
  „Zeigen Sie …“, „Beurteilen Sie …“, Sachkontext, Fallunterscheidung/Grenzfall.

Jede Lösung mit dem Wolfram-MCP nachgerechnet (auch die jeweils *nicht* gefragten Fälle);
Bilder L5 und L6 je Trainer mit `tests/bild.py` erzeugt und angesehen.

## Abgrenzung der vier Trainer gegeneinander und gegen die Nachbarblöcke

| Trainer | Inhalt |
|---|---|
| 11-ableitungsregeln | Potenz-, Faktor-, Summenregel, negative Exponenten, zweite Ableitung, Parameter in der Funktionsgleichung. **Ohne** Produkt- und Kettenregel (die liegen im Nachbartrainer) |
| 11-ableitung-ketten-produkt | Ketten- und Produktregel, e-Funktion und Trigonometrie als Bausteine, verzahnte Anwendung beider Regeln |
| 11-aenderungsrate | mittlere und lokale Änderungsrate, Differenzenquotient, h-Methode, Rate gegen Bestand im Sachkontext. **Ohne** Tangentengleichungen |
| 11-tangenten-normalen | Tangente und Normale aufstellen, Berührbedingung, Tangente durch einen vorgegebenen Punkt, Steigungswinkel |

„Tangente aufstellen“ gehört ausschließlich zu `11-tangenten-normalen`; die entsprechenden
Aufgaben sind aus `11-aenderungsrate` entfernt worden. Extrem- und Wendepunkte bleiben den
Trainern `11-extrempunkte-wendepunkte`, `11-monotonie-kruemmung` und
`11-kurvendiskussion-ganzrational` vorbehalten — hier wird nur nach „waagerechter Tangente“
im Sinne von \(f'(x) = 0\) gefragt, nie nach Art oder Anzahl von Extrempunkten.

---

## 11-ableitungsregeln

Audit: KEIN_AFB3 L5; KOLLAPS L2/L3; DUENNER_WEG (Stufen 1, 4). Der im Audit offen gelassene
Punkt (10 Aufgaben ab Stufe 4 werden an der Stelle \(x = 0\) ausgewertet) war beim Öffnen der
Datei bereits behoben — das Level-Gate meldete keine Warnung mehr. Die Produkt- und
Kettenregelaufgaben der alten Stufen 4–6 sind trotzdem entfallen: sie doppelten
`11-ableitung-ketten-produkt` (#33/#34 waren dort wortgleich vorhanden).

| id | Level | Kriterium |
|---|---|---|
| 1, 2, 3 | 1 | DUENNER_WEG behoben: Lösungsweg zeigt jetzt Potenzregel und Einsetzen getrennt |
| 19 | 4 | Verfahren wählen: \(f'=0\) und Ausklammern, Nebenlösung \(x=0\) durch Bedingung ausgeschlossen |
| 20 | 4 | Umkehraufgabe: Faktor \(a\) aus \(f'(2)=36\) |
| 21 | 4 | Modell aus Sachtext: Bestand, momentan unveränderlich |
| 22 | 4 | Rückwärts denken: welche Funktion hat die gegebene Ableitung (MC) |
| 23 | 4 | Verfahren wählen: Bruch gliedweise zerlegen statt Quotientenregel |
| 24 | 4 | Umkehraufgabe mit negativem Exponenten, Vorzeichenfall \(\pm 3\) |
| 25 | 5 | Parameter aus zwei Bedingungen (\(f'(1)=0\), \(f'(2)=9\)) |
| 26 | 5 | Fehler in vorgelegter Rechnung: Nenner abgeleitet statt umgeschrieben (MC) |
| 27 | 5 | zwei Verfahren: \(f'\) und \(f''\) aufstellen, quadratische Gleichung, beide Lösungen geprüft |
| 28 | 5 | \(f'=0\) bei negativem Exponenten, Lösungsmenge \(\pm 2\) auf Bereich eingeschränkt |
| 29 | 5 | Sachkontext, Vorzeichenwechsel der Rate, Nebenlösung außerhalb des Zeitraums |
| 30 | 5 | Parameterbedingung mit Grenzfall \(p = 0\) ausdrücklich diskutiert (MC) |
| 31 | 6 | Abi-Format: „Zeigen Sie … genau zwei Tage“, Sachkontext Wasserstand, beide Lösungen im Intervall |
| 32 | 6 | zwei Bedingungen, Term mit \(x^{-1}\), Probe im Lösungsweg |
| 33 | 6 | Behauptung prüfen: \(f'=3(x+1)^2\), doppelte Nullstelle ist eine Stelle, nicht zwei (MC) |
| 34 | 6 | „Zeigen Sie, dass f überall steigt“ über quadratische Ergänzung, kleinster Ableitungswert |
| 35 | 6 | Abi-Format: stärkstes Wachstum über \(U''=0\), Sachkontext Umsatz |
| 36 | 6 | Behauptung prüfen im Sachkontext: Wachstum ist eine Aussage über die Rate (MC) |

## 11-ableitung-ketten-produkt

Audit: KEIN_AFB3 L5 **und** L6; KOLLAPS L2/L3 **und** L5/L6; KURZ (Stufen 1, 2, 3, 4, 6);
DUENNER_WEG (Stufen 1, 2, 3) — der dünnste Trainer des Blocks. Deshalb **alle 36 Aufgaben**
überarbeitet: Stufe 1 nur sprachlich (volle Fragesätze, Lösungswege), Stufe 2–6 neu.

Der Trainer wertete vorher 14 Aufgaben an der Stelle \(x = 0\) aus (darunter zehn ab Stufe 4);
dort fällt bei Produkt- und Kettenregel jeweils ein Summand weg, die Aufgabe prüft die Regel
also gar nicht. Alle Auswertungsstellen sind jetzt von null verschieden, und ab Stufe 5 wird
statt eines Funktionswerts die Ableitungsfunktion selbst bzw. die Stelle mit \(f'(x)=0\) verlangt.

| id | Level | Kriterium |
|---|---|---|
| 1–6 | 1 | KURZ/DUENNER_WEG behoben: vollständige Fragesätze, Lösungsweg nennt innere und äußere Funktion |
| 7–12 | 2 | Kettenregel an Klammerpotenzen, Auswertung an \(1, 2, -2, 1, 2\) statt an \(0\); Lösungsweg mit \(u, u'\) |
| 13–18 | 3 | Kettenregel an der e-Funktion, Auswertung an \(1\) bzw. \(-1\); Vorzeichenfallen benannt |
| 19 | 4 | Produktregel an negativer Stelle, Ausklammern von \(e^x\) |
| 20 | 4 | Produktregel mit \(\sin\), Werte bei \(\pi\) |
| 21 | 4 | Ableitungsterm gesucht, Vereinfachung \(e^x(x-1+1)=xe^x\) (MC) |
| 22 | 4 | Umkehraufgabe: Parameter im Exponenten aus \(f'(1)=2e^2\), Eindeutigkeit begründet |
| 23 | 4 | Verfahren wählen: Kettenregel oder ausmultiplizieren, Probe im Lösungsweg |
| 24 | 4 | Modell aus Sachtext: Wirkstoffkonzentration, Rate nach 4 Stunden |
| 25 | 5 | Produkt + Kette, \(f'=0\) über Ausklammern; Eindeutigkeit aus der Linearität |
| 26 | 5 | zwei Lösungen, beide geprüft, größere gefragt |
| 27 | 5 | Fehler in vorgelegter Rechnung: fehlende Nachdifferenzierung (MC) |
| 28 | 5 | Parameter aus der Bedingung \(f'(1)=0\), Probe |
| 29 | 5 | Produkt + Kette führen auf \(\tan x = 1\); zweite Lösung außerhalb des Intervalls |
| 30 | 5 | Ableitungsfunktion selbst verlangt (Wurzel, Kettenregel), Distraktoren sind die typischen Teilfehler (MC) |
| 31 | 6 | Abi-Format: „Zeigen Sie … genau einen Höchstwert“, Sachkontext Wirkstoff, Vorzeichenargument |
| 32 | 6 | Behauptung prüfen: Produkt aus \(k\) und \(e^{kx}\) wird nie null (MC) |
| 33 | 6 | Fallunterscheidung über die Diskriminante: \(c<1\), \(c=1\), \(c>1\) |
| 34 | 6 | zwei Modelle vergleichen, Exponentialgleichung, Deutung des Ergebnisses |
| 35 | 6 | quadratische Gleichung mit zwei reellen Lösungen, kleinere gefragt |
| 36 | 6 | Behauptung prüfen mit Probe über \(\sin(2x)\) (MC) |

## 11-aenderungsrate

Audit: KEIN_AFB3 L5; DUENNER_WEG (Stufen 4, 5, 6). Stufe 4 wurde mit neu geschrieben, weil
sie fast vollstaendig aus Tangentenaufgaben bestand — die gehoeren zur Trainer-Abgrenzung nach
`11-tangenten-normalen`. Der Trainer behandelt jetzt ausschliesslich mittlere und lokale
Aenderungsrate, Differenzenquotient und die Unterscheidung von Rate und Bestand im Sachkontext.
Stufe 1-3 (Begriffe, Differenzenquotient, h-Methode) bleiben unveraendert.

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | Umkehraufgabe im Sachkontext: Zeitpunkt zu vorgegebener Momentangeschwindigkeit |
| 20 | 4 | Modell aus Text: zwei Messwerte, mittlere Rate je Stunde |
| 21 | 4 | Begriffsvergleich mittlere/lokale Rate mit Gegenbeispiel im Lösungsweg (MC) |
| 22 | 4 | Umkehraufgabe: Intervallende aus gegebener mittlerer Änderungsrate, Kürzen mit 3. binom. Formel |
| 23 | 4 | Modell aus Text, Vorzeichen der Abflussrate |
| 24 | 4 | Verfahren wählen: höchster Punkt über \(h'(t)=0\) |
| 25 | 5 | zwei Schritte: Anfangsrate bestimmen, dann Bedingung „halb so groß“ |
| 26 | 5 | Fehler in vorgelegter Rechnung: durch die rechte Grenze statt durch die Intervalllänge geteilt (MC) |
| 27 | 5 | zwei Schritte im Sachkontext, Rate bleibt positiv |
| 28 | 5 | Parameter aus zwei Bedingungen, mittlere **und** lokale Rate nebeneinander |
| 29 | 5 | zwei Verfahren kombiniert: Durchschnitts- und Momentangeschwindigkeit gleichsetzen |
| 30 | 5 | Folgerung aus mittlerer Rate \(0\) (Mittelwertsatz anschaulich), Gegenbeispiele im Lösungsweg (MC) |
| 31 | 6 | Abi-Format: „Zeigen Sie … genau einmal“, Vorzeichenwechsel der Rate, Sachkontext Gewässer |
| 32 | 6 | Abi-Format: stärkster Zuwachs über \(B''=0\), Abgrenzung Rate gegen Bestand |
| 33 | 6 | Behauptung prüfen: fallende Rate ist nicht dasselbe wie fallender Bestand (MC) |
| 34 | 6 | allgemeiner Differenzenquotient auf \([-a;a]\), Symmetrie, Anzahl der Lösungen |
| 35 | 6 | Abi-Format: Übergang Zunahme/Abnahme, zweite Lösung außerhalb des Zeitraums |
| 36 | 6 | Behauptung prüfen: mittlere Geschwindigkeit ist Weg durch Zeit, nicht Mittelwert der Tempi (MC) |

## 11-tangenten-normalen

Audit: KEIN_AFB3 L5 **und** L6; KOLLAPS L2/L3 **und** L4/L5; DUENNER_WEG (Stufen 3, 4).
Dazu die beiden Gate-Warnungen `#27` (richtige MC-Option deutlich laenger) und `#34`
(Tipp nannte den Loesungswert 63) — beide Aufgaben sind neu.

Gegen den Kollaps L2/L3 ist Stufe 3 auf **Normalen** zugespitzt (#13-#17): vorher stand dort
dieselbe Aufgabenart wie in Stufe 2 (Tangentensteigung berechnen). Stufe 4 ist neu, weil sie
sich mit Stufe 5 doppelte.

| id | Level | Kriterium |
|---|---|---|
| 13, 15, 16 | 3 | DUENNER_WEG behoben: Lösungsweg zeigt Ableitung, Einsetzen und Kehrwertbildung getrennt |
| 14 | 3 | von Tangenten- auf Normalensteigung umgestellt (Kollaps L2/L3) |
| 17 | 3 | von Tangenten- auf Normalengleichung umgestellt, Distraktoren sind die typischen Fehler (MC) |
| 19 | 4 | Tangente aufstellen und auf der \(y\)-Achse auswerten |
| 20 | 4 | Umkehraufgabe: Stelle zu vorgegebener Steigung, Nebenlösung \(-2\) diskutiert |
| 21 | 4 | Normale aufstellen, Distraktoren mit falschem Vorzeichen bzw. ohne Kehrwert (MC) |
| 22 | 4 | Normalensteigung bei fallender Tangente |
| 23 | 4 | Modell aus Sachtext: Stütze senkrecht zum Hangprofil |
| 24 | 4 | zwei Tangenten aufstellen und gleichsetzen |
| 25 | 5 | Tangente durch einen vorgegebenen Punkt, allgemeine Berührstelle, beide Lösungen |
| 26 | 5 | Berührbedingung als zwei Bedingungen, Probe über die doppelte Nullstelle |
| 27 | 5 | Berührbedingung als Auswahl; MC-Optionen auf gleiche Länge gebracht (Gate-Warnung) |
| 28 | 5 | Normale aufstellen **und** mit der Funktion schneiden (zwei Verfahren) |
| 29 | 5 | Parallelitätsbedingung, beide Lösungen, negative gefragt |
| 30 | 5 | Parameter aus der Bedingung „Tangente durch den Ursprung“ |
| 31 | 6 | Abi-Format: Tangente im Sachkontext (Tunnelprofil), Auswertung auf der Achse |
| 32 | 6 | „Zeigen Sie …“: doppelte Nullstelle, Faktorisierung, allgemeine Aussage \(-2x_0\) |
| 33 | 6 | Behauptung prüfen: Wendetangente berührt und durchsetzt zugleich (MC) |
| 34 | 6 | Steigungswinkel rückwärts: \(60°\) vorgegeben, Stelle gesucht (ersetzt die Aufgabe mit dem verratenen Wert 63) |
| 35 | 6 | Normale durch einen vorgegebenen Punkt, allgemeine Stelle, Deutung des konstanten Summanden |
| 36 | 6 | Grenzfall \(m_t = 0\): Normale ohne Steigung (MC) |

## Offen (bewusst nicht in dieser Welle)

- `11-aenderungsrate` und `11-tangenten-normalen`: KOLLAPS-Reste in Stufe 1/2 werden laut Plan
  nicht angefasst (Stufe 1-3 nur entdoppelt, nicht neu geschrieben).
- `11-ableitungsregeln`: Stufe 2 und 3 unterscheiden sich weiterhin nur durch den negativen
  Exponenten (Audit-Befund KOLLAPS L2/L3); die Rubrik sieht Stufe 1-3 in dieser Welle nicht vor.
- Die Aufgaben zum Steigungswinkel (`11-tangenten-normalen` #34) setzen den Tangens als
  Werkzeug voraus; er kommt in Stufe 1-3 dieses Trainers nicht vor.
