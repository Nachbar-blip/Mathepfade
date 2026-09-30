"""Gate fuer die Level-Rubrik der DifferenzierungsEngine (Plan 2026-09-17, Schritt 1).

Prueft Trainer-HTMLs ohne Browser auf Verstoesse gegen die Level-Rubrik:
Formel-/Rechenweg-Ansage ab Level 4, MC-Lastigkeit in Level 5/6, ratbare MC,
fehlende Toleranz, Duplikate ueber Trainer hinweg, trivialisierende Stellen.

Aufruf:
    python tests/level_check.py                      # alle Trainer, nur Bericht
    python tests/level_check.py --strict trainer/10-exp-funktionen.html ...
                                                     # Exit 1 bei hartem Verstoss

Die AUFGABEN-Arrays werden per node ausgewertet (echtes JS, kein JSON).
"""

import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRAINER_DIR = ROOT / "trainer"

# Harte Regeln (Rubrik "Verboten"):
FORMEL_ANSAGE = re.compile(
    r"\(Formel|Formel:|Modell:|Verwende\s|Nutze\s|Hinweis:\s*(zuerst|erst)|Tipp:", re.I)
RECHENART_ANSAGE = re.compile(
    r"^\s*(Addiere|Subtrahiere|Multipliziere|Dividiere|Kuerze|Kürze|Erweitere)\b", re.I)
NULL_AUSWERTUNG = re.compile(r"f'\(0\)|f\\'\(0\)|an der Stelle\s*(x\s*=\s*)?0\b", re.I)
# Die Engine rendert kein Markdown: **fett** erscheint woertlich (Sichtpruefung 2026-09-18).
MARKDOWN_FETT = re.compile(r"\*\*[^*\r\n]+\*\*")
# Trainer, in denen die Auswertung bei x = 0 die Regel trivialisiert (je ein Summand faellt weg).
# Befund 2026-09-30: Das Muster hing an "ableitungsregeln|kettenregel" und verfehlte damit
# 11-ableitung-ketten-produkt — genau den Trainer mit 14 solchen Aufgaben.
KETTEN_TRAINER = re.compile(r"ableitung|kettenregel")
# KaTeX-Befehlswoerter, die nach dem JS-Auswerten ohne Backslash dastehen (=> im Quelltext stand "\cdot").
KATEX_OHNE_BACKSLASH = re.compile(
    r"(?<![A-Za-z\\])(cdot|frac|tfrac|dfrac|sqrt|times|Rightarrow|implies|approx|neq|leq|geq|"
    r"ldots|infty|overline|mathbb|quad|left\(|right\))(?![A-Za-z])")
# Mathe-Umgebungen: was hier drin steht, rendert KaTeX. Alles ausserhalb erscheint woertlich.
MATHE_UMGEBUNG = re.compile(r"\\\(.*?\\\)|\\\[.*?\\\]|\$\$.*?\$\$", re.S)
# Markup, das nur innerhalb einer Mathe-Umgebung etwas bedeutet (Dezimalkomma, Befehl, Index/Exponent).
MATHE_MARKUP = re.compile(r"\{,\}|\\[a-zA-Z]{2,}|\^\{|_\{")


def mathe_markup_ausserhalb(a: dict) -> list:
    """Felder, die KaTeX-Markup ausserhalb von \\(...\\)/$$...$$ tragen — das rendert woertlich.
    Befund 2026-09-30 (Review Kl. 10 Block C): MC-Option '0{,}5' stand im Klartext und war
    im Browser als '0{,}5' zu lesen; katex_check rendert nicht, was ausserhalb der Umgebung
    steht, und level_check kannte nur fehlende Backslaesche. Nur die Sichtpruefung fand es."""
    felder = [(f, str(a.get(f) or "")) for f in ("frage", "tipp", "loesungsweg")]
    felder += [(f"optionen[{i}]", str(o)) for i, o in enumerate(a.get("optionen") or [])]
    return [f for f, text in felder if MATHE_MARKUP.search(MATHE_UMGEBUNG.sub(" ", text))]


