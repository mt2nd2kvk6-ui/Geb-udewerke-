# Textänderungen je Seite

Stand 31.10.2026. „Vorher“ bezieht sich auf den Commit `2fa69c5` (Ausgangsstand). Der Design-Agent baut parallel um. Maßgeblich ist der Wortlaut, nicht das HTML-Element. Preise und Fakten bleiben unverändert. Alles, was hier neu steht, ist aus Angaben abgeleitet, die bereits auf der Website oder in `projekt/google-profil.json` stehen.

## 0. Schreibregeln für alle Texte

* Ort: **Bruchsal** steht vorne. Hambrücken nur in Anschrift, Impressum, Kontakt/Anfahrt, Footer-Adresse und Schema-Adresse.
* Nicht „aus Bruchsal“ schreiben, wenn der Firmensitz gemeint ist (Hambrücken ist eine eigene Gemeinde). Richtig: „in Bruchsal“, „für Bruchsal und Umgebung“, „Ihr Hausmeisterservice in Bruchsal“. So bleibt jede Aussage wahr.
* Keine Gedankenstriche (– oder —). Keine Floskeln („Ihr zuverlässiger Partner“, „maßgeschneidert“, „rundum sorglos“, „ganzheitlich“, „nahtlos“). Kein „Egal ob … oder …“, kein „nicht nur … sondern auch“. Keine rhetorischen Fragen als Einstieg, kein „Sprechen Sie uns gerne an!“ unter jedem Abschnitt.
* Überschriften nicht durchgehend im Muster „X: Y“.
* Konkrete Details statt Adjektive: Turnus, Uhrzeiten, Preise, Ortsteile, Paragrafen.
* Keyword-Sätze, die nur für Suchmaschinen geschrieben wurden („X in Bruchsal heißt: …“), werden gestrichen. Sie wiederholen den Absatz davor und klingen nach Maschine.
* Kurzantworten für KI-Systeme: 40 bis 60 Wörter, erster Satz beantwortet die Frage vollständig, mit Ort und Zahl, ohne Verweis auf „oben“ oder „unten“.

---

## 1. Seitenübergreifend

### 1.1 Einheitliche Schreibweise (Name, Adresse, Telefon)

| Element | Einheitlich | bisher gefunden |
|---|---|---|
| Name im Fließtext | Gebäudewerke | gleich |
| Rechtlicher Name (Impressum, Footer-Copyright, Schema legalName) | Gebäudewerke GbR | gleich |
| Name im Google-Profil | Gebäudewerke - Hausmeisterservice & Gebäudereinigung | Website nennt das nirgends. Im Schema als `alternateName` ergänzen, auf der Website nicht als Firmenname schreiben. |
| Telefon sichtbar | 0163 7221790 | „01637221790“ (Kopfleiste, Impressum), „0163 7221790“, „+49 163 7221790“ (Footer) |
| Telefon im Link | `tel:+491637221790` | gleich |
| E-Mail | info@gebaeudewerke.de | gleich |
| Anschrift | Allmend 2, 76707 Hambrücken | gleich |
| Bürozeiten | Mo bis Fr 7 bis 17 Uhr | teils „07:00 bis 17:00 Uhr“; beides ok, aber je Bauteil gleich |
| Notdienst | täglich 17 bis 24 Uhr | gleich |

### 1.2 Kopfleiste

Vorher: `Notdienst täglich 17 bis 24 Uhr: 01637221790 · Allmend 2, 76707 Hambrücken · Mo bis Fr 07:00 bis 17:00 Uhr`

Nachher: `Notdienst täglich 17 bis 24 Uhr: 0163 7221790 · Mo bis Fr 7 bis 17 Uhr · Hausmeisterservice in Bruchsal und im Landkreis Karlsruhe`

(Adresse wandert in Footer und Kontakt. Sie bleibt dort vollständig.)

### 1.3 Footer

Vorher (Spaltenkopf über Adresse): keiner. Footer-Teaser auf Impressum: „Ein Ansprechpartner für Ihr Objekt in Bruchsal“ (gut, beibehalten).

Nachher, neuer Kurztext unter dem Logo (vor der Adresse):
> Hausmeisterservice, Gebäudereinigung, Gartenpflege und Winterdienst für Wohnanlagen, Eigentümergemeinschaften und Gewerbe in Bruchsal und im Landkreis Karlsruhe.

Darunter unverändert: Gebäudewerke GbR, Allmend 2, 76707 Hambrücken, Telefon 0163 7221790, E-Mail.

Footer-Spalte „Erreichbarkeit“, Eintrag `Einsatzgebiet: Bruchsal und Landkreis Karlsruhe` wird ein Link auf `/einsatzgebiet.html`.

### 1.4 Vertrauensleiste (neu, unter jeder Hero-Einleitung der Leistungsseiten und auf der Startseite)

Sechs kurze Punkte, jeweils wahr und auf der Seite belegt:
* Eigenes Personal, keine Subunternehmer
* Fester Ansprechpartner für Ihr Objekt
* Schriftlicher Festpreis nach kostenlosem Ortstermin
* Protokoll mit Datum, Uhrzeit und Fotos zu jedem Einsatz
* Betriebshaftpflicht bis 5 Mio. Euro
* 5,0 Sterne bei 7 Google-Bewertungen (Zahl aus google-profil.json, bei neuen Bewertungen anpassen)

### 1.5 Bewertungsblock „Kundenstimmen auf Google“

Der Design-Agent hat den Block bereits eingebaut. Text-Vorgaben:
* Überschrift: `Kundenstimmen auf Google`
* Unterzeile: `5,0 von 5 bei 7 Bewertungen auf Google. Stand: 31.10.2026.`
* Zitate wörtlich, mit Vorname und Initial bzw. so wie auf Google angezeigt, mit Datum. Keine Kürzung, die den Sinn verändert. Die Bewertung „Türhelden Schlüsseldienst“ ist ein Firmenkonto. Sie darf gezeigt werden, auf Startseite und Gebäudereinigung aber nicht als erste, weil ein Schlüsseldienst als Rezensent bei Besuchern Fragen aufwirft.
* Zuordnung nach Thema: Daniela Azevedo und Türhelden (Gebäudereinigung) auf gebaeudereinigung.html und treppenhausreinigung.html; Leon Göler (Schlösser) auf metallarbeiten-schloesser.html; Luca Fritscher, I. Bendi, Stefanie Fl auf Startseite und hausmeisterservice.html. Ayse G hat keinen Text und erscheint nur in der Anzahl.
* Links: „Alle Bewertungen auf Google“ → https://share.google/dHbp6caGIhLZVhp4Y, „Bewertung schreiben“ → Link aus google-profil.json.

### 1.6 Gestrichene Keyword-Sätze (alle Leistungsseiten)

Diese Absätze wiederholen den Absatz davor und werden **ersatzlos gestrichen**:

