# Klasse 11, Block A3 — Kriterien je Trainer (Welle Task 8, Stand 2026-09-30)

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

## Abgrenzung der drei Trainer (gegen sinngleiche Aufgaben)

| Trainer | Gegenstand |
|---|---|
| 11-extremwertaufgaben | Optimierung mit Nebenbedingung aus Sachkontext — die Leistung ist das **Aufstellen der Zielfunktion** |
| 11-kurvendiskussion-ganzrational | vollstaendige Untersuchung einer **gegebenen** Funktion (Nullstellen, Symmetrie, Extrema, Wendepunkte, Randverhalten) |
| 11-steckbriefaufgaben | Funktion aus Eigenschaften **rekonstruieren** (Gleichungssystem aus Bedingungen, Probe) |

Abstand gehalten zu `11-extrempunkte-wendepunkte` und `11-monotonie-kruemmung` (dort gehoert das
reine Bestimmen von Extrem- und Wendestellen hin; hier steckt es jeweils im groesseren Zusammenhang)
sowie zu `11-tangenten-normalen`.

---

## 11-extremwertaufgaben

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
| 31 | 6 | Abi-Format Sachkontext: Gewinn auf abgeschlossenem Intervall, Randwerte mitvergleichen (\(x=3\)) |
| 32 | 6 | „Zeigen Sie" als MC: offener Zylinder minimaler Oberflaeche erfuellt \(h=r\) **fuer jedes** \(V\) |
| 33 | 6 | Abi-Format mehrschrittig: Tunnelquerschnitt Rechteck + Halbkreis, Umfang \(10\,\text{m}\), \(b=\frac{20}{4+\pi}\approx 2{,}80\) |
| 34 | 6 | **Randfall** mit Nebenbedingung: Tank \(4000\,\text{cm}^3\), Grundkante hoechstens \(10\,\text{cm}\) (\(O=1700\)) |
| 35 | 6 | Behauptung beurteilen (MC): \(A_{\max}=\frac{U^2}{16}\) — doppelter Umfang vervierfacht die Flaeche |
| 36 | 6 | Abi-Format mit gewichteten Kosten: Deckel/Boden doppelt so teuer, \(r=\frac{5}{\sqrt[3]{\pi}}\approx 3{,}41\), Deutung \(h\approx 4r\) |

DUENNER_WEG behoben in #5, #6, #7, #9, #10, #11, #12, #13, #14, #15, #16, #17, #19, #20, #24:
Loesungswege zeigen jetzt Nebenbedingung → Zielfunktion → Ableitung → Art des Extremums.
#30 (alte Begriffsabfrage zur Randwertbetrachtung, zugleich MC-Laengen-Warnung) ist durch eine
echte Randfall-Rechnung ersetzt; die Randbetrachtung wird jetzt **gerechnet** statt abgefragt.

## 11-kurvendiskussion-ganzrational

Audit: KEIN_AFB3 L6; DUENNER_WEG (Stufen 1–5). Lehrplan-Gate: #11 nannte „Polynomdivision".
Gate-Warnung: #34 (Tipp enthielt den Loesungswert 16).