# Auszeichnung, die die Engine bewusst rendern soll (CLAUDE.md: Fettdruck als <b>…</b>).
ERLAUBTE_TAGS = re.compile(r"</?(b|i|br|sub|sup|em|strong)\s*/?>", re.I)
# '<' unmittelbar vor Buchstabe oder '/' startet fuer den HTML-Parser ein Tag.
# '< ' und '<0' sind harmlos: dort liest der Parser Text.
TAG_START = re.compile(r"<[a-zA-Z/]")


def html_frisst_text(a: dict) -> list:
    """Felder, in denen '<' direkt vor einem Buchstaben steht — die Engine setzt diese Felder
    per innerHTML, der HTML-Parser haelt das fuer einen Tag-Anfang und verschluckt den Text bis
    zum naechsten '>'. Befund 2026-09-30 (Review Kl. 11 Block A2): In zwei Traineren fehlte im
    Bild dadurch die Fallunterscheidung, die den Kern der Aufgabe ausmachte. level_check sah es
    nicht (gueltiger String), katex_check auch nicht (er rendert, was uebrig bleibt).
    Abhilfe im Text: Leerzeichen setzen (\\(1 < x < 5\\)) oder \\lt benutzen."""
    felder = [(f, str(a.get(f) or "")) for f in ("frage", "tipp", "loesungsweg")]
    felder += [(f"optionen[{i}]", str(o)) for i, o in enumerate(a.get("optionen") or [])]
    return [f for f, text in felder if TAG_START.search(ERLAUBTE_TAGS.sub(" ", text))]


# Verweis auf eine MC-Option ueber ihren Buchstaben. Die Engine mischt die Reihenfolge,
# der Buchstabe zeigt im Bild also auf etwas anderes als im Quelltext.
OPTIONS_VERWEIS = re.compile(
    r"(?:Option|Antwort|Auswahl|Variante|Wahl|Aussage)\s+[A-D]\b"
    r"|(?:^|[.;:!?]\s+)[A-D]\)\s")


def optionsbuchstabe(a: dict) -> list:
    """Felder einer MC-Aufgabe, die eine Option ueber ihren Buchstaben ansprechen.
    Befund 2026-09-30 (Welle Kl. 11): Zwei Renderings derselben Aufgabe zeigten die Optionen
    in verschiedener Reihenfolge - ein Loesungsweg mit 'Option B' weist damit auf die falsche.
    Im Quelltext ist der Fehler nicht zu sehen, nur im Bild. Richtig ist, die Option ueber
    ihren Inhalt zu benennen (den Term, den Wert, die Aussage)."""
    if a.get("typ") != "mc":
        return []
    felder = [(f, str(a.get(f) or "")) for f in ("frage", "tipp", "loesungsweg")]
    return [f for f, text in felder if OPTIONS_VERWEIS.search(MATHE_UMGEBUNG.sub(" ", text))]


def lade_aufgaben(pfad: Path) -> list:
    js = r"""
const fs=require('fs');const h=fs.readFileSync(process.argv[1],'utf8');
const blocks=h.match(/<script>([\s\S]*?)<\/script>/g)||[];
for(const b of blocks){const code=b.replace(/<\/?script>/g,'');
  if(!/AUFGABEN/.test(code))continue;
  const fn=new Function(code+';return AUFGABEN;');
  process.stdout.write(JSON.stringify(fn()));process.exit(0);}
process.exit(2);
"""
    r = subprocess.run(["node", "-e", js, str(pfad)], capture_output=True, text=True,
                       encoding="utf-8")
    if r.returncode != 0:
        raise RuntimeError(f"{pfad.name}: AUFGABEN nicht auswertbar: {r.stderr.strip()[:200]}")
    return json.loads(r.stdout)