| Seite | zu streichender Absatz (vorher) |
|---|---|
| entruempelung.html | „Entrümpelung, Haushaltsauflösung und Transport in Bruchsal bieten wir aus einer Hand an. Bei einer Haushaltsauflösung in Bruchsal besichtigen wir das Objekt, nennen einen Festpreis und übergeben die Räume besenrein, wenn wir fertig sind.“ |
| gartenpflege.html | „Gartenpflege und Außenanlagen in Bruchsal übernehmen wir im Jahresvertrag von März bis November. Rasen, Hecken, Beete, Laub und Hofflächen werden nach einem festen Plan gepflegt, die Jahrespauschale wird in zwölf Raten abgerechnet.“ (die zwölf Raten stehen weiter unten bereits) |
| gebaeudereinigung.html | „Gebäudereinigung und Treppenhausreinigung in Bruchsal richten sich nach einem schriftlichen Reinigungsplan. Mittel und Geräte sind im Preis enthalten, Sonderreinigungen rechnen wir als Festpreis ab.“ |
| kleinreparaturen.html | „Kleinreparaturen, Montage und Renovierung in Bruchsal erledigen wir in einem Termin, damit Sie nicht fünf Handwerker nacheinander bestellen müssen. Handwerkerservice Bruchsal heißt bei uns: eine Liste, ein Ansprechpartner, ein Protokoll.“ |
| metallarbeiten-schloesser.html | „Metallarbeiten, Türen, Tore und Schlösser in Bruchsal klären wir in der Regel in einem Termin. Zäune, Tore und Geländer reparieren wir, Zylinder tauschen wir, und Schließanlagen gehören ebenfalls zum Leistungsumfang.“ |
| winterdienst.html | „Winterdienst in Bruchsal mit Einsatzprotokoll heißt: Wir räumen und streuen Wohnanlagen, Gewerbe und Parkplätze von November bis März. Jeder Einsatz wird protokolliert, damit sich im Schadensfall nachvollziehen lässt, was wann erledigt wurde.“ |
| wohnungsuebergabe.html | „Wohnungsübergabe und Immobilienservice in Bruchsal umfasst Abnahmen, Leerstandskontrollen und Fotoprotokolle. Wohnungsübergabe Bruchsal mit Fotoprotokoll bedeutet: Zustand, Zählerstände und Mängel sind am selben Tag dokumentiert.“ |
| kontakt.html | „Kontakt zu Gebäudewerke in Bruchsal nehmen Sie am schnellsten über das Formular, per Telefon oder über WhatsApp auf. …“ (zweiter Absatz unter „So erreichen Sie uns“; wiederholt die Einleitung, Ersatz siehe 13.) |
| ratgeber/muelltonnendienst-bruchsal.html | „Mülltonnendienst in Bruchsal heißt: Tonnen am Abfuhrtag bereitstellen, danach zurückstellen und den Standplatz sauber halten.“ |
| ratgeber/treppenhausreinigung-bruchsal.html | „Treppenhausreinigung nach festem Plan heißt: feste Aufgaben in festen Abständen, schriftlich festgehalten. …“ |
| ratgeber/winterdienst-beauftragen-bruchsal.html | „Winterdienst in Bruchsal rechtzeitig beauftragen heißt: den Saisonvertrag vor Beginn der Saison abschließen, …“ |

---

## 2. Startseite (index.html)

### 2.1 Einleitung unter der H1

Vorher:
> Gebäudemanagement in Bruchsal aus einer Hand: Hausmeister, Reinigung und Außenanlagen für Ihr Objekt in Bruchsal und im Landkreis Karlsruhe. Dazu Kontrollgänge, Winterdienst und die Reparaturen, die dabei anfallen. Mit festen Terminen, einem Ansprechpartner und einem Protokoll, das zeigt, wann jemand da war.

Nachher (Kurzantwort, 52 Wörter):
> Gebäudewerke betreut Mehrfamilienhäuser, Eigentümergemeinschaften und Gewerbeobjekte in Bruchsal und im Landkreis Karlsruhe. Hausmeisterservice, Treppenhaus- und Gebäudereinigung, Gartenpflege und Winterdienst laufen über einen Vertrag und einen Ansprechpartner. Wir arbeiten mit eigenem Personal, schreiben zu jedem Einsatz ein Protokoll und nennen den Preis nach einem kostenlosen Ortstermin schriftlich.

### 2.2 Hero-Faktenliste

Vorher: `Sitz bei Bruchsal / Allmend 2, Hambrücken`
Nachher: `Im Einsatz in Bruchsal / mit allen Stadtteilen und im Landkreis Karlsruhe`

(Die übrigen drei Punkte bleiben.)

### 2.3 H2 „Für wen wir arbeiten“ → „Für Hausverwaltungen, Eigentümer und Gewerbe“

Text bleibt.

### 2.4 H2 „Gebäudewerke auf einen Blick“, erster Absatz

Vorher:
> Gebäudewerke ist ein Objekt- und Gebäudeservice mit Sitz in Hambrücken bei Bruchsal. Wir betreuen Mehrfamilienhäuser, …

Nachher:
> Gebäudewerke ist ein Objekt- und Gebäudeservice für Bruchsal und den Landkreis Karlsruhe. Wir betreuen Mehrfamilienhäuser, Eigentümergemeinschaften und Gewerbeimmobilien und übernehmen Hausmeisterservice, Gebäudereinigung, Gartenpflege, Winterdienst, Wohnungsübergaben, Entrümpelung, Kleinreparaturen sowie Metallarbeiten und Schließanlagen.

Fakten-Tabelle: Zeile `Sitz` bleibt mit voller Anschrift (Fakt), Zeile `Einsatzgebiet` bekommt einen Link „alle Orte“ auf /einsatzgebiet.html. Neue Zeile: `Google-Bewertungen | 5,0 von 5 bei 7 Bewertungen` (bei neuen Bewertungen anpassen).

### 2.5 H2 „Bruchsal und der Landkreis Karlsruhe“ → „Im Einsatz in Bruchsal und im Landkreis Karlsruhe“

Vorher, erster Absatz:
> Unser Betrieb sitzt in der Allmend 2 in Hambrücken, nordwestlich von Bruchsal. Wir betreuen Objekte in der Bruchsaler Kernstadt und in den Stadtteilen Büchenau, Heidelsheim, Helmsheim, Obergrombach und Untergrombach sowie im übrigen Landkreis Karlsruhe. Reinigungsaufträge haben wir unter anderem bereits in Bruchsal, Bad Schönborn und Östringen ausgeführt.

Nachher:
> Wir betreuen Objekte in der Bruchsaler Kernstadt und in allen Stadtteilen: Büchenau, Heidelsheim, Helmsheim, Obergrombach und Untergrombach. Dazu kommen die Gemeinden im Landkreis Karlsruhe rund um Bruchsal. Reinigungsaufträge haben wir unter anderem in Bruchsal, Bad Schönborn und Östringen ausgeführt. Unser Betrieb liegt in Hambrücken, wenige Kilometer nordwestlich der Bruchsaler Kernstadt.

Ortsliste: Die Liste auf der Startseite und in allen FAQ-Antworten „In welchen Orten …“ einheitlich so führen (bisher fehlen je nach Seite Kronau, Waghäusel, Philippsburg, Graben-Neudorf):
Bruchsal Kernstadt, Büchenau, Heidelsheim, Helmsheim, Obergrombach, Untergrombach, Forst, Karlsdorf-Neuthard, Ubstadt-Weiher, Bad Schönborn, Östringen, Kronau, Hambrücken, Waghäusel, Philippsburg, Graben-Neudorf, Stutensee, Bretten.

Absatz nach der Liste, vorher: „Kurze Wege sind beim Winterdienst keine Bequemlichkeit, sondern Voraussetzung. Deshalb bündeln wir …“ Nachher: „Beim Winterdienst entscheiden kurze Wege. Deshalb bündeln wir …“ (Rest gleich).

Nach der Liste neuer Link-Absatz:
> Alle Orte und was dort gilt: <a href="/einsatzgebiet.html">Einsatzgebiet rund um Bruchsal</a>

### 2.6 FAQ Startseite

* Frage „In welchem Gebiet sind Sie im Einsatz?“ → „In welchen Orten rund um Bruchsal sind Sie im Einsatz?“ Antwort: Ortsliste aus 2.5 statt der bisherigen Auswahl, Schluss unverändert.
* Frage „Welcher Anbieter übernimmt Hausmeister, Reinigung, Garten und Winterdienst aus einer Hand?“ → „Wer übernimmt Hausmeister, Reinigung, Garten und Winterdienst in einem Vertrag?“ Antwort bleibt.
* Frage „Ist ein Hausmeisterservice besser als ein einzelner Hausmeister?“ → „Hausmeisterservice oder eigener Hausmeister, was passt besser?“ Antwort bleibt.

---

## 3. Hausmeisterservice (hausmeisterservice.html)

### 3.1 H2 „Ihr Hausmeister für Bruchsal und Umgebung“ → „Ihr Hausmeister in Bruchsal und Umgebung“

Erster Absatz, vorher:
> Gebäudewerke übernimmt als Hausmeisterservice die Aufgaben, für die früher ein Hausmeister im Haus angestellt war: … Wer in Bruchsal einen Hausmeister sucht, bekommt bei uns einen festen Betreuer mit Vertretung im Team. …

Nachher (Kurzantwort, 55 Wörter):
> Unser Hausmeisterservice übernimmt in Bruchsal die Aufgaben, für die früher ein Hausmeister im Haus angestellt war: Kontrollgänge, Kleinreparaturen, Schlüssel, Mülltonnen und der Blick auf die Haustechnik. Sie bekommen einen festen Betreuer, der Ihr Objekt kennt, und eine Vertretung aus dem Team für Urlaub und Krankheit. Gartenpflege und Winterdienst kommen auf Wunsch in denselben Vertrag.

