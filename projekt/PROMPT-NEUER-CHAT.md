# Auftrag: Neuauftritt gebaeudewerke.de, Website als Eyecatcher

Im Anhang liegt `gebaeudewerke-website-2026-11-06.zip`. Darin ist die komplette aktuelle Website samt Werkzeugen, SEO-Unterlagen und unseren Flyern als Impuls (`impuls/Gebaeudewerke_Flyer_Alle_Zielgruppen.pdf`). Bitte entpacken, zuerst alles lesen (README.md, website/, werkzeuge/, projekt/), dann loslegen.

## Wer wir sind

Gebäudewerke GbR, Allmend 2, 76707 Hambrücken. Objekt- und Gebäudeservice für Bruchsal und den Landkreis Karlsruhe: Hausmeisterservice, Treppenhaus- und Gebäudereinigung, Büro- und Praxisreinigung, Gartenpflege, Winterdienst, Entrümpelung, Wohnungsübergaben, Kleinreparaturen, Metallarbeiten und Schlösser. Wir sind vier Mann zwischen 30 und 40, mit eigenem Personal, ohne Subunternehmer.

Zielgruppen: Hausverwaltungen und WEG, private Eigentümer und Vermieter, Firmen und Büros, Praxen, Verkaufsflächen, Hallen und Gewerbe.

## Was ich will

Die Website ist unsere Visitenkarte, und im Moment sieht sie aus wie jede andere Baukasten-Seite: großes Foto, Icon-Leiste, Leistungskarten, lange Texte, blauer Kontaktblock. Das will ich nicht mehr.

Ich will eine Seite, bei der man denkt: „Wow, was ist da los, das ist mal geil.“ Wer sie öffnet, soll sofort merken: Da sind junge Leute mit Power, mit denen hab ich Bock. Und am Ende soll er zum Telefon greifen oder uns auf WhatsApp schreiben.

- **Auffallen und abheben.** Wir haben 2026. Setz optisch neue Standards für Gebäudeservice, bleib dabei professionell und seriös. Mut ja, Kirmes nein.
- **Zum Anrufen provozieren.** Jede Seite muss in den ersten Sekunden klar machen, was wir tun, für wen, und wie man uns erreicht. Anrufen und WhatsApp sind die Hauptaktion, nicht ein Button unter vielen.
- **Bock machen zu lesen.** Keiner liest lange Keyword-Texte. Kurze, starke Sätze. Schlagzeilen mit Haltung. Inhalte, die man in Sekunden erfasst: Zahlen, Uhrzeiten, Abläufe, Checklisten, Belege. Wer Details will, kann aufklappen oder weiterklicken.
- **Für jede Zielgruppe die passende Ansprache**, so wie auf den Flyern: Hausverwaltung tickt anders als ein Privatkunde, eine Praxis anders als eine Lagerhalle.

## Die Flyer als Impuls

Die Flyer (12 Seiten, im Paket unter `impuls/`) sind schon gute Blickfänge. Nimm sie als Richtung, nicht als Kopiervorlage:

- **Schlagzeilen mit Wumms:** „Fünf Gewerke. Eine Nummer.“, „Wir waren schon da.“, „Läuft. Auch wenn Sie nicht hinsehen.“, „Ihre Liste. Unser Job.“, „Wir räumen. Sie haben den Beleg.“ Fette Grotesk, dazu ein Wort in kursiver Serifenschrift als Akzent.
- **Echte Arbeitsbelege als Gestaltung:** Objektprotokoll mit Uhrzeit und Status, Einsatzprotokoll Winterdienst mit Witterung und Streumittel, Reinigungsplan mit Häkchen, durchgestrichene To-do-Liste.
- **Riesige Uhrzeiten als Bildmotiv:** „06:30“ bei Büros, „07:00“ beim Winterdienst, als feine Konturziffern.
- **Eigene Farbwelt je Zielgruppe:** Werkblau/Gelb für Hausverwaltungen, Creme/Koralle für Büros, Mint/Dunkelgrün für Praxen, Schwarz/Orange mit Warnstreifen für Gewerbe, Gelb für Privatkunden, Nachtblau/Eisblau für den Winterdienst.
- **Riesige Telefonnummer** als Abschluss, kleine Pills wie „FÜR BÜROS“, nummerierte 3 Schritte „Anrufen oder WhatsApp, Ortstermin, Festpreis“.

