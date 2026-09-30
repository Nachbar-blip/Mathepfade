# Klasse 12, Block B2 (Analytische Geometrie, eA) — Kriterien je Trainer

Welle Task 9, Stand 2026-09-30. Lokale Nachvollziehbarkeit; im Public-HTML stehen die
Kriterien bewusst nicht.

Grundlage: Rubrik aus `2026-09-26-lehrplan-th-und-level-progression-plan.md`, Befunde aus
`../audit/audit-2026-09-19-mathepfade.md` (Zeilen 123–141). Lesart Kl. 12 eA:

- **L4 (AFB II)**: Verfahren selbst wählen, Modell aus einem Sachtext aufstellen, Umkehraufgabe
  (Parameter oder Stelle gesucht statt Ergebniswert). Das Verfahren wird im Text **nicht** genannt.
- **L5 (AFB III)**: zwei Verfahren kombinieren, Parameter aus zwei Bedingungen, Fehler in einer
  vorgelegten Lage- oder Abstandsbestimmung finden.
- **L6 (AFB III, Abi-Format eA)**: mehrschrittig, mit Begründungs- bzw. Beweisanteil
  („Zeigen Sie …“, „Begründen Sie …“, „Beurteilen Sie …“), Sachkontext, Parameter,
  Fallunterscheidung oder Grenzfall.

Jede Lösung mit dem Wolfram-MCP nachgerechnet — bei Lagebeziehungen ausdrücklich alle vier Fälle
(parallel / schneidend / windschief / identisch), bei den Scharen zusätzlich die Grenzfälle des
Parameters. Bilder je Trainer und Stufe mit `tests/bild.py --aufgabe <id>` erzeugt und angesehen.

## Abgrenzung der vier Trainer gegeneinander

| Trainer | Inhalt |
|---|---|
| 12-lk-geom-abstaende | Abstände: Punkt–Punkt, Punkt–Ebene (HNF), Punkt–Gerade (Lotfuß und Kreuzprodukt), parallele Geraden und Ebenen, windschiefe Geraden |
| 12-lk-geom-lagebeziehungen | vollständige Lagediskussion Gerade–Gerade, Gerade–Ebene, Ebene–Ebene, Schnittgerade, drei Ebenen |
| 12-lk-geom-schnittwinkel | Winkel: Vektor–Vektor, Gerade–Gerade, Gerade–Ebene (Sinusformel), Ebene–Ebene |
| 12-lk-dgl (**Ersatz**) | Geraden- und Ebenenscharen im Raum (TH 4.2 eA) |

Gegen die gA-Trainer des Parallelblocks (`12-vektoren-grundlagen`, `12-geraden-raum`, `12-ebenen`,
`12-skalarprodukt`) grenzt sich Block B2 durch die eA-Tiefe ab: dort die Grundlagen, hier
Parameter, Fallunterscheidung und Beweisanteil. Gegen `11-lk-funktionsscharen` grenzt sich der
Ersatz-Trainer dadurch ab, dass dort Funktionsscharen in der Analysis stehen, hier Scharen von
Geraden und Ebenen **im Raum**.

---

### 12-lk-geom-abstaende

Audit: KEIN_AFB3 L5; **KOLLAPS L3/L4**; DUENNER_WEG (Stufe 2). Wegen des Kollapses ist auch
Stufe 4 neu geschrieben: Sie bestand vorher aus denselben Standardrechnungen wie Stufe 3, nur mit
anderer Formel. Jetzt steht in Stufe 4 durchgehend eine Entscheidung (Verfahren wählen,
Sachmodell, Umkehraufgabe). Die Gate-Warnungen `#25` und `#28` (richtige MC-Option deutlich
länger) sind mit den Aufgaben entfallen.

