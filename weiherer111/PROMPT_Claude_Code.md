# Auftrag: Weiherer Straße 111, Ubstadt-Weiher: Umbau zu 7 Wohnungen als begehbares 3D-Modell mit Modernisierungsplan

Arbeite auf Deutsch. Schreibe sachlich, ohne Emojis, ohne Ausrufezeichen, ohne Gedankenstriche. Nenne Annahmen ausdrücklich. Wenn etwas unklar ist und das Ergebnis wesentlich verändert, frag mich, bevor du baust. Wenn du einen Widerspruch oder eine schlechte Idee in meinen Vorgaben siehst, sag es einmal deutlich und setze danach um, was ich entscheide.

## 1. Ziel

Ich habe das Mehrfamilienhaus gekauft (4 Wohnungen, Baujahr Altbau 1949, Anbauten 1954/55 und 1966). Die Bank verlangt einen Modernisierungsplan, ich will über KfW 261 (Effizienzhaus) fördern lassen. Das meiste machen wir selbst.

Zeig mir das Haus vollständig fertig umgebaut. Zwei Dinge sind gleich wichtig:

1. **Realistisch, wirtschaftlich, mit möglichst wenig Aufwand.** Immer die einfachste und günstigste Lösung, die baurechtlich und technisch hält und die KfW-Anforderungen erfüllt. Keine Showlösungen, kein Treppenturm, kein teures Treppenhaus.
2. **Maximale Mieteinnahmen.** Möglichst viel vermietbare Wohnfläche nach WoFlV, sinnvolle Wohnungsgrößen für den Markt in Ubstadt-Weiher.

## 2. Unterlagen im Projektordner

| Datei | Inhalt |
|---|---|
| `Zeichnungen_Grundrisse_Weiherer_Str_111.pdf` | Aufmaß Nagel vom 24.09.2026 (KG, EG, OG, DG, 2 Schnitte, 3 Ansichten), Exposé, Energieausweis, Bauakte 1949 bis 1966, Lageplan. Lege ich selbst in den Ordner. |
| `bestand_geometrie.py` | Geprüftes Bestandsmodell als Python (Wände, Öffnungen, Böden, Treppen, Dächer, Räume mit Flächen). Maße in Metern. |
| `generator.py` | Erzeugt aus der Geometrie eine JSON-Datei: `python generator.py bestand_geometrie.py bestand.json` |
| `vorlage_rundgang.html` | Three.js-Seite mit Ich-Perspektive (Joystick links, Umsehen rechts, WASD), Treppensteigen, Ducken unter Schrägen, Raumanzeige, Modellansicht mit Ebenen ausblenden. Platzhalter `__DATA__` wird durch die JSON ersetzt. |
| `bestand.html` | Fertig erzeugter Bestandsrundgang zum Vergleich. |

Nutze diese Dateien als Grundlage. Lies das PDF selbst nach, wo du Maße brauchst (Seiten als Bild rendern und ansehen). Die Werte unten sind bereits aus dem PDF abgeleitet und gegengeprüft.

## 3. Bestand: gesicherte Daten

### 3.1 Koordinaten und Höhenbezug

- x nach Osten, y nach Süden (Planrichtung), Ursprung nordwestliche Außenecke Anbau West. Höhe z ab Oberkante Fertigfußboden Keller = ±0,00.
- In Three.js: X = x, Y = z, Z = y.
- Gelände laut Schnitten ca. **+0,40 bis +0,42**. Hof und Garten liegen rund ums Haus **eben auf diesem Niveau**. Das ist so in echt, bitte keine abgesenkten Bereiche mehr modellieren (im mitgelieferten Bestandsmodell ist vor dem Hauseingang noch fälschlich eine Senke auf ±0; korrigieren).
- Bezeichnungen „EG links“, „EG oben“, „EG unten“ im Aufmaß sind **Lagen im Plan**, keine Höhenlagen.
- Ansicht „Hofseite“ ist die **Westfassade** (Norden links). Ansicht „Straßenseite“ ist die **Nordfassade**, von der Straße aus gesehen liegt Osten links.
- Ostwand ist Grenzwand ohne Öffnungen.

### 3.2 Baukörper

