# Klasse 10, Block C (Stochastik) — Überarbeitung je Trainer (Stand 2026-09-30)

Lokale Nachvollziehbarkeit; im Public-HTML stehen die Kriterien bewusst nicht.
Grundlage: Rubrik aus `docs/plans/2026-09-26-lehrplan-th-und-level-progression-plan.md`
(Lesart Kl. 10 Stochastik: L4 = Verfahren selbst wählen, Modell aus Text, Bedingung
richtig herum ansetzen; L5 = zwei Verfahren kombinieren (Tafel vervollständigen und dann
bedingen, mit und ohne Zurücklegen vergleichen), Parameter aus zwei Bedingungen,
Fehler in vorgelegter Rechnung; L6 = Behauptung begründet prüfen, Fallunterscheidung
bzw. Grenzfallbetrachtung, Rückwärtsaufgabe über die volle Vierfeldertafel),
Befunde aus `docs/audit/audit-2026-09-19-mathepfade.md` (beide Trainer: KEIN_AFB3 L5 **und** L6).
Niveau: TH-Lehrplan 2.3.4 (Vierfeldertafel, stochastische Unabhängigkeit, mehrstufige
Zufallsversuche, Pfadregeln, Ziehen mit und ohne Zurücklegen, Gegenereignis).
Jede Lösung mit Wolfram nachgerechnet; Bilder L5/L6 per `tests/bild.py` angesehen.

## Abgrenzung der beiden Trainer (gegen Dubletten im Pool)

`10-stoch-bedingte-wsk` = **Vierfeldertafel und stochastische Unabhängigkeit**: Tafel aus
absoluten Zahlen oder Anteilen füllen, bedingte Wahrscheinlichkeit als Einschränkung der
Grundmenge, Produktkriterium \(P(A \cap B) = P(A) \cdot P(B)\), Additionssatz, Gegenereignis
als Merkmalsausprägung. Keine Urnenziehungen ab Stufe 4.

`10-stoch-mehrstufig` = **Baumdiagramm und Pfadregeln**: mehrstufige Versuche, Ziehen mit
und ohne Zurücklegen, Gegenereignis bei „mindestens eins", Pfade zählen und addieren,
Umkehraufgaben nach der Urnenzusammensetzung. Keine Vierfeldertafel, kein Unabhängigkeits-
kriterium als Rechenziel.

| Trainer | Audit-Befund | Geändert |
|---|---|---|
| 10-stoch-bedingte-wsk | KEIN_AFB3 L5; KEIN_AFB3 L6; MC-Längen-Warnung #19/#34; Rückverweise #12/#16/#17 | L5/L6 komplett neu (12 Aufgaben): Tafel vervollständigen und „genau eines" bestimmen, Fehler „Bedingung im Nenner vertauscht", Eckzelle für Unabhängigkeit, Schnitt aus Vereinigung und dann bedingen, \(P(B)\) aus Additionssatz plus Unabhängigkeit, Abweichung von der Unabhängigkeits-Eckzelle; „ausschließend = unabhängig?", kleinstmögliches \(P(A \cup B)\) (Grenzfall \(B \subseteq A\)), Rückwärtsaufgabe über die volle Tafel, „\(P(A\mid B) > P(A) \Rightarrow P(B\mid A) > P(B)\)?", \(P(A\mid \overline B)\) aus drei bedingten Angaben, Unabhängigkeit überträgt sich auf das Gegenereignis. L4 #19 (reine Bayes-Formel-Abfrage, MC-Längen-Warnung) durch eine Modellaufgabe ersetzt. Rückverweise „in obigem Beispiel"/„(Gleiche Situation:)" in #12/#16/#17 durch vollständige Angaben ersetzt |
| 10-stoch-mehrstufig | KEIN_AFB3 L5 (L5 war durchgehend Erwartungswert, Thema der Kl. 12); KEIN_AFB3 L6; Rückverweis im Tipp #32 | L5/L6 komplett neu (12 Aufgaben): Urnenzusammensetzung aus gegebener Pfadwahrscheinlichkeit, Fehler „3 · 1/6 statt Gegenereignis", „höchstens ein Ausfall" als zwei Fälle, Vergleich mit/ohne Zurücklegen, Mindestanzahl Drehungen für 90 %, genau zwei Treffer bei drei verschiedenen Wahrscheinlichkeiten; „zweiter Zug ungünstiger?" (bedingt gegen unbedingt), Wartezeit „mehr als zwei Züge", Anzahl leerer Batterien aus der Pfadgleichung, „erreicht die 1?", Doppelzählung bei „oder" korrigieren, Raten mit mindestens zwei von drei Treffern |

### 10-stoch-bedingte-wsk

