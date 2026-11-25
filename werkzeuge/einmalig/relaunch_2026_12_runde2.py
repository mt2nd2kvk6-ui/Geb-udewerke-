#!/usr/bin/env python3
"""Einmalig Relaunch 12/2026, Runde 2: Entscheidungen des Inhabers vom 25.11.2026.

- Einsatzgebiet: Kraichtal, Weingarten (Baden), Linkenheim-Hochstetten, Eggenstein-Leopoldshafen
  (Orte aus dem Google-Profil) und die Stadt Karlsruhe kommen dazu. Text, Ortslisten, FAQ und FAQPage,
  JSON-LD areaServed, llms.txt und das Kartenschema der Startseite.
- Impressum: Anrufnummer 0176 74025524 (Wunsch Inhaber). Überall sonst nur 0163 7221790.
Mehrfach ausführbar. Reihenfolge: zusammenfuehren → startseite → dieses Skript → layout_anwenden.py.
Aufruf: python3 werkzeuge/einmalig/relaunch_2026_12_runde2.py"""
import glob, math, os, re

BASIS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WEB = os.path.join(BASIS, 'website')
NEU = ['Kraichtal', 'Weingarten (Baden)', 'Linkenheim-Hochstetten', 'Eggenstein-Leopoldshafen']
NEU_TEXT = 'Kraichtal, Weingarten (Baden), Linkenheim-Hochstetten und Eggenstein-Leopoldshafen'
protokoll = []


def ersetzen(name, s, alt, neu, pflicht=True):
    if neu in s:
        return s
    if alt not in s:
        if pflicht:
            raise SystemExit(f'{name}: nicht gefunden: {alt[:90]}')
        return s
    protokoll.append(f'{name}: {s.count(alt)}× {alt[:60]}…')
    return s.replace(alt, neu)


def seiten():
    return sorted(glob.glob(WEB + '/*.html') + glob.glob(WEB + '/ratgeber/*.html') + [WEB + '/ratgeber/index.php'])


# ------------------------------------------------------------------ Texte und Listen
LISTE_ALT = 'Graben-Neudorf, Stutensee und Bretten'
FAQ_ALT = 'Für Objekte in der Stadt Karlsruhe fragen Sie bitte an. Wir prüfen, ob das Objekt in eine bestehende Tour passt. Der Schwerpunkt unserer Arbeit liegt in Bruchsal und den umliegenden Gemeinden.'
FAQ_NEU = ('Ja. Die Stadt Karlsruhe gehört zu unserem Einsatzgebiet, ebenso Linkenheim-Hochstetten und Eggenstein-Leopoldshafen. '
           'Der Schwerpunkt unserer Arbeit liegt in Bruchsal und den umliegenden Gemeinden, Winterdienst übernehmen wir so weit, wie es die Touren zulassen.')
LI_ALT = '<li>Bretten</li></ul>'
LI_NEU = '<li>Bretten</li>' + ''.join(f'<li>{o}</li>' for o in NEU) + '<li>Karlsruhe</li></ul>'
JSON_ALT = '{"@type":"City","name":"Bretten"}'
JSON_NEU = JSON_ALT + ''.join(',{"@type":"City","name":"' + o + '"}' for o in NEU) + \
    ',{"@type":"City","name":"Karlsruhe","sameAs":"https://de.wikipedia.org/wiki/Karlsruhe"}'

