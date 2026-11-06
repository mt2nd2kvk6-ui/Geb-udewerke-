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
- Eine kurze Notiz: was du geändert hast, offene `[PRÜFEN]`-Punkte und was ich in der Search Console tun muss.

Wenn etwas unklar ist, frag mich, bevor du baust.
