# Mathepfade Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build Mathepfade — 90 adaptive math trainers covering the Thüringen G8 curriculum (Klasse 7–12), deployed via GitHub Pages.

**Architecture:** Clone-and-adapt from Ref4OHG. Shared spirale-engine.js + spirale.css (1:1 copy with bugfixes), new index.html dashboard for 90 trainers (6 Klassen + GK/LK filter), 90 trainer HTML files each with 36 Aufgaben across 6 difficulty levels, Playwright test suite.

**Tech Stack:** Vanilla HTML/CSS/JS, KaTeX for math rendering, localStorage for progress, Playwright + pytest for testing, GitHub Pages for hosting.

**Reference projects (read these for patterns):**
- `C:/DevProjects/schule/zzz_TOP/Ref4OHG/` — Niedersachsen, 76 Trainer (latest bugfixes)
- `C:/DevProjects/schule/zzz_TOP/DifferenzierungsEngine/` — Sachsen-Anhalt, 87 Trainer (GK/LK pattern)

**Design doc:** `docs/plans/2026-04-12-mathepfade-design.md`

---

## Task 0: GitHub Repo + Scaffolding

**Files:**
- Working dir: `C:/DevProjects/schule/zzz_TOP/Mathepfade/`
- Create: `.gitignore`
- Copy: `spirale-engine.js` (from Ref4OHG — has bugfixes)
- Copy: `spirale.css` (from Ref4OHG — has bugfixes)
- Create: `trainer/` directory (empty)
- Create: `tests/` directory (empty)

**Step 1: Create GitHub repo**

```bash
cd C:/DevProjects/schule/zzz_TOP/Mathepfade
gh repo create Nachbar-blip/Mathepfade --public --source=. --push
```

**Step 2: Copy shared engine files from Ref4OHG**

```bash
cp ../Ref4OHG/spirale-engine.js .
cp ../Ref4OHG/spirale.css .
```

These are the bugfixed versions (feedback-richtig/falsch, correct/wrong MC classes, input styling, level animation fix, comma regex, etc.).

**Step 3: Create .gitignore**

```
__pycache__/
.pytest_cache/
tests/reports/
*.pyc
```

**Step 4: Create directories**

```bash
mkdir -p trainer tests/reports
```

**Step 5: Commit scaffolding**

```bash
git add .gitignore spirale-engine.js spirale.css
git commit -m "chore: Scaffolding — Engine + CSS von Ref4OHG (mit Bugfixes)"
git push
```

---

## Task 1: index.html Dashboard

**Files:**
- Create: `index.html`
- Reference: `../Ref4OHG/index.html` (1195 Zeilen) and `../DifferenzierungsEngine/index.html`

**Step 1: Build index.html**

Adapt from Ref4OHG with these changes:

