# Klasse 12, Block A (Integralrechnung) — Kriterien je Trainer

Welle Task 9, Stand 2026-09-30. Lokale Nachvollziehbarkeit; im Public-HTML stehen die
Kriterien bewusst nicht. Grundlage: Rubrik aus
`2026-09-26-lehrplan-th-und-level-progression-plan.md`, Befunde aus
`../audit/audit-2026-09-19-mathepfade.md` (Zeilen 123–141).

Lesart Kl. 12 durchgängig:

- **L4 (AFB II)**: Verfahren selbst wählen, Modell aus einem Sachtext aufstellen,
  Umkehraufgabe (Parameter oder Grenze gesucht statt Wert).
- **L5 (AFB III)**: zwei Verfahren kombinieren, Parameter aus zwei Bedingungen,
  Fehler in einer vorgelegten Rechnung finden. Bei jeder Fehlersuchaufgabe wurde geprüft,
  dass der vorgeführte falsche Weg auch wirklich auf ein **falsches Ergebnis** führt
  (Lehre aus Kl. 11, wo ein falscher Weg zufällig die richtige Lösung lieferte).
- **L6 (AFB III, Abi-Format)**: mehrschrittig mit Begründungs- oder Nachweisanteil,
  Sachkontext, Formulierungen „Zeigen Sie …“, „Begründen Sie …“, „Beurteilen Sie …“,
  Fallunterscheidung oder Grenzfall. In den eA-Trainern in der eA-Variante.

Jede Lösung mit dem Wolfram-MCP nachgerechnet — auch die jeweils *nicht* gefragten Fälle
(Nebenlösungen, Vorzeichenwechsel im Intervall, Grenzfälle). Bilder je Trainer mit
`tests/bild.py --aufgabe <id>` erzeugt und angesehen.

## Abgrenzung der fünf Trainer gegeneinander

| Trainer | Inhalt |
|---|---|
| 12-stammfunktionen | Stammfunktion bilden, Regeln, unbestimmtes Integral, Integrationskonstante aus einer Bedingung. **Keine** Berechnung bestimmter Integrale mehr (lag vorher in Stufe 5) |
| 12-bestimmtes-integral | bestimmte Integrale berechnen, Hauptsatz, Linearität und Intervalladditivität, orientierter Flächeninhalt, Rate gegen Bestand |
| 12-flaechenberechnung | Flächen zwischen Graph und Achse bzw. zwischen zwei Graphen, Nullstellen und Schnittstellen als Grenzen, Aufteilen bei Vorzeichenwechsel |
| 12-lk-integral-rotationskoerper (eA) | Volumen von Rotationskörpern um beide Achsen, Hohlkörper, Parameter und Scharen |
| 12-lk-integral-uneigentlich (eA) | **Ersatz:** Stetigkeit, Asymptoten, Periodizität (TH 4.1 eA) |

Der Betrag im Integranden liegt bei `12-bestimmtes-integral` (dort als Zerlegung des
Intervalls), das Aufteilen an Nullstellen bei `12-flaechenberechnung`. Die Fläche zwischen
zwei Graphen kommt in `12-lk-integral-rotationskoerper` nur als Ausgangsfläche eines
Körpers vor, nie als Selbstzweck.

---

## 12-bestimmtes-integral

Audit: KEIN_AFB3 L5; KOLLAPS L2/L3 **und** L3/L4; KURZ (Stufen 1, 2, 3, 4).
Wegen KOLLAPS L3/L4 wurde auch Stufe 4 neu geschrieben. Die knappen Aufgabentexte der
Stufen 2 und 3 („\(\int_0^2 2x\,dx = ?\)“) sind zu vollständigen Aufträgen ausformuliert;
Zahlen und Lösungen dort unverändert (Befund KURZ, nicht KOLLAPS).

