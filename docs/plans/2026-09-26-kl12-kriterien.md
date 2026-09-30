# Klasse 12 — Kriterien je Trainer (Welle Task 9, Stand 2026-09-30)

Lokale Nachvollziehbarkeit; im Public-HTML stehen die Kriterien bewusst nicht.
Grundlage: Rubrik aus `2026-09-26-lehrplan-th-und-level-progression-plan.md`, Befunde aus
`../audit/audit-2026-09-19-mathepfade.md` (Zeilen 123-141). Lesart Kl. 12:
L4 = Verfahren selbst waehlen / Modell aus Text / Umkehraufgabe; L5 = zwei Verfahren
kombinieren, Parameter aus zwei Bedingungen, Fehler in vorgelegter Rechnung;
**L6 = Abi-Format** (mehrschrittig, Begruendungsanteil, Sachkontext; in den eA-Bloecken
mit Beweis- und Modellkritikanteil).
Jede Loesung mit Wolfram nachgerechnet; Bilder je geaenderter Aufgabe per `tests/bild.py`
angesehen. Jeder Block wurde von einem zweiten Agenten geprueft; Befunde und Behebung stehen
je Block unter "Review-Nachtrag".

Die fuenf Bloecke der Welle:

| Block | Trainer | Umfang |
|---|---|---|
| A Integralrechnung | 5 | bestimmtes Integral, Stammfunktionen, Flaechenberechnung, Rotationskoerper, **Ersatz** 12-lk-integral-uneigentlich -> Stetigkeit und Asymptoten (eA) |
| B1 Geometrie gA | 4 | Vektoren, Geraden im Raum, Ebenen, Skalarprodukt |
| B2 Geometrie eA | 4 | Abstaende, Lagebeziehungen, Schnittwinkel, **Ersatz** 12-lk-dgl -> Geraden- und Ebenenscharen (eA) |
| C1 Stochastik gA | 4 | Binomialverteilung, Sigma-Regeln, Zufallsgroessen, **Ersatz** 12-stoch-hypothesentests -> Prognoseintervalle |
| C2 Stochastik eA | 2 | Normalverteilung, **Ersatz** 12-lk-stoch-prozesse -> Konfidenzintervalle (eA) |

## Zwei Abgrenzungen, die diese Welle bestimmt haben

**Geometrie gA gegen eA.** Die vollstaendige Lagediskussion (inklusive windschief), Abstaende
und Schnittwinkel gehoeren nach eA; gA bleibt bei Vektorrechnung, Geradengleichung, Ebenenformen
und Skalarprodukt. Vier Aufgaben in `12-geraden-raum` wurden deshalb auf gA-Tiefe zurueckgezogen,
mehrere eA-Aufgaben umgebaut, die gA-Stoff wiederholten.

**Prognose- gegen Konfidenzintervall.** Ein Prognoseintervall schliesst von bekanntem p auf die
Haeufigkeit, ein Konfidenzintervall von der beobachteten Haeufigkeit h auf das unbekannte p.
Die beiden Ersatz-Trainer entstanden parallel in verschiedenen Bloecken; ihre Verwechslung ist
zugleich die vorgesehene Fehlersuchaufgabe im eA-Trainer. Der Sonderfall p = h = 0,5, in dem
beide Formeln zusammenfallen, wurde bewusst aufgeloest.

---

# Block A — Integralrechnung
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

### Abgrenzung der fünf Trainer gegeneinander

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

### 12-bestimmtes-integral

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
| 35 | 6 | **Review:** Zufluss gegen Abfluss, Zeitpunkt des größten Inhalts aus dem Vorzeichenwechsel der Netto-Rate, danach die Zunahme. Ersetzt den Bremsweg, der mit #31 dasselbe Muster hatte (linear fallende Rate, „Zeigen Sie, dass … versiegt/steht“, dann Integral von \(0\) bis \(T\)) |
| 36 | 6 | Integral als Funktion der oberen Grenze, Minimum dieser Funktion; Begründung des Vorzeichens |