for p in seiten():
    name = os.path.relpath(p, WEB)
    s = open(p, encoding='utf-8').read()
    alt = s
    s = ersetzen(name, s, JSON_ALT, JSON_NEU, pflicht=False)
    # Aufzählung in FAQ und Fließtext: „…, Graben-Neudorf, Stutensee und Bretten. Liegt Ihr Objekt …“
    s = ersetzen(name, s, LISTE_ALT + '. Liegt Ihr Objekt',
                 f'Graben-Neudorf, Stutensee, Bretten, {NEU_TEXT}, dazu in der Stadt Karlsruhe. Liegt Ihr Objekt', pflicht=False)
    s = ersetzen(name, s, FAQ_ALT, FAQ_NEU, pflicht=False)
    s = ersetzen(name, s, 'Wir arbeiten in Bruchsal mit allen Stadtteilen und im Landkreis Karlsruhe. Für Objekte in der Stadt Karlsruhe fragen Sie bitte an.',
                 'Wir arbeiten in Bruchsal mit allen Stadtteilen, im Landkreis Karlsruhe und in der Stadt Karlsruhe.', pflicht=False)
    if name in ('index.html', 'einsatzgebiet.html'):
        s = ersetzen(name, s, LI_ALT, LI_NEU)
    if name == 'einsatzgebiet.html':
        s = ersetzen(name, s, LISTE_ALT + '. Für Objekte weiter weg fragen Sie bitte an.',
                     f'Graben-Neudorf, Stutensee, Bretten, {NEU_TEXT}, außerdem die Stadt Karlsruhe. Für Objekte weiter weg fragen Sie bitte an.')
        s = ersetzen(name, s, '<h3>Stutensee und Bretten</h3>\n<p>Auch Objekte in Stutensee und Bretten betreuen wir. Ob ein Objekt in eine bestehende Tour passt, klären wir bei der Anfrage.</p>\n',
                     '<h3>Stutensee und Bretten</h3>\n<p>Auch Objekte in Stutensee und Bretten betreuen wir. Ob ein Objekt in eine bestehende Tour passt, klären wir bei der Anfrage.</p>\n'
                     '<h3>Kraichtal und Weingarten (Baden)</h3>\n<p>In Kraichtal und Weingarten (Baden) übernehmen wir ebenfalls Objekte, mit denselben Leistungen wie in Bruchsal.</p>\n'
                     '<h3>Linkenheim-Hochstetten, Eggenstein-Leopoldshafen und Karlsruhe</h3>\n<p>Auch in Linkenheim-Hochstetten, Eggenstein-Leopoldshafen und in der Stadt Karlsruhe sind wir im Einsatz. '
                     'Für den Winterdienst klären wir beim Ortstermin, ob das Objekt in eine feste Tour passt.</p>\n')
        s = ersetzen(name, s, 'Für Objekte in der Stadt Karlsruhe oder weiter weg prüfen wir', 'Für Objekte weiter weg prüfen wir')
        s = ersetzen(name, s, '12 Gemeinden im Landkreis Karlsruhe', '16 Gemeinden im Landkreis Karlsruhe und die Stadt Karlsruhe')
    if name == 'impressum.html':
        s = ersetzen(name, s, '<p>Telefon: <a href="tel:+491637221790">0163 7221790</a><br>E-Mail:',
                     '<p>Telefon: <a href="tel:+4917674025524">0176 74025524</a><br>Telefon und WhatsApp für Anfragen: <a href="tel:+491637221790">0163 7221790</a><br>E-Mail:')
        s = ersetzen(name, s, 'Kontakt, Telefon 0163 7221790, Gesellschafter', 'Kontakt, Telefon 0176 74025524, Gesellschafter')
    if s != alt:
        open(p, 'w', encoding='utf-8', newline='\n').write(s)

p = os.path.join(WEB, 'llms.txt')
s = open(p, encoding='utf-8').read()
s = ersetzen('llms.txt', s, 'Graben-Neudorf, Stutensee und Bretten. Stadt Karlsruhe auf Anfrage.',
             f'Graben-Neudorf, Stutensee, Bretten, {NEU_TEXT} sowie die Stadt Karlsruhe.')
open(p, 'w', encoding='utf-8', newline='\n').write(s)

