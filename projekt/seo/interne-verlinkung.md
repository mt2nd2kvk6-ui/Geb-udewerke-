# Interne Verlinkung

Ziel: Jede Leistungsseite bekommt Links mit beschreibendem Ankertext von Startseite, Navigation, Footer, passenden Ratgebern, Preisen und Einsatzgebiet. Ratgeber verweisen nach oben auf genau eine Leistungsseite (die „Geldseite“ des Themas) und seitwärts auf zwei bis drei verwandte Artikel. Alle Ankertexte variieren leicht, damit nicht überall derselbe exakte Suchbegriff steht.

## 1. Technische Regeln wegen `auslieferung.php`

`auslieferung.php` entfernt Links auf Ratgeberartikel mit Datum in der Zukunft. Es erkennt nur diese drei Formen:

1. `<li><a … href="/ratgeber/x.html" …>…</a></li>` wird komplett entfernt.
2. `<p><a … href="/ratgeber/x.html" …>…</a></p>` wird komplett entfernt.
3. Jedes andere `<a … href="/ratgeber/x.html" …>Text</a>` wird zu `Text` (Link weg, Text bleibt).

Daraus folgen feste Bauregeln:

| Regel | Grund |
|---|---|
| `href` immer als `/ratgeber/slug.html` (absolut ab Wurzel) oder `https://gebaeudewerke.de/ratgeber/slug.html`. Kein `../ratgeber/…`, kein `./slug.html`, kein `slug.html` innerhalb von `/ratgeber/`. | Das Muster erkennt nur `(https://gebaeudewerke.de)?/?ratgeber/slug.html`. Relative Pfade wie `slug.html` oder `../` würden nicht entfernt und auf eine 404 zeigen. |
| `<li>` und `<p>` ohne Attribute direkt vor `<a` schreiben: `<li><a href="…">`. Kein `<li class="…">`, kein Leerzeichen oder Zeilenumbruch zwischen `<li>` und `<a`. Ebenso `</a></li>` ohne Zwischenraum. | Sonst greift nur Regel 3, und es bleibt ein leerer oder reiner Text-Listenpunkt stehen. |
| In Listen-Links nichts außer dem Linktext: kein Datum, kein Teaser, kein Bild im selben `<li>` außerhalb des `<a>`. Teaser oder Datum gehören **in** das `<a>`. | Siehe oben. |
| Listen ohne Leerraum zwischen den Einträgen bauen (`<ul class="weitere"><li>…</li><li>…</li></ul>`) und als letzten Eintrag immer einen Link auf ein **veröffentlichtes** Ziel setzen, z. B. `<li><a href="/ratgeber/">Alle Ratgeberbeiträge</a></li>`. | Der Ersatz für leere Listen greift nur bei exakt `<ul class="weitere"></ul>` oder `<ul></ul>`. Mit dem festen letzten Eintrag kann die Liste nie leer werden. |
| Karten mit Bild (Teaser-Kacheln) nur für bereits veröffentlichte Artikel oder über `ratgeber/index.php` (das filtert selbst). | Kacheln aus `<div>`/`<article>` werden nicht entfernt, nur ihr Link wird zu Text. Übrig bliebe eine Karte ohne Ziel. |
| Inline-Links im Fließtext auf künftige Artikel nur in Sätzen, die ohne Link genauso lesbar sind. Nicht: „Mehr dazu <a>hier</a>.“ | Regel 3 macht aus „hier“ ein loses Wort. |
| Keine Links auf künftige Artikel in JSON-LD, `<link rel>`, Buttons (`<a class="btn">` außerhalb von `<li>`/`<p>`) oder Navigation. | Werden nicht oder nur teilweise bereinigt. |
| `llms.txt`: jeder Ratgeberlink in einer eigenen Zeile. | `auslieferung.php` löscht dort ganze Zeilen mit dem Slug. |

