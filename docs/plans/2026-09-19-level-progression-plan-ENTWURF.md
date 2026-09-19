# Änderungsplan Level-Progression Mathepfade — ENTWURF zur Absprache (2026-09-19)

Status: **Entwurf, noch nicht begonnen.** Anlass ist die am 2026-09-18 abgeschlossene
Level-Progression der DifferenzierungsEngine (alle 103 Trainer, Kl. 5–12). Mathepfade teilt mit ihr
Engine, Stylesheet und Aufgabenformat und hat deshalb voraussichtlich dieselben strukturellen
Mängel — die **Inhalte** sind hier jedoch weitgehend eigenständig.

Dieser Plan beruht auf einer **Messung**, nicht auf einer Vermutung — die Zahlen unten stammen aus
dem Rubrik-Gate der DiffEngine (`tests/level_check.py`), angewendet auf die 90 Mathepfade-Trainer,
sowie aus einem Textvergleich gegen den DiffEngine-Stand vor der Überarbeitung (Commit `9baddf3`).

## Befundlage (gemessen am 2026-09-19)

**Umfang:** 90 Trainer, je 36 Aufgaben in 6 Stufen. Klassen 7–12
(7: 12 · 8: 14 · 9: 16 · 10: 14 · 11: 15 · 12: 19), darunter 12 LK-Trainer (`*-lk-*`).
Damit ist Mathepfade das **größte** der drei Angebote.

**Rubrik-Gate (DiffEngine-Maßstab, versuchsweise angewendet):**

| Ergebnis | Trainer |
|---|---|
| ohne Beanstandung | 58 |
| mit Warnung | 14 |
| mit hartem Fehler | 18 |

Verteilung der Fehler: Kl. 7 und Kl. 10 je fünf Trainer, Kl. 11 und 12 je drei, Kl. 8 und 9 je einer.

**Das ist deutlich besser als Ref4OHG** (dort 32 von 76 mit hartem Fehler) und liegt in derselben
Größenordnung wie die DifferenzierungsEngine vor ihrer Überarbeitung. Die Mängel sind hier also
weniger flächendeckend, dafür gezielter zu suchen.

**Fehlerarten im Einzelnen:**

- **11 Trainer mit wortgleichen Aufgaben im eigenen Trainer** — der schwerwiegendste Befund. Beispiele:
  - `11-lk-kurvendisk-erweitert`: Aufgabe #4 = #8 = #20, #5 = #9 = #21, #6 = #16
  - `11-steckbriefaufgaben`: #18 = #20 = #26 = #29 = #34 — dieselbe Frage fünfmal, über vier Stufen verteilt
  - `11-lk-newton`: #11 = #23 = #30 · `10-substitution`: #15 = #22, #27 = #32
  - dazu `12-stoch-hypothesentests`, `9-stoch-boxplot`
  Wenn dieselbe Frage auf Stufe 1, 3 und 5 steht, ist die Stufung an dieser Stelle **nachweislich**
  keine Steigerung, sondern Wiederholung. Das ist kein Schönheitsfehler, sondern genau der Mangel,
  um den es in diesem Plan geht — und er ist hier maschinell nachweisbar.
- **8 Stufen mit MC-Überhang** in L5/L6 (bis zu 6 von 6 Aufgaben als Multiple Choice). Vier
  Antwortmöglichkeiten machen eine Begründungsaufgabe zur Ratefrage; der Maßstab erlaubt höchstens 3.
- **4 Aufgaben mit Formel- oder Rechenweg-Ansage ab Stufe 4** — ab AFB II soll der Weg selbst
  gewählt werden.
- **5 Stellen Markdown-Sternchen** (`**fett**`). Die Engine rendert kein Markdown, die Sternchen
  erscheinen wörtlich. (Zum Vergleich: DiffEngine 124 Stellen, Ref4OHG 87 — hier also fast sauber.)
- **2 Dezimallösungen ohne Toleranz** — der Schüler muss exakt treffen.

**Darstellungsfehler in `spirale.css`:** `.aufgabe-text` ist eine Flex-Zeile
(`display: flex; align-items: center`). Dadurch steht jede Inline-Formel `\(...\)` als eigenes
Element in einer eigenen Zeile — derselbe Fehler, der in der DiffEngine am 2026-09-18 an der Ursache
behoben wurde (Commit `2b35b72`). Betrifft **alle 90 Trainer** gleichzeitig.

**Keine Gates vorhanden:** `tests/` enthält nur `test_trainer.py`. Die Prüfskripte `level_check.py`
und `katex_check.py` existieren bisher nur in der DifferenzierungsEngine.

