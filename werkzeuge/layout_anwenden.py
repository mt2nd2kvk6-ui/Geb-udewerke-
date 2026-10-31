#!/usr/bin/env python3
"""Gebäudewerke: gemeinsames Layout auf alle Seiten anwenden.

Aufruf (beliebig oft wiederholbar):   python3 werkzeuge/layout_anwenden.py
Nur prüfen, nichts schreiben:          python3 werkzeuge/layout_anwenden.py --pruefen

Was das Skript macht (seitenspezifische Inhalte bleiben unangetastet):
  1. <head>: ersetzt Icons, Font-Preload, CSS und Skript-Einbindung durch den Block
     <!-- layout:kopf-start --> … <!-- layout:kopf-ende -->. Titel, Meta-Tags,
     Canonical, Artikel-Metas und JSON-LD bleiben erhalten.
     CSS-Quelle ist website/assets/css/style.css. Sie wird verkleinert und inline
     geschrieben (keine render-blockierende CSS-Datei, ca. 8 KB gzip pro Seite).
  2. Alles zwischen <body> und <main id="inhalt"> (Infoleiste, Kopf, Navigation)
     und alles zwischen </main> und </body> (Fuß, Schnellkontakt, mobile Leiste)
     wird neu erzeugt. aria-current wird pro Seite gesetzt.
  3. In <main>: Google-Bewertungen zwischen <!-- bewertungen:start --> und
     <!-- bewertungen:ende --> werden neu erzeugt (Startseite, Leistungsseiten,
     Kontakt). Fehlt der Block, wird er an der vorgesehenen Stelle eingefügt.
     Ratgeber-Links in <ul class="weitere"> und <div class="weiterlesen"> werden
     zu Bildkarten (<li><a class="teaser" href="…">…</a></li>, kompatibel mit
     auslieferung.php, das Links auf geplante Beiträge entfernt).
     Vertrauensstreifen (<!-- vertrauen:start -->) unter dem ersten Abschnitt der
     Startseite und der Leistungsseiten; Autorenbox (<!-- autorenbox:start -->) am
     Ende jedes Ratgeberartikels (Autor aus "von NAME" in .beitrag-meta, Daten aus
     artikel-datum / artikel-aktualisiert, Zuständigkeit aus TEAM unten).
  4. JSON-LD: Firmen-Entität (#organisation) bekommt aggregateRating, die
     Startseite zusätzlich review[] (Bewertungen mit Text). Alter Google-Link wird
     überall durch den aktuellen ersetzt (auch llms.txt).

BEWERTUNGEN PFLEGEN (Inhaber):
  Alle Zahlen und Texte kommen aus projekt/google-profil.json:
  bewertung_schnitt, bewertung_anzahl, bewertungen[] (name, sterne, datum, text,
  optional thema), profil_link, bewertung_schreiben, abgerufen (= "Stand").
  Neue Bewertung: Eintrag oben in "bewertungen" ergänzen, Anzahl/Schnitt und
  "abgerufen" anpassen, dann dieses Skript ausführen. Schema, Badge in Kopf/Fuß
  und Laufband werden dabei überall aktualisiert. Nichts in den HTML-Dateien
  von Hand ändern.
"""
import glob, hashlib, html, json, os, re, sys

BASIS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(BASIS, 'website')
PROFIL = json.load(open(os.path.join(BASIS, 'projekt', 'google-profil.json'), encoding='utf-8'))
PRUEFEN = '--pruefen' in sys.argv

ALT_GOOGLE = 'https://share.google/v7XolrfYaCO55YrZz'
GOOGLE = PROFIL['profil_link']
SCHREIBEN = PROFIL['bewertung_schreiben']
SCHNITT = float(PROFIL['bewertung_schnitt'])
ANZAHL = int(PROFIL['bewertung_anzahl'])
MONATE = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August',
          'September', 'Oktober', 'November', 'Dezember']


def monat(datum):
    j, m = datum[:4], int(datum[5:7])
    return f'{MONATE[m - 1]} {j}'


STAND = monat(PROFIL['abgerufen'])
SCHNITT_DE = f'{SCHNITT:.1f}'.replace('.', ',')