Werkblau #0D2B4F und unser Logo bleiben die Basis der Marke. Die Akzentfarben der Flyer sind je Zielgruppe ausdrücklich erlaubt. Finde eine Lösung, wie diese Farbwelten auf der Website zusammenpassen und trotzdem als eine Marke erkennbar sind.

## Wie du vorgehen sollst

1. Lies die aktuelle Website und die Flyer. Schlag mir dann **zwei bis drei klar unterschiedliche Design-Richtungen** vor, jeweils mit einem kurzen Satz zur Idee und einem Entwurf der Startseite (oben bis zum ersten Scroll, Handy und Desktop) als klickbare Vorschau. Ich entscheide, dann baust du aus.
2. Bau danach Startseite, alle Leistungsseiten, Preise, Einsatzgebiet, Über uns, Kontakt, Karriere und die Ratgeber-Übersicht im neuen Design. Die Ratgeber-Artikel bekommen das neue Layout, ihr Text bleibt im Wesentlichen.
3. Zeig mir zwischendurch und am Ende eine **durchklickbare Vorschau**. Erst nach meiner Freigabe baust du den Installer.

## Texte

- Schreib die Texte der Haupt- und Leistungsseiten neu: kurz, direkt, mit Haltung, Anrede „Sie“. Als Richtwert höchstens 2 bis 3 kurze Sätze pro Block, ganz oben pro Seite höchstens 25 Wörter.
- Keine KI-Floskeln, keine Gedankenstriche als Stilmittel, keine Emojis, nichts von „rundum sorglos“, „maßgeschneidert“, „Ihr zuverlässiger Partner“.
- **Keine Fakten, Preise, Zahlen, Siegel, Kundenzahlen oder Referenzen erfinden.** Nutze nur, was auf der Website oder den Flyern steht. Fehlt etwas, setz `[PRÜFEN: …]` und nenn es mir.
- SEO darf nicht leiden: Jede Seite behält ihr Hauptkeyword (Liste in `projekt/seo/hauptkeywords.json`), ihre Title-, Description- und H1-Logik sowie die FAQ-Inhalte. Längere Erklärungen dürfen in aufklappbare Bereiche wandern, solange sie im HTML stehen. Prüfe mit `werkzeuge/seo_pruefen.py` und `werkzeuge/links_pruefen.py`, beide müssen 0 Befunde melden.

## SEO und GEO müssen auf Höchstniveau bleiben (Ziel: 100 von 100)

Das neue Design darf das Ranking nicht schwächen, es soll es stärken. Bei Google und in KI-Antworten (ChatGPT, Perplexity, Google AI Overviews) wollen wir in Bruchsal und im Landkreis Karlsruhe vorne sein. Jede Seite muss alle folgenden Punkte erfüllen. Prüfe sie am Ende Seite für Seite und liste das Ergebnis auf.

