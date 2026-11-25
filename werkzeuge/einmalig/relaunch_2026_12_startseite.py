#!/usr/bin/env python3
"""Einmalig Relaunch 12/2026, Schritt 2: Startseite zusammenführen.

Aufbau, Gestaltung und Interaktion vom 07.11. (G = f38d527): Gebäudemodell, „Was steht an?“,
Karteikarten mit „Heute in Bruchsal“, Kartenschema. Texte vom 16.11. (V = 0638e7d): überall dort, wo
derselbe Abschnitt in beiden Ständen vorkommt, gilt der Text vom 16.11. (Konfliktliste in
projekt/relaunch-2026-12/konflikte.md, Nummern K1 bis K16 stehen unten als Kommentar).

Änderungen gegenüber dem 07.11. für Barrierefreiheit und „ohne JavaScript lesbar“:
- Modell-Punkte sind Buttons mit sichtbarer Beschriftung (vorher Links mit tabindex="-1").
  Die gewählte Zone steht in der Infozeile unter dem Modell, dort mit Link auf die Leistungsseite
  (Hausmeister: Ankertext „Hausmeisterservice Bruchsal“).
- Alle Aufgaben stehen ohne hidden im HTML, die Filterung übernimmt main.js.
- Karteikarten stehen ohne JavaScript untereinander, die Reiter blendet erst main.js ein.
Aufruf: python3 werkzeuge/einmalig/relaunch_2026_12_startseite.py"""
import html, os, re, subprocess

BASIS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WEB = os.path.join(BASIS, 'website')
G, V = 'f38d527', '0638e7d'


def git(rev, pfad):
    return subprocess.run(['git', 'show', f'{rev}:{pfad}'], cwd=BASIS, capture_output=True).stdout.decode('utf-8')


g = git(G, 'website/index.html')
v = git(V, 'website/index.html')
gm = re.search(r'<main id="inhalt">.*?</main>', g, re.S).group(0)
vm = re.search(r'<main id="inhalt">.*?</main>', v, re.S).group(0)


def such(muster, text, gruppe=0):
    m = re.search(muster, text, re.S)
    if not m:
        raise SystemExit('nicht gefunden: ' + muster[:80])
    return m.group(gruppe)


def ohne_tags(t):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', t))).strip()


def preise(t):
    """Werte aus der Preistabelle (preise.html, Senkung um 15 % vom 02.11.2026)."""
    for alt, neu in (('130&nbsp;€', '111&nbsp;€'), ('190&nbsp;€', '162&nbsp;€'), ('280&nbsp;€', '238&nbsp;€'),
                     ('449&nbsp;€', '382&nbsp;€'), ('1.435&nbsp;€', '1.220&nbsp;€')):
        t = t.replace(alt, neu)
    return t


TEL, TEL_TEXT = 'tel:+491637221790', '0163 7221790'
WA = 'https://api.whatsapp.com/send?phone=491637221790&amp;text=Hallo%20Geb%C3%A4udewerke%2C%20ich%20habe%20eine%20Anfrage%20zu%20einem%20Objekt.'
I = {n: such(r'(<svg\b[^>]*>(?:(?!</svg>).)*' + re.escape(p) + r'.*?</svg>)', gm, 1) for n, p in (
    ('tel', 'M5 3.5h3.2'), ('wa', 'M17.472 14.382'), ('pfeil', 'M5 12h14M13 6l6 6-6 6'))}

