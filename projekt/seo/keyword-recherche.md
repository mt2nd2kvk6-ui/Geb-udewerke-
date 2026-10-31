# Keyword-Recherche Gebäudewerke (Stand 31.10.2026)

## 1. Methode

1. Bestandsaufnahme der Website (`website/`): alle 13 indexierbaren Hauptseiten, `ratgeber/index.php`, 31 Ratgeberartikel, `llms.txt`, `robots.txt`, Sitemaps, Schema. Titel, Meta, Überschriften, Kurzantworten und interne Links wurden ausgelesen.
2. Suchvolumen gebündelt über **OpenSEO `get_keyword_metrics`** (Google-Ads-Daten Deutschland, Ersatz für den Keyword Planner): 151 Begriffe in einem Aufruf, Cluster „Leistung + Bruchsal“, „Leistung + Karlsruhe / Landkreis / Nachbarorte“, „Leistung ohne Ort“, „in der Nähe“, Ratgeber-Long-Tails.
3. Ideen und Fragen über **Seobility** (`keyword_autocomplete`, `keyword_questions_and_similar_searches` für 10 Seeds).
4. Wettbewerb über **OpenSEO `get_serp_results`** (organisch, mobil, Standort Bruchsal) für 8 Suchbegriffe und **`get_local_serp_results`** (Google Maps) für 3 Abfragen: „hausmeisterservice“ ab Bruchsal-Mitte, „hausmeisterservice“ ab Hambrücken, „gebäudereinigung“ ab Bruchsal-Mitte.
5. Onpage-Stichprobe über **Seobility `seo_check`** (Startseite) und **`keyword_check`** (hausmeisterservice.html), Ranking-Stichprobe über `ranking_check`.
6. Prüfkriterien von Ahrefs Site Audit, rankingCoach (lokale To-dos) und Seobility-Onpage als Checkliste angewendet (Ergebnisse in `technik-und-schema.md`).

### Credits

| Tool | Stand vorher | Stand nachher | verbraucht | Budget |
|---|---|---|---|---|
| Seobility | 3.018 | siehe Abschlussbericht (ca. 2.740) | ca. 280 | 1.500 |
| OpenSEO | 227 | 156 | 71 | 150 |

Teuerste Einzelaufrufe: Seobility `seo_check` 100 Credits, OpenSEO `get_keyword_metrics` (151 Keywords) 25 Credits, OpenSEO organische SERP ca. 5 Credits je Keyword, Maps-SERP ca. 3 Credits.

### Was die Tools nicht geliefert haben (ehrlich dokumentiert)

* Für viele lokale Kombinationen liefert Google Ads **kein Volumen** (Wert fehlt = unter der Meldeschwelle, praktisch 0 bis 10 im Monat). Betroffen u. a.: winterdienst bruchsal, treppenhausreinigung bruchsal, büroreinigung bruchsal, praxisreinigung bruchsal, gebäudemanagement bruchsal, objektbetreuung bruchsal, facility management bruchsal, gebäudeservice bruchsal, hausmeisterservice landkreis karlsruhe, alle „hausmeisterservice + Ortsteil/Nachbarort“ außer Bretten, gartenservice bruchsal, heckenschnitt bruchsal, kellerentrümpelung bruchsal, schneeräumdienst bruchsal, zylinder tauschen bruchsal, schließanlage bruchsal, montageservice bruchsal, hausmeister jobs bruchsal. Das heißt nicht „niemand sucht das“, sondern: zu wenig für eine Ausweisung. Diese Begriffe werden trotzdem bedient, weil die Kaufabsicht hoch ist.
* `glasreinigung bruchsal`, `leerstandskontrolle`, `wohnungsauflösung bruchsal`: Volumen „null“ zurückgegeben.
* Seobility `keyword_competition` für wohlverde.de und hausmeisterservice-bruchsal.de: keine Daten (Domains zu klein für den Index).
* Seobility `keyword_similar_top_ten` lieferte überwiegend verschlüsselte Google-Weiterleitungen, deshalb wurden die SERPs über OpenSEO abgefragt.
* Seobility-Fragen: Das Werkzeug liefert Fragen meist ohne Volumen (0). Sie werden nur als Formulierungshilfe für FAQ genutzt.
* Eine organische SERP („treppenhausreinigung bruchsal“) schlug im ersten Lauf mit Providerfehler fehl und wurde mit Tiefe 10 wiederholt.