**Seobility-Kriterien (Onpage-Score 100 %)**
- Title höchstens 575 px (Arial 20 px), Description höchstens 990 px (Arial 14 px), beide gemessen, nicht nach Zeichen geschätzt. Jede Seite hat einen eigenen Title und eine eigene Description, kein Duplikat.
- Title nie wortgleich zur H1. Jedes Wort aus Title und H1 kommt im Fließtext vor.
- Genau eine H1 pro Seite, saubere Überschriften-Hierarchie (H2, H3 ohne Sprünge).
- Genug Text für Google trotz kurzer, knackiger Darstellung. Mindestwerte inklusive aufklappbarer Bereiche, gezählt nur im Inhalt (ohne Navigation und Fußbereich):
  - Startseite mindestens 1.000 Wörter, jede Leistungsseite mindestens 800 Wörter
  - Preise, Einsatzgebiet und Über uns mindestens 600 Wörter, Ratgeber-Übersicht mindestens 300 Wörter, Kontakt und Karriere mindestens 400 Wörter
  - Ratgeber-Artikel behalten ihre heutige Länge (nicht kürzen, höchstens straffen und gliedern)
  - Keine indexierbare Seite darf unter 80 % ihrer heutigen Wortzahl fallen. Miss die Wortzahl jeder Seite vorher und nachher und liste beides auf.
  - Der Seobility-Punkt „Textlänge“ muss auf jeder Seite grün sein.
  - Alles steht im HTML, nichts wird erst per JavaScript geladen.
- Keyword-Dichte natürlich, Hauptkeyword ungefähr 1 bis 2 %, keine Häufung. Hauptkeyword in Title, H1, erstem Absatz, Description und im Alt-Text des Hauptbildes.
- Keine doppelten Textblöcke (auch nicht durch Laufband oder Wiederholungen), keine doppelten Fettungen, durchschnittliche Satzlänge kurz.
- Jedes Bild hat einen beschreibenden Alt-Text mit Leistung und Ort, rein dekorative Bilder haben `alt=""`.
- Interne Links: ausreichend viele, keine kaputten Links, kein Ankertext zeigt auf zwei verschiedene Seiten, wichtige Seiten (vor allem `hausmeisterservice.html`) bekommen viele Links aus dem Fließtext.
- Canonical, `lang="de"`, Viewport, Favicon und Apple-Touch-Icon, Open-Graph- und Twitter-Tags auf jeder Seite. HTTPS, gzip, kleine HTML-Größe, schnelle Antwortzeit.

**Ahrefs-Site-Audit (keine Fehler, keine Warnungen)**
- Keine 4xx/5xx, keine Weiterleitungsketten, keine kaputten internen oder externen Links.
- Keine verwaisten Seiten: jede indexierbare Seite ist intern verlinkt.
- `sitemap.xml` enthält nur erreichbare, indexierbare, kanonische URLs mit 200, nichts mit noindex. `robots.txt` bleibt gültig.
- Keine doppelten Inhalte, keine fehlenden oder doppelten H1, Titles und Descriptions.
- Bilder in WebP mit `width`/`height`, nicht größer als nötig, Hero-Bild mit `fetchpriority="high"`, übrige `loading="lazy"`.
- Keine internen nofollow-Links, kein Mixed Content, strukturierte Daten ohne Fehler.

**PageSpeed und Core Web Vitals**
- Lighthouse mobil Ziel 100, mindestens 95 bei Performance. 100 bei Barrierefreiheit, Best Practices und SEO.
- LCP mobil unter 1,8 s, CLS 0, INP unter 200 ms. Kritisches CSS inline, Schrift per Preload, kein render-blockierendes JavaScript, Animationen nur über transform und opacity.

**Lokales SEO und GEO (Bruchsal im Fokus)**
- `geo.placename` Bruchsal, `geo.position` und `ICBM` 49.1291927;8.5914434 auf jeder Seite.
- GPS-Koordinaten von Bruchsal (49.1291927, 8.5914434) in den EXIF-Daten aller Fotos. Neue oder ersetzte Bilder ebenfalls mit `werkzeuge/bilder_geotaggen.py` versehen.
- Name, Adresse und Telefonnummer überall identisch: Gebäudewerke GbR, Allmend 2, 76707 Hambrücken, Telefon 0176 74025524, E-Mail info@gebaeudewerke.de.
- JSON-LD vollständig und gültig: HomeAndConstructionBusiness mit allen Orten in `areaServed` (Bruchsal zuerst), Öffnungszeiten, Notdienst, `sameAs` mit Google-Profil, `aggregateRating`; je Leistungsseite ein `Service` mit Angebot; `FAQPage` exakt synchron zu den sichtbaren Fragen; `BreadcrumbList`; Ratgeber als `Article` mit Autor (Person) und Herausgeber; Team als `Person`.
- Für KI-Suchen: am Anfang wichtiger Abschnitte eine zitierfähige Kurzantwort (40 bis 60 Wörter), FAQ in der Sprache echter Suchanfragen, `llms.txt` auf dem neuesten Stand.
- Bruchsal und die Ortsteile (Büchenau, Heidelsheim, Helmsheim, Obergrombach, Untergrombach) sowie die Orte im Landkreis natürlich im Text, keine Ortsseiten nur für Keywords.

