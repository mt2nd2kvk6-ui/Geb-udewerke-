#!/usr/bin/env python3
"""Baut die drei Design-Richtungen (Startseite bis zum ersten Scroll) als eigenständige HTML-Seiten.
Aufruf: python3 projekt/entwuerfe/richtungen/bauen.py ZIELORDNER
Schriften werden als data-URI eingebettet, Logos als Datei daneben gelegt."""
import base64, os, re, shutil, sys

HIER = os.path.dirname(os.path.abspath(__file__))
BASIS = os.path.dirname(os.path.dirname(os.path.dirname(HIER)))
ZIEL = sys.argv[1]
os.makedirs(ZIEL, exist_ok=True)


def b64(name):
    return base64.b64encode(open(os.path.join(HIER, 'fonts', name), 'rb').read()).decode()


FONTS = (
    '@font-face{font-family:"Archivo";src:url(data:font/woff2;base64,%s) format("woff2");font-weight:400 800;font-stretch:100%% 116%%;font-display:swap}'
    '@font-face{font-family:"Instrument Serif";src:url(data:font/woff2;base64,%s) format("woff2");font-style:italic;font-weight:400;font-display:swap}'
    '@font-face{font-family:"JetBrains Mono";src:url(data:font/woff2;base64,%s) format("woff2");font-weight:500;font-display:swap}'
) % (b64('archivo-var.woff2'), b64('instrument-serif-italic.woff2'), b64('jetbrains-mono-medium.woff2'))

TEL = 'tel:+4917674025524'
NUMMER = '0176 74025524'
WA = 'https://wa.me/491637221790?text=Hallo%20Geb%C3%A4udewerke%2C%20ich%20habe%20eine%20Anfrage%20zu%20einem%20Objekt.'
I_TEL = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" '
         'stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 3.5h3.2l1.6 4.2-2 1.3a11 11 0 0 0 '
         '5.2 5.2l1.3-2 4.2 1.6V17a2 2 0 0 1-2.2 2A15.5 15.5 0 0 1 3 5.7 2 2 0 0 1 5 3.5z"/></svg>')
# WhatsApp-Glyphe: simple-icons (CC0)
I_WA = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>')
I_MENUE = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" '
           'aria-hidden="true" focusable="false"><path d="M4 7h16M4 12h16M4 17h10"/></svg>')
I_ZU = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" '
        'aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6L6 18"/></svg>')
I_PFEIL = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
           'stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6"/></svg>')
STERNE = ('<svg viewBox="0 0 84 14" fill="currentColor" aria-hidden="true" focusable="false">' + ''.join(
    f'<path transform="translate({i * 17.5} 0) scale(.58)" d="M12 1.5l3.1 6.6 7.2.9-5.3 5 1.4 7.1L12 17.6l-6.4 3.5 1.4-7.1-5.3-5 7.2-.9z"/>'
    for i in range(5)) + '</svg>')
GOOGLE = 'https://share.google/v7XolrfYaCO55YrZz'

NAV = [('Leistungen', '#'), ('Preise', '#'), ('Einsatzgebiet', '#'), ('Ratgeber', '#'), ('Über uns', '#'), ('Kontakt', '#')]


def kopf(variante):
    logo = 'logo-quer-weiss.svg' if variante == 'dunkel' else 'logo-quer.svg'
    nav = ''.join(f'<a href="{h}">{t}</a>' for t, h in NAV)
    return f'''<header class="kopf kopf--{variante}"><div class="wrap">
<a class="kopf__logo" href="#"><img src="{logo}" width="1716" height="442" alt="Gebäudewerke Logo, zur Startseite"></a>
<nav class="nav" aria-label="Hauptnavigation">{nav}</nav>
<div class="kopf__aktion">
<a class="btn kopf__tel" href="{TEL}">{I_TEL}<span>Anrufen</span></a>
<a class="btn btn--wa kopf__wa" href="{WA}" rel="noopener" target="_blank">{I_WA}<span>WhatsApp</span></a>
<button class="menue-knopf" type="button" aria-controls="menue" aria-expanded="false" aria-label="Menü öffnen" data-menue-auf>{I_MENUE}</button>
</div></div></header>'''


