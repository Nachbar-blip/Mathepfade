# Klasse 11, Block B (eA) — Kriterien je Trainer (Welle Task 8, Stand 2026-09-30)

Lokale Nachvollziehbarkeit; im Public-HTML stehen die Kriterien bewusst nicht.
Grundlage: Rubrik aus `2026-09-26-lehrplan-th-und-level-progression-plan.md`,
Befunde aus `../audit/audit-2026-09-19-mathepfade.md` (Zeilen 108–122),
Muster der Einträge: `2026-09-26-kl10-kriterien.md`.

Lesart Kl. 11 eA durchgängig: L4 = Verfahren selbst wählen / Modell aus Text /
Umkehraufgabe (Parameter gesucht); L5 = zwei Verfahren verbinden, Parameter aus
zwei Bedingungen, Fehler in vorgelegter Rechnung; **L6 = Abi-Format eA** —
mehrschrittig, mit Begründungs- und Beweisanteil („Zeigen Sie…", „Beurteilen Sie…"),
Fallunterscheidung nach Parameter, Grenzfall.

Jede Lösung mit dem Wolfram-MCP nachgerechnet; Bilder der geänderten Stufen per
`tests/bild.py` erzeugt **und angesehen**.

| Trainer | Audit-Befund | Geändert |
|---|---|---|
| 11-lk-funktionsscharen | KEIN_AFB3 L5 und L6; KOLLAPS L2/L3; DUENNER_WEG (1–5); Warnung #16 (Tipp mit Lösungswert) | L5/L6 neu (12 Aufgaben); Tipp #16 ohne Lösungswert; dünne Lösungswege in #1, #8, #10, #14, #15, #22 ausgebaut |
| 11-lk-gebrochen-rational | KEIN_AFB3 L5 und L6; DUENNER_WEG (alle Stufen); **Lehrplan-Gate: #13/#14 „Polynomdivision"**; Warnung #29 (MC-Länge) | L5/L6 neu (12 Aufgaben); #13/#14/#15 ohne Polynomdivision neu gefasst (Gradvergleich, Grenzwert, Abspalten); dünne Lösungswege in #7, #11, #22, #23 ausgebaut; **hebbare Lücke aus der Kl.-10-Welle hier eingebaut** |
| 11-lk-kurvendisk-erweitert | KEIN_AFB3 L5 und L6; **KOLLAPS L3/L4**; KURZ (1,2,3,5,6); DUENNER_WEG (alle Stufen) | L4, L5 und L6 neu (18 Aufgaben) — Stufe 4 wegen des Kollapses; dünne Lösungswege in #13/#14 ausgebaut, Rückverweise in #17/#18 durch den Funktionsterm ersetzt |
| 11-lk-newton (Dateiname historisch) | Ersatz-Trainer; Lehrplan-Gate: „Newton-Verfahren" in #2 und #29 | **Alle 36 Aufgaben neu: Thema ln-Funktion (eA)**, TH 4.1. `<title>`, `THEMA_CONFIG.name = 'ln-Funktion (eA)'`, Index-Zeilentext „ln-Funktion" und Kommentar in Zeile 2 der Datei geändert; `THEMA_KEY` unverändert (Schülerfortschritt) |

