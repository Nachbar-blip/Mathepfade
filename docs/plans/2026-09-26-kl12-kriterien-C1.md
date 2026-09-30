# Klasse 12, Block C1 — Stochastik gA: Kriterien je Trainer

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

## Abgrenzung der vier Trainer gegeneinander

| Trainer | Inhalt |
|---|---|
| 12-stoch-zufallsgroessen | Zufallsgröße, Wahrscheinlichkeitsverteilung, Erwartungswert, Varianz und Standardabweichung, lineare Transformation, faires Spiel. **Keine** σ-Umgebungen, keine kumulierten Binomialwerte |
| 12-stoch-binomialverteilung | Bernoulli-Kette und ihre Voraussetzungen, Binomialkoeffizient, kumulierte Wahrscheinlichkeiten, „mindestens/höchstens“, Mindestanzahl-Aufgaben. **Keine** σ-Umgebungen |
| 12-stoch-sigma-regeln | σ-Umgebungen, 68,3 / 95,4 / 99,7 %, Laplace-Bedingung σ > 3, ganzzahlige Grenzen, Abweichung in Einheiten von σ. **Kein** Schluss auf ein unbekanntes p aus einer Beobachtung |
| 12-stoch-hypothesentests → **Prognoseintervalle** | Prognoseintervall für **absolute und relative** Häufigkeit, Beurteilung einer Beobachtung, n aus geforderter Genauigkeit |

Abstand nach außen: zu `10-stoch-mehrstufig` und `10-stoch-bedingte-wsk` (Pfadregeln,
Vierfeldertafel — hier nur einmal als Hilfsmittel in #27 der Binomialverteilung) und zum
eA-Trainer `12-lk-stoch-normalverteilung` des Parallelblocks.

## Prognoseintervall gegen Konfidenzintervall (Beschluss 2026-09-30)

Der Ersatz-Trainer schließt ausschließlich **von bekanntem \(p\) auf die Häufigkeit**. Der
umgekehrte Schluss — von einer Beobachtung auf das unbekannte \(p\) — entsteht parallel im
eA-Trainer `12-lk-stoch-prozesse` („Konfidenzintervalle“) und kommt hier nirgends als
Rechenziel vor. Die Abgrenzung wird in #3 und #24 ausdrücklich zum Aufgabeninhalt gemacht
(beide MC, „Was leistet ein Prognoseintervall?“), damit die Verwechslung benannt ist, bevor
sie im eA-Trainer als Fehlersuchaufgabe auftaucht. Aufgabe #21 beurteilt zwar mehrere
Kandidaten für \(p\), tut dies aber über deren **eigene Prognoseintervalle** — nicht über
ein aus der Beobachtung gebildetes Intervall.

---

## Ersatz-Trainer: 12-stoch-hypothesentests → Prognoseintervalle (TH 4.3 gA)

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

## 12-stoch-binomialverteilung

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

## 12-stoch-sigma-regeln

Audit-Befund: KEIN_AFB3 L5 **und** L6; **KOLLAPS L2/L3 und L3/L4**; DUENNER_WEG (Stufen 2, 6).
Geändert: Stufe 3, 4, 5 und 6 komplett neu (24 Aufgaben), dazu der dünne Lösungsweg von
#9 (Stufe 2) ausgeführt.

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

## 12-stoch-zufallsgroessen

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

## Review-Nachtrag (Prüf-Agent, 2026-09-30)

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

## Gates am Ende des Blocks

```
python tests/level_check.py --strict trainer/12-stoch-*.html      -> Exit 0, 0 Warnungen
python tests/lehrplan_check.py --strict trainer/12-stoch-*.html   -> 0 Befunde (vorher 4)
python tests/katex_check.py trainer/12-stoch-*.html               -> 4x ok
python -m pytest tests/test_trainer.py -k "…" -q                  -> 28 passed
```

Behobene Gate-Warnungen aus dem Bestand: Tipp mit Lösungswert (#26 alt, sigma-regeln),
zu lange richtige MC-Option in `12-stoch-sigma-regeln` #35 alt, `12-stoch-zufallsgroessen`
#23/#33/#36 alt und `12-stoch-hypothesentests` #32/#35 alt, Tipp mit Lösungswert
(#13 alt, hypothesentests). Ein Lösungsweg sprach eine MC-Option über ihren Buchstaben
bzw. ihre Position an („die dritte Antwort“) — in `12-stoch-sigma-regeln` #35 und
im Ersatz-Trainer #31 durch den Wortlaut der Option ersetzt, weil die Engine mischt.

## Offen

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