Veröffentlichungsdaten (aus `ratgeber/plan.json`), Stand 31.10.2026:
* **live:** bauendreinigung, bueroreinigung-praxisreinigung, entruempelung-ablauf, gartenpflege-jahresvertrag, glasreinigung, hausmeisterkosten-umlagefaehig, hecke-schneiden-erlaubt, kleinreparaturen, laub-gehweg-pflicht (31.10.), muelltonnendienst, raeum-und-streupflicht, schluesselverwaltung, stoerungsmeldung-gewerbeobjekt, streugut-entfernen-fruehjahr, streuprotokoll-winterdienst, tiefgarage-keller-reinigung, treppenhausreinigung, unkraut-pflaster-entfernen, winterdienst-beauftragen, wohnungsuebergabe-protokoll
* **geplant:** ortstermin-angebot (03.11.), zaehlerstaende-ablesen (06.11.), hausmeisterservice-hausverwaltung (10.11.), sturmschaden-kontrolle (13.11.), besichtigung-vorbereiten (17.11.), grundreinigung-gewerbeboden (20.11.), handwerkerkoordination (24.11.), kosten-hausmeisterservice (27.11.), hausmeisterservice-weg (01.12.), dienstleister-wechseln (08.12.), treppenhaus-rettungsweg (15.12.)

## 2. Navigation

Hauptnavigation (Desktop und Mobil), Reihenfolge nach Nachfrage und Umsatz:

1. **Leistungen** (Aufklapper)
   * Hausmeisterservice → `/hausmeisterservice.html`
   * Treppenhausreinigung → `/treppenhausreinigung.html` (sobald live)
   * Gebäudereinigung → `/gebaeudereinigung.html`
   * Büroreinigung → `/bueroreinigung.html` (nur wenn gebaut)
   * Gartenpflege → `/gartenpflege.html`
   * Winterdienst → `/winterdienst.html`
   * Entrümpelung und Haushaltsauflösung → `/entruempelung.html`
   * Wohnungsübergabe → `/wohnungsuebergabe.html`
   * Kleinreparaturen → `/kleinreparaturen.html`
   * Metallarbeiten und Schlösser → `/metallarbeiten-schloesser.html`
2. **Preise** → `/preise.html`
3. **Einsatzgebiet** → `/einsatzgebiet.html`
4. **Ratgeber** → `/ratgeber/`
5. **Über uns** → `/ueber-uns.html`
6. **Kontakt** → `/kontakt.html` (als Button „Angebot anfragen“)

Karriere wandert aus der Hauptnavigation in den Footer. Die bisherigen langen Navigationsnamen („Hausmeisterservice und Objektbetreuung“, „Gebäudereinigung und Treppenhausreinigung“ …) werden kürzer, weil Treppenhaus eine eigene Seite bekommt.

## 3. Footer

| Spalte | Links (Ankertext → Ziel) |
|---|---|
| Leistungen in Bruchsal | Hausmeisterservice Bruchsal → hausmeisterservice.html · Treppenhausreinigung → treppenhausreinigung.html · Gebäudereinigung Bruchsal → gebaeudereinigung.html · Gartenpflege Bruchsal → gartenpflege.html · Winterdienst Bruchsal → winterdienst.html · Entrümpelung Bruchsal → entruempelung.html · Wohnungsübergabe mit Protokoll → wohnungsuebergabe.html · Handwerkerservice → kleinreparaturen.html · Schlösser und Metallarbeiten → metallarbeiten-schloesser.html |
| Unternehmen | Preise und Richtpreise → preise.html · Einsatzgebiet → einsatzgebiet.html · Team und Unternehmen → ueber-uns.html · Ratgeber → /ratgeber/ · Jobs bei Gebäudewerke → karriere.html · Kontakt und Anfahrt → kontakt.html |
| Erreichbarkeit | Telefon 0163 7221790 · WhatsApp · E-Mail · Bürozeiten · Notdienst · Bewertungen auf Google → https://share.google/dHbp6caGIhLZVhp4Y |
| Rechtliches | Impressum · Datenschutz · Cookie-Einstellungen |

Der Footer-Link „Häufige Fragen“ (`/#fragen`) entfällt, er ist für Nutzer wenig hilfreich.

## 4. Breadcrumbs (sichtbar und als BreadcrumbList)

| Seitentyp | Pfad |
|---|---|
| Leistungsseite | Startseite › Leistungen › Hausmeisterservice |
| Preise | Startseite › Preise |
| Einsatzgebiet | Startseite › Einsatzgebiet |
| Über uns, Kontakt, Karriere | Startseite › Über uns (usw.) |
| Ratgeber-Übersicht | Startseite › Ratgeber |
| Ratgeberartikel | Startseite › Ratgeber › Kurzname des Artikels |