## 2. Suchbegriffe mit Volumen, Wettbewerb und Intention

Volumen = Ø Suchen/Monat Deutschland (Google Ads). Bei Begriffen mit Ort entspricht das praktisch dem lokalen Volumen. KD = Keyword Difficulty (0 bis 100, DataForSEO). Wettbewerb = Google-Ads-Wettbewerb (bezahlte Anzeigen, nicht organisch). CPC in Euro als Indikator für den Geldwert eines Klicks.

### 2.1 Lokal: Bruchsal

| Suchbegriff | Volumen | KD | Ads-Wettbewerb | CPC | Intention | Bewertung |
|---|---|---|---|---|---|---|
| sperrmüll bruchsal | 590 | 0 | niedrig | 1,70 | Info/Behörde | Nutzer suchen den städtischen Sperrmülltermin. Nicht als Ziel, höchstens Erwähnung im Entrümpelungs-Ratgeber. |
| schlüsseldienst bruchsal | 390 | 0 | niedrig | – | Notfall (Türöffnung) | Nicht zielen: Gebäudewerke bietet keine Notöffnung rund um die Uhr an. |
| hausverwaltung bruchsal | 140 | 3 | mittel | 2,03 | navigational | Fremde Dienstleistung, aber Zielgruppe. Nur für Offpage (Kooperationen). |
| entrümpelung bruchsal | 110 | 0 | hoch | 10,76 | transaktional | **Top-Ziel**, höchster CPC im Set. |
| gebäudereinigung bruchsal | 70 | 0 | mittel | 4,29 | kommerziell | **Top-Ziel**. |
| haushaltsauflösung bruchsal | 70 | 0 | mittel | 8,08 | transaktional | **Top-Ziel**, gehört auf Entrümpelungsseite. |
| reinigungskraft bruchsal | 70 | 0 | mittel | 0,59 | gemischt (Job + Privathaushalt) | Karriere-Seite, Nebenkeyword. |
| reinigungsfirma bruchsal | 50 | 0 | hoch | 1,04 | kommerziell | Gebäudereinigung. |
| gartenbau bruchsal | 50 | 0 | niedrig | 1,14 | GaLaBau (Neuanlage) | Nicht zielen, andere Leistung. |
| schlosser bruchsal / schlosserei bruchsal | je 50 | 13 | niedrig | 0,59 | gemischt | Metallarbeiten-Seite. |
| hausmeisterservice bruchsal | 40 | 0 | niedrig | – | kommerziell | **Haupt-Keyword der Hausmeisterseite**, Hauptkategorie im Google-Profil. |
| metallbau bruchsal | 40 | 0 | mittel | 0,58 | navigational | Nebenkeyword Metallarbeiten. |
| gartenpflege bruchsal | 20 | – | mittel | 5,42 | kommerziell | **Ziel**, Gebäudewerke rankt bereits organisch auf Platz 7. |
| gärtner bruchsal | 20 | 51 | mittel | 1,87 | navigational | Nebenkeyword Gartenpflege (Kategorie „Gärtner“ im Profil). |
| handwerker bruchsal | 20 | – | mittel | 1,76 | navigational | Nebenkeyword Kleinreparaturen. |
| fensterputzer bruchsal | 20 | – | hoch | 2,72 | transaktional | Nebenkeyword Gebäudereinigung. |
| hausmeister bruchsal | 10 | – | mittel | 0,38 | navigational | Hausmeisterseite. |
| fensterreinigung bruchsal | 10 | – | hoch | 1,63 | transaktional | Gebäudereinigung. |
| putzfirma bruchsal | 10 | – | hoch | 0,48 | transaktional | Gebäudereinigung. |
| unterhaltsreinigung bruchsal | 10 | – | – | – | kommerziell | Gebäudereinigung / Büroreinigung. |
| winterdienst, treppenhausreinigung, büroreinigung, praxisreinigung, bauendreinigung, objektbetreuung, gebäudemanagement + bruchsal | keine Daten (0 bis 10) | | | | kommerziell | trotzdem Zielbegriffe, hohe Abschlussnähe, sehr wenig Wettbewerb mit passenden Seiten (siehe SERP-Analyse). |

### 2.2 Lokal: Karlsruhe, Landkreis, Nachbarorte

