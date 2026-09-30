# Klasse 12, Block B1 (Analytische Geometrie, gA) — Kriterien je Trainer

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

## Abgrenzung der vier Trainer gegeneinander und gegen den eA-Block

| Trainer | Inhalt |
|---|---|
| 12-vektoren-grundlagen | Vektorbegriff, Rechnen mit Vektoren, Betrag, Linearkombination, Kollinearität, Mittel- und Teilpunkte, Schwerpunkt |
| 12-geraden-raum | Geradengleichung aufstellen, Punktprobe, Lagebeziehung zweier Geraden (parallel / identisch / schneidend / windschief), Spurpunkte |
| 12-ebenen | Parameter-, Normalen- und Koordinatenform, Umwandlung zwischen ihnen, Lage Gerade/Ebene, Lage zweier Ebenen |
| 12-skalarprodukt | Skalarprodukt, Orthogonalität, Winkel zwischen Vektoren, Projektionslänge |

Abstände (Punkt–Ebene, Punkt–Gerade, windschiefe Geraden), Schnittwinkel von Gerade und Ebene und
die vollständige Lagediskussion mit Parameterscharen gehören in die eA-Trainer
`12-lk-geom-abstaende`, `12-lk-geom-lagebeziehungen`, `12-lk-geom-schnittwinkel` und bleiben hier
außen vor. Deshalb sind in `12-ebenen` die alten Abstandsaufgaben der Stufen 5 und 6 (Hesse-Form,
Abstand paralleler Ebenen) mit dem neuen Block entfallen; die Hesse-Normalenform bleibt nur auf
Stufe 4 als Begriff stehen.

---

## 12-vektoren-grundlagen

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

## 12-geraden-raum

Audit: KEIN_AFB3 L5 **und** L6; KOLLAPS L5/L6. Stufe 5 und 6 vollständig neu (id 25–36).
Gate-Warnungen #29 und #32 sind mit dem neuen Block entfallen.

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | Schnittpunkt: zwei Zeilen bestimmen die Parameter, die dritte ist die Probe (ohne sie keine Aussage) |
| 26 | 5 | Fehlersuche: unvollständige Punktprobe (nur zwei Zeilen geprüft). Der falsche Schluss ist nachweislich falsch, \(P\) liegt nicht auf \(g\) |
| 27 | 5 | Parameter, für den aus windschief schneidend wird; im Lösungsweg begründet, warum parallel ausscheidet |
| 28 | 5 | Identität nachweisen: kollineare Richtungen **und** Punktprobe — zwei Bedingungen |
| 29 | 5 | Gerade aus zwei Punkten aufstellen und fehlende Koordinate eines Geradenpunkts bestimmen |
| 30 | 5 | Punkt in vorgegebenem Abstand vom Aufpunkt: Betrag des Richtungsvektors als Maßstab des Parameters |
| 31 | 6 | Abi-Format, Flugbahnen: Kreuzungspunkt **und** Zeitvergleich \(t = s\) als Begründung der Kollisionsgefahr |
| 32 | 6 | Lagebeziehung vollständig entscheiden (Richtungen, dann System): windschief. MC, weil die Einordnung selbst die Leistung ist |
| 33 | 6 | Abi-Format, Sichtlinie und Traverse: Schnitt **plus** Randbedingung \(0 \le u \le 1\) — ohne sie kein gesicherter Treffer |
| 34 | 6 | Fallunterscheidung parallel/identisch: \(a = \pm 1\), Punktprobe entscheidet je Fall |
| 35 | 6 | Abi-Format, Straßenkreuzung: beide Geraden selbst aufstellen, dann Schnittpunkt |
| 36 | 6 | Behauptung prüfen: kollineare Richtungen schließen gemeinsame Punkte nicht aus (identisch) |

## 12-ebenen

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
| 34 | 6 | Fallunterscheidung: Richtung immer parallel, der Aufpunkt entscheidet zwischen „in \(E\)“ und „echt parallel“ |
| 35 | 6 | Abi-Format, Schattenwurf: Strahl als Gerade modellieren, Schnitt mit der Panelebene |
| 36 | 6 | Abi-Format, Satteldach: Schnittgerade zweier Ebenen durch Addition/Subtraktion, freie \(x\)-Koordinate gedeutet |

## 12-skalarprodukt

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

## Gate-Ergebnisse

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

## Offen

- Stufe 1–3 wurde planmäßig nicht neu geschrieben. `12-vektoren-grundlagen` behält den
  DUENNER_WEG-Befund auf Stufe 3, `12-ebenen` auf den Stufen 2 und 3 (kurze Lösungswege im Bestand).
- `12-ebenen` nutzt auf Stufe 4 (#26) weiterhin das Kreuzprodukt zur Normalenbestimmung. In den neuen
  Aufgaben wird der Normalenvektor stattdessen über Orthogonalitätsbedingungen gewonnen, was zur
  gA-Tiefe besser passt; die Altaufgabe blieb unangetastet.
- Die Hesse-Normalenform steht in `12-ebenen` noch als Begriff auf Stufe 4 (#29 alt). Sie wird in den
  neuen Stufen nicht mehr gebraucht; ob sie in den gA-Trainer gehört, wäre beim Abschluss zu klären.
