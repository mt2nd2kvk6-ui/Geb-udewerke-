# Technik und strukturierte Daten

Stand 31.10.2026. Grundlage: Quellcode `website/`, Seobility-SEO-Check der Startseite (Score 92 %, Onpage 100 %, Backlinks 0 %), Prüfkriterien von Ahrefs Site Audit, rankingCoach und Seobility.

## 1. Befund in Kürze

| Bereich | Status | Maßnahme |
|---|---|---|
| Title, Meta, H1, Canonical, HTTPS, Sprache, Viewport | gut (Seobility 100 %) | Feinschliff laut `seiten-spezifikation.json` |
| Backlinks | 0 verweisende Domains | siehe `offpage-und-gbp.md` |
| robots.txt | fehlerhaft (Gruppen, Widerspruch zu noindex) | Abschnitt 4 |
| Maps-/Profil-Links | zwei verschiedene Share-Links | überall `https://share.google/dHbp6caGIhLZVhp4Y` bzw. CID-Link |
| Telefonformat | drei Schreibweisen | `0163 7221790` sichtbar |
| Name | Website „Gebäudewerke GbR“, Profil „Gebäudewerke - Hausmeisterservice & Gebäudereinigung“ | Abschnitt 7 |
| geo-Meta | zeigt Hambrücken | Abschnitt 3.9 |
| Inline-CSS | ca. 62 KB in jeder Seite | Abschnitt 6 |
| Ratgeber-Titel mit „2026“ | veraltet ab Januar | in Spezifikation entfernt |
| Bilder | Stockfotos, Alt-Texte teils falsch | `alt-texte.json` |
| Interne Duplikat-Ankertexte | Seobility-Warnung | `interne-verlinkung.md` 5.3 |

## 2. Gesamtbild der strukturierten Daten

Ein zusammenhängender `@graph` je Seite, Entitäten über `@id` verknüpft:

| @id | Typ | auf welchen Seiten vollständig | sonst |
|---|---|---|---|
| `https://gebaeudewerke.de/#organisation` | HomeAndConstructionBusiness | Startseite, Kontakt, Über uns, Einsatzgebiet | auf allen anderen Seiten nur als Referenz `{"@id": …}` plus `name` |
| `https://gebaeudewerke.de/#website` | WebSite | Startseite | Referenz |
| `…/ueber-uns.html#person-fatih-altun` usw. | Person | Über uns | Referenz in Article.author |
| `<url>#webseite` | WebPage / AboutPage / ContactPage / CollectionPage | jede Seite | |
| `<url>#brotkrumen` | BreadcrumbList | jede Seite außer Startseite | |
| `<url>#leistung` | Service | jede Leistungsseite | |
| `<url>#fragen` | FAQPage | Seiten mit sichtbarem FAQ | |
| `<url>#artikel` | Article | jeder Ratgeber | |

Heute steht das volle Firmenobjekt (inkl. OfferCatalog mit 8 Services) auf jeder Seite, auch auf 404/danke. Das ist erlaubt, bläht aber jede Seite um mehrere KB auf. Empfehlung: volles Objekt nur auf den vier genannten Seiten, sonst Referenz.

## 3. Schema im Detail

### 3.1 Firma (HomeAndConstructionBusiness)