### 3.2 Block „Kurz beantwortet“

Überschriften wie in der Spezifikation. Antworttexte bleiben, mit diesen Änderungen:

* H3 alt „Wer übernimmt im Landkreis Karlsruhe die laufende Betreuung einer Wohnanlage mit Reinigung, Kontrollgängen und kleinen Reparaturen?“ entfällt als eigene Frage. Der Antworttext wird an die Antwort „Welcher Hausmeisterservice passt zu einem Mehrfamilienhaus?“ als zweiter Absatz angehängt, ohne den Satz „Unser Sitz ist in Hambrücken bei Bruchsal“.
* H3 alt „Welcher Anbieter in Bruchsal übernimmt das Gebäudemanagement aus einer Hand?“ → neu „Was gehört zum Gebäudemanagement und was nicht?“
  Vorher erster Satz: „Gebäudewerke deckt das infrastrukturelle Gebäudemanagement ab: …“
  Nachher erster Satz: „Wir übernehmen das infrastrukturelle Gebäudemanagement, also alles, was im Haus und drumherum laufend anfällt: …“ Rest bleibt.
* H3 „In welchen Orten betreuen Sie Objekte?“: Ortsliste aus 2.5 und Link auf /einsatzgebiet.html.

### 3.3 H2 „Preise für den Hausmeisterservice in Bruchsal“ → „Kosten für den Hausmeisterservice in Bruchsal“

Neuer erster Absatz (Kurzantwort, 46 Wörter):
> Bei zwei Terminen pro Woche kostet der Hausmeisterservice in Bruchsal ab 130 € netto im Monat für Häuser bis 6 Wohneinheiten, ab 190 € für 7 bis 20 Einheiten und ab 280 € für größere Anlagen. Den festen Monatspreis bekommen Sie nach dem kostenlosen Ortstermin schriftlich.

Die bisherigen zwei Absätze folgen danach unverändert.

---

## 4. Gebäudereinigung (gebaeudereinigung.html)

### 4.1 H2 „Das Treppenhaus ist der erste Eindruck“ → „Reinigung nach Plan statt nach Zuruf“

Nach dem Streichen (1.6) beginnt der Abschnitt mit diesem neuen Absatz (Kurzantwort, 50 Wörter):
> Wir reinigen Treppenhäuser, Büros, Praxen, Keller, Tiefgaragen und Fenster in Bruchsal nach einem schriftlichen Reinigungsplan. Darin stehen Flächen, Turnus und Verfahren. Das Treppenhaus kommt meist wöchentlich dran, Keller und Tiefgarage monatlich bis quartalsweise, Glas zwei- bis viermal im Jahr. Mittel und Geräte sind im Preis enthalten.

Dann folgen unverändert: „Mieter, Kunden und Interessenten sehen zuerst …“, „Reinigung funktioniert nur mit Plan …“, „Neben der laufenden Reinigung …“.

### 4.2 Kurz beantwortet

* „Welche Gebäudereinigung in Bruchsal eignet sich für Treppenhäuser und Gemeinschaftsflächen?“ → „Welche Reinigungsfirma eignet sich für Treppenhäuser und Gemeinschaftsflächen?“
* „Wer reinigt Treppenhäuser im Mehrfamilienhaus und dokumentiert Mängel gleich mit?“ → „Wer reinigt das Treppenhaus und meldet Mängel gleich mit?“
* „Was kostet eine Treppenhausreinigung pro Monat im kleineren Mehrfamilienhaus?“ → „Was kostet eine Treppenhausreinigung im Monat?“ Antwort am Ende ergänzen: „Mehr dazu auf der Seite <a href="/treppenhausreinigung.html">Treppenhausreinigung in Bruchsal</a>.“ (sobald die Seite live ist)
* „Welche Gebäudereinigung übernimmt auch Keller, Tiefgarage und Glasflächen?“ → „Reinigen Sie auch Keller, Tiefgarage und Fenster?“
* „Reinigungsfirma oder kombinierter Hausmeister- und Reinigungsdienst: was passt besser?“ → „Reinigungsfirma oder Hausmeister mit Reinigung?“
* „Gibt es Fensterreinigung und laufende Objektpflege aus einer Hand?“ → „Was kostet eine Fensterreinigung?“ Antwort: erster Satz tauschen gegen „Ab 235 € netto für bis zu 30 m² Glasfläche einseitig, mit Rahmen und Falz bei normaler Verschmutzung.“ Danach: „Fenster- und Glasreinigung lässt sich mit Treppenhausreinigung und Hausmeisterservice in einem Vertrag kombinieren.“
* „Bieten Sie regelmäßige Unterhaltsreinigung für Wohn- und Gewerbeimmobilien an?“ → „Was kostet eine regelmäßige Büroreinigung?“ Antwort bleibt.
* „In welchen Orten reinigt Gebäudewerke?“ → „In welchen Orten reinigen Sie?“ Ortsliste aus 2.5.

### 4.3 FAQ „Was kostet eine Treppenhausreinigung?“

Vorher: „Der Preis richtet sich nach Etagenzahl, Bodenbelag und Turnus. Nach einer Besichtigung bekommen Sie eine feste Monatspauschale.“
Nachher: „Der Preis richtet sich nach Etagenzahl, Bodenbelag und Turnus. Einen pauschalen Richtpreis nennen wir nicht, weil sich zwei Häuser mit gleicher Wohnungszahl stark unterscheiden. Nach dem kostenlosen Ortstermin bekommen Sie eine feste Monatspauschale, Mittel und Geräte sind enthalten.“

---

## 5. Gartenpflege (gartenpflege.html)

Seite rankt bereits. Nur:
* Streichung aus 1.6.
* H2 „So läuft es ab“ → „So läuft das Gartenjahr ab“.
* Kurz beantwortet: „Wer übernimmt Gartenpflege für Wohnanlagen mit Rasen, Hecken und Laub im Jahresvertrag?“ → „Wer pflegt Rasen, Hecken und Laub einer Wohnanlage im Jahresvertrag?“; „Worauf kommt es bei regelmäßiger Gartenpflege für Mietobjekte im Landkreis Karlsruhe an?“ → „Worauf kommt es bei der Gartenpflege für Mietobjekte an?“; „Gibt es Hausmeisterservice, Gartenpflege und Winterdienst aus einer Hand?“ → „Gibt es Hausmeisterservice, Gartenpflege und Winterdienst zusammen?“; „Übernehmen Sie auch Kehrdienst und Laubentfernung?“ → „Übernehmen Sie auch Kehrdienst und Laub?“
* FAQ „Wann dürfen Hecken geschnitten werden?“ → „Wann darf man Hecken schneiden?“ Antwort am Ende ergänzen: „Mehr dazu im Ratgeber <a href="/ratgeber/hecke-schneiden-erlaubt.html">Wann darf man Hecken schneiden?</a>“

---

## 6. Winterdienst (winterdienst.html)

### 6.1 Einleitung unter H1 (bleibt, ist bereits eine gute Kurzantwort)

### 6.2 Kurz beantwortet

* „Wer bietet in Bruchsal zuverlässigen Winterdienst für Gehwege und Hauseingänge an?“ → „Wer räumt in Bruchsal Gehwege und Hauseingänge zuverlässig?“
* „Was kostet Winterdienst für ein Mehrfamilienhaus oder ein kleines Gewerbeobjekt?“ → „Was kostet Winterdienst für ein Mehrfamilienhaus?“
* Neue H3 „Bin ich nach der Beauftragung aus der Haftung?“ an dritter Stelle. Antwort (Kurzantwort, 54 Wörter):
  > Nein, nicht vollständig. In Bruchsal ist die Räum- und Streupflicht per Satzung auf die Anlieger übertragen. Die Ausführung können Sie an uns abgeben, die Pflicht zur sorgfältigen Auswahl und Kontrolle bleibt bei Ihnen. Dafür gibt es unser Einsatzprotokoll mit Datum, Uhrzeit, Witterung und Streumittel. Damit belegen Sie, dass geräumt und kontrolliert wurde.
