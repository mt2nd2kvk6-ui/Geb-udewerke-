#!/usr/bin/env python3
"""Zählt die Wörter im Inhalt jeder Seite (nur <main>, ohne Navigation und Fußbereich).
Aufklappbare Bereiche (<details>) zählen mit, Skripte, Styles und SVG nicht.
Gezählt wird die Seite so, wie der Server sie ausliefert (lokaler Testserver, inkl. auslieferung.php).
Aufruf: python3 werkzeuge/wortzahl.py [--speichern DATEI] [--server http://127.0.0.1:8095]"""
import html, json, os, re, sys, urllib.request, urllib.error
BASIS = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); WEB = os.path.join(BASIS, 'website')
SERVER = sys.argv[sys.argv.index('--server') + 1] if '--server' in sys.argv else 'http://127.0.0.1:8095'
WORT = re.compile(r'[0-9A-Za-zÄÖÜäöüßéèàáç]+(?:[-’\'][0-9A-Za-zÄÖÜäöüßéèàáç]+)*')

def urls():
    l = ['/'] + ['/' + f for f in sorted(os.listdir(WEB)) if f.endswith('.html') and f != 'index.html']
    l += ['/ratgeber/'] + ['/ratgeber/' + f for f in sorted(os.listdir(os.path.join(WEB, 'ratgeber'))) if f.endswith('.html')]
    return l

def text(s):
    s = re.sub(r'<(script|style|svg|template)\b.*?</\1>', ' ', s, flags=re.S | re.I)
    s = re.sub(r'<br\s*/?>|</(p|li|h[1-6]|td|th|dt|dd|div|summary|figcaption|blockquote)>', ' \n ', s, flags=re.I)
    return html.unescape(re.sub(r'<[^>]+>', ' ', s))

def zaehlen(seite_html):
    m = re.search(r'<main\b.*?</main>', seite_html, re.S)
    inhalt = m.group(0) if m else seite_html
    return len(WORT.findall(text(inhalt)))

def holen(u):
    try:
        r = urllib.request.urlopen(SERVER + u)
        return r.status, r.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        return e.code, ''

if __name__ == '__main__':
    erg = {}
    for u in urls():
        st, s = holen(u)
        if st != 200: continue
        robots = re.search(r'<meta name="robots" content="([^"]*)"', s)
        noindex = bool(robots and 'noindex' in robots.group(1))
        erg[u] = {'woerter': zaehlen(s), 'noindex': noindex}
    for u, d in erg.items():
        print(f"{d['woerter']:6}  {'noindex ' if d['noindex'] else '        '}{u}")
    if '--speichern' in sys.argv:
        z = sys.argv[sys.argv.index('--speichern') + 1]
        json.dump(erg, open(z, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print('gespeichert:', z)
