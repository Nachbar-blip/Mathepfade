# Mathepfade: Thüringer Lehrplan + Level-Progression — Umsetzungsplan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Alle 90 Mathepfade-Trainer dem Thüringer Lehrplan (Gymnasium 2018) zuordnen und Stufe 4–6 jedes Trainers nach der DiffEngine-Rubrik zu echten Anforderungsstufen machen.

**Architecture:** Klassenzuordnung lebt allein in `index.html` (Spalten `.col-7` … `.col-12`); Dateinamen bleiben (QR-Links). Aufgaben liegen je Trainer als JS-Array `AUFGABEN` (36 Stück, 6 Level × 6) in `trainer/<datei>.html`. Zwei Python-Gates (`tests/level_check.py`, `tests/katex_check.py`) plus Playwright-Suite prüfen; ein neues Gate `tests/lehrplan_check.py` verhindert lehrplanfremde Inhalte. Arbeit in Wellen je Klasse, ein Commit je Block.

**Tech Stack:** Vanilla HTML/JS + KaTeX 0.16.9, Python 3 (pytest, playwright), node (zum Auswerten der AUFGABEN-Arrays), Wolfram-MCP zum Nachrechnen.

**Design:** `docs/plans/2026-09-26-lehrplan-th-und-level-progression-design.md` (freigegeben).

---

## Verbindliche Regeln für jede Aufgabe (aus dem Design, Teil 2)

| Stufe | AFB | Kriterium | Verboten |
|---|---|---|---|
| 1 | I | ein Rechenschritt, schöne Zahlen | Kontext |
| 2 | I | Standardverfahren, zwei Schritte | Kontext, Parameter |
| 3 | I | Klassenarbeits-Standard, Zwischenergebnis | Formel im Text |
| 4 | II | Verfahren wählen / Modell aus Text / Umkehraufgabe | Rechenweg im Text, „Addiere …" |
| 5 | III | zwei Verfahren kombinieren / Parameter aus zwei Bedingungen / Fehler finden | gelieferte Formel, Auswertung bei x = 0 |
| 6 | III | Fallunterscheidung / Behauptung begründet prüfen / Abi-Format (11/12) | L1–L3-Muster mit Kontext |

Weitere Regeln: Level ≠ Teilthema; MC nur, wenn die Auswahl selbst die Leistung ist; keine Rückverweise auf die Vorgängeraufgabe („Dazu b = ?"); Umlaute echt (kein „Flaeche"); Fettdruck als `<b>…</b>`, nie `**`; numerische Aufgaben mit `toleranz`; **Aufgabentexte mit LaTeX nie per Bash-Heredoc schreiben** (Backslash-Verlust) — immer Write/Edit oder Scratchpad-`.js` + Einsetz-Skript, das Zeilenenden erhält.

Aufgabenformat (unverändert):

```js
{ id:19, level:4, typ:"numerisch", frage:"…", loesung:12.5, toleranz:0.1, tipp:"…", loesungsweg:"…" },
{ id:22, level:4, typ:"mc", frage:"…", optionen:["…","…","…","…"], korrekt:2, tipp:"…", loesungsweg:"…" },
```

## Prüfschleife je Block (bindend, Design Teil 3)

```bash
# im Ordner Trainer-Public/Mathepfade
python tests/level_check.py --strict trainer/<datei>.html …     # Exit 0
python tests/lehrplan_check.py --strict                            # Exit 0 (ab Task 2)
python -m http.server 8765 &                                       # einmal je Sitzung
python tests/katex_check.py trainer/<datei>.html …                 # 0 Render-Fehler
python -m pytest tests/test_trainer.py -k "<datei>" -q             # grün
python tests/bild.py trainer/<datei>.html                          # PNG erzeugen …
```
… und das PNG mit dem Read-Tool **ansehen** (Sichtprüfung, `schule/CLAUDE.md`). Jede Zahl vorher mit Wolfram nachgerechnet.

---

### Task 1: Index-Umzug und gA/eA-Benennung

**Files:**
- Modify: `index.html` (Spalten `.col-7` … `.col-12`, Filterleiste Zeile ~338–342, CSS Zeile 188–189, JS Zeile ~1162)
- Modify: `trainer/*.html` — `<title>` und `THEMA_CONFIG.name` der 12 `*-lk-*`-Trainer („(LK)" → „(eA)")
- Create: `tests/test_index.py`