| Suchbegriff | Volumen | KD | Ads-Wettbewerb | CPC | Bewertung |
|---|---|---|---|---|---|
| gebäudereinigung karlsruhe | 1.300 | 0 | mittel | 3,04 | Stadt Karlsruhe ist nicht Kerngebiet (Website sagt: „für Objekte in der Stadt Karlsruhe fragen Sie bitte an“). Nicht als Hauptziel, nur Erwähnung. |
| entrümpelung karlsruhe | 590 | 6 | hoch | 10,20 | dito. |
| haushaltsauflösung karlsruhe | 390 | 0 | mittel | 9,71 | dito. |
| reinigungsfirma karlsruhe | 320 | 10 | mittel | 4,17 | dito. |
| büroreinigung karlsruhe | 260 | 17 | niedrig | 7,69 | dito. |
| hausmeisterservice karlsruhe | 170 | 0 | niedrig | 3,43 | dito. Landkreis-Seite deckt „Landkreis Karlsruhe“ ab. |
| gebäudereinigung bretten | 110 | 0 | niedrig | 0,47 | Bretten steht im Einsatzgebiet. Erwähnung auf Einsatzgebietsseite, keine eigene Ortsseite. |
| entrümpelung bretten | 70 | 0 | mittel | 5,13 | dito. |
| hausmeisterservice bretten | 70 | 0 | niedrig | 1,60 | dito. |
| gartenpflege karlsruhe | 70 | 0 | mittel | 1,63 | |
| winterdienst karlsruhe | 50 | 0 | mittel | 3,64 | |
| treppenhausreinigung karlsruhe | 30 | 0 | mittel | 2,53 | |
| bauendreinigung karlsruhe | 20 | – | mittel | 4,49 | |
| entrümpelung waghäusel | 20 | – | mittel | 5,59 | Waghäusel liegt direkt bei Hambrücken. Einsatzgebietsseite. |
| gartenpflege bretten, winterdienst bretten | je 20 | 0 | | | |
| gebäudereinigung waghäusel, gebäudereinigung östringen | je 10 | – | | | Östringen ist Referenzort (Reinigung bereits ausgeführt). |
| hausmeisterservice + hambrücken/waghäusel/philippsburg/bad schönborn/östringen/ubstadt-weiher/graben-neudorf/stutensee/heidelsheim/untergrombach, hausmeister forst/karlsdorf-neuthard/kronau | keine Daten | | | | Ergebnis: Ortsseiten lohnen nicht (keine Nachfrage messbar, Doorway-Risiko). Eine gebündelte Einsatzgebietsseite reicht. |

### 2.3 Ohne Ort (bundesweit, mit lokaler Ausspielung)

Diese Begriffe werden bei Google mit Local Pack bzw. „in der Nähe“-Logik ausgespielt. Wer in Bruchsal „Hausmeisterservice“ sucht, bekommt lokale Treffer. Deshalb sind sie die eigentlichen Volumenträger, auch wenn der Bruchsaler Anteil nur ein Bruchteil ist.