* H3 alt „Wer räumt, streut und kümmert sich zusätzlich um die Verkehrssicherung?“ entfällt. Ihr Satz über Stolperstellen, lose Platten, Außenbeleuchtung und Totholz wird an die Antwort „Wer räumt in Bruchsal Gehwege …“ angehängt.
* „Welcher Anbieter kombiniert Außenanlagenpflege und Winterdienst?“ → „Gibt es Gartenpflege und Winterdienst bei einem Anbieter?“
* „Wer übernimmt Kehrdienst, Laubentfernung und saisonale Außenpflege für Wohnanlagen?“ → „Wer kehrt Laub und entfernt im Frühjahr den Splitt?“
* „Ist der Winterdienst auf die Mieter umlagefähig?“ → „Kann ich den Winterdienst auf die Mieter umlegen?“

### 6.3 FAQ

* „Bin ich nach der Beauftragung aus der Haftung?“ wandert nach oben (6.2) und wird hier entfernt, damit die Frage nicht doppelt im FAQPage-Schema steht.
* „Ab wann muss morgens geräumt sein?“ → „Bis wann muss in Bruchsal morgens geräumt sein?“ Antwort bleibt.
* Neue FAQ „Kann ich den Winterdienst von der Steuer absetzen?“ (Seobility-Frage):
  > Privathaushalte können Winterdienst auf dem eigenen Grundstück in der Regel als haushaltsnahe Dienstleistung nach § 35a Einkommensteuergesetz geltend machen, abziehbar sind die Arbeitskosten laut Rechnung. Bei Mietern geht das über die Nebenkostenabrechnung. Wie das in Ihrem Fall aussieht, klären Sie bitte mit Ihrem Steuerberater. Auf unserer Rechnung stehen Arbeitskosten und Material getrennt.

  Hinweis: Den letzten Satz nur übernehmen, wenn die Rechnungen das tatsächlich so ausweisen. Sonst weglassen.

---

## 7. Entrümpelung (entruempelung.html)

* Streichung aus 1.6.
* Kurz beantwortet: „Woran erkennt man eine seriöse Entrümpelungsfirma in Bruchsal?“ → „Woran erkennt man eine seriöse Entrümpelungsfirma?“; „Wie schnell ist eine Entrümpelung in Bruchsal möglich?“ → „Wie schnell ist eine Entrümpelung möglich?“; „Wer macht eine Haushaltsauflösung im Raum Bruchsal mit Abtransport und besenreiner Übergabe?“ → „Wer macht eine Haushaltsauflösung mit besenreiner Übergabe?“; „Was kostet eine Entrümpelung einer Wohnung oder eines Kellers in Baden-Württemberg?“ → „Was kostet eine Entrümpelung von Wohnung oder Keller?“; „Machen Sie Haushaltsauflösungen in Helmsheim, Heidelsheim und Umgebung?“ → „Räumen Sie auch in Heidelsheim, Helmsheim und den anderen Ortsteilen?“; „Wer übernimmt eine Haushaltsauflösung, wenn die Eigentümer nicht vor Ort sind?“ → „Geht eine Haushaltsauflösung, ohne dass ich vor Ort bin?“; „Wer entsorgt Sperrmüll, Möbel und Kellerinhalte aus einer Hand?“ → „Wer entsorgt Sperrmüll, Möbel und Kellerinhalte?“
* Neue FAQ „Kann ich Fotos statt einer Besichtigung schicken?“:
  > Für kleinere Räume wie Keller oder Garage reichen oft Fotos per WhatsApp an 0163 7221790. Bei Wohnungen und Gewerbeflächen kommen wir vorbei, weil Volumen, Treppen und der Weg zum Fahrzeug den Preis stärker bestimmen, als Fotos zeigen. Die Besichtigung kostet nichts.

---

## 8. Wohnungsübergabe (wohnungsuebergabe.html)

* Streichung aus 1.6.
* H1 neu laut Spezifikation („Wohnungsübergabe und Leerstandskontrolle in Bruchsal“). „Immobilienservice“ bleibt im Navigationsnamen.
* Kurz beantwortet: „Wer übernimmt Wohnungsübergaben mit Fotoprotokoll für Vermieter und Hausverwaltungen?“ → „Wer übernimmt Wohnungsübergaben mit Fotoprotokoll?“; „Wer dokumentiert im Raum Bruchsal und Karlsruhe Abnahmen, Schlüsselrücknahmen und Zählerstände?“ → „Was wird bei der Abnahme dokumentiert?“ (Antwort: zweiter Satz „Unser Einsatzgebiet ist …“ ersetzen durch „Wir arbeiten in Bruchsal mit allen Stadtteilen und im Landkreis Karlsruhe.“); „Was kostet ein externer Dienstleister für Wohnungsübergabe oder Leerstandskontrolle?“ → „Was kostet eine Wohnungsübergabe durch einen Dienstleister?“; „Ich wohne nicht in der Nähe: wie organisiere ich den Mieterwechsel trotzdem sauber?“ → „Ich wohne nicht in der Nähe. Wie klappt der Mieterwechsel trotzdem?“; „Gibt es Abnahme, Reinigung und kleine Reparaturen vor der Neuvermietung aus einer Hand?“ → „Gibt es Abnahme, Reinigung und Reparatur aus einer Hand?“
* FAQ „Sind Ihre Protokolle für die Kautionsabrechnung verwendbar?“ → „Kann ich das Protokoll für die Kautionsabrechnung nutzen?“ Antwort bleibt.
* Neuer Satz am Ende der Einleitung: „Was in ein gutes Übergabeprotokoll gehört, zeigt unser Ratgeber <a href="/ratgeber/wohnungsuebergabe-protokoll-bruchsal.html">Übergabeprotokoll beim Mieterwechsel</a>.“

---

## 9. Kleinreparaturen (kleinreparaturen.html)

* Streichung aus 1.6.
* Neuer Block „Kurz beantwortet“ nach „Eine Liste, ein Termin“:

  **Wer erledigt mehrere Kleinreparaturen in einem Termin?**
  > Wir sammeln die offenen Punkte aus Übergabeprotokoll, Begehung oder Mietermeldung und arbeiten sie in einem Termin ab: Leuchten, Silikonfugen, schleifende Türen, lose Sockelleisten, Montage. Die Anfahrt zahlen Sie einmal pro Termin, nicht pro Position. In Bruchsal und im Landkreis Karlsruhe, in Wohnungen, Büros und Treppenhäusern.

  **Was machen Sie selbst und wann kommt ein Fachbetrieb?**
  > Leuchtmittel, Lampen, Beschläge, Silikon, Streichen, Klickvinyl, Laminat und kleiner Trockenbau machen wir selbst. Arbeiten an Strom-, Gas- und Wasserleitungen übernehmen zugelassene Fachbetriebe. Diese Termine koordinieren wir auf Wunsch und sind dabei.

  **Wie wird abgerechnet?**
  > Nach Aufwand mit festem Stundensatz und Materialnachweis oder als Pauschale, wenn der Umfang vorher feststeht. Bei mehreren Positionen ist die Pauschale meist günstiger. Den Festpreis bekommen Sie nach dem kostenlosen Ortstermin schriftlich.

  (Die bisherige FAQ „Wie wird abgerechnet?“ wird dann aus dem FAQ-Block entfernt, um Dopplung im Schema zu vermeiden.)
* H2 „So läuft es ab“ → „So läuft ein Reparaturtermin ab“.

---

## 10. Metallarbeiten und Schlösser (metallarbeiten-schloesser.html)

* Streichung aus 1.6.
* Neuer Block „Kurz beantwortet“:

  **Wer repariert Zaun, Tor oder Geländer in Bruchsal?**
  > Gebäudewerke repariert Zäune, Tore und Geländer in Bruchsal und im Landkreis Karlsruhe selbst, inklusive Zuschnitt und Schweißarbeit. Im Team arbeiten ein geprüfter Industriemeister Metall und ein gelernter Metallbauer. Halterungen, Konsolen und Schutzgitter fertigen wir nach Maß. Für ein Angebot reichen oft Fotos per WhatsApp.

  **Wie schnell wird ein Schließzylinder getauscht?**
  > Standardzylinder tauschen wir am selben oder nächsten Werktag. Gehört die Tür zu einer Schließanlage, bestellen wir über die Sicherungskarte beim Hersteller nach. Dann hängt es an dessen Lieferzeit, üblich sind ein bis drei Wochen.

  **Können Sie eine bestehende Schließanlage erweitern?**
  > Ja, über die Sicherungskarte beim Hersteller. Wir bestellen nach, bauen ein und tragen neue Schlüssel in die Schlüsselliste ein.

  (Die beiden gleichlautenden FAQ unten entfallen dafür.)
