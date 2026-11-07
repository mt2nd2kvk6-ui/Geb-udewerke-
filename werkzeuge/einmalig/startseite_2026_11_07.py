#!/usr/bin/env python3
"""Einmalig 07.11.2026: neue Startseite (Mix aus Modell, Aufgabenliste und Karteikarten) nach website/index.html.
Kopfbereich mit Title, Description, Canonical, Geo, Open Graph und JSON-LD bleibt aus dem Bestand erhalten.
FAQ: Fragen, Antworten und Links aus dem Bestand; der sichtbare Preissatz wird an die Preistabelle und das
JSON-LD angeglichen (111/162/238 € netto, Stand Preisseite). Danach: python3 werkzeuge/layout_anwenden.py"""
import html, json, math, os, re, sys

BASIS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WEB = os.path.join(BASIS, 'website')
sys.path.insert(0, os.path.join(BASIS, 'werkzeuge'))
import modell

TEL, NUMMER = 'tel:+4917674025524', '0176 74025524'
WA = ('https://api.whatsapp.com/send?phone=491637221790&text=Hallo%20Geb%C3%A4udewerke%2C%20'
      'ich%20habe%20eine%20Anfrage%20zu%20einem%20Objekt.')
PROFIL = json.load(open(os.path.join(BASIS, 'projekt', 'google-profil.json'), encoding='utf-8'))
GOOGLE = PROFIL['profil_link']


def svg(p, extra=''):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true" focusable="false"{extra}>{p}</svg>')


I_TEL = svg('<path d="M5 3.5h3.2l1.6 4.2-2 1.3a11 11 0 0 0 5.2 5.2l1.3-2 4.2 1.6V17a2 2 0 0 1-2.2 2A15.5 15.5 0 0 1 3 5.7 2 2 0 0 1 5 3.5z"/>')
I_PFEIL = svg('<path d="M5 12h14M13 6l6 6-6 6"/>', ' stroke-width="2"')
sys.argv = [sys.argv[0]]
import layout_anwenden as L   # WhatsApp-Glyphe und Sterne aus dem Layout-Skript
I_WA, STERNE = L.I_WA, L.sterne()

SEITE = {'hausmeister': 'hausmeisterservice.html', 'treppenhaus': 'treppenhausreinigung.html', 'gewerbe': 'gebaeudereinigung.html',
         'buero': 'bueroreinigung.html', 'garten': 'gartenpflege.html', 'winter': 'winterdienst.html', 'keller': 'entruempelung.html',
         'wohnung': 'wohnungsuebergabe.html', 'reparatur': 'kleinreparaturen.html', 'metall': 'metallarbeiten-schloesser.html'}

M = modell.bauen()
MODELL = M['svg'].replace('aria-label="Modell eines Objekts', 'aria-label="Hausmeister und Reinigung in Bruchsal: Modell eines Objekts') + ''.join(
    f'<a class="punkt punkt--{"links" if x > 60 else "rechts"}" href="{SEITE[z]}" data-zone="{z}" style="left:{x}%;top:{y}%" tabindex="-1" aria-label="{t}">'
    f'<span class="punkt__kern" aria-hidden="true"></span><span class="punkt__label"><b>{t}</b><small>{u}</small></span></a>'
    for z, t, u, (x, y) in M['punkte'])

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