| Teil | Grundriss außen | Geschosse |
|---|---|---|
| Altbau 1949 | x 5,915 bis 15,085; y 0 bis 8,10 (9,17 × 8,10 m) | KG, EG, OG, Dachboden |
| Anbau West 1966 | x 0 bis 6,155; y 0 bis 13,865 | KG, EG, OG, Dachraum |
| Streifen südlich Altbau | x 6,155 bis 15,085; y 8,10 bis 12,21 | EG mit Flachdach |
| Anbau Garten (Wohnung 03) | x 8,475 bis 15,085; y 12,21 bis 21,20 | Garagen/KG, EG, Flachdach |
| Garage mit Balkon darauf | x 11,365 bis 15,085; y 21,20 bis 28,25 | Garage, Balkon Wohnung 03 |

Außenwände 0,24 m (Anbau Garten 0,30 m, Ostwand Streifen 0,28 m).

### 3.3 Höhen (aus Schnitten, z ab Kellerfußboden)

| Bereich | OKFF | lichte Höhe | Decke/Dach darüber |
|---|---|---|---|
| KG | ±0,00 | 2,00 | Decke 0,25 |
| EG W1 (West) | +2,25 | 2,90 | OG-Decke 5,15 bis 5,38 |
| EG W2 (Altbau), Hausflur, WC, Bad W2 | +2,25 | 2,50 (Hausflur bis Flachdach 3,21) | |
| EG W3 mit Zugang und Küche | +3,15 (5 Stufen über Hausflur) | 2,31 | Flachdach UK 5,46, OK 5,76 |
| OG Altbau | +5,00 | 2,41 | Decke 7,41 bis 7,60 |
| OG West | +5,40 (Stufe 0,40 zum Altbau) | **2,27, unter 2,30 nach § 34 LBO BW** | Decke 7,67 bis 7,87 |
| Dachboden Altbau | +7,60 | First innen ca. 2,80 | |

### 3.4 Dächer im Bestand (aus Schnitt Altbau und Westansicht)

- **Hauptdach:** geknicktes Satteldach, First Ost-West bei y 4,05, läuft über die **volle Länge 15,08 m**, also auch über den Nordteil des Anbaus West bis zur Westfassade. Oberkante: Traufe +7,64 (Überstand 0,37), Knick +9,31 bei 2,88 m von der Außenwand, First +10,72. Unten ca. 27 Grad, oben ca. 50 Grad. Auf der Südseite über dem Anbau West läuft die steile Fläche bis ca. y 6,30 durch.
- **Dach Anbau West, Südteil:** Satteldach, First Nord-Süd bei x 3,08, Traufe +7,89, First +9,54, ca. 28 Grad, schließt bei y ca. 5,05 mit einer Kehle an die steile Fläche an.
- Dachboden Altbau ist durch die Giebelwand x 5,915 bis 6,155 vom Dachraum Anbau West getrennt.
- Kamine: x 8,88 bis 9,44 / y 4,13 bis 4,75 (Altbau) und x 5,505 bis 5,915 / y 4,355 bis 4,785 (West), Küche W3 0,49 × 0,32 m.

### 3.5 Wohnungen und Treppen im Bestand

- **W1 EG West:** Flur 2,29, Wohnen/Schlafen 55,16 (mit Raumteiler), Bad 6,04, Küche 5,51, Abstellraum 3,14 m². Eigener Eingang Nordseite über 7 Außenstufen.
- **W2 EG Altbau:** Wohnen 16,35, Schlafen 14,60, Küche 12,01, Flur 3,80, begehbarer Kleiderschrank 9,77, Bad 3,37 m² (im Streifen). Eingang vom Zugang Whg 02/04.
- **W3 EG Anbau Garten:** Zugang 4,43, Küche 6,68, Wohnen/Essen 28,25, Schlafen 16,08, Bad 6,40, Balkon 23,28 m². 5 Stufen vom Hausflur hoch.
- **W4 OG (ganzes OG):** Schlafen 14,01, Bad 5,07, Gäste 12,71, Flur 8,79, Wohnen 31,84 (West); Raum 01 16,35, Raum 02 14,60, Küche 12,02, Hausflur 6,87, Raum 03 9,77 m² (Altbau). Summe 132,0 m².
- **Hauseingang:** große Treppe in der Lücke zwischen Anbau West und Zugang W3 (x 6,155 bis 8,37; y 10,78 bis 13,62) vom Hof in den Hausflur. Mit Gelände +0,40 sind das ca. 10 Steigungen.
- **Treppe EG zum OG:** im Zugang Whg 02/04, x 10,97 bis 11,985, Wendelstufen unten, gerade nach Norden, 15 Steigungen, kommt im OG bei y 4,84 an.
- **Bodentreppe OG zum Dachboden:** x 10,98 bis 11,94, y 7,30 bis 5,41, sehr steil, für Umzüge unbrauchbar.
- **Unsicherheiten** (vor Ort klären, im Modell als Annahme markieren): genaue Lage der beiden Innentreppen zueinander, Garagenhöhe unter W3, Höhe von W3 gegenüber dem Hof, Lage und Breite einzelner Fenster.