* Neue FAQ „Öffnen Sie auch zugefallene Türen?“:
  > Eine Türöffnung rund um die Uhr bieten wir nicht an. Dafür ist ein Schlüsseldienst der richtige Ansprechpartner. Wir kommen danach, wenn der Zylinder getauscht oder die Schließanlage ergänzt werden soll, oder tagsüber zu Objekten, die wir betreuen.

  Hinweis an den Inhaber: Bitte bestätigen. Falls Notöffnungen doch angeboten werden, Antwort anpassen.
* H2 „So läuft es ab“ → „So läuft ein Auftrag ab“.

---

## 11. Preise (preise.html)

### 11.1 Einleitung

Vorher:
> Die Preisliste 2026 nennt unsere Richtpreise für Hausmeisterservice, Reinigung und Gartenpflege in Bruchsal und im Landkreis Karlsruhe. Alle Preise auf dieser Seite sind Nettopreise. …

Nachher:
> Hier stehen unsere Richtpreise für Hausmeisterservice, Reinigung, Gartenpflege und Winterdienst in Bruchsal und im Landkreis Karlsruhe. Alle Preise sind Nettopreise, die Bruttopreise mit 19 % Umsatzsteuer stehen jeweils daneben. Verbindlich wird der Preis nach einem kostenlosen Ortstermin, dann bekommen Sie für Ihr Objekt einen schriftlichen Festpreis. Stand: Oktober 2026.

### 11.2 „Kurz beantwortet: die häufigsten Preisfragen“ → „Die häufigsten Preisfragen“

Fragen werden zu H3 (heute `<p>`). „Was kostet ein Hausmeisterservice für ein Mehrfamilienhaus mit 8 bis 20 Einheiten?“ → „Was kostet ein Hausmeisterservice für 7 bis 20 Wohnungen?“ (die Antwort spricht von 7 bis 20, die Frage bisher von 8 bis 20). Gleiche Korrektur auf hausmeisterservice.html.

### 11.3 H2 „Preise Gartenpflege und Grünpflege (einmalig)“ → „Preise Gartenpflege und Grünpflege“

Erster Satz der Tabellen-Erläuterung ergänzen: „Die Tabelle zeigt einmalige Einsätze.“

---

## 12. Über uns (ueber-uns.html)

### 12.1 Einleitung

Vorher:
> Die Gebäudewerke GbR ist ein Objekt- und Gebäudeservice mit Sitz in Hambrücken bei Bruchsal. Wir betreuen Wohn- und Gewerbeimmobilien in Bruchsal und im Landkreis Karlsruhe, mit eigenem Personal und in festen Touren.

Nachher:
> Die Gebäudewerke GbR betreut Wohn- und Gewerbeimmobilien in Bruchsal und im Landkreis Karlsruhe, mit eigenem Personal und in festen Touren. Hinter dem Betrieb stehen vier Gesellschafter: Fatih Altun, Enes Yesildag, Burak Kartal und Julian Bender. Jeder von ihnen ist für einen Leistungsbereich zuständig, und jedes Objekt hat bei uns einen festen Betreuer.

### 12.2 „Wer wir sind“, zweiter Absatz streichen

Vorher: „Jeder im Team hat einen eigenen Schwerpunkt. Aus Metallbau, Industriemechanik und Vertrieb bringen wir unterschiedliche Erfahrungen in jedes Objekt.“ (wiederholt Absatz 1) → streichen.

Dritter Absatz bleibt, aber ohne die „nicht … und nicht …“-Konstruktion:
Vorher: „Wir sind keine Reinigungsfirma, die nebenbei Hausmeister spielt, und kein Handwerksbetrieb, der die Reinigung mitnimmt. Wir sind der eine Ansprechpartner für alles, was an einem Objekt laufend anfällt.“
Nachher: „Bei uns bekommen Sie einen Ansprechpartner für alles, was an einem Objekt laufend anfällt: Kontrollgang, Treppenhaus, Außenanlage, Winterdienst und die Reparatur, die dabei auffällt.“

### 12.3 Teamkarten (E-E-A-T)

Jede Karte zeigt: Name, Rolle, Qualifikation, Zuständigkeit, Zitat (vorhanden), plus neu „Schreibt im Ratgeber über: …“ mit 2 Links.

| Person | Rolle (sichtbar und jobTitle) | Qualifikation (nur vorhandene Angaben) | Ratgeber-Links |
|---|---|---|---|
| Fatih Altun | Gesellschafter, Metall- und Schlosserarbeiten, Reparaturen | Geprüfter Industriemeister Metall (IHK) | Schlüsselverwaltung, Kleinreparaturen bündeln |
| Enes Yesildag | Gesellschafter, Vertrieb, Hausverwaltung und Wohnungsübergaben | Kaufmann, Vertrieb und Vermarktung | Übergabeprotokoll, Hausmeisterkosten umlagefähig |
| Burak Kartal | Gesellschafter, Qualität, Reinigung und Gartenpflege | Metallbauer, Metallbau sowie Stahl- und Gerüstbau, Qualitätsmanagement | Treppenhaus-Reinigungsplan, Hecke schneiden |
| Julian Bender | Gesellschafter, Hausmeisterservice und Winterdienst | Industriemechaniker, CNC-Fertigung | Räum- und Streupflicht, Streuprotokoll |

Hinweis: „Gesellschafter“ ist durch das Impressum belegt. Kein Gründungsjahr nennen, solange es nicht bekannt ist.

### 12.4 Neuer Abschnitt nach „Worauf Sie sich verlassen können“ (H2 bleibt), Text ergänzen

> Konkret heißt das für Sie: Rückruf am selben oder nächsten Werktag. Kostenloser Ortstermin, danach innerhalb von zwei bis drei Werktagen ein schriftliches Angebot mit Leistungsverzeichnis. Eigenes Personal, keine Subunternehmer. Arbeiten an Elektro, Gas und Trinkwasser übernehmen zugelassene Fachbetriebe, deren Termine wir begleiten. Betriebshaftpflicht mit Deckungssumme bis 5 Mio. Euro, den Nachweis zeigen wir auf Anfrage.

---

## 13. Kontakt (kontakt.html)

* H1 „Kontakt zu Gebäudewerke in Bruchsal“ → „Kontakt zu Gebäudewerke“ (Ortsbezug steht in der Einleitung).
* Einleitung vorher: „Für den Kontakt zu Gebäudewerke schreiben Sie kurz, …“ Nachher:
  > Schreiben Sie uns kurz, um welches Objekt es geht und was gebraucht wird, oder rufen Sie an: 0163 7221790, Montag bis Freitag von 7 bis 17 Uhr. Für kleine Aufträge reichen oft Fotos per WhatsApp. Bei laufenden Leistungen kommen wir vorher zum kostenlosen Ortstermin, weil sich Flächen und Zugänge aus der Ferne nicht seriös kalkulieren lassen.
* Gestrichener Absatz (1.6) wird ersetzt durch:
  > Für dringende Schäden außerhalb der Bürozeiten erreichen Sie unseren Notdienst täglich von 17 bis 24 Uhr unter derselben Nummer.
* H2 „Anfahrt“ → „Anfahrt und Einsatzgebiet“. Erster Absatz bleibt (Adresse Hambrücken ist hier richtig). Zweiter Absatz, vorher „Unser Betrieb in Hambrücken liegt nordwestlich von Bruchsal. Von hier fahren wir …“, nachher:
  > Von hier fahren wir die Objekte in festen Touren an: die Bruchsaler Kernstadt, Büchenau, Heidelsheim, Helmsheim, Obergrombach und Untergrombach und die Gemeinden im Landkreis Karlsruhe rund um Bruchsal. Alle Orte finden Sie unter <a href="/einsatzgebiet.html">Einsatzgebiet</a>.
* Maps-Link: `https://share.google/v7XolrfYaCO55YrZz` durch den Profil-Link `https://share.google/dHbp6caGIhLZVhp4Y` ersetzen (gilt für alle 39 Vorkommen, siehe technik-und-schema.md).

---

## 14. Karriere (karriere.html)

Nur H1: „Jobs im Hausmeisterservice: Karriere bei Gebäudewerke in Bruchsal“ → „Jobs im Hausmeisterservice und in der Reinigung in Bruchsal“. Rest bleibt.

