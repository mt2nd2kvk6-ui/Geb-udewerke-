#!/usr/bin/env python3
"""Baut den Startseiten-Entwurf (Mix aus Modell, Aufgabenliste und Karteikarten).
Aufruf: python3 projekt/entwuerfe/startseite/bauen.py AUSGABEORDNER
Ergebnis: AUSGABEORDNER/startseite.html (vollständige Seite) und artifact-startseite.html (ohne Dokumentrahmen),
dazu eine Kopie der vollständigen Seite in projekt/entwuerfe/startseite/ansehen/."""
import base64, html, json, math, os, re, sys

HIER = os.path.dirname(os.path.abspath(__file__))
BASIS = os.path.dirname(os.path.dirname(os.path.dirname(HIER)))
WEB = os.path.join(BASIS, 'website')
ZIEL = sys.argv[1]
os.makedirs(ZIEL, exist_ok=True)
sys.path.insert(0, HIER)
import modell

lesen = lambda p: open(p, encoding='utf-8').read()
b64 = lambda p: base64.b64encode(open(p, 'rb').read()).decode()

TEL, NUMMER = 'tel:+4917674025524', '0176 74025524'
WA = 'https://wa.me/491637221790?text=Hallo%20Geb%C3%A4udewerke%2C%20ich%20habe%20eine%20Anfrage%20zu%20einem%20Objekt.'
PROFIL = json.load(open(os.path.join(BASIS, 'projekt', 'google-profil.json'), encoding='utf-8'))
GOOGLE, SCHREIBEN = PROFIL['profil_link'], PROFIL['bewertung_schreiben']


def svg(p, extra=''):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true" focusable="false"{extra}>{p}</svg>')


I_TEL = svg('<path d="M5 3.5h3.2l1.6 4.2-2 1.3a11 11 0 0 0 5.2 5.2l1.3-2 4.2 1.6V17a2 2 0 0 1-2.2 2A15.5 15.5 0 0 1 3 5.7 2 2 0 0 1 5 3.5z"/>')
I_WA = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>')
I_MENUE = svg('<path d="M4 7h16M4 12h16M4 17h10"/>')
I_ZU = svg('<path d="M6 6l12 12M18 6L6 18"/>')
I_PFEIL = svg('<path d="M5 12h14M13 6l6 6-6 6"/>', ' stroke-width="2"')
I_PAUSE = svg('<path d="M9 5v14M15 5v14"/>')
STERN = 'M12 1.5l3.1 6.6 7.2.9-5.3 5 1.4 7.1L12 17.6l-6.4 3.5 1.4-7.1-5.3-5 7.2-.9z'


def sterne(rolle=False, anzahl=5):
    p = ''.join(f'<path transform="translate({i * 17.5} 0) scale(.58)" d="{STERN}"/>' for i in range(anzahl))
    a = f' role="img" aria-label="{anzahl} von 5 Sternen"' if rolle else ' aria-hidden="true"'
    return f'<svg viewBox="0 0 84 14" fill="currentColor"{a} focusable="false">{p}</svg>'


# ---------- Modell mit Hotspots (im Entwurf springen sie zu den Leistungen) ----------
ANKER = {'hausmeister': 'l-hausmeister', 'treppenhaus': 'l-treppenhaus', 'gewerbe': 'l-gebaeude', 'buero': 'l-buero',
         'garten': 'l-garten', 'winter': 'l-winter', 'keller': 'l-entruempelung', 'wohnung': 'l-uebergabe',
         'reparatur': 'l-reparatur', 'metall': 'l-metall'}
M = modell.bauen()
svg_m = M['svg'].replace('aria-label="Modell eines Objekts', 'aria-label="Hausmeister und Reinigung in Bruchsal: Modell eines Objekts')
MODELL = svg_m + ''.join(
    f'<a class="punkt punkt--{"links" if x > 60 else "rechts"}" href="#{ANKER[z]}" data-zone="{z}" style="left:{x}%;top:{y}%">'
    f'<span class="punkt__kern" aria-hidden="true"></span><span class="punkt__label"><b>{t}</b><small>{u}</small></span></a>'
    for z, t, u, (x, y) in M['punkte'])