| Suchbegriff | Volumen | KD | Intention | Zielseite |
|---|---|---|---|---|
| hausmeisterservice | 14.800 | 4 | kommerziell | hausmeisterservice.html (+ Google-Profil) |
| haushaltsauflösung | 8.100 | – | gemischt | entruempelung.html |
| entrümpelung in der nähe | 4.400 | 16 | lokal | entruempelung.html / Profil |
| entrümpelung kosten | 3.600 | 0 | Info/kommerziell | entruempelung.html (Kostenabschnitt) + Ratgeber Ablauf |
| gebäudereinigung in der nähe | 3.600 | 0 | lokal | gebaeudereinigung.html / Profil |
| hausmeisterservice in der nähe | 2.900 | 0 | lokal | Profil + hausmeisterservice.html |
| hausmeisterservice in meiner nähe | 1.300 | – | lokal | dito |
| gartenpflege in der nähe | 2.900 | 0 | lokal | gartenpflege.html / Profil |
| treppenhausreinigung | 2.900 | 0 | kommerziell | **neue Seite treppenhausreinigung.html** |
| glasreinigung | 2.400 | 0 | kommerziell | gebaeudereinigung.html, Ratgeber Glas |
| winterdienst in der nähe | 1.300 | 0 | lokal | winterdienst.html / Profil |
| winterdienst kosten | 1.300 | 0 | kommerziell | winterdienst.html + preise.html#winterdienst |
| treppenhausreinigung kosten | 590 | 0 | Info/kommerziell | treppenhausreinigung.html |
| garten und hausmeisterservice | 480 | – | kommerziell | Startseite / gartenpflege.html |
| hausmeisterservice preisliste pdf | 590 | – | kommerziell | preise.html |
| kosten für hausmeisterservice / hausmeisterservice kosten / kosten hausmeisterservice | 390 / 320 / 320 | 0 | kommerziell | Ratgeber kosten-hausmeisterservice (Info) + preise.html (Liste) |
| hausmeisterservice preise / preise für hausmeisterservice | je 260 | 0 | kommerziell | preise.html |
| hausmeisterservice stundenlohn | 390 | – | Info | Ratgeber Kosten (nur wenn ein Stundensatz veröffentlicht wird; aktuell steht keiner auf der Seite, daher nicht bedienen) |
| hausmeisterservice gartenpflege / gartenpflege hausmeisterservice | je 260 | – | kommerziell | gartenpflege.html (Kombi-Abschnitt) |
| hausmeisterservice gartenpflege preise | 170 | – | kommerziell | preise.html#gruenpflege |
| hausmeisterservice winterdienst preise | 140 | – | kommerziell | preise.html#winterdienst |
| was kostet ein hausmeisterservice | 140 | 0 | kommerziell | Ratgeber kosten-hausmeisterservice |
| hausmeister kosten pro monat | 90 | 0 | kommerziell | Ratgeber kosten-hausmeisterservice |
| hausmeisterservice kosten 6 familienhaus | 70 | – | kommerziell | Ratgeber + preise (bis 6 Einheiten ab 130 € netto) |
| tiefgaragenreinigung | 170 | 0 | kommerziell (CPC 13,46) | Ratgeber Tiefgarage + gebaeudereinigung.html |
| tiefgarage reinigen | 90 | 0 | kommerziell | Ratgeber Tiefgarage |
| kellerreinigung | 70 | 0 | kommerziell | gebaeudereinigung.html |
| mülltonnenservice | 110 | 0 | kommerziell | Ratgeber Mülltonnendienst + preise.html#muelltonnen |
| mülltonnen rausstellen service | 30 | – | kommerziell | dito |
| büroreinigung kosten | 40 | 0 | Info | neue Seite bueroreinigung.html |
| hausmeister und gartenservice | 110 | 0 | kommerziell | Startseite |
| wohnungsübergabe service | 20 | – | kommerziell | wohnungsuebergabe.html |
| hausmeister kleinreparaturen | 10 | – | kommerziell | kleinreparaturen.html |

### 2.4 Ratgeber-Long-Tails (informational, bundesweit)

| Suchbegriff | Volumen | KD | Ratgeberartikel |
|---|---|---|---|
| wohnungsübergabe protokoll / wohnungsübergabeprotokoll | 12.100 | 1 | wohnungsuebergabe-protokoll-bruchsal |
| übergabeprotokoll wohnung | 9.900 | 0 | dito |
| wohnungsübergabeprotokoll vorlage | 2.900 | – | dito (nur wenn Checkliste ergänzt wird) |
| wohnungsübergabe auszug / nach mietende | 720 / 170 | – | dito |
| wann darf man hecke schneiden | 8.100 | 20 | hecke-schneiden-erlaubt |
| hecke schneiden erlaubt | 3.600 | 14 | dito |
| zählerstände ablesen | 4.400 | 0 | zaehlerstaende-ablesen-jahreswechsel |
| räum und streupflicht | 1.600 | 15 | raeum-und-streupflicht-bruchsal |
| sturmschaden | 720 | 0 | sturmschaden-kontrolle-gebaeude (realistisch: nur Long-Tail „nach Sturm Gebäude kontrollieren“) |
| schlüsselverwaltung | 210 | 0 | schluesselverwaltung-bruchsal |
| schuhregal treppenhaus | 210 | 0 | treppenhaus-rettungsweg (Intention ist teils Produktkauf, der Rechtsanteil ist aber sicher dabei) |
| hausmeisterkosten umlagefähig | 170 | 0 | hausmeisterkosten-umlagefaehig |
| unkraut pflaster entfernen | 50 | 0 | unkraut-pflaster-entfernen-bruchsal |
| streugut entfernen | 30 | – | streugut-entfernen-fruehjahr |
| hausmeister kündigen | 10 | – | dienstleister-wechseln-hausmeister |