---

## 15. Ratgeber-Übersicht (ratgeber/index.php)

Vorher, zwei Absätze:
> Hier erklären wir, was bei Winterdienst, Gartenpflege, Reinigung und Hausmeisterservice in Bruchsal und im Landkreis Karlsruhe zu beachten ist: Pflichten, Fristen, Kosten und Abläufe, kurz und verständlich.
> Beiträge zu Hausmeisterservice, Winterdienst, Reinigung und Betriebskosten, geschrieben aus der Praxis in Bruchsal. Die Texte richten sich an Eigentümer, Vermieter und Hausverwaltungen, …

Nachher, ein Absatz:
> Pflichten, Fristen, Kosten und Abläufe rund um Mehrfamilienhaus und Gewerbeobjekt, so wie sie uns in Bruchsal im Alltag begegnen. Geschrieben von den vier Gesellschaftern von Gebäudewerke, jeweils zu ihrem Fachgebiet. Rechtliche Hinweise sind allgemein gehalten und ersetzen keine Beratung im Einzelfall.

„Die ersten Beiträge erscheinen in Kürze.“ nur ausgeben, wenn wirklich kein Beitrag veröffentlicht ist (PHP-Bedingung prüfen).

---

## 16. Ratgeberartikel

### 16.1 Für alle 31 Artikel (E-E-A-T)

1. **Kopfzeile** (vorhanden: „Thema · veröffentlicht am … · von …“) ergänzen um „aktualisiert am …“, wenn `artikel-aktualisiert` vom Datum abweicht. Beispiel: `Gebäudereinigung · veröffentlicht am 21.10.2026 · aktualisiert am 29.10.2026 · von Burak Kartal`.
2. **Autorenbox** am Ende vor „Weiterlesen“ (neu):
   > **Burak Kartal** ist Gesellschafter von Gebäudewerke und für Qualität, Reinigung und Gartenpflege zuständig. Er ist gelernter Metallbauer und hat im Metall-, Stahl- und Gerüstbau gearbeitet. <a href="/ueber-uns.html#team">Zum Team</a>

   Texte für die anderen Autoren:
   > **Fatih Altun** ist Gesellschafter von Gebäudewerke, geprüfter Industriemeister Metall (IHK) und zuständig für Metall- und Schlosserarbeiten, Türen, Schließanlagen und Kleinreparaturen.
   > **Enes Yesildag** ist Gesellschafter von Gebäudewerke und Kaufmann. Er betreut Angebote, Hausverwaltungen und Wohnungsübergaben.
   > **Julian Bender** ist Gesellschafter von Gebäudewerke, gelernter Industriemechaniker und zuständig für Hausmeisterservice, Kontrollgänge und Winterdienst.
3. **Quellenzeile**: Paragrafen verlinken, wo die URL sicher ist (Liste in `seiten-spezifikation.json`, Feld `quelle_offiziell`, alle auf gesetze-im-internet.de). Die Streupflichtsatzung der Stadt Bruchsal und die Landesbauordnung BW nur mit geprüfter URL verlinken, sonst als Text stehen lassen. Der Satz „Dieser Beitrag ersetzt keine Rechtsberatung.“ bleibt bei allen Rechtsthemen.
4. **Autorwechsel**: kosten-hausmeisterservice-bruchsal von Fatih Altun auf Enes Yesildag (er macht laut Teamseite die Angebote).

### 16.2 Kurzantworten mit Keyword-Vorsatz bereinigen

| Artikel | vorher (Anfang) | nachher (Anfang) |
|---|---|---|
| bueroreinigung-praxisreinigung-bruchsal | „Für die Büro- und Praxisreinigung gilt: Büros und Praxen werden am besten …“ | „Büros und Praxen werden am besten …“ |
| glasreinigung-bruchsal | „Für die Glasreinigung gilt als Faustregel: Glasflächen im Treppenhaus sollten …“ | „Glasflächen im Treppenhaus sollten …“ |
| treppenhausreinigung-bruchsal | „Für die Treppenhausreinigung gilt: Ein Treppenhaus in einer Wohnanlage sollte …“ | „Ein Treppenhaus in einer Wohnanlage sollte …“ |
| winterdienst-beauftragen-bruchsal | „Wer in Bruchsal einen Winterdienst sucht, sollte ihn bis Ende Oktober beauftragen.“ | „Den Winterdienst sollten Sie bis Ende Oktober beauftragen.“ (Rest bleibt) |

### 16.3 kosten-hausmeisterservice-bruchsal (erscheint 27.11.2026)

Kurzantwort, vorher:
> Was ein Hausmeisterservice kostet, hängt von der Größe des Objekts, den vereinbarten Leistungen und dem Turnus ab. Woraus sich der Preis im Einzelnen zusammensetzt, zeigt der Ortstermin am besten. Seriöse Anbieter nennen deshalb keinen Pauschalpreis pro Quadratmeter, …

Nachher (57 Wörter):
> Ein Hausmeisterservice kostet bei Gebäudewerke ab 130 € netto im Monat für Häuser bis 6 Wohneinheiten, ab 190 € für 7 bis 20 Einheiten und ab 280 € für größere Anlagen, jeweils bei zwei Terminen pro Woche. Der genaue Preis hängt von Größe, Leistungen und Turnus ab und steht nach einem kostenlosen Ortstermin als Monatspauschale fest.

Neuer H2 „Richtpreise pro Monat“ (vor „Warum es keinen Einheitspreis gibt“), Inhalt: die drei Zeilen der Tabelle Objektbetreuung von preise.html (netto und brutto, unverändert übernommen) und der Satz „Alle Richtpreise stehen auf unserer <a href="/preise.html#objektbetreuung">Preisseite</a>.“

Neue FAQ:
* „Was kostet ein Hausmeister für ein 6-Familienhaus?“
  > Für Häuser bis 6 Wohneinheiten liegt unser Richtpreis bei 130 € netto im Monat, brutto 155 €, bei zwei Terminen pro Woche. Den festen Preis nennen wir nach dem Ortstermin.
* „Was kostet ein Hausmeister pro Jahr?“
  > Bei einer Monatspauschale ab 130 € netto sind das ab 1.560 € netto im Jahr für ein Haus bis 6 Einheiten, ab 2.280 € für 7 bis 20 Einheiten. Winterdienst kommt als Saisonpauschale dazu, wenn Sie ihn buchen.

  (Rechnung 130 × 12 und 190 × 12, aus vorhandenen Preisen abgeleitet.)

### 16.4 muelltonnendienst-bruchsal

Neuer H2 „Was kostet der Mülltonnendienst?“ vor „Können die Kosten umgelegt werden?“:
> Unser Richtpreis für den Mülltonnenservice liegt bei 90 € netto, brutto 107 €. Er gilt für Behälter mit 60 bis 120 Liter, 240 Liter, 660 bis 770 Liter und 1.100 Liter. Den Rhythmus wählen Sie, zum Beispiel wöchentlich oder zweimal pro Woche. Biomüll, Karton und andere Fraktionen fragen Sie bitte an. <a href="/preise.html#muelltonnen">Preisliste Mülltonnenservice</a>

Hinweis: Die Preisseite nennt keinen Bezugszeitraum für die 90 €. Vor Veröffentlichung klären, ob pro Monat. Erst dann „im Monat“ ergänzen.

### 16.5 wohnungsuebergabe-protokoll-bruchsal

Neuer H2 „Checkliste für die Wohnungsübergabe“ nach „Was gehört ins Übergabeprotokoll?“:
* Datum, Uhrzeit, Anschrift, Lage der Wohnung
* Namen aller Anwesenden
* Zustand Raum für Raum: Wände, Decken, Böden, Fenster, Türen
* Bad und Küche: Armaturen, Fliesen, Fugen, Einbaugeräte
* Mängel mit Ort, Foto und kurzer Beschreibung
* Zählerstände Wasser, Wärme, Strom und Gas mit Zählernummer und Foto
* Anzahl und Art der Schlüssel, die übergeben werden
* Vereinbarungen, zum Beispiel was der Mieter noch erledigt und bis wann
* Unterschriften beider Seiten

