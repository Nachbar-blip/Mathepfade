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
| 10-stoch-mehrstufig | KEIN_AFB3 L5 (L5 war durchgehend Erwartungswert — nicht lehrplanfremd, aber Thema eines anderen Trainers, siehe Abgrenzung); KEIN_AFB3 L6; Rückverweis im Tipp #32 | L5/L6 komplett neu (12 Aufgaben): Anzahl leerer Batterien aus der Pfadgleichung, Fehler „mit Zurücklegen gerechnet, obwohl die Lose behalten werden", „höchstens ein Ausfall" als zwei Fälle, Vergleich mit/ohne Zurücklegen, Mindestanzahl Drehungen für 90 %, genau zwei Treffer bei drei verschiedenen Wahrscheinlichkeiten; „zweiter Zug ungünstiger?" (bedingt gegen unbedingt), Wartezeit „mehr als zwei Züge", zweistufiger Versuch mit veränderter Urne, „erreicht die 1?", Doppelzählung bei „oder" korrigieren, Raten mit mindestens zwei von drei Treffern. Tipps von #19/#22/#24 (L4) von der fertigen Bernoulli-Gleichung auf den Weg umgestellt |

### 10-stoch-bedingte-wsk

| id | Level | Kriterium |
|---|---|---|
| 12 | 2 | Angaben vollständig im Text (Rückverweis „in obigem Beispiel" entfernt) |
| 16 | 3 | Angaben vollständig im Text (Rückverweis „(Gleiche Situation:)" entfernt) |
| 17 | 3 | Angaben vollständig im Text (Rückverweis „(Gleiche Situation:)" entfernt) |
| 19 | 4 | L4: Bedingung in der ungewohnten Richtung — die Grundmenge (Orchester) steht nicht im Text und muss erst gebildet werden (0,577); ersetzt die reine Formelabfrage zum Satz von Bayes |
| 25 | 5 | L5: zwei Schritte — Tafel füllen, dann „genau eines von beidem" (0,70) |
| 26 | 5 | L5: Fehler finden — Bedingung steht im Nenner, nicht das bedingte Ereignis (MC) |
| 27 | 5 | L5: Parameter aus zwei Randbedingungen — Eckzelle für Unabhängigkeit (100) |
| 28 | 5 | L5: zwei Verfahren — Schnitt aus dem Additionssatz, dann bedingen (0,667) |
| 29 | 5 | L5: Parameter aus zwei Bedingungen — Additionssatz plus Unabhängigkeit (0,4); Tipp nennt nur, dass eine Zusatzinformation im Wort „unabhängig" steckt |
| 30 | 5 | L5: Tafel mit fehlendem Randwert — bedingte Angabe in eine Zelle umrechnen, zwei Randsummen ergänzen, in der anderen Gruppe bedingen (0,30) |
| 31 | 6 | L6: Behauptung prüfen — unvereinbar ist nicht unabhängig, sogar stets abhängig (MC) |
| 32 | 6 | L6: Grenzfallbetrachtung — kleinstmögliches \(P(A \cup B)\) bei \(B \subseteq A\) (0,6) |
| 33 | 6 | L6: Rückwärtsaufgabe über die volle Tafel mit Unabhängigkeit (120) |
| 34 | 6 | L6: Behauptung prüfen — beide Ungleichungen gleichwertig zum Produktkriterium (MC) |
| 35 | 6 | L6: drei bedingte Angaben in die Tafel umrechnen, Bedingung wechseln (0,455) |
| 36 | 6 | L6: Behauptung prüfen — Unabhängigkeit überträgt sich auf das Gegenereignis (MC) |

### 10-stoch-mehrstufig

| id | Level | Kriterium |
|---|---|---|
| 25 | 5 | L5: Umkehraufgabe — Anzahl aus der Pfadgleichung, \(k(k-1) = 6\), negative Lösung verwerfen (3) |
| 26 | 5 | L5: Fehler finden — mit Zurücklegen gerechnet, obwohl die Lose behalten werden (MC) |
| 27 | 5 | L5: „höchstens einer" als zwei Fälle, Pfadanzahl beachten (0,9928) |
| 28 | 5 | L5: zwei Verfahren vergleichen — mit gegen ohne Zurücklegen, Differenz (0,027) |
| 29 | 5 | L5: Umkehraufgabe — Mindestanzahl aus Ungleichung mit Gegenereignis (11) |
| 30 | 5 | L5: dreistufiger Baum mit ungleichen Wahrscheinlichkeiten, Pfade addieren (0,38) |
| 31 | 6 | L6: Behauptung prüfen — bedingt gegen unbedingt im zweiten Zug (MC) |
| 32 | 6 | L6: Ereignis umformulieren — „mehr als zwei Züge" ist ein einziger Pfad (0,30) |
| 33 | 6 | L6: zweistufiger Versuch mit veränderter Urne — die zweite Stufe hängt vom Ausgang der ersten ab (0,35) |
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

## Offene Punkte

- **Erwartungswert und Wahrscheinlichkeitsverteilung sind in Kl. 10 jetzt nicht mehr abgedeckt.**
  Die alte Stufe 5 von `10-stoch-mehrstufig` bestand ausschließlich aus Erwartungswert-Aufgaben;
  entfernt wurde sie wegen der **Trainer-Abgrenzung** (dieser Trainer ist Baumdiagramm und
  Pfadregeln), nicht wegen des Lehrplans. TH 2.3.4 nennt für Klassenstufe 10 ausdrücklich
  „Wahrscheinlichkeitsverteilungen diskreter Zufallsgrößen bestimmen" sowie „Erwartungswert und
  Standardabweichung diskreter Zufallsgrößen berechnen und interpretieren"; erst die
  Binomialverteilung mit 2σ-Regel gehört in die Qualifikationsphase. Ein eigener Kl.-10-Trainer
  dafür wäre die saubere Lösung — Entscheidung des Autors, hier bewusst **nicht** angelegt.
- Bernoulli-Ketten auf Stufe 4 (#19/#22/#24 in `10-stoch-mehrstufig`) bleiben: TH 2.3.4 nennt für
  Kl. 10 wörtlich „Bernoulli-Ketten … die Bernoulli-Formel anwenden, dabei Binomialkoeffizienten
  bestimmen und inhaltlich deuten". Ihre Tipps wurden von der fertigen Gleichung auf den Weg
  umgestellt, damit die Deutung und nicht das Eintippen die Leistung ist.
- Nicht behoben, nur notiert: `10-stoch-bedingte-wsk` #12 hat bei einer Ja/Nein-Frage auf L2 vier
  MC-Optionen; `10-stoch-mehrstufig` #27 und #36 nutzen bei verschiedenem Text dasselbe
  Bernoulli-Rechenmuster.

## Beim Einsetzen aufgefallen

`10-stoch-mehrstufig` #23/#24 (Bestand, Stufe 4): Das Dezimalkomma-Markup `0{,}3` stand im
Aufgabentext **ausserhalb** von `\(…\)` und wurde deshalb woertlich als „0{,}3" angezeigt.
Kein Gate sieht das — weder `level_check` (kein KaTeX-Befehlswort) noch `katex_check` (was
nicht in einer Mathe-Umgebung steht, wird gar nicht erst gerendert). Gefunden allein in der
Sichtpruefung am PNG, behoben durch `\\(0{,}3\\)`. Kandidat fuer eine neue Gate-Regel:
`{,}` im Klartext ausserhalb von `\(…\)` und `$$…$$`.

Der erste Reparaturversuch lief ueber ein Bash-Heredoc und verlor je einen Backslash
(`\\(` wurde zu `\(`, vom JS-String verschluckt) — die Regel „nie Bash-Heredoc fuer
Aufgabentexte" aus `CLAUDE.md` gilt auch fuer kleine Korrekturen. Zweiter Versuch per
Scratchpad-Skript war richtig.


Die Zeile der Aufgabe #36 trägt in beiden Dateien den Array-Abschluss `];` am Zeilenende.
Ein zeilenweises Ersetzen nach `id`-Nummer entfernt ihn und macht die Datei unparsbar
(`level_check` meldet „AUFGABEN nicht auswertbar"). Beim Ersetzen der letzten Aufgabe ist
der Abschluss also mitzuschreiben.