LEISTUNGEN = [
    ('hausmeisterservice.html', 'Hausmeisterservice'),
    ('treppenhausreinigung.html', 'Treppenhausreinigung'),
    ('gebaeudereinigung.html', 'Gebäudereinigung'),
    ('bueroreinigung.html', 'Büroreinigung'),
    ('gartenpflege.html', 'Gartenpflege'),
    ('winterdienst.html', 'Winterdienst'),
    ('entruempelung.html', 'Entrümpelung und Haushaltsauflösung'),
    ('wohnungsuebergabe.html', 'Wohnungsübergabe'),
    ('kleinreparaturen.html', 'Kleinreparaturen'),
    ('metallarbeiten-schloesser.html', 'Metallarbeiten und Schlösser'),
]
FUSS_LEISTUNGEN = [
    ('hausmeisterservice.html', 'Hausmeisterservice Bruchsal'),
    ('treppenhausreinigung.html', 'Treppenhausreinigung'),
    ('gebaeudereinigung.html', 'Gebäudereinigung Bruchsal'),
    ('bueroreinigung.html', 'Büro- und Praxisreinigung'),
    ('gartenpflege.html', 'Gartenpflege Bruchsal'),
    ('winterdienst.html', 'Winterdienst Bruchsal'),
    ('entruempelung.html', 'Entrümpelung Bruchsal'),
    ('wohnungsuebergabe.html', 'Wohnungsübergabe mit Protokoll'),
    ('kleinreparaturen.html', 'Handwerkerservice'),
    ('metallarbeiten-schloesser.html', 'Schlösser und Metallarbeiten'),
]
HAUPT = [('preise.html', 'Preise'), ('einsatzgebiet.html', 'Einsatzgebiet'),
         ('ratgeber/', 'Ratgeber'), ('ueber-uns.html', 'Über uns'), ('kontakt.html', 'Kontakt')]

# Bewertungen: Seite -> (Variante, bevorzugtes Thema, Einfügen vor diesem Muster)
BEWERTUNG_SEITEN = {
    'index.html': ('voll', None, r'<section[^>]*aria-labelledby="zusagen-titel"'),
    'kontakt.html': ('kompakt', None, r'<section[^>]*aria-labelledby="anfahrt-titel"'),
    'gebaeudereinigung.html': ('kompakt', 'Gebäudereinigung', r'<section class="cta-band"'),
    'metallarbeiten-schloesser.html': ('kompakt', 'Schlösser', r'<section class="cta-band"'),
    'kleinreparaturen.html': ('kompakt', 'Schlösser', r'<section class="cta-band"'),
    'treppenhausreinigung.html': ('kompakt', 'Gebäudereinigung', r'<section class="cta-band"'),
    'bueroreinigung.html': ('kompakt', 'Gebäudereinigung', r'<section class="cta-band"'),
    'einsatzgebiet.html': ('kompakt', None, r'<section class="cta-band"'),
}
for _s, _ in LEISTUNGEN:
    BEWERTUNG_SEITEN.setdefault(_s, ('kompakt', None, r'<section class="cta-band"'))

TEL = 'tel:+491637221790'
WA = ('https://api.whatsapp.com/send?phone=491637221790&text=Hallo%20Geb%C3%A4udewerke%2C%20'
      'ich%20habe%20eine%20Anfrage%20zu%20einem%20Objekt.')


def svg(pfade, klasse=''):
    k = f' class="{klasse}"' if klasse else ''
    return ('<svg' + k + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">' + pfade + '</svg>')


I_TEL = svg('<path d="M5 3.5h3.2l1.6 4.2-2 1.3a11 11 0 0 0 5.2 5.2l1.3-2 4.2 1.6V17a2 2 0 0 1-2.2 2A15.5 15.5 0 0 1 3 5.7 2 2 0 0 1 5 3.5z"/>')
I_WA = svg('<path d="M4 5h16v11H9l-4.5 3.5V16H4z"/><path d="M8 9.5h8M8 12.5h5"/>')
I_FORM = svg('<path d="M4 4h16v16H4z"/><path d="M8 9h8M8 13h8M8 17h5"/>')
I_ZU = svg('<path d="M6 6l12 12M18 6L6 18"/>')
I_MENUE = svg('<path d="M4 7h16M4 12h16M4 17h16"/>')
I_RUNTER = svg('<path d="M5 9l7 7 7-7"/>')
I_PFEIL = svg('<path d="M5 12h14M13 6l6 6-6 6"/>')
I_PAUSE = svg('<path d="M9 5v14M15 5v14"/>')
STERN = 'M12 2.5l2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.4l-5.9 3.1 1.2-6.5L2.5 9.4l6.6-.9z'


def sterne(anzahl=5, beschriftet=False):
    pfad = ''.join(f'<path transform="translate({i * 25} 0)" d="{STERN}"/>' for i in range(anzahl))
    if beschriftet:
        return (f'<span class="sterne" role="img" aria-label="{anzahl} von 5 Sternen">'
                f'<svg viewBox="0 0 121 24" fill="currentColor" aria-hidden="true" focusable="false">{pfad}</svg></span>')
    return (f'<span class="sterne" aria-hidden="true"><svg viewBox="0 0 121 24" fill="currentColor" '
            f'focusable="false">{pfad}</svg></span>')


G_LOGO = ('<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M21.6 12.2c0-.7-.1-1.4-.2-2H12v3.8h5.4a4.6 4.6 0 0 1-2 3v2.5h3.2c1.9-1.7 3-4.3 3-7.3z" opacity=".9"/>'
          '<path fill="currentColor" d="M12 22c2.7 0 5-.9 6.6-2.4l-3.2-2.5c-.9.6-2 1-3.4 1a6 6 0 0 1-5.6-4.1H3.1v2.6A10 10 0 0 0 12 22z" opacity=".75"/>'
          '<path fill="currentColor" d="M6.4 14a6 6 0 0 1 0-3.9V7.5H3.1a10 10 0 0 0 0 9z" opacity=".6"/>'
          '<path fill="currentColor" d="M12 6c1.5 0 2.8.5 3.9 1.5l2.9-2.9A10 10 0 0 0 3.1 7.5l3.3 2.6A6 6 0 0 1 12 6z" opacity=".45"/></svg>')


def badge(klasse='google-badge'):
    return (f'<a class="{klasse}" href="{GOOGLE}" rel="noopener" target="_blank">{sterne()}'
            f'<span><span class="visuell-versteckt">Bewertung </span><strong>{SCHNITT_DE}</strong>'
            f'<span class="visuell-versteckt"> von 5</span> · {ANZAHL} Google-Bewertungen</span></a>')


# ---------------------------------------------------------------- CSS / Kopf

def css_klein(css):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r'\s*([{};,>])\s*', r'\1', css)
    css = re.sub(r':\s+', ':', css)
    css = css.replace(';}', '}')
    # Leerzeichen in calc()/Selektoren mit + bleiben erhalten
    return css.strip()


