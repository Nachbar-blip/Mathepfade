# -*- coding: utf-8 -*-
"""Lehrplan-Gate Thueringen (Gymnasium 2018): meldet Begriffe, die in der Klassenspalte
laut TH-Lehrplan nicht vorkommen duerfen. Klassenzuordnung wird aus index.html gelesen
(Kapitel 2.2 = Kl. 7/8, 2.3 = Kl. 9/10, 4 = Qualifikationsphase 11/12).

Aufruf:  python tests/lehrplan_check.py [--strict] [trainer/x.html ...]
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from level_check import lade_aufgaben, normalisiere, ROOT, TRAINER_DIR  # noqa: E402

INDEX = ROOT / "index.html"

# Vektoren/Determinanten erst in der Qualifikationsphase (TH Kap. 4, Analytische Geometrie)
_SI_VEKTOR = {"vektor", "determinante", "skalarprodukt"}
# In keiner Klassenstufe des TH-Lehrplans
_KEIN_TH = {"polynomdivision", "hypothesentest", "signifikanzniveau", "nullhypothese",
            "newton-verfahren", "newtonverfahren", "differenzialgleichung", "differentialgleichung",
            "übergangsmatrix", "uneigentlich"}
VERBOTEN = {
    7: _SI_VEKTOR | _KEIN_TH | {"logarithm", "sinus", "kosinus", "ableitung"},
    8: _SI_VEKTOR | _KEIN_TH | {"logarithm", "ableitung"},
    9: _SI_VEKTOR | _KEIN_TH | {"ableitung", "integral"},
    10: _SI_VEKTOR | _KEIN_TH | {"integral"},
    11: _KEIN_TH,
    12: _KEIN_TH,
}
AUSNAHMEN = {9: {"sinus", "kosinus"}}   # 9-trig-* (TH 2.3.3 Trigonometrie)
FELDER = ("frage", "loesungsweg", "tipp")


def klassen_aus_index() -> dict:
    """{dateiname: klasse} aus den .col-N-Bloecken von index.html."""
    html = INDEX.read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r'<div class="col col-(\d+)">(.*?)(?=<div class="col col-|</div>\s*<!-- /grid|\Z)',
                         html, re.S):
        klasse = int(m.group(1))
        for h in re.findall(r'href="trainer/([^"]+\.html)"', m.group(2)):
            out[h] = klasse
    return out


def _muster(klasse: int) -> re.Pattern:
    # Wortanfang muss stimmen (kein "Integralzeichen"-Problem im Wortinneren), Endung frei:
    # "vektor" trifft "Vektoren", "ableitung" trifft "Ableitungen".
    verboten = VERBOTEN.get(klasse, set()) - AUSNAHMEN.get(klasse, set())
    return re.compile(r"(?<![a-zäöüß])(" + "|".join(map(re.escape, sorted(verboten))) + ")")


def pruefe(klasse: int, name: str, aufgaben: list) -> list:
    muster = _muster(klasse)
    treffer = []
    for a in aufgaben:
        text = normalisiere(" ".join(str(a.get(k) or "") for k in FELDER)
                            + " " + " ".join(a.get("optionen") or []))
        m = muster.search(text)
        if m:
            treffer.append(f"{name} #{a['id']} L{a['level']}: '{m.group(1)}' "
                           f"(Kl. {klasse} nicht im TH-Lehrplan)")
    return treffer


def main(argv):
    strict = "--strict" in argv
    dateien = [Path(x) for x in argv if x.endswith(".html")] or sorted(TRAINER_DIR.glob("*.html"))
    dateien = [d if d.is_absolute() else ROOT / d for d in dateien]
    klassen = klassen_aus_index()

    befunde = []
    for d in dateien:
        if d.name not in klassen:
            befunde.append(f"{d.name}: nicht in index.html eingeordnet")
            continue
        befunde += pruefe(klassen[d.name], d.name, lade_aufgaben(d))
    for b in befunde:
        print(f"FEHLER  {b}")
    print(f"== Lehrplan-Gate: {len(befunde)} Befunde in {len(dateien)} Trainern")
    return 1 if (befunde and strict) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
