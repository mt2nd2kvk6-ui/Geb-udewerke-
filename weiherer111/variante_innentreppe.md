# Variante B: innenliegendes Treppenhaus statt Außentreppe

Stand: 26.11.2026. Ergänzung zum Modernisierungsplan. Im Rundgang `umbau_rundgang.html` mit dem Schalter „Umbau B Innentreppe“ begehbar. Pläne: `plaene/innen_EG.svg`, `innen_OG.svg`, `innen_DG.svg`, Längsschnitt `innen_Schnitt_C-C.svg`. Kosten: `massnahmen_und_kosten.xlsx`, Blatt „Variante B Innentreppe“.

## Idee

Die Treppe liegt in der vorhandenen Eingangszone zwischen Anbau West und Altbau (x 6,16 bis 8,37 m, y 8,10 bis 13,63 m). Dort sind heute Hauseingang, Eingangstreppe und der westliche Teil des Hausflurs, also schon Allgemeinfläche. Die alte Holztreppe in W2 wird nicht genutzt. Keine Wohnung verliert Fläche.

Die Zone wird zum durchgehenden Treppenraum vom Hauseingang bis unter das Dach. Die Treppe ist zweiläufig gegenläufig mit zwei Laufspuren von je 1,05 m und einem Treppenauge von 0,11 m. Die Podeste liegen abwechselnd im Norden (Wohnungseingänge) und im Süden (Zwischenpodeste mit Fenster zum Hof).

| Lauf | von | nach | Steigungen | Steigung | Auftritt |
|---|---|---|---|---|---|
| 1 | Hauseingang +0,41 (Süd) | Hausflur EG +2,25 (Nord) | 10 | 18,4 cm | 27 cm |
| 2 | Hausflur EG +2,25 | Podest 1 +3,92 (Süd) | 9 | 18,5 cm | 27 cm |
| 3 | Podest 1 +3,92 | OG-Podest +5,40 (Nord) | 8 | 18,5 cm | 27 cm |
| 4 | OG-Podest +5,40 | Podest 2 +6,68 (Süd) | 7 | 18,2 cm | 27 cm |
| 5 | Podest 2 +6,68 | DG-Podest +7,95 (Nord) | 7 | 18,2 cm | 27 cm |

Zugang der Wohnungen:

| Wohnung | Zugang |
|---|---|
| W1 | unverändert eigener Eingang Nordseite |
| W2 | Hausflur EG, Tür in der Altbau-Südwand |
| W3 | Hausflur EG, 5 Stufen zum Zugang W3 |
| W4 (OG West, +5,40) | OG-Podest, stufenlos durch die Westwand in eine neue Diele (2,55 m²) mit Tür zum Flur und zum Wohnraum |
| W5 (OG Altbau, +5,00) | OG-Podest durch die Altbau-Südwand in die Küche/Essen, innen ein Podest und 3 Stufen à 13,3 cm hinunter |
| W6 (DG West, +7,95) | DG-Podest, stufenlos |
| W7 (DG Ost, +7,70) | DG-Podest über das Zwerchhaus, innen 2 Stufen à 12,5 cm hinunter |

Prüfung im Modell (`pruefung.py umbau_innen.json`): alle 43 Ziele erreichbar, größte Stufe 0,186 m, Kopfhöhe auf allen Läufen und Podesten mindestens 2,00 m (kleinster Wert unter dem DG-Podest 2,05 m), kein Bauteil durch die Dachhaut. Ein Sofa von 2,20 m passt auf den geraden Läufen; an den Podesten (1,10 × 2,22 m, Raumhöhe über 2,30 m) muss es hochkant gedreht werden.

## Brandschutz

Weil der DG-Fußboden über 7 m über Gelände liegt (Gebäudeklasse 4), ist die Treppe eine notwendige Treppe in einem notwendigen Treppenraum. Daraus folgen, und so ist es eingeplant:

* Wände des Treppenraums hochfeuerhemmend, auch unter mechanischer Beanspruchung: Mauerwerk. Die West- und Nordwand gibt es schon (Außenwände von Anbau West und Altbau), Ost- und Südwand werden oberhalb des Flachdachs neu gemauert.
* Treppe aus nichtbrennbaren Baustoffen: Stahlwangen mit Betonwerksteinstufen, Podeste aus Stahlbeton.
* Der Treppenraum reicht bis unter die Dachhaut; oberer Abschluss ist das Dach.
* Rauchabzug oben mit mindestens 1 m² Öffnung, auslösbar im EG und am DG-Podest.
* Wohnungstüren zum Treppenraum dicht- und selbstschließend.
* Unmittelbarer Ausgang ins Freie über die Haustür.
* Keine Fenster von Wohnungen in den Treppenraum: Das Küchenfenster W2 zum Hausflur und das Küchenfenster W5 werden geschlossen oder als Brandschutzverglasung ausgeführt. Die Küche von W5 ist über die 2 m breite Öffnung mit dem Wohnraum verbunden; fensterlose Küchen sind mit wirksamer Lüftung zulässig.
* Zweiter Rettungsweg wie in Variante A über anleiterbare Fenster.