| id | Level | Kriterium |
|---|---|---|
| 12 | 2 | Angaben vollständig im Text (Rückverweis „in obigem Beispiel" entfernt) |
| 16 | 3 | Angaben vollständig im Text (Rückverweis „(Gleiche Situation:)" entfernt) |
| 17 | 3 | Angaben vollständig im Text (Rückverweis „(Gleiche Situation:)" entfernt) |
| 19 | 4 | L4: Modell aus Text — Bedingung erkennen, Grundmenge einschränken (\(6/10\)); ersetzt die reine Formelabfrage zum Satz von Bayes |
| 25 | 5 | L5: zwei Schritte — Tafel füllen, dann „genau eines von beidem" (0,70) |
| 26 | 5 | L5: Fehler finden — Bedingung steht im Nenner, nicht das bedingte Ereignis (MC) |
| 27 | 5 | L5: Parameter aus zwei Randbedingungen — Eckzelle für Unabhängigkeit (100) |
| 28 | 5 | L5: zwei Verfahren — Schnitt aus dem Additionssatz, dann bedingen (0,667) |
| 29 | 5 | L5: Parameter aus zwei Bedingungen — Additionssatz plus Unabhängigkeit (0,4) |
| 30 | 5 | L5: Vergleich beobachtete Zelle gegen Unabhängigkeitswert (20) |
| 31 | 6 | L6: Behauptung prüfen — unvereinbar ist nicht unabhängig, sogar stets abhängig (MC) |
| 32 | 6 | L6: Grenzfallbetrachtung — kleinstmögliches \(P(A \cup B)\) bei \(B \subseteq A\) (0,6) |
| 33 | 6 | L6: Rückwärtsaufgabe über die volle Tafel mit Unabhängigkeit (120) |
| 34 | 6 | L6: Behauptung prüfen — beide Ungleichungen gleichwertig zum Produktkriterium (MC) |
| 35 | 6 | L6: drei bedingte Angaben in die Tafel umrechnen, Bedingung wechseln (0,455) |
| 36 | 6 | L6: Behauptung prüfen — Unabhängigkeit überträgt sich auf das Gegenereignis (MC) |

### 10-stoch-mehrstufig

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | L5: Umkehraufgabe — Urnenzusammensetzung aus gegebener Pfadwahrscheinlichkeit (5) |
| 26 | 5 | L5: Fehler finden — überlappende Pfade addiert statt Gegenereignis (MC) |
| 27 | 5 | L5: „höchstens einer" als zwei Fälle, Pfadanzahl beachten (0,9928) |
| 28 | 5 | L5: zwei Verfahren vergleichen — mit gegen ohne Zurücklegen, Differenz (0,027) |
| 29 | 5 | L5: Umkehraufgabe — Mindestanzahl aus Ungleichung mit Gegenereignis (11) |
| 30 | 5 | L5: dreistufiger Baum mit ungleichen Wahrscheinlichkeiten, Pfade addieren (0,38) |
| 31 | 6 | L6: Behauptung prüfen — bedingt gegen unbedingt im zweiten Zug (MC) |
| 32 | 6 | L6: Ereignis umformulieren — „mehr als zwei Züge" ist ein einziger Pfad (0,30) |
| 33 | 6 | L6: Parameter aus der Pfadgleichung, \(k(k-1) = 6\), negative Lösung verwerfen (3) |
| 34 | 6 | L6: Behauptung prüfen — Grenzwert 1 wird nie erreicht (MC) |
| 35 | 6 | L6: vorgelegte Doppelzählung korrigieren, Differenz erklären (0,643) |
| 36 | 6 | L6: „mindestens zwei von drei" als Fallunterscheidung, Pfade zählen (0,1563) |

## Gates nach der Arbeit

```
python tests/level_check.py --strict trainer/10-stoch-bedingte-wsk.html trainer/10-stoch-mehrstufig.html   # Exit 0, 0 Warnungen
python tests/lehrplan_check.py --strict trainer/10-stoch-bedingte-wsk.html trainer/10-stoch-mehrstufig.html # Exit 0, 0 Befunde
python tests/katex_check.py trainer/10-stoch-bedingte-wsk.html trainer/10-stoch-mehrstufig.html             # ok
python -m pytest tests/test_trainer.py -k "bedingte or mehrstufig" -q                                        # 14 passed
python tests/bild.py trainer/<datei>.html --level 5 / --level 6                                              # vier PNG angesehen
```

## Beim Einsetzen aufgefallen

Die Zeile der Aufgabe #36 trägt in beiden Dateien den Array-Abschluss `];` am Zeilenende.
Ein zeilenweises Ersetzen nach `id`-Nummer entfernt ihn und macht die Datei unparsbar
(`level_check` meldet „AUFGABEN nicht auswertbar"). Beim Ersetzen der letzten Aufgabe ist
der Abschluss also mitzuschreiben.
