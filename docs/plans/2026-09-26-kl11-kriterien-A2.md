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

Abstand gehalten wurde ausserdem zu `11-ableitungsregeln`, `11-ableitung-ketten-produkt`
(Regeln an ganzrationalen Termen), `11-tangenten-normalen` (Tangentengleichungen als Thema)
und `11-kurvendiskussion-ganzrational` (vollstaendige Kurvendiskussion).

---

## 11-e-funktion

Audit: KEIN_AFB3 L5 **und** L6; KOLLAPS L5/L6; KURZ (Stufen 1–4); DUENNER_WEG (alle Stufen).
Neu geschrieben: Stufe 5 und 6 vollstaendig (#25–#36). In Stufe 1–4 wurden die zehn
Aufgaben mit zu duennem Weg (#5, #6, #11, #12, #17, #18, #19, #20, #22, #23) um einen
vollstaendigen Rechenweg und eine Kontrolle ergaenzt; die Aufgabentexte dieser Nummern
sind zugleich zu ganzen Fragesaetzen ausgebaut (Befund KURZ).

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
| 34 | 6 | Behauptung „\(e^{-x}\) wird negativ" begruendet widerlegen (MC), Wertebereich und Asymptote |
| 35 | 6 | Abi-Format Sachkontext: Zeitpunkt der Unterschreitung, Monotonie begruendet das „erstmals" |
| 36 | 6 | Fallunterscheidung nach \(c\) fuer die Loesbarkeit von \(e^x=c\) (MC), inkl. Fall \(0<c<1\) |

## 11-e-funktion-ableitung

Audit: der schwaechste Trainer der Welle — KEIN_AFB3 L5 **und** L6; KOLLAPS L1/L2, L4/L5
**und** L5/L6; KURZ (Stufen 1,2,3,4,6); DUENNER_WEG (alle Stufen).
Neu geschrieben: Stufe 4, 5 und 6 vollstaendig (#19–#36). Die alte Stufe 4/5 bestand aus
Extremstellen- und Wendestellen-Aufgaben und gehoerte damit inhaltlich in
`11-extrempunkte-wendepunkte`; sie wurde durch Ableitungs-, Tangenten- und
Aenderungsratenaufgaben ersetzt. Die beiden Integral-Aufgaben der alten Stufe 6
(#34, #35) sind entfallen — Integralrechnung ist TH-Stoff der Klasse 12.
In Stufe 2/3 wurden #10, #12 und #15 um einen vollstaendigen Weg ergaenzt.
Die Gate-Warnung zu #36 (MC-Laenge) ist mit der Neufassung erledigt.

| id | Level | Kriterium |
|---|---|---|
| 19 | 4 | Verfahren selbst waehlen: Produkt- und Kettenregel ineinander, \(f'(1)=5e^3\approx 100{,}43\) |
| 20 | 4 | Tangentensteigung als Ableitungswert, Vorzeichen der inneren Ableitung; \(-0{,}5e^{-1}\approx -0{,}184\) |
| 21 | 4 | Umkehraufgabe: Vorfaktor aus geforderter Steigung, \(a=2e^{-2}\approx 0{,}271\) |
| 22 | 4 | Produkt- und Kettenregel, Zusammenfassen durch Ausklammern (MC); \(4x\,e^{2x}\) |
| 23 | 4 | Modell aus Text: momentane Aenderungsrate \(N'(10)=48e^{0{,}6}\approx 87{,}5\); Bestand vs. Rate |
| 24 | 4 | Umkehraufgabe ueber die zweite Ableitung, \(a^2=9\) mit beiden Vorzeichen geprueft, \(a=3\) |
| 25 | 5 | Fehler in vorgelegter Rechnung: Produktregel als Produkt der Ableitungen; richtig \(5e^{5x}\) (MC) |
| 26 | 5 | Parameter aus zwei Bedingungen \(f(1)=0\), \(f'(1)=2e\); \(a=2\), Auswertung bewusst nicht bei \(x=0\) |
| 27 | 5 | drei Schritte: Produktregel, Tangentengleichung, Auswertung an der \(y\)-Achse; \(4e^{-2}\approx 0{,}541\) |
| 28 | 5 | Ausklammern und Argument „\(e\)-Potenz wird nie null"; \(x=\ln 2\approx 0{,}693\) |
| 29 | 5 | Behauptung ueber gleiche Steigung zweier Graphen widerlegen (MC); \(x=-\ln 2\) |
| 30 | 5 | Produktregel, Ausklammern, quadratischer Restfaktor; \(x=\sqrt2\approx 1{,}414\), negative Loesung ausgeschlossen |
| 31 | 6 | Abi-Format Sachkontext: Zu- oder Abnahme aus dem Vorzeichen von \(K'(3)\approx -0{,}56\) beurteilen (MC) |
| 32 | 6 | Abi-Format, zwei Bedingungen: \(k\) aus der Lage des groessten Wertes, \(a=3e\approx 8{,}15\); Vorzeichenwechsel geprueft |
| 33 | 6 | Tangente vom Ursprung an \(e^x\): Ansatz an unbekannter Beruehrstelle, \(x_0=1\) |
| 34 | 6 | Behauptung \(f'=k\cdot f\) fuer \(c\,e^{kx}\) allgemein begruenden (MC), Bezug zum Wachstumsmodell |
| 35 | 6 | Abi-Format Sachkontext Tank: Zuflussrate als Ableitung, \(t=\frac{\ln 2{,}5}{0{,}2}\approx 4{,}58\) |
| 36 | 6 | Fallunterscheidung nach \(k\) fuer die Existenz einer waagerechten Tangente (MC); nur \(k<0\) |

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
Die Gate-Warnungen zu #33 und #36 (MC-Laenge) sind mit den neuen Aufgaben erledigt; #36 ist
weiterhin die Frage nach \(f'(x_0)=f''(x_0)=0\), aber mit vier gleich langen, jeweils
begruendeten Optionen.
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
| 34 | 6 | Behauptung „Grad vier \(\Rightarrow\) Wendepunkt" mit Gegenbeispiel \(x^4\) widerlegen (MC) |
| 35 | 6 | Parameter aus zwei Bedingungen (Extremstelle und Funktionswert); \(a=2\), Art des Extremums nachgeprueft |
| 36 | 6 | notwendige gegen hinreichende Bedingung: \(f'=f''=0\) laesst Extremum und Sattelpunkt zu (MC), zwei Beispiele im Weg |

---

## Offen (bewusst nicht in dieser Welle)

- KOLLAPS L1/L2 und L2/L3 in `11-extrempunkte-wendepunkte` sowie L2/L3 in
  `11-monotonie-kruemmung`: Stufe 1–3 werden nach Plan nur nachgebessert, nicht neu geschrieben.
- In `11-e-funktion` sind Stufe 1–3 weiterhin ueberwiegend Ein-Schritt-Aufgaben zu den
  Potenzgesetzen; inhaltlich richtig, aber eng am Kollaps L2/L3.
- `11-e-funktion` L3 arbeitet mit \(\ln\); der eigene ln-Trainer entsteht erst im Block 11B
  (Ersatz `11-lk-newton`). Ueberschneidungen dort beim Schreiben pruefen.