LEISTUNGEN_DATEN = [
    ('Im Modell: Eingang und Tonnen', 'Hausmeisterservice für Wohnanlagen und Gewerbe',
     'Kontrollgänge im festen Turnus, Schlüsselverwaltung, Zählerstände und Mängelmeldung. Dazu ein Objektbericht, der in die Verwaltung passt.',
     'hausmeisterservice.html', 'Hausmeisterservice in Bruchsal'),
    ('Im Modell: Treppenhaus', 'Treppenhausreinigung nach festem Plan',
     'Stufen, Podeste, Handläufe und Eingang am gleichen Wochentag. Aushang mit Datum und Kürzel, Mängel melden wir mit Foto.',
     'treppenhausreinigung.html', 'Treppenhausreinigung im Detail'),
    ('Im Modell: Halle', 'Gebäudereinigung für Keller, Tiefgarage und Glas',
     'Gemeinschaftsflächen, Keller, Tiefgarage und Fenster nach festem Reinigungsplan. Dazu Grund-, Bauend- und Leerstandsreinigung.',
     'gebaeudereinigung.html', 'Gebäudereinigung in Bruchsal'),
    ('Im Modell: Erdgeschoss', 'Büro- und Praxisreinigung',
     'Reinigung vor Betriebsbeginn oder nach Feierabend, nach schriftlichem Reinigungsplan. Sie kommen morgens ins saubere Büro.',
     'bueroreinigung.html', 'Büroreinigung in Bruchsal'),
    ('Im Modell: Garten', 'Gartenpflege und Außenanlagen',
     'Rasen, Hecken, Beete und Laub, dazu Wege, Höfe und Parkplätze. Im Jahresvertrag von März bis November oder als Einzeltermin.',
     'gartenpflege.html', 'Gartenpflege in Bruchsal'),
    ('Im Modell: Gehweg', 'Winterdienst mit Einsatzprotokoll',
     'Räumen und Streuen von November bis März. Jeder Einsatz mit Datum, Uhrzeit, Witterung und Streumittel im Protokoll.',
     'winterdienst.html', 'Winterdienst in Bruchsal'),
    ('Im Modell: Keller', 'Entrümpelung und Haushaltsauflösung',
     'Keller, Dachboden, Wohnung oder Gewerbefläche. Festpreis nach Besichtigung, Übergabe besenrein.',
     'entruempelung.html', 'Entrümpelung zum Festpreis'),
    ('Im Modell: Wohnungen', 'Wohnungsübergabe mit Protokoll',
     'Übergaben und Abnahmen mit Fotoprotokoll, Zählerständen und Schlüsselrücknahme. Leerstände kontrollieren wir mit.',
     'wohnungsuebergabe.html', 'Wohnungsübergabe im Detail'),
    ('Im Modell: Fenster mit Licht', 'Kleinreparaturen und Montage',
     'Montage, Silikon, Streichen, Klickvinyl und kleiner Trockenbau. Mehrere Punkte in einem Termin statt fünf Handwerker.',
     'kleinreparaturen.html', 'Kleinreparaturen in Bruchsal'),
    ('Im Modell: Gartentor', 'Metallarbeiten, Tore und Schlösser',
     'Zäune, Tore, Geländer, kleinere Schweißarbeiten, Zylinder und Schließanlagen. Metall machen wir selbst, vom Kellerfenster bis zum Gartentor.',
     'metallarbeiten-schloesser.html', 'Metallarbeiten und Schlösser'),
]
LEISTUNGEN = '\n'.join(
    f'<li class="leistung"><span class="leistung__zone">{z}</span><h3>{h}</h3><p>{t}</p><a href="{l}">{a} {I_PFEIL}</a></li>'
    for z, h, t, l, a in LEISTUNGEN_DATEN) + (
    '\n<li class="leistung leistung--info"><span class="leistung__zone">Wenn es eine Zulassung braucht</span>'
    '<p>Für Elektro, Gas und Trinkwasser holen wir Fachbetriebe dazu, koordinieren den Termin und sind vor Ort dabei. '
    'Alles andere machen wir mit eigenem Personal.</p></li>')