# ------------------------------------------------------------------ Texte vom 16.11.
v_h1 = ohne_tags(such(r'<h1[^>]*>(.*?)</h1>', vm, 1))
v_lead = such(r'<p class="hero__lead">(.*?)</p>', vm, 1)
v_fakten = re.findall(r'<li><svg\b.*?</svg><span>(.*?)</span></li>', such(r'<ul class="hero__fakten">.*?</ul>', vm))
v_band = re.findall(r'<li><svg\b.*?</svg><div><strong>(.*?)</strong><span>(.*?)</span></div></li>', such(r'<div class="fakten-band">.*?</ul>', vm))
v_protokoll = such(r'<tbody>(.*?)</tbody>', such(r'<figure class="protokoll".*?</figure>', vm), 1)
v_protokoll_fuss = such(r'<figcaption class="protokoll__fuss">(.*?)</figcaption>', vm, 1)
v_verzeichnisse = such(r'<section class="abschnitt vertrauen".*?</section>', vm)
v_zusagen = such(r'<section class="abschnitt" aria-labelledby="zusagen-titel">.*?</section>', vm)
v_leistungen = such(r'<section class="abschnitt abschnitt--kalk" id="leistungen".*?</section>', vm)
v_zielgruppen = such(r'<section class="abschnitt" aria-labelledby="zielgruppen-titel">.*?</section>', vm)
v_blick = such(r'<section class="abschnitt abschnitt--kalk" id="auf-einen-blick".*?</section>', vm)
v_ablauf = such(r'<section class="abschnitt abschnitt--blau" aria-labelledby="ablauf-titel">.*?</section>', vm)
v_team = such(r'<section class="abschnitt" aria-labelledby="team-titel">.*?</section>', vm)
v_gebiet = such(r'<section class="abschnitt abschnitt--kalk" aria-labelledby="gebiet-titel">.*?</section>', vm)
v_ratgeber = such(r'<section class="abschnitt abschnitt--kalk" aria-labelledby="ratgeber-titel">.*?</section>', vm)
v_fragen = such(r'<section class="abschnitt" id="fragen".*?</section>', vm)
v_kontakt = such(r'<section class="abschnitt abschnitt--blau" id="kontakt".*?</section>', vm)


def kopf_text(abschnitt):
    h2 = such(r'<h2[^>]*>(.*?)</h2>', abschnitt, 1)
    p = re.search(r'</h2>\s*<p>(.*?)</p>', abschnitt, re.S)
    return h2, (p.group(1) if p else '')


# ------------------------------------------------------------------ 1. Hero mit Modell (07.11.)
modell_g = such(r'<div class="modell" id="modell">.*?</nav>', gm)
svg_modell = such(r'<svg class="modell__svg".*?</svg>', modell_g)
punkte = re.findall(r'<a class="punkt (punkt--(?:links|rechts))" href="([^"]+)" data-zone="([^"]+)" style="([^"]+)" tabindex="-1" aria-label="[^"]*">'
                    r'<span class="punkt__kern" aria-hidden="true"></span><span class="punkt__label"><b>(.*?)</b><small>(.*?)</small></span></a>', modell_g)
assert len(punkte) == 10, len(punkte)
# Ankertexte der Infozeile: Hauptkeyword der Leistungsseite (projekt/seo/keyword-map.md)
ANKER = {
    'hausmeisterservice.html': 'Hausmeisterservice Bruchsal', 'treppenhausreinigung.html': 'Treppenhausreinigung Bruchsal',
    'gebaeudereinigung.html': 'Gebäudereinigung Bruchsal', 'bueroreinigung.html': 'Büroreinigung Bruchsal',
    'gartenpflege.html': 'Gartenpflege Bruchsal', 'winterdienst.html': 'Winterdienst Bruchsal',
    'entruempelung.html': 'Entrümpelung Bruchsal', 'wohnungsuebergabe.html': 'Wohnungsübergabe Bruchsal',
    'kleinreparaturen.html': 'Kleinreparaturen Bruchsal', 'metallarbeiten-schloesser.html': 'Metallarbeiten Bruchsal',
}
knoepfe = ''.join(
    f'<button class="punkt {seite}" type="button" data-zone="{zone}" data-ziel="{href}" data-anker="{ANKER[href]}" style="{stil}" aria-pressed="false" aria-controls="unterzeile">'
    f'<span class="punkt__kern" aria-hidden="true"></span><span class="punkt__label"><b>{name}</b><small>{klein}</small></span></button>'
    for seite, href, zone, stil, name, klein in punkte)
start = next(p for p in punkte if p[2] == 'hausmeister')
liste10 = such(r'<nav class="liste10".*?</nav>', modell_g)
himmel = ''.join(re.findall(r'<div class="himmel himmel--\w+" aria-hidden="true"></div>\n', modell_g))

hero_vertrauen = (f'<li>{such(r"<li><a class=\"google-hinweis\".*?</a></li>", gm)[4:-5]}</li>'
                  + ''.join(f'<li>{x}</li>' for x in v_fakten))