```json
{
  "@type": "HomeAndConstructionBusiness",
  "@id": "https://gebaeudewerke.de/#organisation",
  "name": "Gebäudewerke",
  "legalName": "Gebäudewerke GbR",
  "alternateName": ["Gebäudewerke Objekt- und Gebäudeservice", "Gebäudewerke - Hausmeisterservice & Gebäudereinigung"],
  "description": "Hausmeisterservice, Treppenhaus- und Gebäudereinigung, Gartenpflege, Winterdienst, Wohnungsübergaben, Entrümpelung, Kleinreparaturen sowie Metallarbeiten und Schließanlagen für Wohnanlagen, Eigentümergemeinschaften und Gewerbe in Bruchsal und im Landkreis Karlsruhe.",
  "url": "https://gebaeudewerke.de/",
  "logo": {"@type": "ImageObject", "url": "https://gebaeudewerke.de/assets/img/logo-voll.png", "width": 800, "height": 495},
  "image": "https://gebaeudewerke.de/assets/img/social-vorschau.jpg",
  "telephone": "+49 163 7221790",
  "email": "info@gebaeudewerke.de",
  "address": {"@type": "PostalAddress", "streetAddress": "Allmend 2", "postalCode": "76707", "addressLocality": "Hambrücken", "addressRegion": "Baden-Württemberg", "addressCountry": "DE"},
  "geo": {"@type": "GeoCoordinates", "latitude": 49.192062, "longitude": 8.5403253},
  "hasMap": "https://www.google.com/maps?cid=5771542189821334782",
  "sameAs": [
    "https://share.google/dHbp6caGIhLZVhp4Y",
    "https://www.google.com/maps?cid=5771542189821334782",
    "https://www.instagram.com/gebaeudewerke"
  ],
  "areaServed": [ "…siehe 3.2…" ],
  "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "07:00", "closes": "17:00"}],
  "contactPoint": [ "…wie bisher: customer service Mo bis Fr 7 bis 17 Uhr, emergency täglich 17:00 bis 23:59…" ],
  "employee": [{"@id": "https://gebaeudewerke.de/ueber-uns.html#person-fatih-altun"}, {"@id": "…#person-enes-yesildag"}, {"@id": "…#person-burak-kartal"}, {"@id": "…#person-julian-bender"}],
  "knowsAbout": ["Hausmeisterservice", "Treppenhausreinigung", "Gebäudereinigung", "Gartenpflege", "Winterdienst", "Räum- und Streupflicht", "Wohnungsübergabe", "Entrümpelung", "Kleinreparaturen", "Metallarbeiten", "Schließanlagen", "Betriebskostenverordnung"],
  "hasOfferCatalog": { "…wie bisher, plus Treppenhausreinigung und ggf. Büroreinigung…" },
  "aggregateRating": { "…siehe 3.3…" }
}
```

Hinweise:
* `geo` der Firma bleibt bei der **echten Anschrift** in Hambrücken (49.192062, 8.5403253). Würde man hier Bruchsaler Koordinaten eintragen, widersprächen sich `address` und `geo`. Google gleicht beides mit dem Profil ab. Der Bruchsal-Fokus wird über `areaServed`, Texte, geo-Meta-Tags (3.9) und Bild-`contentLocation` (3.8) hergestellt.
* `hasMap` und `sameAs`: bisher `https://share.google/v7XolrfYaCO55YrZz`. Dieser Link weicht vom Profil-Link in google-profil.json ab. Ersetzen (auch in sichtbaren „In Google Maps öffnen“-Links, insgesamt 39 Vorkommen im Ausgangsstand, und in `llms.txt`).
* Keine `priceRange` mit Fantasiewerten. Wenn gewünscht: `"priceRange": "ab 130 € netto im Monat"` (steht so auf der Seite).
* Telefon im Schema im internationalen Format, sichtbar national.

### 3.2 areaServed (Bruchsal zuerst)

```json
"areaServed": [
  {"@type": "City", "name": "Bruchsal", "sameAs": "https://de.wikipedia.org/wiki/Bruchsal"},
  {"@type": "Place", "name": "Bruchsal-Büchenau", "containedInPlace": {"@type": "City", "name": "Bruchsal"}},
  {"@type": "Place", "name": "Bruchsal-Heidelsheim", "containedInPlace": {"@type": "City", "name": "Bruchsal"}},
  {"@type": "Place", "name": "Bruchsal-Helmsheim", "containedInPlace": {"@type": "City", "name": "Bruchsal"}},
  {"@type": "Place", "name": "Bruchsal-Obergrombach", "containedInPlace": {"@type": "City", "name": "Bruchsal"}},
  {"@type": "Place", "name": "Bruchsal-Untergrombach", "containedInPlace": {"@type": "City", "name": "Bruchsal"}},
  {"@type": "City", "name": "Forst (Baden)"},
  {"@type": "City", "name": "Karlsdorf-Neuthard"},
  {"@type": "City", "name": "Ubstadt-Weiher"},
  {"@type": "City", "name": "Bad Schönborn"},
  {"@type": "City", "name": "Östringen"},
  {"@type": "City", "name": "Kronau"},
  {"@type": "City", "name": "Hambrücken"},
  {"@type": "City", "name": "Waghäusel"},
  {"@type": "City", "name": "Philippsburg"},
  {"@type": "City", "name": "Graben-Neudorf"},
  {"@type": "City", "name": "Stutensee"},
  {"@type": "City", "name": "Bretten"},
  {"@type": "AdministrativeArea", "name": "Landkreis Karlsruhe", "sameAs": "https://de.wikipedia.org/wiki/Landkreis_Karlsruhe"}
]
```