MENUE = f'''<div class="menue" id="menue" role="dialog" aria-modal="true" aria-label="Menü" hidden>
<div class="menue__kopf"><img src="logo-quer-weiss.svg" width="1716" height="442" alt="Gebäudewerke Logo"><button class="menue__zu" type="button" aria-label="Menü schließen" data-menue-zu>{I_ZU}</button></div>
{''.join(f'<a class="menue__link" href="{h}">{t}</a>' for t, h in NAV)}
<div class="menue__knoepfe"><a class="btn btn--tel" href="{TEL}" style="background:#fff;color:#0D2B4F">{I_TEL}<span>Anrufen: {NUMMER}</span></a><a class="btn btn--wa" href="{WA}" rel="noopener" target="_blank">{I_WA}<span>WhatsApp schreiben</span></a></div>
</div>'''

MOBILLEISTE = f'''<nav class="mobilleiste" aria-label="Schnellkontakt">
<a class="btn btn--tel" href="{TEL}">{I_TEL}<span>Anrufen</span></a>
<a class="btn btn--wa" href="{WA}" rel="noopener" target="_blank">{I_WA}<span>WhatsApp</span></a>
</nav>'''

MENUE_JS = '''<script>(function(){var m=document.getElementById('menue'),a=document.querySelector('[data-menue-auf]'),z=document.querySelector('[data-menue-zu]');
function s(o){if(!m)return;if(o){m.hidden=false;requestAnimationFrame(function(){m.classList.add('offen')});z&&z.focus()}else{m.classList.remove('offen');setTimeout(function(){m.hidden=true},300);a&&a.focus()}a&&a.setAttribute('aria-expanded',o?'true':'false')}
a&&a.addEventListener('click',function(){s(true)});z&&z.addEventListener('click',function(){s(false)});
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&m&&!m.hidden)s(false)});
document.addEventListener('click',function(e){var l=e.target.closest&&e.target.closest('a[href="#"]');if(l)e.preventDefault()});})();</script>'''

ENTWURF = ('<div class="entwurf">Entwurf {N}: Startseite bis zum ersten Scroll. Inhalte mit „Beispiel“ sind Muster aus den Flyern. '
           '<a href="index.html" style="color:inherit">Zur Übersicht</a></div>')

GEMEINSAM = open(os.path.join(HIER, 'gemeinsam.css'), encoding='utf-8').read().replace('{{FONTS}}', FONTS)

for datei in sorted(os.listdir(os.path.join(HIER, 'src'))):
    if not datei.endswith('.html'):
        continue
    s = open(os.path.join(HIER, 'src', datei), encoding='utf-8').read()
    n = datei[0].upper()
    ersetzen = {
        '{{GEMEINSAM}}': '<style>' + GEMEINSAM + '</style>',
        '{{KOPF_HELL}}': kopf('hell'), '{{KOPF_DUNKEL}}': kopf('dunkel'),
        '{{MENUE}}': MENUE, '{{MOBILLEISTE}}': MOBILLEISTE, '{{MENUE_JS}}': MENUE_JS,
        '{{ENTWURF}}': ENTWURF.replace('{N}', n),
        '{{I_TEL}}': I_TEL, '{{I_WA}}': I_WA, '{{I_PFEIL}}': I_PFEIL, '{{STERNE}}': STERNE,
        '{{TEL}}': TEL, '{{NUMMER}}': NUMMER, '{{WA}}': WA, '{{GOOGLE}}': GOOGLE,
    }
    for k, v in ersetzen.items():
        s = s.replace(k, v)
    rest = re.findall(r'\{\{[A-Z_]+\}\}', s)
    if rest:
        sys.exit(f'{datei}: Platzhalter offen: {rest}')
    open(os.path.join(ZIEL, datei), 'w', encoding='utf-8').write(s)
    print(f'{datei}: {len(s) / 1024:.0f} KB')

for logo in ('logo-quer.svg', 'logo-quer-weiss.svg'):
    shutil.copy(os.path.join(BASIS, 'website', 'assets', 'img', logo), os.path.join(ZIEL, logo))
bilder = os.path.join(HIER, 'bilder')
if os.path.isdir(bilder):
    for f in os.listdir(bilder):
        shutil.copy(os.path.join(bilder, f), os.path.join(ZIEL, f))
uebersicht = os.path.join(HIER, 'uebersicht.html')
if os.path.exists(uebersicht):
    shutil.copy(uebersicht, os.path.join(ZIEL, 'index.html'))
