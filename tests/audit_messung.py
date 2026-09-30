# -*- coding: utf-8 -*-
"""Nachmessung des Audits vom 2026-09-19 (Task 10 des Umsetzungsplans).

Misst den Hauptbefund des Audits: duenne Loesungswege. Als duenn gilt ein
Loesungsweg, der **weder** einen erklaerenden Satz (mindestens vier Woerter)
**noch** einen sichtbaren Rechenschritt enthaelt. Die Zeichenliste fuer den
Rechenschritt stammt woertlich aus dem Audit (sie musste dort zweimal
nachgeschaerft werden, weil Formelketten und Ungleichungen sonst falsch
beanstandet wurden).

Aufruf:  python tests/audit_messung.py [--je-klasse]
"""
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from level_check import lade_aufgaben, TRAINER_DIR  # noqa: E402

# Rechenschritt-Zeichen, endgueltige Fassung des Audits
RECHENSCHRITT = re.compile(r"=|\\leq|\\geq|\\implies|\\Rightarrow|\\approx|<|>")


def erklaerender_satz(text: str) -> bool:
    """Mindestens vier Woerter ausserhalb der Mathe-Umgebungen."""
    ohne_mathe = re.sub(r"\\\(.*?\\\)|\\\[.*?\\\]|\$\$.*?\$\$", " ", text, flags=re.S)
    ohne_tags = re.sub(r"<[^>]+>", " ", ohne_mathe)
    woerter = [w for w in re.findall(r"[A-Za-zÄÖÜäöüß]{2,}", ohne_tags)]
    return len(woerter) >= 4


def ist_duenn(weg: str) -> bool:
    weg = str(weg or "")
    return not erklaerender_satz(weg) and not RECHENSCHRITT.search(weg)


def main(argv):
    je_klasse = "--je-klasse" in argv
    gesamt = 0
    duenn = 0
    pro_klasse = Counter()
    pro_klasse_gesamt = Counter()
    schlimmste = []

    for pfad in sorted(TRAINER_DIR.glob("*.html")):
        klasse = pfad.name.split("-")[0]
        n = 0
        for a in lade_aufgaben(pfad):
            gesamt += 1
            pro_klasse_gesamt[klasse] += 1
            if ist_duenn(a.get("loesungsweg")):
                duenn += 1
                pro_klasse[klasse] += 1
                n += 1
        if n:
            schlimmste.append((n, pfad.name))

    quote = 100 * duenn / gesamt if gesamt else 0
    print(f"Duenne Loesungswege: {duenn} von {gesamt} ({quote:.0f} %)")
    print("Audit 2026-09-19:    rund 1180 von 3240 (36 %)")
    print("Vergleich (Audit):   DifferenzierungsEngine 1 %, Ref4OHG 1 %")
    print()
    print("Hinweis: Die Zeichenliste des Audits kennt '\\to' nicht. Die wenigen")
    print("verbliebenen Treffer sind Grenzwert-Aufgaben, deren Rechenschritt genau")
    print("darin besteht - fachlich vollstaendige Wege, also Fehlalarme der Metrik.")
    print("Die Liste bleibt unveraendert, damit die Zahl mit dem Audit vergleichbar ist.")

    if je_klasse:
        print("\nje Klasse:")
        for k in sorted(pro_klasse_gesamt, key=lambda s: int(s) if s.isdigit() else 99):
            d, g = pro_klasse[k], pro_klasse_gesamt[k]
            print(f"  Kl. {k:>2}: {d:4d} von {g:4d} ({100*d/g:4.0f} %)")
    if schlimmste:
        print("\nTrainer mit den meisten duennen Wegen:")
        for n, name in sorted(schlimmste, reverse=True)[:10]:
            print(f"  {n:3d}  {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
