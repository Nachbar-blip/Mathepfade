# Mathepfade: Thüringer Lehrplan und Level-Progression — Design (2026-09-26)

Status: vom Autor freigegeben am 2026-09-26.

## Ausgangslage

- Die DifferenzierungsEngine hat alle 103 Trainer nach einer festen Level-Rubrik überarbeitet
  (`../DifferenzierungsEngine/docs/plans/2026-09-17-level-progression-plan-ENTWURF.md`, Schritt 0).
  Mathepfade hat davon bisher nur die Gates, die Kontext-Fragen und die Lösungswege übernommen
  (`2026-09-19-level-progression-plan-ENTWURF.md`, `docs/audit/audit-2026-09-19-mathepfade.md`).
  Die Neubesetzung von Stufe 4 bis 6 steht aus.
- Mathepfade ist die Thüringen-Variante. Der Abgleich mit dem Thüringer Lehrplan Gymnasium 2018
  (`schule/Referenz/Lehrplaene/Mathe/TH/lp_gy_mathematik_TH_2018.txt`) war bisher nicht gemacht.

## Der Thüringer Lehrplan in Kürze

- Kompetenzen werden je **Doppeljahrgang** ausgewiesen: 5/6, 7/8 (Kapitel 2.2), 9/10 (Kapitel 2.3).
  Innerhalb des Doppeljahrgangs legt die Schule die Reihenfolge fest.