Neue FAQ „Was passiert, wenn der Mieter nicht unterschreibt?“:
> Dann halten Sie im Protokoll fest, dass die Unterschrift verweigert wurde, und dokumentieren den Zustand trotzdem vollständig mit Fotos und Datum. Am besten ist eine weitere Person als Zeuge dabei. Wie Sie im Streitfall vorgehen, klären Sie mit Ihrer Verwaltung oder einer rechtlichen Beratung.

### 16.6 entruempelung-ablauf-bruchsal

Neue FAQ „Wer muss die Wohnung eines Verstorbenen ausräumen?“:
> In der Regel die Erben, denn der Mietvertrag geht auf sie über. Wer die Erbschaft ausschlägt, ist dafür nicht mehr zuständig. Bei Fragen zum Erbrecht hilft ein Notar oder Anwalt. Die Räumung selbst übernehmen wir zum Festpreis, auch wenn die Erben weiter weg wohnen.

Hinweis: Erbrechtlicher Inhalt ist allgemein und korrekt (Eintritt in das Mietverhältnis nach § 564 BGB). Quelle in der Quellenzeile ergänzen: § 564 BGB, https://www.gesetze-im-internet.de/bgb/__564.html

### 16.7 raeum-und-streupflicht-bruchsal

Neue FAQ „Ist Streusalz auf dem eigenen Grundstück erlaubt?“:
> Die Bruchsaler Satzung regelt vor allem die Gehwege. Dort wird grundsätzlich abstumpfend mit Sand, Splitt oder Asche gestreut, Salz nur in Ausnahmefällen wie Eisregen oder an Treppen. Für reine Privatflächen gilt die Satzung meist nicht, Salz schadet Pflaster, Beton und Pflanzen aber auch dort. Den genauen Wortlaut erfahren Sie bei der Stadt Bruchsal.

### 16.8 treppenhausreinigung-bruchsal

Neue FAQ „Was gehört zur Treppenhausreinigung durch Mieter?“:
> Was Mieter reinigen müssen, steht im Mietvertrag oder in der Hausordnung. Üblich ist das Kehren und feuchte Wischen von Stufen und Podesten vor der eigenen Wohnung bis zur nächsten Etage, oft auch Handlauf und Fenster in diesem Bereich. Ohne Regelung im Vertrag muss der Mieter nicht putzen.

Bestehende FAQ-Antworten sind sehr knapp (ein Satz). Erweitern, Beispiel „Wie oft sollte ein Treppenhaus gereinigt werden?“:
Vorher: „In Wohnanlagen meist wöchentlich, in kleinen Häusern auch alle zwei Wochen. Dazu monatliche und jährliche Arbeiten nach Plan.“
Nachher: „In Wohnanlagen meist einmal pro Woche, in kleinen Häusern mit wenig Verkehr auch alle zwei Wochen. Monatlich kommen Geländer, Türen, Briefkästen und Heizkörper dazu, mehrmals im Jahr die Fenster.“

### 16.9 metallarbeiten im Ratgeber schluesselverwaltung-bruchsal

FAQ „Können Sie Schließzylinder tauschen?“: Link auf /metallarbeiten-schloesser.html in die Antwort.

---

## 17. Neue Seiten

### 17.1 einsatzgebiet.html

**H1** Unser Einsatzgebiet in Bruchsal und im Landkreis Karlsruhe

**Einleitung (Kurzantwort, 50 Wörter)**
> Gebäudewerke betreut Wohnanlagen, Eigentümergemeinschaften und Gewerbeobjekte in Bruchsal mit allen Stadtteilen und in den Gemeinden rund um Bruchsal im Landkreis Karlsruhe. Dazu gehören Forst, Karlsdorf-Neuthard, Ubstadt-Weiher, Bad Schönborn, Östringen, Kronau, Hambrücken, Waghäusel, Philippsburg, Graben-Neudorf, Stutensee und Bretten. Für Objekte weiter weg fragen Sie bitte an.

**H2 Bruchsal mit allen Stadtteilen**
> In Bruchsal sind wir in der Kernstadt und in allen fünf Stadtteilen unterwegs. Hier liegt der Schwerpunkt unserer Touren, hier haben wir auch schon Reinigungsaufträge ausgeführt.

H3 Kernstadt / H3 Büchenau, Heidelsheim, Helmsheim / H3 Obergrombach und Untergrombach: je ein bis zwei Sätze, **nur** mit Aussagen, die stimmen, z. B. „Hausmeisterservice, Treppenhausreinigung, Gartenpflege und Winterdienst übernehmen wir in allen Stadtteilen zu denselben Bedingungen wie in der Kernstadt.“ Keine erfundenen Straßen, Objekte oder Kunden.

**H2 Gemeinden rund um Bruchsal** mit den vier H3-Gruppen aus der Spezifikation. Je Gruppe ein Satz, z. B.:
> Forst, Karlsdorf-Neuthard und Ubstadt-Weiher grenzen direkt an Bruchsal. Für Objekte dort gelten dieselben Leistungen und Preise.

(Bitte vom Inhaber bestätigen lassen, dass Preise im ganzen Gebiet gleich sind. Falls nicht: Satz weglassen.)

> In Bad Schönborn und Östringen haben wir bereits Reinigungsaufträge ausgeführt.

**H2 Welche Leistungen es überall gibt**
> Im ganzen Gebiet übernehmen wir Hausmeisterservice, Treppenhaus- und Gebäudereinigung, Gartenpflege, Winterdienst, Wohnungsübergaben, Entrümpelungen, Kleinreparaturen sowie Metallarbeiten und Schließanlagen. Den Preis nennen wir nach einem kostenlosen Ortstermin schriftlich.
Darunter Liste mit Links auf alle Leistungsseiten.

**H2 Warum wir in festen Touren fahren**
> Beim Winterdienst entscheiden kurze Wege. Wenn um 7 Uhr in Bruchsal geräumt sein muss, zählt jede Minute zwischen zwei Objekten. Deshalb bündeln wir Objekte zu festen Touren und nehmen nur an, was sich darin sinnvoll unterbringen lässt. Ist ein Objekt zu weit weg für eine verlässliche Zeit, sagen wir das vorher.

**H2 Ihr Ort ist nicht dabei?**
> Fragen Sie trotzdem an. Für Objekte in der Stadt Karlsruhe oder weiter weg prüfen wir, ob sie in eine Tour passen, und sagen Ihnen kurzfristig Bescheid.

**FAQ**
* Kommen Sie auch nach Karlsruhe? → „Für Objekte in der Stadt Karlsruhe fragen Sie bitte an. Wir prüfen, ob das Objekt in eine bestehende Tour passt. Der Schwerpunkt unserer Arbeit liegt in Bruchsal und den umliegenden Gemeinden.“
* Kostet die Anfahrt in die Ortsteile extra? → **Platzhalter, vom Inhaber auszufüllen.** Bei laufenden Verträgen ist die Anfahrt laut Gebäudereinigungsseite in der Monatspauschale enthalten („In der Monatspauschale stecken Arbeitszeit, Reinigungsmittel, Geräte und Anfahrt“). Für Einzelaufträge bitte Regel nennen.
* Gilt der Winterdienst im ganzen Gebiet? → „Ja, aber nur so weit, wie es die Touren zulassen. Wir nehmen nur so viele Objekte an, wie wir bei starkem Schneefall in der vorgeschriebenen Zeit schaffen. Wer früh beauftragt, ist sicher eingeplant.“
* Wo haben Sie schon gearbeitet? → „Reinigungsaufträge haben wir unter anderem in Bruchsal, Bad Schönborn und Östringen ausgeführt.“

### 17.2 treppenhausreinigung.html

**H1** Treppenhausreinigung in Bruchsal für Mehrfamilienhäuser und WEG

**Einleitung (Kurzantwort, 55 Wörter)**
> Wir reinigen Treppenhäuser in Bruchsal und im Landkreis Karlsruhe nach einem schriftlichen Reinigungsplan, immer am gleichen Wochentag. Stufen, Podeste, Handläufe und Eingang meist jede Woche, in kleinen Häusern alle zwei Wochen. Jede Reinigung wird am Aushang mit Datum und Kürzel abgezeichnet. Mittel und Geräte sind im Preis enthalten, den Festpreis bekommen Sie nach dem Ortstermin.