hero = f'''<section class="hero" id="start" aria-labelledby="titel">
<div class="wrap hero__raster">
<div class="hero__text">
<p class="live beispiel" id="live-chip">Bruchsal und Landkreis Karlsruhe</p>
<h1 id="titel" class="h1-ort">{html.escape(v_h1, quote=False)}</h1>
<p class="h1-claim breit"><span class="zeile">Vom <span class="gelb">Keller</span></span> <span class="zeile">bis zum</span> <span class="zeile"><span class="gelb">Gartentor.</span></span></p>
<p class="intro">Hausmeisterservice, Reinigung, Garten, Winterdienst und Reparaturen für Bruchsal und den Landkreis Karlsruhe. Ein Team, eine Nummer, Festpreis nach dem Ortstermin.</p>
<div class="cta">
<a class="btn btn--weiss btn--gross" href="{TEL}" data-pos="hero">{I['tel']}<span class="btn__zwei"><span class="btn__klein">Anrufen</span><span class="btn__gross">{TEL_TEXT}</span></span></a>
<a class="btn btn--wa btn--gross" href="{WA}" rel="noopener" target="_blank" data-pos="hero">{I['wa']}<span class="btn__zwei"><span class="btn__klein">Foto oder Frage</span><span class="btn__gross">WhatsApp</span></span></a>
</div>
<ul class="hero__vertrauen">
{hero_vertrauen}
</ul>
</div>
<div class="modell" id="modell">
<div class="modell__flaeche">
{himmel}{svg_modell}{knoepfe}
<button class="modell__pause" type="button" aria-pressed="false" hidden>Rundgang anhalten</button>
</div>
<p class="unterzeile" id="unterzeile"><span class="unterzeile__text"><b>{start[4]}</b><small>{start[5]}</small></span><a href="{start[1]}">{ANKER[start[1]]} {I['pfeil']}</a></p>
</div>
{liste10}
</div>
</section>
<!-- K1 H1 vom 16.11., Claim vom 07.11. als Gestaltungszeile. K2 Einstieg max. 25 Wörter, Text vom 16.11. steht unten bei den Leistungen. -->
<div class="vertrauen vertrauen--start"><div class="wrap"><ul class="vertrauen__liste">
''' + ''.join(f'<li><span><strong>{a}</strong><span>{b}</span></span></li>' for a, b in v_band) + '''
</ul></div></div>'''

# ------------------------------------------------------------------ 2. Was steht an? (07.11.)
anstehen = such(r'<section class="abschnitt" id="anstehen".*?</section>', gm)
anstehen = anstehen.replace('tel:+4917674025524', TEL).replace('0176 74025524', TEL_TEXT)
anstehen = re.sub(r'(<li data-fuer="[^"]*") hidden>', r'\1>', anstehen)   # ohne JavaScript alle Aufgaben sichtbar

# ------------------------------------------------------------------ 3. Karteikarten (07.11.)
heute = such(r'<section class="abschnitt abschnitt--kalk" id="bruchsal-heute".*?</section>', gm)
# K3 Protokoll der Hausverwaltungs-Karte: sechs Einträge und Bildunterschrift vom 16.11. statt vier
zeilen = re.findall(r'<tr><td>(.*?)</td><td>(.*?)</td><td><span class="protokoll__(ok|offen)">(?:<svg\b.*?</svg>)?(.*?)</span></td></tr>', v_protokoll, re.S)
protokoll = ''.join(f'<li><time>{z}</time><span>{t}</span><span class="{"ok" if k == "ok" else "gemeldet"}">{s}</span></li>' for z, t, k, s in zeilen)
heute = heute.replace('<div class="blatt__kopf"><span>Objektprotokoll · Wohnanlage</span><span>Beispiel</span></div>',
                      '<div class="blatt__kopf"><span>Objektprotokoll · ' + such(r'<p class="protokoll__objekt">(.*?)</p>', vm, 1) + '</span><span>Beispiel</span></div>')
heute = re.sub(r'<ul class="protokoll">.*?</ul>', f'<ul class="protokoll">{protokoll}</ul>\n<p class="lage__fuss">{v_protokoll_fuss}</p>', heute, flags=re.S)
# Ohne wetter.php und ohne JavaScript: feste Texte statt „wird geladen“
heute = heute.replace('<span class="punktlive beispiel" data-heute="status">Wetter wird geladen</span>',
                      '<span class="punktlive beispiel" data-heute="status">Wetter vom DWD</span>')
heute = heute.replace('<span data-heute="wetter">Wetter vom Deutschen Wetterdienst</span>',
                      '<span data-heute="wetter">Aktuelle Werte und Warnungen veröffentlicht der Deutsche Wetterdienst auf dwd.de</span>')