| id | Level | Kriterium |
|---|---|---|
| 7, 11, 12 | 2 | DUENNER_WEG behoben: Lösungsweg zeigt Verbindungsvektor, Betragsbildung und Deutung getrennt |
| 19 | 4 | Lotfußpunkt über die Senkrechtbedingung, ohne dass das Verfahren genannt wird |
| 20 | 4 | Umkehraufgabe: Koordinate eines Punktes aus vorgegebenem Abstand zu einer Geraden, Vorzeichenfall \(\pm 4\) |
| 21 | 4 | Modell aus Sachtext (Rohrleitung); der Lotfußpunkt ist ohne Formel ablesbar |
| 22 | 4 | Verfahren wählen: welcher Arbeitsschritt bei einer nur durch drei Punkte gegebenen Ebene zuerst nötig ist (MC) |
| 23 | 4 | Abstand zweier **paralleler Geraden** — Kollinearität erkennen, dann auf Punkt–Gerade zurückführen |
| 24 | 4 | Abstand zweier paralleler Ebenen über einen bequem gewählten Punkt |
| 25 | 5 | zwei Schritte: Windschiefe nachweisen, dann Abstand über das Spatprodukt |
| 26 | 5 | **Fehlersuche**: Aufpunktabstand \(5\) statt Lotabstand \(4\) — der falsche Weg endet nachweislich falsch (MC) |
| 27 | 5 | Parameter aus zwei Bedingungen: Punkt auf einer Geraden **und** vorgegebener Abstand zu einer Ebene; beide Lösungen (\(r=0\) und \(r=12\)) diskutiert |
| 28 | 5 | zwei Verfahren: Parallelität von Gerade und Ebene nachweisen, dann Abstand über einen Geradenpunkt |
| 29 | 5 | Gerade nur durch zwei Punkte gegeben — Richtungsvektor selbst bilden, dann Kreuzproduktformel |
| 30 | 5 | Umkehraufgabe mit Parameter: Abstand als Term in \(c\), Lösung \(3\sqrt3\); Grenzfall \(c=0\) benannt |
| 31 | 6 | Abi-Format: „Zeigen Sie, dass alle vier Dachkanten gleich lang sind“ + Abstand Spitze–Grundkante, Sachkontext |
| 32 | 6 | Abi-Format: Windschiefe **begründen** und Mindestabstand zweier Trassen bestimmen, Deutung des Ergebnisses |
| 33 | 6 | Parameter im Normalenvektor; nur \(a^2\) geht ein, beide Lösungen \(\pm 1\) diskutiert |
| 34 | 6 | Behauptung prüfen: Abstand \(0\) lässt schneidend **und** identisch zu (MC) |
| 35 | 6 | Punkte auf einer Geraden mit vorgegebenem Abstand zu einer Ebene, zwei Lösungen auf verschiedenen Seiten |
| 36 | 6 | Grenzfall-Einsicht: der Parameter fällt heraus, weil die Gerade parallel zur Ebene liegt — Abstand konstant \(\sqrt6\) |

### 12-lk-geom-lagebeziehungen

Audit: KEIN_AFB3 L5 **und** L6; DUENNER_WEG (Stufe 4). Stufe 5 und 6 sind komplett neu; in
Stufe 4 sind die drei dünnsten Lösungswege (`#19`, `#20`, `#22`) ausgeschrieben worden.
Gate-Warnungen `#29` und `#35` mit den Aufgaben entfallen.

**Pflicht-Fix:** Im alten `#36` stand „Abi-LK:“ im Aufgabentext. Thüringen kennt keinen
Leistungskurs; die neue Aufgabe `#36` trägt „Abi eA:“. `grep -n "Abi-LK"` liefert jetzt nichts.

| id | Level | Kriterium |
|---|---|---|
| 19, 20, 22 | 4 | DUENNER_WEG behoben: Lösungsweg zeigt das Gleichungssystem, den Rechenschritt und die Probe |
| 25 | 5 | Parameter aus zwei Bedingungen: Aufpunkt in \(E\) **und** Richtung parallel zu \(E\) |
| 26 | 5 | **Fehlersuche**: aus \(\vec u \cdot \vec n = 0\) wird voreilig „echt parallel“ geschlossen; die Punktprobe zeigt, dass \(g\) in \(E\) liegt (MC) |
| 27 | 5 | identische Ebenen: erst den Streckfaktor aus den rechten Seiten, dann den Parameter |
| 28 | 5 | Schnitt zweier Geraden: System aufstellen, zwei Zeilen lösen, dritte als Probe — Abgrenzung gegen windschief |
| 29 | 5 | Parameter so bestimmen, dass sich zwei Geraden schneiden; sonst windschief |
| 30 | 5 | drei Ebenen, \(3\times3\)-System, Eindeutigkeit begründet (Gegenfall „gemeinsame Gerade“ benannt) |
| 31 | 6 | Abi-Format Sachkontext: Existenz der Schnittgeraden begründen, Firsthöhe bestimmen |
| 32 | 6 | Abi-Format: Ebene aus drei Spurpunkten über die Achsenabschnittsform, Schnitt nachweisen, Parameter bestimmen |
| 33 | 6 | Behauptung prüfen: senkrechte Normalen schließen einen Schnitt gerade **nicht** aus (MC) |
| 34 | 6 | Schnittgerade zweier Ebenen liegt in einer dritten — die Einsicht ist, dass der Term von \(t\) unabhängig wird |
| 35 | 6 | Lage dreier Ebenen ohne gemeinsamen Punkt (Prismenlage) — Fallunterscheidung als MC |
| 36 | 6 | **Abi eA** (ersetzt „Abi-LK“): Sachkontext Laserstrahl, Treffer nachweisen, Auftreffhöhe, Vorzeichen von \(t\) gedeutet |

