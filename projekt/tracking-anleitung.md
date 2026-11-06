# Tracking-Anleitung: GA4 und Search Console einrichten

Stand 06.11.2026. Mess-ID G-PKEXEYK6CG (Property 561433000), Search Console sc-domain:gebaeudewerke.de.

Was die Website von sich aus tut: Google Analytics lädt erst nach „Alle akzeptieren“ im Cookie-Banner. Vorher wird kein Byte an Google geschickt. Nach der Zustimmung setzt Consent Mode v2 `analytics_storage` auf „granted“, Werbe-Signale bleiben aus. Alle Ereignisse laufen über eine Funktion (`gwEreignis` in `assets/js/consent.js`, die Auslöser stehen in `assets/js/tracking.js`). Jedes Ereignis trägt `seite`, `position` und, wo die Seite einer Zielgruppe zugeordnet ist, `zielgruppe`.

Alles Weitere stellen Sie einmalig in GA4 und in der Search Console ein. Dauer etwa 30 Minuten.

## 1. Schlüsselereignisse markieren (GA4)

GA4 öffnen → unten links **Verwaltung** (Zahnrad) → Spalte „Datenanzeige“ → **Ereignisse**.

Die Ereignisse erscheinen in der Liste erst, nachdem sie mindestens einmal gesendet wurden. Lösen Sie sie deshalb nach dem Livegang selbst einmal aus (Banner akzeptieren, auf Anrufen klicken, WhatsApp klicken, E-Mail klicken, Testanfrage senden). Bis zu 24 Stunden später stehen sie in der Liste.

Dann bei jedem dieser Ereignisse rechts den Schalter **„Als Schlüsselereignis markieren“** einschalten:

| Ereignis | Bedeutung |
|---|---|
| `generate_lead` | Anfrageformular erfolgreich gesendet (Danke-Seite) |
| `anruf_klick` | Klick auf die Telefonnummer |
| `whatsapp_klick` | Klick auf einen WhatsApp-Kontakt |
| `email_klick` | Klick auf info@gebaeudewerke.de |

Optional, wenn Sie es als Erfolg zählen wollen: `cta_klick` (Angebot/Ortstermin-Buttons), `bewertung_schreiben_klick`.

Falls ein Ereignis noch nicht in der Liste steht: Verwaltung → **Schlüsselereignisse** → „Neues Schlüsselereignis“ → Namen genau so eintippen.

## 2. Benutzerdefinierte Dimensionen anlegen (GA4)

Ohne diesen Schritt sehen Sie die Parameter in keinem Bericht. Verwaltung → Spalte „Datenanzeige“ → **Benutzerdefinierte Definitionen** → **Benutzerdefinierte Dimension erstellen**. Umfang jeweils **Ereignis**. Dimensionsname frei (Vorschlag unten), Ereignisparameter genau wie in der Tabelle:

| Dimensionsname (Vorschlag) | Ereignisparameter | Werte |
|---|---|---|
| Position | `position` | kopf, hero, inhalt, kontaktblock, mobilleiste, schnellkontakt, fuss |
| Zielgruppe | `zielgruppe` | hausverwaltung, buero, praxis, gewerbe, privat, winterdienst |
| Seite | `seite` | Pfad, z. B. /hausmeisterservice.html |
| CTA-Text | `cta_text` | Beschriftung des Buttons |
| Thema | `thema` | Ratgeber-Thema, z. B. Winterdienst |
| Abschnitt | `abschnitt` | preise, ablauf, kontakt, … |
| Frage | `frage` | geöffnete FAQ-Frage |
| Titel | `titel` | aufgeklappter Bereich oder Artikel |
| Tabelle | `tabelle` | Preistabelle, z. B. objektbetreuung |
| Prozent | `prozent` | 25, 50, 75, 90 (als Dimension, nicht Messwert) |
| Kanal | `kanal` | whatsapp, email (Seite teilen) |
| Link-Ziel | `ziel` | Hostname bei ausgehenden Links |
| Link-Text | `link_text` | Beschriftung bei Anruf/WhatsApp/E-Mail |
| Adresse | `adresse` | aufgerufene Adresse auf der 404-Seite |
| Formular | `formular` | Startseite, Kontaktseite |

Das Kontingent liegt bei 50 Dimensionen pro Property, 15 reichen also. Daten laufen ab dem Zeitpunkt der Anlage ein, nicht rückwirkend.

## 3. Search Console mit GA4 verknüpfen

1. GA4 → **Verwaltung** → Spalte „Produktverknüpfungen“ → **Search Console-Verknüpfungen** → **Verknüpfen**.
2. „Konten auswählen“ → `sc-domain:gebaeudewerke.de` anhaken → Bestätigen.
3. Web-Datenstream der Website wählen → Weiter → **Senden**.
4. Danach in GA4 → Berichte → Bibliothek → Sammlung „Search Console“ → **Veröffentlichen**. Dann gibt es unter Berichte die Punkte „Google organische Suchanfragen“ und „Google organische Zugriffe“.