Wikipedia-`sameAs` je Gemeinde ist optional. Nur eintragen, wenn die URL geprüft ist (Forst heißt dort „Forst (Baden)“). Die Liste muss mit der sichtbaren Ortsliste auf `einsatzgebiet.html` übereinstimmen.

### 3.3 AggregateRating und Review (Entscheidung des Inhabers: wird eingebaut)

Der Inhaber hat nach Risikohinweis entschieden, AggregateRating und Review-Markup einzubauen. So wird es sauber und möglichst richtlinienkonform umgesetzt:

```json
"aggregateRating": {
  "@type": "AggregateRating",
  "ratingValue": "5.0",
  "bestRating": "5",
  "worstRating": "1",
  "ratingCount": "7",
  "reviewCount": "6"
}
```

Regeln:
1. **Werte exakt wie im Google-Profil** (google-profil.json): Schnitt 5,0, 7 Bewertungen. `ratingCount` = alle Bewertungen (7). `reviewCount` = Bewertungen mit Text (6, Ayse G hat keinen Text). Wer das vereinfachen will, setzt beide auf 7; dann muss aber auch die Bewertung ohne Text als Review im Markup stehen. Der Design-Agent hat derzeit `reviewCount: 7`. Beides ist vertretbar, wichtig ist die Übereinstimmung mit dem, was sichtbar ist.
2. **Sichtbar auf derselben Seite**: Schnitt und Anzahl stehen im Badge bzw. im Block „Kundenstimmen auf Google“ mit Quelle „Google“ und Stand-Datum. Markup ohne sichtbare Entsprechung ist ein Richtlinienverstoß.
3. **Nur am Firmenobjekt**, nicht an Service, Article oder WebPage. Auf jeder Seite dasselbe Objekt (über `@id`), nicht pro Seite andere Zahlen.
4. **Review-Einträge nur auf der Startseite**, wörtlich, mit Autor so wie auf Google angezeigt, Datum und Sternen:
   ```json
   "review": [{
     "@type": "Review",
     "author": {"@type": "Person", "name": "Daniela Azevedo"},
     "datePublished": "2026-10-14",
     "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
     "reviewBody": "Ich bin sehr zufrieden! Schon die Beratung war super freundlich, …",
     "publisher": {"@type": "Organization", "name": "Google"}
   }]
   ```
   Die Firmenbewertung „Türhelden Schlüsseldienst“ mit `author` vom Typ `Organization`. Emojis im Zitat dürfen bleiben (Originaltext), im übrigen Seitentext nicht.
5. **Pflege**: Bei jeder neuen Google-Bewertung Zahl, Schnitt, Badge, Block und Markup am selben Tag anpassen (google-profil.json als einzige Quelle; der Design-Agent hat dafür `werkzeuge/layout_anwenden.py` vorgesehen). Keine Bewertungen weglassen, die schlechter ausfallen.
6. Keine Bewertungen aus anderen Quellen mit Google-Zahlen vermischen.

Restrisiko in einem Satz: Google zeigt für selbst eingebundene Bewertungen eines LocalBusiness bzw. einer Organisation über sich selbst seit 2019 grundsätzlich keine Sterne in den Suchergebnissen an, das Markup bringt also voraussichtlich keine Sterne und kann bei Abweichungen von den sichtbaren Werten als irreführend gewertet werden (manuelle Maßnahme gegen strukturierte Daten möglich).

### 3.4 Service (je Leistungsseite)

```json
{
  "@type": "Service",
  "@id": "https://gebaeudewerke.de/hausmeisterservice.html#leistung",
  "name": "Hausmeisterservice in Bruchsal",
  "serviceType": "Hausmeisterservice",
  "description": "<Kurzantwort der Seite>",
  "provider": {"@id": "https://gebaeudewerke.de/#organisation"},
  "areaServed": "<gleiche Liste wie 3.2 oder Referenz auf Bruchsal + Landkreis>",
  "audience": {"@type": "BusinessAudience", "audienceType": "Hausverwaltungen, Eigentümergemeinschaften, Vermieter, Gewerbe"},
  "offers": {
    "@type": "AggregateOffer",
    "priceCurrency": "EUR",
    "lowPrice": "130",
    "priceSpecification": {"@type": "UnitPriceSpecification", "price": "130", "priceCurrency": "EUR", "unitText": "Monat", "valueAddedTaxIncluded": false}
  },
  "hasOfferCatalog": {"…Teilleistungen wie Kontrollgänge, Schlüsselverwaltung…"}
}
```