Gate-Warnungen aus dem Bestand (#22, #35, MC-Länge) sind mit den neuen Stufen entfallen.

**Review-Nachtrag.** In den Altstufen nannten die Tipps von #3, #8, #10, #16 und #17 den
Lösungswert oder die fertige Gleichung; sie zeigen jetzt nur noch den Weg. Der Lösungsweg von
##15 bestand aus einer Formelzeile, obwohl die Aufgabe eine Deutung verlangt — die Deutung
(orientierter gegen absoluten Inhalt) steht jetzt dort. Bei #32 stand die Mittelwertformel im
Aufgabentext, was auf Stufe 6 verboten ist; gefragt ist jetzt der mittlere Funktionswert, die
Formel steht nur noch im Hinweis. Die vier Optionen von #33 waren nach dem immer gleichen
Muster gebaut („Sie trifft nur …“ ist nie richtig) und sind umformuliert.

### 12-stammfunktionen

Audit: KEIN_AFB3 L5 **und** L6; DUENNER_WEG (Stufen 2, 4). Stufen 5 und 6 neu.
Die alten Stufen 5/6 rechneten überwiegend bestimmte Integrale — das gehört zum
Nachbartrainer und ist entfallen.

| id | Level | Kriterium |
|---|---|---|
| 8, 9, 10 | 2 | DUENNER_WEG behoben: Lösungsweg zeigt Potenzregel bzw. Summenregel getrennt, mit Probe; die Aufgabentexte verlangen jetzt ausdrücklich das Bilden der Stammfunktion, nicht nur das Einsetzen. **Review:** die Tipps von #8 bis #12 nannten die fertige Gleichung und nennen jetzt nur den Weg |
| 15, 17 | 3 | **Review:** beide waren reines Einsetzen in eine vorgegebene Funktion (bei #17 sogar ein bestimmtes Integral, entgegen der eigenen Abgrenzung). Jetzt ist die Stammfunktion selbst zu bilden |
| 19–24 | 4 | **Review:** Stufe 4 war leichter als Stufe 3 — fünf von sechs MC-Abrufe einzelner Grundstammfunktionen, dabei #20/#24 praktisch gleich und #21/#22 einander verratend. Neu: Integrationskonstante aus einer Bedingung (#19, #22), Verfahrenswahl bei Logarithmus und e-Funktion (#20), Stammfunktion mit Bedingung im trigonometrischen Fall (#21), eine MC zur Verfahrenswahl (#23), Modell aus Sachtext (#24). Der MC-Anteil des Trainers sinkt damit von 23 auf 19 von 36 |
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

### 12-flaechenberechnung

Audit: KEIN_AFB3 L5 **und** L6. Stufen 5 und 6 neu; im **Review** kam Stufe 4 komplett dazu,
außerdem #9 (L2) und #17 (L3).

Im Altbestand stand der Wert \(10{,}\overline{6}\) viermal und \(1{,}\overline{3}\) fünfmal,
über die Stufen 2 bis 6 verteilt. Der erste Durchgang hat diese Wiederholungen **nur aus den
Stufen 5 und 6** entfernt — in den Altstufen standen sie weiter: #9, #14 und #24 liefen alle
auf \(\int (4-x^2)\,dx\) über \([-2;2]\) hinaus, #13, #17 und #22 alle auf \(1{,}\overline{3}\).
Seit dem Review bleibt von jedem Wert genau eine Aufgabe: \(10{,}\overline{6}\) nur noch bei
##14, \(1{,}\overline{3}\) nur noch bei #13.

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | **Review:** Schnittstellen selbst bestimmen (Parabel gegen Gerade), Lage durch Probe |
| 20 | 4 | **Review:** Umkehraufgabe — obere Grenze aus vorgegebenem Flächeninhalt |
| 21 | 4 | **Review:** Modell aus Sachtext (Grundstück), vorab Prüfung auf Vorzeichenwechsel |
| 22 | 4 | **Review:** Nullstellen durch Ausklammern, danach Fläche |
| 23 | 4 | **Review:** Schnittstellen aus \(x^3=x\), Einschränkung \(x \ge 0\) beachten |
| 24 | 4 | **Review:** Nullstellen einer nach unten geöffneten Parabel, Symmetrie ausgenutzt |
| 25 | 5 | **Review:** Fehler finden — es fehlt die untere Funktion. Falscher Weg \(7{,}5\), richtig \(4{,}5\). Zuvor war der Fehler „obere und untere vertauscht“; dessen Ergebnis \(-4{,}5\) ist der bloße Gegenwert, wer gewohnheitsmäßig den Betrag nimmt, landet trotzdem richtig |
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

### 12-lk-integral-rotationskoerper (eA)

Audit: KEIN_AFB3 L5 **und** L6; DUENNER_WEG (Stufe 6); Gate-Warnung `#31 (L6)` — der Tipp
nannte den Lösungswert 15. Stufen 5 und 6 neu; die Warnung ist damit behoben.

| id | Level | Kriterium |
|---|---|---|
| 14, 16 | 3 | **Review:** statt der Körperformeln für Halbkugel und Kegel (Stoff aus Kl. 8/9, der Tipp lieferte die Formel) jetzt zwei echte Rotationsansätze: linearer Rand mit Klammer-Stammfunktion, Kehrwert mit negativem Exponenten |
| 19 | 4 | **Review:** Modell aus Sachtext (Sektkelch); Volumen ausdrücklich mit dem Faktor \(\pi\) |
| 20 | 4 | **Review:** e-Funktion, Exponent verdoppelt sich beim Quadrieren |
| 21 | 4 | **Review:** \(\sin^2\) über die Formel mit doppeltem Argument; das Verfahren steht <b>nicht</b> im Aufgabentext |
| 22 | 4 | **Review:** Quadrat einer Summe ausmultiplizieren, Wurzel in Potenzschreibweise |
| 23 | 4 | **Review:** Umkehraufgabe — obere Grenze aus vorgegebenem Volumen |
| 24 | 4 | **Review:** Polynom quadrieren; der Graph liegt unterhalb der Achse, was das Volumen nicht berührt |
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

### 12-lk-integral-uneigentlich (eA) — **Ersatz-Trainer**

Alle 36 Aufgaben neu. Der Dateiname bleibt wegen der QR-Links, ebenso `THEMA_KEY`
(localStorage-Schlüssel — sonst verlieren Schülerinnen und Schüler ihren Fortschritt).
Geändert: `<title>`, `THEMA_CONFIG.name = 'Stetigkeit und Asymptoten (eA)'`, Kommentar in
Zeile 2. Das Wort „uneigentlich“ kommt im gesamten Inhalt nicht mehr vor; es steht nur noch
im unveränderlichen `THEMA_KEY` und im Dateinamen. Neuer Index-Text siehe unten.

Neues Thema: **Stetigkeit, Asymptoten, Periodizität** (TH 4.1 eA).

#### Abgrenzung gegen die Nachbartrainer

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
| 1 | 1 | Begriff Stetigkeit: Grenzwert gleich Funktionswert. **Review:** Optionen gekürzt, die richtige war die längste |
| 2 | 1 | Sprungstelle erkennen. **Review:** alle vier Optionen sind jetzt abschnittsweise erklärte Funktionen gleicher Bauart; vorher war die richtige die einzige mehrzeilige und im Bild sofort zu erkennen |
| 3 | 1 | Periode von \(\sin x\) |
| 4 | 1 | Waagerechte Näherungsgerade einer e-Funktion für \(x \to -\infty\). **Review:** Konstante geändert, weil die Aufgabe zuvor mit `10-polynomdivision` #16 in Term und Antwort übereinstimmte |
| 5 | 1 | Verhalten von \(e^{-x}\) für \(x \to \infty\) |
| 6 | 1 | Periode von \(\sin(2x)\), Wirkung des Faktors im Argument |
| 7 | 2 | **Review:** Anzahl voller Perioden über einem Intervall — ein Zwischenschritt mehr als die reine Formel \(p=\frac{2\pi}{b}\), die vorher dreimal (#7, #14, #18) abgefragt wurde |
| 8 | 2 | Periode mit gebrochenem Faktor; der Vorfaktor wirkt nicht auf die Periode |
| 9, 11 | 2 | Nahtstelle abschnittsweise erklärter Funktionen: beide Teilterme auswerten und vergleichen |
| 10, 12 | 2 | Waagerechte Näherungsgerade aus dem konstanten Summanden einer e-Funktion |
| 13 | 3 | Stetige Fortsetzung: Zähler faktorisieren, kürzen, Wert ergänzen |
| 14 | 3 | Periode trotz Vorfaktor und Verschiebung |
| 15 | 3 | Senkrechte Näherungsgerade: e-Zähler kann sich nicht kürzen. **Review:** Nenner geändert, zuvor deckungsgleich mit `10-polynomdivision` #9 |
| 16 | 3 | Betragsfunktion: stetig, aber nicht differenzierbar (Vorbereitung auf L5/L6) |
| 17 | 3 | **Review:** dreiteilig erklärte Funktion, Anzahl der Unstetigkeitsstellen — zwei Nahtstellen nacheinander zu prüfen. Vorher war die Aufgabe #4 (Stufe 1) mit anderer Konstante, also ein Stufen-Kollaps L1/L3 |
| 18 | 3 | Periode von \(\cos(\pi x)\), Kreiszahl kürzt sich |
| 19, 20 | 4 | Parameter für stetigen Anschluss; zuerst die Seite ohne Parameter auswerten. **Review:** beide waren dieselbe Aufgabe mit derselben Lösung (nur einmal der linke, einmal der rechte Ast mit Parameter). #19 hat jetzt einen anderen Zielwert, #20 einen Wurzelast, bei dem vor dem Gleichsetzen die Wurzel zu ziehen ist |
| 21 | 4 | Umkehraufgabe: Faktor im Argument aus vorgegebener Periode |
| 22 | 4 | Verhalten von \(e^{-x^2}\) nach beiden Seiten; Quadrat im Exponenten |
| 23 | 4 | **Review:** statt der Wertetabelle (die mit `10-polynomdivision` #19 dieselbe Stufe und dasselbe Format belegte) jetzt Erweitern auf den bekannten Grenzwert \(\frac{\sin u}{u}\) |
| 24 | 4 | Parameter aus dem Achsenschnittpunkt; die Angabe zur Näherungsgeraden ist bereits erfüllt |
| 25, 29 | 5 | **Zwei Bedingungen: stetig und differenzierbar.** Wertegleichung und Steigungsgleichung; bei #25 ist der lineare Ast gerade die Tangente, bei #29 führt die Steigungsbedingung zuerst zum Ziel |
| 26 | 5 | **Review:** Amplitude und Mittellinie aus größtem und kleinstem Wert; die Angabe zur Periode wird für die Antwort nicht gebraucht. Vorher stand hier eine dritte Aufgabe vom Typ „stetig und differenzierbar“ |
| 27 | 5 | **Fehler in einer Asymptoten-Begründung. Review:** vorher \(2+e^{-x}\) — das beantworteten schon #5 (L1) und #12 (L2), AFB III war nicht erreicht. Jetzt \(\frac{3e^{x}}{e^{x}+2}\): der Quotient zweier unbeschränkt wachsender Terme, erst das Kürzen durch \(e^{x}\) zeigt die Gerade \(y=3\) |
| 28 | 5 | Fehler: Stetigkeit an einer Stelle behauptet, die nicht zum Definitionsbereich gehört. **Review:** der Lösungsweg lieferte die Begründung von #36 wörtlich vorweg und endet jetzt bei der Definitionsbereichsfrage |
| 30 | 5 | Parameter, für den eine stetige Fortsetzung überhaupt möglich ist (Zähler muss mitverschwinden). **Review:** e-Term statt Polynom, weil die Aufgabe zuvor `11-lk-gebrochen-rational` #25 bis auf die Zahlen entsprach |
| 31 | 6 | Behauptung prüfen: aus Differenzierbarkeit folgt Stetigkeit, die Umkehrung nicht. **Review:** Distraktoren umgebaut (siehe unten) |
| 32 | 6 | **Review:** Abi-Format mit Sachkontext (Abbau eines Medikaments): Grenzverhalten begründen, danach Exponentialgleichung mit Logarithmus. Vorher ein reines \(2 \times 2\)-Gleichungssystem ohne Kontext — inhaltlich richtig, aber kein Abi-Format, und der dritte Aufguss von #25/#29 |
| 33 | 6 | Behauptung prüfen: periodisch und waagerechte Näherungsgerade schließen einander aus |
| 34 | 6 | Abi-Format mit Sachkontext (Tide): Schranken aus dem Wertebereich des Sinus, Periode als Dauer |
| 35 | 6 | Abi-Format eA: dritte binomische Formel mit \(e^{2x}=\left(e^{x}\right)^2\), stetige Fortsetzung |
| 36 | 6 | Behauptung prüfen: überall stetige Funktion auf \(\mathbb{R}\) hat keine senkrechte Näherungsgerade; das naheliegende Gegenbeispiel taugt nicht |

#### Nachzutragen in `index.html` (bewusst nicht von diesem Agenten geändert)

Zeile 947, `<span class="theme-name">`: statt „Uneigentliche Integrale“ neu

```
Stetigkeit &amp; Asymptoten
```

---

### Gefundene und behobene Fehler während der Umsetzung

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

#### Aus dem Review des zweiten Agenten (2026-09-30)

Rechnerisch war nichts zu beanstanden — alle neuen Werte, Nahtstellen, einseitigen Ableitungen,
Perioden und Grenzwerte hielten der Nachprüfung stand, und alle zehn Fehlersuchaufgaben enden
nachweislich falsch. Die Befunde lagen fast vollständig in den **Altstufen 2 bis 4**, die beim
ersten Durchgang mitgenommen, aber nicht geprüft worden waren:

- **Wiederholte Werte in den Altstufen** (`12-flaechenberechnung`): dreimal \(10{,}\overline{6}\),
  dreimal \(1{,}\overline{3}\). Behoben; die Kriterien-Datei behauptete zudem, diese
  Wiederholungen seien bereits verschwunden — das galt nur für die Stufen 5 und 6 und ist
  oben richtiggestellt.
- **Stufe 4 war kein AFB II** (`12-flaechenberechnung`, `12-lk-integral-rotationskoerper`,
  `12-stammfunktionen`): Formelabfragen, mitgelieferte Schnittstellen, reine Nullstellen-
  Teilaufgaben, sechsmal derselbe Stamm. Alle drei Stufen neu geschrieben.
- **Aufgaben, die einander verrieten:** `12-flaechenberechnung` #21 lieferte die Grenzen von
  #22 und #23 die von #24; `12-stammfunktionen` #21 und #22 verrieten einander;
  Ersatz-Trainer #19 und #20 waren dieselbe Aufgabe mit derselben Lösung.
- **Verfahren im Aufgabentext genannt** (`12-lk-integral-rotationskoerper` #22, #24: „mit
  partieller Integration“) — auf Stufe 4 verboten; das Gate erkennt diese Formulierung nicht.
  Die Aufgaben sind ersetzt.
- **Körperformeln statt Rotationsansatz** (`12-lk-integral-rotationskoerper` #14, #16): Stoff
  aus Kl. 8/9, der Tipp lieferte die Formel. Ersetzt.
- **Tipps mit Lösungswert oder fertiger Gleichung**, systematisch in den Altstufen: insgesamt
  24 Stellen in allen vier Bestandstrainern. Das Gate greift erst ab Betrag 10 und nur bei
  Dezimalzahlen, Brüche und \(\pi\)-Terme rutschen durch. Alle Tipps nennen jetzt den Weg.
- **Formel im Aufgabentext auf Stufe 6** (`12-bestimmtes-integral` #32, Mittelwertformel).
- **Zwei Stufe-6-Aufgaben mit demselben Muster** (`12-bestimmtes-integral` #31 und #35).
- **Stufen-Kollaps im Ersatz-Trainer** (#17 war #4 mit anderer Konstante) und dreimal
  dieselbe Periodenformel ohne Zwischenschritt.
- **Ratbarer Optionssatz:** „Sie trifft nur für ganzrationale Funktionen zu“ und
  „Sie trifft nur zu, wenn …“ standen achtmal über den Block verteilt und waren **nie**
  richtig. Die Distraktorformen sind jetzt variiert („Zutreffend …“, „Widerlegt …“,
  „Nur mit dem Zusatz …“), und bei `12-flaechenberechnung` #32 ist die Einschränkungsoption
  die **richtige** — dort wird die Behauptung erst mit dem Zusatz wahr.
- **Fehlersuchaufgabe mit rettbarem Fehler** (`12-flaechenberechnung` #25): der falsche Weg
  lieferte den bloßen Gegenwert, wer gewohnheitsmäßig den Betrag nimmt, landete richtig.
  Jetzt fehlt im vorgelegten Ansatz die untere Funktion, das Ergebnis ist \(7{,}5\) statt
  \(4{,}5\).
- Kleinere Punkte: verunglückter Satz in `12-bestimmtes-integral` #33, Formelzeile als
  Lösungsweg bei #15, zwei Stammfunktions-Aufgaben, die reines Einsetzen waren, eine
  Nachkommastellen-Angabe, die nicht zur gespeicherten Toleranz passte, und die gemischte
  Anrede im Ersatz-Trainer (jetzt: Stufe 1–5 duzen, Stufe 6 siezen).

### Offen

- **KOLLAPS L2/L3 in `12-bestimmtes-integral`** bleibt bestehen: die Stufen 1–3 werden
  planmäßig nur entdoppelt und ausformuliert, nicht neu geschrieben. Stufe 3 unterscheidet
  sich von Stufe 2 jetzt durch Trigonometrie, e-Funktion und Kehrwert, die Messgröße des
  Audits (Textlänge) dürfte das aber weiterhin als Kollaps ausweisen.
- `12-stammfunktionen` hat auch nach dem Review noch 19 MC-Aufgaben von 36; der Schwerpunkt
  liegt in den Stufen 1 bis 3, die planmäßig nicht neu geschrieben werden.
- Das Level-Gate erkennt drei der Review-Befunde nicht: ein im Aufgabentext genanntes
  Verfahren („mit partieller Integration“), einen Tipp, der einen Bruch oder \(\pi\)-Term als
  Lösung nennt, und eine Formel, die auf Stufe 5/6 im Aufgabentext mitgeliefert wird. Die
  Erweiterung des Tipp-Gates hat der Koordinator angekündigt; die beiden anderen bleiben
  vorerst Sache der Durchsicht.
- `index.html` ist nicht angefasst (vier Ersatz-Trainer der Welle brauchen die Datei
  gleichzeitig); der neue `theme-name`-Text steht oben.

---

# Block B1 — Analytische Geometrie (gA)
Welle Task 9, Stand 2026-09-30. Lokale Nachvollziehbarkeit; im Public-HTML stehen die
Kriterien bewusst nicht.

Grundlage: Rubrik aus `2026-09-26-lehrplan-th-und-level-progression-plan.md`, Befunde aus
`../audit/audit-2026-09-19-mathepfade.md` (Zeilen 123–141), Werkzeug- und Gate-Hinweise aus
`2026-09-26-STAND.md`. Muster der Darstellung: `2026-09-26-kl11-kriterien.md`.

Lesart Klasse 12 (gA) durchgängig:

- **L4 (AFB II)**: Verfahren selbst wählen, Modell aus einem Sachtext, Umkehraufgabe.
- **L5 (AFB III)**: zwei Verfahren verzahnen, Parameter aus zwei Bedingungen, Fehler in einer
  vorgelegten Rechnung finden. Bei jeder Fehlersuchaufgabe wurde geprüft, dass der vorgeführte
  falsche Weg auch wirklich auf ein **falsches** Ergebnis führt (Lehre aus Kl. 11).
- **L6 (AFB III, Abi-Format gA)**: mehrschrittig, mit Begründungsanteil („Zeigen Sie …“,
  „Beurteilen Sie …“), Sachkontext (Dach, Flugbahn, Sichtlinie, Rampe, Schatten), Fallunterscheidung
  oder Randfallprüfung.

Jede Zahl wurde mit dem Wolfram-MCP nachgerechnet, einschließlich der jeweils **nicht** gefragten
Fälle (bei Lagebeziehungen wurde zwischen parallel, schneidend, windschief und identisch
unterschieden; bei quadratischen Parameterbedingungen wurden beide Lösungen geprüft).
Bilder der geänderten Aufgaben mit `tests/bild.py --aufgabe <id>` erzeugt und angesehen:
Spaltenvektoren erscheinen als Matrizen, kein abgeschnittener Text, MC-Optionen vollständig.

### Abgrenzung der vier Trainer gegeneinander und gegen den eA-Block

| Trainer | Inhalt |
|---|---|
| 12-vektoren-grundlagen | Vektorbegriff, Rechnen mit Vektoren, Betrag, Linearkombination, Kollinearität, Mittel- und Teilpunkte, Schwerpunkt |
| 12-geraden-raum | Geradengleichung aufstellen, Punktprobe, Schnittpunkt, Lage zweier Geraden in gA-Tiefe (parallel / identisch / schneidend), Spurpunkte |
| 12-ebenen | Parameter-, Normalen- und Koordinatenform, Umwandlung zwischen ihnen, Lage Gerade/Ebene, Lage zweier Ebenen |
| 12-skalarprodukt | Skalarprodukt, Orthogonalität, Winkel zwischen Vektoren, Projektionslänge |

Abstände (Punkt–Ebene, Punkt–Gerade, windschiefe Geraden), Schnittwinkel von Gerade und Ebene und
die vollständige Lagediskussion mit Parameterscharen gehören in die eA-Trainer
`12-lk-geom-abstaende`, `12-lk-geom-lagebeziehungen`, `12-lk-geom-schnittwinkel` und bleiben hier
außen vor. Deshalb sind in `12-ebenen` die alten Abstandsaufgaben der Stufen 5 und 6 (Hesse-Form,
Abstand paralleler Ebenen) mit dem neuen Block entfallen. Auch die vollständige Lagediskussion mit
windschiefen Geraden gehört nach dem Review nicht mehr in `12-geraden-raum`: dort wird windschief
allenfalls festgestellt, nicht zum Ziel der Aufgabe gemacht.

---

### 12-vektoren-grundlagen

Audit: KEIN_AFB3 L5 **und** L6; KOLLAPS L5/L6; DUENNER_WEG (Stufe 3).
Stufe 5 und 6 vollständig neu (id 25–36). Stufe 4 blieb inhaltlich (kein KOLLAPS L3/L4 oder L4/L5),
nur die MC-Längen in #22 wurden angeglichen.

| id | Level | Kriterium |
|---|---|---|
| 22 | 4 | Gate-Warnung behoben: richtige Option gekürzt, Distraktoren angeglichen (Inhalt unverändert) |
| 25 | 5 | Linearkombination: zwei Faktoren aus zwei Zeilen, dritte Zeile als Existenzkontrolle |
| 26 | 5 | Kollinearität mit **zwei** Unbekannten — Faktor erst aus der Zeile ohne Unbekannte |
| 27 | 5 | Parameter aus einer Längenbedingung (gleichseitiges Dreieck); Symmetrieargument für die dritte Seite |
| 28 | 5 | Fehlersuche: „Beträge addieren“. Falscher Weg 7, richtig 5 — der falsche Weg endet nachweislich falsch |
| 29 | 5 | Darstellbarkeit als Linearkombination: Parameter so, dass das System gerade noch lösbar ist |
| 30 | 5 | Teilpunkt einer Strecke aus einem Längenverhältnis (Umkehr der Mittelpunktsformel) |
| 31 | 6 | Abi-Format, Zeltdach: vier Kantenvektoren bilden, Gleichheit der Beträge **begründen**, Länge angeben |
| 32 | 6 | Abi-Format, Drohne: Betrag des Geschwindigkeitsvektors, dann Weg; Kontrolle über den Ortsvektor |
| 33 | 6 | Behauptung prüfen: Eindeutigkeit des Einheitsvektors; Gegenvektor als Abgrenzung (MC, Auswahl ist die Leistung) |
| 34 | 6 | Abi-Format, Fensterrahmen: vierte Ecke konstruieren, dann Umfang — zwei Schritte mit Nachweis |
| 35 | 6 | Fallunterscheidung: kollinear für \(k = 2\) und \(k = -2\), beide Fälle im Lösungsweg gedeutet |
| 36 | 6 | Abi-Format, Sensoren: Schwerpunkt als Mittel der Ortsvektoren, danach Abstand zu einer Ecke |

### 12-geraden-raum

Audit: KEIN_AFB3 L5 **und** L6; KOLLAPS L5/L6. Stufe 5 und 6 vollständig neu (id 25–36).
Gate-Warnungen #29 und #32 sind mit dem neuen Block entfallen.

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | Schnittpunkt: zwei Zeilen bestimmen die Parameter, die dritte ist die Probe (ohne sie keine Aussage) |
| 26 | 5 | Fehlersuche: unvollständige Punktprobe (nur zwei Zeilen geprüft). Der falsche Schluss ist nachweislich falsch, \(P\) liegt nicht auf \(g\) |
| 27 | 5 | Spurpunkt mit der \(xy\)-Ebene: Parameter aus der vorgegebenen ersten Koordinate, dann Aufpunkt-Parameter aus der Spurbedingung |
| 28 | 5 | Identität nachweisen: kollineare Richtungen **und** Punktprobe — zwei Bedingungen |
| 29 | 5 | Gerade aus zwei Punkten aufstellen und fehlende Koordinate eines Geradenpunkts bestimmen |
| 30 | 5 | Punkt in vorgegebenem Abstand vom Aufpunkt: Betrag des Richtungsvektors als Maßstab des Parameters |
| 31 | 6 | Abi-Format, Flugbahnen: Kreuzungspunkt **und** Zeitvergleich \(t = s\) als Begründung der Kollisionsgefahr |
| 32 | 6 | Abi-Format, Kranhaken: vollständige Punktprobe als Nachweis (alle drei Zeilen), danach Weglänge über den Betrag des Richtungsvektors |
| 33 | 6 | Abi-Format, Sichtlinie und Traverse: Schnitt **plus** Randbedingung \(0 \le u \le 1\) — ohne sie kein gesicherter Treffer |
| 34 | 6 | Spurpunkt mit Fallunterscheidung: gesuchter Wert \(a = -1\); für \(a = 0\) verläuft \(g\) parallel zur \(xy\)-Ebene und hat gar keinen Spurpunkt |
| 35 | 6 | Abi-Format, Straßenkreuzung: beide Geraden selbst aufstellen, dann Schnittpunkt |
| 36 | 6 | Behauptung prüfen: dieselbe Gerade hat unendlich viele Parametergleichungen (Aufpunkt und Vielfache der Richtung frei) |

### 12-ebenen

Audit: KEIN_AFB3 L5 **und** L6; DUENNER_WEG (Stufen 2, 3). Stufe 5 und 6 vollständig neu (id 25–36);
Stufe 4 inhaltlich unverändert, nur MC-Längen in #19, #21 und #24 angeglichen (Gate-Warnungen).
Die Abstandsaufgaben der alten Stufen 5/6 sind entfallen (gehören in den eA-Block).

| id | Level | Kriterium |
|---|---|---|
| 19, 21, 24 | 4 | Gate-Warnungen behoben: Distraktoren auf die Länge der richtigen Option gebracht, Inhalt unverändert |
| 25 | 5 | Parameterform → Koordinatenform: Normalenvektor aus zwei Orthogonalitätsbedingungen, Aufpunkt für \(d\) |
| 26 | 5 | Drei Achsenschnittpunkte → Koordinatenform, danach Punktprobe mit Parameter |
| 27 | 5 | Echt parallel: zwei Bedingungen (\(\vec u \cdot \vec n = 0\) **und** Aufpunkt nicht in \(E\)) |
| 28 | 5 | Fehlersuche: Vorzeichen von \(-y\) beim Einsetzen. Falscher Weg liefert \(t = 0{,}5\), richtig \(t = 1\) — Probe zeigt den Unterschied |
| 29 | 5 | Ebene aus Gerade und Punkt: Richtung legt \(b\) fest, zwei Punkte legen \(d\) und \(c\) fest |
| 30 | 5 | Zwei Ebenen: kollineare Normalen **und** verschiedene rechte Seiten — echt parallel statt identisch |
| 31 | 6 | Abi-Format, Pultdach: Ebene aus drei Ecken, vierte Ecke per Punktprobe — Ebenheit wird bewiesen, nicht behauptet |
| 32 | 6 | Behauptung prüfen: fehlendes \(z\) bedeutet parallel zur \(z\)-Achse; \(d = 0\) unterscheidet „enthält“ von „echt parallel“ |
| 33 | 6 | Abi-Format, Drohne trifft Hangebene: Gerade in Koordinatenform einsetzen, Höhe ablesen |
| 34 | 6 | Gerade ganz in \(E\), von der anderen Seite her: Aufpunkt ist nachzuweisen, gesucht ist der Parameter in der **Richtung** (Sachkontext Förderband) |
| 35 | 6 | Abi-Format, Schattenwurf: Strahl als Gerade modellieren, Schnitt mit der Panelebene |
| 36 | 6 | Abi-Format, Entwässerungsgraben: Schnittgerade zweier Ebenen durch Addition/Subtraktion, freie \(y\)-Koordinate gedeutet |

### 12-skalarprodukt

Audit: KEIN_AFB3 L5 **und** L6. Stufe 5 und 6 vollständig neu (id 25–36);
Gate-Warnung #25 ist mit dem neuen Block entfallen.

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | Vektor aus zwei Bedingungen: Orthogonalität **und** Betrag; zweite Lösung als Gegenvektor gedeutet |
| 26 | 5 | Fehlersuche: Summe statt Produkt der Beträge im Nenner. Falscher Weg \(48{,}2^\circ\), richtig \(63{,}6^\circ\) |
| 27 | 5 | \(\lvert\vec a - \vec b\rvert\) allein aus Beträgen und Skalarprodukt — die Vektoren selbst sind unbekannt |
| 28 | 5 | Orthogonal zu zwei Vektoren: lineares System aus zwei Skalarproduktbedingungen |
| 29 | 5 | Größter Innenwinkel: mehrere Winkel berechnen und vergleichen, Winkelsumme als Kontrolle |
| 30 | 5 | Projektionslänge auf einen Vektor, der keine Achsenrichtung ist (Stufe 4 hatte den Achsenfall) |
| 31 | 6 | Abi-Format, Rampe: Neigung gegen die Waagerechte über den waagerechten Anteil, Vorgabe beurteilen |
| 32 | 6 | Abi-Format, Dachfläche: Parallelogramm zeigen, Rechtwinkligkeit über das Skalarprodukt, dann Flächeninhalt |
| 33 | 6 | Behauptung prüfen: Kürzen beim Skalarprodukt; Gegenbeispiel im Lösungsweg |
| 34 | 6 | Fallunterscheidung: quadratische Orthogonalitätsbedingung mit \(k = \pm 2\), beide Lösungen geprüft |
| 35 | 6 | Abi-Format, Arbeit im Sachkontext: Wert berechnen **und** beurteilen, welcher Kraftanteil nichts beiträgt |
| 36 | 6 | Abi-Format, Messpunkte: Rechtwinkligkeit beurteilen (sie liegt **nicht** vor) und Winkel angeben |

---

### Gate-Ergebnisse

```
python tests/level_check.py --strict trainer/12-vektoren-grundlagen.html trainer/12-geraden-raum.html \
    trainer/12-ebenen.html trainer/12-skalarprodukt.html      -> Exit 0, 0 Fehler, 0 Warnungen
python tests/lehrplan_check.py --strict <dieselben>           -> Exit 0, 0 Befunde
python tests/katex_check.py <dieselben>                       -> 4x ok
python -m pytest tests/test_trainer.py -k "<die vier Stems>"  -> 28 passed
```

Sichtprüfung per `tests/bild.py --aufgabe <id>` für Aufgaben 25, 26, 28, 31, 32, 33, 34, 35 in den
betroffenen Trainern: Spaltenvektoren als Matrix gesetzt, Brüche und Gradzeichen korrekt, MC-Optionen
vollständig und gemischt (keine Buchstabenverweise im Lösungsweg).

### Offen

- Stufe 1–3 wurde planmäßig nicht neu geschrieben. `12-vektoren-grundlagen` behält den
  DUENNER_WEG-Befund auf Stufe 3, `12-ebenen` auf den Stufen 2 und 3 (kurze Lösungswege im Bestand).
- `12-ebenen` nutzt auf Stufe 4 (#26) weiterhin das Kreuzprodukt zur Normalenbestimmung. In den neuen
  Aufgaben wird der Normalenvektor stattdessen über Orthogonalitätsbedingungen gewonnen, was zur
  gA-Tiefe besser passt; die Altaufgabe blieb unangetastet.
- `12-skalarprodukt` #30 (Projektionslänge) ist im TH-Kanon für gA nicht ausdrücklich genannt.
  Die Aufgabe bleibt bewusst stehen: die Projektionslänge ist hier reine Rechentechnik aus
  Skalarprodukt und Betrag, sie wird nirgends zu einem Abstandsverfahren ausgebaut (das bleibt eA),
  und sie macht anschaulich, was das Skalarprodukt geometrisch misst. Auf Stufe 4 steht bereits der
  einfache Achsenfall, #30 ist dessen Fortsetzung.

### Review-Nachtrag (2026-09-30)

Der Prüf-Agent hat Geometrie gA und eA gemeinsam geprüft. **Kein Rechenfehler** in den vier
Trainern; alle drei Fehlersuchaufgaben enden nachweislich falsch; Spaltenvektoren im Bild
durchgehend als Matrix. Behoben wurden Abgrenzungs- und Kontextbefunde:

| Fundstelle | Befund | Behebung |
|---|---|---|
| `12-geraden-raum` #27, #32, #34, #36 | vollständige Lagediskussion inklusive windschief — das ist eA (`12-lk-geom-lagebeziehungen` #28/#29) | alle vier zurückgezogen und durch gA-Aufgaben ersetzt: #27 Spurpunkt mit Parameter aus zwei Bedingungen, #32 Abi-Format Kranhaken (vollständige Punktprobe als Nachweis, dann Weglänge), #34 Spurpunkt-Fallunterscheidung (kein Spurpunkt für \(a = 0\)), #36 Behauptung zur Vieldeutigkeit der Parameterform |
| `12-ebenen` #34 | „Für welchen Parameter liegt \(g\) ganz in \(E\)“ stand dreifach im Block | umakzentuiert: der **Aufpunkt** ist jetzt gegeben und nachzuweisen, gesucht ist der Parameter in der **Richtung**; dazu Sachkontext Förderband |
| `12-ebenen` #36 | Satteldach-Kontext und Gleichungspaar zu nah an zwei eA-Aufgaben; Dachkontext im Block fünffach | Kontext auf Entwässerungsgraben gewechselt, Gleichungen \(2x+z = 14\) / \(-2x+z = 2\), Schnittgerade in der Höhe \(z = 8\) |
| `12-vektoren-grundlagen` #6, `12-skalarprodukt` #19 | deutsche Anführung unten mit geradem `"` geschlossen (die Falle, die anderswo einen JS-String beendet hat) | auf `“` umgestellt |
| alle vier Trainer | Stufenkommentare (`// LEVEL 5 -- Spurpunkte` usw.) passten nicht mehr zum Inhalt | nachgezogen für Stufe 5 und 6 |

Die Zeltdach-Aufgabe `12-vektoren-grundlagen` #31 bleibt unverändert; das gleichlautende eA-Pendant
wird dort ersetzt. Die neuen Werte wurden erneut mit Wolfram nachgerechnet (\(a = -2\); \(t = 4\) und
\(4\sqrt{26} \approx 20{,}40\); \(a = -1\) mit Sonderfall \(a = 0\); \(a = 1\) bei erfülltem Aufpunkt;
\(z = 8\), \(x = 3\)).

---

# Block B2 — Analytische Geometrie (eA)
Welle Task 9, Stand 2026-09-30. Lokale Nachvollziehbarkeit; im Public-HTML stehen die
Kriterien bewusst nicht.

Grundlage: Rubrik aus `2026-09-26-lehrplan-th-und-level-progression-plan.md`, Befunde aus
`../audit/audit-2026-09-19-mathepfade.md` (Zeilen 123–141). Lesart Kl. 12 eA:

- **L4 (AFB II)**: Verfahren selbst wählen, Modell aus einem Sachtext aufstellen, Umkehraufgabe
  (Parameter oder Stelle gesucht statt Ergebniswert). Das Verfahren wird im Text **nicht** genannt.
- **L5 (AFB III)**: zwei Verfahren kombinieren, Parameter aus zwei Bedingungen, Fehler in einer
  vorgelegten Lage- oder Abstandsbestimmung finden.
- **L6 (AFB III, Abi-Format eA)**: mehrschrittig, mit Begründungs- bzw. Beweisanteil
  („Zeigen Sie …“, „Begründen Sie …“, „Beurteilen Sie …“), Sachkontext, Parameter,
  Fallunterscheidung oder Grenzfall.

Jede Lösung mit dem Wolfram-MCP nachgerechnet — bei Lagebeziehungen ausdrücklich alle vier Fälle
(parallel / schneidend / windschief / identisch), bei den Scharen zusätzlich die Grenzfälle des
Parameters. Bilder je Trainer und Stufe mit `tests/bild.py --aufgabe <id>` erzeugt und angesehen.

### Abgrenzung der vier Trainer gegeneinander

| Trainer | Inhalt |
|---|---|
| 12-lk-geom-abstaende | Abstände: Punkt–Punkt, Punkt–Ebene (HNF), Punkt–Gerade (Lotfuß und Kreuzprodukt), parallele Geraden und Ebenen, windschiefe Geraden |
| 12-lk-geom-lagebeziehungen | vollständige Lagediskussion Gerade–Gerade, Gerade–Ebene, Ebene–Ebene, Schnittgerade, drei Ebenen |
| 12-lk-geom-schnittwinkel | Winkel: Vektor–Vektor, Gerade–Gerade, Gerade–Ebene (Sinusformel), Ebene–Ebene |
| 12-lk-dgl (**Ersatz**) | Geraden- und Ebenenscharen im Raum (TH 4.2 eA) |

Gegen die gA-Trainer des Parallelblocks (`12-vektoren-grundlagen`, `12-geraden-raum`, `12-ebenen`,
`12-skalarprodukt`) grenzt sich Block B2 durch die eA-Tiefe ab: dort die Grundlagen, hier
Parameter, Fallunterscheidung und Beweisanteil. Gegen `11-lk-funktionsscharen` grenzt sich der
Ersatz-Trainer dadurch ab, dass dort Funktionsscharen in der Analysis stehen, hier Scharen von
Geraden und Ebenen **im Raum**.

---

### 12-lk-geom-abstaende

Audit: KEIN_AFB3 L5; **KOLLAPS L3/L4**; DUENNER_WEG (Stufe 2). Wegen des Kollapses ist auch
Stufe 4 neu geschrieben: Sie bestand vorher aus denselben Standardrechnungen wie Stufe 3, nur mit
anderer Formel. Jetzt steht in Stufe 4 durchgehend eine Entscheidung (Verfahren wählen,
Sachmodell, Umkehraufgabe). Die Gate-Warnungen `#25` und `#28` (richtige MC-Option deutlich
länger) sind mit den Aufgaben entfallen.

| id | Level | Kriterium |
|---|---|---|
| 7, 11, 12 | 2 | DUENNER_WEG behoben: Lösungsweg zeigt Verbindungsvektor, Betragsbildung und Deutung getrennt |
| 19 | 4 | Lotfußpunkt über die Senkrechtbedingung, ohne dass das Verfahren genannt wird |
| 20 | 4 | Umkehraufgabe: Koordinate eines Punktes aus vorgegebenem Abstand zu einer Geraden, Vorzeichenfall \(\pm 4\) |
| 21 | 4 | Modell aus Sachtext (Rohrleitung); der Lotfußpunkt ist ohne Formel ablesbar |
| 22 | 4 | Verfahren wählen: welcher Arbeitsschritt bei einer nur durch drei Punkte gegebenen Ebene zuerst nötig ist (MC) |
| 23 | 4 | Abstand zweier **paralleler Geraden** — Kollinearität erkennen, dann auf Punkt–Gerade zurückführen |
| 24 | 4 | Abstand zweier paralleler Ebenen über einen bequem gewählten Punkt |
| 25 | 5 | zwei Schritte: Windschiefe nachweisen, dann Abstand über das Spatprodukt |
| 26 | 5 | **Fehlersuche**: Aufpunktabstand \(5\) statt Lotabstand \(4\) — der falsche Weg endet nachweislich falsch (MC) |
| 27 | 5 | Parameter aus zwei Bedingungen: Punkt auf einer Geraden **und** vorgegebener Abstand zu einer Ebene; beide Lösungen (\(r=0\) und \(r=12\)) diskutiert |
| 28 | 5 | zwei Verfahren: Parallelität von Gerade und Ebene nachweisen, dann Abstand über einen Geradenpunkt |
| 29 | 5 | Gerade nur durch zwei Punkte gegeben — Richtungsvektor selbst bilden, dann Kreuzproduktformel |
| 30 | 5 | Umkehraufgabe mit Parameter: Abstand als Term in \(c\), Lösung \(3\sqrt3\); Grenzfall \(c=0\) benannt |
| 31 | 6 | Abi-Format: „Zeigen Sie, dass alle vier Dachkanten gleich lang sind“ + Abstand Spitze–Grundkante, Sachkontext |
| 32 | 6 | Abi-Format: Windschiefe **begründen** und Mindestabstand zweier Trassen bestimmen, Deutung des Ergebnisses |
| 33 | 6 | Parameter im Normalenvektor; nur \(a^2\) geht ein, beide Lösungen \(\pm 1\) diskutiert |
| 34 | 6 | Behauptung prüfen: Abstand \(0\) lässt schneidend **und** identisch zu (MC) |
| 35 | 6 | Punkte auf einer Geraden mit vorgegebenem Abstand zu einer Ebene, zwei Lösungen auf verschiedenen Seiten |
| 36 | 6 | Grenzfall-Einsicht: der Parameter fällt heraus, weil die Gerade parallel zur Ebene liegt — Abstand konstant \(\sqrt6\) |

### 12-lk-geom-lagebeziehungen

Audit: KEIN_AFB3 L5 **und** L6; DUENNER_WEG (Stufe 4). Stufe 5 und 6 sind komplett neu; in
Stufe 4 sind die drei dünnsten Lösungswege (`#19`, `#20`, `#22`) ausgeschrieben worden.
Gate-Warnungen `#29` und `#35` mit den Aufgaben entfallen.

**Pflicht-Fix:** Im alten `#36` stand „Abi-LK:“ im Aufgabentext. Thüringen kennt keinen
Leistungskurs; die neue Aufgabe `#36` trägt „Abi eA:“. `grep -n "Abi-LK"` liefert jetzt nichts.

| id | Level | Kriterium |
|---|---|---|
| 19, 20, 22 | 4 | DUENNER_WEG behoben: Lösungsweg zeigt das Gleichungssystem, den Rechenschritt und die Probe |
| 25 | 5 | Parameter aus zwei Bedingungen: Aufpunkt in \(E\) **und** Richtung parallel zu \(E\) |
| 26 | 5 | **Fehlersuche**: aus \(\vec u \cdot \vec n = 0\) wird voreilig „echt parallel“ geschlossen; die Punktprobe zeigt, dass \(g\) in \(E\) liegt (MC) |
| 27 | 5 | identische Ebenen: erst den Streckfaktor aus den rechten Seiten, dann den Parameter |
| 28 | 5 | Schnitt zweier Geraden: System aufstellen, zwei Zeilen lösen, dritte als Probe — Abgrenzung gegen windschief |
| 29 | 5 | Parameter so bestimmen, dass sich zwei Geraden schneiden; sonst windschief |
| 30 | 5 | drei Ebenen, \(3\times3\)-System, Eindeutigkeit begründet (Gegenfall „gemeinsame Gerade“ benannt) |
| 31 | 6 | Abi-Format Sachkontext: Existenz der Schnittgeraden begründen, Firsthöhe bestimmen |
| 32 | 6 | Abi-Format: Ebene aus drei Spurpunkten über die Achsenabschnittsform, Schnitt nachweisen, Parameter bestimmen |
| 33 | 6 | Behauptung prüfen: senkrechte Normalen schließen einen Schnitt gerade **nicht** aus (MC) |
| 34 | 6 | Schnittgerade zweier Ebenen liegt in einer dritten — die Einsicht ist, dass der Term von \(t\) unabhängig wird |
| 35 | 6 | Lage dreier Ebenen ohne gemeinsamen Punkt (Prismenlage) — Fallunterscheidung als MC |
| 36 | 6 | **Abi eA** (ersetzt „Abi-LK“): Sachkontext Laserstrahl, Treffer nachweisen, Auftreffhöhe, Vorzeichen von \(t\) gedeutet |

### 12-lk-geom-schnittwinkel

Audit: KEIN_AFB3 L5 **und** L6; **KOLLAPS L2/L3 und L3/L4**; DUENNER_WEG (Stufen 2, 3).
Deshalb sind hier die **Stufen 3 bis 6** neu geschrieben, dazu die beiden dünnsten Lösungswege
der Stufe 2 (`#7`, `#12`). Die Gate-Warnung `#24` ist mit der Aufgabe entfallen.

Der Doppelkollaps hatte eine klare Ursache: Stufe 2 und Stufe 3 stellten dieselbe Aufgabe
(„Winkel zweier Vektoren“), nur unter anderer Überschrift, und Stufe 4 wiederholte die
Sinusformel mit Zahlen, die meist \(0°\) oder \(90°\) ergaben. Der neue Schnitt:

- **Stufe 2** bleibt Winkel zweier Vektoren (unverändert bis auf zwei Lösungswege).
- **Stufe 3** sind Geraden in Parameterform bzw. durch zwei Punkte, einschließlich der Regel,
  dass der Schnittwinkel zweier Geraden der **spitze** ist (Betrag im Zähler).
- **Stufe 4** ist Gerade–Ebene mit Entscheidungsanteil (Sachmodell, Umkehraufgabe, Begründung,
  warum dort der Sinus steht).
- **Stufe 5** ist Ebene–Ebene und Kombinationsaufgaben.

| id | Level | Kriterium |
|---|---|---|
| 7, 12 | 2 | DUENNER_WEG behoben: Lösungsweg begründet, warum das Skalarprodukt allein entscheidet bzw. woher das Vorzeichen kommt |
| 13 | 3 | Winkel zweier Geraden in Parameterform; Aufpunkte sind ohne Bedeutung |
| 14 | 3 | negatives Skalarprodukt — der Betrag liefert \(60°\) statt \(120°\), Begründung im Lösungsweg |
| 15 | 3 | Geraden nur durch je zwei Punkte gegeben, Richtungsvektoren selbst bilden |
| 16 | 3 | Auswahl des Vektorpaars mit \(60°\); alle vier Paare im Lösungsweg durchgerechnet (MC) |
| 17 | 3 | gleiche Beträge, kleiner Winkel — Deutung „Kosinus nahe \(1\)“ |
| 18 | 3 | Umkehraufgabe: Parameter aus der Orthogonalitätsbedingung |
| 19 | 4 | Gerade–Ebene; der Lösungsweg begründet den Übergang vom Kosinus zum Sinus |
| 20 | 4 | Modell aus Sachtext (Laderampe), Ergebnis an der Steigung geprüft |
| 21 | 4 | Verfahren begründen: warum bei Gerade–Ebene der Sinus steht (MC) |
| 22 | 4 | Umkehraufgabe: Parameter im Richtungsvektor aus vorgegebenem Winkel \(45°\) |
| 23 | 4 | Gerade–Ebene mit negativer Komponente, kleiner Winkel gedeutet |
| 24 | 4 | Folgerung aus \(\alpha = 0°\): parallel zur Ebene, aber Lage offen (ersetzt die Aufgabe mit der zu langen richtigen Option) |
| 25 | 5 | zwei Schritte: Normalenvektor aus drei Punkten, dann Winkel zur Koordinatenebene |
| 26 | 5 | **Fehlersuche**: fehlender Betrag liefert \(109{,}5°\) statt \(70{,}5°\) — der falsche Weg endet nachweislich falsch (MC) |
| 27 | 5 | Parameter aus zwei Bedingungen: Punktprobe **und** Orthogonalität zweier Ebenen |
| 28 | 5 | Gerade aus zwei Punkten, dann Winkel zur Ebene; sehr flacher Winkel, Schnitt trotzdem vorhanden |
| 29 | 5 | zwei Verfahren verzahnt: Kreuzprodukt für die Schnittgerade, Sinusformel für den Winkel |
| 30 | 5 | Umkehraufgabe mit Parameter im Normalenvektor, Lösung \(a = \pm 1\) diskutiert |
| 31 | 6 | Abi-Format: Neigungswinkel eines Pultdachs bestimmen **und** gegen eine Schranke beurteilen |
| 32 | 6 | Abi-Format Pyramide: Seitenfläche aus drei Punkten, Winkel zur Grundfläche |
| 33 | 6 | „Zeigen Sie, dass zwei Winkel gleich sind“ — Begründung über die gleichen Komponenten des Richtungsvektors |
| 34 | 6 | Behauptung prüfen: \(\alpha + \beta = 90°\), daher mal der eine, mal der andere größer (MC) |
| 35 | 6 | Parameter aus vorgegebenem Winkel \(30°\), Lösung \(\sqrt6\), Probe im Lösungsweg |
| 36 | 6 | **Abi eA**: Schnittwinkel zweier Dachflächen **und** Erklärung, warum der sichtbare Firstwinkel der stumpfe Nebenwinkel ist |

### 12-lk-dgl → Geraden- und Ebenenscharen (eA) — Ersatz-Trainer

Audit: KEIN_AFB3 L5 **und** L6; DUENNER_WEG (Stufen 1, 2). Alle 36 Aufgaben sind neu.
Differenzialgleichungen stehen nicht im Thüringer Lehrplan; das Lehrplan-Gate meldete hier
zuvor zwei Treffer (`#1` und `#5`), jetzt keinen mehr.

Geändert wurden außerdem:

- `<title>`: `Geraden- und Ebenenscharen (eA) - Mathepfade`
- `THEMA_CONFIG = { name: 'Geraden- und Ebenenscharen (eA)', bereich: 'geometrie' }`
  (vorher `bereich: 'analysis'` — der Trainer gehört jetzt in den Abschnitt „Geometrie eA“)
- Kommentar in Zeile 2: `<!-- Dateiname historisch (QR-Links); Inhalt seit 2026-09: Geraden- und Ebenenscharen, TH-Lehrplan Kap. 4.2 -->`
- **`THEMA_KEY` bleibt `'12-lk-dgl'`** — sonst verlieren Schülerinnen und Schüler ihren
  gespeicherten Fortschritt.

**Neuer Index-Zeilentext (`theme-name`), noch einzutragen:** `Geraden- &amp; Ebenenscharen`

| id | Level | Kriterium |
|---|---|---|
| 1 | 1 | Begriff der Schar: ein Parameter, der nicht die Punkte, sondern die Gerade auswählt (MC) |
| 2 | 1 | ein Schritt: Scharparameter und Geradenparameter nacheinander einsetzen |
| 3 | 1 | Parameter steht nur im Richtungsvektor → gemeinsamer Punkt (MC) |
| 4 | 1 | Punktprobe in einer Ebenenschar, nach dem Parameter auflösen |
| 5 | 1 | Begriff: parameterfreier Richtungsvektor bedeutet lauter parallele Geraden (MC) |
| 6 | 1 | Parameter im Aufpunkt: dritte Komponente ist von \(t\) unabhängig |
| 7 | 2 | Orthogonalität des Richtungsvektors zu einem festen Vektor |
| 8 | 2 | Parallelität zweier Ebenen über den Streckfaktor der Normalenvektoren; „echt parallel“ geprüft |
| 9 | 2 | gemeinsamer Spurpunkt einer Ebenenschar auf der \(x\)-Achse — der Parameter fällt heraus |
| 10 | 2 | Lage der Schargeraden zueinander: Büschel, nicht parallel (MC) |
| 11 | 2 | zwei Schritte: \(t\) aus der \(x\)-Forderung, dann \(k\) aus der \(z\)-Forderung |
| 12 | 2 | gemeinsamen Punkt erkennen **und** seinen Betrag bilden |
| 13 | 3 | Ebenenschar durch eine **feste Gerade**: nach \(a\) sortieren, Koeffizientenvergleich |
| 14 | 3 | Parameter für Orthogonalität zweier Ebenen |
| 15 | 3 | Parameter, für den eine Schargerade eine feste Gerade schneidet; Zwischenergebnis \(t=-1\) |
| 16 | 3 | Gerade senkrecht auf einer Ebene: Kollinearität mit dem Normalenvektor (MC) |
| 17 | 3 | zweite Variante der festen Gerade, Parameter in zwei Koeffizienten |
| 18 | 3 | Orthogonalität zweier Geraden, nicht ganzzahlige Lösung \(-\tfrac13\) |
| 19 | 4 | „kein gemeinsamer Punkt“ **ohne** Nennung des Verfahrens; zweiter Schritt Aufpunktprobe, damit nicht versehentlich „liegt in E“ |
| 20 | 4 | Punkt auf der Schnittgeraden: die parameterfreie Ebene zuerst prüfen |
| 21 | 4 | Verfahren begründen: wie man den gemeinsamen Punkt einer Geradenschar findet (MC) |
| 22 | 4 | Modell aus Sachtext (Mast senkrecht auf einer Dachebene) → Kollinearität mit \(\vec n\) |
| 23 | 4 | Parameter, für den sich zwei Geraden schneiden; sonst windschief |
| 24 | 4 | gemeinsame Ebene aller Schargeraden aus der konstanten Koordinate erkennen (MC) |
| 25 | 5 | Parameter aus **zwei** Bedingungen: Richtung parallel zu \(E\), dann Aufpunkt in \(E\) — gefragt ist die zweite Unbekannte |
| 26 | 5 | **Fehler in einer Lagebestimmung**: aus \(\vec u \cdot \vec n = 0\) wird „echt parallel“ geschlossen, obwohl \(g_1\) in \(E\) liegt; der falsche Weg endet nachweislich falsch (MC) |
| 27 | 5 | zwei Bedingungen zugleich: Schnittpunkt in \(E\) **und** in der \(xz\)-Ebene; Lösung \(-\tfrac23\) |
| 28 | 5 | Grenzfall \(a=-1\): parallel — mit Aufpunktprobe gegen „liegt in E“ abgesichert |
| 29 | 5 | zwei Verfahren: Scharparameter einsetzen, dann Winkel zweier Ebenen |
| 30 | 5 | Parallelität zweier **Scharen**; Fallunterscheidung \(k = \pm 1\), Gegenvektor als dieselbe Richtung erkannt |
| 31 | 6 | Abi-Format, **Fallunterscheidung**: Aufpunkt liegt für jedes \(k\) in \(E\), also nie echt parallel; \(k=-0{,}5\) liefert „liegt in \(E\)“, sonst schneidend |
| 32 | 6 | Abi-Format: gemeinsame Gerade einer Ebenenschar nachweisen **und** ihren Abstand vom Ursprung bestimmen (zwei Verfahren) |
| 33 | 6 | **Fallunterscheidung** schneidend/windschief nach dem Parameter, mit Begründung, warum parallel ausscheidet (MC) |
| 34 | 6 | Abi-Format Sachkontext: Schar durch eine feste Gerade (First) nachweisen, dann Parameter aus dem Neigungswinkel \(30°\) |
| 35 | 6 | **Fallunterscheidung** identisch/schneidend über das Kreuzprodukt der Normalen; „echt parallel“ tritt nie auf |
| 36 | 6 | **Abi eA**: gemeinsamer Achsenpunkt der Schar nachweisen **und** Schnittwinkel zweier Scharebenen bestimmen |

---

### Gate-Ergebnisse (Block B2, 2026-09-30)

| Gate | Ergebnis |
|---|---|
| `level_check --strict` (4 Trainer) | Exit 0, **0 Fehler, 0 Warnungen** (vorher 5 Warnungen: abstaende #25/#28, lagebeziehungen #29/#35, schnittwinkel #24) |
| `lehrplan_check --strict` (4 Trainer) | 0 Befunde (vorher 2 in `12-lk-dgl`: „Differenzialgleichung“ in #1 und #5) |
| `katex_check` (4 Trainer) | 0 Render-Fehler |
| `pytest tests/test_trainer.py` | grün für alle vier Trainer |
| Sichtprüfung | PNG je Trainer und Stufe angesehen; Spaltenvektoren erscheinen als Matrix, deutsche Anführungen schließen mit `“` |

### Offen

- Der neue `theme-name`-Text `Geraden- &amp; Ebenenscharen` muss in `index.html` nachgetragen
  werden; die Datei war während der Welle für parallel arbeitende Agenten gesperrt.
- In `12-lk-geom-abstaende` bleibt Stufe 3 (Punkt–Ebene über die HNF) inhaltlich unverändert;
  der Plan sieht für Stufe 1–3 nur Entdopplung vor.
- In `12-lk-geom-schnittwinkel` sind in Stufe 2 noch mehrere Aufgaben, die auf \(90°\) hinauslaufen;
  sie stehen dort bewusst als Einführung der Orthogonalitätsprüfung.

---

### Review-Nachtrag 2026-09-30

Der Pruef-Agent hat Geometrie gA und eA gemeinsam geprueft. **Kein Rechenfehler** in den acht
Trainern; alle Befunde betrafen Dubletten und Zuschnitt. Behoben wurde:

| Nr. | Befund | Behebung |
|---|---|---|
| 1 | `abstaende` #27 (L5) und #35 (L6) waren dieselbe Aufgabe, beide mit Loesung 12 | #35 ersetzt: Scheinwerfer, zwei Pfosten, **Vergleich** zweier Punkt-Gerade-Abstaende (1,795 gegen 4,854) |
| 2 | `lagebeziehungen` #26 und `lk-dgl` #26 waren identisch (gleiche Fehlersuche, gleicher Optionssatz) | `lk-dgl` #26 auf einen anderen Fehlertyp umgestellt: **Grenzfall des Parameters** — ausgeklammerter Faktor \(k\) macht alle Geraden identisch, \(k=0\) liefert gar keine Gerade |
| 3 | `lagebeziehungen` #31 war dieselbe Aufgabe wie `12-ebenen` #36 (Satteldach, Firsthoehe 4) | ersetzt: drei Ebenen, dritte mit Parameter; **Fallunterscheidung** \(a \ne 2\) (genau ein Punkt) gegen \(a = 2\) (keiner) |
| 4 | `abstaende` #31 uebernahm das Zeltdach-Modell aus `12-vektoren-grundlagen` #31 | ersetzt: Tunnelachse, Nachweis "Messpunkt liegt nicht auf der Achse" ueber das Kreuzprodukt, Abstand 24 m |
| 5 | `schnittwinkel` #13/#14/#15/#17 waren viermal dieselbe arccos-Rechnung (Kollaps L2/L3) | #14 → **Innenwinkel im Dreieck** (ohne Betrag, weil stumpf moeglich), #17 → **Raum- gegen Flaechendiagonale im Quader**; #13 und #15 bleiben als die zwei zulaessigen Standardfaelle |
| 6 | `schnittwinkel` #19/#20/#23 dreimal Gerade–Ebene ueber \(\sin\alpha\) | #23 ersetzt: Umkehraufgabe **ohne Quadrieren** — aus \(90°\) folgt Kollinearitaet mit \(\vec n\), gesucht \(b+c = 8\) |
| 7 | `schnittwinkel` #22/#30/#35 dreimal "Parameter aus Winkelbedingung, quadrieren" | #35 ersetzt: **obere Schranke** \(90°\) der Winkel, Begruendung, dass sie Grenzwert und nicht Maximum ist |
| 8 | `lk-dgl` #21 war reine Methodenwissens-MC auf einer AFB-II-Stufe | ersetzt: das Verfahren **anwenden**, gemeinsamer Punkt einer Schar, \(y = 1\) |
| 9 | `lk-dgl` #29 war eine gewoehnliche Schnittwinkel-Rechnung (Ueberschneidung mit `schnittwinkel`) | ersetzt: **zwei Bedingungen** an den Scharparameter, eine davon fuer jedes \(a\) erfuellt; \(a = -5\) |
| 10 | `lk-dgl` #7 und #18 beide "Skalarprodukt null" (Kollaps L2/L3) | #7 ersetzt: **Betrag** des Richtungsvektors, \(k = 1\) |
| 11 | `lk-dgl` #13 und #17 beide "nach \(a\) sortieren, gemeinsame Gerade" | #17 ersetzt: **Spurpunkt** auf der \(z\)-Achse, \(a = 2\), Grenzfall \(a = 0\) benannt |
| 12 | `lk-dgl` #19 (L4) und #28 (L5) beide "kein Schnittpunkt" (Kollaps L4/L5) | #28 ersetzt: Parameter in der **Ebene**, Punktprobe fuer jedes \(a\) erfuellt, Parallelitaet liefert \(a = 1{,}5\) |
| 13 | "Fuer welchen Parameter liegt \(g\) in \(E\)" stand dreifach im Block | Akzente getrennt: `lagebeziehungen` #25 hat den Parameter in der **Geraden**, `lk-dgl` #31 in der **Ebenenschar** und verlangt die vollstaendige Fallunterscheidung |
| 14 | Sattel-/Pultdach-Kontext fuenfmal im Block; `schnittwinkel` #36 nutzte die Gleichungen von `12-ebenen` #36 | `lagebeziehungen` #31 ohne Dach (drei Ebenen), `schnittwinkel` #31 → **Solarmodul**, #36 → **Flusstal** mit neuen Zahlen (73,7° statt 53,1°), `lk-dgl` #34 → **Drehachse einer Klappe**, `lk-dgl` #22 → **Hangflaeche** statt Dachebene |

Zusaetzlich beim Nachlauf gefunden und behoben: `lagebeziehungen` #24 hatte im Tipp den
Loesungswert stehen (`k=2`), und der neue Tipp zu #31 nannte `E_2`, was das Gate ebenfalls als
Loesungswert las — beide Tipps nennen jetzt nur noch den Weg.

Alle geaenderten Werte erneut mit Wolfram nachgerechnet. Gates danach: `level_check --strict`
Exit 0 ohne Warnung, `lehrplan_check --strict` 0 Befunde, `katex_check` 0 Fehler,
`pytest tests/test_trainer.py` 28 passed; PNG je geaenderter Aufgabe angesehen.

---

# Block C1 — Stochastik (gA)
Welle Task 9, Stand 2026-09-30. Lokale Nachvollziehbarkeit; im Public-HTML stehen die
Kriterien bewusst nicht.

Grundlage: Rubrik aus `2026-09-26-lehrplan-th-und-level-progression-plan.md`, Befunde aus
`../audit/audit-2026-09-19-mathepfade.md` (Zeilen 123–141). Niveau: TH-Lehrplan Kap. 4.3 gA
(Bernoulli-Ketten, Binomialverteilung, Erwartungswert und Standardabweichung, σ-Regeln,
Prognoseintervalle). Lesart Kl. 12 gA durchgängig:

- **L4 (AFB II)**: Verfahren selbst wählen, Modell aus einem Sachtext aufstellen,
  Umkehraufgabe (Parameter statt Wert gesucht).
- **L5 (AFB III)**: zwei Verfahren verzahnen, Parameter aus zwei Bedingungen, Fehler in
  einer vorgelegten Rechnung finden. Der vorgeführte falsche Weg muss zu einem **falschen**
  Ergebnis führen — jede Fehlersuchaufgabe wurde daraufhin nachgerechnet.
- **L6 (AFB III, Abi-Format gA)**: mehrschrittig, mit Begründungsanteil und Sachkontext,
  Formulierungen „Berechnen Sie … und beurteilen Sie“, „Zeigen Sie“, Fallunterscheidung
  oder Grenzfall.

Jede Zahl mit dem Wolfram-MCP nachgerechnet (kumulierte Binomialwerte exakt, nicht
geschätzt). Bilder mit `tests/bild.py --aufgabe <id>` und einem Scratchpad-Skript, das den
Lösungsweg aufdeckt, in mehreren Stufen je Trainer angesehen.

### Abgrenzung der vier Trainer gegeneinander

| Trainer | Inhalt |
|---|---|
| 12-stoch-zufallsgroessen | Zufallsgröße, Wahrscheinlichkeitsverteilung, Erwartungswert, Varianz und Standardabweichung, lineare Transformation, faires Spiel. **Keine** σ-Umgebungen, keine kumulierten Binomialwerte |
| 12-stoch-binomialverteilung | Bernoulli-Kette und ihre Voraussetzungen, Binomialkoeffizient, kumulierte Wahrscheinlichkeiten, „mindestens/höchstens“, Mindestanzahl-Aufgaben. **Keine** σ-Umgebungen |
| 12-stoch-sigma-regeln | σ-Umgebungen, 68,3 / 95,4 / 99,7 %, Laplace-Bedingung σ > 3, ganzzahlige Grenzen, Abweichung in Einheiten von σ. **Kein** Schluss auf ein unbekanntes p aus einer Beobachtung |
| 12-stoch-hypothesentests → **Prognoseintervalle** | Prognoseintervall für **absolute und relative** Häufigkeit, Beurteilung einer Beobachtung, n aus geforderter Genauigkeit |

Abstand nach außen: zu `10-stoch-mehrstufig` und `10-stoch-bedingte-wsk` (Pfadregeln,
Vierfeldertafel — hier nur einmal als Hilfsmittel in #27 der Binomialverteilung) und zum
eA-Trainer `12-lk-stoch-normalverteilung` des Parallelblocks.

### Prognoseintervall gegen Konfidenzintervall (Beschluss 2026-09-30)

Der Ersatz-Trainer schließt ausschließlich **von bekanntem \(p\) auf die Häufigkeit**. Der
umgekehrte Schluss — von einer Beobachtung auf das unbekannte \(p\) — entsteht parallel im
eA-Trainer `12-lk-stoch-prozesse` („Konfidenzintervalle“) und kommt hier nirgends als
Rechenziel vor. Die Abgrenzung wird in #3 und #24 ausdrücklich zum Aufgabeninhalt gemacht
(beide MC, „Was leistet ein Prognoseintervall?“), damit die Verwechslung benannt ist, bevor
sie im eA-Trainer als Fehlersuchaufgabe auftaucht. Aufgabe #21 beurteilt zwar mehrere
Kandidaten für \(p\), tut dies aber über deren **eigene Prognoseintervalle** — nicht über
ein aus der Beobachtung gebildetes Intervall.

---

### Ersatz-Trainer: 12-stoch-hypothesentests → Prognoseintervalle (TH 4.3 gA)

Alle 36 Aufgaben neu. Dateiname bleibt (QR-Links), `THEMA_KEY` bleibt
`'12-stoch-hypothesentests'` (sonst verlieren Schüler ihren localStorage-Fortschritt).
Geändert: `<title>`, `THEMA_CONFIG.name = 'Prognoseintervalle'`, Kommentar in Zeile 2.
Die Datei hatte gemischte Zeilenenden (CRLF **und** LF) und wurde auf CRLF vereinheitlicht.

**Index-Zeilentext (`theme-name`), vom Autor nachzutragen:** `Prognoseintervalle`
(Abschnitt „Stochastik“, Spalte `.col-12`).

Audit-Befund war RUECKFALL L5 und RUECKFALL L6 (Stufe 5 und 6 leichter als Stufe 4) sowie
4 Lehrplan-Treffer auf `nullhypothese` / `signifikanzniveau` (#1, #4, #7, #28). Beides mit
dem Neuschrieb erledigt; das Lehrplan-Gate meldet 0 Befunde.

| id | Level | Kriterium |
|---|---|---|
| 1–2 | 1 | ein Rechenschritt: μ bzw. σ aus n und p (n = 400, p = 0,5) |
| 3 | 1 | Begriff: Richtung des Schlusses (bekanntes p → Häufigkeit); benennt den Gegenbegriff, ohne ihn zu rechnen |
| 4 | 1 | μ bei p = 1/3 |
| 5 | 1 | Faktor 2 gehört zu 95 % (Zuordnung der drei Sigma-Regeln) |
| 6 | 1 | σ mit schönem Ergebnis (4,8) |
| 7–8 | 2 | Standardverfahren: beide Grenzen des 95-%-Intervalls, ganzzahlige Rechnung |
| 9 | 2 | erste gebrochene Grenze → Abrunden nach außen (26,4 → 26) |
| 10–11 | 2 | σ als Zwischenergebnis, dann obere Grenze (n = 2500) |
| 12 | 2 | Begründung der Rundungsrichtung (MC) |
| 13–14 | 3 | Klassenarbeits-Standard: relative Häufigkeit über die absolute Grenze, zwei Schritte |
| 15 | 3 | Breite = 4σ, Erwartungswert wird dafür nicht gebraucht |
| 16 | 3 | p muss aus dem Sachverhalt erschlossen werden (faire Münze), n = 10 000 |
| 17 | 3 | obere Grenze absolut mit ganzzahligem σ |
| 18 | 3 | relative obere Grenze mit gebrochenem σ (27,17 %) |
| 19 | 4 | Modell aus Text: p erschließen, Abweichung in σ ausdrücken (3,07 — außerhalb) |
| 20 | 4 | Umkehrrichtung: Intervall zur Annahme bilden, Beobachtung einordnen (230 liegt drin) |
| 21 | 4 | Verfahren wählen: vier Kandidaten für p, je eigenes Intervall; nur p = 0,50 auszuschließen (Randfälle bewusst vermieden, alle drei übrigen liegen deutlich innen) |
| 22 | 4 | Modell aus Text (Umfrage), Aufrunden der oberen Grenze |
| 23 | 4 | Modell aus Text mit relativer Quote; Beobachtung 28,4 % gegen Grenze 25,06 % |
| 24 | 4 | Was leistet ein Prognoseintervall — Abgrenzung gegen den Schluss auf p (MC) |
| 25 | 5 | n aus geforderter Genauigkeit; n kürzt sich fast heraus, Genauigkeit wächst nur mit √n (2500) |
| 26 | 5 | **Fehlersuche σ**: √(np) statt √(np(1−p)); falscher Weg gibt 12,25, richtig 10,25 — der falsche Wert ist zudem größer als das Maximum ½√n ≈ 11,18 |
| 27 | 5 | **Fehlersuche**: absolutes σ auf einen Anteil addiert; negative untere Grenze als Sachprobe (MC) |
| 28 | 5 | n aus geforderter Breite, diesmal Schranke nach **oben** (absolutes Intervall wächst mit n) |
| 29 | 5 | zwei Schritte: Grenze runden, dann Differenz zur Beobachtung (18) |
| 30 | 5 | Parameter aus zwei Bedingungen: Breite 48 → σ = 12 → p(1−p) = 0,24 → p = 0,4 oder 0,6, Zusatzbedingung entscheidet |
| 31 | 6 | **Behauptung prüfen** (Vorgabe): „Liegt h außerhalb, ist p sicher falsch?“ — rund 5 % fallen auch bei richtigem p heraus (MC) |
| 32 | 6 | Abi-Format: Laplace prüfen, Intervall, Beurteilung einer Meldung von 130 gegen Grenze 120; „höchstens“-Zusage macht die Betrachtung einseitig |
| 33 | 6 | Abi-Format: relative Breite ∝ 1/√n, Faktor 3 bei neunfachem Umfang, mit Zahlenprobe |
| 34 | 6 | Behauptung prüfen: doppeltes n ⇒ doppelte Breite? Faktor √2 (MC) |
| 35 | 6 | Abi-Format: Grenze der Näherung — σ ≈ 0,99, Laplace verletzt, μ − 2σ wäre negativ |
| 36 | 6 | Abi-Format, **Grenzfall**: μ + 2σ = 330 exakt ganzzahlig, erste Zahl außerhalb ist 331; Begründung, warum der Fall hier ohne Rundungsregel entschieden werden kann |

MC-Anteil: Stufe 6 enthält 2 MC (#31, #34) — die Obergrenze von 3 ist eingehalten.

---

### 12-stoch-binomialverteilung

Audit-Befund: KEIN_AFB3 L5 **und** L6. Geändert: Stufe 5 und 6 komplett neu (12 Aufgaben).
Stufe 1–4 unverändert (kein KOLLAPS gemeldet).

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | zwei kumulierte Werte verrechnen, P(X ≤ 5) − P(X ≤ 1); die häufige Verwechslung mit P(X ≤ 2) wird im Weg benannt (0,7486) |
| 26 | 5 | **Fehlersuche**: 1 − P(X ≤ 4) statt 1 − P(X ≤ 3); falscher Weg gibt 0,1642, richtig 0,3518 — Differenz ist genau P(X = 4) |
| 27 | 5 | zwei Verfahren verzahnt: Bernoulli-Formel und bedingte Wahrscheinlichkeit, P(X = 2 \| X ≥ 2) = 0,4689 |
| 28 | 5 | Umkehr über das Gegenereignis mit Logarithmus-Ungleichung; Kippen des Zeichens beim Teilen durch ln 0,96 (74) |
| 29 | 5 | Vereinigung zweier unvereinbarer Ereignisse, Symmetrie bei p = 0,5 als Abkürzung (0,1094) |
| 30 | 5 | **Fehlersuche Modell**: Ziehen ohne Zurücklegen als Bernoulli-Kette gerechnet; konkrete p-Werte nach Gewinn und Niete im Weg (MC) |
| 31 | 6 | Abi-Format: Qualitätszusage, P(X ≥ 6) = 0,0378, Beurteilung inkl. Hinweis auf zu kleine Stichprobe |
| 32 | 6 | Abi-Format: Modus der Binomialverteilung; μ = 5,95 grenzt nur ein, der Vergleich P(5)/P(6)/P(7) entscheidet — Begründungsanteil: Runden von μ ist kein Argument |
| 33 | 6 | Abi-Format: Gewinnwahrscheinlichkeit 0,2632 gegen Erwartungswert μ = 1 beurteilen |
| 34 | 6 | **Behauptung prüfen**: doppeltes n ⇒ doppeltes P(X ≥ 1)? Gegenrechnung plus Grenzbetrachtung „Wahrscheinlichkeiten überschreiten 1 nicht“ (MC) |
| 35 | 6 | Abi-Format: Bestehen durch Raten, P(X ≥ 6) = 0,0544, Beurteilung der Bestehensgrenze mit Alternative (Grenze 7 → 1,4 %) |
| 36 | 6 | Abi-Format: p aus P(X = 0) = 0,5 (≈ 0,067) und Begründung der Größenordnung **ohne** Taschenrechner über 0,9¹⁰ ≈ 0,349 |

MC in Stufe 6: 1 (#34). Keine Aufgabenform dreimal in derselben Stufe.

---

### 12-stoch-sigma-regeln

Audit-Befund: KEIN_AFB3 L5 **und** L6; **KOLLAPS L2/L3 und L3/L4**; DUENNER_WEG (Stufen 2, 6).
Geändert: Stufe 3, 4, 5 und 6 komplett neu (24 Aufgaben), dazu der dünne Lösungsweg von
##9 (Stufe 2) ausgeführt.

Ursache des Doppel-Kollapses war, dass Stufe 2, 3 und 4 dieselbe Rechnung enthielten
(μ ± kσ aus gegebenen μ, σ). Neuer Schnitt: **Stufe 2** bleibt „aus gegebenem μ und σ“,
**Stufe 3** verlangt μ und σ erst aus n und p sowie die ganzzahlige Rundung mit Begründung,
**Stufe 4** verlangt das Erschließen von p aus dem Sachtext oder die Umkehrrichtung.

| id | Level | Kriterium |
|---|---|---|
| 13 | 3 | zwei Schritte aus n und p, gebrochene untere Grenze, Abrunden **nach außen** begründet (330) |
| 14 | 3 | obere Grenze der 3σ-Umgebung, Aufrunden (127) |
| 15 | 3 | σ mit Bruchwerten; Kontrolle, was ohne den Faktor 1 − p herauskäme (16,33) |
| 16 | 3 | Begründung der Rundungsrichtung (MC) |
| 17 | 3 | Laplace-Bedingung prüfen, dann Anteil **oberhalb** μ + 2σ auf eine Seite verteilen (2,3 %) |
| 18 | 3 | Abweichung in Einheiten von σ (1,92 — noch innerhalb) |
| 19 | 4 | Modell aus Text: Erfolg ist das **Erscheinen**, nicht das Fehlen (p = 0,92 statt 0,08); untere Grenze 221 |
| 20 | 4 | Umkehraufgabe: n aus σ und p (192), mit Probe |
| 21 | 4 | Schranke „mehr als 2σ darüber“ → erste ganze Zahl oberhalb 52,33, also 53 |
| 22 | 4 | Verfahren wählen: vier Kombinationen gegen die Laplace-Bedingung prüfen (MC) |
| 23 | 4 | p aus dem Sachverhalt (Würfel, p = 1/6); σ = 10 ganzzahlig |
| 24 | 4 | p aus dem Sachverhalt (Raten bei Ja/Nein), σ ≈ 3,87 — Näherung gerade noch vertretbar (38) |
| 25 | 5 | Parameter aus zwei Bedingungen: σ = 20 bei n = 2500 → p = 0,2 oder 0,8, Zusatzbedingung p > 0,5 entscheidet |
| 26 | 5 | **Fehlersuche σ**: √(np) statt √(np(1−p)); falsch 12,25, richtig 10,25; zusätzlich die Schranke σ ≤ ½√n ≈ 11,18 als Sachprobe |
| 27 | 5 | **Fehlersuche**: Varianz 250 statt σ ≈ 15,81 eingesetzt; Intervall [0; 1000] als offensichtlicher Widerspruch (MC) |
| 28 | 5 | Abzählen der ganzen Zahlen in der 2σ-Umgebung: 328 − 272 + 1 = 57 (das „+1“ ist der Kern) |
| 29 | 5 | zwei Reihen getrennt rechnen und Breiten vergleichen (8,94); Deutung: kleines p drückt σ stärker, als n es hebt |
| 30 | 5 | Parameter aus zwei Bedingungen: μ = 180 und σ = 12 → Quotient liefert 1 − p, dann n = 900 |
| 31 | 6 | Abi-Format: Umfrage, obere Grenze 226, Beurteilung von 235 (2,77σ) mit Abwägung |
| 32 | 6 | **Behauptung prüfen**: doppeltes n ⇒ doppelte Breite? Faktor √2, plus Hinweis auf die relative Verschmälerung (MC) |
| 33 | 6 | **Fallunterscheidung**: σ = 9 bei n = 900 → p = 0,1 oder 0,9, beide zulässig; Symmetrie von p(1−p) als Grund benannt |
| 34 | 6 | Abi-Format: Abfüllanlage, 3,15σ, Beurteilung mit ausdrücklicher Grenze der Aussage („wie selten der Befund wäre, nicht wie wahrscheinlich die Störung ist“) |
| 35 | 6 | **Behauptung prüfen**: Wert innerhalb ⇒ Annahme bestätigt? Gegenbeispiel mit benachbarten p (MC) |
| 36 | 6 | Abi-Format, **einseitige** Betrachtung: 99,85 % einer Seite entspricht μ + 3σ = 345; Begründung, warum der untere Rand hier nicht zählt |

MC in Stufe 6: 2 (#32, #35). #26 wurde eigens daraufhin geprüft, dass der falsche Weg
tatsächlich einen falschen Wert liefert (12,25 ≠ 10,25).

---

### 12-stoch-zufallsgroessen

Audit-Befund: KEIN_AFB3 L5 **und** L6; DUENNER_WEG (Stufen 2, 4, 5).
Geändert: Stufe 5 und 6 komplett neu (12 Aufgaben); Stufe 4 in den Aufgabenformen
aufgefächert und die Lösungswege ausgeführt (DUENNER_WEG); dazu der dünne Weg von #12
(Stufe 2) ausgeführt.

Stufe 4 bestand aus vier gleichartigen Fair-Spiel-Aufgaben. Jetzt: Begriffsklärung (#19),
Nettogewinn berechnen (#20), Einsatz gesucht (#21), Erwartungswert bei Gleichverteilung
(#22), Deutung von E(X) < 0 (#23), **Wahrscheinlichkeit gesucht** (#24, neue Umkehrrichtung
statt der zweiten Einsatzaufgabe).

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | Begriff „fair“ über den Nettogewinn; Weg erklärt, warum gleiche Wahrscheinlichkeiten weder nötig noch hinreichend sind (MC, Längen angeglichen) |
| 20 | 4 | Nettogewinn: Einsatz wird unabhängig vom Ausgang fällig (0 €) |
| 21 | 4 | Umkehraufgabe: Einsatz aus der Fairness-Bedingung (5 €) |
| 22 | 4 | Sonderfall Gleichverteilung: Erwartungswert = arithmetisches Mittel (5 €) |
| 23 | 4 | Deutung von E(X) < 0 als Durchschnitt vieler Spiele (MC, Längen angeglichen; alte Option „Nichts“ ersetzt) |
| 24 | 4 | Umkehraufgabe neue Richtung: gesuchte **Wahrscheinlichkeit** für Fairness (0,002) |
| 25 | 5 | Verteilung aus zwei Bedingungen: Summennormierung und E(X) = 2,9 → P(X = 5) = 0,5, mit Probe |
| 26 | 5 | **Fehlersuche**: arithmetisches statt gewichtetes Mittel; falsch 2,5, richtig 3,7 — Sachprobe „90 % liegen bei 4“ |
| 27 | 5 | zwei Verfahren verzahnt: lineare Transformation und Verschiebungssatz, E((2X−7)²) = 37; der Fehlschluss E(Y²) = E(Y)² wird benannt |
| 28 | 5 | Fairness mit zusätzlicher Margenbedingung: Einsatz 3,70 € statt 3,20 € |
| 29 | 5 | **Fehlersuche**: V(X+X) mit dem Additionssatz gerechnet; X ist von sich selbst nicht unabhängig, richtig V(2X) = 4V(X) (MC) |
| 30 | 5 | Umkehraufgabe: unbekannter Wert a aus E(X) = 4 und P(X = 1) = 0,25 (a = 5) |
| 31 | 6 | Abi-Format: Versicherung, Gewinn 10 €, Beurteilung mit Gesetz der großen Zahlen und der Abhängigkeitsfalle (Unwetter) |
| 32 | 6 | **Behauptung prüfen**: gleicher Erwartungswert ⇒ gleiche Streuung? Gegenbeispiel mit σ = 1 gegen σ = 101 (MC) |
| 33 | 6 | **Bezug zur Binomialverteilung** (Abgrenzung gegen Kl.-10-Niveau): n und p aus E(X) = 24 und V(X) = 14,4, Quotient kürzt np heraus (n = 60) |
| 34 | 6 | Abi-Format: Verteilung des Nettogewinns selbst aufstellen, dann σ ≈ 2,61 über den Verschiebungssatz; Deutung Streuung gegen Erwartungswert |
| 35 | 6 | **Behauptung prüfen**: faires Spiel ⇒ σ = 0? Gegenbeispiel mit E(X) = 0 und σ = 4 (MC) |
| 36 | 6 | Abi-Format: zwei Anlagen mit gleichem Erwartungswert, σ(B) = 60 gegen σ(A) = 100; Entscheidung braucht mehr als den Erwartungswert |

MC in Stufe 6: 2 (#32, #35).

---

---

### Review-Nachtrag (Prüf-Agent, 2026-09-30)

Bestätigt wurden: alle kumulierten Binomialwerte, alle σ-Grenzen und Rundungsrichtungen,
alle E(X)/V(X); die Trennung Prognose- gegen Konfidenzintervall; dass keine Fehlersuchaufgabe
über den falschen Weg zur richtigen Lösung führt; Stufe 6 als Abi-Format.

**Behobene Befunde:**

| Befund | Behebung |
|---|---|
| `hypothesentests #19`: Intervall im Lösungsweg als [82; 119] angegeben — μ ± 2σ = [81,74; 118,26], nach außen also **[81; 119]**; der Beitext lehrte das Gegenteil der eigenen Rundungsregel | Zahl korrigiert und die Rundung ausgeschrieben |
| `hypothesentests #26` war **buchstäblich** dieselbe Aufgabe wie `sigma-regeln #26` (n = 500, p = 0,3, √(np) statt √(np(1−p)), 10,25) | Ersetzt durch eine Prognose-eigene Fehlersuche: der Prüfer fragt nach „zu hoch“ und berechnet die **untere** Grenze — beide Zahlen sind für sich richtig gerechnet, nur beantwortet die eine die Sachfrage nicht (275) |
| Identische MC-Sätze über beide Trainer: `hypothesentests #12` ≡ `sigma-regeln #16` (Rundungsregel), `#34` ≡ `sigma-regeln #32` (doppeltes n, sogar dasselbe Zahlenbeispiel), `#35` ≡ Zahlen aus `sigma-regeln #22` | Rundungs-MC steht nur noch in `sigma-regeln`; `hypothesentests #12` ist jetzt eine Rechenaufgabe mit Einordnung, `#34` prüft stattdessen das **Niveau** (99,7 % gegen 95 % → Faktor 1,5 statt 2), `#35` rechnet mit n = 80, p = 0,03 (σ ≈ 1,53) |
| `zufallsgroessen` #10, #12, #13, #14, #15, #16, #18: Tipps nannten die fertige Rechnung oder das Zwischenergebnis | Alle sieben auf den Weg umgestellt |
| `sigma-regeln #22`: √(400·0,15·0,85) im Lösungsweg als ≈ 6,96 statt √51 ≈ **7,14** | Zahl korrigiert, Wurzelwert ergänzt |
| Vier Trainer stellten dieselbe Umkehraufgabe „quadratische Gleichung für p aus σ“; `sigma-regeln #25`/`#33` zusätzlich ein Kollaps L5/L6 | Die Aufgabenform steht jetzt **einmal** im Block, in `sigma-regeln #25` (L5). `sigma-regeln #33` ist eine Umkehraufgabe an der Laplace-Bedingung geworden (kleinstes n bei p = 0,02 → 460, mit Prüfung beider Nachbarn); `hypothesentests #30` erschließt p über die Intervallmitte aus Grenze und Breite |
| `hypothesentests` Stufen 1–3 waren rechnerisch deckungsgleich mit `sigma-regeln` Stufen 2–4; das Unterscheidungsmerkmal setzte erst ab Stufe 4 ein | Stufen 1–3 neu geschnitten: **L1** liest Grenzen aus einem gegebenen Intervall, misst den Abstand eines Ergebnisses und bestimmt die Breite; **L2** bildet das Intervall aus n und p und hält jeweils ein Ergebnis dagegen (#9 Würfel, #10 Deutung, #12 Beobachtung 268); **L3** ist durchgehend die relative Häufigkeit |
| `hypothesentests #3` (L1) und `#24` (L4) waren dieselbe Frage, #3 verriet #24 | `#24` fragt jetzt nach dem passenden **Werkzeug** für vier Fragestellungen (Verfahren wählen, AFB II) |
| Drei bis vier gleichartige Aufgaben je Stufe | `hypothesentests` L2/L3 neu geschnitten (keine zwei Aufgaben mehr mit denselben n und p); `zufallsgroessen` L4 #22 und #24 neu (Modell aus Text mit Restwahrscheinlichkeit; Erwartungswert und Hochrechnung auf 20 Tage) statt zweier weiterer Fairness-Aufgaben; `zufallsgroessen` L6 #36 jetzt Varianzaddition statt eines dritten σ über E(X²) |
| Rückfälle unter das Stufenniveau: `hypothesentests #17` rein absolut; `zufallsgroessen #22` leichter als #11 (L2); `zufallsgroessen #31` nur eine Multiplikation und eine Subtraktion | #17 rechnet jetzt die relative Grenze; #22 verlangt die Verteilung samt Restwahrscheinlichkeit aus dem Text; #31 bestimmt σ des Jahresgewinns (315,6) und begründet, dass die Prämie als additive Konstante die Streuung nicht ändert |
| Acht gerade `"` als Schlusszeichen nach korrektem `„` | Alle auf `“` umgestellt; Kontrollzählung `grep -c '\"'` liefert in allen vier Dateien 0 |
| `zufallsgroessen #16`/`#18`: Lösungsweg nur eine nackte Formelzeile | Beide ausgeführt (Symmetrieargument bzw. Verschiebungssatz mit beiden Erwartungswerten) |
| `zufallsgroessen #1`/`#2`: richtige MC-Option deutlich die längste | Alle vier Optionen je Aufgabe auf dieselbe Satzform gebracht |
| `zufallsgroessen #14`/`#15`/`#18`: „(2 Dez.)“ statt „(2 Nachkommastellen)“ | Vereinheitlicht |

Nicht übernommen wurde nichts; alle Befunde sind umgesetzt. Ein neuer Gate-Fehler entstand
beim Umbau (`hypothesentests #18` sprach eine MC-Option als „die zweite Antwort“ an) und
wurde vor dem Commit behoben.

### Gates am Ende des Blocks

```
python tests/level_check.py --strict trainer/12-stoch-*.html      -> Exit 0, 0 Warnungen
python tests/lehrplan_check.py --strict trainer/12-stoch-*.html   -> 0 Befunde (vorher 4)
python tests/katex_check.py trainer/12-stoch-*.html               -> 4x ok
python -m pytest tests/test_trainer.py -k "…" -q                  -> 28 passed
```

Behobene Gate-Warnungen aus dem Bestand: Tipp mit Lösungswert (#26 alt, sigma-regeln),
zu lange richtige MC-Option in `12-stoch-sigma-regeln` #35 alt, `12-stoch-zufallsgroessen`
##23/#33/#36 alt und `12-stoch-hypothesentests` #32/#35 alt, Tipp mit Lösungswert
(#13 alt, hypothesentests). Ein Lösungsweg sprach eine MC-Option über ihren Buchstaben
bzw. ihre Position an („die dritte Antwort“) — in `12-stoch-sigma-regeln` #35 und
im Ersatz-Trainer #31 durch den Wortlaut der Option ersetzt, weil die Engine mischt.

### Offen

- **Stufe 1–3 der drei Bestandstrainer** wurde planmäßig nicht neu geschrieben
  (Ausnahme: `12-stoch-sigma-regeln`, dort verlangte der Doppel-Kollaps Stufe 3).
- **`12-stoch-zufallsgroessen` Stufe 1–3** bleibt damit auf dem Stand, der sich inhaltlich
  mit dem in Kl. 10 fehlenden Thema „Wahrscheinlichkeitsverteilung und Erwartungswert
  diskreter Zufallsgrößen“ (TH 2.3.4) überschneidet. Ab Stufe 4 ist der Trainer eindeutig
  Abiturniveau, Stufe 6 nutzt die Binomialverteilung ausdrücklich (#33). Sobald der in
  `2026-09-26-kl10-kriterien.md` als offen vermerkte Kl.-10-Trainer entsteht, sollten
  Stufe 1–3 hier angehoben werden.
- **Index-Zeile für den Ersatz-Trainer** ist nicht gesetzt (`index.html` war während der
  Welle für vier parallel arbeitende Agenten gesperrt): `theme-name` → `Prognoseintervalle`.
- `THEMA_KEY` enthält weiterhin die Zeichenfolge `hypothesentests`. Das ist ein technischer
  Schlüssel für den localStorage-Fortschritt, kein Aufgabentext; das Lehrplan-Gate wertet
  nur die Aufgabenfelder aus und meldet 0 Befunde. Eine Umbenennung würde den Fortschritt
  aller Schüler löschen und unterbleibt bewusst.

---

# Block C2 — Stochastik (eA)
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

### Abgrenzung

- **12-lk-stoch-normalverteilung** = Normalverteilung selbst: Dichte, Wendestellen, Φ-Funktion,
  Standardisierung, Quantile, Näherung der Binomialverteilung samt Stetigkeitskorrektur.
- **12-lk-stoch-prozesse** = Schluss von der Stichprobe auf das unbekannte \(p\):
  Konfidenzintervall, Intervallbreite, Stichprobenumfang.
- Gegen die gA-Trainer des Parallelblocks (`12-stoch-binomialverteilung`,
  `12-stoch-sigma-regeln`, `12-stoch-zufallsgroessen`, künftig „Prognoseintervalle“) wurde
  abgegrenzt: dort die gA-Tiefe, hier die eA-Tiefe. Der Duplikat-Lauf von `level_check`
  über alle 90 Trainer meldet für beide Dateien nichts.

#### Konfidenzintervall gegen Prognoseintervall (der fachliche Kern des Ersatz-Trainers)

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

### 12-lk-stoch-prozesse → Konfidenzintervalle (eA), Ersatz-Trainer

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
| 10 | 2 | von der unteren auf die obere Grenze: Radius aus \(\sigma_h\), zwei Radien Abstand |
| 11 | 2 | Abhängigkeit von \(n\) (MC): vierfaches \(n\) halbiert die Breite — \(n\) steht unter der Wurzel |
| 12 | 2 | Radius in Prozentpunkten; Bezug zur üblichen Angabe „\(\pm 2{,}5\) Prozentpunkte“ |
| 13 | 3 | Klassenarbeits-Standard mit Zwischenergebnis: \(h\) aus 520/1000, dann untere Grenze |
| 14 | 3 | Umrechnung Anteil → Anzahl: obere Intervallgrenze mal Grundgesamtheit; Lösungsweg mahnt die Reihenfolge an |
| 15 | 3 | Rechnung mit dem Faktor \(1{,}96\); Lösungsweg begründet die Wahl gegen den Faktor \(2\) |
| 16 | 3 | Breite in Prozentpunkten, Ergebnis zusätzlich als Prozentintervall gedeutet |
| 17 | 3 | kleine relative Häufigkeit (Ausschussquote), vier Dezimalstellen nötig |
| 18 | 3 | Laplace-Bedingung: \(\sigma(X)\) der Trefferanzahl berechnen und gegen die Faustregel \(\sigma \gt 3\) stellen |
| 19 | 4 | Umkehr: \(n\) aus geforderter Breite bei \(h = 0{,}4\) (→ 2400); Probe an \(n\) und \(n-1\), **Aufrunden begründet** |
| 20 | 4 | Verfahren wählen + Entscheidung: behauptetes \(p = 0{,}30\) liegt außerhalb von \([0{,}3171;\,0{,}4029]\) |
| 21 | 4 | zwei veröffentlichte Intervalle mit gleicher Mitte: aus dem Verhältnis der Radien auf das Verhältnis der Umfänge schließen (Faktor 4) |
| 22 | 4 | Umkehraufgabe mit zwei Lösungen: \(h(1-h) = 0{,}16\) liefert \(0{,}2\) und \(0{,}8\), Symmetrie erklärt |
| 23 | 4 | Meldung in Prozent: Intervall bilden, in Prozent zurückrechnen, den Schluss „unter 45 %“ entkräften |
| 24 | 4 | Maßnahmen beurteilen (MC); die höhere Sicherheit verbreitert das Intervall, sie verschmälert es nicht |
| 25 | 5 | **Fehlersuche „Konfidenzintervall = Prognoseintervall“** — siehe Abschnitt oben; Intervalle überlappen sich nicht |
| 26 | 5 | zwei Verfahren: beide Breiten getrennt, Vergleich in Prozentpunkten; Faktor \(\sqrt{400/900} = \tfrac23\) |
| 27 | 5 | **zwei Bedingungen**: Breite \(\le\) 3 Prozentpunkte **und** \(\sigma(X) \gt 3\); die schärfere gewinnt, Probe im Weg |
| 28 | 5 | Fehlersuche: \(n\) statt \(\sqrt{n}\) im Nenner; falscher Radius 25-mal zu klein, Plausibilitätskontrolle ergänzt |
| 29 | 5 | zwei Intervalle, Breite der Überlappung; Deutung: 6 Prozentpunkte Unterschied sind Stichprobenschwankung |
| 30 | 5 | zwei Befragungen zusammenfassen (Treffer und Umfänge addieren) und Intervall bilden; der Mittelwert der Einzelquoten wäre falsch |
| 31 | 6 | Abi eA: KI mit \(1{,}96\), Beurteilung einer Zeitungsaussage; Grenzfall — mit Faktor \(2\) kippt die Entscheidung |
| 32 | 6 | Abi eA, Modellkritik: die Näherung liefert eine **negative** untere Grenze; \(\sigma(X) \approx 1{,}72 \lt 3\), Verteilung rechtsschief |
| 33 | 6 | Abi eA: dasselbe \(h\) für 95 % und 99 % (Faktoren \(1{,}96\) und \(2{,}58\)); Beurteilung, was die höhere Sicherheit kostet |
| 34 | 6 | **Beweisanteil**: \(h(1-h)\) maximal bei \(h = 0{,}5\) über \(g'\) und \(g''\); daraus der sichere Umfang \(49^2\) |
| 35 | 6 | Begründung (MC): warum \(h\) und nicht \(p\) in der Streuung steht — der Unterschied zum Prognoseintervall |
| 36 | 6 | Abi eA, Modellkritik: Selbstselektion bei einer Online-Umfrage; ein schmales Intervall misst nur die Zufallsschwankung |

#### Formen je Stufe (gegen die Befunde an den Ersatz-Trainern der Kl. 10 und 11)

Nach dem Review (siehe unten) steht in keiner Stufe dieselbe Aufgabenform mehr als zweimal:
L1 Begriff, \(\sigma_h\), Radius, Breite, Grenze, Zugehörigkeit; L2 zwei Grenzenaufgaben
neben Breite-aus-Anzahl, Grenze-aus-Grenze, MC und Prozentpunkten; L3 zwei Grenzenaufgaben
neben Umrechnung auf Anzahl, Faktor-1,96-Einführung, Breite und Laplace-Prüfung; L4 je einmal
Umfangsplanung, Behauptungsprüfung, Intervallvergleich, quadratische Umkehr, Prozentmeldung
und MC; L5 je zweimal Fehlersuche und Stichprobenvergleich, dazu Zusammenfassen und die
Zwei-Bedingungen-Aufgabe; L6 zwei Modellkritiken, Beurteilung, Sicherheitsvergleich,
Beweisaufgabe und MC.

Der **Stichprobenumfang** steht nur noch in vier von 36 Aufgaben (`#19`, `#21` indirekt,
`#27`, `#34`) — vorher waren es sieben. Und nicht als dasselbe Verfahren mit größeren Zahlen:
`#19` löst die Ungleichung, `#21` schließt aus zwei Intervallen auf das Verhältnis der Umfänge,
`#27` verbindet die Forderung mit der Laplace-Bedingung, `#34` begründet zuerst über eine
Extremwertbetrachtung, welcher Fall der schlechteste ist.

---

### 12-lk-stoch-normalverteilung — Stufe 5 und 6 neu

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

### Gates (Stand nach dem Block)

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

### Index

`index.html` wurde von diesem Block **nicht** angefasst (vier Ersatz-Trainer brauchten sie
gleichzeitig). Nachzuziehen ist der `theme-name` der Zeile zu `12-lk-stoch-prozesse.html`:

```
Konfidenzintervalle
```

### Offen

- Die Stufen 1–4 der Normalverteilung sind planmäßig nicht neu geschrieben worden; der
  KOLLAPS-Rest zwischen L3 und L4 (Standardisieren gegen Standardisieren mit Näherung)
  bleibt bestehen.
- Der Ersatz-Trainer benutzt durchgehend die Näherungsformel mit \(h\) in der Streuung
  (Wald-Intervall). Genauere Verfahren sind in der Schule nicht vorgesehen; `#32` zeigt
  ausdrücklich, wo dieses Verfahren versagt.
- Der Name „Stochastische Prozesse“ verschwindet mit der Index-Zeile; der Dateiname bleibt
  wegen der QR-Links historisch.

---

### Review-Nachtrag (Prüf-Agent, 2026-09-30)

Bestätigt hat der Prüfer: die Trennung von Prognose- und Konfidenzintervall ist durchgehend
korrekt (die Streuung wird nie vertauscht), keine Fehlersuchaufgabe führt über den falschen
Weg zur richtigen Lösung, die Faktoren \(1{,}96\) und \(2\) werden sauber benannt, Stufe 6 ist
durchgehend Abi-Format.

Behoben wurden:

| Befund | Behebung |
|---|---|
| **Rechenfehler `#21`**: `loesung: 1024` bei gefordertem Radius \(0{,}0125\) und \(h = 0{,}2\); richtig wäre \(0{,}16/0{,}0000390625 = 4096\) gewesen (mit \(n = 1024\) ist der Radius \(0{,}025\), also doppelt so groß wie gefordert). Der Lösungsweg stellte die Ungleichung korrekt auf und schrieb dann die falsche Zahl hin | Aufgabe **ersetzt** statt nur korrigiert — sie war zugleich die dritte Umfangsaufgabe der Stufe. `#21` fragt jetzt nach dem Verhältnis zweier Stichprobenumfänge aus zwei veröffentlichten Intervallen. Gegenprobe mit Wolfram: \(n = 4096\) wäre tatsächlich das kleinste gewesen (\(n = 4095\) gibt \(0{,}0125015\)) |
| **Kollision mit dem Parallelblock**: `#19` war numerisch identisch mit `12-stoch-hypothesentests #25` (beide \(n = 2500\)); weil für \(p = h = 0{,}5\) beide Formeln zusammenfallen, unterlief ausgerechnet dieses Paar die Trennung der Trainer | `#19` rechnet jetzt mit \(h = 0{,}4\) (→ 2400). Der Fall \(h = 0{,}5\) bleibt `#34` vorbehalten, wo er als schlechtester Fall **begründet** wird |
| **Drei bis vier gleichartige Aufgaben je Stufe**: L2 `#7, #8, #10` dreimal „Grenze“, L4 `#19, #21, #23` dreimal „Stichprobenumfang“, insgesamt 7 von 36 Umfangsaufgaben | `#10`, `#21`, `#23`, `#30` und `#33` durch andere Formen ersetzt (siehe Tabelle oben); Umfangsaufgaben jetzt 4 von 36 |
| **Rückfall `#14`** (L3): Mitte zweier Zahlen bilden und subtrahieren — einschrittig und leichter als `#7` auf L2 | ersetzt durch die Umrechnung des Intervalls auf die Anzahl in der Grundgesamtheit (zwei Schritte, eigene Fehlerquelle in der Reihenfolge) |
| **Toleranz zu weit**: `toleranz: 1` bei ganzzahligen „kleinstes \(n\)“-Aufgaben ließ den Nachbarwert durch — und der ist dort die typische Fehlantwort | alle ganzzahligen Antworten des Trainers auf `toleranz: 0` (`#14`, `#19`, `#21`, `#27`, `#34`) |
| `12-lk-stoch-normalverteilung #34` nannte die erwartete Form nicht („geben Sie diesen Bruchteil an“); plausibel wären auch \(e^{-1/2}\) oder \(60{,}65\) gewesen | „als Dezimalzahl auf vier Nachkommastellen“ ergänzt |
| `12-lk-stoch-normalverteilung #6` nutzte `p<0{,}5` statt des sonst durchgehaltenen `\lt` | auf `\lt` umgestellt |

Nicht geändert: der Zeilenumbruch von \(\mu \pm \sigma\) in `normalverteilung #34` (im Bild
geprüft, bleibt lesbar). Gerade Schlusszeichen `"` gibt es in beiden Dateien nicht.

Gates nach dem Review: `level_check --strict` und `lehrplan_check --strict` je Exit 0 ohne
Warnung, `katex_check` 0 Renderfehler, `pytest -k "normalverteilung or stoch-prozesse"`
14 passed, Duplikat-Lauf über alle 90 Trainer ohne Befund. Alle geänderten Zahlen mit Wolfram
nachgerechnet, die geänderten Aufgaben `#14`, `#19`, `#21`, `#30`, `#33` und
`normalverteilung #34` als PNG angesehen — Aufgabenseite und aufgedeckter Lösungsweg.

---
