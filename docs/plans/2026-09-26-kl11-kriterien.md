# Klasse 11 — Kriterien je Trainer (Welle Task 8, Stand 2026-09-30)

Lokale Nachvollziehbarkeit; im Public-HTML stehen die Kriterien bewusst nicht.
Grundlage: Rubrik aus `2026-09-26-lehrplan-th-und-level-progression-plan.md`, Befunde aus
`../audit/audit-2026-09-19-mathepfade.md` (Zeilen 108-122, 240-250). Lesart Kl. 11:
L4 = Verfahren selbst waehlen / Modell aus Text / Umkehraufgabe; L5 = zwei Verfahren
kombinieren, Parameter aus zwei Bedingungen, Fehler in vorgelegter Rechnung;
**L6 = Abi-Format** (mehrschrittig, Begruendungsanteil, Sachkontext; in Block B eA-Variante).
Jede Loesung mit Wolfram nachgerechnet; Bilder je geaenderter Aufgabe per `tests/bild.py`
angesehen. Jeder Block wurde von einem zweiten Agenten geprueft; Befunde und Behebung stehen
je Block unter "Review-Nachtrag".

Die vier Bloecke der Welle:

| Block | Trainer | Umfang |
|---|---|---|
| A1 Ableitung und Steigung | 4 | Ableitungsregeln, Ketten-/Produktregel, Aenderungsrate, Tangenten/Normalen |
| A2 e-Funktion und Kurvenverhalten | 4 | e-Funktion, e-Funktion-Ableitung, Monotonie/Kruemmung, Extrem-/Wendepunkte |
| A3 Anwendungen | 3 | Extremwertaufgaben, Kurvendiskussion, Steckbriefaufgaben |
| B eA | 4 | Funktionsscharen, gebrochen-rational, erweiterte Kurvendiskussion, **Ersatz** 11-lk-newton -> ln-Funktion (eA) |

## Abgrenzung der Ableitungs-Trainer (Beschluss 2026-09-30)

Die Bloecke A1 und A2 hatten denselben Stoff doppelt. Entschieden wurde:
`11-ableitung-ketten-produkt` = die **Regeln** an allen Funktionstypen (e-Terme als einer
Typ neben Wurzel, Bruch, Klammer, Sinus/Kosinus; Stufe 3 entsprechend umgestellt).
`11-e-funktion-ableitung` = die **e-Funktion in Anwendung und Argumentation**
(Wachstums-/Zerfallsmodelle, Tangenten, Parameterbestimmung, Vergleich von Raten);
reine "Leite ab"-Aufgaben gehoeren dort nicht hin.

---

# Block A1 — Ableitung und Steigung
Welle Task 8, Stand 2026-09-30. Lokale Nachvollziehbarkeit; im Public-HTML stehen die
Kriterien bewusst nicht.

Grundlage: Rubrik aus `2026-09-26-lehrplan-th-und-level-progression-plan.md`, Befunde aus
`../audit/audit-2026-09-19-mathepfade.md` (Zeilen 108–112, 122 und der offene Punkt in
Zeile 240 ff.). Lesart Kl. 11 durchgängig:

- **L4 (AFB II)**: Verfahren selbst wählen, Modell aus einem Sachtext aufstellen, Umkehraufgabe
  (Parameter oder Stelle gesucht statt Funktionswert).
- **L5 (AFB III)**: zwei Verfahren kombinieren, Parameter aus zwei Bedingungen, Fehler in einer
  vorgelegten Rechnung finden. **Keine** Auswertung an der Stelle \(x = 0\) (Rubrik-Verbot; sie
  trivialisiert Produkt- und Kettenregel).
- **L6 (AFB III, Abi-Format gA)**: mehrschrittige Aufgabe mit Begründungsanteil, Formulierungen
  „Zeigen Sie …“, „Beurteilen Sie …“, Sachkontext, Fallunterscheidung/Grenzfall.

Jede Lösung mit dem Wolfram-MCP nachgerechnet (auch die jeweils *nicht* gefragten Fälle);
Bilder L5 und L6 je Trainer mit `tests/bild.py` erzeugt und angesehen.

### Abgrenzung der vier Trainer gegeneinander und gegen die Nachbarblöcke

| Trainer | Inhalt |
|---|---|
| 11-ableitungsregeln | Potenz-, Faktor-, Summenregel, negative Exponenten, zweite Ableitung, Parameter in der Funktionsgleichung. **Ohne** Produkt- und Kettenregel (die liegen im Nachbartrainer) |
| 11-ableitung-ketten-produkt | Ketten- und Produktregel, e-Funktion und Trigonometrie als Bausteine, verzahnte Anwendung beider Regeln |
| 11-aenderungsrate | mittlere und lokale Änderungsrate, Differenzenquotient, h-Methode, Rate gegen Bestand im Sachkontext. **Ohne** Tangentengleichungen |
| 11-tangenten-normalen | Tangente und Normale aufstellen, Berührbedingung, Tangente durch einen vorgegebenen Punkt, Steigungswinkel |

