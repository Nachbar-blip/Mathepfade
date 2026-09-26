"""Struktur-Tests fuer index.html: Klassenzuordnung (Thueringer Lehrplan) und gA/eA-Benennung."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = (ROOT / "index.html").read_text(encoding="utf-8")


def spalten():
    """{dateiname: klasse} aus den .col-N-Bloecken von index.html."""
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