Nur ein GA4-Datenstream kann mit einer Search-Console-Property verknüpft sein.

## 4. Sitemaps in der Search Console einreichen

Search Console → Property `gebaeudewerke.de` → **Sitemaps** → „Neue Sitemap hinzufügen“, nacheinander:

- `sitemap.xml`
- `ratgeber/sitemap.php`

Beide stehen auch in der robots.txt. Status nach ein bis zwei Tagen prüfen: „Erfolgreich“, gefundene URLs 17 (sitemap.xml) und die Zahl der bereits veröffentlichten Ratgeber (sitemap.php, geplante Beiträge kommen am Erscheinungstag automatisch dazu).

Nach dem Livegang des neuen Designs: in der Search Console → **URL-Prüfung** → Startseite eingeben → „Indexierung beantragen“. Dasselbe für hausmeisterservice.html und preise.html. Mehr ist nicht nötig, der Rest wird über die Sitemaps gefunden.

## 5. Datenaufbewahrung

Verwaltung → Spalte „Datenerhebung und -änderung“ → **Datenaufbewahrung**. Aktuell 2 Monate, so steht es in der Datenschutzerklärung.

Empfehlung: **14 Monate**. Mit 2 Monaten können Sie in Explorationen keinen Vorjahresvergleich und keine Saisonauswertung machen (Winterdienst-Anfragen Oktober gegen Januar). Die Standardberichte sind davon nicht betroffen, Explorationen und Trichter schon. Wenn Sie umstellen, sagen Sie mir Bescheid, dann ändere ich in der Datenschutzerklärung (Punkt 7, Speicherdauer) „zwei Monaten“ in „14 Monaten“. Bis dahin bleibt es bei 2 Monaten, Text und Einstellung passen zusammen.

Ebenfalls dort: „Zurücksetzen bei neuer Aktivität“ auf **Aus** lassen.

## 6. Berichtsvorschlag: Anfragen nach Seite, Zielgruppe, Position und Quelle

Am schnellsten als GA4-Exploration, ohne Looker Studio:

1. GA4 → **Erkunden** → „Leer“.
2. Dimensionen importieren: Seitenpfad (`Seite` oder die Standarddimension „Seitenpfad und Bildschirmklasse“), `Zielgruppe`, `Position`, „Sitzung – Quelle/Medium“, „Sitzung – Kampagne“, „Ereignisname“.
3. Messwerte importieren: „Ereignisanzahl“, „Schlüsselereignisse“, „Sitzungen“.
4. Technik „Freies Format“, Tabelle:
   - Zeilen: Seitenpfad, darunter Position
   - Spalten: Ereignisname
   - Werte: Ereignisanzahl
   - Filter: Ereignisname stimmt genau überein mit `anruf_klick`, `whatsapp_klick`, `email_klick`, `generate_lead` (Filter „Ereignisname enthält _klick“ plus zweite Tabelle für generate_lead ist am einfachsten).
5. Zweiter Tab derselben Exploration: Zeilen „Sitzung – Quelle/Medium“ und „Sitzung – Kampagne“, Spalten Ereignisname, Werte Ereignisanzahl. Hier sehen Sie: google / organic (Suche), flyer / print mit Kampagne hausverwaltung … winterdienst (die QR-Codes), google / organic mit Kampagne gbp (Unternehmensprofil), (direct) / (none).
6. Dritter Tab: Zeilen Zielgruppe, Spalten Ereignisname.

Exploration speichern als „Anfragen nach Seite und Quelle“. Datumsbereich beliebig, aber nie länger als die Aufbewahrung (Punkt 5).

Wer lieber Looker Studio nutzt: Neuer Bericht → Datenquelle „Google Analytics“ → Property Gebäudewerke → Tabelle mit denselben Dimensionen. Die benutzerdefinierten Dimensionen aus Punkt 2 erscheinen dort unter ihrem Namen.

## 7. Prüfen, ob alles läuft

- Website in einem privaten Fenster öffnen, Banner mit „Nur notwendige“ schließen: in den Entwicklertools (Netzwerk) darf kein Aufruf an googletagmanager.com oder google-analytics.com erscheinen.
- Banner über „Cookie-Einstellungen“ im Fuß erneut öffnen, „Alle akzeptieren“: jetzt lädt gtag.js, GA4 → Berichte → **Echtzeit** zeigt Sie innerhalb von 30 Sekunden.
- Auf Anrufen klicken: in Echtzeit erscheint `anruf_klick`, beim Aufklappen „Position“ steht z. B. „kopf“.
- Die Liste aller Ereignisse mit Beispielparametern steht in `projekt/tracking-ereignisse.md`.
