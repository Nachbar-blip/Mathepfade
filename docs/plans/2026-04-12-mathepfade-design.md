# Mathepfade — Adaptives Mathe-Training Thüringen G8

## Zusammenfassung

Mathepfade ist die Thüringen-Variante der adaptiven Mathe-Trainer-Reihe (nach DifferenzierungsEngine/Sachsen-Anhalt und Ref4OHG/Niedersachsen). 90 Trainer decken den Thüringer Gymnasiallehrplan Klasse 7–12 (G8) vollständig ab — inkl. 12 LK-Vertiefungen.

## Architektur

Identisch zu DiffEngine und Ref4OHG:

```
Mathepfade/
  index.html              — Dashboard (Klasse 7–12 Filter + GK/LK-Filter)
  spirale-engine.js       — Adaptive Spiral-Engine (1:1 von Ref4OHG inkl. Bugfixes)
  spirale.css             — Shared Styles (1:1 von Ref4OHG inkl. Bugfixes)
  trainer/                — 90 HTML-Trainer (je 36 Aufgaben, 6 Level a 6)
  tests/                  — Playwright-Testsuite
    conftest.py
    helpers.py
    test_trainer.py
    pytest.ini
    requirements.txt
  docs/plans/             — Dieses Dokument
  .gitignore
```

## Unterschiede zu Ref4OHG (Niedersachsen)

| Aspekt | Ref4OHG | Mathepfade |
|--------|---------|------------|
| Bundesland | Niedersachsen | Thueringen |
| Schulform | G9 (Kl. 7–13) | G8 (Kl. 7–12) |
| Trainer-Anzahl | 76 | 90 |
| Oberstufen-Split | gA/eA (Klasse 13) | GK/LK (Klasse 11–12) |
| Filter-Labels | "Nur gA" / "Nur eA" | "Nur GK" / "Nur LK" |
| Neue Themen | — | Stoch. Prozesse, gebr.-rat. Fkt., Rotationskoerper, DGL, Newton, uneigentl. Integrale |

## Farbschema & Branding

- Projektname: **Mathepfade**
- CSS-Gradient: neues Farbschema (nicht identisch mit Ref4OHG/DiffEngine)
- Bereiche: Analysis (blau/lila), Geometrie (gruen), Stochastik (orange) — wie gehabt

## Trainer-Themenliste (90 Trainer)

### Klasse 7 — 12 Trainer

| Nr | Dateiname | Thema | Bereich |
|----|-----------|-------|---------|
| 1 | 7-terme-aufstellen | Terme aufstellen & interpretieren | Analysis |
| 2 | 7-terme-umformungen | Termumformungen (Klammern, Produkte) | Analysis |
| 3 | 7-binomische-formeln | Binomische Formeln | Analysis |
| 4 | 7-gleichungen-linear | Lineare Gleichungen | Analysis |
| 5 | 7-ungleichungen | Lineare Ungleichungen & Intervalle | Analysis |
| 6 | 7-potenzgesetze | Potenzgesetze (natuerliche Exp.) | Analysis |
| 7 | 7-dreiecke-kongruenz | Dreiecke & Kongruenzsaetze | Geometrie |
| 8 | 7-konstruktionen | Konstruktionen (Zirkel & Lineal) | Geometrie |
| 9 | 7-winkel-winkelsumme | Winkel, Winkelsumme, Scheitelwinkel | Geometrie |
| 10 | 7-symmetrie | Achsen- & Punktsymmetrie | Geometrie |
| 11 | 7-vierecke | Symmetrische Vierecke | Geometrie |
| 12 | 7-daten-diagramme | Daten & Diagramme — Kenngroessen | Stochastik |

### Klasse 8 — 14 Trainer