**Prüfung**
- `werkzeuge/seo_pruefen.py` und `werkzeuge/links_pruefen.py` müssen 0 Befunde melden. Erweitere die Skripte, wo Punkte von oben noch nicht geprüft werden (z. B. Wortzahl, Keyword-Dichte, Alt-Texte, doppelte Textblöcke, Open Graph, Sitemap-Abgleich).
- Lighthouse für Startseite, eine Leistungsseite, Kontakt, Ratgeber-Übersicht und einen Artikel, jeweils mobil.
- Liste am Ende pro Seite: Title px, Description px, Wortzahl, Keyword-Dichte, Lighthouse-Werte, offene Punkte.
- Sei ehrlich: Onpage, Technik und Inhalt können 100 erreichen. Backlinks und Domain-Stärke kommen nicht aus dem Code. Dafür nenn mir am Ende konkrete Offpage-Schritte, statt Werte zu beschönigen.

## Tracking und Analyse: alles messbar in GA4, Search Console eingebunden

Ich will sehen, was auf der Seite passiert: wer woher kommt, was gelesen wird, was geklickt wird und was am Ende zu einer Anfrage führt. Bestehende Daten: GA4-Mess-ID **G-PKEXEYK6CG** (Property 561433000), Search Console als Domain-Property **sc-domain:gebaeudewerke.de** (bereits bestätigt).

**Rahmen**
- Google Analytics lädt weiterhin erst nach Zustimmung im Cookie-Banner. Baue zusätzlich **Google Consent Mode v2** ein (Standard: alles „denied“, nach Zustimmung „granted“ für `analytics_storage`; Werbe-Signale bleiben aus). Die Banner-Logik in `consent.js` darfst du dafür erweitern, ihr Verhalten für den Besucher bleibt gleich.
- Alle Ereignisse laufen über eine zentrale Funktion mit einheitlichen Namen und Parametern. Jedes Ereignis bekommt mindestens `seite` (Pfad), `zielgruppe` (falls die Seite einer zugeordnet ist) und `position` (wo auf der Seite: kopf, hero, inhalt, kontaktblock, mobilleiste, schnellkontakt, fuss).

**Ereignisse, die gemessen werden sollen**
- `anruf_klick`, `whatsapp_klick`, `email_klick` (bestehen schon, um `position` ergänzen), damit ich sehe, welcher Button wirklich angerufen wird.
- `generate_lead` beim erfolgreichen Absenden des Formulars (Danke-Seite, besteht schon), dazu `formular_start` (erstes Feld ausgefüllt) und `formular_fehler` (Fehlerseite aufgerufen).
- `cta_klick` für „Angebot anfragen“, „Ortstermin anfragen“ und ähnliche Buttons mit `cta_text`.
- `google_bewertung_klick` (Link „5,0 Sterne auf Google“) und `bewertung_schreiben_klick`.
- `scroll_tiefe` bei 25, 50, 75 und 90 %.
- `abschnitt_gesehen`, wenn ein wichtiger Abschnitt sichtbar wird (z. B. Preise, Ablauf, Kontaktblock), über IntersectionObserver.
- `faq_geoeffnet` mit der Frage, `aufklappen` für aufklappbare Textbereiche.
- `ratgeber_gelesen`, wenn ein Artikel zu 75 % gelesen wurde, mit `thema`.
- `preis_ansicht` auf der Preisseite je Preistabelle.
- `karte_geladen` (Zwei-Klick-Karte), `laufband_pause`, `menue_geoeffnet` (Handy-Menü).
- `seite_teilen` (WhatsApp/E-Mail teilen), `ausgehender_link` für alle externen Links.
- `fehlerseite` auf der 404-Seite mit der aufgerufenen Adresse.
- Die Entscheidung im Cookie-Banner selbst wird nicht gemessen. Ohne Zustimmung geht keine einzige Anfrage an Google.