ORTE = [
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
H = round(W * (B1 - B0) / ((L1 - L0) * math.cos(math.radians(49.13))))
xy = lambda b, l: ((l - L0) / (L1 - L0) * W, (B1 - b) / (B1 - B0) * H)
k = (f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Schematische Karte: Bruchsal mit Stadtteilen und Gemeinden im Landkreis Karlsruhe, Sitz in Hambrücken" '
     'focusable="false" style="font-family:var(--font)">')
bx, by = xy(49.1242, 8.5980)
k += '<defs><radialGradient id="glut"><stop offset="0" stop-color="#FFD21E" stop-opacity=".35"/><stop offset="1" stop-color="#FFD21E" stop-opacity="0"/></radialGradient></defs>'
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
KARTE = k + '</svg>'

# ---------- Bestand: Kopf, JSON-LD, FAQ ----------
p = os.path.join(WEB, 'index.html')
alt = open(p, encoding='utf-8').read()
if 'class="hero__raster"' in alt and 'id="modell"' in alt:
    sys.exit('index.html ist schon die neue Startseite, nichts zu tun.')
kopf = alt[:alt.index('<body>')]
faq_alt = re.search(r'<div class="faq">(.*?)</div>\n</div></section>', alt, re.S).group(1)
alt_preis = 'bei 130&nbsp;€ netto für kleine Häuser bis 6 Einheiten, bei 190&nbsp;€ netto für 7 bis 20 Wohneinheiten und bei 280&nbsp;€ netto für größere Anlagen'
neu_preis = 'bei 111&nbsp;€ netto für kleine Häuser bis 6 Einheiten, bei 162&nbsp;€ netto für 7 bis 20 Wohneinheiten und bei 238&nbsp;€ netto für größere Anlagen'
assert alt_preis in faq_alt
FAQ = faq_alt.replace(alt_preis, neu_preis).replace('</details><details>', '</details>\n<details>')
kopf = re.sub(r'"dateModified":"[\d-]+"', '"dateModified":"2026-11-07"', kopf, count=1)
form = re.search(r'<form class="formular" id="anfrage-start".*?</form>', alt, re.S).group(0)
form = form.replace('<p class="pseudo-h3">Kurze Anfrage</p>', '<p class="formular__titel">Oder kurz schreiben</p>').replace('class="btn btn--voll" type="submit"', 'class="btn btn--blau" type="submit"')

MAIN = f'''
<section class="hero" id="start" aria-labelledby="titel">
<div class="wrap hero__raster">
<div class="hero__text">
<p class="live beispiel" id="live-chip">Bruchsal und Landkreis Karlsruhe</p>
<h1 id="titel"><span class="h1-ort">Hausmeister und Reinigung in Bruchsal</span> <span class="h1-claim breit"><span class="zeile">Vom <span class="gelb">Keller</span></span> <span class="zeile">bis zum</span> <span class="zeile"><span class="gelb">Gartentor.</span></span></span></h1>
<p class="intro">Hausmeisterservice, Reinigung, Garten, Winterdienst und Reparaturen für Bruchsal und den Landkreis Karlsruhe. Ein Team, eine Nummer, Festpreis nach dem Ortstermin.</p>
<div class="cta">
<a class="btn btn--weiss btn--gross" href="{TEL}" data-pos="hero">{I_TEL}<span class="btn__zwei"><span class="btn__klein">Anrufen</span><span class="btn__gross">{NUMMER}</span></span></a>
<a class="btn btn--wa btn--gross" href="{WA}" rel="noopener" target="_blank" data-pos="hero">{I_WA}<span class="btn__zwei"><span class="btn__klein">Foto oder Frage</span><span class="btn__gross">WhatsApp</span></span></a>
</div>
<ul class="hero__vertrauen">
<li><a class="google-hinweis" href="{GOOGLE}" rel="noopener" target="_blank">{STERNE}<span>5,0 Sterne auf Google</span></a></li>
<li>Eigenes Personal</li>
<li>Notdienst täglich 17 bis 24 Uhr</li>
</ul>
</div>
<div class="modell" id="modell">
<div class="himmel himmel--schnee" aria-hidden="true"></div>
<div class="himmel himmel--regen" aria-hidden="true"></div>
<div class="himmel himmel--nebel" aria-hidden="true"></div>
{MODELL}
<p class="unterzeile" id="unterzeile" aria-hidden="true"><b>Treppenhausreinigung</b><small>fester Wochentag, Aushang mit Datum</small></p>
</div>
<nav class="liste10" aria-label="Leistungen am Objekt">
<p class="liste10__kopf"><span>Zehn Leistungen, ein Team</span><span>Keine Subunternehmer</span></p>
<ul>
<li><a href="hausmeisterservice.html" data-zone="hausmeister">Hausmeisterservice</a></li>
<li><a href="treppenhausreinigung.html" data-zone="treppenhaus">Treppenhausreinigung</a></li>
<li><a href="gebaeudereinigung.html" data-zone="gewerbe">Gebäudereinigung</a></li>
<li><a href="bueroreinigung.html" data-zone="buero">Büro- und Praxisreinigung</a></li>
<li><a href="gartenpflege.html" data-zone="garten">Gartenpflege</a></li>
<li><a href="winterdienst.html" data-zone="winter">Winterdienst</a></li>
<li><a href="entruempelung.html" data-zone="keller">Entrümpelung</a></li>
<li><a href="wohnungsuebergabe.html" data-zone="wohnung">Wohnungsübergabe</a></li>
<li><a href="kleinreparaturen.html" data-zone="reparatur">Kleinreparaturen</a></li>
<li><a href="metallarbeiten-schloesser.html" data-zone="metall">Metallarbeiten und Schlösser</a></li>
</ul>
</nav>
</div>
</section>

<section class="abschnitt" id="anstehen" aria-labelledby="t-an">
<div class="wrap an-raster">
<div class="an-links">
<p class="auge">Anfrage in 20 Sekunden</p>
<h2 id="t-an">Was steht an?</h2>
<p class="intro">Tippen Sie an, was erledigt werden soll. Ihre Liste landet fertig formuliert in WhatsApp, Sie schicken sie nur noch ab. Wir melden uns am selben oder nächsten Werktag.</p>
<div class="anfrage" id="anfrage">
<div class="anfrage__kopf"><span>Ihre Anfrage</span><span class="zaehler"><b id="zahl">0</b> Aufgaben</span></div>
<ul class="chips" id="chips"></ul>
<a class="btn btn--wa" id="wa-senden" href="{WA}" rel="noopener" target="_blank" data-pos="inhalt">{I_WA}<span>Per WhatsApp senden</span></a>
<a class="anfrage__tel" href="{TEL}" data-pos="inhalt">{I_TEL}<span>Lieber anrufen: <b>{NUMMER}</b></span></a>
</div>
</div>
<div>
<div class="fuer" role="group" aria-label="Sie sind"><span>Sie sind</span>
<button type="button" data-fuer="alles" aria-pressed="true">Alle</button>
<button type="button" data-fuer="hv" aria-pressed="false">Hausverwaltung</button>
<button type="button" data-fuer="privat" aria-pressed="false">Eigentümer</button>
<button type="button" data-fuer="buero" aria-pressed="false">Büro und Praxis</button>
<button type="button" data-fuer="gewerbe" aria-pressed="false">Gewerbe</button>
</div>
<p class="fuer__satz" id="satz">Zehn Leistungen, ein Team, eigenes Personal.</p>
<ul class="aufgaben" id="aufgaben">
{AUFGABEN}
</ul>
</div>
</div>
</section>

<section class="abschnitt abschnitt--kalk" id="bruchsal-heute" aria-labelledby="t-heute">
<div class="wrap">
<div class="kopfteil">
<p class="auge">Karteikarten mit Daten aus Bruchsal</p>
<h2 id="t-heute">Ihr Objekt. <mark>Heute</mark> in Bruchsal.</h2>
<p class="intro">Für jede Art von Objekt eine Karteikarte. Dazu, was heute in Bruchsal gilt: Wetter und amtliche Warnungen vom Deutschen Wetterdienst, die Räumpflicht nach Satzung und die Regeln für den Heckenschnitt.</p>
</div>
<div class="register" role="tablist" aria-label="Karteikarten">
<button type="button" role="tab" class="r-heute" id="r-heute" aria-controls="b-heute" aria-selected="true">Bruchsal heute</button>
<button type="button" role="tab" class="r-hv" id="r-hv" aria-controls="b-hv" aria-selected="false" tabindex="-1">Hausverwaltung</button>
<button type="button" role="tab" class="r-buero" id="r-buero" aria-controls="b-buero" aria-selected="false" tabindex="-1">Büro und Praxis</button>
<button type="button" role="tab" class="r-gewerbe" id="r-gewerbe" aria-controls="b-gewerbe" aria-selected="false" tabindex="-1">Gewerbe</button>
<button type="button" role="tab" class="r-privat" id="r-privat" aria-controls="b-privat" aria-selected="false" tabindex="-1">Eigentümer</button>
<button type="button" role="tab" class="r-winter" id="r-winter" aria-controls="b-winter" aria-selected="false" tabindex="-1">Winterdienst</button>
</div>
<div class="blaetter">
<div class="blatt b-heute aktiv" role="tabpanel" id="b-heute" aria-labelledby="r-heute">
<div class="blatt__kopf"><span data-heute="kopf">Bruchsal · Lage am Objekt</span><span class="punktlive beispiel" data-heute="status">Wetter wird geladen</span></div>
<div>
<p class="heute-gross breit"><span data-heute="datum">Bruchsal</span><span data-heute="zeit"></span></p>
<div class="heute-grad"><b class="breit" data-heute="grad">–</b><span data-heute="wetter">Wetter vom Deutschen Wetterdienst</span></div>
<p class="blatt__text" style="margin-top:14px">Was heute am Objekt gilt, steht daneben. Die Regeln stammen aus der Streupflichtsatzung der Stadt Bruchsal und dem Bundesnaturschutzgesetz.</p>
</div>
<div class="lage">
<div class="lage__kopf"><span>Heute in Bruchsal</span><span class="punktlive beispiel" data-heute="quelle">DWD</span></div>
<dl>
<div><dt>Amtliche Warnung</dt><dd data-heute="warnung">keine Angabe</dd></div>
<div><dt>Räumpflicht</dt><dd data-heute="raeumen">Gehwege geräumt werktags bis 7 Uhr, samstags bis 8 Uhr, sonn- und feiertags bis 9 Uhr, Pflicht endet 20 Uhr</dd></div>
<div><dt>Winterdienst</dt><dd data-heute="saison">Saison vom 1. November bis 31. März</dd></div>
<div><dt>Heckenschnitt</dt><dd data-heute="hecke">Vom 1. März bis 30. September nur schonender Form- und Pflegeschnitt, starker Rückschnitt von Oktober bis Ende Februar</dd></div>
<div><dt>Laub</dt><dd data-heute="laub">In Bruchsal müssen Anlieger das Laub vom Gehweg entfernen</dd></div>
<div><dt>Licht</dt><dd data-heute="sonne">Sonnenaufgang und Sonnenuntergang für Bruchsal</dd></div>
<div><dt>Erreichbar</dt><dd data-heute="erreichbar">Büro Mo bis Fr 7 bis 17 Uhr, Notdienst täglich 17 bis 24 Uhr</dd></div>
</dl>
</div>
<p class="quelle">Quellen: Deutscher Wetterdienst (Beobachtung und Warnungen für die Stadt Bruchsal), Streupflichtsatzung der Stadt Bruchsal, § 39 Bundesnaturschutzgesetz. Mehr im <a href="/ratgeber/raeum-und-streupflicht-bruchsal.html">Ratgeber zur Räum- und Streupflicht</a> und zum <a href="/ratgeber/hecke-schneiden-erlaubt.html">Heckenschnitt</a>.</p>
</div>
<div class="blatt b-hv" role="tabpanel" id="b-hv" aria-labelledby="r-hv">
<div class="blatt__kopf"><span>Objektprotokoll · Wohnanlage</span><span>Beispiel</span></div>
<div>
<p class="blatt__titel breit">Fünf Gewerke. <em>Ein Betreuer.</em></p>
<p class="blatt__text">Hausmeister, Reinigung, Garten, Winterdienst und Übergaben über einen Vertrag. Jeder Einsatz steht im Protokoll, umlagefähige Positionen sind auf der Rechnung getrennt.</p>
<a class="blatt__mehr" href="hausmeisterservice.html">Hausmeisterservice für Verwaltungen {I_PFEIL}</a>
</div>
<div class="lage">
<ul class="protokoll">
<li><time>Mo 07:10</time><span>Kontrollgang innen und außen, ohne Befund</span><span class="ok">erledigt</span></li>
<li><time>Mi 06:15</time><span>Gehweg geräumt, Splitt gestreut</span><span class="ok">erledigt</span></li>
<li><time>Fr 08:05</time><span>Treppenhaus gereinigt, Aushang abgezeichnet</span><span class="ok">erledigt</span></li>
<li><time>Fr 08:30</time><span>Handlauf 1. OG lose, Foto an Verwaltung</span><span class="gemeldet">gemeldet</span></li>
</ul>
<p class="lage__kopf"><span data-heute="jahreswechsel">Zählerstände zum Jahreswechsel rechtzeitig planen</span><a href="/ratgeber/zaehlerstaende-ablesen-jahreswechsel.html">Ratgeber Zählerstände</a></p>
</div>
</div>
<div class="blatt b-buero" role="tabpanel" id="b-buero" aria-labelledby="r-buero">
<div class="blatt__kopf"><span>Reinigungsplan · Büro und Praxis</span><span>Beispiel</span></div>
<div>
<p class="blatt__titel breit">Sauber, <em>bevor</em> der Tag beginnt.</p>
<p class="blatt__text">Wir reinigen vor Arbeitsbeginn oder nach Feierabend, nach schriftlichem Reinigungsplan und mit festem Team. In Praxen außerhalb der Sprechzeiten.</p>
<a class="blatt__mehr" href="bueroreinigung.html">Büro- und Praxisreinigung {I_PFEIL}</a>
</div>
<div class="lage"><ul class="haken"><li>Arbeitsplätze und Böden</li><li>Sanitärräume und Küche</li><li>Besprechungsräume</li><li>Empfang und Wartebereich</li><li>Behandlungsräume nach Absprache</li><li>Fenster und Glas</li></ul></div>
</div>
<div class="blatt b-gewerbe" role="tabpanel" id="b-gewerbe" aria-labelledby="r-gewerbe">
<div class="blatt__kopf"><span>Hallen · Werkstätten · Gewerbe</span><span>Ein Meldeweg</span></div>
<div>
<p class="blatt__titel breit">Läuft. <em>Auch wenn Sie nicht hinsehen.</em></p>
<p class="blatt__text">Kontrollgänge, Reinigung, Außenanlagen, Winterdienst und Mülltonnen. Ein Vertrag, ein Ansprechpartner und ein fester Meldeweg für Störungen.</p>
<a class="blatt__mehr" href="gebaeudereinigung.html">Gebäudereinigung für Gewerbe {I_PFEIL}</a>
</div>
<div class="lage">
<dl class="drei"><div><dt>Kontrolle</dt><dd>nach Bedarf bis täglich</dd></div><div><dt>Störung</dt><dd>Ihre Mieter melden direkt an uns</dd></div><div><dt>Notdienst</dt><dd>täglich 17 bis 24 Uhr</dd></div></dl>
<p class="lage__kopf"><span class="punktlive" data-heute="notdienst">Notdienst täglich 17 bis 24 Uhr</span></p>
</div>
</div>
<div class="blatt b-privat" role="tabpanel" id="b-privat" aria-labelledby="r-privat">
<div class="blatt__kopf"><span>Für Eigentümer und Vermieter</span><span>Festpreis nach Besichtigung</span></div>
<div>
<p class="blatt__titel breit">Ihre Liste. <em>Ein Termin.</em></p>
<p class="blatt__text">Garten, Entrümpelung, Reparaturen und Hausbetreuung. Schicken Sie ein Foto per WhatsApp, wir melden uns am selben oder nächsten Werktag.</p>
<a class="blatt__mehr" href="kleinreparaturen.html">Kleinreparaturen und Montage {I_PFEIL}</a>
</div>
<div class="lage">
<div class="zettel"><p>Noch zu erledigen</p><ul><li>Hecke schneiden</li><li>Keller ausräumen</li><li>Mülltonnen rausstellen</li><li>Lampe montieren</li><li>Silikonfuge erneuern</li></ul></div>
<p class="lage__kopf"><span data-heute="hecke-kurz">Heckenschnitt: Regeln nach Jahreszeit</span></p>
</div>
</div>
<div class="blatt b-winter" role="tabpanel" id="b-winter" aria-labelledby="r-winter">
<div class="blatt__kopf"><span>Winterdienst · 1. November bis 31. März</span><span data-heute="saison-kurz">Saison</span></div>
<div>
<p class="blatt__titel breit">Wir räumen. <em>Sie haben den Beleg.</em></p>
<p class="blatt__text">Gehwege, Eingänge, Zufahrten und Parkplätze. Jeder Einsatz wird mit Datum, Uhrzeit, Witterung und Streumittel protokolliert, zum Saisonende gibt es den Bericht.</p>
<dl class="einsatz"><div><dt>Beginn</dt><dd>05:40</dd></div><div><dt>Witterung</dt><dd>Neuschnee, −3 °C</dd></div><div><dt>Streumittel</dt><dd>Splitt</dd></div><div><dt>Status</dt><dd>erledigt</dd></div></dl>
<p class="quelle" style="margin-top:8px">Einsatzprotokoll als Beispiel</p>
<a class="blatt__mehr" href="winterdienst.html">Winterdienst mit Protokoll {I_PFEIL}</a>
</div>
<div class="lage">
<div class="lage__kopf"><span>Lage jetzt in Bruchsal</span><span class="punktlive beispiel" data-heute="quelle2">DWD</span></div>
<dl>
<div><dt>Temperatur</dt><dd data-heute="grad2">–</dd></div>
<div><dt>Witterung</dt><dd data-heute="wetter2">Wetter vom Deutschen Wetterdienst</dd></div>
<div><dt>Warnung</dt><dd data-heute="warnung2">keine Angabe</dd></div>
<div><dt>Heute geräumt</dt><dd data-heute="raeumen2">werktags bis 7 Uhr, samstags bis 8 Uhr, sonn- und feiertags bis 9 Uhr</dd></div>
</dl>
</div>
</div>
</div>
</div>
</section>

<section class="abschnitt" id="leistungen" aria-labelledby="t-leistungen">
<div class="wrap">
<div class="kopfteil">
<p class="auge">Alles am Objekt</p>
<h2 id="t-leistungen">Zehn Leistungen. <mark>Ein</mark> Vertrag.</h2>
<p class="intro">Gebäudewerke übernimmt in Bruchsal und im Landkreis Karlsruhe, was an einem Wohn- oder Gewerbeobjekt anfällt. Statt fünf Firmen für fünf Gewerke haben Sie einen Ansprechpartner. Was Ihr Objekt nicht braucht, buchen Sie nicht dazu.</p>
</div>
<ul class="leistungen">
{LEISTUNGEN}
</ul>
</div>
</section>

<!-- bewertungen:start --><!-- bewertungen:ende -->

<section class="abschnitt abschnitt--kalk" id="ablauf" aria-labelledby="t-ablauf">
<div class="wrap">
<div class="kopfteil">
<p class="auge">Vom Anruf zum Start</p>
<h2 id="t-ablauf">Vier Schritte. <mark>Ein</mark> Festpreis.</h2>
<p class="intro">Vor dem Ortstermin entsteht keine Bindung und keine Rechnung. Sie wissen vorher, was es kostet.</p>
</div>
<ol class="ablauf">
<li><div class="ablauf__nr" aria-hidden="true">1</div><h3>Anfrage</h3><p>Sie schildern kurz Objekt, Flächen und Umfang. Per Telefon, WhatsApp oder Formular.</p></li>
<li><div class="ablauf__nr" aria-hidden="true">2</div><h3>Rückruf</h3><p>Wir melden uns am selben oder nächsten Werktag und klären, was für Ihr Objekt sinnvoll ist und was nicht.</p></li>
<li><div class="ablauf__nr" aria-hidden="true">3</div><h3>Ortstermin</h3><p>Wir sehen uns die Liegenschaft an, messen auf und klären Zugänge und Zeitfenster. Der Termin kostet nichts.</p></li>
<li><div class="ablauf__nr" aria-hidden="true">4</div><h3>Festpreis und Start</h3><p>Zwei bis drei Werktage später haben Sie das schriftliche Angebot. Nach Ihrer Freigabe starten wir zum vereinbarten Termin.</p></li>
</ol>
<ul class="zusagen">
<li><h3>Termine halten</h3><p>Ist eine Verschiebung unvermeidbar, sagen wir früh Bescheid und schlagen direkt einen neuen Termin vor.</p></li>
<li><h3>Alles aufschreiben</h3><p>Jeder Einsatz mit Datum, Uhrzeit und Fotos. Beim Winterdienst kann genau das im Streitfall entscheiden.</p></li>
<li><h3>Eigenes Personal</h3><p>Kein wechselndes Subunternehmen im Haus. Jedes Objekt hat einen festen Betreuer, der es kennt.</p></li>
<li><h3>Preise, die gelten</h3><p>Nach dem Ortstermin bekommen Sie einen schriftlichen Festpreis. Richtpreise je Leistung stehen auf der <a href="preise.html">Preisseite</a>.</p></li>
</ul>
</div>
</section>

<section class="abschnitt" id="team" aria-labelledby="t-team">
<div class="wrap">
<div class="kopfteil">
<p class="auge">Das Team</p>
<h2 id="t-team">Vier Mann. <mark>Eigenes</mark> Personal.</h2>
<p class="intro">Wir sind vier Mann zwischen 30 und 40 und machen die Arbeit selbst, ohne Subunternehmer. Für jeden Bereich ist einer von uns zuständig, und jedes Objekt hat einen festen Verantwortlichen.</p>
</div>
<ul class="team">
<li class="person"><span class="monogramm" aria-hidden="true">FA</span><b>Fatih Altun</b><span>Metallarbeiten, Schlösser und Reparaturen</span></li>
<li class="person"><span class="monogramm" aria-hidden="true">EY</span><b>Enes Yesildag</b><span>Vertrieb, Hausverwaltung und Wohnungsübergaben</span></li>
<li class="person"><span class="monogramm" aria-hidden="true">BK</span><b>Burak Kartal</b><span>Qualität, Reinigung und Gartenpflege</span></li>
<li class="person"><span class="monogramm" aria-hidden="true">JB</span><b>Julian Bender</b><span>Hausmeisterservice und Winterdienst</span></li>
</ul>
<a class="mehr-link" href="ueber-uns.html">Mehr über Gebäudewerke {I_PFEIL}</a>
</div>
</section>

<section class="abschnitt abschnitt--kalk" id="einsatzgebiet" aria-labelledby="t-gebiet">
<div class="wrap gebiet">
<div>
<p class="auge">Einsatzgebiet</p>
<h2 id="t-gebiet">Bruchsal und der <mark>Landkreis</mark> Karlsruhe.</h2>
<p class="intro">Wir betreuen Objekte in der Bruchsaler Kernstadt und in allen Stadtteilen: Büchenau, Heidelsheim, Helmsheim, Obergrombach und Untergrombach. Dazu kommen die Gemeinden rund um Bruchsal. Unser Betrieb liegt in Hambrücken, wenige Kilometer nordwestlich der Kernstadt.</p>
<ul class="orte" aria-label="Orte im Einsatzgebiet">
<li class="haupt">Bruchsal Kernstadt</li><li>Büchenau</li><li>Heidelsheim</li><li>Helmsheim</li><li>Obergrombach</li><li>Untergrombach</li><li>Forst</li><li>Karlsdorf-Neuthard</li><li>Ubstadt-Weiher</li><li>Bad Schönborn</li><li>Östringen</li><li>Kronau</li><li>Hambrücken</li><li>Waghäusel</li><li>Philippsburg</li><li>Graben-Neudorf</li><li>Stutensee</li><li>Bretten</li>
</ul>
<p>Beim Winterdienst entscheiden kurze Wege. Deshalb bündeln wir Objekte zu festen Touren und nehmen nur an, was sich darin sinnvoll unterbringen lässt. Ihr Ort fehlt? Fragen Sie an, wir sagen kurzfristig, was möglich ist.</p>
<a class="mehr-link" href="einsatzgebiet.html">Alle Orte im Einsatzgebiet rund um Bruchsal {I_PFEIL}</a>
</div>
<div>
<figure class="karte-schema">{KARTE}<figcaption><span>Schematische Lage der Orte</span><span>Sitz: Hambrücken</span></figcaption></figure>
<div class="karte" data-karte="https://www.google.com/maps?q=Allmend+2,+76707+Hambr%C3%BCcken&amp;hl=de&amp;z=16&amp;output=embed">
<address>Gebäudewerke GbR, Allmend 2, 76707 Hambrücken</address>
<div class="btn-reihe"><button class="btn btn--blau" type="button" data-karte-laden>Karte anzeigen</button><a class="btn btn--rand" href="{GOOGLE}" rel="noopener" target="_blank">In Google Maps öffnen</a></div>
<p style="margin:0">Mit „Karte anzeigen“ wird Google Maps geladen. Dabei werden Daten an Google übertragen, siehe <a href="datenschutz.html">Hinweise zum Datenschutz</a>.</p>
</div>
</div>
</div>
</section>

<section class="abschnitt" id="fakten" aria-labelledby="t-fakten">
<div class="wrap fakten">
<div>
<p class="auge">Kurz und zitierfähig</p>
<h2 id="t-fakten">Gebäudewerke auf einen Blick.</h2>
<p class="zitierfaehig">Gebäudewerke ist ein Objekt- und Gebäudeservice aus Hambrücken für Bruchsal und den Landkreis Karlsruhe. Vier Mann mit eigenem Personal betreuen Wohnanlagen, Eigentümergemeinschaften und Gewerbe: Hausmeisterservice, Reinigung, Garten, Winterdienst, Übergaben, Entrümpelung und Reparaturen. Jeder Einsatz wird protokolliert, der Preis steht nach dem kostenlosen Ortstermin schriftlich fest.</p>
<div class="btn-reihe"><a class="btn btn--rand" href="preise.html">Richtpreise ansehen</a></div>
</div>
<aside class="datenblatt" aria-labelledby="fakten-titel"><p class="datenblatt__titel" id="fakten-titel">Fakten</p><dl>
<div><dt>Firma</dt><dd>Gebäudewerke GbR</dd></div>
<div><dt>Sitz</dt><dd>Allmend 2, 76707 Hambrücken, bei Bruchsal</dd></div>
<div><dt>Einsatzgebiet</dt><dd>Bruchsal mit allen Stadtteilen und Landkreis Karlsruhe</dd></div>
<div><dt>Kunden</dt><dd>Hausverwaltungen, Eigentümergemeinschaften, private Vermieter, Gewerbe</dd></div>
<div><dt>Arbeitsweise</dt><dd>eigenes Personal, fester Betreuer, Protokoll zu jedem Einsatz</dd></div>
<div><dt>Hausmeisterservice</dt><dd>Richtpreise ab 111 € netto im Monat (bis 6 Einheiten, zwei Termine pro Woche)</dd></div>
<div><dt>Winterdienst</dt><dd>Saisonpauschale bis 120 m² Räumfläche 1.220 € netto</dd></div>
<div><dt>Erreichbarkeit</dt><dd>Mo bis Fr 7 bis 17 Uhr, Notdienst täglich 17 bis 24 Uhr</dd></div>
<div><dt>Betriebshaftpflicht</dt><dd>Deckungssumme bis 5 Mio. Euro</dd></div>
<div><dt>Google</dt><dd>7 Bewertungen, Durchschnitt 5,0 (Stand 31.10.2026)</dd></div>
</dl></aside>
</div>
</section>

<section class="abschnitt abschnitt--kalk" id="ratgeber" aria-labelledby="t-ratgeber">
<div class="wrap">
<div class="kopfteil">
<p class="auge">Ratgeber</p>
<h2 id="t-ratgeber">Pflichten, Fristen, Kosten.</h2>
<p class="intro">Was rund ums Objekt gilt, erklärt von unserem Team. Kurz, mit Quellen und ohne Fachchinesisch.</p>
</div>
<ul class="start-ratgeber">
<li><a href="/ratgeber/raeum-und-streupflicht-bruchsal.html"><span class="thema">Winterdienst</span><b>Räum- und Streupflicht in Bruchsal</b><span>Weiterlesen {I_PFEIL}</span></a></li>
<li><a href="/ratgeber/hausmeisterkosten-umlagefaehig.html"><span class="thema">Betriebskosten</span><b>Welche Hausmeisterkosten umlagefähig sind</b><span>Weiterlesen {I_PFEIL}</span></a></li>
<li><a href="/ratgeber/wohnungsuebergabe-protokoll-bruchsal.html"><span class="thema">Wohnungsübergabe</span><b>Übergabeprotokoll beim Mieterwechsel</b><span>Weiterlesen {I_PFEIL}</span></a></li>
</ul>
<a class="mehr-link" href="ratgeber/">Alle Ratgeberbeiträge {I_PFEIL}</a>
</div>
</section>

<section class="abschnitt" id="fragen" aria-labelledby="t-fragen">
<div class="wrap faq-raster">
<div class="kopfteil">
<p class="auge">Häufige Fragen</p>
<h2 id="t-fragen">Kurz gefragt. <mark>Klar</mark> beantwortet.</h2>
<p class="intro">Die Punkte, die im ersten Gespräch fast immer kommen.</p>
</div>
<div class="faq">
{FAQ}
</div>
</div>
</section>

<section class="kontakt" id="kontakt" aria-labelledby="t-kontakt">
<div class="wrap">
<p class="auge">Kontakt</p>
<h2 id="t-kontakt">Rufen Sie an.</h2>
<a class="riesennummer" href="{TEL}" data-pos="kontaktblock">{NUMMER}</a>
<div class="kontakt__raster">
<div>
<div class="cta"><a class="btn btn--wa btn--gross" href="{WA}" rel="noopener" target="_blank" data-pos="kontaktblock">{I_WA}<span class="btn__zwei"><span class="btn__klein">Auch mit Foto</span><span class="btn__gross">WhatsApp schreiben</span></span></a></div>
<dl>
<div><dt>Büro</dt><dd>Montag bis Freitag, 7 bis 17 Uhr</dd></div>
<div><dt>Notdienst</dt><dd>täglich, 17 bis 24 Uhr</dd></div>
<div><dt>Anschrift</dt><dd>Gebäudewerke GbR<br>Allmend 2, 76707 Hambrücken</dd></div>
<div><dt>E-Mail</dt><dd><a href="mailto:info@gebaeudewerke.de" data-pos="kontaktblock">info@gebaeudewerke.de</a></dd></div>
</dl>
</div>
{form}
</div>
</div>
</section>
'''
neu = kopf + '<body>\n<main id="inhalt">\n' + MAIN + '</main>\n</body>\n</html>\n'
open(p, 'w', encoding='utf-8', newline='\n').write(neu)
print('index.html neu geschrieben:', len(neu) // 1024, 'KB (vor Layout)')