**H2 Was zur Treppenhausreinigung gehört**
H3 Jede Woche: Stufen und Podeste kehren und feucht wischen, Handläufe abwischen, Eingangsbereich und Fußmatten.
H3 Jeden Monat: Geländer, Türen und Türgriffe, Briefkastenanlage, Heizkörper, Lichtschalter.
H3 Mehrmals im Jahr: Treppenhausfenster und Glastüren, nach Bedarf Spinnweben und Grundreinigung der Stufen.
(Inhalt aus dem Ratgeber übernommen.)

**H2 Kurz beantwortet**
* Wie oft sollte ein Treppenhaus gereinigt werden? → „In Wohnanlagen meist einmal pro Woche, in kleinen Häusern mit wenig Verkehr alle zwei Wochen. Den Turnus legen wir beim Ortstermin fest und schreiben ihn ins Leistungsverzeichnis.“
* Was kostet eine Treppenhausreinigung im Mehrfamilienhaus? → Antwort aus 4.3 (Nachher).
* Können Mieter zur Treppenhausreinigung verpflichtet werden? → „Ja, über Mietvertrag oder Hausordnung. Viele Eigentümer und Eigentümergemeinschaften vergeben die Reinigung trotzdem, weil es Streit im Haus vermeidet und die Reinigung verlässlich stattfindet.“
* Sind die Kosten auf die Mieter umlegbar? → „Bei Wohnraum in der Regel ja. Die Reinigung gemeinsam genutzter Flächen gehört nach § 2 Nr. 9 Betriebskostenverordnung zu den Betriebskosten, wenn der Mietvertrag die Umlage vorsieht. Übernimmt der Hausmeister die Reinigung, darf sie nicht doppelt abgerechnet werden.“

**H2 Nachweis am Aushang**
> Im Treppenhaus hängt der Reinigungsplan. Nach jeder Reinigung zeichnen wir mit Datum und Kürzel ab. Mieter und Verwaltung sehen auf einen Blick, wann zuletzt gereinigt wurde. Bei Objekten mit vielen Beschwerden machen wir zusätzlich Fotos.

**H2 Sichtkontrolle bei jeder Reinigung**
> Wer jede Woche durchs Treppenhaus geht, sieht, was sich verändert. Defekte Leuchten, lose Handläufe, beschädigte Türen und zugestellte Rettungswege melden wir mit Foto an Sie oder Ihre Verwaltung. Kleinere Mängel beheben wir auf Wunsch direkt, weil Reinigung und Hausmeisterservice bei uns zusammengehören.

**H2 Treppenhausreinigung und Hausmeisterservice in einem Vertrag**
> Viele Eigentümergemeinschaften buchen Treppenhausreinigung, Kontrollgang und Winterdienst zusammen. Dann gibt es einen Ansprechpartner, einen Vertrag und eine Rechnung, auf der umlagefähige Positionen getrennt stehen. Hausmeisterservice ab 130 € netto im Monat, Details auf der Seite <a href="/hausmeisterservice.html">Hausmeisterservice in Bruchsal</a>.

**FAQ**
* Werden Reinigungsmittel und Geräte gestellt? → „Ja, Mittel und Geräte sind im Preis enthalten.“
* Was passiert, wenn Fahrräder oder Kinderwagen im Weg stehen? → „Wir reinigen um die Gegenstände herum und melden der Verwaltung, wenn der Rettungsweg zugestellt ist. Wegräumen dürfen wir fremdes Eigentum nicht. Was im Treppenhaus stehen darf, erklärt unser Ratgeber <a href="/ratgeber/treppenhaus-rettungsweg.html">Treppenhaus als Rettungsweg</a>.“ (Ratgeber erscheint am 15.12.2026. Inline-Link wird bis dahin von auslieferung.php zu Text, der Satz bleibt lesbar.)
* Reinigen Sie auch Keller und Tiefgarage mit? → „Ja. Keller und Tiefgarage reinigen wir meist monatlich bis quartalsweise und nehmen sie in denselben Reinigungsplan auf.“
* Gibt es eine Mindestlaufzeit? → „Bei laufender Reinigung sind zwölf Monate üblich.“ (So steht es für laufende Betreuung auf der Startseite. Vom Inhaber bestätigen lassen, dass das auch für reine Reinigungsverträge gilt.)

### 17.3 bueroreinigung.html (Stufe 2)

**H1** Büroreinigung und Praxisreinigung in Bruchsal

**Einleitung (Kurzantwort, 54 Wörter)**
> Wir reinigen Büros, Praxen und Verkaufsflächen in Bruchsal vor Betriebsbeginn oder nach Geschäftsschluss, nach einem schriftlichen Reinigungsplan mit festen Intervallen. Bei dreimal pro Woche liegen die Richtpreise bei 449 € netto im Monat für 50 m², 705 € für 100 m², 1.049 € für 200 m² und 2.075 € für 500 m².

**H2 Gereinigt wird, wenn niemand arbeitet**: Text aus gebaeudereinigung.html, Abschnitt „Büroreinigung und Praxisreinigung in Bruchsal“, erster Absatz.
**H2 Was im Reinigungsplan steht**: Arbeitsplätze, Böden, Sanitärräume, Küche, Besprechungsräume, Intervalle. Verbrauchsmaterial auf Wunsch, getrennt ausgewiesen.
**H2 Richtpreise für die Büroreinigung**: Tabelle von preise.html mit Voraussetzungen (dreimal pro Woche, Standardnutzung, ein WC, ein Besprechungsraum, eine Küche).
**H2 Praxen und Behandlungsräume**: Verweis auf Hygieneplan der Praxis, Inhalte aus dem Ratgeber.
**H2 Schlüssel, Alarm und Zugang**: Inhalte aus dem Ratgeber (Schlüsselübergabe gegen Unterschrift).
**FAQ**: Antworten aus Ratgeber und Gebäudereinigungsseite übernehmen, keine neuen Fakten.

Nach Veröffentlichung: gebaeudereinigung.html Abschnitt Büroreinigung auf zwei Sätze plus Link kürzen.

---

## 18. E-E-A-T: Vertrauen sichtbar machen (Zusammenfassung)

| Signal | Wo | Text/Umsetzung | Quelle des Fakts |
|---|---|---|---|
| Echte Menschen | Startseite (Team-Abschnitt), Über uns, Ratgeber-Autorenbox | Name, Rolle, Qualifikation, Zuständigkeit (12.3, 16.1) | ueber-uns.html, impressum.html |
| Wer haftet | Footer, Über uns, Impressum | „Gebäudewerke GbR, vertreten durch Fatih Altun“ im Impressum; Gesellschafter im Impressum und auf Über uns | impressum.html |
| Betriebshaftpflicht bis 5 Mio. Euro | Vertrauensleiste, Startseite Fakten, Über uns | wie 1.4 | index.html, impressum.html |
| Eigenes Personal, keine Subunternehmer | Vertrauensleiste, FAQ Startseite | wie 1.4 | index.html |
| Fachbetriebe für Elektro, Gas, Trinkwasser | Startseite, Kleinreparaturen, Über uns | wie 12.4 | index.html |
| Fester Ansprechpartner | Vertrauensleiste | wie 1.4 | index.html |
| Festpreis nach kostenlosem Ortstermin | Vertrauensleiste, jede Leistungsseite | vorhanden | alle Seiten |
| Protokoll zu jedem Einsatz | Vertrauensleiste | vorhanden | index.html |
| Rückruf am selben oder nächsten Werktag | Kontakt, Über uns | 12.4 | index.html |
| Bürozeiten, Notdienst | Kopfleiste, Footer, Kontakt | 1.2 | alle Seiten |
| Google-Bewertungen | Bewertungsblock, Vertrauensleiste | 1.5 | google-profil.json |
| Veröffentlichungs- und Änderungsdatum | jeder Ratgeber | 16.1 | meta artikel-datum/aktualisiert |
| Quellen mit Links auf Gesetzestexte | Ratgeber mit Rechtsbezug | 16.1, Spezifikation | gesetze-im-internet.de |
| Hinweis „keine Rechtsberatung“ | Ratgeber mit Rechtsbezug | vorhanden, beibehalten | |
| Impressum und Datenschutz erreichbar | Footer jeder Seite | vorhanden | |

Nicht verwenden: Siegel, Zertifikate, Gründungsjahr, Kundenzahlen, „seit X Jahren“, Mitgliedschaften, solange sie nicht belegt sind. Die USt-IdNr. steht im Impressum als „wird nach Erteilung ergänzt“. Sobald sie vorliegt, eintragen (siehe offpage-und-gbp.md).
