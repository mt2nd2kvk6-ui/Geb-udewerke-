#!/usr/bin/env python3
"""Prüft interne Links: Ziele existieren, Sprungmarken existieren, Bildverweise existieren,
und kein Ankertext zeigt auf zwei verschiedene Seiten. Aufruf: python3 werkzeuge/links_pruefen.py"""
import glob, html, os, posixpath, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_pruefen import WEB, lesen, seiten
def seitenpfad(p): return '/' + os.path.relpath(p, WEB).replace(os.sep, '/').replace('index.html', '').replace('index.php', '')
def ziel(href, von):
    if re.match(r'^(https?:|mailto:|tel:|data:|javascript:|sms:|//)', href):
        m = re.match(r'^https://gebaeudewerke\.de(/.*)?$', href)
        if not m: return None
        href = m.group(1) or '/'
    teil, _, anker = href.partition('#')
    teil = teil.split('?')[0]
    if teil == '': return (von, anker)
    absolut = teil if teil.startswith('/') else posixpath.normpath(posixpath.join(posixpath.dirname(von) or '/', teil)) + ('/' if teil.endswith('/') else '')
    return (absolut, anker)
def datei(pfad):
    p = os.path.join(WEB, pfad.lstrip('/'))
    if pfad.endswith('/'): return next((os.path.join(p, x) for x in ('index.html', 'index.php') if os.path.isfile(os.path.join(p, x))), None)
    return p if os.path.isfile(p) else None
inhalte = {seitenpfad(p): lesen(p) for p in seiten()}
inhalte['/'] = inhalte.pop('/') if '/' in inhalte else lesen(os.path.join(WEB, 'index.html'))
ids = {k: set(re.findall(r'\sid="([^"]+)"', v)) for k, v in inhalte.items()}
fehler, anker_ziele = [], {}
for von, s in inhalte.items():
    if von.endswith('404.html'): pass
    for m in re.finditer(r'<a\b([^>]*)>(.*?)</a>', s, re.S):
        h = re.search(r'\shref="([^"]*)"', m.group(1))
        if not h or '<?' in h.group(1): continue
        if h.group(1).startswith('#'):          # Sprung innerhalb derselben Seite: nur Ziel prüfen
            if h.group(1)[1:] and h.group(1)[1:] not in ids[von]: fehler.append(f'{von}: Sprungmarke fehlt: {h.group(1)}')
            continue
        z = ziel(html.unescape(h.group(1)), von)
        if z is None: continue
        pfad, sprung = z
        if pfad.endswith('.php') and pfad not in ('/ratgeber/sitemap.php',) and not pfad.endswith('index.php'):
            pass
        f = datei(pfad)
        if not f: fehler.append(f'{von}: Ziel fehlt: {h.group(1)}'); continue
        if sprung and f.endswith(('.html', '.php')):
            zk = seitenpfad(f) if seitenpfad(f) in ids else pfad
            if sprung not in ids.get(zk, set()): fehler.append(f'{von}: Sprungmarke fehlt: {h.group(1)}')
        txt = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'<(svg|span class="visuell-versteckt")\b.*?</(svg|span)>', ' ', m.group(2), flags=re.S)))).strip()
        if not txt:
            alt = re.search(r'alt="([^"]+)"', m.group(2)); txt = alt.group(1) if alt else ''
        if txt and f.endswith(('.html', '.php')):
            anker_ziele.setdefault(txt.lower(), {}).setdefault(seitenpfad(f), set()).add(von)
    for m in re.finditer(r'\s(?:src|srcset)="([^"]+)"', s):
        for u in [x.strip().split(' ')[0] for x in m.group(1).split(',')]:
            z = ziel(u, von)
            if z and not datei(z[0]): fehler.append(f'{von}: Bild/Datei fehlt: {u}')
    for u in re.findall(r'url\("(/?assets/[^"]+)"\)', s):
        if not datei(ziel(u, von)[0]): fehler.append(f'{von}: CSS-Datei fehlt: {u}')
mehrfach = {t: z for t, z in anker_ziele.items() if len(z) > 1}
for t, z in sorted(mehrfach.items()):
    fehler.append(f'Ankertext „{t}“ zeigt auf {len(z)} Seiten: ' + '; '.join(f'{k} (von {", ".join(sorted(v))[:120]})' for k, v in z.items()))
print('\n'.join(fehler) if fehler else 'Keine Fehler'); print(len(fehler), 'Befunde,', len(mehrfach), 'Ankertexte mit mehreren Zielen')