| id | Level | Kriterium |
|---|---|---|
| 7–18 | 2, 3 | KURZ behoben: Aufgabentexte ausformuliert, Arbeitsauftrag benannt (Stammfunktion bilden, Vorzeichen der unteren Grenze, Ergebnis deuten) |
| 19 | 4 | Hauptsatz ohne Kenntnis von \(f\): nur \(F\) an den Grenzen gegeben |
| 20 | 4 | Modell aus Text: Zuflussrate integrieren, Einheit begründet |
| 21 | 4 | Verfahren wählen: lineare innere Funktion, Ausgleich der inneren Ableitung |
| 22 | 4 | Umkehraufgabe: obere Grenze aus der Bedingung „Integral null“, Nebenlösung \(b=0\) ausgeschlossen |
| 23 | 4 | Verfahren wählen: Summe zweier trigonometrischer Terme, Vorzeichen der Stammfunktion des Sinus |
| 24 | 4 | Modell aus Text: Grenzkosten, Differenz der Kostenfunktion; Fixkosten kürzen sich |
| 25 | 5 | Fehler finden: doppeltes Minus beim Einsetzen. Falscher Weg liefert \(-\tfrac83\), richtig ist \(+\tfrac83\) — verschieden geprüft |
| 26 | 5 | Parameter aus zwei Bedingungen (Integralwert und Funktionswert) |
| 27 | 5 | Zwei Verfahren: Betrag zerlegen, beide Teilintegrale |
| 28 | 5 | Intervalladditivität und Linearität verzahnt; die große Zahl darf nicht direkt eingesetzt werden |
| 29 | 5 | Fehler finden: „Integral des Produkts = Produkt der Integrale“. Falscher Weg \(\tfrac{16}{3}\), richtig \(4\) |
| 30 | 5 | Umkehraufgabe mit Exponentialgleichung, Logarithmus nötig |
| 31 | 6 | Abi-Format: Sachkontext Rate/Menge, Nachweis „Zufluss versiegt“ plus Rechnung |
| 32 | 6 | Abi-Format: Mittelwert einer Funktion im Sachkontext, e-Term mit innerer Ableitung |
| 33 | 6 | Beurteilen: „\(\int = 0 \Rightarrow f \equiv 0\)“ — Widerlegung durch Gegenbeispiel |
| 34 | 6 | Schar: allgemeines Integral, Vorzeichennachweis, danach Parameter aus einer Bedingung |
| 35 | 6 | Abi-Format: Bremsweg, Nachweis „steht nach 20 s“, Hinweis auf die Gültigkeitsgrenze des Modells |
| 36 | 6 | Integral als Funktion der oberen Grenze, Minimum dieser Funktion; Begründung des Vorzeichens |