**Step 1: Test schreiben (Klassenzuordnung aus index.html)**

```python
# tests/test_index.py
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = (ROOT / "index.html").read_text(encoding="utf-8")

def spalten():
    """{dateiname: klasse} aus den .col-N-Blöcken von index.html."""
    out = {}
    for m in re.finditer(r'<div class="col col-(\d+)">(.*?)(?=<div class="col col-|</div>\s*<!-- /grid|\Z)',
                         INDEX, re.S):
        klasse = int(m.group(1))
        for h in re.findall(r'href="trainer/([^"]+\.html)"', m.group(2)):
            out[h] = klasse
    return out

ERWARTET = {
    "9-pythagoras.html": 8, "9-raumgeometrie-prisma-zylinder.html": 8,
    "9-raumgeometrie-pyramide-kegel.html": 8,
    "7-potenzgesetze.html": 9, "8-potenzen-negativ.html": 9, "8-strahlensatz.html": 9,
    "8-aehnlichkeit-streckung.html": 9, "8-lgs.html": 9, "8-bruchgleichungen.html": 9,
}

def test_umzug_nach_th_lehrplan():
    s = spalten()
    for datei, klasse in ERWARTET.items():
        assert s[datei] == klasse, f"{datei}: Spalte {s.get(datei)}, erwartet {klasse}"

def test_alle_90_trainer_im_index():
    s = spalten()
    dateien = {p.name for p in (ROOT / "trainer").glob("*.html")}
    assert set(s) == dateien

def test_kein_gk_lk_sichtbar():
    sichtbar = re.sub(r"<script.*?</script>|<style.*?</style>", "", INDEX, flags=re.S)
    assert "Nur GK" not in sichtbar and "Nur LK" not in sichtbar
    assert re.search(r">\s*LK\s*<", sichtbar) is None
    assert "Nur gA" in sichtbar and "Nur eA" in sichtbar
```

Hinweis: Die Regex für die Spalten muss gegen die reale Struktur geprüft werden (`grep -n 'class="col col-' index.html`); falls die Spalten anders schließen, Grenze anpassen, bis `test_alle_90_trainer_im_index` vor dem Umzug grün ist.

**Step 2: Test laufen lassen — muss fehlschlagen**

Run: `python -m pytest tests/test_index.py -q -p no:cacheprovider --override-ini addopts=""`
Expected: `test_umzug_nach_th_lehrplan` FAIL, `test_kein_gk_lk_sichtbar` FAIL, `test_alle_90_trainer_im_index` PASS.

**Step 3: Zeilen verschieben**

Je Trainer den kompletten `<a class="theme-row" …>…</a>`-Block (6 Zeilen) ausschneiden und in die Zielspalte einfügen:
- nach `.col-8`, Abschnitt „B · Geometrie": 9-pythagoras, 9-raumgeometrie-prisma-zylinder, 9-raumgeometrie-pyramide-kegel
- nach `.col-9`, Abschnitt „A · Analysis": 7-potenzgesetze, 8-potenzen-negativ, 8-lgs, 8-bruchgleichungen
- nach `.col-9`, Abschnitt „B · Geometrie": 8-strahlensatz, 8-aehnlichkeit-streckung

Connector-Zeichen prüfen: letzte Zeile eines Abschnitts `&#x2514;`, sonst `&#x251C;`.

**Step 4: gA/eA**

- Filterbuttons: `Nur GK` → `Nur gA`, `Nur LK` → `Nur eA` (data-filter-Werte bleiben `gk`/`lk`)
- Abschnittstitel „A · Analysis LK" → „A · Analysis eA" (analog Geometrie, Stochastik)
- `<span class="lk-badge">LK</span>` → `<span class="lk-badge">eA</span>` (12 Stellen)
- In den 12 `*-lk-*`-Trainern: `<title>… (LK) - Mathepfade</title>` → `(eA)`, `THEMA_CONFIG.name` ebenso.
- Kommentar über der Filterleiste: `<!-- Thüringen: grundlegendes (gA) / erhöhtes Anforderungsniveau (eA), Lehrplan Gymnasium 2018 Kap. 4 -->`

**Step 5: Tests grün**

Run: `python -m pytest tests/test_index.py -q --override-ini addopts=""`
Expected: 3 passed.