| id | Level | Kriterium |
|---|---|---|
| 11 | 2 | **Pflicht-Fix**: Nullstellen von \(x^3+2x^2-8x\) ueber Ausklammern, Vieta und Satz vom Nullprodukt statt Polynomdivision |
| 25 | 5 | Fehler in vorgelegter Argumentation: „hoechster Exponent gerade ⇒ achsensymmetrisch" — Probe mit \(f(-x)\) |
| 26 | 5 | Parameter aus zwei Bedingungen: Wendepunkt bei \(2\) und waagerechte Tangente bei \(1\) (\(b=9\)) |
| 27 | 5 | Zwei Verfahren: Wendestelle bestimmen, dort \(f'\) auswerten (Wendetangente, \(-12\)) |
| 28 | 5 | Sachkontext mit **Randbetrachtung**: Wasserstand auf \([0;7]\), Vergleich der Randwerte |
| 29 | 5 | Faktorisieren als Schluessel: \(f'=4(x-1)^3\), \(f''(1)=0\) — Vorzeichenwechsel entscheidet |
| 30 | 5 | Aus dem Graphen von \(f'\) auf \(f\) schliessen (MC, Ebenenwechsel Ableitung → Funktion) |
| 31 | 6 | **Fallunterscheidung/Grenzfall**: \(x^3-3x+c\) mit drei Nullstellen nur fuer \(-2<c<2\), groesste ganze Zahl \(1\) |
| 32 | 6 | Allgemeine Aussage ueber **jede** Funktion dritten Grades (genau ein Wendepunkt) mit Gegenbeispielen |
| 33 | 6 | Abi-Format Sachkontext: Talquerschnitt, tiefster Punkt gegen hoechsten **Randpunkt** (\(6{,}25\)) |
| 34 | 6 | Behauptung pruefen (MC): \(f''(x_0)=0\) ist nur notwendig, Gegenbeispiel \((x-1)^4\) — ersetzt die Aufgabe mit Tipp-Lösungswert |
| 35 | 6 | Fallunterscheidung ueber die Diskriminante: genau eine waagerechte Tangente fuer \(a=3\), dort Sattelpunkt |
| 36 | 6 | Mehrschrittig: beide Extremstellen, Art klaeren, Differenz der \(y\)-Werte (\(32\)) mit Deutung fuer die Nullstellenzahl |

DUENNER_WEG behoben in #1, #6, #10, #12, #13, #14, #16, #17, #21, #22.

## 11-steckbriefaufgaben

Audit: KEIN_AFB3 L5 **und** L6; DUENNER_WEG (Stufen 1, 2, 4, 5, 6). Der in Audit-Zeile 66 genannte
Ein-Zeilen-Weg von #2 (`\(f(2)=5\).`) war bereits ausgebaut (nachgeprueft).

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | Vier Bedingungen, vier Unbekannte: Wendepunkt \((1\mid2)\), Steigung \(-3\), \(f(0)=6\) (\(a=-1\)), Probe gegen alle vier |
| 26 | 5 | „Beruehrt die \(x\)-Achse" in doppelte Nullstelle uebersetzen, Produktansatz \(a(x-3)^2\) (\(a=2\)) |
| 27 | 5 | Fehler in vorgelegtem Ansatz: Hochpunkt verlangt \(f'=0\), nicht \(f''=0\) |
| 28 | 5 | Vielfachheiten in Produktdarstellung uebersetzen, ausmultiplizieren, Koeffizientenvergleich (\(b=-3\)) |
| 29 | 5 | Sachkontext (Strassenfuehrung): knickfreier Anschluss und „wieder waagerecht" (\(a=-0{,}25\)) |
| 30 | 5 | Scheitelform aus zwei Angaben, dann Umschreiben in die allgemeine Form (\(b=-4\)) |
| 31 | 6 | Abi-Format: Wendepunkt, Wendetangentensteigung und \(f(0)=0\) — vier Gleichungen (\(a=4\)), Probe |
| 32 | 6 | Symmetrieansatz erkennen (nur gerade Exponenten), drei Angaben genuegen (\(a=1\)) |
| 33 | 6 | Beurteilen (MC): Bedingungen zaehlen — fuenf Gleichungen fuer vier Unbekannte, **ueberbestimmt** |
| 34 | 6 | Abi-Format Sachkontext: Rutsche mit vier Bedingungen, danach \(f'(3)=-1{,}5\) auswerten |
| 35 | 6 | Parameter fuer Wendepunkt an vorgegebener Stelle, **Vorzeichenwechsel** und Fall \(a\le 0\) mitgeprueft |
| 36 | 6 | Behauptung pruefen (MC): Sattelpunkt mit Koordinaten liefert drei, eine Sattel**stelle** nur zwei Bedingungen |

DUENNER_WEG behoben in #11, #15, #17, #19 (die uebrigen Stufen 1–4 waren bereits ausgebaut).
MC-Laengen in #33 und #36 angeglichen, damit die richtige Option nicht die laengste ist.

---

## Offen (bewusst nicht in dieser Welle)

- `11-extremwertaufgaben`: Stufe 1–3 enthaelt weiterhin Paare aus Stelle und Wert derselben Aufgabe
  (#7/#8, #10/#11, #16/#17). Das ist didaktisch gewollt, erzeugt aber wenig Formatvielfalt.
- `11-kurvendiskussion-ganzrational`: Stufe 3 und 4 fragen fast durchgaengig nach \(x\)- oder
  \(y\)-Koordinaten von Extrem- und Wendepunkten; eine Umkehraufgabe auf Stufe 4 waere ein Gewinn.
- `11-steckbriefaufgaben`: Auf Stufe 6 sind vier von sechs Aufgaben numerische Parameterbestimmungen
  — mehr Begruendungsformate waeren moeglich.
- Die Abgrenzung gegen `11-extrempunkte-wendepunkte` wurde nur einseitig geprueft (aus diesen drei
  Trainern heraus); der dortige Implementierer sollte die Gegenrichtung pruefen.
