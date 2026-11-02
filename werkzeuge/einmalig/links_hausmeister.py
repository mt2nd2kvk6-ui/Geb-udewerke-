#!/usr/bin/env python3
"""Einmalig 02.11.2026: mehr Links im Fließtext auf hausmeisterservice.html.
Je Seite (außer der Zielseite und noindex-Seiten) wird das erste unverlinkte Vorkommen von
'Hausmeisterservice' in einem Textabsatz verlinkt, sofern im Fließtext noch kein Link darauf steht."""
import glob, os, re
WEB = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'website')
ZIEL = re.compile(r'href="(?:/|\.\./)?hausmeisterservice\.html"')
neu, schon = [], []
for p in sorted(glob.glob(WEB + '/*.html') + glob.glob(WEB + '/ratgeber/*.html')):
    d = os.path.relpath(p, WEB)
    if d == 'hausmeisterservice.html': continue
    s = open(p, encoding='utf-8').read()
    if 'noindex' in (re.search(r'name="robots" content="([^"]*)"', s) or [None, ''])[1]: continue
    m = re.search(r'<main.*?</main>', s, re.S); main = m.group(0)
    # nur echter Fließtext: <p> ohne Klasse in Inhaltsbereichen, keine generierten Blöcke
    inhalt = re.sub(r'<!-- (bewertungen|vertrauen|autorenbox):start.*?:ende -->', lambda x: ' ' * len(x.group(0)), main, flags=re.S)
    ps = [x for x in re.finditer(r'<p(?: class="(?:kurzantwort|lead|seitenkopf__text|einleitung)[^"]*")?>(.*?)</p>', inhalt, re.S)]
    if any(ZIEL.search(x.group(0)) for x in ps): schon.append(d); continue
    href = '/hausmeisterservice.html' if d.startswith('ratgeber/') else 'hausmeisterservice.html'
    for x in ps:
        t = x.group(1)
        # erstes Vorkommen außerhalb eines Links
        for w in re.finditer(r'(?<![\wÄÖÜäöüß-])Hausmeisterservice(?![\wÄÖÜäöüß-])', t):
            vor = t[:w.start()]
            if vor.count('<a ') > vor.count('</a>'): continue
            neu_t = t[:w.start()] + f'<a href="{href}">Hausmeisterservice</a>' + t[w.end():]
            a = m.start() + x.start(1)
            s = s[:a] + neu_t + s[a + len(t):]
            open(p, 'w', encoding='utf-8').write(s); neu.append(d); break
        else: continue
        break
print('neu verlinkt:', len(neu), neu); print('hatten schon Link im Text:', len(schon))
alle = [os.path.relpath(p, WEB) for p in sorted(glob.glob(WEB + '/*.html') + glob.glob(WEB + '/ratgeber/*.html'))]
print('ohne Link:', [d for d in alle if d not in neu and d not in schon and d != 'hausmeisterservice.html'])