**Step 6: Sichtprüfung**

Run: `python tests/bild.py index.html` (Task 3 liefert das Skript — falls noch nicht vorhanden, Task 3 vorziehen) und PNG ansehen: Spalten 8 und 9 vollständig, keine leeren Abschnitte, Filter „Nur gA / Nur eA".

**Step 7: Commit**

```bash
git add index.html trainer/*-lk-*.html tests/test_index.py
git commit -m "Thueringer Lehrplan: 9 Trainer in Doppeljahrgang-Spalte verschoben, gA/eA statt GK/LK"
```

---

### Task 2: Lehrplan-Gate `tests/lehrplan_check.py`

**Files:**
- Create: `tests/lehrplan_check.py`
- Create: `tests/test_lehrplan_check.py`

**Step 1: Test schreiben**

```python
# tests/test_lehrplan_check.py
from pathlib import Path
import lehrplan_check as lc

def test_verbotene_begriffe_je_klasse():
    assert "vektor" in lc.VERBOTEN[8] and "determinante" in lc.VERBOTEN[9]
    assert "hypothesentest" in lc.VERBOTEN[12] and "polynomdivision" in lc.VERBOTEN[10]

def test_findet_treffer_im_text():
    aufgaben = [{"id": 1, "level": 1, "frage": "Berechne die Determinante.", "loesungsweg": ""}]
    assert lc.pruefe(9, "x.html", aufgaben) == ["x.html #1 L1: 'determinante' (Kl. 9 nicht im TH-Lehrplan)"]

def test_erlaubte_woerter_bleiben_still():
    aufgaben = [{"id": 1, "level": 1, "frage": "Berechne den Wachstumsfaktor.", "loesungsweg": ""}]
    assert lc.pruefe(9, "x.html", aufgaben) == []
```

**Step 2: Test laufen lassen — Fehler „No module named lehrplan_check"**

Run: `cd tests && python -m pytest test_lehrplan_check.py -q --override-ini addopts=""`

**Step 3: Implementieren**

```python
# tests/lehrplan_check.py
"""Lehrplan-Gate Thueringen (Gymnasium 2018): meldet Begriffe, die in der Klassenspalte
laut TH-Lehrplan nicht vorkommen duerfen. Klassenzuordnung wird aus index.html gelesen.

Aufruf:  python tests/lehrplan_check.py [--strict] [trainer/x.html ...]
"""
import re, sys
from pathlib import Path
from level_check import lade_aufgaben, normalisiere, ROOT, TRAINER_DIR

INDEX = ROOT / "index.html"

# Begriffe (kleingeschrieben, Teilwort reicht), die in dieser Klasse NICHT auftauchen duerfen.
_SI_VEKTOR = {"vektor", "determinante", "skalarprodukt"}
_KEIN_TH = {"polynomdivision", "hypothesentest", "signifikanzniveau", "nullhypothese",
            "newton-verfahren", "newtonverfahren", "differenzialgleichung", "differentialgleichung",
            "übergangsmatrix", "uneigentliche"}
VERBOTEN = {
    7: _SI_VEKTOR | _KEIN_TH | {"logarithm", "sinus", "kosinus", "ableitung"},
    8: _SI_VEKTOR | _KEIN_TH | {"logarithm", "ableitung"},
    9: _SI_VEKTOR | _KEIN_TH | {"ableitung", "integral"},
    10: _SI_VEKTOR | _KEIN_TH | {"integral"},
    11: _KEIN_TH,
    12: _KEIN_TH,
}
# Woerter, die einen Treffer entschaerfen (z. B. "Sinus" in 9-trig-* ist erlaubt).
AUSNAHMEN = {
    9: {"sinus", "kosinus"},   # 9-trig-* (TH 9/10)
}

def klassen_aus_index() -> dict:
    html = INDEX.read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r'<div class="col col-(\d+)">(.*?)(?=<div class="col col-|\Z)', html, re.S):
        for h in re.findall(r'href="trainer/([^"]+\.html)"', m.group(2)):
            out[h] = int(m.group(1))
    return out

def pruefe(klasse: int, name: str, aufgaben: list) -> list:
    verboten = VERBOTEN.get(klasse, set()) - AUSNAHMEN.get(klasse, set())
    treffer = []
    for a in aufgaben:
        text = normalisiere(" ".join(str(a.get(k, "")) for k in ("frage", "loesungsweg", "tipp"))
                            + " " + " ".join(a.get("optionen", []) or []))
        for w in sorted(verboten):
            if w in text:
                treffer.append(f"{name} #{a['id']} L{a['level']}: '{w}' (Kl. {klasse} nicht im TH-Lehrplan)")
                break
    return treffer

def main(argv):
    strict = "--strict" in argv
    dateien = [ROOT / x for x in argv if x.endswith(".html")] or sorted(TRAINER_DIR.glob("*.html"))
    klassen = klassen_aus_index()
    fehler = []
    for d in dateien:
        k = klassen.get(d.name)
        if k is None:
            fehler.append(f"{d.name}: nicht in index.html"); continue
        fehler += pruefe(k, d.name, lade_aufgaben(d))
    for f in fehler: print("FEHLER", f)
    print(f"{len(fehler)} Befunde in {len(dateien)} Trainern")
    return 1 if (fehler and strict) else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
```