„Leistungen“ verlinkt auf `/#leistungen` (es gibt keine eigene Leistungsübersicht). Im BreadcrumbList-Schema wird „Leistungen“ weggelassen oder ebenfalls mit `/#leistungen` geführt; einheitlich halten. Die Ratgeber-Brotkrume heißt sichtbar „Ratgeber“ (bisher „Ratgeber-Übersicht“), wie im Schema.

## 5. Linkmatrix Leistungsseiten

Format: Ankertext → Ziel. „Kontext“ = Fließtext, „Block“ = eigener Linkblock.

### 5.1 Startseite (`/`)

| Ziel | Ankertext | Ort |
|---|---|---|
| hausmeisterservice.html | Hausmeisterservice für Wohnanlagen und Gewerbe | Leistungskachel (H3) |
| hausmeisterservice.html | Hausmeisterservice im Detail | Abschnitt „Auf einen Blick“ |
| treppenhausreinigung.html | Treppenhausreinigung nach festem Plan | neue Kachel oder Link unter Kachel Gebäudereinigung |
| gebaeudereinigung.html | Gebäudereinigung für Treppenhaus, Büro und Glas | Kachel |
| gartenpflege.html | Gartenpflege und Außenanlagen | Kachel |
| winterdienst.html | Winterdienst mit Einsatzprotokoll | Kachel |
| entruempelung.html | Entrümpelung und Haushaltsauflösung | Kachel |
| wohnungsuebergabe.html | Wohnungsübergabe und Abnahme mit Protokoll | Kachel |
| kleinreparaturen.html | Kleinreparaturen, Montage und Renovierung | Kachel |
| metallarbeiten-schloesser.html | Metallarbeiten, Tore und Schließanlagen | Kachel |
| preise.html | Richtpreise ansehen | Abschnitt „Auf einen Blick“ + „Preise, die gelten“ |
| einsatzgebiet.html | Alle Orte im Einsatzgebiet | Ortsabschnitt |
| ueber-uns.html | Mehr über das Team | Team-Abschnitt |
| /ratgeber/raeum-und-streupflicht-bruchsal.html | Räum- und Streupflicht in Bruchsal | neuer Block „Aus dem Ratgeber“ (`<ul class="weitere">`, 3 Einträge, nur live-Artikel) |
| /ratgeber/hausmeisterkosten-umlagefaehig.html | Welche Hausmeisterkosten umlagefähig sind | dito, außerdem in FAQ-Antwort „umlagefähig“ |
| /ratgeber/wohnungsuebergabe-protokoll-bruchsal.html | Übergabeprotokoll beim Mieterwechsel | dito |
| kontakt.html | Anfrage senden / Ortstermin anfragen | Hero, CTA |

### 5.2 Leistungsseiten untereinander und zu Preisen/Ratgeber