CSS = css_klein(open(os.path.join(WEB, 'assets', 'css', 'style.css'), encoding='utf-8').read())


def version(pfad):
    return hashlib.md5(open(os.path.join(WEB, pfad), 'rb').read()).hexdigest()[:8]


V_CONSENT = version('assets/js/consent.js')
V_MAIN = version('assets/js/main.js')


def kopf_block(b):
    return ('<!-- layout:kopf-start (automatisch: werkzeuge/layout_anwenden.py, nicht von Hand ändern) -->\n'
            f'<link rel="icon" href="{b}favicon.ico" sizes="48x48">\n'
            f'<link rel="icon" href="{b}favicon.svg" type="image/svg+xml">\n'
            f'<link rel="icon" type="image/png" sizes="32x32" href="{b}favicon-32.png">\n'
            f'<link rel="apple-touch-icon" href="{b}apple-touch-icon.png">\n'
            f'<link rel="manifest" href="{b}site.webmanifest">\n'
            f'<link rel="preload" href="{b}assets/fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>\n'
            f'<style>{CSS.replace("{{BASIS}}", b)}</style>\n'
            f'<script src="{b}assets/js/consent.js?v={V_CONSENT}" defer></script>\n'
            f'<script src="{b}assets/js/main.js?v={V_MAIN}" defer></script>\n'
            '<!-- layout:kopf-ende -->')


ALTE_KOPF_TEILE = [
    r'<link rel="icon"[^>]*>\n?', r'<link rel="apple-touch-icon"[^>]*>\n?', r'<link rel="manifest"[^>]*>\n?',
    r'<link rel="preload"[^>]*archivo[^>]*>\n?', r'<style>.*?</style>\n?',
    r'<script src="[^"]*assets/js/(?:consent|main)\.js[^"]*"[^>]*></script>\n?',
]


def kopf_anwenden(s, b):
    block = kopf_block(b)
    m = re.search(r'<!-- layout:kopf-start.*?<!-- layout:kopf-ende -->', s, re.S)
    if m:
        return s[:m.start()] + block + s[m.end():]
    k_ende = s.index('</head>')
    kopf = s[:k_ende]
    pos = None
    for muster in ALTE_KOPF_TEILE:
        t = re.search(muster, kopf, re.S)
        if t and (pos is None or t.start() < pos):
            pos = t.start()
    for muster in ALTE_KOPF_TEILE:
        kopf = re.sub(muster, '\x00' if pos is not None else '', kopf, flags=re.S)
    if pos is None:
        kopf = kopf + block + '\n'
    else:
        kopf = kopf.replace('\x00', block + '\n', 1).replace('\x00', '')
    return kopf + s[k_ende:]


# ---------------------------------------------------------------- Kopf/Fuß im body

def aktuell(seite):
    """Liefert (aktiver Hauptpunkt, aktive Leistungsseite, Wert für aria-current)."""
    if seite in [l[0] for l in LEISTUNGEN]:
        return 'leistungen', seite
    if seite.startswith('ratgeber/'):
        return 'ratgeber/', None
    return seite, None


