#!/usr/bin/env python3
"""Prüft alle Seiten: Title/Description in Pixeln (Seobility: Arial 20 px / 14 px, gemessen mit
der metrisch identischen Liberation Sans), Duplikate, Title = H1, Wörter aus Title/H1 im Fließtext.
Aufruf: python3 werkzeuge/seo_pruefen.py [--tabelle]"""
import glob, html, json, os, re, sys
from PIL import ImageFont
BASIS = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); WEB = os.path.join(BASIS, 'website')
FONT = '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
T_MAX, D_MAX = 575, 990
F20, F14 = ImageFont.truetype(FONT, 20), ImageFont.truetype(FONT, 14)
def px20(t): return round(F20.getlength(t))
def px14(t): return round(F14.getlength(t))
STOP = set('und oder der die das den dem des ein eine einer eines einem einen für mit von im in am an auf zu zur zum bei aus nach vor ist sind was wie wann wer ohne statt sie ihr ihre ihren ihrem es was|'.split())

def seiten():
    l = sorted(glob.glob(WEB + '/*.html')) + sorted(glob.glob(WEB + '/ratgeber/*.html')) + [WEB + '/ratgeber/index.php']
    return [p for p in l if not os.path.basename(p).startswith('_')]

def text(s):
    s = re.sub(r'<(script|style|svg)\b.*?</\1>', ' ', s, flags=re.S)
    return html.unescape(re.sub(r'<[^>]+>', ' ', s))

def woerter(t): return [w for w in re.findall(r'[\wÄÖÜäöüß-]+', t) if w.lower() not in STOP and not w.isdigit() or w.isdigit() and len(w) == 4]

def lesen(p):
    if not p.endswith('.php'):
        return open(p, encoding='utf-8').read()
    import subprocess
    ht = os.path.join(WEB, '.htaccess'); da = os.path.exists(ht)
    out = subprocess.run(['php', p], capture_output=True, text=True, cwd=os.path.dirname(p)).stdout
    if not da and os.path.exists(ht): os.remove(ht)   # einrichtung.php legt sie an
    return out

def daten(p):
    s = lesen(p)
    t = html.unescape(re.search(r'<title>(.*?)</title>', s, re.S).group(1).strip())
    d = re.search(r'<meta name="description" content="([^"]*)"', s); d = html.unescape(d.group(1)) if d else ''
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S); h1 = re.sub(r'\s+', ' ', text(h1.group(1))).strip() if h1 else ''
    main = re.search(r'<main.*?</main>', s, re.S); main = main.group(0) if main else s
    fliess = re.sub(r'<h1[^>]*>.*?</h1>', ' ', main, flags=re.S)
    fliess = re.sub(r'<!-- bewertungen:start.*?<!-- bewertungen:ende -->', ' ', fliess, flags=re.S)
    ft = ' ' + re.sub(r'\s+', ' ', text(fliess)).lower() + ' '
    noindex = 'noindex' in (re.search(r'<meta name="robots" content="([^"]*)"', s) or [None, ''])[1]
    h1m = re.search(r'<h1[^>]*>.*?</h1>', main, re.S)
    ps = [re.sub(r'\s+', ' ', text(x)).strip() for x in re.findall(r'<p\b[^>]*>(.*?)</p>', main[h1m.end():] if h1m else main, re.S)]
    lead = next((x for x in ps if 'veröffentlicht am' not in x and len(x) > 60), '')
    return dict(seite=os.path.relpath(p, WEB), title=t, desc=d, h1=h1, lead=lead, tpx=px20(t), dpx=px14(d), noindex=noindex, fliess=ft)

if __name__ == '__main__':
    alle = [daten(p) for p in seiten()]
    fehler = []
    for k in ('title', 'desc'):
        z = {}
        for a in alle: z.setdefault(a[k], []).append(a['seite'])
        fehler += [f'Doppelt ({k}): {v}' for t, v in z.items() if len(v) > 1]
    for a in alle:
        if a['tpx'] > T_MAX: fehler.append(f"{a['seite']}: Title {a['tpx']} px > {T_MAX}")
        if a['dpx'] > D_MAX: fehler.append(f"{a['seite']}: Description {a['dpx']} px > {D_MAX}")
        if not a['desc']: fehler.append(f"{a['seite']}: keine Description")
        if a['title'].strip().lower() == a['h1'].strip().lower(): fehler.append(f"{a['seite']}: Title = H1")
        if a['noindex']: continue
        fehlend = sorted({w for w in woerter(a['title'].replace('|', ' ') + ' ' + a['h1'])
                          if not re.search(r'(?<![\wÄÖÜäöüß])' + re.escape(w.lower()) + r'(?![\wÄÖÜäöüß])', a['fliess'])})
        if fehlend: fehler.append(f"{a['seite']}: nicht im Fließtext: {', '.join(fehlend)}")
    kw = json.load(open(os.path.join(BASIS, 'projekt', 'seo', 'hauptkeywords.json'), encoding='utf-8'))
    z = {}
    for k in kw.values(): z[k.lower()] = z.get(k.lower(), 0) + 1
    fehler += [f'Keyword doppelt: {k}' for k, n in z.items() if n > 1]
    FUELL = {'und', 'der', 'die', 'das', 'dem', 'auf', 'in', 'ein', 'für', 'im', 'einem', 'was', 'zum', 'nach'}
    for a in alle:
        k = kw.get(a['seite'])
        if a['seite'].startswith('ratgeber/') and a['seite'] != 'ratgeber/index.php' and '2026' not in a['title']:
            fehler.append(f"{a['seite']}: 2026 fehlt im Title")
        if a['seite'] in ('ratgeber/treppenhausreinigung-bruchsal.html', 'ratgeber/bueroreinigung-praxisreinigung-bruchsal.html') and 'bruchsal' in a['title'].lower():
            fehler.append(f"{a['seite']}: Bruchsal im Title")
        if not k: continue
        for feld in ('title', 'desc', 'h1', 'lead'):
            f = [w for w in re.findall(r'[\wÄÖÜäöüß]+', k) if w.lower() not in FUELL and w.lower() not in a[feld].lower()]
            if f: fehler.append(f"{a['seite']}: Keyword-Wörter fehlen in {feld}: {f}")
    if '2026' not in alle[[a['seite'] for a in alle].index('preise.html')]['title']: fehler.append('preise.html: 2026 fehlt')
    if '--tabelle' in sys.argv:
        for a in alle: print(f"{a['tpx']:4} {a['dpx']:4} {a['seite']:55} {a['title']}  ||  H1: {a['h1']}")
    print('\n'.join(fehler) if fehler else 'Keine Fehler'); print(len(fehler), 'Befunde')