# ---------- Aufgaben (Was steht an?) ----------
AUFGABEN_DATEN = [
    ('alles hv', 'Treppenhaus reinigen', 'fester Wochentag, Aushang mit Datum'),
    ('alles hv', 'Hausmeister für alles', 'Kontrollgang, Zähler, Schlüssel'),
    ('alles buero', 'Büro reinigen', 'vor Arbeitsbeginn oder nach Feierabend'),
    ('alles privat', 'Hecke schneiden', 'einmalig oder im Jahresvertrag'),
    ('alles hv privat buero gewerbe', 'Schnee räumen', 'Saisonpauschale, Protokoll je Einsatz'),
    ('alles privat', 'Keller entrümpeln', 'Festpreis nach Besichtigung'),
    ('alles hv privat', 'Wohnung übergeben', 'Fotoprotokoll und Zählerstände'),
    ('alles privat', 'Lampe montieren', 'mehrere Punkte in einem Termin'),
    ('alles hv privat', 'Schloss tauschen', 'Zylinder und Schließanlagen'),
    ('hv gewerbe', 'Außenanlagen pflegen', 'Rasen, Hecken, Wege, Höfe'),
    ('hv', 'Mülltonnen rausstellen', 'Rhythmus frei wählbar'),
    ('hv buero gewerbe', 'Handwerker koordinieren', 'wir begleiten den Termin'),
    ('privat', 'Silikonfuge erneuern', 'auch Streichen und Klickvinyl'),
    ('privat', 'Haus kontrollieren', 'wenn Sie nicht vor Ort sind'),
    ('buero', 'Praxis reinigen', 'außerhalb der Sprechzeiten'),
    ('buero hv', 'Fenster und Glas', 'in derselben Tour'),
    ('buero', 'Sanitär und Küche', 'nach Reinigungsplan'),
    ('buero gewerbe', 'Schlüssel und Zugang', 'Übergabe schriftlich'),
    ('gewerbe', 'Kontrollgänge', 'nach Bedarf bis täglich'),
    ('gewerbe', 'Halle grundreinigen', 'Festpreis nach Ortstermin'),
    ('gewerbe', 'Störungen annehmen', 'Notdienst täglich 17 bis 24 Uhr'),
    ('gewerbe', 'Tor und Zaun reparieren', 'Metall machen wir selbst'),
]
AUFGABEN = '\n'.join(
    f'<li data-fuer="{f}"{"" if "alles" in f.split() else " hidden"}><button type="button" class="aufgabe" aria-pressed="false">'
    f'<span class="kreis" aria-hidden="true"></span><span class="aufgabe__text">{t}</span><span class="aufgabe__info">{i}</span></button></li>'
    for f, t, i in AUFGABEN_DATEN)