def header(seite, b):
    haupt, leistung = aktuell(seite)
    unter = ''.join(
        f'<li><a href="{b}{h}"' + (' aria-current="page"' if h == leistung else '') + f'>{t}</a></li>'
        for h, t in LEISTUNGEN)
    knopf_cur = ' aria-current="true"' if haupt == 'leistungen' else ''
    punkte = ''
    for h, t in HAUPT:
        cur = ''
        if h == haupt:
            cur = ' aria-current="page"' if (h != 'ratgeber/' or seite == 'ratgeber/index.php') else ' aria-current="true"'
        punkte += f'<li><a class="nav__link" href="{b}{h}"{cur}>{t}</a></li>\n'
    return f'''
<a class="sprunglink" href="#inhalt">Zum Inhalt springen</a>
<div class="leiste"><div class="wrap">
<span class="leiste__notdienst"><span class="leiste__punkt" aria-hidden="true"></span>Notdienst täglich 17 bis 24 Uhr: <a href="{TEL}">0163 7221790</a></span>
<span class="leiste__rechts">{badge('google-badge google-badge--leiste')}<span class="leiste__adresse">Für Bruchsal und den Landkreis Karlsruhe</span><span>Mo bis Fr 7 bis 17 Uhr</span></span>
</div></div>
<header class="kopf"><div class="wrap">
<a class="kopf__logo" href="/"><img src="{b}assets/img/logo-quer.svg" width="1716" height="442" alt="Gebäudewerke Logo, zur Startseite"></a>
<nav id="hauptnavigation" class="nav" aria-label="Hauptnavigation">
<button class="menue-knopf nav__schliessen" type="button" aria-label="Menü schließen">{I_ZU}</button>
<ul class="nav__liste">
<li><button class="nav__link" type="button" data-untermenue aria-expanded="false" aria-controls="unter-leistungen"{knopf_cur}>Leistungen {I_RUNTER}</button>
<ul class="nav__unter" id="unter-leistungen">{unter}</ul></li>
{punkte}</ul>
<div class="nav__mobil"><a class="btn btn--voll" href="{b}kontakt.html">{I_FORM}Angebot anfragen</a><a class="btn btn--rand" href="{TEL}">{I_TEL}0163 7221790</a><a class="btn btn--wa" href="{WA}" rel="noopener" target="_blank">{I_WA}WhatsApp</a></div>
</nav>
<div class="kopf__aktionen">
<a class="btn btn--rand" href="{TEL}">{I_TEL}Anrufen</a>
<a class="btn btn--voll" href="{b}kontakt.html">Angebot anfragen</a>
<button class="menue-knopf" id="menue-oeffnen" type="button" aria-controls="hauptnavigation" aria-expanded="false" aria-label="Menü öffnen">{I_MENUE}</button>
</div>
</div></header>
<div class="nav-schleier" aria-hidden="true"></div>
'''


def q(t):
    from urllib.parse import quote
    return quote(t, safe='')