## Was sich gegenüber Variante A ändert

* Es entfallen Hoftreppe, Podeste P1 und P2, die Treppe zum DG, der Laubengang und die Tieferlegung der Flachdachdecke.
* Das Flachdach über Hausflur Ost, Technikraum und Bad W2 bleibt auf alter Höhe und wird gedämmt. Der Höhenkonflikt mit den OG-Fenstern wird anders gelöst: Die zwei Südfenster von W5 an dieser Stelle (Flur und Bad) bekommen eine Brüstung bei +6,15. So bleiben 15 cm Abdichtungshochzug über der neuen Dachoberkante.
* Das Schleppdach des Westflügels läuft über den Treppenraum weiter. Darauf liegen 4 weitere PV-Module, zusammen 7,3 kWp und rund 7.000 kWh im Jahr.
* W6 verliert die Fenster in der Ostwand (sie ist jetzt Treppenraumwand). Dafür bekommt der Wohnraum zwei Dachflächenfenster im Westhang.
* Der Hof bleibt frei von Treppen.

## Vergleich

| Kriterium | A: Außentreppe, Laubengang | B: Innentreppe |
|---|---|---|
| Kosten brutto inkl. Reserve | 539.242 € | 553.021 € (+13.779 €, +2,6 %) |
| Wohnfläche | 454,60 m² | 454,59 m² |
| Komfort, Vermietbarkeit | Wege im Freien, bei Regen und Eis unangenehm, Laubengang führt an Fenstern vorbei | geschützter, beheizbarer Zugang mit Klingel und Briefkästen, üblicher Standard; eher leichter zu vermieten |
| Brandschutz, Genehmigung | Außentreppe muss im Brandfall sicher nutzbar sein; Fenster neben der Treppe prüfen | klare Regellösung, aber mit Rauchabzug, Türen und Wandqualität |
| Bauen im bewohnten Haus | Eingang EG bleibt unberührt | Eingangszone wird umgebaut; W2 und W3 brauchen für einige Tage einen Behelfszugang (Gerüsttreppe), wenn Lauf 1 und 2 eingehoben werden |
| Hof | Treppe mit Podest belegt rund 16 m² Hof | Hof frei |
| Unterhalt | verzinkter Stahl außen, Abdichtung Laubengang | gering |
| Licht in den Wohnungen | unverändert | W2-Küche und W5-Küche ohne eigenes Fenster, W6 mit Dachfenstern statt Ostfenstern |

**Einschätzung:** Variante B ist nur 2,6 % teurer, ergibt die besseren Wohnungen und ist die übliche, leicht genehmigungsfähige Lösung. Ich würde B nehmen, wenn die Brandschutzplanung die Lage des Treppenraums bestätigt und sich der Bauablauf an der Eingangszone mit den Mietern von W2 und W3 regeln lässt. A bleibt sinnvoll, wenn das Budget um jeden Euro geht oder die EG-Mieter keine Bauarbeiten am Hauseingang dulden.

## Zusätzliche offene Punkte zu Variante B

| Nr | Punkt | Zuständig |
|---|---|---|
| V1 | Lage, Wände, Türen und Rauchabzug des Treppenraums mit dem Brandschutzplaner abstimmen; Türen von Technikraum und Keller zum Treppenraum (Feuerschutzabschluss). | Brandschutzplaner |
| V2 | Abfangung der neuen Ostwand über dem Hausflur, Deckenausschnitt für Lauf 1 über dem Keller, Auflager der Podeste in Bestandswänden von 1949 und 1966. | Statiker |
| V3 | Behelfszugang für W2 und W3 während des Einbaus von Lauf 1 und 2, Bauablauf mit Kran. | Bauleitung, Mieter |
| V4 | Kellerzugang: Liegt die Kellertreppe in der Eingangszone? Wenn ja, Abtrennung zum Treppenraum. | Architekt (Aufmaß) |
| V5 | Zählerschrank im Technikraum am Treppenraum: Leitungsanlagen im Treppenraum nur nach Leitungsanlagen-Richtlinie. | Elektrofachbetrieb, Brandschutzplaner |
| V6 | Keine Abstellflächen im Treppenraum, auch nicht unter Lauf 2 (Brandlast). | Eigentümer |
| V7 | Möbeltransport über die Podeste (Sofa hochkant) mit realen Maßen prüfen. | Architekt |
