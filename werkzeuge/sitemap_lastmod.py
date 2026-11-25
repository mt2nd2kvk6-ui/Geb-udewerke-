#!/usr/bin/env python3
"""Setzt <lastmod> in website/sitemap.xml und dateModified im JSON-LD je Seite auf das Datum der
letzten inhaltlichen Änderung.

Inhalt = Title, Description, H1 und Text in <main>, ohne automatisch erzeugte Bausteine
(Bewertungs-Laufband, Vertrauensstreifen, Kontaktband, Autorenbox, Ratgeber-Teaser) und ohne
Kopf, Navigation, Fuß, CSS und Skripte. Eine reine Gestaltungsänderung verschiebt lastmod also nicht.

Datum einer Änderung = Datum des Commits, mit dem sie live ging:
- Commits vom 07.11.2026 (Zweig claude/gallant-einstein-ossqki nach 70c8eb2) waren nie live und
  werden übersprungen, ihr Inhalt geht erst mit dem Relaunch online.
- Änderungen nach dem Stand vom 16.11.2026 (0638e7d) und im Arbeitsverzeichnis gehen mit dem
  Installer live und bekommen das Datum aus --live (Standard: heute).
- ratgeber/ listet die Beiträge automatisch: lastmod ist zusätzlich mindestens das Datum des
  neuesten bis --live erschienenen Beitrags.
Aufruf: python3 werkzeuge/sitemap_lastmod.py [--live JJJJ-MM-TT] [--pruefen]"""
import datetime, glob, html, os, re, subprocess, sys

BASIS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(BASIS, 'website')
LIVE = sys.argv[sys.argv.index('--live') + 1] if '--live' in sys.argv else datetime.date.today().isoformat()
PRUEFEN = '--pruefen' in sys.argv
STAND_1611 = '0638e7d'          # letzter Live-Stand vor dem Relaunch
NIE_LIVE_VON, NIE_LIVE_BIS = '70c8eb2', 'f38d527'   # Neuauftritt 07.11.2026, nicht ausgeliefert


def git(*a):
    return subprocess.run(['git', *a], cwd=BASIS, capture_output=True, text=True).stdout


def inhalt(s):
    if not s:
        return ''
    t = re.search(r'<title>(.*?)</title>', s, re.S)
    d = re.search(r'<meta name="description" content="([^"]*)"', s)
    m = re.search(r'<main\b.*?</main>', s, re.S)
    m = m.group(0) if m else ''
    for muster in (r'<!-- bewertungen:start.*?<!-- bewertungen:ende -->', r'<!-- vertrauen:start.*?<!-- vertrauen:ende -->',
                   r'<!-- autorenbox:start.*?<!-- autorenbox:ende -->', r'<section class="cta-band".*?</section>',
                   r'<ul class="weitere">.*?</ul>', r'<div class="weiterlesen">.*?</div>', r'<(script|style|svg)\b.*?</\1>',
                   r'<\?php.*?\?>'):
        m = re.sub(muster, ' ', m, flags=re.S)
    text = html.unescape(re.sub(r'<[^>]+>', ' ', m))
    return re.sub(r'\s+', ' ', ' '.join([t.group(1) if t else '', d.group(1) if d else '', text])).strip()


def urls():
    s = open(os.path.join(WEB, 'sitemap.xml'), encoding='utf-8').read()
    return re.findall(r'<loc>https://gebaeudewerke\.de/([^<]*)</loc>', s)


def datei(pfad):
    return 'index.html' if pfad == '' else ('ratgeber/index.php' if pfad == 'ratgeber/' else pfad)


def lastmod(name):
    nie_live = set(git('rev-list', f'{NIE_LIVE_VON}..{NIE_LIVE_BIS}').split())
    nach_1611 = set(git('rev-list', f'{STAND_1611}..HEAD').split())
    zeilen = git('log', '--first-parent', '--reverse', '--format=%H %ad', '--date=short', 'HEAD', '--', 'website/' + name).split('\n')
    vorher, datum = None, None
    for z in filter(None, zeilen):
        h, d = z.split()
        if h in nie_live:
            continue
        jetzt = inhalt(git('show', f'{h}:website/{name}'))
        if jetzt != vorher:
            datum = LIVE if h in nach_1611 else d
        vorher = jetzt
    arbeit = inhalt(open(os.path.join(WEB, name), encoding='utf-8').read())
    if arbeit != vorher:
        datum = LIVE
    if name == 'ratgeber/index.php':
        erschienen = []
        for p in glob.glob(os.path.join(WEB, 'ratgeber', '*.html')):
            m = re.search(r'<meta name="artikel-datum" content="(\d{4}-\d{2}-\d{2})"', open(p, encoding='utf-8').read(20000))
            if m and m.group(1) <= LIVE:
                erschienen.append(m.group(1))
        datum = max([datum] + erschienen)
    return datum


if __name__ == '__main__':
    p = os.path.join(WEB, 'sitemap.xml')
    s = open(p, encoding='utf-8').read()
    neu = s
    for u in urls():
        d = lastmod(datei(u))
        # dieselbe Angabe im JSON-LD der Seite (WebPage.dateModified)
        q = os.path.join(WEB, datei(u))
        seite = open(q, encoding='utf-8').read()
        seite_neu = re.sub(r'"dateModified":"\d{4}-\d{2}-\d{2}"', f'"dateModified":"{d}"', seite)
        if seite_neu != seite and not PRUEFEN:
            open(q, 'w', encoding='utf-8', newline='\n').write(seite_neu)
        neu = re.sub(r'(<loc>https://gebaeudewerke\.de/' + re.escape(u) + r'</loc><lastmod>)[^<]*(</lastmod>)', r'\g<1>' + d + r'\g<2>', neu)
        print(f'{d}  /{u}')
    if neu != s and not PRUEFEN:
        open(p, 'w', encoding='utf-8', newline='\n').write(neu)
    print(('Würde ändern' if PRUEFEN else 'Geschrieben') if neu != s else 'Unverändert', '(Relaunch live ab', LIVE + ')')