def footer(seite, b, url, titel):
    leist = ''.join(f'<li><a href="{b}{h}">{t}</a></li>' for h, t in FUSS_LEISTUNGEN)
    teilen = (f'<p class="teilen">Seite teilen: <a href="https://wa.me/?text={q(url)}" rel="noopener" target="_blank">Per WhatsApp teilen</a> · '
              f'<a href="mailto:?subject={q(titel)}&amp;body={q(url)}">Per E-Mail teilen</a> · '
              '<a href="https://www.instagram.com/gebaeudewerke" rel="noopener" target="_blank">Gebäudewerke auf Instagram</a></p>')
    return f'''
<footer class="fuss"><div class="wrap">
<div class="fuss__cta">
<div><p class="fuss__cta-titel">Ein Ansprechpartner für Ihr Objekt in Bruchsal</p>{badge('google-badge google-badge--fuss')}</div>
<div class="btn-reihe"><a class="btn btn--hell" href="{b}kontakt.html">Anfrage senden</a><a class="btn btn--hellrand" href="{TEL}">{I_TEL}0163 7221790</a></div>
</div>
<div class="fuss__raster">
<div><a class="fuss__logo" href="/"><img src="{b}assets/img/logo-quer-weiss.svg" width="1716" height="442" alt="Gebäudewerke Logo, zur Startseite" loading="lazy"></a>
<p class="fuss__text">Hausmeisterservice, Gebäudereinigung, Gartenpflege und Winterdienst für Wohnanlagen, Eigentümergemeinschaften und Gewerbe in Bruchsal und im Landkreis Karlsruhe.</p>
<address>Gebäudewerke GbR<br>Allmend 2<br>76707 Hambrücken<br>Telefon: <a href="{TEL}">0163 7221790</a><br><a href="mailto:info@gebaeudewerke.de">E-Mail an info@gebaeudewerke.de</a></address></div>
<div><p class="fuss__titel">Leistungen</p><ul>{leist}</ul></div>
<div><p class="fuss__titel">Unternehmen</p><ul><li><a href="{b}preise.html">Preise und Richtpreise</a></li><li><a href="{b}einsatzgebiet.html">Einsatzgebiet</a></li><li><a href="{b}ueber-uns.html">Team und Unternehmen</a></li><li><a href="{b}ratgeber/">Ratgeber</a></li><li><a href="{b}karriere.html">Jobs bei Gebäudewerke</a></li><li><a href="{b}kontakt.html">Kontakt und Anfahrt</a></li></ul></div>
<div><p class="fuss__titel">Erreichbarkeit</p><ul><li>Büro: Mo bis Fr 7 bis 17 Uhr</li><li>Notdienst: täglich 17 bis 24 Uhr</li><li><a href="{b}einsatzgebiet.html">Einsatzgebiet: Bruchsal und Landkreis Karlsruhe</a></li><li><a href="{WA}" rel="noopener" target="_blank">Nachricht per WhatsApp</a></li><li><a href="{GOOGLE}" rel="noopener" target="_blank">Bewertungen auf Google</a></li></ul></div>
</div>
<div class="fuss__unten"><span>© 2026 Gebäudewerke GbR</span>{teilen}<ul><li><a href="{b}impressum.html">Impressum</a></li><li><a href="{b}datenschutz.html">Datenschutz</a></li><li><a href="{b}datenschutz.html#google-analytics" data-cookie-einstellungen>Cookie-Einstellungen</a></li></ul></div>
</div></footer>
<div class="schnellkontakt">
<a class="schnellkontakt__tel" href="{TEL}">{I_TEL}<span>Sofort anrufen</span></a>
<a class="schnellkontakt__wa" href="{WA}" rel="noopener" target="_blank">{I_WA}<span>WhatsApp-Chat</span></a>
</div>
<nav class="mobilleiste" aria-label="Schnellkontakt mobil">
<a href="{TEL}">{I_TEL}Anrufen</a>
<a class="mobilleiste__wa" href="{WA}" rel="noopener" target="_blank">{I_WA}WhatsApp</a>
<a href="{b}kontakt.html">{I_FORM}Anfrage</a>
</nav>
'''


# ---------------------------------------------------------------- Bewertungen

def bewertungen_html(variante, thema, hintergrund):
    liste = [r for r in PROFIL['bewertungen'] if r.get('text')]
    liste.sort(key=lambda r: r['datum'], reverse=True)
    if thema:
        liste.sort(key=lambda r: 0 if r.get('thema') == thema else 1)
    karten = ''
    for r in liste:
        name = html.escape(r['name'])
        text = html.escape(r['text'].strip()).replace('\n', ' ')
        karten += (f'<li class="bewertung"><figure>{sterne(int(r["sterne"]), True)}'
                   f'<blockquote><p>{text}</p></blockquote>'
                   f'<figcaption><span class="bewertung__initial" aria-hidden="true">{html.escape(r["name"][:1].upper())}</span>'
                   f'<span><strong>{name}</strong><span>{monat(r["datum"])} · Google</span></span></figcaption></figure></li>')
    klasse = 'abschnitt bewertungen' + (' abschnitt--kalk' if hintergrund == 'kalk' else '') + (' bewertungen--kompakt' if variante == 'kompakt' else '')
    titel = 'Was Kunden über uns sagen' if variante == 'voll' else 'Kundenstimmen auf Google'
    return f'''<!-- bewertungen:start
PFLEGE-HINWEIS: Dieser Block wird automatisch erzeugt. Nicht hier bearbeiten.
Neue Google-Bewertung: in projekt/google-profil.json unter "bewertungen" ergänzen
(name, sterne, datum JJJJ-MM-TT, text, optional thema), "bewertung_anzahl",
"bewertung_schnitt" und "abgerufen" anpassen, dann python3 werkzeuge/layout_anwenden.py
ausführen. Bewertungen ohne Text erscheinen nur in der Anzahl, nicht im Laufband.
-->
<section class="{klasse}" aria-labelledby="bewertungen-titel"><div class="wrap">
<div class="bewertungen__kopf">
<div><h2 id="bewertungen-titel">{titel}</h2>
<p class="bewertungen__schnitt">{sterne()}<strong>{SCHNITT_DE}</strong><span>von 5 · {ANZAHL} Google-Bewertungen</span></p></div>
<div class="btn-reihe"><a class="btn btn--rand" href="{GOOGLE}" rel="noopener" target="_blank">Alle Bewertungen auf Google</a><a class="btn btn--voll" href="{SCHREIBEN}" rel="noopener" target="_blank">Bewertung schreiben</a></div>
</div>
<div class="laufband" data-laufband tabindex="0" role="region" aria-label="Google-Bewertungen, horizontal scrollbar">
<div class="laufband__spur">
<ul class="laufband__gruppe">{karten}</ul>
<ul class="laufband__gruppe" aria-hidden="true">{karten.replace(' role="img" aria-label="5 von 5 Sternen"', ' aria-hidden="true"')}</ul>
</div>
</div>
<div class="bewertungen__fuss"><p class="bewertungen__hinweis">Bewertungen aus unserem Google-Unternehmensprofil, Stand {STAND}.</p><button class="laufband__knopf" type="button" hidden>{I_PAUSE}<span>Laufband anhalten</span></button></div>
</div></section>
<!-- bewertungen:ende -->'''