**Flyer und Google-Profil messbar machen**
- Erzeuge für jede Flyer-Zielgruppe einen eigenen Link mit UTM-Parametern, z. B. `https://gebaeudewerke.de/?utm_source=flyer&utm_medium=print&utm_campaign=hausverwaltung` (ebenso buero, praxis, gewerbe, privat, winterdienst), und dazu je einen QR-Code als SVG und PNG in `projekt/qr/`. So sehe ich in GA4, welcher Flyer Besucher bringt.
- Ein Link für das Google-Unternehmensprofil: `https://gebaeudewerke.de/?utm_source=google&utm_medium=organic&utm_campaign=gbp`, den trage ich im Profil als Website ein.
- Prüfe, dass UTM-Parameter die Seite nicht kaputt machen (Canonical bleibt ohne Parameter, `auslieferung.php` liefert normal aus).

**Was ich selbst in GA4 und Search Console einstellen muss**
Schreib mir dazu eine kurze Klick-Anleitung (Datei `projekt/tracking-anleitung.md`):
- Welche Ereignisse ich in GA4 als **Schlüsselereignis** markiere (mindestens `generate_lead`, `anruf_klick`, `whatsapp_klick`, `email_klick`).
- Welche Parameter ich als **benutzerdefinierte Dimensionen** anlege (`position`, `zielgruppe`, `cta_text`, `thema` usw.), damit sie in Berichten auftauchen.
- **Search Console mit GA4 verknüpfen** (GA4 Verwaltung → Produktverknüpfungen → Search Console) und die Sitemaps `sitemap.xml` und `ratgeber/sitemap.php` einreichen.
- Datenaufbewahrung in GA4 (aktuell 2 Monate, so steht es in der Datenschutzerklärung). Wenn du eine längere Aufbewahrung empfiehlst, sag es mir, und passe dann auch die Datenschutzerklärung an.
- Einen Vorschlag für einen Bericht (GA4-Exploration oder Looker Studio): Anfragen, Anrufe und WhatsApp pro Seite, pro Zielgruppe, pro Button-Position und pro Quelle (Google, Flyer, Google-Profil, direkt).

**Datenschutz**
- Die Datenschutzerklärung muss zum Tracking passen. Ergänze, was sich ändert (Consent Mode, gemessene Ereignisse in allgemeiner Form), ohne den Rest umzuschreiben. Speicherdauer und Auftragsverarbeitung bleiben wie angegeben, außer ich entscheide anders.

**Prüfung**
- Teste im Browser, dass ohne Zustimmung keine einzige Anfrage an Google geht und nach „Alle akzeptieren“ jedes Ereignis mit den richtigen Parametern ankommt (dataLayer bzw. Netzwerk mitschneiden). Liste alle Ereignisse mit Beispiel-Parametern in der Abschlussnotiz.

## Feste Vorgaben, nicht verhandelbar