# ---------- Leistungen ----------
LEISTUNGEN_DATEN = [
    ('l-hausmeister', 'Im Modell: Eingang und Tonnen', 'Hausmeisterservice für Wohnanlagen und Gewerbe',
     'Kontrollgänge im festen Turnus, Schlüsselverwaltung, Zählerstände und Mängelmeldung. Dazu ein Objektbericht, der in die Verwaltung passt.',
     'hausmeisterservice.html', 'Hausmeisterservice in Bruchsal'),
    ('l-treppenhaus', 'Im Modell: Treppenhaus', 'Treppenhausreinigung nach festem Plan',
     'Stufen, Podeste, Handläufe und Eingang am gleichen Wochentag. Aushang mit Datum und Kürzel, Mängel melden wir mit Foto.',
     'treppenhausreinigung.html', 'Treppenhausreinigung im Detail'),
    ('l-gebaeude', 'Im Modell: Halle', 'Gebäudereinigung für Keller, Tiefgarage und Glas',
     'Gemeinschaftsflächen, Keller, Tiefgarage und Fenster nach festem Reinigungsplan. Dazu Grund-, Bauend- und Leerstandsreinigung.',
     'gebaeudereinigung.html', 'Gebäudereinigung in Bruchsal'),
    ('l-buero', 'Im Modell: Erdgeschoss', 'Büro- und Praxisreinigung',
     'Reinigung vor Betriebsbeginn oder nach Feierabend, nach schriftlichem Reinigungsplan. Sie kommen morgens ins saubere Büro.',
     'bueroreinigung.html', 'Büroreinigung in Bruchsal'),
    ('l-garten', 'Im Modell: Garten', 'Gartenpflege und Außenanlagen',
     'Rasen, Hecken, Beete und Laub, dazu Wege, Höfe und Parkplätze. Im Jahresvertrag von März bis November oder als Einzeltermin.',
     'gartenpflege.html', 'Gartenpflege in Bruchsal'),
    ('l-winter', 'Im Modell: Gehweg', 'Winterdienst mit Einsatzprotokoll',
     'Räumen und Streuen von November bis März. Jeder Einsatz mit Datum, Uhrzeit, Witterung und Streumittel im Protokoll.',
     'winterdienst.html', 'Winterdienst in Bruchsal'),
    ('l-entruempelung', 'Im Modell: Keller', 'Entrümpelung und Haushaltsauflösung',
     'Keller, Dachboden, Wohnung oder Gewerbefläche. Festpreis nach Besichtigung, Übergabe besenrein.',
     'entruempelung.html', 'Entrümpelung zum Festpreis'),
    ('l-uebergabe', 'Im Modell: Wohnungen', 'Wohnungsübergabe mit Protokoll',
     'Übergaben und Abnahmen mit Fotoprotokoll, Zählerständen und Schlüsselrücknahme. Leerstände kontrollieren wir mit.',
     'wohnungsuebergabe.html', 'Wohnungsübergabe im Detail'),
    ('l-reparatur', 'Im Modell: Fenster mit Licht', 'Kleinreparaturen und Montage',
     'Montage, Silikon, Streichen, Klickvinyl und kleiner Trockenbau. Mehrere Punkte in einem Termin statt fünf Handwerker.',
     'kleinreparaturen.html', 'Kleinreparaturen in Bruchsal'),
    ('l-metall', 'Im Modell: Gartentor', 'Metallarbeiten, Tore und Schlösser',
     'Zäune, Tore, Geländer, kleinere Schweißarbeiten, Zylinder und Schließanlagen. Metall machen wir selbst, vom Kellerfenster bis zum Gartentor.',
     'metallarbeiten-schloesser.html', 'Metallarbeiten und Schlösser'),
]
LEISTUNGEN_INFO = ('<li class="leistung leistung--info"><span class="leistung__zone">Wenn es eine Zulassung braucht</span>'
                   '<p>Für Elektro, Gas und Trinkwasser holen wir Fachbetriebe dazu, koordinieren den Termin und sind vor Ort dabei. '
                   'Alles andere machen wir mit eigenem Personal.</p></li>')
LEISTUNGEN = '\n'.join(
    f'<li class="leistung" id="{i}"><span class="leistung__zone">{z}</span><h3>{h}</h3><p>{t}</p><a href="{l}">{a} {I_PFEIL}</a></li>'
    for i, z, h, t, l, a in LEISTUNGEN_DATEN) + '\n' + LEISTUNGEN_INFO

# ---------- Bewertungen aus dem Google-Profil (Texte unverändert) ----------
MONATE = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember']
bew = sorted([r for r in PROFIL['bewertungen'] if r.get('text')], key=lambda r: r['datum'], reverse=True)
BEWERTUNGEN = ''.join(
    f'<li class="bewertung"><figure>{sterne(True, int(r["sterne"]))}<blockquote><p>{html.escape(r["text"].strip())}</p></blockquote>'
    f'<figcaption><span class="initial" aria-hidden="true">{html.escape(r["name"][:1].upper())}</span><span><b>{html.escape(r["name"])}</b>'
    f'{MONATE[int(r["datum"][5:7]) - 1]} {r["datum"][:4]} · Google</span></figcaption></figure></li>' for r in bew)
STERNE_GROSS = sterne().replace('viewBox="0 0 84 14"', 'viewBox="0 0 84 14" width="120" height="20"')