## 4. Was ich will

### 4.1 Wohnungen: insgesamt 7

| Geschoss | Wohnungen | Vorgabe |
|---|---|---|
| EG | W1, W2, W3 | bleiben, werden renoviert. Zugang über den Hauseingang einfach und klar. |
| OG | 2 Wohnungen | sinnvoll aufteilen, naheliegend an der Höhenstufe 0,40 zwischen West und Altbau. Eingang über die Terrasse. |
| DG | 2 Wohnungen | durch Anheben **beider** Dächer. Prüfe als Vorzugslösung die Teilung an der vorhandenen Giebelwand x 5,915 bis 6,155 (DG Ost über Altbau, DG West über Anbau West). Jede Wohnung hat dann ein einheitliches Fußbodenniveau, die Wand ist schon da. |

Wohnungen innen modern, **ohne Möbel**, aber realistisch: Böden, Wandflächen, Innentüren, Bäder mit bodengleicher Dusche und fest eingebauten Sanitärobjekten, Küchenbereich als Anschluss- und Stellfläche markiert, Heizkreisverteiler, Lüftungsauslässe, Treppen und Geländer.

### 4.2 Dächer und Gauben

- Beide Dächer anheben, sodass vollwertige Wohnungen entstehen. Prüfe: Kniestock ca. 1,00 bis 1,20 m innen, einfacher Satteldachaufbau statt Knickdach, wenig Gauben mit großer Wirkung (Schleppgauben bevorzugt, Zwerchhaus nur wenn es die Erschließung braucht).
- Ich will die Neueindeckung und Dämmung in Eigenleistung machen. Ursprünglich geplant: Dämmung von innen (Zwischen- und Untersparren). Vergleiche das ehrlich mit Aufsparrendämmung, wenn der Dachstuhl ohnehin neu entsteht. Statik und Abbund/Richten des neuen Dachstuhls einplanen, das geht praktisch nur mit Zimmerer und Statiker.
- Prüfe, ob beim Anheben über dem Anbau West die OG-West-Decke neu und höher gesetzt werden kann, sodass das OG West auf mindestens 2,30 m kommt. Kosten und Nutzen nennen.
- Photovoltaik auf der Süddachfläche des Hauptdachs (First Ost-West), Größe in kWp und Ertrag grob angeben.

### 4.3 Erschließung

- OG über eine günstige, feuerverzinkte Stahltreppe vom Hof auf die Terrasse über dem EG-Streifen, von dort Wohnungseingänge.
- DG: bring mir die einfachste regelkonforme Lösung (zum Beispiel weiter über die Terrasse mit kurzer Treppe zu einem Eingang im Dach, oder eine neue gerade Innentreppe ab Terrassenebene). Laufbreite mindestens 1,00 m, gerade Läufe, Möbel wie ein 2,20-m-Sofa müssen durchgehen.
- **Bekannter Höhenkonflikt, ausdrücklich lösen:** Flachdach-OK +5,76 liegt über dem OG Altbau (+5,00) und dem OG West (+5,40); die Südfenster im OG Altbau haben Brüstung +5,82. Prüfe zum Beispiel, ob das Flachdach nur über Hausflur, WC und Bad W2 (Fußboden 2,25, viel Raumhöhe) tiefer gesetzt werden kann, sodass dort ein Laubengang auf ca. +4,85 bis +5,00 entsteht. Über Zugang und Küche W3 (Fußboden 3,15) geht das nicht.
- Jede Treppe braucht einen erreichbaren Anfang und ein erreichbares Ende, jede Wohnung einen ersten und zweiten Rettungsweg. Kopfhöhe auf Treppen mindestens 2,00 m. Steigung 17 bis 19 cm, Auftritt 26 bis 29 cm.