def bewertungen_anwenden(main, seite):
    if seite not in BEWERTUNG_SEITEN:
        return main
    variante, thema, vor = BEWERTUNG_SEITEN[seite]
    m = re.search(r'<!-- bewertungen:start.*?<!-- bewertungen:ende -->', main, re.S)
    if m:
        davor, danach = main[:m.start()], main[m.end():]
    else:
        t = re.search(vor, main)
        pos = t.start() if t else len(main)
        davor, danach = main[:pos], '\n' + main[pos:]
    sektionen = re.findall(r'<section class="([^"]*)"', davor)
    hg = 'weiss' if (sektionen and 'abschnitt--kalk' in sektionen[-1]) else 'kalk'
    if seite == 'index.html':
        hg = 'kalk'
    return davor + bewertungen_html(variante, thema, hg) + danach


# ---------------------------------------------------------------- Ratgeber-Teaser

ARTIKEL = {}
for _p in glob.glob(os.path.join(WEB, 'ratgeber', '*.html')):
    _s = open(_p, encoding='utf-8').read(20000)
    _m = lambda n: (re.search(r'<meta name="' + n + r'" content="([^"]*)"', _s) or [None, ''])[1]
    ARTIKEL[os.path.basename(_p)[:-5]] = {'bild': _m('artikel-bild'), 'thema': _m('artikel-thema')}

TEASER = re.compile(r'<li><a (?:class="teaser" )?href="((?:https://gebaeudewerke\.de)?/?ratgeber/([a-z0-9-]+)\.html)">(.*?)</a></li>', re.S)


def teaser_karte(m, b):
    href, slug, inhalt = m.group(1), m.group(2), m.group(3)
    t = re.search(r'<span class="teaser__titel">(.*?)</span>', inhalt, re.S)
    titel = t.group(1) if t else inhalt
    if '<' in titel or slug not in ARTIKEL or not ARTIKEL[slug]['bild']:
        return m.group(0)
    a = ARTIKEL[slug]
    bild = b + a['bild'].lstrip('/')
    thema = f'<span class="teaser__thema">{a["thema"]}</span>' if a['thema'] else ''
    return (f'<li><a class="teaser" href="{href}"><span class="teaser__bild"><img src="{bild}" width="800" height="600" alt="" loading="lazy" decoding="async"></span>'
            f'<span class="teaser__text">{thema}<span class="teaser__titel">{titel}</span>'
            f'<span class="teaser__mehr" aria-hidden="true">Weiterlesen {I_PFEIL}</span></span></a></li>')


def teaser_anwenden(main, b):
    def bereich(m):
        return TEASER.sub(lambda t: teaser_karte(t, b), m.group(0))
    main = re.sub(r'<ul class="weitere">.*?</ul>', bereich, main, flags=re.S)
    main = re.sub(r'<div class="weiterlesen">.*?</ul>', bereich, main, flags=re.S)
    return main


# ---------------------------------------------------------------- Vertrauensstreifen

VERTRAUEN_SEITEN = {'index.html', 'einsatzgebiet.html'} | {l[0] for l in LEISTUNGEN}
I_SCHILD = svg('<path d="M12 3l7 3v5.5c0 4.4-3 8-7 9.5-4-1.5-7-5.1-7-9.5V6z"/><path d="M9 12l2 2 4-4"/>')
I_TEAM = svg('<circle cx="9" cy="8" r="3"/><path d="M3.5 19a5.5 5.5 0 0 1 11 0"/><path d="M16 5.5a3 3 0 0 1 0 5.5M17.5 14.5a5.5 5.5 0 0 1 3 4.5"/>')
I_PREIS = svg('<rect x="5" y="4" width="14" height="17" rx="1"/><path d="M9 4V2.8h6V4"/><path d="M8.5 11.5l2 2 4.5-4.5"/><path d="M8.5 17h7"/>')


