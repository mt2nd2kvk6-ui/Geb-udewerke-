# Gebäudewerke – Website gebaeudewerke.de

Objekt- und Gebäudeservice in Bruchsal und im Landkreis Karlsruhe.

## Ordner

- `website/`: die komplette Website (HTML, PHP, Bilder). Wird 1:1 auf den Webspace übertragen.
- `projekt/`: Arbeitsunterlagen (Google-Profil und Bewertungen, SEO-Konzept, Screenshots). Wird nicht hochgeladen.
- `werkzeuge/`: Skripte für Pflege und Veröffentlichung.

## Häufige Aufgaben

| Aufgabe | So geht's |
|---|---|
| Neue Google-Bewertungen eintragen | `projekt/google-profil.json` ergänzen (Anzahl, Schnitt, Bewertung), dann `python3 werkzeuge/layout_anwenden.py` |
| Kopf, Navigation oder Fußbereich ändern | Vorlage in `werkzeuge/layout_anwenden.py` ändern, Skript ausführen |
| Design ändern | `website/assets/css/style.css` bearbeiten, dann `python3 werkzeuge/layout_anwenden.py` (CSS wird in jede Seite eingesetzt) |
| Neuen Ratgeberartikel einplanen | HTML-Datei in `website/ratgeber/` mit `<meta name="artikel-datum" content="JJJJ-MM-TT">`; erscheint automatisch ab dem Datum |
| GPS-Daten (Bruchsal) in neue Fotos schreiben | `python3 werkzeuge/bilder_geotaggen.py` |
| Lokal testen | `php -S 127.0.0.1:8080 -t website werkzeuge/dev_router.php`, dann http://127.0.0.1:8080 |
| Installer bauen | `python3 werkzeuge/installer_bauen.py` → `ausgabe/gw-installer.php` |

## Veröffentlichen bei IONOS

1. `ausgabe/gw-installer.php` im Webspace Explorer ins Hauptverzeichnis hochladen.
2. https://gebaeudewerke.de/gw-installer.php im Browser öffnen.
3. Die Seite meldet „Fertig: Website ist installiert“. Der Installer löscht sich selbst.
