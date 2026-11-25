#!/usr/bin/env python3
"""Gleicht jeden Eurobetrag der Website mit den Preistabellen auf preise.html ab.

Gültig sind nur Beträge, die in einer Preistabelle (<table>) auf preise.html stehen, dazu der
Mülltonnenservice (77 € netto, 92 € brutto, steht auf preise.html als Text). Jahreswerte gelten,
wenn sie genau 12 x einem Monatswert aus der Tabelle entsprechen und im Satz „Jahr“ steht. Geprüft werden sichtbarer Text, Meta-Tags, JSON-LD und llms.txt.
Alte Werte vor der Senkung um 15 % vom 02.11.2026 werden immer als Befund gemeldet.

Aufruf: python3 werkzeuge/preise_pruefen.py [--liste]   (--liste gibt jede Fundstelle aus)"""
import glob, html, os, re, sys

BASIS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(BASIS, 'website')
BETRAG = re.compile(r'(?<![\d.,])(\d{1,3}(?:\.\d{3})*)(?:,\d{2})?(?:&nbsp;|\s| | )?€')
# Werte vor dem 02.11.2026 (netto und brutto), siehe projekt/seo/preise-angeglichen-2026-11-07.txt
ALT = {'130', '190', '280', '155', '226', '333', '150', '175', '235', '449', '705', '1.049', '2.075',
       '1.435', '1.708', '2.100', '2.499', '90', '107'}


def gueltige_werte():
    s = open(os.path.join(WEB, 'preise.html'), encoding='utf-8').read()
    werte = set()
    for t in re.findall(r'<table\b.*?</table>', s, re.S):
        werte |= set(BETRAG.findall(t))
    m = re.search(r'Mülltonnenservice.{0,200}?Richtpreis ab (\d+)&nbsp;€ netto im Monat, brutto ab (\d+)&nbsp;€', s, re.S) or \
        re.search(r'Mülltonnenservice.{0,200}?Richtpreis ab (\d+) € netto im Monat, brutto ab (\d+) €', s, re.S)
    if m:
        werte |= {m.group(1), m.group(2)}
    return werte


def bereiche(s):
    """Zerlegt eine Seite in (Art, Text): jsonld, meta, sichtbar."""
    teile = []
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        teile.append(('JSON-LD', m.group(1)))
    for m in re.finditer(r'<meta [^>]*content="([^"]*€[^"]*)"', s):
        teile.append(('Meta', html.unescape(m.group(1))))
    t = re.sub(r'<(script|style|svg)\b.*?</\1>', ' ', s, flags=re.S)
    t = re.sub(r'<head>.*?</head>', ' ', t, flags=re.S)
    t = html.unescape(re.sub(r'<[^>]+>', ' ', t))
    teile.append(('sichtbar', re.sub(r'\s+', ' ', t)))
    return teile


def pruefen(liste=False):
    gueltig = gueltige_werte()
    dateien = sorted(glob.glob(WEB + '/*.html') + glob.glob(WEB + '/ratgeber/*.html') + [WEB + '/ratgeber/index.php', WEB + '/llms.txt'])
    befunde, alle = [], []
    for p in dateien:
        s = open(p, encoding='utf-8').read()
        name = os.path.relpath(p, WEB)
        teile = [('llms.txt', s)] if p.endswith('.txt') else bereiche(s)
        for art, text in teile:
            for m in BETRAG.finditer(text):
                w = m.group(1)
                kontext = re.sub(r'\s+', ' ', html.unescape(text[max(0, m.start() - 70):m.end() + 25])).replace('&nbsp;', ' ')
                if w in ALT and w not in gueltig:
                    status = 'ALTER WERT'
                elif w in gueltig:
                    status = 'ok'
                elif any(int(w.replace('.', '')) == 12 * int(g.replace('.', '')) for g in gueltig) and 'Jahr' in kontext:
                    status = 'ok (12 x Monatswert)'
                else:
                    status = 'nicht in preise.html'
                alle.append((name, art, w, status, kontext))
                if not status.startswith('ok'):
                    befunde.append(f'{name} [{art}] {w} €: {status}  …{kontext}…')
    if liste:
        for name, art, w, status, kontext in alle:
            print(f'{status:22} {w:>7} €  {name:58} {art:9} …{kontext}…')
    print('\n'.join(befunde) if befunde else 'Keine Fehler')
    print(len(befunde), 'Befunde,', len(alle), 'Eurobeträge geprüft, gültige Werte aus preise.html:', len(gueltig))
    return befunde, alle


if __name__ == '__main__':
    pruefen('--liste' in sys.argv)
