# Klasse 12, Block C2 (Stochastik eA) — Kriterien je Aufgabe

Welle Task 9, Stand 2026-09-30. Lokale Nachvollziehbarkeit; im Public-HTML stehen die
Kriterien bewusst nicht. Grundlage: Rubrik aus
`2026-09-26-lehrplan-th-und-level-progression-plan.md`, Befunde aus
`../audit/audit-2026-09-19-mathepfade.md` (Zeilen 123–141 und 202), Muster der Einträge:
`2026-09-26-kl11-kriterien.md`.

Lesart Kl. 12 eA durchgängig:

- **L4 (AFB II)**: Verfahren selbst wählen, Modell aus einem Sachtext, Umkehraufgabe
  (Parameter oder Umfang gesucht statt Ergebnis).
- **L5 (AFB III)**: zwei Verfahren verbinden, Parameter aus zwei Bedingungen, Fehler in einer
  vorgelegten Rechnung finden.
- **L6 (AFB III, Abi-Format eA)**: mehrschrittig, mit Begründungs- und Beweisanteil
  („Zeigen Sie …“, „Beurteilen Sie …“), Modellkritik, Grenzfall.

Jede Lösung mit dem Wolfram-MCP nachgerechnet (Φ-Werte, Quantile, Wurzeln, beide Lösungen
quadratischer Gleichungen). Bilder mehrerer Stufen mit `tests/bild.py --aufgabe <id>` erzeugt
**und angesehen**, zusätzlich Lösungswege über ein Scratchpad-Skript aufgedeckt und angesehen
(`tests/bild.py` zeigt nur die Aufgabenseite, nicht den Rechenweg).