## Der entscheidende Unterschied zu Ref4OHG: die Inhalte sind eigen

| Deckung mit dem DiffEngine-Altstand | Trainer |
|---|---|
| ≥ 80 % (Stufenblock übertragbar) | **0** |
| 40–79 % | 3 (`10-trig-einheitskreis`, `10-trig-sinusfunktion`, `11-ableitungsregeln`) |
| < 40 % (eigenständig) | **87** |

Insgesamt sind nur 66 von 3223 Aufgabenfragen (2 %) wortgleich mit der DifferenzierungsEngine.

**Konsequenz:** Anders als bei Ref4OHG (dort 57 übertragbare Kopien) lässt sich hier **fast nichts
übertragen**. Mathepfade braucht denselben Weg, den die DifferenzierungsEngine gegangen ist:
erst ein Audit, dann Überarbeitung Trainer für Trainer. Das ist der größere Aufwand — aber es ist
auch der Grund, warum der Bestand bisher besser dasteht: Die Aufgaben sind eigens für Thüringen
geschrieben worden und nicht durch mehrfaches Kopieren verwässert.

## Ziel

Dasselbe wie in der DifferenzierungsEngine: Jede Stufe eines Trainers ist eine eigene
**Anforderungsstufe**, nicht ein weiteres Teilthema.

- **Stufe 1–3 = AFB I** — Grundrechenarten, Standardverfahren, Klassenarbeitsniveau
- **Stufe 4 = AFB II** — Transfer; die Rechenart wird *nicht* mehr angesagt
- **Stufe 5/6 = AFB III** — mehrschrittig, Fehler finden, Aussage prüfen, Umkehraufgabe,
  Spezialfall begründen; in Kl. 11/12 auf Abiturniveau (eA in den `*-lk-*`Trainern)

Für die Klassen 7–10 heißt das konkret: L4 = Rechenart selbst wählen, L5 = zweischrittige
Sachaufgabe ohne vorgegebenen Weg oder Fehlersuche, L6 = Umkehraufgabe, Behauptung prüfen,
Spezialfall.

## Vorgehen

### Schritt 1 — Gates und CSS-Fix übernehmen (Voraussetzung für alles Weitere)

1. `tests/level_check.py` und `tests/katex_check.py` aus der DifferenzierungsEngine übernehmen.
   Beide sind projektunabhängig geschrieben und laufen bereits jetzt gegen Mathepfade.
2. `.aufgabe-text` in `spirale.css` von `display: flex` auf `display: block` umstellen
   (Begründungskommentar aus der DiffEngine mitnehmen), danach **Sichtprüfung am Bild**.
3. Die 5 Markdown-Stellen auf `<b>…</b>` umstellen, die 2 fehlenden Toleranzen ergänzen.

Reine Reparaturen ohne didaktische Entscheidung, als ein Block committierbar.

### Schritt 2 — Die 11 Trainer mit Dubletten im eigenen Trainer

Das ist der **schnellste inhaltliche Gewinn** und zugleich der härteste Nachweis für kollabierte
Stufen. Je Trainer: die mehrfach vorkommende Aufgabe auf der niedrigsten Stufe belassen, auf den
höheren Stufen durch eine echte Steigerung ersetzen. `11-steckbriefaufgaben` (dieselbe Frage
fünfmal) zuerst.

### Schritt 3 — Audit aller 90 Trainer

Nach dem Muster der DifferenzierungsEngine
(`../DifferenzierungsEngine/docs/audit/audit-2026-09-17-level-progression.md`): je Trainer
Score 0–3, kollabierende Stufen, Hauptmangel, fehlende AFB-III-Formate, konkrete Ersatzvorschläge.
Das Audit ist die Arbeitsgrundlage für alles Weitere — ohne es wird jede Welle zum Ratespiel.

Das DiffEngine-Audit umfasst 127 KB für 103 Trainer; für 90 Trainer ist Vergleichbares zu erwarten.

### Schritt 4 — Überarbeitung in Wellen

Bündelung zu je 8–10 Trainern entlang von Jahrgang und Sachgebiet (so wie in der DiffEngine:
Analysis, Geometrie, Stochastik getrennt). Reihenfolge nach Absprache — siehe offene Fragen.

### Schritt 5 — Die 3 teilweise deckungsgleichen Trainer