heute = heute.replace('<dd data-heute="warnung">keine Angabe</dd>', '<dd data-heute="warnung">Amtliche Warnungen für Bruchsal auf dwd.de</dd>')
heute = heute.replace('<dd data-heute="warnung2">keine Angabe</dd>', '<dd data-heute="warnung2">Amtliche Warnungen für Bruchsal auf dwd.de</dd>')
heute = heute.replace('<dd data-heute="wetter2">Wetter vom Deutschen Wetterdienst</dd>', '<dd data-heute="wetter2">Aktuelle Werte auf dwd.de</dd>')
# Räumzeiten und Laubpflicht wie auf der Website (Ratgeber vom 16.10. und 31.10.), Entscheidung Inhaber 25.11.2026
heute = heute.replace('Streupflichtsatzung der Stadt Bruchsal, § 39 Bundesnaturschutzgesetz.',
                      'Streupflichtsatzung der Stadt Bruchsal, § 39 Abs. 5 Nr. 2 Bundesnaturschutzgesetz.')
heute = heute.replace('<p class="quelle" style="margin-top:8px">Einsatzprotokoll als Beispiel</p>',
                      '<p class="quelle quelle--abstand">Einsatzprotokoll als Beispiel</p>')
heute = heute.replace(' style="margin-top:14px"', '')
# Reiter-Rollen setzt main.js (ohne JavaScript stehen die Karten untereinander)
heute = heute.replace('<div class="register" role="tablist" aria-label="Karteikarten">', '<div class="register" aria-label="Karteikarten">')
heute = re.sub(r'<button type="button" role="tab" (class="r-\w+" id="r-\w+" aria-controls="b-\w+") aria-selected="(?:true|false)"(?: tabindex="-1")?>', r'<button type="button" \1>', heute)
heute = re.sub(r'(<div class="blatt b-\w+(?: aktiv)?") role="tabpanel" id="(b-\w+)" aria-labelledby="r-\w+">', r'\1 id="\2">', heute)
assert 'role="tab' not in heute
assert '[PRÜFEN' not in heute and 'Wetter wird geladen' not in heute

# ------------------------------------------------------------------ 4. Leistungen: Aufbau 07.11., Texte 16.11. (K4)
lh2, lp = kopf_text(v_leistungen)
v_karten = {m[0]: (m[1], m[2]) for m in re.findall(r'<a class="lv__link" href="([^"]+)">\s*<h3 class="lv__name">(.*?)</h3>.*?<p class="lv__text">(.*?)</p>', v_leistungen, re.S)}
g_karten = re.findall(r'<li class="leistung"><span class="leistung__zone">(.*?)</span><h3>.*?</h3><p>.*?</p><a href="([^"]+)">(.*?) <svg', gm)
karten = ''.join(f'<li class="leistung"><span class="leistung__zone">{zone}</span><h3>{v_karten[href][0]}</h3><p>{preise(v_karten[href][1])}</p>'
                 f'<a href="{href}">{anker} {I["pfeil"]}</a></li>\n' for zone, href, anker in g_karten)
info = such(r'<li class="leistung leistung--info">.*?</li>', gm)
leistungen = f'''<section class="abschnitt" id="leistungen" aria-labelledby="t-leistungen" data-abschnitt="leistungen">
<div class="wrap">
<div class="kopfteil">
<p class="auge">Alles am Objekt</p>
<h2 id="t-leistungen">{lh2}</h2>
<p class="kurzantwort">{v_lead}</p>
<p class="intro">{lp}</p>
</div>
<ul class="leistungen">
{karten}{info}
</ul>
</div>
</section>'''

# ------------------------------------------------------------------ 5. Zielgruppen (nur 16.11.)
zg = v_zielgruppen.replace('<section class="abschnitt" aria-labelledby="zielgruppen-titel"><div class="wrap">',
                           '<section class="abschnitt abschnitt--kalk" aria-labelledby="zielgruppen-titel"><div class="wrap">')
zg = zg.replace('<div class="abschnitt__kopf"><h2', '<div class="kopfteil"><p class="auge">Für wen wir arbeiten</p><h2')
zg = zg.replace('<p class="pseudo-h3">', '<h3>').replace('</p><p>Ein Ansprechpartner', '</h3><p>Ein Ansprechpartner')
zg = re.sub(r'<h3>([^<]*)</p>', r'<h3>\1</h3>', zg)

# ------------------------------------------------------------------ 6. Bewertungen (automatisch) und Verzeichnisse (16.11.)
bewertungen = such(r'<!-- bewertungen:start.*?<!-- bewertungen:ende -->', gm)
verz = v_verzeichnisse.replace('<section class="abschnitt vertrauen"', '<section class="abschnitt verzeichnisse"')
for a, b in (('vertrauen__kopf', 'verzeichnisse__kopf'), ('vertrauen__raster', 'verzeichnisse__raster'),
             ('vertrauen__presse', 'verzeichnisse__presse'), ('vertrauen-titel', 'verzeichnisse-titel')):
    verz = verz.replace(a, b)

