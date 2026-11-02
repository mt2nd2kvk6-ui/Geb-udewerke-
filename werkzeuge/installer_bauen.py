#!/usr/bin/env python3
"""Baut gw-installer.php aus dem Ordner website/.

Aufruf:  python3 werkzeuge/installer_bauen.py  [Ausgabedatei]
Ergebnis: ausgabe/gw-installer.php (Standard). Diese Datei per Webspace Explorer
bei IONOS in das Hauptverzeichnis laden und einmal im Browser aufrufen:
https://gebaeudewerke.de/gw-installer.php
"""
import base64, datetime, io, os, sys, zipfile

BASIS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUELLE = os.path.join(BASIS, 'website')
KOPF = os.path.join(BASIS, 'werkzeuge', 'installer_kopf.php')
AUSGABE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASIS, 'ausgabe', 'gw-installer.php')
AUSLASSEN = {'.DS_Store', 'Thumbs.db'}

puffer = io.BytesIO()
anzahl = 0
with zipfile.ZipFile(puffer, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for wurzel, ordner, dateien in os.walk(QUELLE):
        ordner[:] = sorted(o for o in ordner if not o.startswith('.'))
        for d in sorted(dateien):
            if d in AUSLASSEN or d == '.htaccess':
                continue
            pfad = os.path.join(wurzel, d)
            name = os.path.relpath(pfad, QUELLE).replace(os.sep, '/')
            z.write(pfad, name)
            anzahl += 1

kopf = open(KOPF, encoding='utf-8').read()
heute = datetime.date.today().strftime('%d.%m.%Y')
kopf = kopf.replace('Stand 29.10.2026 (b, mit Conversions)', 'Stand ' + heute + ' (Relaunch)', 1)
daten = base64.b64encode(puffer.getvalue()).decode('ascii')
zeilen = '\n'.join(daten[i:i + 76] for i in range(0, len(daten), 76))
os.makedirs(os.path.dirname(AUSGABE), exist_ok=True)
with open(AUSGABE, 'w', encoding='utf-8', newline='\n') as f:
    f.write(kopf.rstrip('\n') + '\n' + zeilen + '\n')
print(f'{anzahl} Dateien, {os.path.getsize(AUSGABE) / 1e6:.1f} MB -> {AUSGABE}')