`10-trig-einheitskreis`, `10-trig-sinusfunktion`, `11-ableitungsregeln`: Hier passt rund die Hälfte
der Aufgaben zur DiffEngine, der entsprechende Stufenblock kann teilweise übernommen werden.

## Arbeitsweise je Trainer (bewährt, aus der DifferenzierungsEngine)

1. Auditbefund lesen → neuen Stufenblock in eine Scratchpad-`.js` schreiben
2. Einsetzen per Skript (Zeilenenden der Zieldatei erhalten!)
3. `level_check.py` — Rubrik
4. **Jede Zahl mit Wolfram nachrechnen** — ohne Ausnahme
5. `katex_check.py` (braucht `python -m http.server 8765`)
6. Screenshot erzeugen **und ansehen** (Sichtprüfung ist bindend, `schule/CLAUDE.md`)
7. Commit je Block

**Warnung aus der DiffEngine-Arbeit:** Aufgabentexte mit LaTeX niemals über ein Bash-Heredoc
schreiben — dabei werden doppelte Backslashes zerstört, `\\frac` wird zu `\f` (Seitenvorschub), und
KaTeX bricht. Immer Write/Edit verwenden.

**Materialindex:** Für neue Aufgaben gilt `schule/CLAUDE.md` — Aufgaben*formen* und Zahlenmuster aus
`Material-Lokal/Index/` dürfen als Vorlage dienen (umformuliert, ohne Quellenangabe), Rohmaterial und
Verlagsmetadaten dürfen **niemals** in dieses öffentliche Repo gelangen.

## Aufwandsschätzung

| Schritt | Trainer | Aufwand |
|---|---|---|
| 1 Gates, CSS, Markdown, Toleranzen | alle 90 | ein Arbeitsblock |
| 2 Dubletten im eigenen Trainer | 11 | 1–2 Wellen |
| 3 Audit | alle 90 | eigener Arbeitsblock |
| 4 Überarbeitung | ~80 | 9–10 Wellen |
| 5 teilweise deckungsgleich | 3 | zusammen mit Welle Kl. 10/11 |

Zum Vergleich: Die 103 DiffEngine-Trainer haben Audit plus zwei Arbeitstage und gut 20 Commits
gebraucht. Mathepfade liegt in derselben Größenordnung — Ref4OHG ist dank der Kopien deutlich
billiger und wäre, falls die Zeit knapp ist, zuerst zu machen.

## Offene Fragen an den Autor

1. **Reihenfolge der drei Projekte:** Ref4OHG ist mit 57 übertragbaren Kopien schnell erledigt,
   Mathepfade ist die eigentliche Arbeit. Erst Ref4OHG abräumen, oder Mathepfade zuerst, weil es
   der größere Bestand ist?
2. **Thüringer Lehrplan:** Soll ich beim Audit den Lehrplanabgleich je Jahrgang mitmachen (erkennt
   Aufgaben über oder unter Niveau, kostet aber spürbar mehr), oder rein die Stufenlogik prüfen?
3. **LK-Trainer (12 Stück, `*-lk-*`):** In der DiffEngine wurden in zwei LK-Geometrie-Trainern
   lehrplanfremde Inhalte (Radikalachse, Kreisbüschel, Ähnlichkeitspunkte) durch lehrplankonforme
   eA-Aufgaben ersetzt. Falls hier Vergleichbares auftaucht — streichen oder als Ausblick behalten?
4. **Engine-Tempo:** In der DiffEngine ist offengeblieben, ob der Stufenaufstieg nach 3 statt 2
   richtigen Antworten erfolgen soll. Gilt für Mathepfade dieselbe Zurückstellung?
5. **Audit-Umfang:** Alle 90 Trainer auditieren, oder zunächst nur die 18 mit hartem Gate-Fehler
   plus die 14 mit Warnung? Das wäre schneller, übersieht aber die Trainer, deren Stufen kollabieren,
   ohne eine Gate-Regel zu verletzen — und genau das war in der DiffEngine der häufigste Fall.

## Grundlagen

- `../DifferenzierungsEngine/docs/plans/2026-09-17-level-progression-plan-ENTWURF.md` — Ursprungsplan
- `../DifferenzierungsEngine/docs/audit/audit-2026-09-17-level-progression.md` — Auditmuster
- `../DifferenzierungsEngine/tests/level_check.py`, `katex_check.py` — die zu übernehmenden Gates
- `../Ref4OHG/docs/plans/2026-09-19-level-progression-plan-ENTWURF.md` — Schwesterplan
- `schule/CLAUDE.md` — Sichtprüfung (bindend), Materialindex (strikt lokal)
