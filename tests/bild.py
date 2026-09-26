# -*- coding: utf-8 -*-
"""Screenshot eines Trainers oder des Index fuer die Sichtpruefung.

    python tests/bild.py trainer/7-vierecke.html            -> tests/reports/bild-7-vierecke.png
    python tests/bild.py trainer/7-vierecke.html --level 5  -> tests/reports/bild-7-vierecke-L5.png
    python tests/bild.py index.html                         -> tests/reports/bild-index.png

Braucht einen lokalen Server im Projektordner: python -m http.server 8765
(KaTeX kommt per CDN, die Trainer laden spirale-engine.js relativ).
Vorbild: Trainer-Lokal/KA-Generator/blattbild.py - das PNG wird angesehen, nicht gemessen.
"""
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = os.environ.get("MATHEPFADE_BASE_URL", "http://127.0.0.1:8765")


def _katex_abwarten(seite, ms=4000):
    """Wartet, bis KaTeX gesetzt hat - sonst zeigt das Bild rohes LaTeX."""
    try:
        seite.wait_for_function(
            "() => !window.katex || document.querySelectorAll('.katex').length > 0",
            timeout=ms)
    except Exception:
        seite.wait_for_timeout(800)


def bild(rel, level=None):
    """Schreibt tests/reports/bild-<name>[-L<level>].png und gibt den Pfad zurueck."""
    from playwright.sync_api import sync_playwright
    name = f"bild-{Path(rel).stem}" + (f"-L{level}" if level else "") + ".png"
    ziel = ROOT / "tests" / "reports" / name
    ziel.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        seite = browser.new_page(viewport={"width": 1240, "height": 900})
        seite.goto(f"{BASE}/{rel}", wait_until="networkidle")
        if level:
            # Die Engine liest 'spirale-<THEMA_KEY>' und ergaenzt fehlende Felder
            # aus DEFAULT_STATE - level allein reicht, damit initApp() nach dem
            # Reload direkt eine Aufgabe dieses Levels rendert (kein Startbildschirm).
            key = seite.evaluate("typeof THEMA_KEY !== 'undefined' ? THEMA_KEY : null")
            if not key:
                raise SystemExit(f"{rel}: kein THEMA_KEY - ist das ein Trainer?")
            seite.evaluate(
                "([k, l]) => localStorage.setItem('spirale-' + k, JSON.stringify({level: l}))",
                [key, level])
            seite.reload(wait_until="networkidle")
        _katex_abwarten(seite)
        seite.screenshot(path=str(ziel), full_page=True)
        browser.close()
    return ziel


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        raise SystemExit(__doc__)
    lvl = int(args[args.index("--level") + 1]) if "--level" in args else None
    print(bild(args[0], lvl))