# ------------------------------------------------------------------ 7. Zusagen und Ablauf: Aufbau 07.11., Texte 16.11. (K5, K6)
zh2, zp = kopf_text(v_zusagen)
zusagen_li = ''.join(f'<li><h3>{a}</h3><p>{b}</p></li>' for a, b in
                     re.findall(r'<div class="zusage"><p class="pseudo-h3">(.*?)</p><p>(.*?)</p></div>', v_zusagen, re.S))
ah2, ap = kopf_text(v_ablauf)
sterne = such(r'<p class="cta-sterne">.*?</p>', v_ablauf)
schritte = ''.join(f'<li><div class="ablauf__nr" aria-hidden="true">{n}</div><h3>{a}</h3><p>{b}</p></li>' for n, a, b in
                   re.findall(r'<li><div class="ablauf__nr" aria-hidden="true">(\d)</div><p class="pseudo-h3">(.*?)</p><p>(.*?)</p></li>', v_ablauf, re.S))
ablauf = f'''<section class="abschnitt" id="zusagen" aria-labelledby="zusagen-titel">
<div class="wrap">
<div class="kopfteil">
<p class="auge">Woran Sie uns messen</p>
<h2 id="zusagen-titel">{zh2}</h2>
<p class="intro">{zp}</p>
</div>
<ul class="zusagen zusagen--oben">{zusagen_li}</ul>
</div>
</section>

<section class="abschnitt abschnitt--kalk" id="ablauf" aria-labelledby="t-ablauf" data-abschnitt="ablauf">
<div class="wrap">
<div class="kopfteil">
<p class="auge">Vom Anruf zum Start</p>
<h2 id="t-ablauf">{ah2}</h2>
<p class="intro">{ap}</p>
{sterne}
</div>
<ol class="ablauf">{schritte}</ol>
</div>
</section>'''

# ------------------------------------------------------------------ 8. Team: Aufbau 07.11., Texte 16.11. (K7)
th2, tp = kopf_text(v_team)
team = f'''<section class="abschnitt" id="team" aria-labelledby="t-team">
<div class="wrap">
<div class="kopfteil">
<p class="auge">Vier Mann, eigenes Personal</p>
<h2 id="t-team">{th2}</h2>
<p class="intro">{tp}</p>
</div>
{such(r'<ul class="team">.*?</ul>', gm)}
<a class="mehr-link" href="ueber-uns.html">Mehr über uns {I['pfeil']}</a>
</div>
</section>'''

# ------------------------------------------------------------------ 9. Einsatzgebiet: Aufbau 07.11., Texte 16.11. (K8)
gh2 = such(r'<h2[^>]*>(.*?)</h2>', v_gebiet, 1)
g_text = such(r'</h2>(.*?)<p><a href="einsatzgebiet.html">', v_gebiet, 1)
g_text = g_text.replace('<ul class="orte">', '<ul class="orte" aria-label="Orte im Einsatzgebiet">').replace('<li>Bruchsal Kernstadt</li>', '<li class="haupt">Bruchsal Kernstadt</li>')
karte = such(r'<div class="karte" data-karte=.*?</p>\n</div>', such(r'<section class="abschnitt abschnitt--kalk" id="einsatzgebiet".*?</section>', gm))
karte = karte.replace('<p style="margin:0">', '<p class="karte__hinweis">')
gebiet = f'''<section class="abschnitt abschnitt--kalk" id="einsatzgebiet" aria-labelledby="t-gebiet">
<div class="wrap gebiet">
<div>
<p class="auge">Einsatzgebiet</p>
<h2 id="t-gebiet">{gh2}</h2>
{g_text.strip()}
<a class="mehr-link" href="einsatzgebiet.html">Alle Orte im Einsatzgebiet rund um Bruchsal {I['pfeil']}</a>
</div>
<div>
{such(r'<figure class="karte-schema">.*?</figure>', gm)}
{karte}
</div>
</div>
</section>'''