# ---------- FAQ: Fragen, Antworten und Links aus der heutigen Startseite ----------
idx = lesen(os.path.join(WEB, 'index.html'))
faq = re.search(r'<div class="faq">(.*?)</div>\n</div></section>', idx, re.S).group(1)
alt_preis = 'bei 130&nbsp;€ netto für kleine Häuser bis 6 Einheiten, bei 190&nbsp;€ netto für 7 bis 20 Wohneinheiten und bei 280&nbsp;€ netto für größere Anlagen'
neu_preis = 'bei 111&nbsp;€ netto für kleine Häuser bis 6 Einheiten, bei 162&nbsp;€ netto für 7 bis 20 Wohneinheiten und bei 238&nbsp;€ netto für größere Anlagen'
assert alt_preis in faq, 'Preissatz in der FAQ nicht gefunden'
FAQ = faq.replace(alt_preis, neu_preis).replace('</details><details>', '</details>\n<details>')
assert FAQ.count('<details>') == 11

# ---------- Schematische Karte des Einsatzgebiets ----------
ORTE = [  # Name, Breite, Länge, Art, Beschriftung (dx, dy, Ausrichtung)
    ('Bruchsal', 49.1242, 8.5980, 'stadt', (12, 5, 'start')),
    ('Büchenau', 49.1050, 8.5590, 'teil', (-9, 4, 'end')), ('Heidelsheim', 49.0950, 8.6510, 'teil', (9, 12, 'start')),
    ('Helmsheim', 49.1170, 8.6640, 'teil', (9, 4, 'start')), ('Obergrombach', 49.0770, 8.5900, 'teil', (9, 12, 'start')),
    ('Untergrombach', 49.0870, 8.5570, 'teil', (-9, 4, 'end')), ('Forst', 49.1530, 8.5800, 'ort', (-9, 4, 'end')),
    ('Karlsdorf-Neuthard', 49.1360, 8.5380, 'ort', (-9, 4, 'end')), ('Ubstadt-Weiher', 49.1660, 8.6300, 'ort', (9, 4, 'start')),
    ('Bad Schönborn', 49.2050, 8.6460, 'ort', (9, 4, 'start')), ('Östringen', 49.2186, 8.7106, 'ort', (-9, -8, 'end')),
    ('Kronau', 49.2236, 8.6311, 'ort', (-9, -6, 'end')), ('Hambrücken', 49.1890, 8.5420, 'sitz', (-12, 4, 'end')),
    ('Waghäusel', 49.2490, 8.5130, 'ort', (9, 4, 'start')), ('Philippsburg', 49.2353, 8.4560, 'ort', (9, 4, 'start')),
    ('Graben-Neudorf', 49.1700, 8.4900, 'ort', (9, 4, 'start')), ('Stutensee', 49.0650, 8.4880, 'ort', (9, 4, 'start')),
    ('Bretten', 49.0364, 8.7061, 'ort', (-9, 4, 'end')),
]
L0, L1, B0, B1, W = 8.43, 8.74, 49.02, 49.265, 460
kx = math.cos(math.radians(49.13))
H = round(W * (B1 - B0) / ((L1 - L0) * kx))
xy = lambda b, l: ((l - L0) / (L1 - L0) * W, (B1 - b) / (B1 - B0) * H)
k = f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Schematische Karte: Bruchsal mit Stadtteilen und Gemeinden im Landkreis Karlsruhe, Sitz in Hambrücken" focusable="false" style="font-family:var(--font)">'
bx, by = xy(49.1242, 8.5980)
k += f'<defs><radialGradient id="glut"><stop offset="0" stop-color="#FFD21E" stop-opacity=".35"/><stop offset="1" stop-color="#FFD21E" stop-opacity="0"/></radialGradient></defs>'
k += ''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="rgba(234,240,247,.06)"/>' for x in range(0, W, 46))
k += ''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="rgba(234,240,247,.06)"/>' for y in range(0, H, 46))
k += f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="120" fill="url(#glut)"/>'
hx, hy = xy(49.1890, 8.5420)
k += f'<line x1="{hx:.1f}" y1="{hy:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="#FFD21E" stroke-width="1.4" stroke-dasharray="4 5" opacity=".7"/>'
for n, b, l, art, (dx, dy, anker) in ORTE:
    x, y = xy(b, l)
    r, fill, fs, fw, farbe = {'stadt': (9, '#FFD21E', 19, 800, '#FFFFFF'), 'teil': (5, '#FFD21E', 13, 600, '#EAF0F7'),
                              'ort': (4.5, '#9FB2C8', 13, 500, 'rgba(234,240,247,.8)'), 'sitz': (6, '#FFFFFF', 14, 700, '#FFFFFF')}[art]
    if art == 'sitz':
        k += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11" fill="none" stroke="#FFFFFF" stroke-width="1.5"/>'
    k += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}"/>'
    k += f'<text x="{x + dx:.1f}" y="{y + dy:.1f}" text-anchor="{anker}" font-size="{fs}" font-weight="{fw}" fill="{farbe}">{n}{" (Sitz)" if art == "sitz" else ""}</text>'