### 4.4 Energie: KfW 261 tauglich

- Ziel ist ein Effizienzhaus nach KfW 261, voraussichtlich EH 85 EE oder EH 70 EE. Recherchiere die **aktuellen** Anforderungen und Fördersätze auf kfw.de, im GEG und in den BEG-Richtlinien und nenne die Quelle. Prüfe auch, ob der Altbau als Worst Performing Building gilt (Energieausweis im PDF, Baujahr 1949), wie neu geschaffene Wohnungen im DG gefördert werden und unter welchen Bedingungen Eigenleistung (Materialkosten) förderfähig ist.
- Bauteile mit Ziel-U-Werten aus den aktuellen Anforderungen: Fassade (WDVS, in Eigenleistung), Dach, oberste bzw. unterste Decke, Kellerdecke von unten, Fenster 3-fach in KfW-Standard (Uw mindestens nach aktueller Vorgabe), Haustüren.
- Luft-Wasser-Wärmepumpe (Aufstellort, Schallabstand zur Grenze prüfen), Fußbodenheizung im Bestand möglichst als Fräs- oder Dünnschichtsystem ohne große Aufbauhöhe, im DG Trockensystem.
- Lüftung: Lüftungskonzept nach DIN 1946-6, kostengünstige Abluftanlage (zentral oder dezentral je Wohnung) mit Außenluftdurchlässen.
- Warmwasser: zentral über die Wärmepumpe oder dezentral elektrisch, mit ehrlicher Abwägung von Kosten, Effizienzhaus-Nachweis und Betrieb.
- Eine grobe Abschätzung des Effizienzhaus-Niveaus (Hüllfläche, Transmissionswärmeverlust, Primärenergie) gegen die Referenz. Kennzeichne klar, dass der Nachweis vom Energieeffizienz-Experten kommen muss.

### 4.5 Außen

- Fassade schön, aber günstig: WDVS mit hellem Putz, dunkler Sockel, ruhige Fensterteilung, gleiche Fensterformate wo möglich.
- Dach in Anthrazit, Gauben passend, Rinnen und Fallrohre.
- Hof umlaufend befestigt, Garten ebenerdig.
- **Stellplätze:** sinnvoll anordnen nach den Regeln. Recherchiere § 37 LBO BW und eine eventuelle Stellplatzsatzung der Gemeinde Ubstadt-Weiher, beachte die GaVO BW. Planungsansatz 2,50 × 5,00 m. Vorhandene Garagen anrechnen. Lageplan aus dem PDF für Grundstücksgrenzen und Zufahrt nutzen. Fahrradstellplätze nach LBO BW prüfen.

## 5. Ergebnisse, die ich am Ende haben will