### 12-lk-geom-schnittwinkel

Audit: KEIN_AFB3 L5 **und** L6; **KOLLAPS L2/L3 und L3/L4**; DUENNER_WEG (Stufen 2, 3).
Deshalb sind hier die **Stufen 3 bis 6** neu geschrieben, dazu die beiden dünnsten Lösungswege
der Stufe 2 (`#7`, `#12`). Die Gate-Warnung `#24` ist mit der Aufgabe entfallen.

Der Doppelkollaps hatte eine klare Ursache: Stufe 2 und Stufe 3 stellten dieselbe Aufgabe
(„Winkel zweier Vektoren“), nur unter anderer Überschrift, und Stufe 4 wiederholte die
Sinusformel mit Zahlen, die meist \(0°\) oder \(90°\) ergaben. Der neue Schnitt:

- **Stufe 2** bleibt Winkel zweier Vektoren (unverändert bis auf zwei Lösungswege).
- **Stufe 3** sind Geraden in Parameterform bzw. durch zwei Punkte, einschließlich der Regel,
  dass der Schnittwinkel zweier Geraden der **spitze** ist (Betrag im Zähler).
- **Stufe 4** ist Gerade–Ebene mit Entscheidungsanteil (Sachmodell, Umkehraufgabe, Begründung,
  warum dort der Sinus steht).
- **Stufe 5** ist Ebene–Ebene und Kombinationsaufgaben.

| id | Level | Kriterium |
|---|---|---|
| 7, 12 | 2 | DUENNER_WEG behoben: Lösungsweg begründet, warum das Skalarprodukt allein entscheidet bzw. woher das Vorzeichen kommt |
| 13 | 3 | Winkel zweier Geraden in Parameterform; Aufpunkte sind ohne Bedeutung |
| 14 | 3 | negatives Skalarprodukt — der Betrag liefert \(60°\) statt \(120°\), Begründung im Lösungsweg |
| 15 | 3 | Geraden nur durch je zwei Punkte gegeben, Richtungsvektoren selbst bilden |
| 16 | 3 | Auswahl des Vektorpaars mit \(60°\); alle vier Paare im Lösungsweg durchgerechnet (MC) |
| 17 | 3 | gleiche Beträge, kleiner Winkel — Deutung „Kosinus nahe \(1\)“ |
| 18 | 3 | Umkehraufgabe: Parameter aus der Orthogonalitätsbedingung |
| 19 | 4 | Gerade–Ebene; der Lösungsweg begründet den Übergang vom Kosinus zum Sinus |
| 20 | 4 | Modell aus Sachtext (Laderampe), Ergebnis an der Steigung geprüft |
| 21 | 4 | Verfahren begründen: warum bei Gerade–Ebene der Sinus steht (MC) |
| 22 | 4 | Umkehraufgabe: Parameter im Richtungsvektor aus vorgegebenem Winkel \(45°\) |
| 23 | 4 | Gerade–Ebene mit negativer Komponente, kleiner Winkel gedeutet |
| 24 | 4 | Folgerung aus \(\alpha = 0°\): parallel zur Ebene, aber Lage offen (ersetzt die Aufgabe mit der zu langen richtigen Option) |
| 25 | 5 | zwei Schritte: Normalenvektor aus drei Punkten, dann Winkel zur Koordinatenebene |
| 26 | 5 | **Fehlersuche**: fehlender Betrag liefert \(109{,}5°\) statt \(70{,}5°\) — der falsche Weg endet nachweislich falsch (MC) |
| 27 | 5 | Parameter aus zwei Bedingungen: Punktprobe **und** Orthogonalität zweier Ebenen |
| 28 | 5 | Gerade aus zwei Punkten, dann Winkel zur Ebene; sehr flacher Winkel, Schnitt trotzdem vorhanden |
| 29 | 5 | zwei Verfahren verzahnt: Kreuzprodukt für die Schnittgerade, Sinusformel für den Winkel |
| 30 | 5 | Umkehraufgabe mit Parameter im Normalenvektor, Lösung \(a = \pm 1\) diskutiert |
| 31 | 6 | Abi-Format: Neigungswinkel eines Pultdachs bestimmen **und** gegen eine Schranke beurteilen |
| 32 | 6 | Abi-Format Pyramide: Seitenfläche aus drei Punkten, Winkel zur Grundfläche |
| 33 | 6 | „Zeigen Sie, dass zwei Winkel gleich sind“ — Begründung über die gleichen Komponenten des Richtungsvektors |
| 34 | 6 | Behauptung prüfen: \(\alpha + \beta = 90°\), daher mal der eine, mal der andere größer (MC) |
| 35 | 6 | Parameter aus vorgegebenem Winkel \(30°\), Lösung \(\sqrt6\), Probe im Lösungsweg |
| 36 | 6 | **Abi eA**: Schnittwinkel zweier Dachflächen **und** Erklärung, warum der sichtbare Firstwinkel der stumpfe Nebenwinkel ist |