| Nr | Dateiname | Thema | Bereich |
|----|-----------|-------|---------|
| 13 | 8-bruchterme-grundlagen | Bruchterme (kuerzen, erweitern, rechnen) | Analysis |
| 14 | 8-bruchgleichungen | Bruchgleichungen | Analysis |
| 15 | 8-lineare-funktionen-grund | Lineare Funktionen — Grundlagen | Analysis |
| 16 | 8-lineare-funktionen-anwendungen | Lineare Funktionen — Anwendungen | Analysis |
| 17 | 8-lgs | Lineare Gleichungssysteme | Analysis |
| 18 | 8-potenzen-negativ | Potenzen mit negativen Exponenten | Analysis |
| 19 | 8-proportionalitaet | Proportionalitaet & Dreisatz | Analysis |
| 20 | 8-aehnlichkeit-streckung | Aehnlichkeit & zentr. Streckung | Geometrie |
| 21 | 8-strahlensatz | Strahlensaetze | Geometrie |
| 22 | 8-kreise | Kreisumfang & Kreisflaeche | Geometrie |
| 23 | 8-raumgeometrie-grund | Grundlagen der Raumgeometrie | Geometrie |
| 24 | 8-vektoren-2d | Vektoren (zweidimensional) | Geometrie |
| 25 | 8-stoch-laplace | Laplace-Wahrscheinlichkeit | Stochastik |
| 26 | 8-stoch-zaehlprinzip | Zaehlprinzip & Ergebnismengen | Stochastik |

### Klasse 9 — 16 Trainer

| Nr | Dateiname | Thema | Bereich |
|----|-----------|-------|---------|
| 27 | 9-quadratwurzeln | Quadratwurzeln & reelle Zahlen | Analysis |
| 28 | 9-potenzen-ganzzahlig | Potenzgesetze (ganzzahlige Exp.) | Analysis |
| 29 | 9-potenzen-rational | Potenzen & Wurzeln (rationale Exp.) | Analysis |
| 30 | 9-quadratische-funktionen | Quadratische Funktionen | Analysis |
| 31 | 9-quadratische-gleichungen | Quadratische Gleichungen & Vieta | Analysis |
| 32 | 9-exponentielles-wachstum | Exponentielles Wachstum | Analysis |
| 33 | 9-pythagoras | Satz des Pythagoras | Geometrie |
| 34 | 9-trig-rechtwinkliges-dreieck | Trigonometrie am rechtwinkl. Dreieck | Geometrie |
| 35 | 9-raumgeometrie-prisma-zylinder | Prisma & Zylinder | Geometrie |
| 36 | 9-raumgeometrie-pyramide-kegel | Pyramide & Kegel | Geometrie |
| 37 | 9-raumgeometrie-anwendungen | Raumgeometrie — Anwendungen | Geometrie |
| 38 | 9-flaechenberechnung-determinante | Flaechenberechnung (Determinante) | Geometrie |
| 39 | 9-stoch-haeufigkeiten | Relative Haeufigkeit | Stochastik |
| 40 | 9-stoch-boxplot | Histogramm & Boxplot | Stochastik |
| 41 | 9-wurzelgleichungen | Wurzelgleichungen | Analysis |
| 42 | 9-potenzgleichungen | Potenzgleichungen | Analysis |

### Klasse 10 — 14 Trainer

| Nr | Dateiname | Thema | Bereich |
|----|-----------|-------|---------|
| 43 | 10-ganzrationale-funktionen | Ganzrationale Funktionen | Analysis |
| 44 | 10-polynomdivision | Polynomdivision & Nullstellen | Analysis |
| 45 | 10-potenzfunktionen | Potenzfunktionen | Analysis |
| 46 | 10-graphen-transformationen | Verschieben, Spiegeln, Strecken | Analysis |
| 47 | 10-exponentialfunktionen | Exponentialfunktionen & Wachstum | Analysis |
| 48 | 10-logarithmus | Logarithmus & Rechenregeln | Analysis |
| 49 | 10-substitution | Gleichungen loesen durch Substitution | Analysis |
| 50 | 10-trig-einheitskreis | Sinus & Kosinus am Einheitskreis | Geometrie |
| 51 | 10-trig-sinusfunktion | Allgemeine Sinusfunktion | Geometrie |
| 52 | 10-trig-gleichungen | Trigonometrische Gleichungen | Geometrie |
| 53 | 10-trig-sinussatz-kosinussatz | Sinus- & Kosinussatz | Geometrie |
| 54 | 10-kreissektor | Kreissektor & Kreissegment, Bogenmass | Geometrie |
| 55 | 10-stoch-bedingte-wsk | Bedingte Wahrscheinlichkeit | Stochastik |
| 56 | 10-stoch-mehrstufig | Mehrstufige Zufallsexperimente | Stochastik |

### Klasse 11–12 GK — 22 Trainer