# ------------------------------------------------------------------ Kartenschema der Startseite
# Gleiche Projektion wie werkzeuge/einmalig/startseite_2026_11_07.py, Ausschnitt nach Westen und Süden erweitert.
ORTE = [
    ('Bruchsal', 49.1242, 8.5980, 'stadt', (12, 5, 'start')),
    ('Büchenau', 49.1050, 8.5590, 'teil', (-9, -5, 'end')), ('Heidelsheim', 49.0950, 8.6510, 'teil', (9, 12, 'start')),
    ('Helmsheim', 49.1170, 8.6640, 'teil', (9, 15, 'start')), ('Obergrombach', 49.0770, 8.5900, 'teil', (9, 12, 'start')),
    ('Untergrombach', 49.0870, 8.5570, 'teil', (9, 4, 'start')), ('Forst', 49.1530, 8.5800, 'ort', (-9, 4, 'end')),
    ('Karlsdorf-Neuthard', 49.1360, 8.5380, 'ort', (-9, 4, 'end')), ('Ubstadt-Weiher', 49.1660, 8.6300, 'ort', (9, 4, 'start')),
    ('Bad Schönborn', 49.2050, 8.6460, 'ort', (9, 4, 'start')), ('Östringen', 49.2186, 8.7106, 'ort', (-9, -8, 'end')),
    ('Kronau', 49.2236, 8.6311, 'ort', (-9, -6, 'end')), ('Hambrücken', 49.1890, 8.5420, 'sitz', (-12, 4, 'end')),
    ('Waghäusel', 49.2490, 8.5130, 'ort', (9, 4, 'start')), ('Philippsburg', 49.2353, 8.4560, 'ort', (9, 4, 'start')),
    ('Graben-Neudorf', 49.1700, 8.4900, 'ort', (9, 4, 'start')), ('Stutensee', 49.0650, 8.4880, 'ort', (9, -6, 'start')),
    ('Bretten', 49.0364, 8.7061, 'ort', (-9, 4, 'end')),
    ('Kraichtal', 49.1300, 8.7330, 'ort', (6, -10, 'end')), ('Weingarten (Baden)', 49.0517, 8.5300, 'ort', (9, 14, 'start')),
    ('Linkenheim-Hochstetten', 49.1258, 8.4100, 'ort', (9, 10, 'start')), ('Eggenstein-Leopoldshafen', 49.0900, 8.3950, 'ort', (9, 4, 'start')),
    ('Karlsruhe', 49.0094, 8.4037, 'karlsruhe', (9, 5, 'start')),
]
L0, L1, B0, B1, W = 8.36, 8.76, 48.99, 49.265, 460
H = round(W * (B1 - B0) / ((L1 - L0) * math.cos(math.radians(49.13))))
xy = lambda b, l: ((l - L0) / (L1 - L0) * W, (B1 - b) / (B1 - B0) * H)
k = (f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Schematische Karte: Bruchsal mit Stadtteilen, '
     'Gemeinden im Landkreis Karlsruhe und die Stadt Karlsruhe, Sitz in Hambrücken" focusable="false" style="font-family:var(--font)">')
bx, by = xy(49.1242, 8.5980)
k += '<defs><radialGradient id="glut"><stop offset="0" stop-color="#FFD21E" stop-opacity=".35"/><stop offset="1" stop-color="#FFD21E" stop-opacity="0"/></radialGradient></defs>'
k += ''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="rgba(234,240,247,.06)"/>' for x in range(0, W, 46))
k += ''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="rgba(234,240,247,.06)"/>' for y in range(0, H, 46))
k += f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="110" fill="url(#glut)"/>'
hx, hy = xy(49.1890, 8.5420)
k += f'<line x1="{hx:.1f}" y1="{hy:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="#FFD21E" stroke-width="1.4" stroke-dasharray="4 5" opacity=".7"/>'
for n, b, l, art, (dx, dy, anker) in ORTE:
    x, y = xy(b, l)
    r, fill, fs, fw, farbe = {'stadt': (9, '#FFD21E', 19, 800, '#FFFFFF'), 'teil': (5, '#FFD21E', 13, 600, '#EAF0F7'),
                              'ort': (4.5, '#9FB2C8', 13, 500, 'rgba(234,240,247,.8)'), 'sitz': (6, '#FFFFFF', 14, 700, '#FFFFFF'),
                              'karlsruhe': (6, '#9FB2C8', 15, 700, '#EAF0F7')}[art]
    if art == 'sitz':
        k += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11" fill="none" stroke="#FFFFFF" stroke-width="1.5"/>'
    k += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}"/>'
    k += f'<text x="{x + dx:.1f}" y="{y + dy:.1f}" text-anchor="{anker}" font-size="{fs}" font-weight="{fw}" fill="{farbe}">{n}{" (Sitz)" if art == "sitz" else ""}</text>'
KARTE = k + '</svg>'
p = os.path.join(WEB, 'index.html')
s = open(p, encoding='utf-8').read()
neu = re.sub(r'(<figure class="karte-schema">)<svg\b.*?</svg>', lambda m: m.group(1) + KARTE, s, count=1, flags=re.S)
if neu != s:
    protokoll.append('index.html: Kartenschema neu (23 Orte)')
    open(p, 'w', encoding='utf-8', newline='\n').write(neu)
print('\n'.join(protokoll) or 'nichts zu tun')