def tipp_verraet_loesung(tipp: str, loesung) -> bool:
    """Warnung, wenn der Loesungswert (ab Betrag 10, sonst zu viele Zufallstreffer) im Tipp steht.
    Review-Befund 2026-09-26: Tipps wie '30000 cm³ = 30 l' nehmen die Antwort vorweg."""
    x = float(loesung)
    if abs(x) < 10:
        return False
    kompakt = re.sub(r"\\[,;]|\s|\{,\}", lambda m: "," if m.group(0) == "{,}" else "", tipp or "")
    formen = {str(x).replace(".", ",")}
    if x == int(x):
        formen.add(str(int(x)))
    return any(re.search(r"(?<![\d,.])" + re.escape(z) + r"(?![\d])", kompakt) for z in formen)


def richtige_option_zu_lang(optionen: list, korrekt: int) -> bool:
    """True, wenn die richtige Option laenger ist als jede andere und mehr als 1,3-mal so lang
    wie die laengste Ablenker-Option (gemessen am sichtbaren Text ohne KaTeX-Steuerzeichen)."""
    def sichtbar(s):
        return len(re.sub(r"\\[a-zA-Z]+|[\\{}$()]", "", str(s)))
    laengen = [sichtbar(o) for o in optionen]
    r = laengen[korrekt]
    andere = [l for i, l in enumerate(laengen) if i != korrekt]
    return bool(andere) and r > max(andere) * 1.3