| Nr | Dateiname | Thema | Bereich |
|----|-----------|-------|---------|
| 57 | 11-aenderungsrate | Mittlere & lokale Aenderungsrate | Analysis |
| 58 | 11-ableitungsregeln | Ableitungsregeln (Potenz, Summe, Faktor) | Analysis |
| 59 | 11-ableitung-ketten-produkt | Ketten- & Produktregel | Analysis |
| 60 | 11-monotonie-kruemmung | Monotonie & Kruemmung | Analysis |
| 61 | 11-extrempunkte-wendepunkte | Extrem- & Wendepunkte | Analysis |
| 62 | 11-kurvendiskussion-ganzrational | Kurvendiskussion ganzrational | Analysis |
| 63 | 11-tangenten-normalen | Tangentengleichung & Steigungswinkel | Analysis |
| 64 | 11-extremwertaufgaben | Extremwertaufgaben | Analysis |
| 65 | 11-e-funktion | e-Funktion & ln — Grundlagen | Analysis |
| 66 | 11-e-funktion-ableitung | e-Funktion & ln — Ableitung | Analysis |
| 67 | 11-steckbriefaufgaben | Bestimmung ganzrationaler Funktionen | Analysis |
| 68 | 12-stammfunktionen | Stammfunktion | Analysis |
| 69 | 12-bestimmtes-integral | Bestimmtes Integral | Analysis |
| 70 | 12-flaechenberechnung | Integrale — Flaechenberechnung | Analysis |
| 71 | 12-vektoren-grundlagen | Vektoren im Raum — Grundlagen | Geometrie |
| 72 | 12-geraden-raum | Geraden im Raum | Geometrie |
| 73 | 12-ebenen | Ebenen (Parameter-/Normalen-/Koordinatenform) | Geometrie |
| 74 | 12-skalarprodukt | Skalarprodukt & Vektorprodukt | Geometrie |
| 75 | 12-stoch-binomialverteilung | Binomialverteilung | Stochastik |
| 76 | 12-stoch-sigma-regeln | Sigma-Regeln | Stochastik |
| 77 | 12-stoch-zufallsgroessen | Zufallsgroessen & Verteilungsfunktion | Stochastik |
| 78 | 12-stoch-hypothesentests | Testen von Hypothesen | Stochastik |

### Klasse 11–12 LK-Extras — 12 Trainer

| Nr | Dateiname | Thema | Bereich |
|----|-----------|-------|---------|
| 79 | 11-lk-funktionsscharen | Funktionenscharen | Analysis |
| 80 | 11-lk-newton | Newton-Verfahren | Analysis |
| 81 | 11-lk-gebrochen-rational | Gebrochen-rationale Funktionen | Analysis |
| 82 | 11-lk-kurvendisk-erweitert | Kurvendiskussion (trig, exp, gebr.-rat.) | Analysis |
| 83 | 12-lk-integral-rotationskoerper | Rotationskoerper (Volumen) | Analysis |
| 84 | 12-lk-integral-uneigentlich | Uneigentliche Integrale | Analysis |
| 85 | 12-lk-dgl | Differentialgleichungen | Analysis |
| 86 | 12-lk-geom-abstaende | Abstandsbestimmungen im Raum | Geometrie |
| 87 | 12-lk-geom-lagebeziehungen | Lagebeziehungen (Geraden, Ebenen) | Geometrie |
| 88 | 12-lk-geom-schnittwinkel | Schnittwinkel | Geometrie |
| 89 | 12-lk-stoch-normalverteilung | Normalverteilung | Stochastik |
| 90 | 12-lk-stoch-prozesse | Stochastische Prozesse (Matrizen) | Stochastik |

## Index-Dashboard Struktur

6 Klassen-Spalten (7–12), aufgeteilt in Section-Cards nach Bereich:
- Analysis (blau/lila)
- Geometrie (gruen)
- Stochastik (orange)

Filter-Bars:
- Klasse: Alle | 7 | 8 | 9 | 10 | 11 | 12
- Niveau: Alle | Nur GK | Nur LK

LK-Trainer bekommen LK-Badge und `.lk-only`-Klasse (analog zu DiffEngine).

## Infrastruktur

- GitHub-Repo: `Mathepfade`
- GitHub Pages: `https://nachbar-blip.github.io/Mathepfade`
- Tests: Playwright-Suite mit 90 parametrisierten Trainern
- spirale-engine.js: Ref4OHG-Version mit allen Bugfixes
- spirale.css: Ref4OHG-Version mit allen Bugfixes