| Trainer | Audit-Befund | Geändert |
|---|---|---|
| 12-lk-stoch-normalverteilung | KEIN_AFB3 L5 **und** L6; DUENNER_WEG (Stufen 1,3,4,5); Warnungen `#30` und `#34` (Tipp mit Lösungswert) | Stufe 5 und 6 komplett neu (12 Aufgaben); sechs dünne Lösungswege (#7, #8, #10, #12, #13, #14) ausgebaut |
| 12-lk-stoch-prozesse (Dateiname historisch) | Ersatz-Trainer; **27 Befunde — die meisten des Projekts**; KOLLAPS L3/L4 und L4/L5; DUENNER_WEG (Stufen 2–6); Lehrplan-Gate: „Übergangsmatrix“ in #5, #15, #16 | **Alle 36 Aufgaben neu: Konfidenzintervall und Stichprobenumfang**, TH 4.3 eA. `<title>`, `THEMA_CONFIG.name = 'Konfidenzintervalle (eA)'` und Kommentar in Zeile 2 geändert; `THEMA_KEY` **unverändert** (Schülerfortschritt) |

## Abgrenzung

- **12-lk-stoch-normalverteilung** = Normalverteilung selbst: Dichte, Wendestellen, Φ-Funktion,
  Standardisierung, Quantile, Näherung der Binomialverteilung samt Stetigkeitskorrektur.
- **12-lk-stoch-prozesse** = Schluss von der Stichprobe auf das unbekannte \(p\):
  Konfidenzintervall, Intervallbreite, Stichprobenumfang.
- Gegen die gA-Trainer des Parallelblocks (`12-stoch-binomialverteilung`,
  `12-stoch-sigma-regeln`, `12-stoch-zufallsgroessen`, künftig „Prognoseintervalle“) wurde
  abgegrenzt: dort die gA-Tiefe, hier die eA-Tiefe. Der Duplikat-Lauf von `level_check`
  über alle 90 Trainer meldet für beide Dateien nichts.

### Konfidenzintervall gegen Prognoseintervall (der fachliche Kern des Ersatz-Trainers)

Ein **Konfidenzintervall** schließt von der beobachteten relativen Häufigkeit \(h\) auf das
unbekannte \(p\): Mitte ist \(h\), und weil \(p\) fehlt, wird auch die Streuung mit \(h\)
geschätzt. Ein **Prognoseintervall** geht umgekehrt vor: \(p\) ist bekannt, Mitte und Streuung
werden damit gebildet, gefragt sind die zu erwartenden Häufigkeiten. Diese Verwechslung ist
die Fehlersuchaufgabe `#25`. Die Zahlen sind so gewählt, dass die beiden Intervalle **sichtbar
verschieden** sind — \([0{,}40;\,0{,}60]\) gegen \([0{,}5229;\,0{,}7171]\). Beide Grenzen liegen
über 11 Prozentpunkte auseinander (unten \(0{,}1229\), oben \(0{,}1171\), mit Wolfram
nachgerechnet); der falsche Weg führt also sicher auf ein falsches Ergebnis (Lehre aus Kl. 11,
wo eine Fehlersuchaufgabe zufällig die richtige Lösung traf).

Beim Schreiben stand im Lösungsweg zunächst, das Konfidenzintervall liege „vollständig über
\(0{,}60\)“ — das war falsch, die beiden Intervalle überlappen sich auf \([0{,}5229;\,0{,}60]\).
Gefunden beim Nachrechnen der Differenz; der Satz nennt jetzt die beiden Grenzabstände.

---

## 12-lk-stoch-prozesse → Konfidenzintervalle (eA), Ersatz-Trainer

Levelaufbau nach der Vorgabe aus Task 9. Nach der Umstellung kommt das Wort
„Übergangsmatrix“ in der Datei nicht mehr vor (Lehrplan-Gate: 0 Befunde).

Näherungsfaktor: L1–L3 durchgängig die \(2\sigma\)-Näherung, ab `#15` wird der genauere
Faktor \(1{,}96\) eingeführt und im Lösungsweg gegen die \(2\) abgegrenzt
(\(2\Phi(1{,}96)-1 = 0{,}95\); der Faktor \(2\) gehört zu \(95{,}4\,\%\) und liefert ein
etwas vorsichtigeres Intervall). Jede Aufgabe sagt, welcher Faktor gilt.
Aufgerundet wird bei jeder Mindestforderung an \(n\), und im Lösungsweg steht warum.

| id | Level | Kriterium |
|---|---|---|
| 1 | 1 | Begriff (MC): Konfidenzintervall schätzt das unbekannte \(p\), nicht \(h\), \(n\) oder die Trefferzahl |
| 2 | 1 | \(\sigma_h\) aus \(h\) und \(n\), ein Rechenschritt, Wurzel geht auf |
| 3 | 1 | halbe Breite als \(2\sigma_h\) bei gegebenem \(\sigma_h\) |
| 4 | 1 | Breite aus zwei Intervallgrenzen |
| 5 | 1 | untere Grenze aus \(h\) und Radius |
| 6 | 1 | Zugehörigkeit eines Wertes zum Intervall (MC, vier gleich lange Zahlenoptionen) |
| 7 | 2 | Standardverfahren: \(\sigma_h\), Radius, untere Grenze |
| 8 | 2 | dasselbe zur oberen Grenze, andere Zahlen |
| 9 | 2 | zwei Schritte: \(h\) aus Anzahl und Umfang, dann Breite \(4\sigma_h\) |
| 10 | 2 | obere Grenze, Zahlen so gewählt, dass die Wurzel aufgeht |
| 11 | 2 | Abhängigkeit von \(n\) (MC): vierfaches \(n\) halbiert die Breite — \(n\) steht unter der Wurzel |
| 12 | 2 | Radius in Prozentpunkten; Bezug zur üblichen Angabe „\(\pm 2{,}5\) Prozentpunkte“ |
| 13 | 3 | Klassenarbeits-Standard mit Zwischenergebnis: \(h\) aus 520/1000, dann untere Grenze |
| 14 | 3 | Umkehr-Lesart: Mitte und Radius aus einem gegebenen Intervall |
| 15 | 3 | Rechnung mit dem Faktor \(1{,}96\); Lösungsweg begründet die Wahl gegen den Faktor \(2\) |
| 16 | 3 | Breite in Prozentpunkten, Ergebnis zusätzlich als Prozentintervall gedeutet |
| 17 | 3 | kleine relative Häufigkeit (Ausschussquote), vier Dezimalstellen nötig |
| 18 | 3 | Laplace-Bedingung: \(\sigma(X)\) der Trefferanzahl berechnen und gegen die Faustregel \(\sigma \gt 3\) stellen |
| 19 | 4 | Umkehr: \(n\) aus geforderter Breite, schlechtester Fall \(h = 0{,}5\); **Aufrunden begründet** |
| 20 | 4 | Verfahren wählen + Entscheidung: behauptetes \(p = 0{,}30\) liegt außerhalb von \([0{,}3171;\,0{,}4029]\) |
| 21 | 4 | \(n\) aus geforderter Genauigkeit bei \(h = 0{,}2\); Lösungsweg zeigt, warum ein kleineres \(n\) genügt |
| 22 | 4 | Umkehraufgabe mit zwei Lösungen: \(h(1-h) = 0{,}16\) liefert \(0{,}2\) und \(0{,}8\), Symmetrie erklärt |
| 23 | 4 | Modell aus Text: halbe Breite ⇒ vierfaches \(n\) (900 → 3600) |
| 24 | 4 | Maßnahmen beurteilen (MC); die höhere Sicherheit verbreitert das Intervall, sie verschmälert es nicht |
| 25 | 5 | **Fehlersuche „Konfidenzintervall = Prognoseintervall“** — siehe Abschnitt oben; Intervalle überlappen sich nicht |
| 26 | 5 | zwei Verfahren: beide Breiten getrennt, Vergleich in Prozentpunkten; Faktor \(\sqrt{400/900} = \tfrac23\) |
| 27 | 5 | **zwei Bedingungen**: Breite \(\le\) 3 Prozentpunkte **und** \(\sigma(X) \gt 3\); die schärfere gewinnt, Probe im Weg |
| 28 | 5 | Fehlersuche: \(n\) statt \(\sqrt{n}\) im Nenner; falscher Radius 25-mal zu klein, Plausibilitätskontrolle ergänzt |
| 29 | 5 | zwei Intervalle, Breite der Überlappung; Deutung: 6 Prozentpunkte Unterschied sind Stichprobenschwankung |
| 30 | 5 | Umkehr aus Mitte und Breite auf \(n\); hier wird **nicht** gerundet — begründet |
| 31 | 6 | Abi eA: KI mit \(1{,}96\), Beurteilung einer Zeitungsaussage; Grenzfall — mit Faktor \(2\) kippt die Entscheidung |
| 32 | 6 | Abi eA, Modellkritik: die Näherung liefert eine **negative** untere Grenze; \(\sigma(X) \approx 1{,}72 \lt 3\), Verteilung rechtsschief |
| 33 | 6 | mehrschrittig: \(h\) aus 96/1200, dann Faktor 9 für ein Drittel der Breite, mit Begründung über \(1/\sqrt{n}\) |
| 34 | 6 | **Beweisanteil**: \(h(1-h)\) maximal bei \(h = 0{,}5\) über \(g'\) und \(g''\); daraus der sichere Umfang \(49^2\) |
| 35 | 6 | Begründung (MC): warum \(h\) und nicht \(p\) in der Streuung steht — der Unterschied zum Prognoseintervall |
| 36 | 6 | Abi eA, Modellkritik: Selbstselektion bei einer Online-Umfrage; ein schmales Intervall misst nur die Zufallsschwankung |

### Formen je Stufe (gegen die Befunde an den Ersatz-Trainern der Kl. 10 und 11)

Innerhalb keiner Stufe steht dieselbe Aufgabenform dreimal. In L1 wechseln Begriff,
\(\sigma_h\), Radius, Breite, Grenze und Zugehörigkeit; in L4 stehen zwei Umfangsaufgaben
neben Entscheidung, quadratischer Umkehraufgabe, Textmodell und MC; in L5 je zwei
Fehlersuch-, Vergleichs- und Umkehraufgaben.

Über die Stufen hinweg kehrt der Stichprobenumfang wieder — das ist das Thema des Trainers —,
aber **nicht als dasselbe Verfahren mit größeren Zahlen**: L4 löst die Ungleichung,
L5 verbindet sie mit einer zweiten Bedingung bzw. rechnet aus Mitte und Breite zurück,
L6 begründet erst den schlechtesten Fall über eine Extremwertbetrachtung bzw. leitet den
Skalierungsfaktor her.

---

## 12-lk-stoch-normalverteilung — Stufe 5 und 6 neu

Stufe 1–4 bleiben inhaltlich; dort wurden nur sechs dünne Lösungswege ausgebaut.

| id | Level | Kriterium |
|---|---|---|
| 7, 8, 10, 12 | 2 | DUENNER_WEG behoben: \(\mu = np\) bzw. \(\sigma = \sqrt{np(1-p)}\) mit Zwischenschritt, Deutung und Hinweis auf die Laplace-Bedingung |
| 13, 14 | 3 | DUENNER_WEG behoben: Lösungsweg nennt jetzt ausdrücklich, dass in \(N(\mu;\sigma^2)\) die **Varianz** steht, und zeigt die Standardisierung als Abstand in \(\sigma\)-Einheiten |
| 25 | 5 | **Parameter aus zwei Bedingungen**: \(\Phi\)-Werte \(0{,}8413\) und \(0{,}0228\) ⇒ \(z = 1\) und \(z = -2\), Gleichungssystem, \(\mu = \tfrac{160}{3}\), Probe |
| 26 | 5 | **Fehlersuche**: durch \(\sigma^2 = 64\) statt \(\sigma = 8\) geteilt; falsch \(0{,}438\) gegen richtig \(0{,}1056\) — fast das Vierfache, Größenordnungskontrolle im Weg |
| 27 | 5 | zwei Verfahren: Binomialparameter, Laplace-Prüfung, Quantil \(2{,}326\); \(k = 547\), **Aufrunden begründet** (546 verletzt die Forderung) |
| 28 | 5 | zwei Schritte: \(\mu\) und \(\sigma\) aus den Wendestellen der Dichte ablesen, dann \(\Phi(2)\) |
| 29 | 5 | **Fehlersuche** Stetigkeitskorrektur in die falsche Richtung: \(470{,}5\) gehört zu \(P(X \ge 471)\); falsch \(0{,}0859\) gegen richtig \(0{,}0968\) |
| 30 | 5 | quadratische Umkehraufgabe: \(400p(1-p) = 36\) ⇒ \(p = 0{,}1\) und \(0{,}9\), Bedingung \(p \lt 0{,}5\) wählt aus (bewusst andere Zahlen als `#22` des Nachbartrainers) |
| 31 | 6 | Abi eA: Abfüllanlage, kleinstes \(\mu\) aus einer Höchstquote; **Rundungsrichtung begründet**, Deutung des Aufschlags |
| 32 | 6 | Abi eA, Modellkritik: \(\sigma \approx 1{,}07 \lt 3\) — „\(n\) ist groß genug“ ist als Begründung falsch; rechtsschiefe Verteilung, exakt binomial rechnen |
| 33 | 6 | Abi eA, **„Beurteilen Sie“**: \(P(X \gt 330) \approx 3{,}9\,\%\) — „praktisch ausgeschlossen“ ist zurückzuweisen; Grenze \(\mu + 3\sigma\) als Maßstab |
| 34 | 6 | **Beweisanteil**: \(\varphi(\mu\pm\sigma)/\varphi(\mu) = e^{-1/2}\) — Vorfaktoren kürzen sich, das Ergebnis hängt weder von \(\mu\) noch von \(\sigma\) ab |
| 35 | 6 | Grenzfall/Falle: symmetrisches Intervall mit \(0{,}90\) verlangt das \(0{,}95\)-Quantil; der falsche Tabellenwert \(1{,}282\) wird im Weg durchgerechnet |
| 36 | 6 | Abi eA, Modellkritik: Normalverteilung ist auf ganz \(\mathbb{R}\) definiert und gibt auch unmöglichen Größen positive Wahrscheinlichkeit — an den Rändern nicht tragfähig |

Beide Gate-Warnungen sind damit weg: `#30` und `#34` sind ersetzt, die neuen Tipps nennen nur
den Weg, keinen Wert, keine Zwischenlösung und keine fertige Gleichung.

## Gates (Stand nach dem Block)

```
python tests/level_check.py --strict trainer/12-lk-stoch-prozesse.html \
                                     trainer/12-lk-stoch-normalverteilung.html   # 0 Fehler, 0 Warnungen
python tests/lehrplan_check.py --strict (beide)                                  # 0 Befunde
python tests/katex_check.py (beide)                                              # 0 Renderfehler
python -m pytest tests/test_trainer.py -k "stoch-prozesse or stoch-normalverteilung" -q   # 14 passed
python tests/level_check.py            # Duplikat-Lauf über alle 90 Trainer: beide ohne Befund
```

Sichtprüfung: `#25`, `#34`, `#35` des Ersatz-Trainers sowie `#25`, `#31`, `#34` der
Normalverteilung als PNG angesehen — Aufgabenseite und aufgedeckter Lösungsweg. Dabei
behoben: ein Zeilenumbruch, der in `#34` die schließende Klammer hinter „Faktor 1,96“ allein
in die nächste Zeile setzte (Klammer durch „mit dem Faktor“ ersetzt), und sechs Stellen mit
`&quot;` als Schlusszeichen, die jetzt die deutsche Schlussanführung tragen.

## Index

`index.html` wurde von diesem Block **nicht** angefasst (vier Ersatz-Trainer brauchten sie
gleichzeitig). Nachzuziehen ist der `theme-name` der Zeile zu `12-lk-stoch-prozesse.html`:

```
Konfidenzintervalle
```

## Offen

- Die Stufen 1–4 der Normalverteilung sind planmäßig nicht neu geschrieben worden; der
  KOLLAPS-Rest zwischen L3 und L4 (Standardisieren gegen Standardisieren mit Näherung)
  bleibt bestehen.
- Der Ersatz-Trainer benutzt durchgehend die Näherungsformel mit \(h\) in der Streuung
  (Wald-Intervall). Genauere Verfahren sind in der Schule nicht vorgesehen; `#32` zeigt
  ausdrücklich, wo dieses Verfahren versagt.
- Der Name „Stochastische Prozesse“ verschwindet mit der Index-Zeile; der Dateiname bleibt
  wegen der QR-Links historisch.