| Von | Ankertext → Ziel (Kontext) | Block „Passende Ratgeber“ (Reihenfolge, live zuerst) | Block „Weitere Leistungen“ |
|---|---|---|---|
| hausmeisterservice.html | „Übergabe und Abnahme beim Mieterwechsel“ → wohnungsuebergabe.html · „Treppenhausreinigung“ → treppenhausreinigung.html (Absatz „Ihr Hausmeister …“) · „Alle Richtpreise zur Objektbetreuung“ → preise.html#objektbetreuung · „alle Orte“ → einsatzgebiet.html (H3 Orte) · „welche Hausmeisterkosten umlagefähig sind“ → /ratgeber/hausmeisterkosten-umlagefaehig.html | Hausmeisterkosten: was umlagefähig ist · Schlüsselverwaltung im Mehrfamilienhaus · Störungen im Gewerbeobjekt melden · Zählerstände zum Jahreswechsel (ab 06.11.) · Hausmeisterservice für Hausverwaltungen (ab 10.11.) · Handwerkertermine koordinieren (ab 24.11.) · Was ein Hausmeisterservice kostet (ab 27.11.) · Hausmeister für die WEG (ab 01.12.) · Dienstleister wechseln (ab 08.12.) · Alle Ratgeberbeiträge | alle anderen Leistungen, Treppenhausreinigung an erster Stelle |
| treppenhausreinigung.html (neu) | „Hausmeisterservice in Bruchsal“ → hausmeisterservice.html · „Keller und Tiefgarage“ → gebaeudereinigung.html · „Preise“ → preise.html#unterhaltsreinigung | Reinigungsplan fürs Treppenhaus · Glasreinigung im Treppenhaus · Tiefgarage und Keller reinigen · Treppenhaus als Rettungsweg (ab 15.12.) · Alle Ratgeberbeiträge | Hausmeisterservice, Gebäudereinigung, Winterdienst, Gartenpflege |
| gebaeudereinigung.html | „Treppenhausreinigung in Bruchsal“ → treppenhausreinigung.html · „Büroreinigung“ → bueroreinigung.html (wenn gebaut) · „Richtpreise Fensterreinigung“ → preise.html#fenster · „Richtpreise Unterhaltsreinigung“ → preise.html#unterhaltsreinigung | Reinigungsplan fürs Treppenhaus · Tiefgarage und Keller reinigen · Glasreinigung: wie oft · Büroreinigung außerhalb der Öffnungszeiten · Bauendreinigung · Grundreinigung von Gewerbeböden (ab 20.11.) · Alle Ratgeberbeiträge | Treppenhausreinigung, Hausmeisterservice, Wohnungsübergabe, Gartenpflege, Winterdienst, Entrümpelung, Kleinreparaturen, Metall |
| gartenpflege.html | „Hausmeisterservice mit festem Betreuer“ → hausmeisterservice.html · „Winterdienst“ → winterdienst.html · „Richtpreise Grünpflege“ → preise.html#gruenpflege · „Wann darf man Hecken schneiden?“ → /ratgeber/hecke-schneiden-erlaubt.html (FAQ-Antwort) | Gartenpflege im Jahresvertrag · Hecke schneiden: was erlaubt ist · Unkraut auf Pflaster · Laub auf dem Gehweg · Alle Ratgeberbeiträge | Winterdienst, Hausmeisterservice, … |
| winterdienst.html | „Gartenpflege für Wohnanlagen“ → gartenpflege.html · „Richtpreise Winterdienst“ → preise.html#winterdienst · „Räum- und Streupflicht in Bruchsal“ → /ratgeber/raeum-und-streupflicht-bruchsal.html (FAQ „Bis wann muss …“) | Räum- und Streupflicht in Bruchsal · Räum- und Streuprotokoll · Winterdienst rechtzeitig beauftragen · Streugut entfernen im Frühjahr · Laub auf dem Gehweg · Alle Ratgeberbeiträge | Hausmeisterservice, Gartenpflege, … |
| entruempelung.html | „Kleinreparaturen, Streichen und Montage“ → kleinreparaturen.html · „Wohnungsübergabe mit Protokoll“ → wohnungsuebergabe.html · „Preisseite“ → preise.html#ohne-richtpreis | So läuft eine Entrümpelung ab · Mülltonnendienst · Bauendreinigung · Alle Ratgeberbeiträge | Gebäudereinigung, Kleinreparaturen, Wohnungsübergabe, … |
| wohnungsuebergabe.html | „Kleinreparaturen, Streichen und Montage“ → kleinreparaturen.html · „Entrümpelung“ → entruempelung.html · „Übergabeprotokoll beim Mieterwechsel“ → /ratgeber/wohnungsuebergabe-protokoll-bruchsal.html (Einleitung, Inline) | Übergabeprotokoll beim Mieterwechsel · Schlüsselverwaltung · Zählerstände zum Jahreswechsel (ab 06.11.) · Besichtigung vorbereiten (ab 17.11.) · Alle Ratgeberbeiträge | Kleinreparaturen, Gebäudereinigung, Entrümpelung, Hausmeisterservice |
| kleinreparaturen.html | „Hausmeisterservice“ → hausmeisterservice.html · „Metallarbeiten und Schlösser“ → metallarbeiten-schloesser.html | Kleinreparaturen bündeln · Störungen im Gewerbeobjekt · Handwerkertermine koordinieren (ab 24.11.) · Sturmschaden kontrollieren (ab 13.11.) · Alle Ratgeberbeiträge | Metall, Wohnungsübergabe, Hausmeisterservice, … |
| metallarbeiten-schloesser.html | „Schlüsselverwaltung im Mehrfamilienhaus“ → /ratgeber/schluesselverwaltung-bruchsal.html · „Kleinreparaturen“ → kleinreparaturen.html | Schlüsselverwaltung im Mehrfamilienhaus · Kleinreparaturen bündeln · Alle Ratgeberbeiträge | Kleinreparaturen, Hausmeisterservice, … |
| preise.html | je Preisabschnitt „Zur Leistung …“ → Leistungsseite (vorhanden) · neu: Unterhaltsreinigung → „Treppenhausreinigung“ → treppenhausreinigung.html | Abschnitt Objektbetreuung: „Was kostet ein Hausmeisterservice?“ → /ratgeber/kosten-hausmeisterservice-bruchsal.html (ab 27.11., als `<li>` in der vorhandenen Linkliste, wird bis dahin automatisch entfernt) · Fenster → Glasreinigung · Grünpflege → Jahresvertrag · Hecke → Hecke schneiden · Mülltonnen → Mülltonnendienst · Winterdienst → Winterdienst beauftragen | |
| einsatzgebiet.html (neu) | alle Leistungsseiten (Liste „Welche Leistungen es überall gibt“) · „Kontakt“ → kontakt.html · „Räum- und Streupflicht in Bruchsal“ → Ratgeber (Abschnitt Touren) | | |
| ueber-uns.html | je Teamkarte 2 Ratgeber (siehe textaenderungen.md 12.3, nur live-Artikel) · Zuständigkeiten → jeweilige Leistungsseite (z. B. „Türen, Tore und Schließanlagen“ → metallarbeiten-schloesser.html) | | |
| kontakt.html | „Einsatzgebiet“ → einsatzgebiet.html · „Richtpreise“ → preise.html · „So läuft der Ortstermin ab“ → /ratgeber/ortstermin-angebot-hausmeisterservice.html (ab 03.11., als `<p><a>`) | | |