# ------------------------------------------------------------------ 10. Auf einen Blick: Aufbau 07.11., Texte 16.11. (K9)
bh2 = such(r'<h2[^>]*>(.*?)</h2>', v_blick, 1)
b_text = such(r'</h2>\s*(.*?)\s*</div>\s*<aside', v_blick, 1)
b_text = preise(b_text.replace('<p class="kurzantwort">', '<p class="zitierfaehig">'))
b_aside = preise(such(r'<aside class="datenblatt datenblatt--statisch".*?</aside>', v_blick)).replace(' datenblatt--statisch', '')
blick = f'''<section class="abschnitt" id="fakten" aria-labelledby="blick-titel-start">
<div class="wrap fakten">
<div>
<p class="auge">Kurz und zitierfähig</p>
<h2 id="blick-titel-start">{bh2}</h2>
{b_text}
</div>
{b_aside}
</div>
</section>'''

# ------------------------------------------------------------------ 11. Ratgeber: Aufbau 07.11., Texte 16.11. (K10)
rh2 = such(r'<p class="pseudo-h2" id="ratgeber-titel">(.*?)</p>', v_ratgeber, 1)
rp = such(r'<p class="pseudo-h2" id="ratgeber-titel">.*?</p><p>(.*?)</p>', v_ratgeber, 1)
ratgeber = f'''<section class="abschnitt abschnitt--kalk" id="ratgeber" aria-labelledby="t-ratgeber">
<div class="wrap">
<div class="kopfteil">
<p class="auge">Ratgeber</p>
<h2 id="t-ratgeber">{rh2}</h2>
<p class="intro">{rp}</p>
</div>
{such(r'<ul class="start-ratgeber">.*?</ul>', gm)}
<a class="mehr-link" href="ratgeber/">Alle Ratgeberbeiträge {I['pfeil']}</a>
</div>
</section>'''

# ------------------------------------------------------------------ 12. Fragen: Aufbau 07.11., Texte 16.11. (K11)
fh2, fp = kopf_text(v_fragen)
faq = preise(such(r'<div class="faq">.*?</details></div>', v_fragen))
fragen = f'''<section class="abschnitt" id="fragen" aria-labelledby="t-fragen">
<div class="wrap faq-raster">
<div class="kopfteil">
<p class="auge">Kurz gefragt, klar beantwortet</p>
<h2 id="t-fragen">{fh2}</h2>
<p class="intro">{fp}</p>
</div>
{faq}
</div>
</section>'''

# ------------------------------------------------------------------ 13. Kontakt: Aufbau 07.11., Texte 16.11. (K12)
kh2, kp = kopf_text(v_kontakt)
form = such(r'<form class="formular".*?</form>', v_kontakt).replace('<p class="pseudo-h3">Kurze Anfrage</p>', '<p class="formular__titel">Kurze Anfrage</p>')
form = form.replace('<button class="btn btn--voll" type="submit">', '<button class="btn btn--blau" type="submit">')
kontakt = f'''<section class="kontakt" id="kontakt" aria-labelledby="t-kontakt" data-abschnitt="kontaktblock">
<div class="wrap">
<p class="auge">Kontakt</p>
<h2 id="t-kontakt">{kh2}</h2>
<p class="kontakt__satz">{kp}</p>
<a class="riesennummer" href="{TEL}" data-pos="kontaktblock">{TEL_TEXT}</a>
<div class="kontakt__raster">
<div>
<div class="cta"><a class="btn btn--wa btn--gross" href="{WA}" rel="noopener" target="_blank" data-pos="kontaktblock">{I['wa']}<span class="btn__zwei"><span class="btn__klein">Auch mit Foto</span><span class="btn__gross">WhatsApp schreiben</span></span></a></div>
{such(r'<dl>.*?</dl>', v_kontakt).replace('<a href="tel:', '<a data-pos="kontaktblock" href="tel:').replace('<a href="mailto:', '<a data-pos="kontaktblock" href="mailto:')}
</div>
{form}
</div>
</div>
</section>'''

neu_main = '\n\n'.join(['<main id="inhalt">', hero, anstehen, heute, leistungen, zg, bewertungen, verz, ablauf, team, gebiet, blick, ratgeber, fragen, kontakt]) + '\n</main>'
neu_main = neu_main.replace('&amp;text=', '&text=').replace('&text=', '&amp;text=')
neu = v[:v.index('</head>')] + g[g.index('</head>'):g.index('<main id="inhalt">')] + neu_main + g[g.index('</main>') + 7:]
for a, b in (('0176 74025524', TEL_TEXT), ('+4917674025524', '+491637221790')):
    neu = neu.replace(a, b)
open(os.path.join(WEB, 'index.html'), 'w', encoding='utf-8', newline='\n').write(neu)
print('index.html geschrieben,', len(neu), 'Zeichen')