### 12-lk-dgl → Geraden- und Ebenenscharen (eA) — Ersatz-Trainer

Audit: KEIN_AFB3 L5 **und** L6; DUENNER_WEG (Stufen 1, 2). Alle 36 Aufgaben sind neu.
Differenzialgleichungen stehen nicht im Thüringer Lehrplan; das Lehrplan-Gate meldete hier
zuvor zwei Treffer (`#1` und `#5`), jetzt keinen mehr.

Geändert wurden außerdem:

- `<title>`: `Geraden- und Ebenenscharen (eA) - Mathepfade`
- `THEMA_CONFIG = { name: 'Geraden- und Ebenenscharen (eA)', bereich: 'geometrie' }`
  (vorher `bereich: 'analysis'` — der Trainer gehört jetzt in den Abschnitt „Geometrie eA“)
- Kommentar in Zeile 2: `<!-- Dateiname historisch (QR-Links); Inhalt seit 2026-09: Geraden- und Ebenenscharen, TH-Lehrplan Kap. 4.2 -->`
- **`THEMA_KEY` bleibt `'12-lk-dgl'`** — sonst verlieren Schülerinnen und Schüler ihren
  gespeicherten Fortschritt.

**Neuer Index-Zeilentext (`theme-name`), noch einzutragen:** `Geraden- &amp; Ebenenscharen`

