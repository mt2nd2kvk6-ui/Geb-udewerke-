#!/usr/bin/env python3
"""Baut eine klickbare Vorschau der Website (statisch, ohne PHP) für die Anzeige im Chat.
Voraussetzung: lokaler Server läuft (php -S 127.0.0.1:8095 -t website werkzeuge/dev_router.php).
Ausgabe: Ordner, der als Artifact veröffentlicht wird (index.html = Startseite)."""
import os, re, sys, glob, shutil, posixpath, urllib.request, urllib.error
BASIS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(BASIS, 'website'); ZIEL = sys.argv[1]; SERVER = 'http://127.0.0.1:8095'
shutil.rmtree(ZIEL, ignore_errors=True); os.makedirs(ZIEL)

seiten = ['/'] + ['/' + f for f in sorted(os.listdir(WEB)) if f.endswith('.html')] + ['/ratgeber/'] + \
         ['/ratgeber/' + os.path.basename(f) for f in sorted(glob.glob(WEB + '/ratgeber/*.html'))]
def ausgabepfad(u):
    return 'index.html' if u == '/' else (u.lstrip('/') + 'index.html' if u.endswith('/') else u.lstrip('/'))
live = {}
for u in seiten:
    try: live[u] = urllib.request.urlopen(SERVER + u).read().decode()
    except urllib.error.HTTPError: pass   # geplante Artikel (404) auslassen
ziele = {ausgabepfad(u) for u in live}
assets = set()

HINWEIS = ('<div style="position:fixed;left:0;right:0;bottom:0;z-index:9999;background:#F0B323;color:#0D2B4F;'
           'font:600 13px/1.35 system-ui,sans-serif;text-align:center;padding:6px max(16px,env(safe-area-inset-left,0px)) '
           'calc(6px + env(safe-area-inset-bottom,0px))">Vorschau der neuen Website. Formular, Anruf und Karte funktionieren erst auf gebaeudewerke.de.</div>')
FORM_JS = ('<script>document.addEventListener("submit",function(e){e.preventDefault();'
           'var f=e.target,m=f.querySelector(".vorschau-meldung");if(!m){m=document.createElement("p");'
           'm.className="vorschau-meldung";m.style.cssText="margin-top:1rem;padding:.8rem 1rem;background:#EEF1F4;'
           'border-left:4px solid #F0B323;font-weight:600";f.appendChild(m)}'
           'm.textContent="Vorschau: Die Anfrage wird erst auf gebaeudewerke.de wirklich versendet.";},true);</script>')

for u, h in live.items():
    pfad = ausgabepfad(u); ordner = posixpath.dirname(pfad)
    def umschreiben(wert):
        if re.match(r'^(https?:|mailto:|tel:|data:|#|//|javascript:|sms:)', wert) or wert == '': 
            m = re.match(r'^https://gebaeudewerke\.de(/[^"#]*)?(#.*)?$', wert)
            if not m: return wert
            wert = (m.group(1) or '/') + (m.group(2) or '')
        teil, _, anker = wert.partition('#')
        teil = teil.split('?')[0]
        absolut = teil if teil.startswith('/') else posixpath.normpath(posixpath.join('/' + ordner, teil)) + ('/' if teil.endswith('/') else '')
        ziel = ausgabepfad(absolut) if (absolut.endswith('/') or absolut.endswith('.html')) else absolut.lstrip('/')
        if ziel.endswith('.html') and ziel not in ziele: ziel = 'index.html'
        if not ziel.endswith('.html') and os.path.isfile(os.path.join(WEB, ziel)): assets.add(ziel)
        rel = posixpath.relpath(ziel, ordner or '.')
        return rel + ('#' + anker if anker else '')
    h = re.sub(r'(\s(?:href|src|action)=")([^"]*)(")', lambda m: m.group(1) + umschreiben(m.group(2)) + m.group(3), h)
    h = re.sub(r'(\ssrcset=")([^"]*)(")', lambda m: m.group(1) + ', '.join(
        ' '.join([umschreiben(t.strip().split(' ')[0])] + t.strip().split(' ')[1:]) for t in m.group(2).split(',')) + m.group(3), h)
    h = re.sub(r'url\("(/?assets/[^"]+)"\)', lambda m: 'url("%s")' % umschreiben(m.group(1)), h)
    h = re.sub(r'<script[^>]+consent\.js[^>]*></script>', '', h)            # keine Statistik in der Vorschau
    h = re.sub(r'<meta name="robots" content="[^"]*">', '<meta name="robots" content="noindex, nofollow">', h)
    h = h.replace('</body>', FORM_JS + HINWEIS + '</body>', 1)
    if pfad == 'index.html':   # Startseite: Dokumentrahmen entfernen, das Artifact setzt ihn selbst
        h = re.sub(r'^\s*<!doctype html>\s*<html[^>]*>\s*<head>', '', h, flags=re.I)
        h = re.sub(r'</head>\s*<body[^>]*>', '', h, count=1, flags=re.I)
        h = re.sub(r'</body>\s*</html>\s*$', '', h, flags=re.I)
    os.makedirs(os.path.join(ZIEL, ordner), exist_ok=True)
    open(os.path.join(ZIEL, pfad), 'w', encoding='utf-8').write(h)
for a in assets:
    os.makedirs(os.path.dirname(os.path.join(ZIEL, a)), exist_ok=True)
    shutil.copy(os.path.join(WEB, a), os.path.join(ZIEL, a))
print(len(live), 'Seiten,', len(assets), 'Dateien')
