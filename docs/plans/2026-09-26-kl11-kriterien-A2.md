# Klasse 11, Block A2 — Kriterien je Trainer (Welle Task 8, Stand 2026-09-30)

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

## Abgrenzung der vier Trainer dieses Blocks

| Trainer | Inhalt | ausdruecklich nicht |
|---|---|---|
| `11-e-funktion` | die Funktion selbst: Wachstum/Zerfall, Graph und Wertebereich, Transformationen von \(e^x\), Gleichungen mit \(e\) | Ableiten |
| `11-e-funktion-ableitung` | Ableiten von \(e\)-Termen (Ketten- und Produktregel), Tangenten an \(e\)-Funktionen, Aenderungsraten | Extrem-/Wendestellen als Aufgabenziel, Integrale |
| `11-monotonie-kruemmung` | Monotonie- und Kruemmungsintervalle, Vorzeichen von \(f'\) und \(f''\) | Bestimmen einzelner Extrem-/Wendepunkte |
| `11-extrempunkte-wendepunkte` | Extrem- und Wendestellen bestimmen, notwendige und hinreichende Bedingung, Sattelpunkt | Intervallbeschreibungen der Monotonie |

Abstand gehalten wurde ausserdem zu `11-ableitungsregeln`, `11-tangenten-normalen`
(Tangentengleichungen als Thema) und `11-kurvendiskussion-ganzrational`
(vollstaendige Kurvendiskussion).

### Korrektur 2026-09-30: die Abgrenzung zu `11-ableitung-ketten-produkt` trug zunaechst nicht

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

## 11-e-funktion

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

## 11-e-funktion-ableitung

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

## 11-monotonie-kruemmung

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

## 11-extrempunkte-wendepunkte

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

## Offen (bewusst nicht in dieser Welle)

- KOLLAPS L1/L2 und L2/L3 in `11-extrempunkte-wendepunkte` sowie L2/L3 in
  `11-monotonie-kruemmung`: Stufe 1–3 werden nach Plan nur nachgebessert, nicht neu geschrieben.
- In `11-e-funktion` sind Stufe 1–3 weiterhin ueberwiegend Ein-Schritt-Aufgaben zu den
  Potenzgesetzen; inhaltlich richtig, aber eng am Kollaps L2/L3.
- `11-e-funktion` L3 arbeitet mit \(\ln\); der eigene ln-Trainer entsteht erst im Block 11B
  (Ersatz `11-lk-newton`). Ueberschneidungen dort beim Schreiben pruefen.

---

## Review-Nachtrag 2026-09-30

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