Wortlisten sind ein Startpunkt: Beim ersten Lauf über alle 90 Trainer die Treffer sichten und die Listen so anpassen, dass **nur** die 8 Ersatz-Trainer (Design 1b) und echte Verstöße gemeldet werden. Jede Ausnahme mit Kommentar und TH-Kapitelnummer begründen.

**Step 4: Tests grün, Gate laufen lassen**

Run: `cd tests && python -m pytest test_lehrplan_check.py -q --override-ini addopts=""` → 3 passed
Run: `python tests/lehrplan_check.py` → Befunde ausschließlich in den 8 Ersatz-Trainern (die verschwinden mit den Wellen).

**Step 5: Commit**

```bash
git add tests/lehrplan_check.py tests/test_lehrplan_check.py
git commit -m "Lehrplan-Gate Thueringen: verbotene Begriffe je Klassenspalte"
```

---

### Task 3: Screenshot-Werkzeug `tests/bild.py`

**Files:**
- Create: `tests/bild.py` (Vorbild: `../../Trainer-Lokal/KA-Generator/blattbild.py`, Funktion `bild()`)

**Step 1: Skript**

```python
# tests/bild.py
"""Screenshot eines Trainers/Index fuer die Sichtpruefung.
Aufruf: python tests/bild.py trainer/7-vierecke.html [--level 5]  -> tests/reports/bild-<name>[-L5].png
Braucht python -m http.server 8765 im Projektordner (KaTeX-CDN, relative Pfade)."""
import sys, os
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
BASE = os.environ.get("DIFFENGINE_BASE_URL", "http://127.0.0.1:8765")

def bild(rel: str, level: int | None = None) -> Path:
    ziel = ROOT / "tests" / "reports" / (f"bild-{Path(rel).stem}" + (f"-L{level}" if level else "") + ".png")
    with sync_playwright() as p:
        b = p.chromium.launch(); page = b.new_page(viewport={"width": 1240, "height": 900})
        page.goto(f"{BASE}/{rel}"); page.wait_for_timeout(1500)
        if level:  # Level im localStorage setzen und neu laden, damit eine L5/L6-Aufgabe sichtbar ist
            key = page.evaluate("typeof THEMA_KEY!=='undefined'?THEMA_KEY:null")
            if key:
                page.evaluate(f"localStorage.setItem('spirale-{key}', JSON.stringify({{level:{level},streak:0}}))")
                page.reload(); page.wait_for_timeout(1500)
        page.screenshot(path=str(ziel), full_page=True); b.close()
    return ziel

if __name__ == "__main__":
    args = sys.argv[1:]; lvl = int(args[args.index("--level") + 1]) if "--level" in args else None
    print(bild(args[0], lvl))
```

Vorher in `spirale-engine.js` prüfen, unter welchem Schlüssel und in welcher Form der Zustand gespeichert wird (`grep -n "localStorage" spirale-engine.js`), und die `setItem`-Zeile daran anpassen.

**Step 2: Ausprobieren**

Run: `python tests/bild.py trainer/7-vierecke.html --level 5` → PNG mit dem Read-Tool ansehen: Aufgabe sichtbar, KaTeX gerendert, kein abgeschnittener Text.

**Step 3: Commit**

```bash
git add tests/bild.py
git commit -m "tests/bild.py: Screenshot fuer die Sichtpruefung je Trainer und Level"
```