def vertrauen_html():
    return ('<!-- vertrauen:start (automatisch: werkzeuge/layout_anwenden.py) -->\n'
            '<div class="vertrauen"><div class="wrap"><ul class="vertrauen__liste">'
            f'<li><a class="vertrauen__google" href="{GOOGLE}" rel="noopener" target="_blank">{sterne()}<span><strong>{SCHNITT_DE} bei Google</strong>'
            f'<span>{ANZAHL} Bewertungen<span class="visuell-versteckt">, Durchschnitt {SCHNITT_DE} von 5</span></span></span></a></li>'
            f'<li>{I_SCHILD}<span><strong>Betriebshaftpflicht</strong><span>bis 5 Mio. Euro</span></span></li>'
            f'<li>{I_TEAM}<span><strong>Eigenes Personal</strong><span>keine Subunternehmer</span></span></li>'
            f'<li>{I_PREIS}<span><strong>Festpreis</strong><span>nach dem Ortstermin</span></span></li>'
            '</ul></div></div>\n<!-- vertrauen:ende -->')


def vertrauen_anwenden(main, seite):
    m = re.search(r'<!-- vertrauen:start.*?<!-- vertrauen:ende -->', main, re.S)
    if m:
        return main[:m.start()] + vertrauen_html() + main[m.end():] if seite in VERTRAUEN_SEITEN else main[:m.start()] + main[m.end():]
    if seite not in VERTRAUEN_SEITEN or '</section>' not in main:
        return main
    pos = main.index('</section>') + len('</section>')
    return main[:pos] + '\n' + vertrauen_html() + main[pos:]


# ---------------------------------------------------------------- Autorenbox (Ratgeber)

TEAM = {  # Name: (Anker auf ueber-uns.html, Zuständigkeit, Qualifikation laut Teamseite)
    'Fatih Altun': ('person-1', 'Metallarbeiten, Schlösser und Reparaturen', 'Geprüfter Industriemeister Metall (IHK)'),
    'Enes Yesildag': ('person-2', 'Vertrieb, Hausverwaltung und Wohnungsübergaben', 'Kaufmann, Vertrieb und Vermarktung'),
    'Burak Kartal': ('person-3', 'Qualität, Reinigung und Gartenpflege', 'Gelernter Metallbauer, Erfahrung im Stahl- und Gerüstbau'),
    'Julian Bender': ('person-4', 'Hausmeisterservice und Winterdienst', 'Gelernter Industriemechaniker'),
}


def datum_de(d):
    return f'{d[8:10]}.{d[5:7]}.{d[:4]}'


def autorenbox_anwenden(s, main):
    """Autorenbox am Ende des Artikeltextes. Autor aus <p class="beitrag-meta">… von NAME, …</p>,
    Daten aus meta artikel-datum / artikel-aktualisiert. Zuständigkeit siehe TEAM."""
    m = re.search(r'<!-- autorenbox:start.*?<!-- autorenbox:ende -->\n?', main, re.S)
    if m:
        main = main[:m.start()] + main[m.end():]
    a = re.search(r'class="beitrag-meta">[^<]*?von ([^,<]+)', main)
    if not a or a.group(1).strip() not in TEAM:
        return main
    name = a.group(1).strip()
    anker, rolle, quali = TEAM[name]
    d1 = re.search(r'<meta name="artikel-datum" content="([\d-]+)"', s)
    d2 = re.search(r'<meta name="artikel-aktualisiert" content="([\d-]+)"', s)
    daten = f'Veröffentlicht am {datum_de(d1.group(1))}' if d1 else ''
    if d2 and (not d1 or d2.group(1) != d1.group(1)):
        daten += f' · Aktualisiert am {datum_de(d2.group(1))}'
    initial = ''.join(t[0] for t in name.split()[:2]).upper()
    box = ('<!-- autorenbox:start (automatisch: werkzeuge/layout_anwenden.py) -->\n'
           f'<aside class="autorenbox" aria-label="Über den Autor"><span class="autorenbox__initial" aria-hidden="true">{initial}</span>'
           f'<div><p class="autorenbox__titel">Geschrieben von <a href="/ueber-uns.html#{anker}">{name}</a></p>'
           f'<p class="autorenbox__rolle">Gesellschafter der Gebäudewerke GbR · {rolle}</p>'
           f'<p class="autorenbox__rolle">{quali}</p>'
           f'<p class="autorenbox__daten">{daten}</p></div></aside>\n'
           '<!-- autorenbox:ende -->\n')
    z = re.search(r'\n</div>\n<aside class="datenblatt"', main)
    if z:
        return main[:z.start() + 1] + box + main[z.start() + 1:]
    z = re.search(r'<div class="hinweisbox">', main)
    pos = z.start() if z else len(main)
    return main[:pos] + box + main[pos:]


# ---------------------------------------------------------------- JSON-LD

def rating():
    return {'@type': 'AggregateRating', 'ratingValue': f'{SCHNITT:.1f}', 'bestRating': '5', 'worstRating': '1',
            'ratingCount': str(ANZAHL), 'reviewCount': str(ANZAHL)}


