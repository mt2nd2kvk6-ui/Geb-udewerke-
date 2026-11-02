#!/usr/bin/env python3
"""Setzt Title/Description/H1/Textstellen aus projekt/seo/meta_2026.py in die Seiten ein.
Ersetzt jeweils alle Kopien (title, og:title, twitter:title, JSON-LD name/headline/description)."""
import html, json, os, re, sys
BASIS = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); WEB = os.path.join(BASIS, 'website')
sys.path.insert(0, os.path.join(BASIS, 'projekt', 'seo')); from meta_2026 import SPEC
def attr(t): return html.escape(t, quote=True).replace('&#x27;', "'")
def js(t): return json.dumps(t, ensure_ascii=False)[1:-1]
fehler = []
for seite, sp in SPEC.items():
    p = os.path.join(WEB, seite); s = open(p, encoding='utf-8').read(); alt = s
    if 't' in sp:
        ot = html.unescape(re.search(r'<title>(.*?)</title>', s, re.S).group(1).strip())
        for a, b in ((attr(ot), attr(sp['t'])), (js(ot), js(sp['t'])), (ot, sp['t'])):
            s = s.replace('"' + a + '"', '"' + b + '"').replace('>' + a + '<', '>' + b + '<')
        # PHP-Seite: Title kann im PHP-Code stehen
    if 'd' in sp:
        od = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', s).group(1))
        for a, b in ((attr(od), attr(sp['d'])), (js(od), js(sp['d']))):
            s = s.replace('"' + a + '"', '"' + b + '"')
    if sp.get('h1'):
        m = re.search(r'(<h1[^>]*>)(.*?)(</h1>)', s, re.S)
        oh = m.group(2).strip()
        s = s[:m.start()] + m.group(1) + html.escape(sp['h1'], quote=False) + m.group(3) + s[m.end():]
        s = s.replace('"headline":"' + js(html.unescape(oh)) + '"', '"headline":"' + js(sp['h1']) + '"')
    for a, b in sp.get('txt', []):
        if a in s: s = s.replace(a, b)          # sichtbarer Text und gleichlautende JSON-LD-Kopie
        elif b not in s: fehler.append(f'{seite}: Textstelle nicht gefunden: {a[:50]}')
    t_neu = html.unescape(re.search(r'<title>(.*?)</title>', s, re.S).group(1).strip())
    if 't' in sp and t_neu != sp['t']: fehler.append(f'{seite}: Title nicht ersetzt')
    if s != alt: open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('\n'.join(fehler) or 'alle Ersetzungen ok')