- **Title:** "Mathepfade — Adaptives Mathe-Training"
- **Subtitle:** "Thüringen · Gymnasium · Klasse 7–12"
- **Gradient:** New color scheme — use `#10b981` (emerald) to `#059669` (darker emerald) for a fresh look distinct from Ref4OHG (#667eea/#764ba2) and DiffEngine (same)
- **Klassen-Filter:** Alle | 7 | 8 | 9 | 10 | 11 | 12 (NO Klasse 13)
- **Niveau-Filter:** Alle | Nur GK | Nur LK (like DiffEngine, NOT gA/eA)
- **CSS filter classes:** `filter-gk` hides `.lk-only`, `filter-lk` hides `.theme-row:not(.lk-only)`
- **localStorage keys:** `mathepfade-klasse-filter`, `mathepfade-gklk-filter`
- **6 column groups:** col-7 through col-12

Section cards per Klasse organized into Analysis / Geometrie / Stochastik sections. LK trainers get class `lk-only` and an LK-badge.

Full trainer grid layout (90 rows total):

**Klasse 7 (12 Trainer):**
- A · Terme & Gleichungen: 7-terme-aufstellen, 7-terme-umformungen, 7-binomische-formeln, 7-gleichungen-linear, 7-ungleichungen, 7-potenzgesetze
- B · Geometrie: 7-dreiecke-kongruenz, 7-konstruktionen, 7-winkel-winkelsumme, 7-symmetrie, 7-vierecke
- C · Stochastik: 7-daten-diagramme

**Klasse 8 (14 Trainer):**
- A · Algebra & Funktionen: 8-bruchterme-grundlagen, 8-bruchgleichungen, 8-lineare-funktionen-grund, 8-lineare-funktionen-anwendungen, 8-lgs, 8-potenzen-negativ, 8-proportionalitaet
- B · Geometrie: 8-aehnlichkeit-streckung, 8-strahlensatz, 8-kreise, 8-raumgeometrie-grund, 8-vektoren-2d
- C · Stochastik: 8-stoch-laplace, 8-stoch-zaehlprinzip

**Klasse 9 (16 Trainer):**
- A · Analysis: 9-quadratwurzeln, 9-potenzen-ganzzahlig, 9-potenzen-rational, 9-quadratische-funktionen, 9-quadratische-gleichungen, 9-exponentielles-wachstum, 9-wurzelgleichungen, 9-potenzgleichungen
- B · Geometrie: 9-pythagoras, 9-trig-rechtwinkliges-dreieck, 9-raumgeometrie-prisma-zylinder, 9-raumgeometrie-pyramide-kegel, 9-raumgeometrie-anwendungen, 9-flaechenberechnung-determinante
- C · Stochastik: 9-stoch-haeufigkeiten, 9-stoch-boxplot

**Klasse 10 (14 Trainer):**
- A · Analysis: 10-ganzrationale-funktionen, 10-polynomdivision, 10-potenzfunktionen, 10-graphen-transformationen, 10-exponentialfunktionen, 10-logarithmus, 10-substitution
- B · Geometrie: 10-trig-einheitskreis, 10-trig-sinusfunktion, 10-trig-gleichungen, 10-trig-sinussatz-kosinussatz, 10-kreissektor
- C · Stochastik: 10-stoch-bedingte-wsk, 10-stoch-mehrstufig

**Klasse 11 (15 Trainer — 11 GK + 4 LK):**
- A · Analysis: 11-aenderungsrate, 11-ableitungsregeln, 11-ableitung-ketten-produkt, 11-monotonie-kruemmung, 11-extrempunkte-wendepunkte, 11-kurvendiskussion-ganzrational, 11-tangenten-normalen, 11-extremwertaufgaben, 11-e-funktion, 11-e-funktion-ableitung, 11-steckbriefaufgaben
- A · Analysis LK: 11-lk-funktionsscharen, 11-lk-newton, 11-lk-gebrochen-rational, 11-lk-kurvendisk-erweitert

**Klasse 12 (19 Trainer — 11 GK + 8 LK):**
- A · Analysis: 12-stammfunktionen, 12-bestimmtes-integral, 12-flaechenberechnung
- A · Analysis LK: 12-lk-integral-rotationskoerper, 12-lk-integral-uneigentlich, 12-lk-dgl
- B · Geometrie: 12-vektoren-grundlagen, 12-geraden-raum, 12-ebenen, 12-skalarprodukt
- B · Geometrie LK: 12-lk-geom-abstaende, 12-lk-geom-lagebeziehungen, 12-lk-geom-schnittwinkel
- C · Stochastik: 12-stoch-binomialverteilung, 12-stoch-sigma-regeln, 12-stoch-zufallsgroessen, 12-stoch-hypothesentests
- C · Stochastik LK: 12-lk-stoch-normalverteilung, 12-lk-stoch-prozesse

**Step 2: Verify localStorage progress display works**

The JS at the bottom of index.html reads `spirale-*` keys and updates level-badges + progress bars. The key pattern is `spirale-{dateiname-ohne-html}`. Ensure all 90 data-key attributes match.

**Step 3: Commit**

```bash
git add index.html
git commit -m "feat: index.html Dashboard — 90 Trainer, Klasse 7–12, GK/LK-Filter"
git push
```

---

## Task 2: Klasse 7 Trainer (12 Dateien)

**Files:**
- Create: `trainer/7-terme-aufstellen.html`
- Create: `trainer/7-terme-umformungen.html`
- Create: `trainer/7-binomische-formeln.html`
- Create: `trainer/7-gleichungen-linear.html`
- Create: `trainer/7-ungleichungen.html`
- Create: `trainer/7-potenzgesetze.html`
- Create: `trainer/7-dreiecke-kongruenz.html`
- Create: `trainer/7-konstruktionen.html`
- Create: `trainer/7-winkel-winkelsumme.html`
- Create: `trainer/7-symmetrie.html`
- Create: `trainer/7-vierecke.html`
- Create: `trainer/7-daten-diagramme.html`
- Reference: `../Ref4OHG/trainer/7-dreiecke-konstruktionen.html` (~388 Zeilen)

**Pattern for every trainer HTML file:**

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{Thema} - Mathepfade</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
    <link rel="stylesheet" href="../spirale.css">
    <style>:root { --spirale-primary: #10b981; --spirale-secondary: #059669; }</style>
</head>
<body>
    <div class="spirale-container" id="app"></div>
    <script>
    const THEMA_KEY = '{dateiname-ohne-html}';
    const THEMA_CONFIG = { name: '{Thema}', bereich: '{analysis|geometrie|stochastik}' };
    const AUFGABEN = [
      // ========== LEVEL 1 — babyleicht ==========
      { id: 1, level: 1, typ: "mc"|"numerisch", frage: "...", ... },
      // 6 Aufgaben pro Level, 6 Level = 36 total
    ];
    </script>
    <script src="../spirale-engine.js"></script>
</body>
</html>
```

**Aufgaben-Regeln (KRITISCH — fuer jeden Trainer einhalten):**
- Exakt 36 Aufgaben: 6 Level x 6 Aufgaben
- IDs: 1–36 fortlaufend
- Level 1 (babyleicht) bis Level 6 (wagnerisch) — Schwierigkeit steigend
- typ "mc": Felder frage, optionen (4 Stueck), korrekt (0-basierter Index), tipp, loesungsweg
- typ "numerisch": Felder frage, loesung (Zahl), toleranz (optional, default 0), tipp, loesungsweg
- Mathe-Formeln in KaTeX: `\\( ... \\)` inline, `$$ ... $$` display
- Loesungsweg darf HTML enthalten (`<b>`, `<br>`)
- Thueringer Lehrplan beachten — Aufgaben muessen zum LP passen
- Mix aus MC und numerisch pro Level (ca. 3:3 oder 4:2)

**Step 1: Create all 12 Klasse-7 trainer files**

Use parallel subagents — 4 Trainer pro Agent (3 Agents). Each agent reads the reference trainer `../Ref4OHG/trainer/7-dreiecke-konstruktionen.html` for pattern, then creates Thueringen-spezifische Aufgaben.

**Step 2: Verify each file has exactly 36 Aufgaben, 6 Level a 6**

Quick local check (open in browser or grep for `id:` count).

**Step 3: Commit**

```bash
git add trainer/7-*.html
git commit -m "feat: Klasse 7 — 12 Trainer (Terme, Gleichungen, Geometrie, Daten)"
git push
```

---

## Task 3: Klasse 8 Trainer (14 Dateien)

**Files:** Create `trainer/8-*.html` (14 files as listed in design doc)

Same pattern as Task 2. Themen: Bruchterme, Bruchgleichungen, lineare Funktionen, LGS, Potenzen negativ, Proportionalitaet, Aehnlichkeit, Strahlensatz, Kreise, Raumgeometrie, Vektoren 2D, Stochastik.

**Step 1: Create all 14 trainer files** (parallel: 5+5+4 Agents)
**Step 2: Verify 36 Aufgaben pro Datei**
**Step 3: Commit**

```bash
git add trainer/8-*.html
git commit -m "feat: Klasse 8 — 14 Trainer (Bruchterme, lin. Fkt., LGS, Geometrie, Stochastik)"
git push
```

---

## Task 4: Klasse 9 Trainer (16 Dateien)

**Files:** Create `trainer/9-*.html` (16 files as listed in design doc)

Themen: Quadratwurzeln, Potenzen, quadratische Fkt/Gleichungen, exp. Wachstum, Pythagoras, Trig, Raumgeometrie (Prisma/Zylinder/Pyramide/Kegel), Determinante, Stochastik, Wurzel-/Potenzgleichungen.

**Step 1: Create all 16 trainer files** (parallel: 4x4 Agents)
**Step 2: Verify 36 Aufgaben pro Datei**
**Step 3: Commit**

```bash
git add trainer/9-*.html
git commit -m "feat: Klasse 9 — 16 Trainer (Quadratisch, Potenzen, Trig, Raumgeometrie)"
git push
```

---

## Task 5: Klasse 10 Trainer (14 Dateien)

**Files:** Create `trainer/10-*.html` (14 files as listed in design doc)

Themen: Ganzrationale Fkt., Polynomdivision, Potenzfkt., Graphen-Trafo, Exponentialfkt., Logarithmus, Substitution, Trig (Einheitskreis, Sinusfkt., Gleichungen, Saetze), Kreissektor, bedingte Wsk., mehrstufig.

**Step 1: Create all 14 trainer files** (parallel: 5+5+4 Agents)
**Step 2: Verify 36 Aufgaben pro Datei**
**Step 3: Commit**

```bash
git add trainer/10-*.html
git commit -m "feat: Klasse 10 — 14 Trainer (Ganzrational, Trig, Exp/Log, Stochastik)"
git push
```

---

## Task 6: Klasse 11 Trainer (15 Dateien — 11 GK + 4 LK)

**Files:** Create `trainer/11-*.html` (15 files as listed in design doc)

GK: Aenderungsrate, Ableitungsregeln, Ketten/Produktregel, Monotonie, Extrempunkte, Kurvendiskussion, Tangenten, Extremwertaufgaben, e-Funktion (2x), Steckbriefaufgaben.
LK: Funktionsscharen, Newton, gebr.-rationale Fkt., erweiterte Kurvendiskussion.

**Step 1: Create all 15 trainer files** (parallel: 5+5+5 Agents)
**Step 2: Verify 36 Aufgaben pro Datei**
**Step 3: Commit**

```bash
git add trainer/11-*.html trainer/11-lk-*.html
git commit -m "feat: Klasse 11 — 15 Trainer (Analysis GK + 4 LK-Vertiefungen)"
git push
```

---

## Task 7: Klasse 12 Trainer (19 Dateien — 11 GK + 8 LK)

**Files:** Create `trainer/12-*.html` (19 files as listed in design doc)

GK Analysis: Stammfunktionen, bestimmtes Integral, Flaechenberechnung.
GK Geometrie: Vektoren, Geraden, Ebenen, Skalarprodukt.
GK Stochastik: Binomialverteilung, Sigma-Regeln, Zufallsgroessen, Hypothesentests.
LK Analysis: Rotationskoerper, uneigentliche Integrale, DGL.
LK Geometrie: Abstaende, Lagebeziehungen, Schnittwinkel.
LK Stochastik: Normalverteilung, stochastische Prozesse.

**Step 1: Create all 19 trainer files** (parallel: 5+5+5+4 Agents)
**Step 2: Verify 36 Aufgaben pro Datei**
**Step 3: Commit**

```bash
git add trainer/12-*.html trainer/12-lk-*.html
git commit -m "feat: Klasse 12 — 19 Trainer (Analysis, Vektoren, Stochastik GK + 8 LK)"
git push
```

---

## Task 8: Playwright Test Suite

**Files:**
- Create: `tests/conftest.py`
- Create: `tests/helpers.py`
- Create: `tests/test_trainer.py`
- Create: `tests/pytest.ini`
- Create: `tests/requirements.txt`
- Reference: `../Ref4OHG/tests/` (identisches Pattern)

**Step 1: Create test files**

Adapt from Ref4OHG tests:
- `BASE_URL = "https://nachbar-blip.github.io/Mathepfade"`
- `TRAINER_FILES` = list of all 90 `.html` filenames
- Tests: test_seite_laedt, test_keine_js_fehler, test_katex_rendert, test_36_aufgaben, test_6_level_je_6, test_alle_aufgaben_durchspielbar

**Step 2: Commit**

```bash
git add tests/
git commit -m "test: Playwright-Testsuite fuer alle 90 Trainer"
git push
```

---

## Task 9: QR-Code DOCX + GitHub Pages

**Step 1: Enable GitHub Pages**

```bash
gh api repos/Nachbar-blip/Mathepfade/pages -X POST -f source.branch=master -f source.path=/
```

**Step 2: Verify deployment**

Wait for Pages build, then check `https://nachbar-blip.github.io/Mathepfade/`

**Step 3: Generate QR-Code DOCX** (optional, same pattern as Ref4OHG_QR.docx)

**Step 4: Final commit**

```bash
git add Mathepfade_QR.docx
git commit -m "docs: QR-Code Dokument fuer Mathepfade"
git push
```

---

## Execution Notes

- **Parallelisierung:** Tasks 2–7 (Trainer-Dateien) sind komplett unabhaengig und koennen maximal parallelisiert werden. Pro Task koennen 3–5 Subagents parallel arbeiten.
- **Qualitaetskontrolle:** Nach jedem Task: Aufgaben-Count pruefen (36 pro Datei), KaTeX-Syntax pruefen, Lehrplan-Abdeckung pruefen.
- **Reihenfolge:** Task 0 → Task 1 → Tasks 2–7 (parallel) → Task 8 → Task 9
- **Geschaetzter Umfang:** 90 Trainer x ~380 Zeilen = ~34.200 Zeilen Trainer-Code + ~1.200 Zeilen index.html + Engine/CSS/Tests