k += '</svg>'
KARTE = k

# ---------- Zusammensetzen ----------
FONTS = (f'@font-face{{font-family:"Mona Sans";src:url(data:font/woff2;base64,{b64(os.path.join(HIER, "fonts", "mona-sans-var.woff2"))}) format("woff2");font-weight:400 900;font-stretch:100% 125%;font-display:swap}}'
         f'@font-face{{font-family:"JetBrains Mono";src:url(data:font/woff2;base64,{b64(os.path.join(HIER, "fonts", "jetbrains-mono-medium.woff2"))}) format("woff2");font-weight:500;font-display:swap}}')
LOGO_WEISS = 'data:image/svg+xml;base64,' + b64(os.path.join(WEB, 'assets', 'img', 'logo-quer-weiss.svg'))
ENTWURF = '<div class="entwurf">Entwurf Startseite: Mix aus Modell, Aufgabenliste und Karteikarten. Unterseiten, Formular und Karte funktionieren erst auf gebaeudewerke.de.</div>'

css = lesen(os.path.join(HIER, 'src', 'startseite.css')).replace('{{FONTS}}', FONTS)
js = lesen(os.path.join(HIER, 'src', 'startseite.js'))
s = lesen(os.path.join(HIER, 'src', 'startseite.html'))
for a, b in {'{{CSS}}': css, '{{JS}}': js, '{{ENTWURF}}': ENTWURF, '{{MODELL}}': MODELL, '{{AUFGABEN}}': AUFGABEN,
             '{{LEISTUNGEN}}': LEISTUNGEN, '{{BEWERTUNGEN}}': BEWERTUNGEN, '{{FAQ}}': FAQ, '{{KARTE}}': KARTE,
             '{{LOGO_WEISS}}': LOGO_WEISS, '{{STERNE_GROSS}}': STERNE_GROSS, '{{STERNE}}': sterne(),
             '{{I_TEL}}': I_TEL, '{{I_WA}}': I_WA, '{{I_MENUE}}': I_MENUE, '{{I_ZU}}': I_ZU, '{{I_PFEIL}}': I_PFEIL, '{{I_PAUSE}}': I_PAUSE,
             '{{TEL}}': TEL, '{{NUMMER}}': NUMMER, '{{WA}}': WA, '{{GOOGLE}}': GOOGLE, '{{SCHREIBEN}}': SCHREIBEN}.items():
    s = s.replace(a, b)
offen = re.findall(r'\{\{[A-Z_]+\}\}', s)
if offen:
    sys.exit('Platzhalter offen: ' + ', '.join(sorted(set(offen))))
open(os.path.join(ZIEL, 'startseite.html'), 'w', encoding='utf-8').write(s)
os.makedirs(os.path.join(HIER, 'ansehen'), exist_ok=True)
open(os.path.join(HIER, 'ansehen', 'startseite.html'), 'w', encoding='utf-8').write(s)

# Artifact-Fassung: Dokumentrahmen weg, Titel und Seitenrand-Hinweis vorn
a = re.sub(r'^\s*<!doctype html>\s*<html[^>]*>\s*<head>\s*<meta charset="utf-8">\s*<meta name="viewport"[^>]*>\s*', '', s, flags=re.I)
a = a.replace('<title>', '<meta name="claude:viewport-fit-sides" content="cover">\n<title>', 1)
a = re.sub(r'</head>\s*<body[^>]*>', '', a, count=1)
a = re.sub(r'</body>\s*</html>\s*$', '', a)
open(os.path.join(ZIEL, 'artifact-startseite.html'), 'w', encoding='utf-8').write(a)
print(f'startseite.html {len(s) // 1024} KB, artifact-startseite.html {len(a) // 1024} KB')