- **Telefon für Anrufe: 0176 74025524** (`tel:+4917674025524`). **WhatsApp: 0163 7221790** (wa.me/491637221790 bzw. api.whatsapp.com/send?phone=491637221790). Die Flyer zeigen noch die alte Nummer als Anrufnummer, die darf NICHT übernommen werden.
- Ein klar erkennbarer **WhatsApp-Button** (mit WhatsApp-Symbol) muss im Kopfbereich neben „Anrufen“ und auf dem Handy immer sichtbar sein. Er darf nie fehlen.
- **Preise:** die aktuellen Preise aus `website/preise.html` unverändert übernehmen, netto und brutto. Nichts neu berechnen.
- **Bewertungen:** sichtbar als „5,0 Sterne auf Google“ mit Link auf https://share.google/v7XolrfYaCO55YrZz. Das Laufband mit den echten Kundenstimmen bleibt, die Texte nicht ändern. Das `aggregateRating` im JSON-LD bleibt auf allen Seiten.
- **Team:** „vier Mann“, nicht „Gesellschafter“ (das Wort steht nur im Impressum). Bei Qualifikationen nur „Meisterbrief“, ohne „Metallmeister“ oder eine andere Richtung.
- **Einsatzgebiet:** Bruchsal mit allen Stadtteilen und die Orte im Landkreis Karlsruhe, Stutensee und Bretten bleiben.
- **Pro Seite nur ein Kontaktblock** unten, mit Anrufen, WhatsApp und Anfrage. Keine Button-Flut.
- **Nicht verändern:** `auslieferung.php`, `ratgeber/plan.json`, `ratgeber/sitemap.php`, `einrichtung.php`, `htaccess.txt`, `anfrage.php`, die Logik von `assets/js/consent.js`, die Datumszeile „veröffentlicht am“ in den Ratgebern. Kein „aktualisiert am“ einfügen.
- **Funktionen müssen bleiben:** Kontaktformular (`action="anfrage.php"`, alle Feldnamen exakt wie jetzt, Honeypot `webseite`), Cookie-Banner (Google Analytics erst nach Zustimmung, Conversions für Anruf, WhatsApp, E-Mail und Anfrage), zeitgesteuerte Ratgeber über `auslieferung.php`, Zwei-Klick-Karte, alle URLs und Dateinamen.
- **Technik:** statisches HTML, kein Framework, keine externen Skripte oder Fonts. Schriften lokal einbinden; neue Schriften nur mit freier Lizenz als Datei im Paket. Lighthouse mobil mindestens 95 bei Performance, 100 bei Barrierefreiheit, Best Practices und SEO. Kein horizontales Scrollen bei 390 px, Kontraste nach WCAG AA, `prefers-reduced-motion` beachten.
- **Bewegung:** gern mutig, aber flüssig. Nur transform und opacity, kein Layout-Springen.
- **Fotos:** Die Website hat zum Großteil Stockfotos. Plane das Design so, dass es ohne Fotos stark wirkt (Typografie, Belege, Uhrzeiten, Farbe) und echte Fotos später einfach einsetzbar sind. Stockfotos nie als „unser Team“ ausgeben.
- Kopf, Fuß und gemeinsame Bausteine laufen über `werkzeuge/layout_anwenden.py`. Passe das Skript an das neue Design an, statt 50 Seiten von Hand zu ändern. Ein zweiter Lauf muss 0 Änderungen ergeben.

## Abgabe

- Durchklickbare Vorschau zur Freigabe (`werkzeuge/vorschau_bauen.py` hilft dabei).
- Danach `gw-installer.php` über `werkzeuge/installer_bauen.py`, im selben Format wie bisher (selbstentpackend, legt `.htaccess` aus `htaccess.txt` an, löscht sich selbst). In einer leeren Testumgebung ausführen und mit dem Quellstand vergleichen.
- `keywords.md` aktualisiert (Seite, Hauptkeyword, Title, px, Description, px, H1), separat, nicht im Installer.
- Die SEO/GEO-Liste pro Seite (siehe oben) mit allen Werten.
- `projekt/tracking-anleitung.md`, die QR-Codes und UTM-Links in `projekt/qr/` und die Liste aller Tracking-Ereignisse mit Beispiel-Parametern.
- Eine kurze Notiz: was du geändert hast, offene `[PRÜFEN]`-Punkte und was ich in der Search Console tun muss.

Wenn etwas unklar ist, frag mich, bevor du baust.