def reviews():
    return [{'@type': 'Review', 'author': {'@type': 'Person', 'name': r['name']}, 'datePublished': r['datum'],
             'reviewBody': r['text'].strip(),
             'reviewRating': {'@type': 'Rating', 'ratingValue': str(r['sterne']), 'bestRating': '5', 'worstRating': '1'}}
            for r in PROFIL['bewertungen'] if r.get('text')]


ORG_VORLAGE = None


def org_vorlage():
    global ORG_VORLAGE
    if ORG_VORLAGE is None:
        s = open(os.path.join(WEB, 'index.html'), encoding='utf-8').read()
        j = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', s, re.S).group(1))
        ORG_VORLAGE = next(o for o in j['@graph'] if o.get('@id') == 'https://gebaeudewerke.de/#organisation')
    o = dict(ORG_VORLAGE)
    o.pop('review', None)
    return o


def jsonld_anwenden(s, seite):
    def ersetzen(m):
        roh = m.group(1)
        j = json.loads(roh)
        graph = j['@graph'] if isinstance(j, dict) and '@graph' in j else None
        if graph is None:
            return m.group(0)
        org = next((o for o in graph if o.get('@id') == 'https://gebaeudewerke.de/#organisation'), None)
        if org is None:
            org = org_vorlage()
            graph.insert(0, org)
        elif 'address' in org and seite != 'index.html':
            # volle Firmen-Entität überall gleich halten (Quelle: index.html)
            i = graph.index(org)
            org = org_vorlage()
            graph[i] = org
        org['aggregateRating'] = rating()
        if seite == 'index.html':
            org['review'] = reviews()
        else:
            org.pop('review', None)
        neu = json.dumps(j, ensure_ascii=False, separators=(',', ':'))
        return '<script type="application/ld+json">' + neu + '</script>'
    return re.sub(r'<script type="application/ld\+json">(.*?)</script>', ersetzen, s, count=1, flags=re.S)


# ---------------------------------------------------------------- Seiten

def seiten():
    liste = sorted(glob.glob(os.path.join(WEB, '*.html'))) + sorted(glob.glob(os.path.join(WEB, 'ratgeber', '*.html')))
    liste.append(os.path.join(WEB, 'ratgeber', 'index.php'))
    return [os.path.relpath(p, WEB).replace(os.sep, '/') for p in liste if not os.path.basename(p).startswith('_')]


def anwenden(seite):
    pfad = os.path.join(WEB, seite)
    alt = open(pfad, encoding='utf-8').read()
    s = alt.replace(ALT_GOOGLE, GOOGLE)
    b = '/' if (seite.startswith('ratgeber/') or seite == '404.html') else ''
    s = kopf_anwenden(s, b)
    s = jsonld_anwenden(s, seite)

    titel = html.unescape(re.search(r'<title>(.*?)</title>', s, re.S).group(1).strip())
    kan = re.search(r'<link rel="canonical" href="([^"]+)"', s)
    url = kan.group(1) if kan else 'https://gebaeudewerke.de/' + seite

    m_body = re.search(r'<body[^>]*>', s)
    m_main = re.search(r'<main id="inhalt">', s)
    m_mainende = s.index('</main>')
    m_bodyende = s.rindex('</body>')
    main = s[m_main.end():m_mainende]
    main = bewertungen_anwenden(main, seite)
    main = teaser_anwenden(main, b)
    main = vertrauen_anwenden(main, seite)
    if seite.startswith('ratgeber/') and seite != 'ratgeber/index.php':
        main = autorenbox_anwenden(s, main)
    s = (s[:m_body.end()] + header(seite, b) + s[m_main.start():m_main.end()] + main + '</main>'
         + footer(seite, b, url, titel) + s[m_bodyende:])
    if s != alt:
        if not PRUEFEN:
            open(pfad, 'w', encoding='utf-8', newline='\n').write(s)
        return True
    return False


def llms():
    p = os.path.join(WEB, 'llms.txt')
    s = open(p, encoding='utf-8').read()
    n = s.replace(ALT_GOOGLE, GOOGLE)
    if n != s and not PRUEFEN:
        open(p, 'w', encoding='utf-8', newline='\n').write(n)
    return n != s


if __name__ == '__main__':
    geaendert = [x for x in seiten() if anwenden(x)]
    if llms():
        geaendert.append('llms.txt')
    print(('Würde ändern' if PRUEFEN else 'Geändert') + f': {len(geaendert)} Dateien')
    for g in geaendert:
        print('  ' + g)
    print(f'CSS inline: {len(CSS)} Zeichen; Bewertungen: {SCHNITT_DE} / {ANZAHL}, Stand {STAND}')