Preise nur dort, wo Richtpreise veröffentlicht sind: Hausmeisterservice (ab 130 €/Monat netto), Büro-Unterhaltsreinigung (ab 449 €/Monat netto), Fensterreinigung (ab 235 € netto), Winterdienst (ab 1.435 € netto/Saison), Mülltonnenservice (ab 90 € netto), Grünpflege und Heckenschnitt laut Tabelle. Treppenhausreinigung, Entrümpelung, Wohnungsübergabe, Kleinreparaturen, Metall: **ohne** `offers.price`.

Neue `serviceType`: „Treppenhausreinigung“ (treppenhausreinigung.html), „Büroreinigung“ (bueroreinigung.html). Einsatzgebiet-Seite: kein Service, sondern `WebPage` mit `about` → Organisation und `mentions` → Orte.

### 3.5 FAQPage

* Nur Fragen, die sichtbar auf der Seite stehen, wörtlich wie im `<summary>` bzw. in der H3.
* Keine Frage doppelt pro Seite (Kurz beantwortet + FAQ). Die Spezifikation entfernt die Dopplungen (Winterdienst „Haftung“, Kleinreparaturen „Abrechnung“, Metall „Zylinder“, „Schließanlage“).
* Google zeigt FAQ-Rich-Results seit 2023 nur noch für Behörden- und Gesundheitsseiten. Das Markup bleibt trotzdem sinnvoll, weil Suchmaschinen und KI-Systeme Frage-Antwort-Paare daraus sauber zuordnen.

### 3.6 BreadcrumbList

Wie sichtbar (siehe `interne-verlinkung.md` 4). Letztes Element mit `item` = eigene URL.

### 3.7 Article für Ratgeber (bisher BlogPosting)

```json
{
  "@type": "Article",
  "@id": "https://gebaeudewerke.de/ratgeber/raeum-und-streupflicht-bruchsal.html#artikel",
  "headline": "<H1>",
  "description": "<Meta-Description>",
  "datePublished": "2026-10-16",
  "dateModified": "<artikel-aktualisiert>",
  "inLanguage": "de-DE",
  "mainEntityOfPage": "https://gebaeudewerke.de/ratgeber/raeum-und-streupflicht-bruchsal.html",
  "image": {"@id": "https://gebaeudewerke.de/assets/img/fotos/winterdienst-bruchsal.webp#bild"},
  "author": {
    "@type": "Person",
    "@id": "https://gebaeudewerke.de/ueber-uns.html#person-julian-bender",
    "name": "Julian Bender",
    "jobTitle": "Gesellschafter, Hausmeisterservice und Winterdienst",
    "url": "https://gebaeudewerke.de/ueber-uns.html#team",
    "worksFor": {"@id": "https://gebaeudewerke.de/#organisation"}
  },
  "publisher": {"@id": "https://gebaeudewerke.de/#organisation"},
  "about": "Räum- und Streupflicht",
  "isPartOf": {"@id": "https://gebaeudewerke.de/ratgeber/#webseite"},
  "citation": ["Streupflichtsatzung der Stadt Bruchsal", "https://www.gesetze-im-internet.de/bgb/__823.html"]
}
```

* `BlogPosting` geht auch, `Article` passt für Fachratgeber besser.
* Autor-Name ohne Zusatz „, Gebäudewerke“ (bisher `"name": "Burak Kartal, Gebäudewerke"`). Die Firma steht in `worksFor`.
* `datePublished` muss mit `artikel-datum` übereinstimmen, `dateModified` mit `artikel-aktualisiert`. Beides sichtbar im Kopf (siehe textaenderungen.md 16.1).
* `citation` nur mit den Quellen, die auf der Seite in der Quellenzeile stehen. Offizielle Links: `quelle_offiziell` in `seiten-spezifikation.json`. Für die Bruchsaler Satzung und die LBO BW nur einen Link setzen, wenn die URL vorher im Browser geprüft wurde.

### 3.8 ImageObject mit contentLocation

Für Hero- und Artikelbilder:

```json
{
  "@type": "ImageObject",
  "@id": "https://gebaeudewerke.de/assets/img/fotos/winterdienst-bruchsal.webp#bild",
  "contentUrl": "https://gebaeudewerke.de/assets/img/fotos/winterdienst-bruchsal.webp",
  "width": 1200,
  "height": 900,
  "caption": "<alt_neu aus alt-texte.json>",
  "contentLocation": {
    "@type": "Place",
    "name": "Bruchsal",
    "address": {"@type": "PostalAddress", "addressLocality": "Bruchsal", "postalCode": "76646", "addressRegion": "Baden-Württemberg", "addressCountry": "DE"},
    "geo": {"@type": "GeoCoordinates", "latitude": 49.1291927, "longitude": 8.5914434}
  },
  "creditText": "<Fotograf/Stockquelle>",
  "copyrightNotice": "<Lizenzhinweis>"
}
```

* Koordinaten 49.1291927, 8.5914434 = Mittelpunkt des Einsatzgebiets im Google-Profil (Vorgabe des Inhabers). Für Logo und Social-Vorschaubild kein `contentLocation`.
* Ehrlicher Hinweis: `contentLocation` bedeutet „Ort, der auf dem Bild zu sehen ist“. Alle aktuellen Fotos sind Stockfotos und nicht in Bruchsal entstanden. Das Signal ist schwach und semantisch ungenau. Sobald eigene Fotos aus Bruchsaler Objekten vorliegen (Empfehlung in `offpage-und-gbp.md`), passt die Angabe wirklich. Bis dahin `creditText` und Lizenzangaben pflegen, damit die Herkunft sauber ist.
* EXIF-GPS übernimmt der Koordinator.

### 3.9 geo-Meta-Tags

Vorher (alle Seiten): `geo.placename = Hambrücken`, `geo.position = 49.192062;8.5403253`, `ICBM = 49.192062, 8.5403253`.

Nachher:
```html
<meta name="geo.region" content="DE-BW">
<meta name="geo.placename" content="Bruchsal">
<meta name="geo.position" content="49.1291927;8.5914434">
<meta name="ICBM" content="49.1291927, 8.5914434">
```
Die Tags beschreiben das Zielgebiet der Seite, nicht die Firmenanschrift. Google wertet sie kaum aus, andere Dienste und manche KI-Crawler schon. Die Firmen-`geo` im Schema bleibt bei der Anschrift (3.1). Diese Trennung (Zielgebiet in Meta und Bildern, Anschrift im Firmenobjekt) ist bewusst so gewählt und wird hier dokumentiert.

### 3.10 Person (Über uns)

```json
{
  "@type": "Person",
  "@id": "https://gebaeudewerke.de/ueber-uns.html#person-fatih-altun",
  "name": "Fatih Altun",
  "jobTitle": "Gesellschafter, Metall- und Schlosserarbeiten",
  "worksFor": {"@id": "https://gebaeudewerke.de/#organisation"},
  "hasCredential": {"@type": "EducationalOccupationalCredential", "credentialCategory": "Meisterbrief", "name": "Geprüfter Industriemeister Metall (IHK)"},
  "knowsAbout": ["Metallarbeiten", "Schließanlagen", "Kleinreparaturen"]
}
```
Analog:
* Enes Yesildag: jobTitle „Gesellschafter, Vertrieb, Hausverwaltung und Wohnungsübergaben“, `hasOccupation` bzw. Beschreibung „Kaufmann“, knowsAbout Hausverwaltung, Wohnungsübergabe, Betriebskosten.
* Burak Kartal: jobTitle „Gesellschafter, Qualität, Reinigung und Gartenpflege“, hasCredential „Metallbauer (Ausbildung)“ mit credentialCategory „Berufsabschluss“, knowsAbout Gebäudereinigung, Gartenpflege, Qualitätsmanagement.
* Julian Bender: jobTitle „Gesellschafter, Hausmeisterservice und Winterdienst“, hasCredential „Industriemechaniker (Ausbildung)“, knowsAbout Hausmeisterservice, Winterdienst, Haustechnik.

`@id` sprechend statt `#person-1` bis `#person-4` (dann überall gleich verwenden). Keine Fotos im Schema, solange keine echten Teamfotos existieren.

### 3.11 Weitere

* `WebSite` ohne `SearchAction` (keine Suche vorhanden).
* `JobPosting` auf karriere.html nur, wenn die Stellen tatsächlich offen sind und Beschäftigungsart, Arbeitsort (Bruchsal) und Datum feststehen. Sonst weglassen, sonst drohen Abwertungen in Google for Jobs.
* `ContactPage` (Kontakt), `AboutPage` (Über uns), `CollectionPage` (Ratgeber) beibehalten.
* `og:image:alt` auf allen Seiten ergänzen (Text in alt-texte.json).

