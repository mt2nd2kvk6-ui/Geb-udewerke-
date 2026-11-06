#!/usr/bin/env python3
"""Macht aus den gebauten Entwürfen Einzeldateien, die ohne Zusatzdateien laden:
  1. ZIEL/artifact-<x>.html  : ohne Dokumentrahmen (der Artifact-Viewer setzt ihn selbst)
  2. projekt/entwuerfe/richtungen/ansehen/ : vollständige Seiten + Übersicht mit Bildern,
     zum Öffnen über einen öffentlichen Datei-Link (z. B. raw.githack.com mit Commit-Kennung)
Logos werden als data-URI eingesetzt, Schriften sind schon eingebettet.
Aufruf: python3 projekt/entwuerfe/richtungen/einzeln_bauen.py GEBAUTER_ORDNER"""
import base64, os, re, shutil, sys

HIER = os.path.dirname(os.path.abspath(__file__))
QUELLE = sys.argv[1]
ANSEHEN = os.path.join(HIER, 'ansehen')
os.makedirs(ANSEHEN, exist_ok=True)

LOGOS = {n: 'data:image/svg+xml;base64,' + base64.b64encode(open(os.path.join(QUELLE, n), 'rb').read()).decode()
         for n in ('logo-quer.svg', 'logo-quer-weiss.svg')}
SEITEN = [('a-register.html', 'a', 'Register'), ('b-modell.html', 'b', 'Das Modell'), ('c-liste.html', 'c', 'Was steht an?')]


def logos_einsetzen(s):
    for n, d in LOGOS.items():
        s = s.replace(f'src="{n}"', f'src="{d}"')
    return s


for datei, k, name in SEITEN:
    s = logos_einsetzen(open(os.path.join(QUELLE, datei), encoding='utf-8').read())
    # vollständige Seite fürs Repo
    open(os.path.join(ANSEHEN, datei), 'w', encoding='utf-8').write(s)
    # Artifact-Fassung: Dokumentrahmen entfernen, body-Attribute per Skript setzen
    body = re.search(r'<body([^>]*)>', s)
    attr = dict(re.findall(r'([\w-]+)="([^"]*)"', body.group(1))) if body else {}
    a = re.sub(r'^\s*<!doctype html>\s*<html[^>]*>\s*<head>\s*', '', s, flags=re.I)
    a = re.sub(r'<meta charset="utf-8">\s*<meta name="viewport"[^>]*>\s*', '', a)
    a = a.replace('<title>', '<meta name="claude:viewport-fit-sides" content="cover">\n<title>', 1)
    a = re.sub(r'</head>\s*<body[^>]*>', '', a, count=1)
    a = re.sub(r'</body>\s*</html>\s*$', '', a)
    a = a.replace('<a href="index.html" style="color:inherit">Zur Übersicht</a>', '')
    if attr:
        setzen = ''.join(f"document.body.setAttribute('{n}','{v}');" for n, v in attr.items())
        a = '<script>' + setzen + '</script>\n' + a
    open(os.path.join(QUELLE, f'artifact-{k}.html'), 'w', encoding='utf-8').write(a)
    print(f'artifact-{k}.html {len(a) // 1024} KB, ansehen/{datei} {len(s) // 1024} KB')

# Übersicht fürs Repo: Bilder + Links, keine Rahmen
for k in 'abc':
    shutil.copy(os.path.join(HIER, 'screenshots', f'version-{k}-v2-klein.jpg'), os.path.join(ANSEHEN, f'version-{k}.jpg'))
karten = ''.join(f'''<section><h2>Version {k.upper()} · {name}</h2>
<a class="bild" href="{datei}"><img src="version-{k}.jpg" width="1600" height="804" alt="Version {k.upper()}, Desktop und Handy"></a>
<a class="knopf" href="{datei}">Version {k.upper()} live öffnen</a></section>''' for datei, k, name in SEITEN)
open(os.path.join(ANSEHEN, 'index.html'), 'w', encoding='utf-8').write(f'''<!doctype html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Gebäudewerke Entwürfe</title><meta name="robots" content="noindex, nofollow">
<style>body{{margin:0;background:#F3F5F8;color:#0B1F38;font:16px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif}}
main{{max-width:1100px;margin:0 auto;padding:24px 16px 64px}}h1{{font-size:clamp(30px,6vw,52px);line-height:1;letter-spacing:-.03em;margin:8px 0 24px}}
section{{margin:0 0 40px}}h2{{font-size:22px;margin:0 0 10px}}.bild img{{width:100%;height:auto;display:block;border-radius:10px;box-shadow:0 10px 30px -18px rgba(0,0,0,.5)}}
.knopf{{display:inline-block;margin-top:12px;background:#0D2B4F;color:#fff;text-decoration:none;font-weight:700;padding:12px 18px;border-radius:999px}}</style></head>
<body><main><h1>Gebäudewerke · Entwürfe</h1>{karten}</main></body></html>''')
print('ansehen/index.html')