### 5.3 Ankertext-Verteilung (Beispiel Hausmeisterservice)

Nicht überall „Hausmeisterservice Bruchsal“. Vorgabe:
* Footer: „Hausmeisterservice Bruchsal“ (1×)
* Navigation: „Hausmeisterservice“
* Startseite: „Hausmeisterservice für Wohnanlagen und Gewerbe“, „Hausmeisterservice im Detail“
* Ratgeber: „unser Hausmeisterservice“, „Hausmeisterservice mit festem Betreuer“, „Hausmeister in Bruchsal“
* Gartenpflege/Winterdienst: „Hausmeisterservice mit festem Betreuer“
Gleiches Prinzip für Winterdienst (Footer „Winterdienst Bruchsal“, sonst „Räum- und Streudienst“, „Winterdienst mit Einsatzprotokoll“, „Winterdienst für Ihr Objekt“) und alle anderen Leistungen.

Wichtig für **Winterdienst**: Die Ratgeber-Übersicht rankt aktuell auf Platz 8 für „winterdienst bruchsal“ statt winterdienst.html. Deshalb verlinken alle sechs Winter-Artikel (raeum-und-streupflicht, streuprotokoll, winterdienst-beauftragen, streugut-entfernen, laub-gehweg, sturmschaden) im ersten Drittel des Textes mit einem Ankertext, der „Winterdienst“ und „Bruchsal“ enthält, auf winterdienst.html, z. B. „unseren Winterdienst in Bruchsal“.

## 6. Ratgeber

### 6.1 Pflichtlinks je Artikel

1. **Nach oben:** ein Kontext-Link im ersten Drittel auf die zugeordnete Leistungsseite (Spalte „Leistung“) plus der vorhandene Hinweiskasten am Ende (Button). Buttons nur auf Leistungsseiten und Kontakt, nie auf andere Ratgeber.
2. **Seitwärts:** Block „Weiterlesen“ als `<ul class="weitere">` mit 2 bis 3 Artikeln, letzter Eintrag immer `<li><a href="/ratgeber/">Alle Ratgeberbeiträge</a></li>`.
3. **Zurück:** Brotkrume „Ratgeber“.
4. **Autor:** Link der Autorenbox auf `/ueber-uns.html#team`.

### 6.2 Matrix