Gate-Warnungen aus dem Bestand (#22, #35, MC-Länge) sind mit den neuen Stufen entfallen.

## 12-stammfunktionen

Audit: KEIN_AFB3 L5 **und** L6; DUENNER_WEG (Stufen 2, 4). Stufen 5 und 6 neu.
Die alten Stufen 5/6 rechneten überwiegend bestimmte Integrale — das gehört zum
Nachbartrainer und ist entfallen.

| id | Level | Kriterium |
|---|---|---|
| 8, 9, 10, 23 | 2, 4 | DUENNER_WEG behoben: Lösungsweg zeigt Potenzregel bzw. Summenregel getrennt, mit Probe; die Aufgabentexte verlangen jetzt ausdrücklich das Bilden der Stammfunktion, nicht nur das Einsetzen |
| 25 | 5 | Fehler finden: Nenner \(4\) statt \(8\). Probe liefert \(2(2x+1)^3\), also das Doppelte — falsches Ergebnis geprüft |
| 26 | 5 | Parameter aus zwei Bedingungen (Funktionswert und Wert der Stammfunktion) |
| 27 | 5 | Zwei Regeln kombiniert: e-Term und Sinus, beide mit innerer Ableitung |
| 28 | 5 | Fehler finden: \(\ln(x^2)\) statt \(-\tfrac1x\). Probe liefert \(\tfrac2x\) — falsch |
| 29 | 5 | Parameter und Integrationskonstante aus zwei Bedingungen |
| 30 | 5 | Konstante aus einer Bedingung an einer Stelle, Auswertung an einer anderen |
| 31 | 6 | Beurteilen: Stammfunktionen unterscheiden sich nur um eine Konstante — Beweis über \(H' = 0\) |
| 32 | 6 | Abi-Format: Bestandsfunktion aus Zuwachsrate, Konstante aus Anfangsbedingung |
| 33 | 6 | „Zeigen Sie“: Nachweis einer Stammfunktion durch Ableiten (Produktregel), danach Differenz |
| 34 | 6 | Schar mit zwei Bedingungen an die Stammfunktion |
| 35 | 6 | Beurteilen: \(F^2\) ist keine Stammfunktion von \(f^2\) — Gegenbeispiel und Produktregel |
| 36 | 6 | Abi-Format: Funktion aus ihrer Ableitung, Formnachweis plus Wert |

## 12-flaechenberechnung

Audit: KEIN_AFB3 L5 **und** L6. Stufen 5 und 6 neu. Im Altbestand stand der Wert
\(10{,}\overline{6}\) viermal und \(1{,}\overline{3}\) fünfmal, über die Stufen 2 bis 6
verteilt; diese Wiederholungen sind mit dem neuen Block verschwunden.

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | Fehler finden: „untere minus obere“ Funktion. Falscher Weg \(-4{,}5\), richtig \(4{,}5\) |
| 26 | 5 | Schnittstellen nicht angegeben, quadratische Gleichung als Zwischenschritt, Lage über Probe |
| 27 | 5 | Parameter aus einer Flächenbedingung; Nullstellen hängen selbst vom Parameter ab |
| 28 | 5 | Fehler finden: Schnittstelle im Intervall übersehen. Falscher Weg \(\tfrac23\), richtig \(1\) |
| 29 | 5 | Zwei Flächenstücke, Schnittstelle im Intervall, Symmetrieargument im Lösungsweg |
| 30 | 5 | Fläche zwischen Kurve und waagerechter Geraden; Konstante wird integriert |
| 31 | 6 | Abi-Format mit Sachkontext (Tunnelquerschnitt), Nachweis der Breite plus Fläche |
| 32 | 6 | Beurteilen: Lage zur \(x\)-Achse gegen Lage zueinander — Gegenbeispiel mit negativem Integral |
| 33 | 6 | „Zeigen Sie“: Nullstellen durch Ausklammern, Lage durch Probe, Betrag des Integrals |
| 34 | 6 | Schnittstellen selbst bestimmen, Fläche zwischen Parabel und Gerade |
| 35 | 6 | „Zeigen Sie“: Schnittstellen über Quadrieren, Wurzel in Potenzschreibweise |
| 36 | 6 | Begründung der Punktsymmetrie, orientierter gegen absoluten Inhalt |

## 12-lk-integral-rotationskoerper (eA)

Audit: KEIN_AFB3 L5 **und** L6; DUENNER_WEG (Stufe 6); Gate-Warnung `#31 (L6)` — der Tipp
nannte den Lösungswert 15. Stufen 5 und 6 neu; die Warnung ist damit behoben.

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | Fehler finden: Quadrat im Integranden vergessen. Falscher Weg \(4\pi\), richtig \(\tfrac{26}{3}\pi\) |
| 26 | 5 | Umkehraufgabe: obere Grenze aus dem Volumen, quadratische Gleichung, negative Lösung verworfen |
| 27 | 5 | Parameter im Integranden, wird mitquadriert; Probe über die Kegelformel |
| 28 | 5 | Fehler finden: \((f-g)^2\) statt \(f^2-g^2\). Falscher Weg \(7{,}2\), richtig \(8{,}8\) |
| 29 | 5 | Umkehraufgabe mit negativem Exponenten; Hinweis auf die Schranke des Terms |
| 30 | 5 | Schnittstellen selbst bestimmen, äußerer Rand durch Probe geklärt |
| 31 | 6 | Abi-Format: Sachkontext Maschinenteil, Formnachweis (Kegelstumpf) plus Volumen in cm³ |
| 32 | 6 | Beurteilen: Verdoppeln der Funktionswerte vervierfacht das Volumen |
| 33 | 6 | Rotation um die \(y\)-Achse, Umkehrfunktion als Radius, Grenzen in \(y\) |
| 34 | 6 | Hohlkörper mit selbst bestimmten Schnittstellen, Quadrate getrennt |
| 35 | 6 | Schar: allgemeiner Nachweis der Volumenformel, danach Parameter aus einer Bedingung |
| 36 | 6 | Vergleich zweier Körper allgemein in \(h\); Verhältnis unabhängig von \(h\) |

## 12-lk-integral-uneigentlich (eA) — **Ersatz-Trainer**

Alle 36 Aufgaben neu. Der Dateiname bleibt wegen der QR-Links, ebenso `THEMA_KEY`
(localStorage-Schlüssel — sonst verlieren Schülerinnen und Schüler ihren Fortschritt).
Geändert: `<title>`, `THEMA_CONFIG.name = 'Stetigkeit und Asymptoten (eA)'`, Kommentar in
Zeile 2. Das Wort „uneigentlich“ kommt im gesamten Inhalt nicht mehr vor; es steht nur noch
im unveränderlichen `THEMA_KEY` und im Dateinamen. Neuer Index-Text siehe unten.

Neues Thema: **Stetigkeit, Asymptoten, Periodizität** (TH 4.1 eA).

### Abgrenzung gegen die Nachbartrainer

Asymptoten liegen bereits in `10-polynomdivision` (heißt inhaltlich „Grenzwerte und
Asymptoten“) und in `11-lk-gebrochen-rational`. Der Schwerpunkt hier ist deshalb
**Stetigkeit und Periodizität**; Asymptoten kommen nur im eA-Zuschnitt vor, und zwar
ausschließlich an **e-Funktionen** (waagerechte Näherungsgerade aus einem konstanten
Summanden) sowie an genau einer Stelle als senkrechte Näherungsgerade eines Terms mit
e-Zähler. Grenzwerte gebrochen-rationaler Terme für \(x \to \pm\infty\), Polstellen gegen
hebbare Lücken, schiefe Asymptoten und die Gradbetrachtung von Zähler und Nenner bleiben
den beiden Nachbartrainern vorbehalten. Der Begriff „Asymptote“ wird hier durchgängig als
„Näherungsgerade“ ausgeschrieben, damit die Aufgabenformulierungen sich nicht mit denen
der Nachbartrainer decken. Genau **eine** Aufgabe zur stetigen Fortsetzung eines
gekürzten Bruchterms (#13) berührt ein Muster aus `11-lk-gebrochen-rational` — mit anderem
Term und anderer Fragestellung; sie ist als Einstieg in den Stetigkeitsbegriff nötig.

| id | Level | Kriterium |
|---|---|---|
| 1 | 1 | Begriff Stetigkeit: Grenzwert gleich Funktionswert |
| 2 | 1 | Sprungstelle an einer abschnittsweise erklärten Funktion erkennen |
| 3 | 1 | Periode von \(\sin x\) |
| 4 | 1 | Waagerechte Näherungsgerade von \(e^{x}+3\) für \(x \to -\infty\) |
| 5 | 1 | Verhalten von \(e^{-x}\) für \(x \to \infty\) |
| 6 | 1 | Periode von \(\sin(2x)\), Wirkung des Faktors im Argument |
| 7, 8 | 2 | Periode mit ganzzahligem bzw. gebrochenem Faktor; Vorfaktor ohne Wirkung auf die Periode |
| 9, 11 | 2 | Nahtstelle abschnittsweise erklärter Funktionen: beide Teilterme auswerten und vergleichen |
| 10, 12 | 2 | Waagerechte Näherungsgerade aus dem konstanten Summanden einer e-Funktion |
| 13 | 3 | Stetige Fortsetzung: Zähler faktorisieren, kürzen, Wert ergänzen |
| 14 | 3 | Periode trotz Vorfaktor und Verschiebung |
| 15 | 3 | Senkrechte Näherungsgerade: e-Zähler kann sich nicht kürzen |
| 16 | 3 | Betragsfunktion: stetig, aber nicht differenzierbar (Vorbereitung auf L5/L6) |
| 17 | 3 | Näherungsgerade für \(x \to -\infty\), Graph erreicht sie nie |
| 18 | 3 | Periode von \(\cos(\pi x)\), Kreiszahl kürzt sich |
| 19, 20 | 4 | Parameter für stetigen Anschluss; zuerst die Seite ohne Parameter auswerten |
| 21 | 4 | Umkehraufgabe: Faktor im Argument aus vorgegebener Periode |
| 22 | 4 | Verhalten von \(e^{-x^2}\) nach beiden Seiten; Quadrat im Exponenten |
| 23 | 4 | Grenzwert aus einer Wertetabelle schließen (\(\frac{\sin x}{x}\)), Rechnung nicht möglich |
| 24 | 4 | Parameter aus dem Achsenschnittpunkt; die Angabe zur Näherungsgeraden ist bereits erfüllt |
| 25, 26 | 5 | **Zwei Bedingungen: stetig und differenzierbar.** Wertegleichung und Steigungsgleichung; bei #25 ist der lineare Ast gerade die Tangente |
| 27 | 5 | **Fehler in einer Asymptoten-Begründung:** \(e^{-x}\) mit \(e^{x}\) verwechselt; richtige Gerade \(y=2\) |
| 28 | 5 | Fehler: Stetigkeit an einer Stelle behauptet, die nicht zum Definitionsbereich gehört |
| 29 | 5 | Zwei Bedingungen an eine Sinusfunktion (Periode und größter Wert) |
| 30 | 5 | Parameter, für den eine stetige Fortsetzung überhaupt möglich ist (Zähler muss mitverschwinden) |
| 31 | 6 | Behauptung prüfen: aus Differenzierbarkeit folgt Stetigkeit, die Umkehrung nicht |
| 32 | 6 | Abi-Format: Gleichungssystem aus Stetigkeit und Differenzierbarkeit in zwei Parametern, mit Probe |
| 33 | 6 | Behauptung prüfen: periodisch und waagerechte Näherungsgerade schließen einander aus |
| 34 | 6 | Abi-Format mit Sachkontext (Tide): Schranken aus dem Wertebereich des Sinus, Periode als Dauer |
| 35 | 6 | Abi-Format eA: dritte binomische Formel mit \(e^{2x}=\left(e^{x}\right)^2\), stetige Fortsetzung |
| 36 | 6 | Behauptung prüfen: überall stetige Funktion auf \(\mathbb{R}\) hat keine senkrechte Näherungsgerade; das naheliegende Gegenbeispiel taugt nicht |

### Nachzutragen in `index.html` (bewusst nicht von diesem Agenten geändert)

Zeile 947, `<span class="theme-name">`: statt „Uneigentliche Integrale“ neu

```
Stetigkeit &amp; Asymptoten
```

---

## Gefundene und behobene Fehler während der Umsetzung

- **Aufgabe verriet die Nachbaraufgabe** (Ersatz-Trainer): #19 (stetiger Anschluss,
  \(x^2\) und \(2x+c\)) und #25 (stetig und differenzierbar, \(x^2\) und \(ax+b\)) hätten
  denselben rechten Ast \(2x-1\) ergeben — wer #25 gelöst hat, kannte die Lösung von #19.
  #19 auf andere Nahtstelle und andere Terme umgestellt.
- Im selben Lösungsweg stand ein halb ausformulierter Satz („die Steigungen sind \(2\) und
  \(2\)… tatsächlich stimmen sie überein“), der einen Knick behauptete, den es nicht gibt.
  Mit der Neufassung entfallen.
- Doppelter Kommentar `// LEVEL 4` in `12-bestimmtes-integral` nach dem Einsetzen entfernt.
- Drei MC-Warnungen des Level-Gates (richtige Option deutlich länger als die Distraktoren)
  behoben: `12-bestimmtes-integral` #33, `12-lk-integral-uneigentlich` #22.

## Offen

- **KOLLAPS L2/L3 in `12-bestimmtes-integral`** bleibt bestehen: die Stufen 1–3 werden
  planmäßig nur entdoppelt und ausformuliert, nicht neu geschrieben. Stufe 3 unterscheidet
  sich von Stufe 2 jetzt durch Trigonometrie, e-Funktion und Kehrwert, die Messgröße des
  Audits (Textlänge) dürfte das aber weiterhin als Kollaps ausweisen.
- `12-stammfunktionen` Stufe 4 besteht weiterhin überwiegend aus MC-Aufgaben zu den
  Grundstammfunktionen (\(\frac1x\), \(e^x\), Sinus, Kosinus). Inhaltlich richtig, aber als
  AFB II grenzwertig; eine eigene Runde für Stufe 4 wäre sinnvoll.
- `index.html` ist nicht angefasst (vier Ersatz-Trainer der Welle brauchen die Datei
  gleichzeitig); der neue `theme-name`-Text steht oben.