1. **`umbau_rundgang.html`**: eine eigenständige Seite, auf dem Handy nutzbar. Umschalter Bestand und Umbau, Ich-Rundgang durch alle 7 Wohnungen, Treppenhaus, Terrasse, Dach. Außenansicht mit Ebenen ausblenden. Raumanzeige mit Name und Fläche. Startpunkte für jede Wohnung. Materialien realistisch (prozedurale Texturen für Putz, Ziegel, Parkett oder Vinyl, Fliesen, Holz, Stahl, Glas), Sonnenstand, Schatten.
2. **Grundrisse** Bestand und Umbau je Geschoss als SVG (Maßketten, Raumflächen nach WoFlV, Höhenkoten) und **ein Schnitt** durch Altbau und Anbau West.
3. **`flaechen_und_mieten.xlsx`**: Wohnflächen nach WoFlV je Raum und Wohnung, Mietansatz je m² mit Quelle (Mietspiegel oder Angebote Ubstadt-Weiher und Bruchsal, recherchieren), Nettokaltmiete je Wohnung und gesamt, vorher und nachher. Rendite so gerechnet: **Nettokaltmiete × 100 / Kaufpreis**, PV-Erlöse außen vor. Den Kaufpreis frage ich dich nicht ab, lass dafür eine Eingabezelle.
4. **`massnahmen_und_kosten.xlsx`**: jede Maßnahme mit Menge, Materialkosten, Fremdleistung, Eigenleistung ja oder nein mit Begründung, Gewerk mit Fachfirmen- oder Nachweispflicht (Statik, Zimmerer, Elektro, Kältekreis, Schornsteinfeger, Energieeffizienz-Experte), Förderfähigkeit. Summen nach Bauabschnitten.
5. **`modernisierungsplan.md`** für die Bank: Zustand, Ziel, Maßnahmen, Reihenfolge, Kosten, Förderung, Zeitplan. Reihenfolge so, wie ich es vorhabe: zuerst Dächer und 2 DG-Wohnungen schaffen und vermieten, danach die Bestandswohnungen nacheinander leerziehen und einzeln sanieren. Haus bleibt während der Bauzeit bewohnt.
6. **`pruefliste.md`**: alle Annahmen und offenen Punkte mit Zuständigkeit. Mindestens: Baugenehmigung und Bebauungsplan bzw. § 34 BauGB, Firsthöhe, Abstandsflächen, Gebäudeklasse (Fußboden DG über mittlerem Gelände, Grenze 7 m nach § 2 LBO BW), zweiter Rettungsweg DG, Brandschutz der Wohnungstrennwände und Decken, Schallschutz DIN 4109, Statik Aufstockung auf Mauerwerk von 1949, lichte Raumhöhe OG West, Stellplätze, Nachbarrecht an der Grenzwand, **KfW-Antrag vor Vorhabenbeginn** und Verträge mit aufschiebender Bedingung.

## 6. Arbeitsweise

1. Lies das PDF und die mitgelieferten Dateien. Rendere die Pläne, Schnitte und Ansichten als Bilder und sieh sie dir an. Gleiche Abschnitt 3 dagegen ab und melde Abweichungen.
2. Korrigiere zuerst das Bestandsmodell (Gelände eben auf ca. +0,40, Hauseingangstreppe mit ca. 10 Steigungen) und lass mich den Bestand kurz bestätigen.
3. Schlag mir dann das Umbaukonzept in einer kurzen Übersicht vor (Wohnungen, Flächen, Erschließung, Dach, Energie, Kostenrahmen), mit maximal zwei Varianten, wo es echte Unterschiede gibt. Erst nach meiner Freigabe ausmodellieren.
4. Baue das Umbaumodell im selben Datenformat wie `bestand_geometrie.py` (eigene Datei `umbau_geometrie.py`), erzeuge die JSON und die Seite.
5. **Prüfe selbst, bevor du mir etwas zeigst:**
   - Laufweg-Test als Skript: Straße oder Hof bis in jede Wohnung, über alle Treppen, auf Terrasse und ins DG. Kein Hindernis, keine Stufe über 0,20 m, Kopfhöhe mindestens 2,00 m auf Treppen.
   - Keine Bauteile, die durch Decken oder Dächer stoßen. Dachunterseite überall über der Raumdecke darunter.
   - Flächen je Wohnung nachrechnen, Summen gegen die Tabellen.
   - Seite mit Playwright headless öffnen, Screenshots von außen (Nordwest, Südwest, Südost) und aus jeder Wohnung machen, ansehen und Fehler beheben. Konsole auf Fehler prüfen.
6. Gib mir am Ende kurz: was entstanden ist, die wichtigsten Zahlen (Wohnfläche vorher und nachher, Miete vorher und nachher, Kosten, Förderung, Eigenleistungsanteil), die größten Risiken und die Dateien.

## 7. Rahmen

- Budget: Die Bank bietet zusätzlich 100.000 € für die Modernisierung. Zeig ehrlich, was davon realistisch abgedeckt ist und was darüber hinaus Eigenleistung, Förderung oder weitere Finanzierung braucht. Schlag eine Reihenfolge vor, die mit diesem Rahmen startet und früh Mieteinnahmen bringt.
- Deutsches Recht, Landesbauordnung Baden-Württemberg. Bei Recht, Steuern und Förderung Primärquellen nennen und auf Fachleute verweisen (Architekt oder Bauvorlageberechtigter, Statiker, Brandschutz, Energieeffizienz-Experte, bei Modernisierungsumlage nach § 559 BGB ein Fachanwalt oder Haus & Grund).
- Datumsformat TT.MM.JJJJ, Beträge in Euro.