Fragen aus Seobility (ohne Volumen, als FAQ-Sprache genutzt): „was kostet eine treppenhausreinigung für ein mehrfamilienhaus“, „wie viel kann man für eine treppenhausreinigung verlangen“, „was gehört zur treppenhausreinigung durch mieter“, „was verlangt eine gebäudereinigung“, „wie viel kostet die schneeräumung“, „kann ich den winterdienst von der steuer absetzen“, „ist streusalz auf dem eigenen grundstück erlaubt“, „was verlangt eine entrümpelungsfirma pro stunde“, „ist die entrümpelung einer wohnung eine haushaltsnahe dienstleistung“, „wer muss die wohnung eines verstorbenen ausräumen“ (20), „wie laufen haushaltsauflösungen ab“, „was kostet ein hausmeister pro jahr“, „was verlangt man für gartenarbeit“.

## 3. Cluster und Auswahl

| Cluster | Kernbegriff | Begründung der Auswahl |
|---|---|---|
| A Hausmeisterservice | hausmeisterservice bruchsal | Hauptkategorie im Google-Profil, 14.800 bundesweit mit lokaler Ausspielung, KD 4. Lokal kleine, aber kaufbereite Nachfrage. |
| B Gebäudereinigung | gebäudereinigung bruchsal | 70/Monat, CPC 4,29, Reinigungsdienst ist Zusatzkategorie, zwei Bewertungen loben ausdrücklich die Gebäudereinigung. |
| C Treppenhausreinigung | treppenhausreinigung (bruchsal) | 2.900 + 590 („kosten“) bundesweit, Kernleistung für WEG und Hausverwaltung, bisher ohne eigene Seite. |
| D Entrümpelung / Haushaltsauflösung | entrümpelung bruchsal, haushaltsauflösung bruchsal | Höchste CPCs (8 bis 11 €), klare Transaktionsabsicht, Kategorie im Profil. |
| E Winterdienst | winterdienst bruchsal | Saisonal (Nachfrage Oktober bis Januar, jetzt aktuell), Kategorie „Schneeräumdienst“ im Profil, Saisonpreise sind veröffentlicht. |
| F Gartenpflege | gartenpflege bruchsal | Bereits Platz 7 organisch, Kategorie „Gärtner“. |
| G Preise | hausmeisterservice preise / kosten | ca. 2.000 Suchen/Monat bundesweit im Cluster, eigene Preisliste ist ein Alleinstellungsmerkmal in Bruchsal (kein Wettbewerber in den SERPs nennt Preise). |
| H Wohnungsübergabe | wohnungsübergabe bruchsal + übergabeprotokoll | Service lokal klein, Ratgeber-Thema riesig (über 20.000 Suchen/Monat, KD 0 bis 1). |
| I Handwerker / Metall | kleinreparaturen bruchsal, schlosser bruchsal | klein, aber passend und wenig Wettbewerb. |
| J Einsatzgebiet | landkreis karlsruhe + Orte | Kein messbares Volumen je Ort, aber wichtig für KI-Antworten („Welcher Hausmeisterservice arbeitet in Ubstadt-Weiher?“) und für das Gebiets-Profil. |

## 4. Wettbewerber in den Suchergebnissen

### 4.1 Organisch (mobil, Standort Bruchsal, 31.10.2026)

**„hausmeisterservice bruchsal“** (Local Pack + organisch)
* Local Pack: P.S. Hausmeisterservice Bruchsal, Hausmeisterservice Hasan Karakus, KALMAN Dienstleistungen, DK Dienstleistungen & Objektbetreuung.
* Organisch: 1 P.S. Hausmeisterservice (hausmeisterservice-bruchsal.de, Exact-Match-Domain), 2 HMS Hausmeisterservice, 3 Impressum von P.S., 4 haendel3g.de, 5 wohlverde.de/hausmeister-service, 6 Verzeichnis „Top 10 Hausmeister in Bruchsal“, 7 chisto-reinigungsfirma.de, danach Branchenbücher.
* Gebäudewerke: nicht unter den Top 20.