| id | Level | Kriterium |
|---|---|---|
| 1 | 1 | Begriff der Schar: ein Parameter, der nicht die Punkte, sondern die Gerade auswählt (MC) |
| 2 | 1 | ein Schritt: Scharparameter und Geradenparameter nacheinander einsetzen |
| 3 | 1 | Parameter steht nur im Richtungsvektor → gemeinsamer Punkt (MC) |
| 4 | 1 | Punktprobe in einer Ebenenschar, nach dem Parameter auflösen |
| 5 | 1 | Begriff: parameterfreier Richtungsvektor bedeutet lauter parallele Geraden (MC) |
| 6 | 1 | Parameter im Aufpunkt: dritte Komponente ist von \(t\) unabhängig |
| 7 | 2 | Orthogonalität des Richtungsvektors zu einem festen Vektor |
| 8 | 2 | Parallelität zweier Ebenen über den Streckfaktor der Normalenvektoren; „echt parallel“ geprüft |
| 9 | 2 | gemeinsamer Spurpunkt einer Ebenenschar auf der \(x\)-Achse — der Parameter fällt heraus |
| 10 | 2 | Lage der Schargeraden zueinander: Büschel, nicht parallel (MC) |
| 11 | 2 | zwei Schritte: \(t\) aus der \(x\)-Forderung, dann \(k\) aus der \(z\)-Forderung |
| 12 | 2 | gemeinsamen Punkt erkennen **und** seinen Betrag bilden |
| 13 | 3 | Ebenenschar durch eine **feste Gerade**: nach \(a\) sortieren, Koeffizientenvergleich |
| 14 | 3 | Parameter für Orthogonalität zweier Ebenen |
| 15 | 3 | Parameter, für den eine Schargerade eine feste Gerade schneidet; Zwischenergebnis \(t=-1\) |
| 16 | 3 | Gerade senkrecht auf einer Ebene: Kollinearität mit dem Normalenvektor (MC) |
| 17 | 3 | zweite Variante der festen Gerade, Parameter in zwei Koeffizienten |
| 18 | 3 | Orthogonalität zweier Geraden, nicht ganzzahlige Lösung \(-\tfrac13\) |
| 19 | 4 | „kein gemeinsamer Punkt“ **ohne** Nennung des Verfahrens; zweiter Schritt Aufpunktprobe, damit nicht versehentlich „liegt in E“ |
| 20 | 4 | Punkt auf der Schnittgeraden: die parameterfreie Ebene zuerst prüfen |
| 21 | 4 | Verfahren begründen: wie man den gemeinsamen Punkt einer Geradenschar findet (MC) |
| 22 | 4 | Modell aus Sachtext (Mast senkrecht auf einer Dachebene) → Kollinearität mit \(\vec n\) |
| 23 | 4 | Parameter, für den sich zwei Geraden schneiden; sonst windschief |
| 24 | 4 | gemeinsame Ebene aller Schargeraden aus der konstanten Koordinate erkennen (MC) |
| 25 | 5 | Parameter aus **zwei** Bedingungen: Richtung parallel zu \(E\), dann Aufpunkt in \(E\) — gefragt ist die zweite Unbekannte |
| 26 | 5 | **Fehler in einer Lagebestimmung**: aus \(\vec u \cdot \vec n = 0\) wird „echt parallel“ geschlossen, obwohl \(g_1\) in \(E\) liegt; der falsche Weg endet nachweislich falsch (MC) |
| 27 | 5 | zwei Bedingungen zugleich: Schnittpunkt in \(E\) **und** in der \(xz\)-Ebene; Lösung \(-\tfrac23\) |
| 28 | 5 | Grenzfall \(a=-1\): parallel — mit Aufpunktprobe gegen „liegt in E“ abgesichert |
| 29 | 5 | zwei Verfahren: Scharparameter einsetzen, dann Winkel zweier Ebenen |
| 30 | 5 | Parallelität zweier **Scharen**; Fallunterscheidung \(k = \pm 1\), Gegenvektor als dieselbe Richtung erkannt |
| 31 | 6 | Abi-Format, **Fallunterscheidung**: Aufpunkt liegt für jedes \(k\) in \(E\), also nie echt parallel; \(k=-0{,}5\) liefert „liegt in \(E\)“, sonst schneidend |
| 32 | 6 | Abi-Format: gemeinsame Gerade einer Ebenenschar nachweisen **und** ihren Abstand vom Ursprung bestimmen (zwei Verfahren) |
| 33 | 6 | **Fallunterscheidung** schneidend/windschief nach dem Parameter, mit Begründung, warum parallel ausscheidet (MC) |
| 34 | 6 | Abi-Format Sachkontext: Schar durch eine feste Gerade (First) nachweisen, dann Parameter aus dem Neigungswinkel \(30°\) |
| 35 | 6 | **Fallunterscheidung** identisch/schneidend über das Kreuzprodukt der Normalen; „echt parallel“ tritt nie auf |
| 36 | 6 | **Abi eA**: gemeinsamer Achsenpunkt der Schar nachweisen **und** Schnittwinkel zweier Scharebenen bestimmen |

---

## Gate-Ergebnisse (Block B2, 2026-09-30)

| Gate | Ergebnis |
|---|---|
| `level_check --strict` (4 Trainer) | Exit 0, **0 Fehler, 0 Warnungen** (vorher 5 Warnungen: abstaende #25/#28, lagebeziehungen #29/#35, schnittwinkel #24) |
| `lehrplan_check --strict` (4 Trainer) | 0 Befunde (vorher 2 in `12-lk-dgl`: „Differenzialgleichung“ in #1 und #5) |
| `katex_check` (4 Trainer) | 0 Render-Fehler |
| `pytest tests/test_trainer.py` | grün für alle vier Trainer |
| Sichtprüfung | PNG je Trainer und Stufe angesehen; Spaltenvektoren erscheinen als Matrix, deutsche Anführungen schließen mit `“` |

## Offen

- Der neue `theme-name`-Text `Geraden- &amp; Ebenenscharen` muss in `index.html` nachgetragen
  werden; die Datei war während der Welle für parallel arbeitende Agenten gesperrt.
- In `12-lk-geom-abstaende` bleibt Stufe 3 (Punkt–Ebene über die HNF) inhaltlich unverändert;
  der Plan sieht für Stufe 1–3 nur Entdopplung vor.
- In `12-lk-geom-schnittwinkel` sind in Stufe 2 noch mehrere Aufgaben, die auf \(90°\) hinauslaufen;
  sie stehen dort bewusst als Einführung der Orthogonalitätsprüfung.