def normalisiere(frage: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", frage)).strip().lower()


def pruefe_trainer(pfad: Path, aufgaben: list):
    """Liefert (harte_fehler, warnungen) als Listen von Strings."""
    hart, warn = [], []
    name = pfad.name

    if len(aufgaben) != 36:
        hart.append(f"{len(aufgaben)} statt 36 Aufgaben")
    ids = [a.get("id") for a in aufgaben]
    if any(not isinstance(i, int) for i in ids):
        hart.append("id nicht ueberall Number")
    if len(set(ids)) != len(ids):
        hart.append("doppelte ids")
    je_level = Counter(a.get("level") for a in aufgaben)
    for lv in range(1, 7):
        if je_level[lv] != 6:
            hart.append(f"Level {lv}: {je_level[lv]} statt 6 Aufgaben")

    for a in aufgaben:
        k = f"#{a.get('id')} L{a.get('level')}"
        frage = a.get("frage", "")
        lv = a.get("level", 0)
        typ = a.get("typ")
        if typ == "mc":
            opt = a.get("optionen") or []
            if not (2 <= len(opt) <= 4) or not (0 <= a.get("korrekt", -1) < len(opt)):
                hart.append(f"{k}: MC-Optionen/korrekt ungueltig")
            elif len(set(opt)) < len(opt):
                hart.append(f"{k}: identische MC-Optionen")
            elif lv >= 4 and richtige_option_zu_lang(opt, a["korrekt"]):
                # Review 2026-09-26: in 31 von 35 MC war die richtige Option die laengste (Begruendung
                # nur dort). Die Laenge darf die Antwort nicht verraten.
                warn.append(f"{k}: richtige MC-Option deutlich laenger als die Distraktoren")
        elif typ == "numerisch":
            loes = a.get("loesung")
            if not isinstance(loes, (int, float)):
                hart.append(f"{k}: loesung fehlt")
            elif float(loes) != int(loes) and not a.get("toleranz"):
                hart.append(f"{k}: Dezimal-Loesung ohne toleranz")
            elif tipp_verraet_loesung(a.get("tipp", ""), loes):
                warn.append(f"{k}: Tipp enthaelt den Loesungswert {loes}")
        else:
            hart.append(f"{k}: typ ungueltig ({typ})")

        for feld in ("frage", "tipp", "loesungsweg"):
            if MARKDOWN_FETT.search(a.get(feld) or ""):
                hart.append(f"{k}: Markdown-Sternchen in '{feld}' (bitte <b>…</b>)")
        # Einfacher Backslash im JS-String frisst den KaTeX-Befehl: "\cdot" -> "cdot".
        # Sichtbar erst im Browser, katex_check meldet es nicht (Befund 2026-09-26, 7-binomische #16/#18).
        for feld in ("frage", "tipp", "loesungsweg"):
            texte = [a.get(feld) or ""]
            if feld == "frage":
                texte += list(a.get("optionen") or [])
            for t in texte:
                if KATEX_OHNE_BACKSLASH.search(t):
                    hart.append(f"{k}: KaTeX-Befehl ohne Backslash in '{feld}' "
                                f"(einfacher statt doppelter Backslash im JS-String)")
                    break
        for feld in optionsbuchstabe(a):
            hart.append(f"{k}: MC-Option ueber ihren Buchstaben angesprochen in '{feld}' "
                        f"(die Engine mischt die Reihenfolge; Option ueber den Inhalt benennen)")
        for feld in html_frisst_text(a):
            hart.append(f"{k}: '<' direkt vor Buchstabe in '{feld}' "
                        f"(innerHTML frisst den Text bis '>'; Leerzeichen setzen oder \\lt)")
        for feld in mathe_markup_ausserhalb(a):
            hart.append(f"{k}: Mathe-Markup ausserhalb von \\(…\\) in '{feld}' "
                        f"(rendert woertlich, z. B. '0{{,}}5')")

        if lv >= 4 and FORMEL_ANSAGE.search(frage):
            hart.append(f"{k}: Formel-/Rechenweg-Ansage in Level >= 4")
        if lv >= 4 and RECHENART_ANSAGE.search(normalisiere(frage)):
            warn.append(f"{k}: Rechenart wird angesagt (Level >= 4)")
        if KETTEN_TRAINER.search(name) and lv >= 4 and NULL_AUSWERTUNG.search(frage):
            warn.append(f"{k}: Auswertung an x = 0 trivialisiert Produkt-/Kettenregel")

    for lv in (5, 6):
        mc = sum(1 for a in aufgaben if a.get("level") == lv and a.get("typ") == "mc")
        if mc > 3:
            hart.append(f"Level {lv}: {mc}/6 MC (max. 3 erlaubt)")

    # Level 1 einer Datei vs. Level >= 4 derselben Datei: gleiche Frage -> Inversion
    fragen = {}
    for a in aufgaben:
        fragen.setdefault(normalisiere(a.get("frage", "")), []).append(a)
    for f, gruppe in fragen.items():
        if len(gruppe) > 1:
            hart.append("identische Frage: " + ", ".join(f"#{a['id']}" for a in gruppe))
    return hart, warn


def main(argv):
    strict = "--strict" in argv
    dateien = [Path(x) for x in argv if x.endswith(".html")]
    if not dateien:
        dateien = sorted(TRAINER_DIR.glob("*.html"))
    dateien = [d if d.is_absolute() else ROOT / d for d in dateien]

    alle = {}
    for d in dateien:
        alle[d] = lade_aufgaben(d)

    # Duplikate ueber Trainer hinweg (gegen den gesamten Pool, nicht nur die Auswahl)
    pool = {}
    for d in sorted(TRAINER_DIR.glob("*.html")):
        aufg = alle.get(d) or lade_aufgaben(d)
        for a in aufg:
            pool.setdefault(normalisiere(a.get("frage", "")), []).append((d.name, a["id"], a["level"]))

    exit_code = 0
    for d, aufg in alle.items():
        hart, warn = pruefe_trainer(d, aufg)
        for a in aufg:
            treffer = [t for t in pool.get(normalisiere(a.get("frage", "")), []) if t[0] != d.name]
            if treffer:
                warn.append(f"#{a['id']} L{a['level']}: identisch mit "
                            + ", ".join(f"{t[0]} #{t[1]} L{t[2]}" for t in treffer))
        status = "FEHLER" if hart else ("WARNUNG" if warn else "ok")
        print(f"== {d.name}: {status}")
        for h in hart:
            print(f"   FEHLER  {h}")
        for w in warn:
            print(f"   warn    {w}")
        if hart and strict:
            exit_code = 1
    return exit_code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