---

## Wellen (Task 4 bis 10)

Jede Welle folgt demselben Verfahren je Trainer. Der Ausführende arbeitet die Trainer **einzeln** ab und committet je Block von 3–5 Trainern.

### Verfahren je Trainer (Standard, „Progression")

1. Audit lesen: Zeile des Trainers in `docs/audit/audit-2026-09-19-mathepfade.md` (Befunde KOLLAPS/KEIN_AFB3/KURZ).
2. Aktuelle Aufgaben lesen: `node -e` wie in `tests/level_check.py::lade_aufgaben` oder direkt die Datei.
3. Neuen Stufenblock schreiben — Stufe 5 und 6 komplett (12 Aufgaben); Stufe 4, wenn das Audit KOLLAPS L3/L4 oder L4/L5 meldet. Vorlagen: passender Trainer der DiffEngine (`../DifferenzierungsEngine/trainer/`, eigene Arbeit, darf adaptiert werden) und Aufgaben*formen* aus dem Materialindex (nur lokal lesen, umformulieren, keine Quellenangabe, kein Rohtext).
4. Jede Lösung mit Wolfram nachrechnen (`mcp WolframAlpha`), Ergebnis im Lösungsweg.
5. Block in die Datei einsetzen (Write/Edit; Zeilenenden CRLF/LF der Datei beibehalten — vorher `file trainer/x.html` bzw. `git config core.autocrlf` beachten).
6. Kriterien-Zeilen in `docs/plans/2026-09-26-klN-kriterien.md` eintragen (Tabelle id / Level / Kriterium, Muster: `../DifferenzierungsEngine/docs/plans/2026-09-18-kl11-kriterien.md`).
7. Prüfschleife (oben), PNG bei `--level 5` und `--level 6` ansehen.

### Verfahren je Trainer („Ersatz", die 8 aus Design 1b)

Wie Standard, aber alle 36 Aufgaben neu, dazu `<title>`, `THEMA_CONFIG.name`, Index-Zeilentext (`theme-name`) und ein Kommentar in Zeile 2 der Datei: `<!-- Dateiname historisch (QR-Links); Inhalt seit 2026-09: <neues Thema>, TH-Lehrplan Kap. <x> -->`. Levelaufbau ist unten je Trainer vorgegeben.

### Verfahren „Umzug" (die 9 aus Design 1a)

Standard, zusätzlich Stufe 1–3 auf Vorwissen der Zielklasse prüfen: In Kl. 8 kein Wurzelgesetz, kein Logarithmus, keine Potenz mit negativem Exponenten; in Kl. 9 dürfen Potenzgesetze/LGS-Aufgaben Zahlen aus 9/10 (Wurzeln, quadratische Gleichungen) nutzen.

---

### Task 4: Welle Kl. 7 (11 Trainer)

**Files (Modify):** `trainer/7-binomische-formeln.html`, `7-daten-diagramme`, `7-dreiecke-kongruenz`, `7-gleichungen-linear`, `7-konstruktionen`, `7-symmetrie`, `7-terme-aufstellen`, `7-terme-umformungen`, `7-ungleichungen`, `7-vierecke`, `7-winkel-winkelsumme`
**Create:** `docs/plans/2026-09-26-kl7-kriterien.md`

Blöcke: A Terme/Gleichungen (binomische-formeln, gleichungen-linear, terme-aufstellen, terme-umformungen, ungleichungen) → B Geometrie (dreiecke-kongruenz, konstruktionen, symmetrie, vierecke, winkel-winkelsumme) → C daten-diagramme.
Vorrang laut Audit: 7-binomische-formeln (KOLLAPS L4/L5), 7-gleichungen-linear (KOLLAPS L3/L4, L4/L5), 7-potenzgesetze ist umgezogen (Task 6).
Lesart Kl. 7: L4 Rechenart selbst wählen; L5 zweischrittige Sachaufgabe ohne Weg oder Fehler in vorgelegter Rechnung; L6 Zahlenrätsel/Umkehraufgabe, „Stimmt die Behauptung?", Sonderfall (keine/unendlich viele Lösungen).
Commit je Block: `git commit -m "Level-Progression Kl. 7 Block A: …"`.

### Task 5: Welle Kl. 8 (12 Trainer)

