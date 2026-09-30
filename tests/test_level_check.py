# -*- coding: utf-8 -*-
"""Tests fuer das Level-Gate (tests/level_check.py).

Befund 2026-09-30 (Review Kl. 10 Block C): In 10-stoch-mehrstufig stand die MC-Option
"0{,}5" ausserhalb einer Mathe-Umgebung und wurde im Browser woertlich angezeigt.
Kein Gate sah das: level_check kannte nur fehlende Backslaesche, katex_check rendert
gar nicht, was ausserhalb von \\(...\\) steht. Nur die Sichtpruefung fand es.
"""
import level_check as lk


def _aufgabe(**kw):
    a = {"id": 1, "level": 1, "typ": "numerisch", "frage": "Berechne 2 + 3.",
         "loesung": 5, "toleranz": 0.1, "tipp": "Zaehle zusammen.", "loesungsweg": "2 + 3 = 5"}
    a.update(kw)
    return a


def test_mathe_markup_ausserhalb_der_umgebung_ist_hart():
    """0{,}5 im Klartext rendert woertlich — harter Fehler."""
    hart = lk.mathe_markup_ausserhalb(_aufgabe(frage="Die Wahrscheinlichkeit ist 0{,}5."))
    assert hart == ["frage"]


def test_markup_innerhalb_der_umgebung_ist_erlaubt():
    """Dasselbe Markup innerhalb von \\(...\\) und $$...$$ ist korrekt."""
    assert lk.mathe_markup_ausserhalb(_aufgabe(frage="Es gilt \\(p = 0{,}5\\).")) == []
    assert lk.mathe_markup_ausserhalb(_aufgabe(loesungsweg="$$p = 0{,}5$$ also die Haelfte.")) == []


def test_befehl_ausserhalb_der_umgebung_ist_hart():
    """Auch ein KaTeX-Befehl ausserhalb der Umgebung rendert woertlich."""
    assert lk.mathe_markup_ausserhalb(_aufgabe(tipp="Nimm \\sqrt{2} als Faktor.")) == ["tipp"]


def test_mc_optionen_werden_mitgeprueft():
    """Der Befund lag in einer MC-Option, nicht im Aufgabentext."""
    a = _aufgabe(typ="mc", optionen=["0", "0{,}5", "1", "je nach Experiment"], korrekt=2)
    assert lk.mathe_markup_ausserhalb(a) == ["optionen[1]"]


def test_normaler_text_bleibt_still():
    """Dezimalkomma als echtes Komma und Prozentzeichen loesen nichts aus."""
    a = _aufgabe(frage="Die Quote betraegt 0,5 bzw. 50 %.", loesungsweg="Haelfte von 1 ist 0,5.")
    assert lk.mathe_markup_ausserhalb(a) == []


def test_gate_meldet_den_befund_als_harten_fehler():
    """Der Check haengt im Gate und landet in der Fehlerliste, nicht in den Warnungen."""
    from pathlib import Path
    aufgaben = [_aufgabe(id=i, level=(i - 1) // 6 + 1) for i in range(1, 37)]
    aufgaben[3]["frage"] = "Die Summe ist 0{,}5."
    hart, warn = lk.pruefe_trainer(Path("x.html"), aufgaben)
    assert any("Mathe-Markup ausserhalb" in f and "#4" in f for f in hart)