Abgrenzung der vier Trainer gegeneinander und gegen die gA-Trainer der Kl. 11:
**Funktionsscharen** = Parameterscharen (Ortskurve, gemeinsame Punkte, Diskussion in
Abhängigkeit vom Parameter); **gebrochen-rational** = Definitionslücken, Polstellen,
hebbare Lücken, Asymptoten; **kurvendisk-erweitert** = zusammengesetzte Funktionen mit
e- und trigonometrischen Termen (Produkt-/Kettenregel in der Diskussion);
**ln-Funktion** = Logarithmus als Umkehrfunktion, Ableitung, Stammfunktion von \(1/x\).
Gegen `11-e-funktion` und `11-e-funktion-ableitung` wurde beim Schreiben abgeglichen
(siehe Abschnitt „Beim Schreiben vermiedene Dubletten").

---

## 11-lk-newton → ln-Funktion (eA), Ersatz-Trainer

Levelaufbau nach der Vorgabe aus Task 8. Vorlage für den Zuschnitt:
`../DifferenzierungsEngine/trainer/12-lk-analysis-ln-substitution.html`, nur der ln-Teil.
Nach der Umstellung kommt das Wort „Newton-Verfahren" in der Datei nicht mehr vor.

| id | Level | Kriterium |
|---|---|---|
| 1 | 1 | \(\ln e\) über die Definition des Exponenten |
| 2 | 1 | \(\ln(1/e)\) — negativer Logarithmuswert |
| 3 | 1 | Umkehrung: \(e^{x}=5\) nach \(x\) |
| 4 | 1 | Definitionsbereich (MC), begründet über den Wertebereich von \(e^{x}\) |
| 5 | 1 | \(\ln(e^{4})\) — Aufhebung der beiden Funktionen |
| 6 | 1 | \(\ln\sqrt{e}\) — gebrochener Exponent |
| 7 | 2 | Ableitung von \(\ln x\) an einer Stelle |
| 8 | 2 | Ableitung von \(a\ln x\) |
| 9 | 2 | Ableitung einer Summe \(\ln x + x^{2}\) |
| 10 | 2 | Tangentenanstieg an vorgegebener Stelle |
| 11 | 2 | Ableitung von \(5\ln x\) (MC, Distraktor \(\frac{1}{5x}\)) |
| 12 | 2 | zwei Schritte: Nullstelle bestimmen, dort Ableitung |
| 13 | 3 | Kettenregel \(\ln(2x+1)\) |
| 14 | 3 | Stammfunktion von \(1/x\) (MC, Potenzregel scheitert) |
| 15 | 3 | \(\int_1^e \frac1x\,dx\) |
| 16 | 3 | \(\int_1^e \frac3x\,dx\) — Faktor vorziehen, \(3\ln x\) statt \(\ln(3x)\) |
| 17 | 3 | Kettenregel \(\ln(x^{2}+1)\) |
| 18 | 3 | Produktregel \(x\ln x\) |
| 19 | 4 | \(\ln x = 2-x\) CAS-frei einschätzen — Intervall der Lösung |
| 20 | 4 | Umkehraufgabe — Stelle aus vorgegebenem Funktionswert |
| 21 | 4 | Flächeninhalt unter \(1/x\), Verfahren nicht genannt |
| 22 | 4 | Umkehraufgabe — Stelle aus vorgegebener Steigung |
| 23 | 4 | Modell aus Text — Verdoppelungszeit, Anfangswert kürzt sich |
| 24 | 4 | Umkehraufgabe — Scharparameter aus der Nullstelle |
| 25 | 5 | Parameter aus Integralbedingung \(\int_1^a \frac1x\,dx = 2\) |
| 26 | 5 | Fehler finden (MC) — \(\ln(a+b) = \ln a + \ln b\) in vorgelegtem Weg; Probe entlarvt das Ergebnis |
| 27 | 5 | Extremum von \(x\ln x\) mit Artbestimmung über \(f''\) |
| 28 | 5 | zwei Schritte — Extremstelle und Extremwert von \(\ln x - \frac{x}{2}\) |
| 29 | 5 | Parameter aus zwei Bedingungen \(f(1)=3\), \(f(e)=7\) |
| 30 | 5 | zwei Verfahren — Tangente durch den Ursprung, Logarithmusgleichung |
| 31 | 6 | Behauptung begründet prüfen (MC): \(\ln x < \sqrt{x}\) über das Minimum der Differenz |
| 32 | 6 | Schar \(\ln(kx)\) (MC): Verschiebung in \(y\)-Richtung über das Produktgesetz |
| 33 | 6 | Schar: Steigung an der eigenen Nullstelle ist gleich \(k\) |
| 34 | 6 | Abi eA: „Zeigen Sie" — genau eine Extremstelle der Schar \(x - a\ln x\), dann Wert für \(a=6\) |
| 35 | 6 | Grenzfall: größte ganze Zahl \(b\) mit \(\ln b < 1\) |
| 36 | 6 | Abi eA: Schnittpunkt der Tangenten an \(e^{x}\) und \(\ln x\) bei \(x=1\) |

## 11-lk-funktionsscharen

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | Ortskurve der Tiefpunkte, Parameter eliminieren, Wert an einer Stelle |
| 26 | 5 | Fehler finden (MC): Ortskurve enthält noch den Parameter; richtig \(y=-2x^{3}\) |
| 27 | 5 | Parameter aus zwei Bedingungen — waagerechte Tangente und \(y\)-Achsenabschnitt |
| 28 | 5 | gemeinsamer Punkt: Term nach dem Parameter sortieren |
| 29 | 5 | Extremwert der Schar \(x e^{-kx}\) gleich \(2\) — Parameter gesucht |
| 30 | 5 | Flächeninhalt in Abhängigkeit vom Parameter, Bedingung \(A=4\) |
| 31 | 6 | Behauptung prüfen (MC): je zwei Graphen schneiden einander genau einmal |
| 32 | 6 | Berührbedingung über die Diskriminante |
| 33 | 6 | Abi eA: „Zeigen Sie" — Wendestelle unabhängig vom Parameter, dann Wert für \(a=5\) |
| 34 | 6 | Fallunterscheidung nach dem Parameter: genau eine Nullstelle; **Grenzfall \(a=0\)** gehört dazu |
| 35 | 6 | Abi eA: Tiefpunkt-Nachweis für die ganze Schar, kleinste ganze Zahl über der \(x\)-Achse; **Grenzfall \(t=0\)** liegt auf der Achse |
| 36 | 6 | Abi eA: Berührung der \(x\)-Achse nachweisen (zwei Bedingungen), dritte Nullstelle über die Zerlegung |

Stufe 1–3 wurden nicht neu geschrieben (KOLLAPS L2/L3 bleibt laut Plan offen);
geändert wurden dort nur Tipps und Lösungswege.

## 11-lk-gebrochen-rational

| id | Level | Kriterium |
|---|---|---|
| 13 | 3 | Pflicht-Fix: schiefe Asymptote über den **Gradvergleich**, nicht über Polynomdivision |
| 14 | 3 | Pflicht-Fix: Näherungsgerade über Abspalten \(x^{2}=(x-1)(x+1)+1\), Verfahren nicht benannt |
| 15 | 3 | \(y\)-Achsenabschnitt der Näherungsgeraden, Abgrenzung gegen \(f(0)\) |
| 25 | 5 | Parameter so, dass die Polstelle entfällt — hebbare Lücke entsteht |
| 26 | 5 | Wert an der hebbaren Lücke von \(\frac{x^{3}-8}{x-2}\) über die Zerlegung |
| 27 | 5 | Fehler finden (MC): „jede Nennernullstelle ist eine Polstelle" |
| 28 | 5 | Parameter aus zwei Bedingungen — Asymptote und \(y\)-Achsenabschnitt |
| 29 | 5 | drei Schritte: umformen, Extremstelle, Art und Wert |
| 30 | 5 | Schnittstelle mit einer Geraden, Definitionsbereich prüfen (Scheinlösung) |
| 31 | 6 | Behauptung prüfen (MC): gemeinsame Nullstelle ⇒ hebbare Lücke? Gegenbeispiel \(\frac{x-1}{(x-1)^{2}}\) |
| 32 | 6 | Fallunterscheidung nach dem Zählergrad über fünf Exponenten |
| 33 | 6 | Abi eA: Schar \(\frac{x}{x^{2}-k}\), Polstellen je nach \(k\); **Grenzfall \(k=0\)** wird gekürzt |
| 34 | 6 | Abi eA: Gerade mit Lücke nachweisen, Nullstelle angeben (aus Kl. 10 verschoben) |
| 35 | 6 | keine Polstelle — Nenner ohne reelle Nullstelle (Diskriminante, quadratische Ergänzung) |
| 36 | 6 | Abi eA: beide Asymptoten der Schar nachweisen, Parameter aus ihrem Schnittpunkt |

## 11-lk-kurvendisk-erweitert

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | Produktregel bei \((x-2)e^{x}\), Exponentialterm ausklammern |
| 20 | 4 | Anzahl der Stellen mit waagerechter Tangente bei \(x^{2}e^{x}\) |
| 21 | 4 | Kettenregel bei \(\sin(2x)\), Hoch- gegen Tiefpunkt im Intervall |
| 22 | 4 | Produkt- und Kettenregel ineinander bei \(x e^{-x^{2}}\) |
| 23 | 4 | Modell aus Text — Abkühlung, Summand vor dem Logarithmieren abziehen |
| 24 | 4 | Art des Extremums entscheidet (naheliegende erste Stelle ist der Hochpunkt) |
| 25 | 5 | zweimal Produktregel, dann quadratische Gleichung — Wendestelle von \((x^{2}-3)e^{x}\) |
| 26 | 5 | Fehler finden (MC): Produktregel übergangen, zweite Extremstelle übersehen |
| 27 | 5 | Parameter aus der Wendepunktbedingung, Nachweis über \(f'''\) |
| 28 | 5 | größter Wert von \(\sin x + \cos x\) mit Randwertvergleich |
| 29 | 5 | zwei Schritte: Wendestelle über \(f''\), dann Steigung über \(f'\) |
| 30 | 5 | Fallunterscheidung: genau eine waagerechte Tangente nur für \(a=1\) |
| 31 | 6 | Behauptung prüfen (MC): \(x^{2}e^{-x}\) wächst nicht über alle Grenzen |
| 32 | 6 | Fallunterscheidung: verdoppeltes Argument verdoppelt die Anzahl der Lösungen |
| 33 | 6 | Abi eA: „Zeigen Sie" — genau ein Extrem- und ein Wendepunkt bei \((x-4)e^{x}\) |
| 34 | 6 | Abi eA: Schar \(x^{2}e^{-ax}\), genau ein Hochpunkt, Parameter aus dessen Höhe |
| 35 | 6 | Behauptung prüfen (MC): unendlich viele Nullstellen der gedämpften Schwingung |
| 36 | 6 | Abi eA: Produkt mit Wurzelterm, größter Wert mit Randwertvergleich |

---

## Beim Schreiben vermiedene Dubletten

Abgleich gegen `11-e-funktion.html` und `11-e-funktion-ableitung.html` (Block A, anderer Agent):

- `11-e-funktion` enthält bereits die Schar \(f_a(x)=e^{x}-a\cdot x\). Die ursprünglich für
  `11-lk-kurvendisk-erweitert #34` geplante Aufgabe zu genau dieser Schar wurde durch
  \(x^{2}e^{-ax}\) ersetzt.
- `11-e-funktion-ableitung` enthält \(f(x)=e^{2x}-4e^{x}\) (waagerechte Tangente) und
  \(f(x)=(ax+b)e^{x}\) mit zwei Bedingungen. Beide Formen wurden in
  `11-lk-kurvendisk-erweitert` nicht verwendet (#22 nutzt \(x e^{-x^{2}}\), #27 einen
  Wendepunkt mit \(x^{3}+a e^{x}\)).
- `11-e-funktion` enthält \(\ln 1\), \(\ln e\), \(\ln(e^{5})\) und \(e^{\ln 7}\) auf L1.
  Im Ersatz-Trainer wurden deshalb #2 (jetzt \(\ln(1/e)\)) und #6 (jetzt \(\ln\sqrt{e}\))
  umgestellt und #20 von \(e^{x}\) auf \(\ln x\) umgeschrieben; \(\ln e\) (#1) und
  \(\ln(e^{4})\) (#5) bleiben als Grundbausteine stehen.
- Innerhalb der vier Trainer: Extremwertaufgaben stehen im Ersatz-Trainer (ln), in
  `kurvendisk-erweitert` (e- und trigonometrische Terme) und in `gebrochen-rational`
  (\(x+\frac4x\)) jeweils mit verschiedenen Funktionsklassen.

## Gate-Ergebnisse

```
python tests/level_check.py --strict trainer/11-lk-funktionsscharen.html \
    trainer/11-lk-gebrochen-rational.html trainer/11-lk-kurvendisk-erweitert.html \
    trainer/11-lk-newton.html                     # Exit 0, 0 Fehler, 0 Warnungen
python tests/lehrplan_check.py --strict (dieselben)   # Exit 0, 0 Befunde
python tests/katex_check.py (dieselben)               # ok
python -m pytest tests/test_trainer.py -k "<stem>" -q # je 7 passed
python -m pytest tests/test_index.py -q                # 3 passed
python tests/bild.py … --level 1/3/4/5/6              # PNG erzeugt und angesehen
```

Die drei Warnungen aus dem Ausgangsbefund sind damit weg: Funktionsscharen #16
(Tipp mit Lösungswert 16), gebrochen-rational #29 (MC-Länge), Newton #21/#28 (MC-Länge).

## Offen (bewusst nicht in dieser Welle)

- **KOLLAPS L2/L3 in `11-lk-funktionsscharen`** bleibt: Stufe 1–3 werden laut Plan nicht neu
  geschrieben. #8/#9 (Extremstelle einer Schar) und #13/#15 (Ortskurve) bleiben nah beieinander.
- `11-lk-gebrochen-rational` #17/#18 kodieren \(\pm\infty\) als \(\pm 1\) in einem numerischen
  Feld — ein Notbehelf des Bestands. Sauberer wären MC-Aufgaben; Stufe 3 war hier nur
  für den Pflicht-Fix geöffnet.
- `11-lk-gebrochen-rational` #24 (\(f(2)\) für \(\frac{x^{2}}{x-1}\), Stufe 4) ist reines
  Einsetzen auf einer AFB-II-Stufe. Der Hinweis auf den Wert wurde aus dem Lösungsweg von
  #23 entfernt, damit die beiden sich nicht gegenseitig verraten.
- `11-lk-kurvendisk-erweitert`: Stufe 1–3 diskutieren dreimal eine ganzrationale Funktion
  (\(x^{3}-3x\), \(x^{4}-4x^{2}\), \(x^{3}-6x^{2}+9x\)) und liegen damit nah an
  `11-kurvendiskussion-ganzrational`. Der eigene Zuschnitt (zusammengesetzte Terme) beginnt
  erst ab Stufe 4. Eine Überarbeitung von Stufe 1–3 wäre der nächste sinnvolle Schritt.
- `11-lk-newton` #15/#16 (\(\int_1^e \frac1x\) und \(\int_1^e \frac3x\)) nutzen dasselbe
  Muster mit verschiedenem Faktor; bewusst beibehalten, weil der Unterschied
  \(3\ln x\) gegen \(\ln(3x)\) didaktisch trägt.