## 4. robots.txt

### 4.1 Fehler

1. **Gruppen überschreiben sich.** Ein Crawler folgt nur der spezifischsten Gruppe, die zu seinem Namen passt. GPTBot, ClaudeBot, PerplexityBot, Bingbot usw. haben eigene Gruppen mit nur `Allow: /`. Für sie gelten die `Disallow`-Zeilen der `*`-Gruppe also nicht. Bingbot darf damit `/anfrage.php`, `/einrichtung.php`, `/htaccess.txt` abrufen.
2. **Widerspruch Sperre und noindex.** `404.html`, `danke.html`, `anfrage-fehler.html` sind per `Disallow` gesperrt und tragen `noindex`. Gesperrte Seiten werden nicht abgerufen, das `noindex` wird nie gelesen. Wenn eine solche URL irgendwo verlinkt ist, kann sie ohne Inhalt („Keine Informationen verfügbar“) im Index landen.
3. `Allow: /` direkt nach dem ersten `Disallow` ist überflüssig.
4. `/ratgeber/_vorlage-beitrag.html` liegt nicht im Paket, die Zeile schadet aber nicht.

### 4.2 Neue robots.txt

```
# Gebäudewerke, robots.txt, Stand 2026-10-31

User-agent: *
User-agent: GPTBot
User-agent: OAI-SearchBot
User-agent: ChatGPT-User
User-agent: ClaudeBot
User-agent: Claude-SearchBot
User-agent: Claude-User
User-agent: PerplexityBot
User-agent: Perplexity-User
User-agent: Google-Extended
User-agent: Applebot-Extended
User-agent: Bingbot
Disallow: /auslieferung.php
Disallow: /anfrage.php
Disallow: /einrichtung.php
Disallow: /htaccess.txt
Disallow: /ratgeber/_vorlage-beitrag.html

Sitemap: https://gebaeudewerke.de/sitemap.xml
Sitemap: https://gebaeudewerke.de/ratgeber/sitemap.php
```

* Mehrere `User-agent`-Zeilen über einer Regelgruppe sind Standard (RFC 9309) und werden von Google, Bing und den KI-Crawlern verstanden. Damit sind die KI-Dienste weiterhin ausdrücklich genannt und bekommen dieselben Regeln.
* `404.html`, `danke.html`, `anfrage-fehler.html` **nicht sperren**. Sie behalten `noindex` (Meta) bzw. `X-Robots-Tag: noindex` (404 über auslieferung.php). Zusätzlich auf diesen drei Seiten das `<link rel="canonical">` entfernen (es zeigt heute auf sich selbst und widerspricht noindex nicht direkt, ist aber überflüssig).
* Impressum und Datenschutz bleiben `noindex, follow`. Für lokales Vertrauen wäre ein indexiertes Impressum leicht vorteilhaft (Name, Anschrift, Vertretung). Empfehlung: Impressum auf `index, follow` stellen, Datenschutz `noindex`. Optional, keine Pflicht.

## 5. Sitemaps

* `sitemap.xml`: neue Seiten `einsatzgebiet.html`, `treppenhausreinigung.html` (und ggf. `bueroreinigung.html`) ergänzen. `lastmod` nur ändern, wenn sich der Inhalt wirklich ändert. `priority` kann weg (wird ignoriert).
* `ratgeber/sitemap.php` funktioniert (nur veröffentlichte Artikel, `lastmod` aus `artikel-aktualisiert`). Header `X-Robots-Tag: noindex` für die Sitemap selbst ist nicht nötig.
* Optional ein Sitemap-Index (`sitemap-index.xml`), der beide Sitemaps einbindet. Pflicht ist das nicht, robots.txt nennt beide.
* Search Console und Bing Webmaster Tools: beide Sitemaps einreichen. Bing speist ChatGPT-Suche und Copilot, das ist für die KI-Sichtbarkeit wichtig. IndexNow für Bing nach jeder Änderung (OpenSEO bietet `submit_indexnow_urls`).

## 6. Performance und Core Web Vitals

Ausgangslage: HTML 47 bis 82 KB je Seite, davon ca. 62 KB Inline-CSS. Antwortzeit laut Seobility 0,10 s, gzip aktiv, HTTP/2. Schrift `archivo-var.woff2` (56 KB) mit `preload` und `font-display: optional`. Hero-Bilder 1200 px WebP um 100 KB mit `-klein`-Variante, `width`/`height` gesetzt, `fetchpriority="high"`. Karte erst nach Klick. Das ist eine gute Basis.