„Tangente aufstellen“ gehört ausschließlich zu `11-tangenten-normalen`; die entsprechenden
Aufgaben sind aus `11-aenderungsrate` entfernt worden. Extrem- und Wendepunkte bleiben den
Trainern `11-extrempunkte-wendepunkte`, `11-monotonie-kruemmung` und
`11-kurvendiskussion-ganzrational` vorbehalten — hier wird nur nach „waagerechter Tangente“
im Sinne von \(f'(x) = 0\) gefragt, nie nach Art oder Anzahl von Extrempunkten.

---

### 11-ableitungsregeln

Audit: KEIN_AFB3 L5; KOLLAPS L2/L3; DUENNER_WEG (Stufen 1, 4). Der im Audit offen gelassene
Punkt (10 Aufgaben ab Stufe 4 werden an der Stelle \(x = 0\) ausgewertet) war beim Öffnen der
Datei bereits behoben — das Level-Gate meldete keine Warnung mehr. Die Produkt- und
Kettenregelaufgaben der alten Stufen 4–6 sind trotzdem entfallen: sie doppelten
`11-ableitung-ketten-produkt` (#33/#34 waren dort wortgleich vorhanden).

| id | Level | Kriterium |
|---|---|---|
| 1, 2, 3 | 1 | DUENNER_WEG behoben: Lösungsweg zeigt jetzt Potenzregel und Einsetzen getrennt |
| 19 | 4 | Verfahren wählen: \(f'=0\) und Ausklammern, Nebenlösung \(x=0\) durch Bedingung ausgeschlossen |
| 20 | 4 | Umkehraufgabe: Faktor \(a\) aus \(f'(2)=36\) |
| 21 | 4 | Modell aus Sachtext: Bestand, momentan unveränderlich |
| 22 | 4 | Rückwärts denken: welche Funktion hat die gegebene Ableitung (MC) |
| 23 | 4 | Verfahren wählen: Bruch gliedweise zerlegen statt Quotientenregel |
| 24 | 4 | Umkehraufgabe mit negativem Exponenten, Vorzeichenfall \(\pm 3\) |
| 25 | 5 | Parameter aus zwei Bedingungen (\(f'(1)=0\), \(f'(2)=9\)) |
| 26 | 5 | Fehler in vorgelegter Rechnung: Nenner abgeleitet statt umgeschrieben (MC) |
| 27 | 5 | zwei Verfahren: \(f'\) und \(f''\) aufstellen, quadratische Gleichung, beide Lösungen geprüft |
| 28 | 5 | \(f'=0\) bei negativem Exponenten, Lösungsmenge \(\pm 2\) auf Bereich eingeschränkt |
| 29 | 5 | Sachkontext, Vorzeichenwechsel der Rate, Nebenlösung außerhalb des Zeitraums |
| 30 | 5 | Parameterbedingung mit Grenzfall \(p = 0\) ausdrücklich diskutiert (MC) |
| 31 | 6 | Abi-Format: „Zeigen Sie … genau zwei Tage“, Sachkontext Wasserstand, beide Lösungen im Intervall |
| 32 | 6 | zwei Bedingungen, Term mit \(x^{-1}\), Probe im Lösungsweg |
| 33 | 6 | Behauptung prüfen: \(f'=3(x+1)^2\), doppelte Nullstelle ist eine Stelle, nicht zwei (MC) |
| 34 | 6 | „Zeigen Sie, dass f überall steigt“ über quadratische Ergänzung, kleinster Ableitungswert |
| 35 | 6 | Abi-Format: stärkstes Wachstum über \(U''=0\), Sachkontext Umsatz |
| 36 | 6 | Behauptung prüfen im Sachkontext: Wachstum ist eine Aussage über die Rate (MC) |

### 11-ableitung-ketten-produkt

Audit: KEIN_AFB3 L5 **und** L6; KOLLAPS L2/L3 **und** L5/L6; KURZ (Stufen 1, 2, 3, 4, 6);
DUENNER_WEG (Stufen 1, 2, 3) — der dünnste Trainer des Blocks. Deshalb **alle 36 Aufgaben**
überarbeitet: Stufe 1 nur sprachlich (volle Fragesätze, Lösungswege), Stufe 2–6 neu.

Der Trainer wertete vorher 18 Aufgaben an der Stelle \(x = 0\) aus (darunter 11 ab Stufe 4);
dort fällt bei Produkt- und Kettenregel jeweils ein Summand weg, die Aufgabe prüft die Regel
also gar nicht. Alle Auswertungsstellen sind jetzt von null verschieden, und ab Stufe 5 wird
statt eines Funktionswerts die Ableitungsfunktion selbst bzw. die Stelle mit \(f'(x)=0\) verlangt.

| id | Level | Kriterium |
|---|---|---|
| 1–6 | 1 | KURZ/DUENNER_WEG behoben: vollständige Fragesätze, Lösungsweg nennt innere und äußere Funktion |
| 7–12 | 2 | Kettenregel an Klammerpotenzen, Auswertung an \(1, 2, -2, 1, 2\) statt an \(0\); Lösungsweg mit \(u, u'\) |
| 13–18 | 3 | Kettenregel an der e-Funktion, Auswertung an \(1\) bzw. \(-1\); Vorzeichenfallen benannt |
| 19 | 4 | Produktregel an negativer Stelle, Ausklammern von \(e^x\) |
| 20 | 4 | Produktregel mit \(\sin\), Werte bei \(\pi\) |
| 21 | 4 | Ableitungsterm gesucht, Vereinfachung \(e^x(x-1+1)=xe^x\) (MC) |
| 22 | 4 | Umkehraufgabe: Parameter im Exponenten aus \(f'(1)=2e^2\), Eindeutigkeit begründet |
| 23 | 4 | Verfahren wählen: Kettenregel oder ausmultiplizieren, Probe im Lösungsweg |
| 24 | 4 | Modell aus Sachtext: Wirkstoffkonzentration, Rate nach 4 Stunden |
| 25 | 5 | Produkt + Kette, \(f'=0\) über Ausklammern; Eindeutigkeit aus der Linearität |
| 26 | 5 | zwei Lösungen, beide geprüft, größere gefragt |
| 27 | 5 | Fehler in vorgelegter Rechnung: fehlende Nachdifferenzierung (MC) |
| 28 | 5 | Parameter aus der Bedingung \(f'(1)=0\), Probe |
| 29 | 5 | Produkt + Kette führen auf \(\tan x = 1\); zweite Lösung außerhalb des Intervalls |
| 30 | 5 | Ableitungsfunktion selbst verlangt (Wurzel, Kettenregel), Distraktoren sind die typischen Teilfehler (MC) |
| 31 | 6 | Abi-Format: „Zeigen Sie … genau einen Höchstwert“, Sachkontext Wirkstoff, Vorzeichenargument |
| 32 | 6 | Behauptung prüfen: Produkt aus \(k\) und \(e^{kx}\) wird nie null (MC) |
| 33 | 6 | Fallunterscheidung über die Diskriminante: \(c<1\), \(c=1\), \(c>1\) |
| 34 | 6 | zwei Modelle vergleichen, Exponentialgleichung, Deutung des Ergebnisses |
| 35 | 6 | quadratische Gleichung mit zwei reellen Lösungen, kleinere gefragt |
| 36 | 6 | Behauptung prüfen mit Probe über \(\sin(2x)\) (MC) |

### 11-aenderungsrate

Audit: KEIN_AFB3 L5; DUENNER_WEG (Stufen 4, 5, 6). Stufe 4 wurde mit neu geschrieben, weil
sie fast vollständig aus Tangentenaufgaben bestand — die gehören zur Trainer-Abgrenzung nach
`11-tangenten-normalen`. Der Trainer behandelt jetzt ausschließlich mittlere und lokale
Änderungsrate, Differenzenquotient und die Unterscheidung von Rate und Bestand im Sachkontext.
Stufe 1–3 (Begriffe, Differenzenquotient, h-Methode) bleiben inhaltlich unverändert.

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | Umkehraufgabe im Sachkontext: Zeitpunkt zu vorgegebener Momentangeschwindigkeit |
| 20 | 4 | Modell aus Text: zwei Messwerte, mittlere Rate je Stunde |
| 21 | 4 | Begriffsvergleich mittlere/lokale Rate mit Gegenbeispiel im Lösungsweg (MC) |
| 22 | 4 | Umkehraufgabe: Intervallende aus gegebener mittlerer Änderungsrate, Kürzen mit 3. binom. Formel |
| 23 | 4 | Modell aus Text, Vorzeichen der Abflussrate |
| 24 | 4 | Verfahren wählen: höchster Punkt über \(h'(t)=0\) |
| 25 | 5 | zwei Schritte: Anfangsrate bestimmen, dann Bedingung „halb so groß“ |
| 26 | 5 | Fehler in vorgelegter Rechnung: durch die rechte Grenze statt durch die Intervalllänge geteilt (MC) |
| 27 | 5 | zwei Schritte im Sachkontext, Rate bleibt positiv |
| 28 | 5 | Parameter aus zwei Bedingungen, mittlere **und** lokale Rate nebeneinander |
| 29 | 5 | zwei Verfahren kombiniert: Durchschnitts- und Momentangeschwindigkeit gleichsetzen |
| 30 | 5 | Folgerung aus mittlerer Rate \(0\) (Mittelwertsatz anschaulich), Gegenbeispiele im Lösungsweg (MC) |
| 31 | 6 | Abi-Format: „Zeigen Sie … genau einmal“, Vorzeichenwechsel der Rate, Sachkontext Gewässer |
| 32 | 6 | Abi-Format: stärkster Zuwachs über \(B''=0\), Abgrenzung Rate gegen Bestand |
| 33 | 6 | Behauptung prüfen: fallende Rate ist nicht dasselbe wie fallender Bestand (MC) |
| 34 | 6 | allgemeiner Differenzenquotient auf \([-a;a]\), Symmetrie, Anzahl der Lösungen |
| 35 | 6 | Abi-Format: Übergang Zunahme/Abnahme, zweite Lösung außerhalb des Zeitraums |
| 36 | 6 | Behauptung prüfen: mittlere Geschwindigkeit ist Weg durch Zeit, nicht Mittelwert der Tempi (MC) |

### 11-tangenten-normalen

Audit: KEIN_AFB3 L5 **und** L6; KOLLAPS L2/L3 **und** L4/L5; DUENNER_WEG (Stufen 3, 4).
Dazu die beiden Gate-Warnungen `#27` (richtige MC-Option deutlich länger) und `#34`
(Tipp nannte den Lösungswert 63) — beide Aufgaben sind neu.

Gegen den Kollaps L2/L3 ist Stufe 3 auf **Normalen** zugespitzt (#13–#17): vorher stand dort
dieselbe Aufgabenart wie in Stufe 2 (Tangentensteigung berechnen). Stufe 4 ist neu, weil sie
sich mit Stufe 5 doppelte.

| id | Level | Kriterium |
|---|---|---|
| 13, 15, 16 | 3 | DUENNER_WEG behoben: Lösungsweg zeigt Ableitung, Einsetzen und Kehrwertbildung getrennt |
| 14 | 3 | von Tangenten- auf Normalensteigung umgestellt (Kollaps L2/L3) |
| 17 | 3 | von Tangenten- auf Normalengleichung umgestellt, Distraktoren sind die typischen Fehler (MC) |
| 19 | 4 | Tangente aufstellen und auf der \(y\)-Achse auswerten |
| 20 | 4 | Umkehraufgabe: Stelle zu vorgegebener Steigung, Nebenlösung \(-2\) diskutiert |
| 21 | 4 | Normale aufstellen, Distraktoren mit falschem Vorzeichen bzw. ohne Kehrwert (MC) |
| 22 | 4 | Normalensteigung bei fallender Tangente |
| 23 | 4 | Modell aus Sachtext: Stütze senkrecht zum Hangprofil |
| 24 | 4 | zwei Tangenten aufstellen und gleichsetzen |
| 25 | 5 | Tangente durch einen vorgegebenen Punkt, allgemeine Berührstelle, beide Lösungen |
| 26 | 5 | Berührbedingung als zwei Bedingungen, Probe über die doppelte Nullstelle |
| 27 | 5 | Berührbedingung als Auswahl; MC-Optionen auf gleiche Länge gebracht (Gate-Warnung) |
| 28 | 5 | Normale aufstellen **und** mit der Funktion schneiden (zwei Verfahren) |
| 29 | 5 | Parallelitätsbedingung, beide Lösungen, negative gefragt |
| 30 | 5 | Parameter aus der Bedingung „Tangente durch den Ursprung“ |
| 31 | 6 | Abi-Format: Tangente im Sachkontext (Tunnelprofil), Auswertung auf der Achse |
| 32 | 6 | „Zeigen Sie …“: doppelte Nullstelle, Faktorisierung, allgemeine Aussage \(-2x_0\) |
| 33 | 6 | Behauptung prüfen: Wendetangente berührt und durchsetzt zugleich (MC) |
| 34 | 6 | Steigungswinkel rückwärts: \(60°\) vorgegeben, Stelle gesucht (ersetzt die Aufgabe mit dem verratenen Wert 63) |
| 35 | 6 | Normale durch einen vorgegebenen Punkt, allgemeine Stelle, Deutung des konstanten Summanden |
| 36 | 6 | Grenzfall \(m_t = 0\): Normale ohne Steigung (MC) |

### Review-Nachtrag 2026-09-30

Befunde des Prüf-Agenten, alle behoben. Die Rechenergebnisse waren durchweg bestätigt;
die Befunde betrafen Abgrenzung, Dubletten, Tipps und Sachkontexte.

**Abgrenzung gegen Nachbartrainer**

- `11-ableitungsregeln #33` war inhaltsgleich mit `11-monotonie-kruemmung #31` (dieselbe
  Funktion \(x^3+3x^2+3x+7\), dieselbe Einsicht \(f'=3(x+1)^2\)). Jetzt \(x^3-9x^2+27x+4\)
  mit \(f'=3(x-3)^2\). `#34` ist von „zeigen Sie, dass \(f\) überall steigt“ auf die kleinste
  vorkommende **Tangentensteigung** umformuliert — Monotonie gehört dem Nachbarn.
- `11-ableitung-ketten-produkt`: Stufe 3 bestand aus sechs e-Funktions-Kettenregeln, dem
  Kerngeschäft von `11-e-funktion-ableitung`. Stufe 3 liegt jetzt auf Wurzel, Bruch mit
  negativem Exponenten, Sinus, Kosinus und quadratischer innerer Funktion; e-Terme bleiben
  nur dort, wo Produkt- **und** Kettenregel verzahnt sind. Ebenso ersetzt: `#22`
  (Parameter jetzt in \((ax-1)^2\) statt im Exponenten, mit Fallunterscheidung \(a>0\)) und
  `#32` (jetzt Fallunterscheidung nach dem Vorzeichen von \(a\) in \((x^2+a)^3\)).

**Lehrplan**

- `11-ableitung-ketten-produkt #34` verlangte \(t = 10\ln 2\); ln ist im Projekt als eA
  eingestuft. Ersetzt durch zwei Modelle mit gleichem Exponenten und unterschiedlichem
  Vorfaktor (\(e^{-0,5t}\) gegen \(t\,e^{-0,5t}\)), Lösung \(t = 3\) ohne Logarithmus.

**Dubletten innerhalb des Blocks**

- `11-tangenten-normalen #17` (L3) und `#21` (L4) waren bis auf den Punkt wortgleich;
  `#17` liegt jetzt auf \(x^2-4x\) im Punkt \((1|-3)\).
- `#25` und `#26` (beide L5) beschrieben dieselbe Gerade \(y = 4x-4\) mit derselben
  Berührstelle. `#26` liegt jetzt auf \(y = x+a\) und \(f(x)=\sqrt x\) (Lösung \(a = 0{,}25\));
  die Wurzelableitung ist durch `#15` auf Stufe 3 vorbereitet.

**Tipps, die die Lösung vorwegnahmen**

- `11-ableitungsregeln #26` nannte den Wortlaut der richtigen MC-Option, `#17` lieferte die
  fertige Ableitung; `11-tangenten-normalen #8` und `#16` lieferten die Zwischenwerte,
  `#36` nannte die Begründung der richtigen Option. Alle auf reine Weg-Hinweise umgestellt.

**Sachkontext und Progression**

- `11-aenderungsrate #29`: Vorfaktor von \(0{,}2\) auf \(0{,}05\) gesenkt — vorher ergab das
  Modell 72 km/h im Mittel und 216 km/h momentan für einen Radfahrer. Ergebnis unverändert.
- `11-tangenten-normalen`: Auf Stufe 4 ist mit `#20` eine **Vorwärtsaufgabe** zum
  Steigungswinkel ergänzt (Steigung \(1\) → \(45°\)). Damit ist `#34` auf Stufe 6 eine echte
  Umkehraufgabe, und ihr Tipp kommt ohne die Formel \(m = \tan\alpha\) aus.

**Form**

- Negative Koordinaten nach dem Trennstrich rendern als „\(1| -3\)“ und lesen sich wie eine
  Subtraktion. In `#17` und `#25` jetzt `(1\,|\,{-3})` bzw. `P(0\,|\,{-4})`; im Bild geprüft.
- MC-Längen im Altbestand angeglichen: `11-aenderungsrate #1`, `#6`, `#10`; Punktschreibweise
  dort auf den Trennstrich vereinheitlicht (`#6`, `#16`).

**Werkzeug-Hinweis für die nächste Welle:** Ein Ersetzen per Bash-Heredoc hat einen doppelten
Backslash zu einem einfachen gemacht (`\\,` → `\,`), was KaTeX als Komma rendert. Nur im Bild
zu sehen, kein Gate meldet es. Die Regel „nie Bash-Heredoc für Aufgabentexte“ gilt also auch
für Python-Skripte, die per Heredoc an die Shell übergeben werden.

### Offen (bewusst nicht in dieser Welle)

- `11-aenderungsrate` und `11-tangenten-normalen`: KOLLAPS-Reste in Stufe 1/2 werden laut Plan
  nicht angefasst (Stufe 1–3 nur entdoppelt, nicht neu geschrieben).
- `11-ableitungsregeln`: Stufe 2 und 3 unterscheiden sich weiterhin nur durch den negativen
  Exponenten (Audit-Befund KOLLAPS L2/L3); die Rubrik sieht Stufe 1–3 in dieser Welle nicht vor.
- Punktschreibweise im Altbestand der übrigen Trainer weiterhin uneinheitlich
  (Komma statt Trennstrich) — außerhalb dieses Blocks nicht angefasst.

---

# Block A2 — e-Funktion und Kurvenverhalten
Lokale Nachvollziehbarkeit; im Public-HTML stehen die Kriterien bewusst nicht.
Grundlage: Rubrik aus `2026-09-26-lehrplan-th-und-level-progression-plan.md`, Befunde aus
`../audit/audit-2026-09-19-mathepfade.md` (Zeilen 108–122).

Lesart Kl. 11 durchgaengig:
L4 = AFB II, Verfahren selbst waehlen / Modell aus Text / Umkehraufgabe;
L5 = AFB III, zwei Verfahren kombinieren, Parameter aus zwei Bedingungen, Fehler in
vorgelegter Rechnung — **keine Auswertung bei \(x=0\)**;
L6 = AFB III im Abi-Format (gA): mehrschrittige Aufgabe mit Begruendungsanteil,
„Zeigen Sie …", „Beurteilen Sie …", Sachkontext, Fallunterscheidung.

Jede Loesung mit Wolfram nachgerechnet; Bilder L5 und L6 je Trainer per `tests/bild.py`
erzeugt und angesehen.

### Abgrenzung der vier Trainer dieses Blocks

| Trainer | Inhalt | ausdruecklich nicht |
|---|---|---|
| `11-e-funktion` | die Funktion selbst: Wachstum/Zerfall, Graph und Wertebereich, Transformationen von \(e^x\), Gleichungen mit \(e\) | Ableiten |
| `11-e-funktion-ableitung` | Ableiten von \(e\)-Termen (Ketten- und Produktregel), Tangenten an \(e\)-Funktionen, Aenderungsraten | Extrem-/Wendestellen als Aufgabenziel, Integrale |
| `11-monotonie-kruemmung` | Monotonie- und Kruemmungsintervalle, Vorzeichen von \(f'\) und \(f''\) | Bestimmen einzelner Extrem-/Wendepunkte |
| `11-extrempunkte-wendepunkte` | Extrem- und Wendestellen bestimmen, notwendige und hinreichende Bedingung, Sattelpunkt | Intervallbeschreibungen der Monotonie |

Abstand gehalten wurde ausserdem zu `11-ableitungsregeln`, `11-tangenten-normalen`
(Tangentengleichungen als Thema) und `11-kurvendiskussion-ganzrational`
(vollstaendige Kurvendiskussion).

#### Korrektur 2026-09-30: die Abgrenzung zu `11-ableitung-ketten-produkt` trug zunaechst nicht

Die erste Fassung dieser Datei hat den Nachbartrainer als „Regeln an ganzrationalen Termen"
beschrieben. Das ist **falsch**: `11-ableitung-ketten-produkt` enthaelt rund 20 Aufgaben mit
\(e\)-Termen, darunter fuenf vom Typ „Stelle mit waagerechter Tangente an einem \(e\)-Produkt"
(#25, #26, #28, #33, #35). Damit lagen meine urspruenglichen `#28`, `#30`, `#32` und `#36`
inhaltlich auf demselben Format, `#24` neben `ketten-produkt #22` (Parameter im Exponenten
aus einem Ableitungswert) und `#19` neben `ketten-produkt #19` (Produktregel an \(x^2e^{x}\)).
Der Nachbartrainer ist der aeltere, also sind diese Aufgaben hier getauscht worden — siehe
Review-Nachtrag. Der tatsaechliche Stand ist jetzt:

| | `11-ableitung-ketten-produkt` (Block A1) | `11-e-funktion-ableitung` (dieser Block) |
|---|---|---|
| Gegenstand | die Regeln selbst, an gemischten Funktionstypen (Klammerpotenz, Wurzel, Sinus, \(e\)) | die \(e\)-Funktion als Gegenstand: Tangenten an \(e\)-Graphen, Aenderungsraten in \(e\)-Modellen, Parameter in \(e\)-Termen |
| „waagerechte Tangente" an \(e\)-Produkten | bleibt dort (5 Aufgaben, aelter) | kommt hier nicht mehr vor |
| Sachkontext-Modelle (\(a\,t\,e^{-kt}\), Zerfall, Zufluss) | `#24`, `#31`, `#34` liegen weiterhin dort | Schwerpunkt hier |

**Entscheidung der Koordination vom 2026-09-30 (Variante A, geschaerft).**
`11-ableitung-ketten-produkt` ist der Trainer der **Regeln** an allen Funktionstypen; \(e\)-Terme
duerfen dort vorkommen, aber als einer von mehreren Typen neben Wurzel, Bruch, Klammer und
Sinus/Kosinus, nicht als Schwerpunkt — Block A1 hat dessen Stufe 3 dafuer bereits umgestellt.
`11-e-funktion-ableitung` ist der Trainer der **\(e\)-Funktion in Anwendung und Argumentation**:
Wachstums- und Zerfallsmodelle, Tangenten, Parameterbestimmung, Vergleich von Raten. Reine
„Leite ab"-Aufgaben gehoeren damit nicht mehr hierher. Die letzte Restkollision war `#22`
(lineare Funktion mal \(e\)-Term, wie `ketten-produkt #21`); sie ist zu einer Modellauswahl
umgestellt worden, deren Leistung nicht das Ableiten, sondern die Entscheidung ist.

Der urspruengliche Vorschlag, der zu dieser Entscheidung gefuehrt hat:
Der Schnitt war damit repariert,
aber noch nicht sauber: Sachkontext-Modelle mit \(e\)-Termen stehen weiterhin in beiden
Trainern. Vorschlag **A** (bevorzugt): `11-ableitung-ketten-produkt` behaelt die reinen
Regel- und Verfahrensaufgaben samt „waagerechter Tangente"; seine drei Sachkontext-Aufgaben
`#24`, `#31`, `#34` wandern hierher oder werden dort durch Regelaufgaben ersetzt. Vorschlag
**B**: umgekehrter Schnitt — alle \(e\)-Terme verlassen `ketten-produkt`, was dort aber die
Stufen 3, 5 und 6 fast leerraeumen wuerde. Ich halte A fuer den kleineren Eingriff; die
Entscheidung gehoert zu Block A1 und ist hier nicht getroffen. — Entschieden wurde A in der
oben festgehaltenen, geschaerften Form.

---

### 11-e-funktion

Audit: KEIN_AFB3 L5 **und** L6; KOLLAPS L5/L6; KURZ (Stufen 1–4); DUENNER_WEG (alle Stufen).
Neu geschrieben: Stufe 5 und 6 vollstaendig (#25–#36). In Stufe 1–4 wurden die zehn
Aufgaben mit zu duennem Weg (#5, #6, #11, #12, #17, #18, #19, #20, #22, #23) um einen
vollstaendigen Rechenweg und eine Kontrolle ergaenzt; die Aufgabentexte dieser Nummern
sind zugleich zu ganzen Fragesaetzen ausgebaut (Befund KURZ).
Im Review-Nachtrag wurden ausserdem #23 und #24 der Stufe 4 ersetzt (vorher AFB I) sowie
die Tipps von #21, #23 und #24 auf das Vorgehen umgestellt.

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | zwei Messwerte, Anfangsbestand kuerzt sich heraus; \(k=\frac{\ln 2{,}5}{5}\approx 0{,}183\) |
| 26 | 5 | Fehler in vorgelegter Rechnung: Logarithmus einer Summe gliedweise zerlegt; richtig ist Substitution \(u=e^x\), \(x=\ln 3\) |
| 27 | 5 | Parameter aus zwei Bedingungen \(f(1)=5\), \(f(5)=80\); Division beseitigt \(a\), \(k=\ln 2\approx 0{,}693\) |
| 28 | 5 | Halbwertszeit in nicht ganzzahligem Vielfachen: \(2^{-2{,}5}\approx 17{,}7\,\%\); Fehlweg lineares Fortschreiben |
| 29 | 5 | zwei Wachstumsmodelle gleichsetzen, \(e\)-Potenzen zusammenfassen; \(t=\frac{\ln 2{,}5}{0{,}06}\approx 15{,}3\) |
| 30 | 5 | zweischrittig: Abkuehlkonstante aus Messung, dann Zielzeit; \(t\approx 22{,}0\) min, Umgebungstemperatur zuerst abziehen |
| 31 | 6 | Abi-Format, Sachkontext Medikament: Behauptung ueber Restanteil beurteilen (MC), Vorfaktor kuerzt sich |
| 32 | 6 | Abi-Format: aus Anteil nach 3 h auf 9 h schliessen ueber \((e^{-3k})^3=0{,}6^3\); Fehlweg lineare Fortschreibung |
| 33 | 6 | Schar \(f_a(x)=e^x-ax\): Beruehrung der \(x\)-Achse als zwei Bedingungen, \(a=e\approx 2{,}72\); Fallunterscheidung \(a<e\)/\(a>e\) im Weg |
| 34 | 6 | Abi-Format Sachkontext Bauteil: Behauptung „Temperatur faellt unter \(20\) °C" widerlegen (MC); Asymptote, Probe \(T(60)\approx 20{,}15\) |
| 35 | 6 | Abi-Format Sachkontext: Zeitpunkt der Unterschreitung, Monotonie begruendet das „erstmals" |
| 36 | 6 | Abi-Format Sachkontext Algen: Zeitpunkt fuer \(80\,\%\) Bedeckung, \(t=\frac{\ln 160}{0{,}4}\approx 12{,}7\); Modellkritik und Fallunterscheidung nach dem Zielwert im Weg |

### 11-e-funktion-ableitung

Audit: der schwaechste Trainer der Welle — KEIN_AFB3 L5 **und** L6; KOLLAPS L1/L2, L4/L5
**und** L5/L6; KURZ (Stufen 1,2,3,4,6); DUENNER_WEG (alle Stufen).
Neu geschrieben: Stufe 4, 5 und 6 vollstaendig (#19–#36). Die alte Stufe 4/5 bestand aus
Extremstellen- und Wendestellen-Aufgaben und gehoerte damit inhaltlich in
`11-extrempunkte-wendepunkte`; sie wurde durch Ableitungs-, Tangenten- und
Aenderungsratenaufgaben ersetzt. Die beiden Integral-Aufgaben der alten Stufe 6
(#34, #35) sind entfallen — Integralrechnung ist TH-Stoff der Klasse 12; die uebersehene
Stammfunktions-Aufgabe #2 der Stufe 1 ist im Review-Nachtrag ebenfalls ersetzt worden.
In Stufe 2/3 wurden #10, #12 und #15 um einen vollstaendigen Weg ergaenzt.
Die Gate-Warnung zu #36 (MC-Laenge) ist mit der Neufassung erledigt.

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | Tangentensteigung an \((3x-2)e^{x}\) bei \(x=2\): Produktregel und Ausklammern, \(7e^2\approx 51{,}72\) |
| 20 | 4 | Tangentensteigung als Ableitungswert, Vorzeichen der inneren Ableitung; \(-0{,}5e^{-1}\approx -0{,}184\) |
| 21 | 4 | Umkehraufgabe: Vorfaktor aus geforderter Steigung, \(a=2e^{-2}\approx 0{,}271\) |
| 22 | 4 | Modellauswahl: welches von vier Bestandsmodellen hat bei \(t=2\) die Rate null (MC); Fehlweg „Funktionsterm statt Ableitung null setzen" im Weg benannt |
| 23 | 4 | Modell aus Text: momentane Aenderungsrate \(N'(10)=48e^{0{,}6}\approx 87{,}5\); Bestand vs. Rate |
| 24 | 4 | zweimal Produktregel: \(f''(1)\) von \(x\,e^{2x}\), \(8e^2\approx 59{,}11\) |
| 25 | 5 | Fehler in vorgelegter Rechnung: Produktregel als Produkt der Ableitungen; richtig \(5e^{5x}\) (MC) |
| 26 | 5 | Parameter aus zwei Bedingungen \(f(1)=0\), \(f'(1)=2e\); \(a=2\), Auswertung bewusst nicht bei \(x=0\) |
| 27 | 5 | drei Schritte: Produktregel, Tangentengleichung, Auswertung an der \(y\)-Achse; \(4e^{-2}\approx 0{,}541\) |
| 28 | 5 | Umkehraufgabe: Stelle mit Tangentensteigung \(6\) bei \(e^{2x}\); Vorfaktor vor dem Logarithmieren beseitigen, \(\frac{\ln 3}{2}\approx 0{,}549\) |
| 29 | 5 | Fehler in vorgelegter Tangentengleichung an \(e^{3x}\): Steigung \(e^3\) statt \(3e^3\) (MC), mit Zahlenprobe |
| 30 | 5 | Abnahmerate \(3\) an der Stelle \(x=4\), gesucht der Funktionswert; \(f'=-0{,}5\,f\) liefert \(6\) ohne Kenntnis von \(a\) |
| 31 | 6 | Abi-Format Sachkontext Ausstellung: Zu- oder Abnahme aus dem Vorzeichen von \(B'(7)\approx -11{,}8\) beurteilen (MC) |
| 32 | 6 | Abi-Format Umkehraufgabe: Vorfaktor aus der Abbaurate \(9\) mg/h nach zwei Stunden, \(a=30e^{0{,}6}\approx 54{,}7\) |
| 33 | 6 | Tangente vom Ursprung an \(e^x\): Ansatz an unbekannter Beruehrstelle, \(x_0=1\) |
| 34 | 6 | Abi-Format Sachkontext: zwei Teilbehauptungen zu \(12e^{-0{,}3t}+3\) getrennt pruefen (MC) — Rate gegen null, Konzentration stets ueber \(3\) |
| 35 | 6 | Abi-Format Sachkontext Tank: Zuflussrate als Ableitung, \(t=\frac{\ln 2{,}5}{0{,}2}\approx 4{,}58\) |
| 36 | 6 | Abi-Format Sachkontext: zwei Zerfallsraten gleichsetzen, \(e\)-Potenzen zusammenfassen; \(t=\frac{\ln 4}{0{,}03}\approx 46{,}2\) Jahre |

### 11-monotonie-kruemmung

Audit: KEIN_AFB3 L5; KOLLAPS L2/L3 **und** L3/L4; KURZ (Stufen 1,3,4,5); DUENNER_WEG (Stufen 1,2,3,5).
Neu geschrieben: Stufe 4, 5 und 6 vollstaendig (#19–#36) — Stufe 4 wegen des Kollapses L3/L4.
Die alte Stufe 5/6 bestand fast durchgaengig aus „Anzahl Wendepunkte" und gehoerte damit in
`11-extrempunkte-wendepunkte`; dieser Trainer beschreibt jetzt durchgaengig **Intervalle**
(Monotonie, Kruemmung) und das Vorzeichenverhalten von \(f'\) und \(f''\).
In Stufe 1/2 wurden #3, #4, #7, #8, #9 und #10 um einen vollstaendigen Weg ergaenzt.
Die Gate-Warnung zu #14 ist behoben: der Tipp nennt nicht mehr den Loesungswert \(-12\),
sondern nur noch das Vorgehen.

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | Monotonie allein aus der faktorisierten Ableitung \((x-1)^2(x-4)\) (MC); doppelte Nullstelle ohne Vorzeichenwechsel |
| 20 | 4 | Umkehraufgabe: kleinster Parameter fuer Monotonie auf ganz \(\mathbb{R}\); \(a=0\) als Grenzfall mit Begruendung |
| 21 | 4 | Laenge des fallenden Intervalls aus \(3(x-1)(x-5)\); Ergebnis \(4\) |
| 22 | 4 | Kruemmungsbereich aus \(f''=12(x-1)(x+1)\) (MC); rechtsgekruemmt auf \((-1;1)\) |
| 23 | 4 | Modell aus Text: Wasserstand steigt bis \(t=6\), Uebersetzung „steigt" \(\to\) \(h'>0\) |
| 24 | 4 | Vorzeichenangaben zu \(f'\) und \(f''\) getrennt lesen und zu einem Verlauf zusammensetzen (MC) |
| 25 | 5 | zwei Bedingungen: \(a\) aus dem Kruemmungswechsel, \(b\ge 12\) aus der Diskriminante; Grenzfall Sattelpunkt |
| 26 | 5 | Fehler in vorgelegter Begruendung: \(f''=0\) ohne Vorzeichenwechsel bei \((x-2)^4\) (MC) |
| 27 | 5 | \(f''=12(x-1)^2\ge 0\): keine Rechtskruemmung, gesuchte Laenge \(0\) — Grenzfall |
| 28 | 5 | zwei Verfahren kombiniert: fallendes Intervall \(\cap\) linksgekruemmter Bereich, Laenge \(1\) |
| 29 | 5 | Parameter aus Kruemmungswechsel und \(f'(1)=3\); \(a=-\tfrac13\approx -0{,}333\) |
| 30 | 5 | Fallunterscheidung ueber die Diskriminante, Abzaehlen ganzer \(c\); \(3\) Werte, Grenzfall \(c=3\) enthalten |
| 31 | 6 | Abi-Format „Zeigen Sie": Monotonie ueber \(f'=3(x+1)^2\) begruenden (MC), Scheinbegruendungen als Distraktoren |
| 32 | 6 | Abi-Format Sachkontext: Behauptung ueber Zunahme im ganzen Intervall widerlegen (MC); \(h'\) hat zwei Nullstellen im Bereich |
| 33 | 6 | Fallunterscheidung \(a<0\), \(a=0\), \(a>0\) fuer die Anzahl der Kruemmungswechsel (MC); genau einer ist unmoeglich |
| 34 | 6 | Abi-Format Sachkontext Strasse: linksgekruemmte Laenge \(10\) im Abschnitt \([0;20]\) |
| 35 | 6 | zwei Bedingungen: \(a\) aus Kruemmungswechsel, \(b=-9\) aus der Laenge des fallenden Intervalls |
| 36 | 6 | Fallunterscheidung ueber die Diskriminante, Abzaehlen ganzer \(k\); \(7\) Werte, beide Grenzfaelle geprueft |

### 11-extrempunkte-wendepunkte

Audit: KEIN_AFB3 L5 **und** L6; KOLLAPS L1/L2 und L2/L3; DUENNER_WEG (Stufen 1,2,5).
Neu geschrieben: Stufe 5 und 6 vollstaendig (#25–#36). Die alte Stufe 5/6 bestand aus
Wiederholungen der Stufe 3 („\(y\)-Wert des Hochpunkts", „Anzahl Wendepunkte") und enthielt
keine AFB-III-Leistung. In Stufe 1–3 wurden #1, #2, #3, #4, #8, #9, #13, #14, #15, #16 und #17
um einen vollstaendigen Weg ergaenzt (Befund DUENNER_WEG).
Die Gate-Warnungen zu #33 und #36 (MC-Laenge) sind mit den neuen Aufgaben erledigt. Im
Review-Nachtrag wurden ausserdem #34 und #36 in Abi-Format ueberfuehrt und die sechs Tipps
der Stufe 4 (#19–#24) neu formuliert, weil sie Zwischenloesungen nannten oder blosse
Stichworte waren; die Loesungswege von #19, #20, #21 und #24 sind dabei von Ergebniszeilen
zu vollstaendigen Wegen ausgebaut worden.
KOLLAPS L1/L2 und L2/L3 bleibt offen — Stufe 1–3 werden laut Plan nicht neu geschrieben.

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | Parameter aus zwei Bedingungen (Hochpunkt bei \(1\), Tiefpunkt bei \(3\)); \(a=-6\), Zuordnung der Arten geprueft |
| 26 | 5 | Fehler in vorgelegter Rechnung: Hoch- und Tiefpunkt vertauscht (MC), hinreichende Bedingung an beiden Stellen |
| 27 | 5 | Grenzfall: \(f'=3(x-1)^2\) ohne Vorzeichenwechsel, \(f''(1)=0\) — Anzahl der Extrempunkte \(0\) |
| 28 | 5 | beide Wendestellen bestimmen, Vorzeichenwechsel pruefen, groessere einsetzen; \((2;-16)\) |
| 29 | 5 | Parameter aus Wendepunktlage und Funktionswert; \(a=0{,}5\), Vorzeichenwechsel kontrolliert |
| 30 | 5 | Sattelpunkt als Doppelbedingung \(f'=f''=0\); \(b=12\), dritte Angabe als ueberzaehlige Information |
| 31 | 6 | Abi-Format Sachkontext Gewinn: Behauptung ueber das Maximum mit Vorzeichenwechsel und Randwert pruefen (MC) |
| 32 | 6 | Abi-Format mehrschrittig: notwendige Bedingung, hinreichende Bedingung, Randvergleich; \(t=8\) |
| 33 | 6 | Fallunterscheidung \(c<0\), \(c=0\), \(c>0\); \(3\) ganze Zahlen, Grenzfall \(c=0\) ausdruecklich ausgeschlossen |
| 34 | 6 | Abi-Format Sachkontext Aufforstung: groesster Zuwachs ueber \(N''\) mit Vorzeichenwechsel, \(t=7\); Bestand \(1736\) gegen Rate \(297\) abgegrenzt |
| 35 | 6 | Parameter aus zwei Bedingungen (Extremstelle und Funktionswert); \(a=2\), Art des Extremums nachgeprueft |
| 36 | 6 | Abi-Format Sachkontext Gewinn: aus \(G'(1)=G''(1)=0\) faelschlich auf einen Sattelpunkt geschlossen; ueber \(G'=4(x-1)^3\) als Tiefpunkt widerlegen (MC) |

---

### Offen (bewusst nicht in dieser Welle)

- KOLLAPS L1/L2 und L2/L3 in `11-extrempunkte-wendepunkte` sowie L2/L3 in
  `11-monotonie-kruemmung`: Stufe 1–3 werden nach Plan nur nachgebessert, nicht neu geschrieben.
- In `11-e-funktion` sind Stufe 1–3 weiterhin ueberwiegend Ein-Schritt-Aufgaben zu den
  Potenzgesetzen; inhaltlich richtig, aber eng am Kollaps L2/L3.
- `11-e-funktion` L3 arbeitet mit \(\ln\); der eigene ln-Trainer entsteht erst im Block 11B
  (Ersatz `11-lk-newton`). Ueberschneidungen dort beim Schreiben pruefen.

---

### Review-Nachtrag 2026-09-30

Behoben nach der Pruefung durch den Review-Agenten. Rechnerisch war nichts zu beanstanden;
die Befunde betrafen Lehrplanzuordnung, Dubletten mit dem Nachbarblock und die Stufenlogik.

**Lehrplan.** `11-e-funktion-ableitung #2` fragte nach der Stammfunktion von \(e^x\) samt
Integrationskonstante — Klasse-12-Stoff, uebrig geblieben beim Entfernen der beiden
Integralaufgaben aus der alten Stufe 6. Ersetzt durch eine Ableitungsaufgabe der Stufe 1
(Steigung von \(e^x\) an der Stelle \(x=1\), Ergebnis \(e\approx 2{,}72\), mit dem Hinweis,
dass Steigung und Funktionswert hier ueberall uebereinstimmen).

**Dubletten mit `11-ableitung-ketten-produkt` (Block A1).** Siehe die Korrektur oben. Getauscht
wurden in `11-e-funktion-ableitung`:

| id | vorher | jetzt |
|---|---|---|
| 19 | \(x^2e^{3x}\), \(f'(1)\) — neben `ketten-produkt #19` | Tangentensteigung an \((3x-2)e^{x}\) bei \(x=2\); \(7e^2\approx 51{,}72\) |
| 24 | \(a\) aus \(f''(0)=9\) bei \(e^{ax}\) — neben `ketten-produkt #22` | \(f''(1)\) von \(x\,e^{2x}\); \(8e^2\approx 59{,}11\), zweimal Produktregel |
| 28 | waagerechte Tangente an \(e^{2x}-4e^{x}\) | Umkehraufgabe: Stelle mit Tangentensteigung \(6\); \(\tfrac{\ln 3}{2}\approx 0{,}549\) |
| 30 | waagerechte Tangente an \(e^{-x}(x^2+2x)\) — neben `ketten-produkt #26` | Abnahmerate \(3\) an der Stelle \(x=4\), gesucht der Funktionswert; \(f'=-0{,}5f\) liefert \(6\) |
| 31 | \(5t\,e^{-0{,}5t}\) mg/l — praktisch identisch mit `ketten-produkt #24` | Besucherzahl \(120\,t\,e^{-0{,}2t}\), Beurteilung am siebten Tag; \(B'(7)\approx -11{,}8\) |
| 32 | \(a\,t\,e^{-kt}\) mit Maximum bei \(t=2\) — neben `ketten-produkt #31` | \(a\) aus der Abbaurate \(9\) mg/h nach zwei Stunden; \(a=30e^{0{,}6}\approx 54{,}7\) |
| 36 | Fallunterscheidung waagerechte Tangente bei \(e^{kx}+x\) — Denkfigur von `ketten-produkt #32` | Vergleich zweier Zerfallsraten; \(t=\tfrac{\ln 4}{0{,}03}\approx 46{,}2\) Jahre |

Zusaetzlich wurde `#29` neu gefasst (Fehler in einer vorgelegten **Tangentengleichung** an
\(e^{3x}\): Steigung \(e^3\) statt \(3e^3\)), damit Stufe 5 nicht zweimal dieselbe Fehlerart
prueft.

**Stufe 6 ohne Abi-Format.** Fuenf Aufgaben waren reine Begriffs-MC ohne Kontext und ohne
Mehrschrittigkeit. Sie sind jetzt eingebettet oder ersetzt — der fachliche Kern ist in allen
Faellen erhalten geblieben:

| Aufgabe | vorher | jetzt |
|---|---|---|
| `11-e-funktion #34` | „\(e^{-x}\) wird nie negativ" | Bauteil kuehlt nach \(20+60e^{-0{,}1t}\); Behauptung „faellt unter \(20\) °C" beurteilen, mit Asymptote und Zahlenprobe \(T(60)\approx 20{,}15\) |
| `11-e-funktion #36` | Loesbarkeit von \(e^x=c\) | Algenbedeckung \(0{,}5e^{0{,}4t}\), Zeitpunkt fuer \(80\,\%\) (\(\approx 12{,}7\) Tage); die Fallunterscheidung nach \(c\) steht jetzt als Modellkritik im Loesungsweg (ab \(13{,}2\) Tagen liefert das Modell ueber \(100\,\%\)) |
| `11-e-funktion-ableitung #34` | \(f'=k\cdot f\) allgemein | Wirkstoff \(12e^{-0{,}3t}+3\); zwei Teilbehauptungen (Rate geht gegen null, Konzentration bleibt ueber \(3\)) getrennt pruefen |
| `11-extrempunkte-wendepunkte #34` | „Grad vier \(\Rightarrow\) Wendepunkt" | Aufforstung \(-t^3+21t^2+150t\): Zeitpunkt des groessten Zuwachses, \(t=7\) ueber \(N''\) mit Vorzeichenwechsel; Bestand \(N(7)=1736\) gegen Rate \(N'(7)=297\) abgegrenzt |
| `11-extrempunkte-wendepunkte #36` | \(f'(x_0)=f''(x_0)=0\), Begriffsfrage | Gewinnmodell \((x-1)^4+3\): ein Praktikant schliesst aus \(G'(1)=G''(1)=0\) auf einen Sattelpunkt; zu widerlegen ueber \(G'(x)=4(x-1)^3\) mit Vorzeichenwechsel — es ist der kleinste Gewinn |

Damit erledigt sich zugleich die Warnung zur MC-Laenge bei `#36`: die richtige Option ist
nicht mehr die einzige zweizeilige.

**Stufe 4 war teils AFB I.** In `11-e-funktion` waren `#23` (Anfangsbestand ablesen) und `#24`
(\(N(10)\) einsetzen) Ein-Schritt-Aufgaben. Jetzt: `#23` Umkehraufgabe (Anfangsbestand aus einer
Messung nach \(20\) Stunden, \(N_0=1478/e^2\approx 200\)), `#24` Modell aus Text (Verdopplungszeit
\(5\) Stunden, \(k=\tfrac{\ln 2}{5}\approx 0{,}139\)). Die Tipps von `#21`, `#23` und `#24`
nennen jetzt das Vorgehen statt der fertigen Rechnung.

**Stichwort-Tipps auf Stufe 4.** In `11-extrempunkte-wendepunkte` nannten die Tipps von `#21`
und `#23` die einzusetzende Stelle, `#19`, `#20`, `#22` und `#24` waren blosse Stichworte
(„Randwerte pruefen.", „Hinreichend."). Alle sechs neu formuliert; die Loesungswege von
`#19`–`#21` und `#24` sind zugleich von Ergebniszeilen zu vollstaendigen Wegen ausgebaut.

**Hinweis aus dem Review, der ab jetzt gilt.** Mathe-Ungleichungen im Text immer mit Leerzeichen
setzen (`\(1 < x < 5\)`), nie `1<x<5` — sonst frisst der Browser den Text ab dem Kleinerzeichen.
Das Level-Gate prueft das inzwischen hart (`html_frisst_text`).

---

# Block A3 — Anwendungen der Differentialrechnung
Lokale Nachvollziehbarkeit; im Public-HTML stehen die Kriterien bewusst nicht.
Grundlage: Rubrik aus `2026-09-26-lehrplan-th-und-level-progression-plan.md`, Befunde aus
`../audit/audit-2026-09-19-mathepfade.md` (Zeilen 108–122, 240–250, Zeile 66).
Niveau: TH-Lehrplan Kap. 4.1 gA (Ableitung, Extrem- und Wendestellen, Kurvenuntersuchung,
Extremwertaufgaben; **keine** Polynomdivision, kein Newton-Verfahren).

Lesart Kl. 11 durchgaengig:
L4 = Verfahren selbst waehlen / Modell aus Text / Umkehraufgabe;
L5 = zwei Verfahren kombinieren, Parameter aus zwei Bedingungen, Fehler in vorgelegter Rechnung;
**L6 = Abi-Format** (mehrschrittig mit Begruendungsanteil, Behauptung pruefen, Fallunterscheidung,
Grenz- und Randfall, Sachkontext) — Form der IQB-Aufgaben gA als Vorlage.

Jede Loesung mit Wolfram nachgerechnet; bei Extremwertaufgaben zusaetzlich **Art des Extremums
und Randfall** geprueft, bei Steckbriefaufgaben die **Probe gegen alle Bedingungen** gerechnet.
Bilder L5/L6 je Trainer per `tests/bild.py` erzeugt und angesehen.

### Abgrenzung der drei Trainer (gegen sinngleiche Aufgaben)

| Trainer | Gegenstand |
|---|---|
| 11-extremwertaufgaben | Optimierung mit Nebenbedingung aus Sachkontext — die Leistung ist das **Aufstellen der Zielfunktion** |
| 11-kurvendiskussion-ganzrational | vollstaendige Untersuchung einer **gegebenen** Funktion (Nullstellen, Symmetrie, Extrema, Wendepunkte, Randverhalten) |
| 11-steckbriefaufgaben | Funktion aus Eigenschaften **rekonstruieren** (Gleichungssystem aus Bedingungen, Probe) |

Abstand gehalten zu `11-extrempunkte-wendepunkte` und `11-monotonie-kruemmung` (dort gehoert das
reine Bestimmen von Extrem- und Wendestellen hin; hier steckt es jeweils im groesseren Zusammenhang)
sowie zu `11-tangenten-normalen`.

---

### 11-extremwertaufgaben

Audit: KEIN_AFB3 L5 **und** L6; DUENNER_WEG (Stufen 1, 2, 6). Gate-Warnung: #30 (MC-Laenge).
Der im Audit genannte KaTeX-Fehler `V_\max` war bereits als `V_{\max}` korrigiert (nachgeprueft).

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | Umkehraufgabe mit Parameter: Optimum allgemein mit \(a\) bestimmen, dann \(V_{\max}=\frac{2a^3}{27}=1024\) nach \(a\) aufloesen (\(a=24\)) |
| 26 | 5 | Fehler in vorgelegter Rechnung: falsche Nebenbedingung \(a+b=30\) statt \(15\) — schon Schritt 1 |
| 27 | 5 | Parameter aus zwei Bedingungen: Rechteck unter \(y=a-x^2\), groesste Flaeche genau \(32\) (\(a=12\)) |
| 28 | 5 | Zielfunktion aus Sachkontext: Gewinn = Erloes − Kosten, beide Kandidaten \(x=0\) und \(x=4\) beurteilen |
| 29 | 5 | Abstand ueber \(d^2\); drei Kandidaten, **Art des Extremums** entscheidet (mittlerer ist ein Maximum) |
| 30 | 5 | **Randfall**: Zaun an nur \(12\,\text{m}\) langer Wand — freies Optimum unzulaessig, Maximum am Rand (\(168\)) |
| 31 | 6 | Abi-Format: Leitungstrasse mit zwei Preisen — Zielfunktion \(5\sqrt{9+x^2}+3(8-x)\) selbst aufstellen, Randvergleich, Minimum im Innern (\(2{,}25\)) |
| 32 | 6 | „Zeigen Sie" als MC: offener Zylinder minimaler Oberflaeche erfuellt \(h=r\) **fuer jedes** \(V\) |
| 33 | 6 | Abi-Format mehrschrittig: Tunnelquerschnitt Rechteck + Halbkreis, Umfang \(10\,\text{m}\), \(b=\frac{20}{4+\pi}\approx 2{,}80\) |
| 34 | 6 | **Randfall** mit Nebenbedingung: Tank \(4000\,\text{cm}^3\), Grundkante hoechstens \(10\,\text{cm}\) (\(O=1700\)) |
| 35 | 6 | Behauptung beurteilen (MC): \(A_{\max}=\frac{U^2}{16}\) — doppelter Umfang vervierfacht die Flaeche |
| 36 | 6 | Abi-Format mit gewichteten Kosten: Deckel/Boden doppelt so teuer, \(r=\frac{5}{\sqrt[3]{\pi}}\approx 3{,}41\), Deutung \(h\approx 4r\) |

DUENNER_WEG behoben in #5, #6, #7, #9, #10, #11, #12, #13, #14, #15, #16, #17, #19, #20, #24:
Loesungswege zeigen jetzt Nebenbedingung → Zielfunktion → Ableitung → Art des Extremums.
##30 (alte Begriffsabfrage zur Randwertbetrachtung, zugleich MC-Laengen-Warnung) ist durch eine
echte Randfall-Rechnung ersetzt; die Randbetrachtung wird jetzt **gerechnet** statt abgefragt.

### 11-kurvendiskussion-ganzrational

Audit: KEIN_AFB3 L6; DUENNER_WEG (Stufen 1–5). Lehrplan-Gate: #11 nannte „Polynomdivision".
Gate-Warnung: #34 (Tipp enthielt den Loesungswert 16).

| id | Level | Kriterium |
|---|---|---|
| 11 | 2 | **Pflicht-Fix**: Nullstellen von \(x^3+2x^2-8x\) ueber Ausklammern, Vieta und Satz vom Nullprodukt statt Polynomdivision |
| 25 | 5 | Fehler in vorgelegter Argumentation: „hoechster Exponent gerade ⇒ achsensymmetrisch" — Probe mit \(f(-x)\) |
| 26 | 5 | Zwei Teiluntersuchungen an **einer gegebenen** Funktion: Wendestellen und Nullstellen von \(x^4-8x^2+7\) vergleichen |
| 27 | 5 | Zwei Verfahren: Wendestelle bestimmen, dort \(f'\) auswerten (Wendetangente, \(-12\)) |
| 28 | 5 | Sachkontext mit **Randbetrachtung**: Wasserstand auf \([0;7]\), Vergleich der Randwerte |
| 29 | 5 | Faktorisieren als Schluessel: \(f'=4(x-1)^3\), \(f''(1)=0\) — Vorzeichenwechsel entscheidet |
| 30 | 5 | Aus dem Graphen von \(f'\) auf \(f\) schliessen (MC, Ebenenwechsel Ableitung → Funktion) |
| 31 | 6 | **Fallunterscheidung/Grenzfall**: \(x^3-3x+c\) mit drei Nullstellen nur fuer \(-2<c<2\), groesste ganze Zahl \(1\) |
| 32 | 6 | Allgemeine Aussage ueber **jede** Funktion dritten Grades (genau ein Wendepunkt) mit Gegenbeispielen |
| 33 | 6 | Abi-Format Sachkontext: Talquerschnitt, tiefster Punkt gegen hoechsten **Randpunkt** (\(6{,}25\)) |
| 34 | 6 | Behauptung zur **vollstaendigen Diskussion** (MC): zwei Wendepunkte erzwingen nicht drei Extremstellen, Gegenbeispiel \(x^4-6x^2+20x\) |
| 35 | 6 | Fallunterscheidung ueber die Diskriminante: genau eine waagerechte Tangente fuer \(a=3\), dort Sattelpunkt |
| 36 | 6 | Begruendungsanteil **im Arbeitsauftrag**: aus der Lage von Hoch- und Tiefpunkt die Anzahl der Nullstellen herleiten (\(3\)) |

DUENNER_WEG behoben in #1, #6, #10, #12, #13, #14, #16, #17, #21, #22.

### 11-steckbriefaufgaben

Audit: KEIN_AFB3 L5 **und** L6; DUENNER_WEG (Stufen 1, 2, 4, 5, 6). Der in Audit-Zeile 66 genannte
Ein-Zeilen-Weg von #2 (`\(f(2)=5\).`) war bereits ausgebaut (nachgeprueft).

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | Vier Bedingungen, vier Unbekannte: Wendepunkt \((1\mid2)\), Steigung \(-3\), \(f(0)=6\) (\(a=-1\)), Probe gegen alle vier |
| 26 | 5 | „Beruehrt die \(x\)-Achse" in doppelte Nullstelle uebersetzen, Produktansatz \(a(x-3)^2\) (\(a=2\)) |
| 27 | 5 | Fehler in vorgelegtem Ansatz: Hochpunkt verlangt \(f'=0\), nicht \(f''=0\) |
| 28 | 5 | Vielfachheiten in Produktdarstellung uebersetzen, ausmultiplizieren, Koeffizientenvergleich (\(b=-3\)) |
| 29 | 5 | Sachkontext (Strassenfuehrung): knickfreier Anschluss und „wieder waagerecht" (\(a=-0{,}25\)) |
| 30 | 5 | Zwei Extremstellen als Nullstellen **derselben** Ableitung lesen, System loesen, Art pruefen (\(b=-6\)) |
| 31 | 6 | Abi-Format: Wendepunkt, Wendetangentensteigung und \(f(0)=0\) — vier Gleichungen (\(a=4\)), Probe |
| 32 | 6 | Symmetrieansatz erkennen (nur gerade Exponenten), drei Angaben genuegen (\(a=1\)) |
| 33 | 6 | Beurteilen (MC): Bedingungen zaehlen — fuenf Gleichungen fuer vier Unbekannte, **ueberbestimmt** |
| 34 | 6 | Abi-Format Sachkontext: Rutsche mit vier Bedingungen, danach \(f'(3)=-1{,}5\) auswerten |
| 35 | 6 | Begruendungsformat (MC): Bedingungen erzwingen \(a=0\) — das System ist loesbar, aber **nicht** mit Grad drei |
| 36 | 6 | Behauptung pruefen (MC): Sattelpunkt mit Koordinaten liefert drei, eine Sattel**stelle** nur zwei Bedingungen |

DUENNER_WEG behoben in #11, #15, #17, #19 (die uebrigen Stufen 1–4 waren bereits ausgebaut).
MC-Laengen in #33 und #36 angeglichen, damit die richtige Option nicht die laengste ist.

---

#### Review-Nachtrag 2026-09-30

Der Pruef-Agent hat alle 36 neuen Aufgaben nachgerechnet: **kein Rechenfehler**, beide Randfaelle,
die Extremum-Arten, die allgemeine Herleitung h = r und saemtliche Steckbrief-Proben bestaetigt.
Die Befunde lagen in der **Abgrenzung**. Behoben:

- **Dublette ueber Trainer hinweg**: `11-kurvendiskussion #34` (Behauptung `f''=0` ⇒ Wendepunkt,
  Gegenbeispiel \((x-a)^4\)) stand sinngleich in `11-monotonie-kruemmung #26` und
  `11-extrempunkte-wendepunkte #36`. Ersetzt durch eine Behauptung, die auf die vollstaendige
  Diskussion zielt: zwei Wendepunkte erzwingen **nicht** drei Extremstellen
  (Gegenbeispiel \(x^4-6x^2+20x\), dessen \(f'\) nur eine reelle Nullstelle hat).
- **Abgrenzung verletzt**: `11-extremwertaufgaben #31` war reine Extremstellenbestimmung an einer
  **gegebenen** Gewinnfunktion — das gehoert zu `11-extrempunkte-wendepunkte` (dort auch schon der
  Gewinn-Sachkontext). Ersetzt durch eine Leitungstrasse mit zwei Preisen: die Zielfunktion muss
  aus der Sachsituation aufgestellt werden, der Randvergleich bleibt erhalten.
- **Steckbrief-Muster im falschen Trainer**: `11-kurvendiskussion #26` war reine Parameter-
  bestimmung aus zwei Bedingungen (Muster von `11-steckbriefaufgaben #25/#31/#32`). Ersetzt durch
  zwei Teiluntersuchungen an **einer gegebenen** Funktion (Wendestellen gegen Nullstellen).
  `#35` (Diskriminanten-Fall) bleibt als vertretbare Parameter-Variante.
- **Begruendung nur im Loesungsweg**: `11-kurvendiskussion #36` verlangte die Deutung nicht.
  Der Arbeitsauftrag fordert jetzt ausdruecklich die Herleitung der Nullstellenzahl aus der Lage
  von Hoch- und Tiefpunkt.
- **L6 zu duenn**: `11-steckbriefaufgaben #35` war eine einzige Gleichung, formatnah an
  `11-monotonie-kruemmung #29`. Ersetzt durch ein Begruendungsformat: Die Bedingungen sind in sich
  stimmig, erzwingen aber \(a=0\) — eine Funktion dritten Grades mit diesen Eigenschaften gibt es
  nicht. Das war der konkrete Hebel hinter dem selbst gemeldeten „L6 formatarm"; `#31/#32/#34`
  hat der Pruefer ausdruecklich als in Ordnung bestaetigt.
- **Tipps und Fragen mit der Loesung** (Altbestand): `11-extremwertaufgaben #21` (Tipp
  „Quadrat 25×25" lieferte 625), `11-kurvendiskussion #20` (Tipp „HP bei x=0", Loesung 0),
  `11-steckbriefaufgaben #20` (fertige Zwischengleichung \(b=-3a\)), `#23` (Loesungswert),
  `#24` (die **Frage** enthielt den Rechenweg „wegen \(f'(0)=0\)"). Alle auf den Denkanstoss
  zurueckgeschnitten, der Rechenweg aus der Frage entfernt.
- **Kleinigkeiten**: `11-extremwertaufgaben #17/#22` schrieben `cm³` als Unicode-Hochzahl (jetzt
  \(	ext{cm}^3\)); `#17` nannte die Loesung von `#16` in der eigenen Frage und ist jetzt
  selbsttragend. `11-kurvendiskussion #28` war die dritte „Wasserstand eines Beckens"-Einkleidung
  in Kl. 11 — gleiche Mathematik, jetzt Gewaechshaus-Temperatur.
  `11-steckbriefaufgaben #30` war die dritte Scheitel-Aufgabe nach `#9`/`#21` und kaum ueber L4
  hinaus — ersetzt durch zwei Extremstellen als Nullstellen derselben Ableitung. In `#23/#24`
  rendert der Punkt jetzt als \((2 \mid -2)\), vorher wirkte `|` neben dem Minus wie ein
  Betragsstrich (nur im Bild sichtbar).

Ein Befund kam erst aus der **Sichtpruefung** der Einzelaufgaben: `11-extremwertaufgaben #22`
hatte \(V = 1\,\text{l} = 1000\,\text{cm}^3\) und rendert im Browser als „V = 11 = 1000 cm³" —
das Liter-\(l\) ist in der Mathe-Schrift von der Ziffer \(1\) nicht zu unterscheiden. Kein Gate
sieht das (KaTeX rendert fehlerfrei). Jetzt „\(1\,\text{Liter}\)" ausgeschrieben.

Neue Zahlen mit Wolfram nachgerechnet: Trassenminimum \(x=	frac94\) mit \(K=36\) (Raender 39
und 42,7); \(4x^3-12x+20\) hat genau eine reelle Nullstelle; das Steckbrief-System liefert
\(a=0,\; b=-4,\; c=8\). Volle Pruefschleife gelaufen, PNG je geaenderter Aufgabe angesehen.

### Offen (bewusst nicht in dieser Welle)

- **Paare aus Stelle und Wert** in Stufe 1–3 (`11-extremwertaufgaben` #7/#8, #10/#11): Der Pruef-Agent
  bestaetigt, dass das ein **repo-weites Muster** ist und als eine Entscheidung angefasst gehoert,
  nicht trainerweise. Bewusst stehen gelassen. (#16/#17 ist entschaerft: #17 nennt die Loesung von
  #16 nicht mehr und traegt die Optimierung selbst.)
- `11-kurvendiskussion-ganzrational`: **10 von 12** Aufgaben auf Stufe 3 und 4 fragen nach \(x\)- oder
  \(y\)-Koordinaten von Extrem- und Wendepunkten. Das braucht einen eigenen Stufen-3/4-Durchgang und
  war nicht Auftrag dieser Welle (der Plan schreibt nur Stufe 5/6 neu).
- `11-steckbriefaufgaben`: Stufe 6 hat jetzt drei Begruendungs- und drei Rechenformate (#33, #35, #36
  gegen #31, #32, #34); der Pruefer haelt diese Mischung fuer angemessen. Erledigt.
- Die Abgrenzung gegen `11-extrempunkte-wendepunkte` wurde nur einseitig geprueft (aus diesen drei
  Trainern heraus); der dortige Implementierer sollte die Gegenrichtung pruefen.

---

# Block B — erhoehtes Anforderungsniveau (eA)
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

### 11-lk-newton → ln-Funktion (eA), Ersatz-Trainer

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

### 11-lk-funktionsscharen

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

### 11-lk-gebrochen-rational

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

### 11-lk-kurvendisk-erweitert

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

### Beim Schreiben vermiedene Dubletten

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

### Gate-Ergebnisse

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

### Offen (bewusst nicht in dieser Welle)

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

---

### Review-Nachtrag 2026-09-30

Der Pruef-Agent hat alle 144 Aufgaben nachgerechnet: kein falscher Loesungswert. Behoben
wurden die folgenden Form- und Dublettenbefunde.

#### MUSS

- **`11-lk-gebrochen-rational #17`**: Der Tipp nannte die Antwort („Von rechts strebt es gegen
  plus unendlich"). Jetzt nur noch das Verfahren (Vorzeichen des Nenners rechts von 1).
- **`11-lk-kurvendisk-erweitert` Stufe 1-3 komplett neu (18 Aufgaben).** Grund: `#6` war
  wortgleich `11-kurvendiskussion-ganzrational #15`, `#14` wortgleich dessen `#22`, `#4/#5`
  Spiegelbilder von dessen `#13/#14`; dazu Stufen-Kollaps (jede Stufe eine ganzrationale
  Funktion in denselben sechs Teilfragen). Die Stufen tragen jetzt denselben Zuschnitt wie
  Stufe 4-6: L1 Symmetrie, Werte und Nullstellen zusammengesetzter Terme; L2 Produkt- und
  Kettenregel bei e- und trigonometrischen Termen; L3 Extrem- und Wendestellen von
  \(x^{2}e^{-x}\), \(e^{x}-2x\) und \((x-1)e^{x}\). Damit sind Befund 2 und Befund 6 erledigt.

#### SOLLTE

- `11-lk-gebrochen-rational #24`: verriet ueber die Frage die Loesung von `#23` (dieselbe
  Funktion, Extremstelle 2 gegen \(f(2)\)) und war reines Einsetzen. Ersetzt durch eine
  Umkehraufgabe: Parameter \(c\) aus der vorgegebenen Nullstelle von \(\frac{2x+c}{x-4}\).
- **Tipps mit fertiger Gleichung** auf den unteren Stufen umgestellt:
  `11-lk-funktionsscharen #7, #9, #11, #13, #17, #18, #23`;
  `11-lk-gebrochen-rational #2, #8, #9, #16, #19, #20`;
  in `11-lk-kurvendisk-erweitert` mit dem Neuschrieb von Stufe 1-3 erledigt.
  Damit sind auch die Nachbar-Leaks weg (`#15`-Tipp nannte die Loesung von `#14` usw.).
- `11-lk-funktionsscharen #19-#22`: Vier gleichartige Aufgaben („Stelle, an der der Parameter
  herausfaellt"). `#20` und `#21` ersetzt — `#20` Umkehraufgabe (Parameter aus der Lage einer
  waagerechten Tangente), `#21` Punktprobe. Die Stelle wird in keiner Frage mehr mitgeliefert.
- `11-lk-gebrochen-rational #15`: lag auf derselben Zerlegung wie `#14` und hatte dieselbe
  Loesung `1`. Jetzt auf \(\frac{x^{2}}{x+2}\) gelegt (Naeherungsgerade \(y=x-2\)).
- **Ersatz-Trainer L1/L2 entzerrt.** L1 heisst jetzt nicht mehr viermal „\(\ln(e^{a})=a\)",
  sondern: Definitionsbereich, Nullstelle, Verlauf des Graphen, \(\ln\frac1e\), \(\ln\sqrt{e}\),
  Vorzeichen zwischen 0 und 1. In L2 ersetzt eine qualitative Aussage ueber \(f'(x)=\frac1x\)
  die zweite Faktor-Aufgabe.
- **Aufteilung gegen `11-e-funktion` (Festlegung des Koordinators):** ln als *Werkzeug*
  (Umkehreigenschaft, Aufloesen von e-Gleichungen) bleibt dort. Im Ersatz-Trainer gestrichen:
  `#1` \(\ln e\), `#3` „Loese \(e^{x}=5\)", `#5` \(\ln(e^{4})\). Er beginnt jetzt mit
  Definitionsbereich und Verlauf und fuehrt ueber Ableitung, Kettenregel und Stammfunktion.
- **`11-lk-gebrochen-rational #17/#18` auf MC umgestellt.** Die alte Kodierung
  \(\pm\infty\) als \(\pm 1\) in einem numerischen Feld war eine Eingabefalle: Wer fachlich
  richtig „+unendlich" eintippt, wurde als falsch gewertet. Optionen jetzt: ueber alle Grenzen
  wachsend / unter jede Schranke fallend / gegen 0 / gegen eine feste Zahl.
- **MC-Laengen im Altbestand** angeglichen: `11-lk-funktionsscharen #1, #7, #17`,
  `11-lk-gebrochen-rational #1, #7`, `11-lk-kurvendisk-erweitert #1/#11` (mit dem Neuschrieb).
  Bei `#17` und `#1` der gebrochen-rationalen wanderte dabei die richtige Antwort auf Index 0.

#### KANN

- `11-lk-kurvendisk-erweitert #26`: Der falsche Weg lieferte mit \(x=0\) zufaellig eine echte
  Extremstelle. Die Aufgabe liegt jetzt auf \((x+3)e^{-x}\) — der falsche Weg fuehrt auf
  „keine Extremstelle", richtig ist \(x=-2\). Damit ist zugleich die Doppelnutzung von
  \(x^{2}e^{-x}\) in `#26` und `#31` weg; `#31` prueft jetzt \(x^{3}e^{-x}\).
- Ersatz-Trainer `#18` rechnete \((x\ln x)'\) vor, was `#27` verlangt — jetzt \(x^{2}\ln x\).
- `11-lk-funktionsscharen #27` war eine Steckbriefaufgabe ohne Scharbezug; jetzt Zweiparameter-
  Schar \(ax^{2}+bx\) mit Punkt- und Steigungsbedingung.
- „ae/ue"-Reste in den JS-Kommentaren beseitigt.

Nachgerechnet mit Wolfram wurden alle geaenderten Werte. Gates nach dem Nachtrag:
`level_check --strict` und `lehrplan_check --strict` ueber die vier Dateien Exit 0 ohne
Warnung, `katex_check` ok, `pytest tests/test_trainer.py` 28 passed, `test_index` 3 passed;
Bilder der Stufen 1 bis 6 erzeugt und angesehen.

#### Weiterhin offen

- `11-lk-funktionsscharen` Stufe 1-3 bleibt bei ganzrationalen Scharen; KOLLAPS L2/L3 ist damit
  nicht vollstaendig aufgeloest (Stufe 1-3 laut Plan nicht im Auftrag, nur entdoppelt).
- `11-lk-gebrochen-rational #16` (Kuerzen von \(\frac{x^{2}+x}{x}\)) bleibt eine sehr einfache
  Stufe-3-Aufgabe.

---