**„gebäudereinigung bruchsal“**
* Local Pack: Bruchsaler Gebäudereinigung, KLARESICHT, SHEMA, CHISTO.
* Organisch: MGR Gebäudereinigung, CHISTO, Gelbe Seiten, WOHLverde, kleinanzeigen, 11880, Engelssauber (wirbt im Snippet mit „5,0 bei 72 Bewertungen“), gebaeudereinigung-clean24.de/standort/bruchsal (überregionale Ortsseite).
* Gebäudewerke: nicht unter den Top 20.

**„entrümpelung bruchsal“**
* Local Pack: EntrümpelX, Freddys Entrümpelungen, Neuberth, FLEX Dienstleistungen.
* Organisch: WohnKomfort, Ortsseiten von Vermittlern („ab 500 €“), EntrümpelX (eigener Ratgeber „Haushaltsauflösung Bruchsal“ auf Platz 10/11), Gelbe Seiten, R&D Recycling.
* Gebäudewerke: nicht unter den Top 20.

**„winterdienst bruchsal“**
* AI Overview vorhanden. Local Pack: P.S. Hausmeisterservice, Eckert Landschaftspflege, CT-Dienstleistungen, Eckert Dienstleistungen.
* Organisch: Hausmeisterservice-Seiten, Verzeichnisse, MASEG (Sinsheim), WOHLverde, Jung Gebäudedienste (Karlsruhe).
* **Gebäudewerke: Platz 8 organisch, aber mit der Ratgeber-Übersicht** („Ratgeber Hausmeisterservice Bruchsal“), nicht mit winterdienst.html. Signal: Die Ratgeber-Übersicht hat stärkere Signale für „Winterdienst Bruchsal“ als die Leistungsseite. Interne Verlinkung mit Ankertext „Winterdienst in Bruchsal“ auf winterdienst.html stärken, Ratgeber-Übersicht nicht auf „Winterdienst Bruchsal“ optimieren.

**„gartenpflege bruchsal“**
* Local Pack: Gartenservice Heta, Gartenpflege Schwall, WOHLverde, Eckert.
* Organisch: überwiegend GaLaBau und Verzeichnisse (Houzz, Trustlocal).
* **Gebäudewerke: Platz 7 organisch mit gartenpflege.html.** Bestes vorhandenes Ranking.

**„treppenhausreinigung bruchsal“**: Local-Services-Anzeigen, AI Overview, Local Pack (Bruchsaler Gebäudereinigung, KLARESICHT, CHISTO, Händel GGG), erstes organisches Ergebnis ist ein Verzeichnis. **Keine einzige echte Treppenhausreinigungs-Seite eines Bruchsaler Anbieters in den Top 10.** Größte Lücke im Set.

**„büroreinigung bruchsal“**: AI Overview, Local Pack (CHISTO, KLARESICHT, Bruchsaler Gebäudereinigung, P.S.), organisch KLARESICHT, Gondelsheimer Gebäudeservice, Jobseite, Verzeichnis. Auch hier keine spezifische Büroreinigungs-Landingpage mit Preisen.

**„hausmeisterservice landkreis karlsruhe“**: Local Pack P.S., Karakus, BLD (Karlsdorf-Neuthard), Reiter (Weingarten). Organisch Karlsruher Anbieter, Gelbe Seiten, WOHLverde. Keine Seite, die das Landkreisgebiet sauber erklärt.

### 4.2 Google Maps (Local Finder)

| Abfrage | Top 5 | Gebäudewerke |
|---|---|---|
| hausmeisterservice, Bruchsal-Mitte (Zoom 12) | Bruchsaler Gebäudereinigung (5,0/10), CT-Dienstleistungen (5,0/3), A.S. Gebäudedienstleistungen (ohne Bewertung), KALMAN (4,4/7), DK Dienstleistungen (5,0/18) | nicht unter 20 |
| hausmeisterservice, Hambrücken (Zoom 13) | BS Dienstleistungen Hambrücken (5,0/19), Hausmeister Läpple (Hambrücken, nicht beansprucht), NAD Waghäusel (4,9/16), STRATX Hambrücken (5,0/10), EN-Service Karlsdorf-Neuthard | nicht unter 12 |
| gebäudereinigung, Bruchsal-Mitte | Bruchsaler Gebäudereinigung, SHEMA, KLARESICHT (4,9/26), CHISTO (4,9/25), KALMAN | nicht unter 20 |