Empfehlungen:
1. **CSS auslagern.** `assets/css/style.css` existiert. 62 KB Inline-CSS in jeder Seite bedeuten, dass jede Unterseite das komplette CSS neu lädt. Besser: nur das Above-the-fold-CSS inline (etwa 8 bis 12 KB), Rest als externe, ein Jahr gecachte Datei mit Versionsparameter.
2. **Bewertungs-Laufband**: horizontale Animation muss `prefers-reduced-motion` respektieren und darf keine Layoutverschiebung auslösen (feste Höhe reservieren). Keine Google-Widgets von außen einbinden (Datenschutz, Ladezeit), die Daten liegen lokal in google-profil.json.
3. **Hero-Bild mobil**: `sizes` so setzen, dass auf Mobilgeräten die 800-px-Variante geladen wird (bei Artikeln vorhanden, auf Leistungsseiten prüfen).
4. **HSTS-Header** ergänzen: `Strict-Transport-Security: max-age=31536000` in htaccess.txt.
5. **Cache für HTML** steht auf `no-cache`. Für statische Seiten ist das unnötig streng, wegen der zeitgesteuerten Ratgeberlinks aber vertretbar. Belassen.
6. Server-Standort meldet Seobility als USA (vermutlich CDN/Proxy bei IONOS). Für das Ranking unerheblich, nur zur Kenntnis.

## 7. Name, Adresse, Telefon (NAP) und Google-Profil

| Merkmal | Website | Google-Profil | Empfehlung |
|---|---|---|---|
| Name | Gebäudewerke / Gebäudewerke GbR | Gebäudewerke - Hausmeisterservice & Gebäudereinigung | Siehe unten |
| Anschrift | Allmend 2, 76707 Hambrücken | ausgeblendet (Gebiets-Unternehmen) | so lassen, Website darf die Anschrift zeigen |
| Telefon | 0163 7221790 (uneinheitlich geschrieben) | +49 163 7221790 | gleiche Nummer, Schreibweise vereinheitlichen |
| Öffnungszeiten | Mo bis Fr 7 bis 17 Uhr, Notdienst 17 bis 24 Uhr | Mo bis Fr 07:00 bis 17:00 | gleich. Notdienst nicht als Öffnungszeit ins Profil, weil dann „geöffnet“ bis 24 Uhr angezeigt wird. |
| Website-Link im Profil | | Startseite | so lassen |
| Kategorien | Hausmeisterservice, Reinigung, Garten, Entrümpelung, Winterdienst | Hausmeisterservice + 4 | passt |

**Profilname:** Die Google-Richtlinien verlangen den Namen, den das Unternehmen im echten Leben führt (Schild, Briefkopf, Rechnung). Zusätze wie „Hausmeisterservice & Gebäudereinigung“ sind nur erlaubt, wenn sie fester Bestandteil des Markennamens sind. Auf der Website heißt die Firma durchgehend „Gebäudewerke“ mit der Unterzeile „Objekt- und Gebäudeservice“. Damit wirkt der Profilname wie Keyword-Zusatz. Risiko: Wettbewerber melden das, Google ändert den Namen oder sperrt das Profil vorübergehend. Zwei saubere Wege:
1. Profilname auf „Gebäudewerke“ ändern (sicher, kurzfristig etwas weniger Relevanz).
2. Den Zusatz wirklich zum Markennamen machen: auf Fahrzeug, Briefkopf, Rechnung, Website-Logo-Unterzeile, Impressum (als Geschäftsbezeichnung) einheitlich „Gebäudewerke Hausmeisterservice & Gebäudereinigung“. Dann im Schema `name` so setzen.
Entscheidung beim Inhaber. Bis dahin steht der Profilname als `alternateName` im Schema (3.1).

## 8. llms.txt