**Files (Modify):** `8-kreise`, `8-lineare-funktionen-anwendungen`, `8-lineare-funktionen-grund`, `8-proportionalitaet`, `8-raumgeometrie-grund`, `8-stoch-laplace`, `8-stoch-zaehlprinzip`, `8-bruchterme-grundlagen`; Umzug: `9-pythagoras`, `9-raumgeometrie-prisma-zylinder`, `9-raumgeometrie-pyramide-kegel`; Ersatz: `8-vektoren-2d`
**Create:** `docs/plans/2026-09-26-kl8-kriterien.md`

Ersatz `8-vektoren-2d` → **Prozent- und Zinsrechnung** (TH 2.2.2), `THEMA_CONFIG = { name: 'Prozent- und Zinsrechnung', bereich: 'analysis' }`, Index-Text „Prozent &amp; Zinsen", Abschnitt A:
- L1: Prozentwert/Prozentsatz/Grundwert direkt (bequeme Sätze), Bruch ↔ Prozent
- L2: Grundaufgaben mit Dreisatz, Prozentsätze über 100 %
- L3: Rabatt, Skonto, Mehrwertsteuer, Steigerung um/auf, Jahreszinsen
- L4: Grundaufgabe selbst erkennen (Text ohne Nennung, was gesucht ist), Zinsen für Monate/Tage, Ratenzahlung
- L5: zweistufige Änderung (erst +20 %, dann −20 %), Fehler „Prozentpunkte vs. Prozent", Kapital aus Zinsen und Zinssatz
- L6: Behauptung prüfen („Zweimal 10 % Rabatt = 20 %?"), Zinssatz aus zwei Kontoständen, Vergleich zweier Angebote mit Fallunterscheidung
Vorlage (eigene Arbeit): `../DifferenzierungsEngine/trainer/7-prozent-grundaufgaben.html`, `7-prozent-anwendungen-zins.html` — Zahlen ändern, Duplikat-Warnung des Level-Gates beachten.

### Task 6: Welle Kl. 9 (19 Trainer, zwei Blöcke à ~10)

**Block 9A Algebra/Funktionen:** `9-exponentielles-wachstum`, `9-potenzen-ganzzahlig`, `9-potenzen-rational`, `9-potenzgleichungen`, `9-quadratische-funktionen`, `9-quadratische-gleichungen`, `9-quadratwurzeln`, `9-wurzelgleichungen`; Umzug: `7-potenzgesetze`, `8-potenzen-negativ`, `8-lgs`, `8-bruchgleichungen`
**Block 9B Geometrie/Stochastik:** `9-raumgeometrie-anwendungen`, `9-trig-rechtwinkliges-dreieck`, `9-stoch-boxplot`, `9-stoch-haeufigkeiten`; Umzug: `8-strahlensatz`, `8-aehnlichkeit-streckung`; Ersatz: `9-flaechenberechnung-determinante`
**Create:** `docs/plans/2026-09-26-kl9-kriterien.md`

Ersatz `9-flaechenberechnung-determinante` → **Flächen im Koordinatensystem** (TH 2.3.3: Dreiecksformel ½·a·b·sin γ, Zerlegen, Strahlensatz-Anteile), `name: 'Flächen im Koordinatensystem'`, Index-Text „Fl&auml;chen im Koordinatensystem", Abschnitt B:
- L1: Rechteck/Dreieck aus Gitterpunkten (achsenparallel)
- L2: Dreieck mit Grundseite auf Achse, Höhe ablesen
- L3: Umrechnung über Zerlegen in Rechteck minus Dreiecke
- L4: Verfahren wählen (Zerlegen oder ½·a·b·sin γ mit gegebenem Winkel), Trapez aus Punkten
- L5: fehlende Koordinate aus gegebener Fläche, Fehler in vorgelegter Zerlegung
- L6: Behauptung prüfen (Punkt auf Geraden ⇔ Fläche 0), Parameter, für den zwei Flächen gleich sind
Kein „Vektor", keine „Determinante" im Text (Gate).

### Task 7: Welle Kl. 10 (14 Trainer)

**Files (Modify):** `10-exponentialfunktionen`, `10-ganzrationale-funktionen`, `10-graphen-transformationen`, `10-kreissektor`, `10-logarithmus`, `10-potenzfunktionen`, `10-stoch-bedingte-wsk`, `10-stoch-mehrstufig`, `10-substitution`, `10-trig-einheitskreis`, `10-trig-gleichungen`, `10-trig-sinusfunktion`, `10-trig-sinussatz-kosinussatz`; Ersatz: `10-polynomdivision`
**Create:** `docs/plans/2026-09-26-kl10-kriterien.md`

`10-stoch-bedingte-wsk`: Schwerpunkt auf Vierfeldertafel und stochastische Unabhängigkeit (TH 2.3.4); der Begriff „bedingte Wahrscheinlichkeit" darf bleiben.
Ersatz `10-polynomdivision` → **Grenzwerte und Asymptoten** (TH 2.3.2: Grenzwertbegriff anschaulich, lim-Schreibweise, waagerechte/senkrechte Asymptoten), `name: 'Grenzwerte und Asymptoten'`, Index-Text „Grenzwerte &amp; Asymptoten", Abschnitt A:
- L1: Verhalten von x², x³, 1/x für x → ±∞ (MC), Wertetabelle deuten
- L2: lim von a·xⁿ + …, senkrechte Asymptote aus Nenner-Nullstelle
- L3: waagerechte Asymptote von (ax+b)/(cx+d), Exponentialfunktion mit Verschiebung
- L4: Funktionstyp aus Graph/Tabelle schließen und Asymptote angeben, Grenzwert ohne Nennung des Verfahrens
- L5: Parameter aus zwei Bedingungen (Asymptote y = 2 und Polstelle x = 1), Fehler in Grenzwert-Argumentation
- L6: Behauptung prüfen („Ein Graph schneidet seine Asymptote nie"), Fallunterscheidung nach Grad
Vorlage: `../DifferenzierungsEngine/trainer/11-analysis-grenzwerte.html` (GK-Teil, ohne Faktorisierung hebbarer Lücken).

### Task 8: Welle Kl. 11 (15 Trainer)

**Block 11A gA:** `11-ableitung-ketten-produkt`, `11-ableitungsregeln` (Audit: 10 Aufgaben bei x = 0 neu stellen), `11-aenderungsrate`, `11-e-funktion-ableitung`, `11-e-funktion`, `11-extrempunkte-wendepunkte`, `11-extremwertaufgaben`, `11-kurvendiskussion-ganzrational`, `11-monotonie-kruemmung`, `11-steckbriefaufgaben`, `11-tangenten-normalen`
**Block 11B eA:** `11-lk-funktionsscharen`, `11-lk-gebrochen-rational`, `11-lk-kurvendisk-erweitert`; Ersatz: `11-lk-newton`
**Create:** `docs/plans/2026-09-26-kl11-kriterien.md`

Stufe 6 in Kl. 11/12 = Abi-Format (IQB gA/eA als Vorlage der *Form*).
Ersatz `11-lk-newton` → **ln-Funktion** (TH 4.1 eA: ln als Umkehrfunktion von eˣ, Ableitung, Stammfunktion von 1/x), `name: 'ln-Funktion (eA)'`, Index-Text „ln-Funktion", Abschnitt „Analysis eA":
- L1: ln(e), ln 1, Umkehrung eˣ = 5 → x, Definitionsbereich
- L2: Ableitung von ln x, a·ln x, ln(x) + x², Tangentenanstieg
- L3: Ableitung ln(2x+1) (Kettenregel), Stammfunktion von 1/x und 3/x, Integral von 1 bis e
- L4: Gleichung ln(x) = 2 − x graphisch/CAS-frei einschätzen, Umkehrfunktion aus Graph bestimmen, Fläche unter 1/x ohne Nennung des Verfahrens
- L5: Parameter a mit ∫₁ᵃ 1/x dx = 2, Fehler „ln(a+b) = ln a + ln b" in Rechenweg finden, Extremum von x·ln x
- L6: Behauptung prüfen (ln x wächst langsamer als jede Wurzel — begründen), Schar f_k = ln(kx), Abi-Format
Vorlage: `../DifferenzierungsEngine/trainer/12-lk-analysis-ln-substitution.html` (nur ln-Teil).

### Task 9: Welle Kl. 12 (19 Trainer, drei Blöcke)

**Block 12A Analysis:** `12-bestimmtes-integral`, `12-flaechenberechnung`, `12-stammfunktionen`, `12-lk-integral-rotationskoerper`; Ersatz: `12-lk-integral-uneigentlich`
**Block 12B Geometrie:** `12-ebenen`, `12-geraden-raum`, `12-skalarprodukt`, `12-vektoren-grundlagen`, `12-lk-geom-abstaende`, `12-lk-geom-lagebeziehungen`, `12-lk-geom-schnittwinkel`; Ersatz: `12-lk-dgl`
**Block 12C Stochastik:** `12-stoch-binomialverteilung`, `12-stoch-sigma-regeln`, `12-stoch-zufallsgroessen`, `12-lk-stoch-normalverteilung`; Ersatz: `12-stoch-hypothesentests`, `12-lk-stoch-prozesse`
**Create:** `docs/plans/2026-09-26-kl12-kriterien.md`

Ersatz-Vorgaben:
- `12-lk-integral-uneigentlich` → **Stetigkeit, Asymptoten, Periodizität** (TH 4.1 eA), `name: 'Stetigkeit und Asymptoten (eA)'`, Abschnitt „Analysis eA". L1–L3: Stetigkeit anschaulich an abschnittsweise definierten Funktionen, Asymptoten von e-Funktionen und einfachen gebrochen-rationalen Termen, Periode von sin(bx); L4: Parameter für stetigen Anschluss; L5: zwei Bedingungen (stetig und differenzierbar), Fehler in Asymptoten-Begründung; L6: Behauptung prüfen, Abi-Format.
- `12-lk-dgl` → **Scharen von Geraden und Ebenen** (TH 4.2 eA), `name: 'Geraden- und Ebenenscharen (eA)'`, Abschnitt „Geometrie eA". L1–L3: gemeinsamer Punkt/Richtung einer Geradenschar, Ebenenschar durch feste Gerade, Parameter für Orthogonalität; L4: Parameter aus Lagebedingung ohne Nennung des Verfahrens; L5: Parameter aus zwei Bedingungen, Fehler in Lagebestimmung; L6: Fallunterscheidung nach Parameter (parallel/schneidend/identisch), Abi-Format.
- `12-stoch-hypothesentests` → **Prognoseintervalle (2σ-Regel)** (TH 4.3 gA), `name: 'Prognoseintervalle'`, Index-Text „Prognoseintervalle", Abschnitt „Stochastik". L1–L3: μ, σ, 95 %-Intervall für absolute und relative Häufigkeit; L4: aus Beobachtung h beurteilen, welche p ausgeschlossen werden können; L5: n aus gefordertem Intervall, Fehler bei σ-Berechnung; L6: Behauptung prüfen („Liegt h außerhalb, ist p sicher falsch?"), Abi-Format. **Keine** Wörter Hypothese/Signifikanz/Nullhypothese (Gate).
- `12-lk-stoch-prozesse` → **Konfidenzintervall und Stichprobenumfang** (TH 4.3 eA), `name: 'Konfidenzintervalle (eA)'`, Abschnitt „Stochastik eA". L1–L3: 95 %-Konfidenzintervall aus h und n (2σ, Näherung), Intervallbreite; L4: n für geforderte Genauigkeit abschätzen; L5: Vergleich zweier Stichproben, Fehler „Konfidenzintervall = Prognoseintervall"; L6: Normalverteilung als Näherung begründen, Abi-Format.

### Task 10: Abschluss

1. `python tests/level_check.py --strict` → Exit 0, `python tests/lehrplan_check.py --strict` → Exit 0, `python tests/katex_check.py` → 0 Fehler, `python -m pytest tests/ -q` → grün.
2. `docs/audit/audit-2026-09-19-mathepfade.md` um Abschnitt „Abschluss Level-Progression (Datum)" ergänzen: Messwerte je Trainer neu erzeugen (Skript aus dem Audit) und die KOLLAPS-Quote gegen DiffEngine (0,27) stellen.
3. `docs/plans/2026-09-19-level-progression-plan-ENTWURF.md` Status auf „umgesetzt, siehe 2026-09-26-Plan" setzen.
4. `Mathepfade_QR.docx` **nicht** neu erzeugen (Links unverändert); `_make_qr_doc.py` nur dann anfassen, wenn dort Themennamen stehen — dann die 8 neuen Namen eintragen.
5. Commit: `git commit -m "Level-Progression Mathepfade abgeschlossen: Audit-Nachmessung, Plan-Status"`.