Weitere starke Profile im Umkreis: Michel-Service-Solution, Ubstadt-Weiher (4,9 bei 137 Bewertungen, 277 Fotos), P.S. Hausmeisterservice Bruchsal (5,0 bei 75, Gebiets-Unternehmen wie Gebäudewerke), WOHLverde Forst (4,9/63), Haus- und Gartenservice Gutjahr Gondelsheim (5,0/32, 45 Fotos), Objektservice 4 You Ubstadt-Weiher (5,0/31, 67 Fotos, 9 Kategorien).

**Einordnung:** Das Profil ist neu (7 Bewertungen, 5 Fotos, Gebiets-Unternehmen mit ausgeblendeter Adresse). Für Gebiets-Unternehmen zählt bei Maps die Nähe zur hinterlegten (verborgenen) Adresse in Hambrücken. In Bruchsal-Mitte stehen ein Dutzend Betriebe mit Bruchsaler Adresse davor. Organisch ist der Weg nach Bruchsal deshalb schneller als über Maps. Für Maps entscheiden jetzt Bewertungsanzahl, Fotos, Aktivität und Kategorien (siehe `offpage-und-gbp.md`).

### 4.3 Was die Wettbewerber besser und schlechter machen

Besser als Gebäudewerke:
* **Bewertungsmenge:** P.S. 75, Michel 137, WOHLverde 63, Gutjahr 32. Gebäudewerke 7.
* **Fotos im Profil:** Michel 277, Objektservice 4 You 67, Gutjahr 45. Gebäudewerke 5.
* **Alter und Links:** P.S. nennt „8 Jahre am Markt“, hat eine Exact-Match-Domain und Branchenbucheinträge. Gebäudewerke hat laut Seobility 0 Backlinks.
* **Adresse in Bruchsal:** Viele Wettbewerber haben eine sichtbare Bruchsaler Adresse, das zählt bei Maps stark.
* **Bewertungssterne im Snippet:** Engelssauber zeigt „5,0 bei 72 Bewertungen“ im Snippet-Text.
* **Lokale Ratgeber:** EntrümpelX rankt mit einem Ratgeber „Haushaltsauflösung Bruchsal“.

Schlechter als Gebäudewerke (Chancen):
* Kaum ein Wettbewerber veröffentlicht **Preise**. Gebäudewerke hat eine vollständige Richtpreisliste (netto/brutto). Das ist für KI-Antworten („Was kostet ein Hausmeisterservice in Bruchsal?“) der stärkste Hebel.
* Keine Bruchsaler **Treppenhausreinigungs-** und **Büroreinigungsseite** mit Leistungsumfang und Preisen.
* Wenig Inhalte für **Hausverwaltung/WEG** (Umlagefähigkeit, Protokoll, Leistungsverzeichnis). Gebäudewerke deckt das mit 31 Fachartikeln ab.
* Viele Seiten sind dünn (Leistungslisten mit Häkchen) oder Vermittler-Ortsseiten ohne echte Ortskenntnis.
* Kaum strukturierte Daten, keine `llms.txt`.

## 5. Kernaussagen

1. Lokale Volumen sind klein. Entscheidend ist, die wenigen kaufbereiten Suchen in Bruchsal zu bekommen und über die bundesweiten Begriffe ohne Ort (Local Pack) sichtbar zu werden. Dafür zählen Google-Profil und Bewertungen mehr als jeder Text.
2. Organisch ist die Website bereits relevant (Gartenpflege Platz 7, Ratgeber-Übersicht Platz 8 für Winterdienst), nach erst einem Monat. Die Seitenstruktur stimmt. Gebraucht werden Feinschliff, eine klarere Zuordnung (keine zwei Seiten pro Begriff) und Links von außen.
3. Treppenhausreinigung ist die größte inhaltliche Lücke, sowohl auf der Website als auch bei den Wettbewerbern.
4. Die Ratgeber-Themen Übergabeprotokoll (über 20.000/Monat), Hecke schneiden (11.700), Zählerstände (4.400) und Räum- und Streupflicht (1.600) bringen bundesweite Reichweite und Autorität. Konversion kommt daraus kaum, aber Sichtbarkeit in KI-Antworten und Vertrauen.