Die Datei ist gut gegliedert. Zu ändern:
1. Ortsfokus: erster Absatz „… ist ein Objekt- und Gebäudeservice für Bruchsal und den Landkreis Karlsruhe (Firmensitz: Allmend 2, 76707 Hambrücken) …“ statt „mit Sitz in Hambrücken bei Bruchsal“.
2. Profil-Link auf `https://share.google/dHbp6caGIhLZVhp4Y`, zusätzlich Maps-CID-Link.
3. Neue Zeilen: `Google-Bewertungen: 5,0 von 5 bei 7 Bewertungen (Stand 31.10.2026)`, `Team: Fatih Altun (Gesellschafter, geprüfter Industriemeister Metall IHK), Enes Yesildag (Gesellschafter, Kaufmann, Vertrieb und Hausverwaltung), Burak Kartal (Gesellschafter, Metallbauer, Qualität, Reinigung und Gartenpflege), Julian Bender (Gesellschafter, Industriemechaniker, Hausmeisterservice und Winterdienst)`.
4. Ortsliste einheitlich (textaenderungen.md 2.5) und Verweis auf `https://gebaeudewerke.de/einsatzgebiet.html`.
5. Neue Leistungsseiten (Treppenhausreinigung, ggf. Büroreinigung) mit je einer Kurzantwort und Quelle.
6. Telefon als `0163 7221790` und `+49 163 7221790`.
7. Gedankenstriche entfernen, Formulierungen wie in den Kurzantworten der Seiten.
8. Jeder Ratgeberlink in einer eigenen Zeile (auslieferung.php löscht künftige Artikel zeilenweise).
9. Optional `llms-full.txt` nicht anlegen, der Mehrwert ist gering.

## 9. Bilder

* Alt-Texte: `alt-texte.json` (74 Bilddateien, Logos, Social-Bild). Wichtigste Korrekturen: hausmeisterservice-bruchsal (gibt Stockfoto als eigenen Hausmeister aus), kleinreparaturen-bruchsal im Ratgeber (beschreibt eine Pumpe, die nicht zu sehen ist), kosten-hausmeisterservice auf preise.html, wohnungsuebergabe-protokoll (verortet Haus in Bruchsal).
* Dateinamen sind sprechend und enthalten Leistung und Ort. Umbenennen ist nicht nötig und würde Links brechen.
* Zwei Bilder passen inhaltlich nicht: ortstermin-angebot (Autohaus) und streugut-entfernen (Birke ohne Streugut). Ersetzen, am besten durch eigene Fotos.
* Langfristig eigene Fotos (Team, Fahrzeug, Objekte vorher/nachher). Eigene Fotos sind für E-E-A-T, Google-Profil und Bildersuche deutlich stärker als Stockfotos.

## 10. E-E-A-T technisch

| Signal | Umsetzung |
|---|---|
| Wer steckt dahinter | Person-Schema mit `jobTitle`, `worksFor`, `hasCredential` (3.10), sichtbare Teamkarten |
| Autorenschaft | Article.author als Person mit `@id` auf Über uns, sichtbare Autorenbox (textaenderungen.md 16.1) |
| Aktualität | `datePublished`/`dateModified` = sichtbare Daten im Artikelkopf |
| Quellen | Quellenzeile mit Links auf gesetze-im-internet.de, `citation` im Schema |
| Haftung und Erreichbarkeit | Impressum mit Gesellschaftern, Vertretung, Betriebshaftpflicht; Kontaktpunkte im Schema |
| Fremdbewertung | Google-Bewertungen sichtbar mit Link zum Profil, Markup nach 3.3 |
| Konsistenz | NAP überall gleich (Abschnitt 7) |

## 11. Prüfliste nach dem Umbau (Ahrefs/Seobility/rankingCoach-Kriterien)

* [ ] Jede indexierbare Seite: genau ein `<title>`, eine Meta-Description, eine H1, Canonical auf sich selbst.
* [ ] Keine doppelten Titles/Descriptions (Spezifikation ist eindeutig).
* [ ] Keine internen Links auf 3xx/4xx, keine relativen Ratgeberlinks.
* [ ] Alle Bilder mit `alt`, `width`, `height`; dekorative Bilder `alt=""`.
* [ ] Strukturierte Daten im Rich-Results-Test und Schema-Validator fehlerfrei; AggregateRating-Werte = sichtbare Werte = google-profil.json.
* [ ] robots.txt neu, Sitemaps eingereicht (Google und Bing).
* [ ] `noindex`-Seiten nicht in Sitemaps und nicht gesperrt.
* [ ] NAP auf allen Seiten gleich geschrieben.
* [ ] PageSpeed Insights mobil: LCP unter 2,5 s, CLS unter 0,1, INP unter 200 ms.
* [ ] Google Search Console: Domain-Property, Abdeckung prüfen, besonders winterdienst.html und hausmeisterservice.html (Ratgeber-Übersicht rankt aktuell statt der Leistungsseite).
