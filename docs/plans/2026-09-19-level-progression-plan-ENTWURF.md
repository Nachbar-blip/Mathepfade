# Änderungsplan Level-Progression Mathepfade — ENTWURF zur Absprache (2026-09-19)

Status: **Schritte 1, 2 und 4 umgesetzt (2026-09-19).** Das Rubrik-Gate meldet für alle 90 Trainer
keinen harten Fehler mehr: **72 ohne Beanstandung, 18 Warnungen, 0 Fehler** (Ausgangslage
55 / 17 / 18). `katex_check` ist für alle geänderten Trainer grün.

| Schritt | Inhalt | Commit |
|---|---|---|
| 1 | Gates übernommen, CSS-Fix, 5 Markdown-Stellen, 2 Toleranzen | `90f423d` |
| 2 | 35 Fragen mit Kontext versehen (erste Runde) | `d4fa200` |
| 2+4 | 33 weitere Fragen mit Kontext, 4 Formel-Ansagen, 1 Dublette, 12 MC-Umwandlungen | `39f9602` |

## Der zentrale Befund

Die Gate-Meldung „identische Frage" war eine Fehlspur. Es handelte sich nicht um Dubletten,
sondern um Fragen, die sich auf die **vorhergehende Aufgabe** beziehen — „Dazu \(b=?\)",
„Gleiche Daten. \(Q_3\)?", „Weiter \(x_2\)?". Weil die Engine innerhalb einer Stufe frei
auswählt, bekommt ein Schüler solche Fragen ohne ihren Bezug zu sehen und kann sie nicht lösen.
Dieselbe Kurzfrage tauchte dadurch mehrfach im Trainer auf — daher die Gate-Meldung.

**Insgesamt 68 Fragen in 11 Trainern** wurden um ihren Kontext ergänzt. Geändert wurde jeweils nur
der Fragetext; alle genannten Parameter und Zwischenergebnisse sind mit Wolfram gegengerechnet.
Ref4OHG und die DifferenzierungsEngine haben diesen Fehler **nicht** (je 0 Vorkommen).

## Offen: der Telegrammstil

Mathepfade ist durchgehend sehr knapp geschrieben: **1022 von 3222 Fragen sind sehr kurz**
gegenüber rund 9 % in Ref4OHG und der DifferenzierungsEngine. Die Lösungswege bestehen vielfach
nur aus dem Ergebnis („Lösungsweg: −3."), geben also keine Erklärung.

Das ist ein Qualitätsproblem des Bestands, kein Stufenproblem, und betrifft rund ein Drittel aller
Aufgaben. Es braucht eine eigene Entscheidung des Autors — eine Überarbeitung in diesem Umfang
ist ein eigenes Vorhaben, kein Nebenprodukt der Level-Progression.

## Noch nicht umgesetzt: Schritt 3 (Audit aller 90 Trainer)

Die harten Gate-Fehler sind behoben, das vollständige Audit nach dem Muster der
DifferenzierungsEngine steht aus. Es würde die Trainer finden, deren Stufen kollabieren, **ohne**
eine Gate-Regel zu verletzen — in der DifferenzierungsEngine war genau das der häufigste Fall.
Die 18 verbliebenen Gate-Warnungen (wortgleiche Aufgaben zwischen Trainern, angesagte Rechenart
auf Stufe 4) sind ein erster Anhaltspunkt dafür.

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