| Artikel | Leistung (Kontext-Link, Ankertext) | Weiterlesen (in dieser Reihenfolge) |
|---|---|---|
| bauendreinigung-bruchsal | gebaeudereinigung.html „Gebäudereinigung in Bruchsal“ | grundreinigung-gewerbeboden · entruempelung-ablauf · bueroreinigung-praxisreinigung |
| besichtigung-vorbereiten-vermietung | wohnungsuebergabe.html „Wohnungsübergabe und Leerstandskontrolle“ | wohnungsuebergabe-protokoll · zaehlerstaende-ablesen · kleinreparaturen |
| bueroreinigung-praxisreinigung-bruchsal | bueroreinigung.html „Büroreinigung in Bruchsal“ (sonst gebaeudereinigung.html „Büro- und Praxisreinigung“) | glasreinigung · grundreinigung-gewerbeboden · schluesselverwaltung |
| dienstleister-wechseln-hausmeister | hausmeisterservice.html „Hausmeisterservice mit festem Betreuer“ | ortstermin-angebot · kosten-hausmeisterservice · hausmeisterservice-hausverwaltung |
| entruempelung-ablauf-bruchsal | entruempelung.html „Entrümpelung zum Festpreis in Bruchsal“ | muelltonnendienst · bauendreinigung · wohnungsuebergabe-protokoll |
| gartenpflege-jahresvertrag-bruchsal | gartenpflege.html „Gartenpflege in Bruchsal“ | hecke-schneiden-erlaubt · unkraut-pflaster · laub-gehweg-pflicht |
| glasreinigung-bruchsal | gebaeudereinigung.html „Fenster- und Glasreinigung“ | treppenhausreinigung · bueroreinigung-praxisreinigung · tiefgarage-keller |
| grundreinigung-gewerbeboden-bruchsal | gebaeudereinigung.html „Grundreinigung für Gewerbe“ | bueroreinigung-praxisreinigung · tiefgarage-keller · bauendreinigung |
| handwerkerkoordination-bruchsal | hausmeisterservice.html „Hausmeisterservice“ und kleinreparaturen.html „Kleinreparaturen“ | kleinreparaturen · stoerungsmeldung-gewerbeobjekt · sturmschaden-kontrolle |
| hausmeisterkosten-umlagefaehig | hausmeisterservice.html „Hausmeisterservice in Bruchsal“, preise.html „Richtpreise“ | kosten-hausmeisterservice · muelltonnendienst · treppenhausreinigung |
| hausmeisterservice-hausverwaltung-bruchsal | hausmeisterservice.html „Hausmeisterservice für Hausverwaltungen“ | hausmeisterservice-weg · hausmeisterkosten-umlagefaehig · stoerungsmeldung-gewerbeobjekt |
| hausmeisterservice-weg-bruchsal | hausmeisterservice.html „Hausmeisterservice für WEG“ | hausmeisterservice-hausverwaltung · hausmeisterkosten-umlagefaehig · treppenhausreinigung |
| hecke-schneiden-erlaubt | gartenpflege.html „Gartenpflege mit Heckenschnitt“ | gartenpflege-jahresvertrag · unkraut-pflaster · laub-gehweg-pflicht |
| kleinreparaturen-bruchsal | kleinreparaturen.html „Kleinreparaturen in Bruchsal“ | handwerkerkoordination · besichtigung-vorbereiten · schluesselverwaltung |
| kosten-hausmeisterservice-bruchsal | preise.html#objektbetreuung „Preisliste“, hausmeisterservice.html „Hausmeisterservice in Bruchsal“ | hausmeisterkosten-umlagefaehig · ortstermin-angebot · dienstleister-wechseln |
| laub-gehweg-pflicht-bruchsal | gartenpflege.html „Herbstpflege“, winterdienst.html „Winterdienst in Bruchsal“ | raeum-und-streupflicht · gartenpflege-jahresvertrag · streugut-entfernen |
| muelltonnendienst-bruchsal | hausmeisterservice.html „Hausmeisterservice“, preise.html#muelltonnen „Preis Mülltonnenservice“ | hausmeisterkosten-umlagefaehig · entruempelung-ablauf · schluesselverwaltung |
| ortstermin-angebot-hausmeisterservice | kontakt.html „Ortstermin anfragen“ | kosten-hausmeisterservice · dienstleister-wechseln · winterdienst-beauftragen |
| raeum-und-streupflicht-bruchsal | winterdienst.html „Winterdienst in Bruchsal“ | streuprotokoll · winterdienst-beauftragen · laub-gehweg-pflicht |
| schluesselverwaltung-bruchsal | metallarbeiten-schloesser.html „Zylindertausch und Schließanlagen“, hausmeisterservice.html | wohnungsuebergabe-protokoll · stoerungsmeldung-gewerbeobjekt · kleinreparaturen |
| stoerungsmeldung-gewerbeobjekt-bruchsal | hausmeisterservice.html „Hausmeisterservice für Gewerbeimmobilien“ | schluesselverwaltung · handwerkerkoordination · sturmschaden-kontrolle |
| streugut-entfernen-fruehjahr | winterdienst.html „Winterdienst in Bruchsal“ | raeum-und-streupflicht · streuprotokoll · unkraut-pflaster |
| streuprotokoll-winterdienst-bruchsal | winterdienst.html „Winterdienst mit Einsatzprotokoll“ | raeum-und-streupflicht · winterdienst-beauftragen · streugut-entfernen |
| sturmschaden-kontrolle-gebaeude | hausmeisterservice.html „Kontrollgänge im Hausmeisterservice“ | stoerungsmeldung-gewerbeobjekt · handwerkerkoordination · laub-gehweg-pflicht |
| tiefgarage-keller-reinigung-bruchsal | gebaeudereinigung.html „Tiefgaragen- und Kellerreinigung“ | treppenhausreinigung · grundreinigung-gewerbeboden · glasreinigung |
| treppenhaus-rettungsweg | treppenhausreinigung.html „Treppenhausreinigung“, hausmeisterservice.html | treppenhausreinigung · sturmschaden-kontrolle · schluesselverwaltung |
| treppenhausreinigung-bruchsal | treppenhausreinigung.html „Treppenhausreinigung in Bruchsal“ | glasreinigung · tiefgarage-keller · hausmeisterkosten-umlagefaehig |
| unkraut-pflaster-entfernen-bruchsal | gartenpflege.html „Pflege von Wegen und Höfen“ | hecke-schneiden-erlaubt · gartenpflege-jahresvertrag · streugut-entfernen |
| winterdienst-beauftragen-bruchsal | winterdienst.html „Winterdienst für Ihr Objekt“, preise.html#winterdienst | raeum-und-streupflicht · streuprotokoll · streugut-entfernen |
| wohnungsuebergabe-protokoll-bruchsal | wohnungsuebergabe.html „Wohnungsübergabe mit Fotoprotokoll“ | zaehlerstaende-ablesen · besichtigung-vorbereiten · kleinreparaturen |
| zaehlerstaende-ablesen-jahreswechsel | hausmeisterservice.html „Zählerstände im Hausmeisterservice“, wohnungsuebergabe.html | wohnungsuebergabe-protokoll · besichtigung-vorbereiten · hausmeisterkosten-umlagefaehig |