- Kapitel 3 („Klassenstufe 11") gilt nur für Realschulabsolventen in der Einführungsphase und ist
  für das Gymnasium nicht maßgeblich.
- Qualifikationsphase = Klassenstufen 11 und 12 (Kapitel 4), abschlussorientiert am Ende von 12
  beschrieben, mit **grundlegendem (gA) und erhöhtem Anforderungsniveau (eA)**. Die Begriffe
  GK/LK kommen im Lehrplan nicht vor.
- Nicht im Lehrplan: Vektoren vor der Qualifikationsphase, Determinanten, Polynomdivision,
  Hypothesentests, Newton-Verfahren, Differenzialgleichungen, stochastische Prozesse/Matrizen,
  uneigentliche Integrale. Stattdessen: Prognoseintervalle (gA) und Konfidenzintervalle mit
  Stichprobenumfang (eA) über die 2σ-Regel, Normalverteilung (eA), Scharen von Geraden und
  Ebenen (eA), Stetigkeit/Asymptoten/Periodizität (eA), ln als Umkehrfunktion (eA).

## Teil 1 — Lehrplanabgleich

### 1a Umzug zwischen Klassenspalten (9 Trainer)

Die Klassenzuordnung steht ausschließlich in `index.html` (Spalten `.col-7` … `.col-12`).
Die **Dateinamen bleiben unverändert**, damit die gedruckten QR-Codes (`Mathepfade_QR.docx`)
und gespeicherte localStorage-Schlüssel (`spirale-<datei>`) weiter funktionieren.

| Trainer | bisher | TH-Lehrplan | neu |
|---|---|---|---|
| 9-pythagoras | 9 | 7/8 (2.2.3) | 8 |
| 9-raumgeometrie-prisma-zylinder | 9 | 7/8 (2.2.3, inkl. Kugel) | 8 |
| 9-raumgeometrie-pyramide-kegel | 9 | 7/8 (2.2.3) | 8 |
| 7-potenzgesetze | 7 | 9/10 (2.3.1) | 9 |
| 8-potenzen-negativ | 8 | 9/10 (Kl. 8 nur natürliche Exponenten) | 9 |
| 8-strahlensatz | 8 | 9/10 (2.3.3) | 9 |
| 8-aehnlichkeit-streckung | 8 | 9/10 (2.3.3) | 9 |
| 8-lgs | 8 | 9/10 (2.3.1) | 9 |
| 8-bruchgleichungen | 8 | 9/10 („einfache Bruchgleichungen") | 9 |

Die Inhalte werden beim Level-Durchgang (Teil 2) auf das Niveau der Zielklasse gebracht — in der
Welle der **Zielklasse**. Beispiel: Pythagoras in Kl. 8 ohne Wurzelgesetze aus Kl. 9;
Strahlensatz in Kl. 9 mit Hauptähnlichkeitssatz.

Bewusst nicht verschoben: 7-winkel-winkelsumme, 7-symmetrie, 7-vierecke (TH 5/6, aber Mathepfade
beginnt bei 7 — bleiben als Wiederholung), 9-stoch-boxplot (Bildungsstandards MSA),
10-ganzrationale-funktionen (Brücke zur Qualifikationsphase), 10-stoch-bedingte-wsk (TH 10:
Vierfeldertafel, Unabhängigkeit — Schwerpunkt dorthin verschieben, Trainer bleibt).

### 1b Ersatz lehrplanfremder Inhalte (8 Trainer)

Dateiname bleibt, Titel und alle 36 Aufgaben werden neu geschrieben. Ersatzthema ist jeweils
eine echte Lücke gegenüber dem TH-Lehrplan:

| Datei | bisher | neu | TH-Beleg |
|---|---|---|---|
| 8-vektoren-2d | Vektoren in der Ebene | Prozent- und Zinsrechnung | 2.2.2 (fehlte bisher ganz) |
| 9-flaechenberechnung-determinante | Determinante | Flächen im Koordinatensystem ohne Vektoren (Zerlegen, Dreiecksformel mit Sinus) | 2.3.3 |
| 10-polynomdivision | Polynomdivision | Grenzwerte und Asymptoten anschaulich | 2.3.2 |
| 12-stoch-hypothesentests | Hypothesentests | Prognoseintervalle mit der 2σ-Regel | 4.3 gA |
| 11-lk-newton | Newton-Verfahren | ln-Funktion: Umkehrfunktion, Ableitung, Stammfunktion von 1/x | 4.1 eA |
| 12-lk-dgl | Differenzialgleichungen | Scharen von Geraden und Ebenen | 4.2 eA |
| 12-lk-stoch-prozesse | Stochastische Prozesse | Konfidenzintervall und Stichprobenumfang | 4.3 eA |
| 12-lk-integral-uneigentlich | Uneigentliche Integrale | Stetigkeit, Asymptoten, Periodizität | 4.1 eA |

Die Dateinamen passen danach nicht mehr zum Inhalt. Das ist der Preis für stabile QR-Links und
wird im Kopf der Datei kommentiert. Der Ersatz geschieht in der Welle der jeweiligen Klasse.

### 1c Benennung

Filter „Nur GK / Nur LK" und Abschnittstitel „… LK" werden zu **gA / eA**; Trainer-Badges
und `lk-only`-Klassen bleiben technisch, die sichtbaren Texte wechseln.

## Teil 2 — Level-Progression nach DiffEngine-Rubrik

Rubrik (übernommen, bindend):

| Stufe | AFB | Kriterium | Verboten |
|---|---|---|---|
| 1 | I | ein Rechenschritt, Objekt gegeben, schöne Zahlen | Kontext |
| 2 | I | Standardverfahren, zwei Schritte | Kontext, Parameter |
| 3 | I | Klassenarbeits-Standard, Zwischenergebnis nötig | Formel im Text |
| 4 | II | Verfahren wählen oder Modell aus Text aufstellen oder Umkehraufgabe | Rechenweg im Text, angesagte Rechenart |
| 5 | III | zwei Verfahren kombinieren oder Parameter aus zwei Bedingungen oder Fehler im Rechenweg finden | gelieferte Formel, trivialisierende Stelle (x = 0) |
| 6 | III | Fallunterscheidung, Aussage begründet prüfen, Abi-Format (Kl. 11/12) | L1–L3-Muster mit Kontext |

Lesart Kl. 7–10: L4 = Rechenart selbst wählen, L5 = zweischrittige Sachaufgabe ohne Weg oder
Fehlersuche, L6 = Umkehraufgabe, Behauptung prüfen, Sonderfall.

Vorgehen:
- **Alle 90 Trainer**, in Wellen je Klasse und Sachgebiet (8–10 Trainer), Reihenfolge Kl. 7 → 12.
- Je Trainer: Stufe 5 und 6 komplett neu (12 Aufgaben), Stufe 4 dort, wo das Audit KOLLAPS L3/L4
  oder L4/L5 meldet. Stufe 1–3 bleiben, werden nur entdoppelt.
- Je Klasse eine Kriterien-Datei `docs/plans/2026-09-XX-klN-kriterien.md` (Muster: DiffEngine).
  Kriterien stehen nicht im öffentlichen HTML.
- Aufstieg nach 2 richtigen Antworten bleibt (Gleichstand mit DiffEngine).
- Aufgabenformen und Zahlenmuster dürfen aus dem Materialindex adaptiert werden — umformuliert,
  ohne Quellenangaben, kein Rohmaterial im Repo (`schule/CLAUDE.md`).

## Teil 3 — Prüfung je Block (bindend)

1. `python tests/level_check.py` — Rubrik-Gate, 0 Fehler
2. Jede Zahl mit Wolfram nachgerechnet
3. `python tests/katex_check.py` (mit `python -m http.server 8765`)
4. Playwright-Suite `tests/test_trainer.py` für die geänderten Trainer
5. Screenshot erzeugen **und ansehen** (Sichtprüfung, `schule/CLAUDE.md`)
6. Ein Commit je Block; Aufgabentexte mit LaTeX nie per Heredoc schreiben (Backslash-Verlust)

Das Gate wird um eine Lehrplan-Regel erweitert: ein Wortlisten-Check je Klassenspalte
(z. B. „Vektor", „Determinante", „Hypothese", „Polynomdivision" außerhalb erlaubter Trainer),
damit lehrplanfremde Inhalte nicht zurückkehren.

## Reihenfolge der Wellen

| Welle | Trainer |
|---|---|
| 7 | 11 verbleibende Kl.-7-Trainer |
| 8 | Kl. 8 (inkl. Zuzug Pythagoras, Prisma/Zylinder, Pyramide/Kegel; Ersatz Prozent/Zins) |
| 9 | Kl. 9 (inkl. Zuzug Potenzen, Strahlensatz, Ähnlichkeit, LGS, Bruchgleichungen; Ersatz Flächen) |
| 10 | Kl. 10 (Ersatz Grenzwerte/Asymptoten) |
| 11 | Kl. 11 gA, dann eA (Ersatz ln-Funktion) |
| 12 | Kl. 12 Analysis, Geometrie gA/eA (Ersatz Scharen), Stochastik gA/eA (Ersatz Prognose-, Konfidenzintervalle, Stetigkeit) |

Index-Umzug und Umbenennung gA/eA (Teil 1a, 1c) erfolgen als erster, eigener Commit.
