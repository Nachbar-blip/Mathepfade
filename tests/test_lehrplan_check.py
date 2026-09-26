# -*- coding: utf-8 -*-
"""Tests fuer das Lehrplan-Gate Thueringen (tests/lehrplan_check.py)."""
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