Bei jedem „Weiterlesen“-Block, dessen drei Ziele alle noch geplant sind, bleibt dank des festen letzten Eintrags „Alle Ratgeberbeiträge“ immer ein Link übrig.

### 6.3 Ratgeber-Übersicht

* Kacheln werden von `index.php` nach Datum gefiltert, dort ist nichts zu tun.
* Neu oben: Themenfilter oder Sprungmarken nach `artikel-thema` (Winterdienst, Betriebskosten, Gebäudereinigung, Gartenpflege, Vermietung, Hausverwaltung, Hausmeisterservice, Entrümpelung, Kleinreparaturen, Angebot).
* Unten: Linkblock „Unsere Leistungen“ auf alle Leistungsseiten (nicht nur Kontakt).

## 7. Prüfliste nach dem Umbau

* Keine internen Links auf Weiterleitungen oder 404 (insbesondere keine relativen Ratgeberlinks).
* Jede Leistungsseite hat mindestens 8 interne Links von anderen Seiten (Navigation und Footer mitgezählt) und mindestens 2 Kontext-Links aus Ratgebern.
* Keine Seite ist mehr als 3 Klicks von der Startseite entfernt (Ratgeber: Start › Ratgeber › Artikel).
* `einsatzgebiet.html` ist aus Footer, Startseite, Kontakt und allen „In welchen Orten“-Antworten verlinkt.
* Nach dem 15.12.2026 sind alle 31 Artikel live; dann einmal alle Seiten auf leere `<li>` oder verwaiste Wörter prüfen.
