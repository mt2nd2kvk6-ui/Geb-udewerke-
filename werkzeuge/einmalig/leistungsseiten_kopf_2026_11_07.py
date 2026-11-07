#!/usr/bin/env python3
"""Einmalig 07.11.2026: neuer Seitenkopf für die zehn Leistungsseiten.
- Einstieg höchstens 25 Wörter mit Hauptkeyword (Fakten aus dem bisherigen Seitentext)
- nur Anrufen und WhatsApp als Knöpfe
- rechts das Objektmodell, die Zone der Leistung leuchtet
- bisheriger Einstiegstext (Kurzantwort) und Foto wandern an den Anfang des ersten Abschnitts, nichts geht verloren
Danach: python3 werkzeuge/layout_anwenden.py"""
import os, re, sys

BASIS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WEB = os.path.join(BASIS, 'website')
sys.path.insert(0, os.path.join(BASIS, 'werkzeuge'))
sys.argv = [sys.argv[0]]
import modell
import layout_anwenden as L

TEL = 'tel:+4917674025524'
I_TEL = L.I_TEL

SEITEN = {
    'hausmeisterservice.html': ('hausmeister', 'Ein fester Betreuer geht Ihr Objekt in Bruchsal ab, erledigt Kleinigkeiten sofort und schreibt alles ins Protokoll. Hausmeisterservice für Wohnanlagen, WEG und Gewerbe.'),
    'treppenhausreinigung.html': ('treppenhaus', 'Treppenhausreinigung in Bruchsal immer am gleichen Wochentag, nach schriftlichem Plan. Jede Reinigung wird am Aushang abgezeichnet, Mittel und Geräte sind inklusive.'),
    'gebaeudereinigung.html': ('gewerbe', 'Gebäudereinigung in Bruchsal für Keller, Tiefgarage, Müllraum und Glas. Nach schriftlichem Plan, Mittel und Geräte bringen wir mit.'),
    'bueroreinigung.html': ('buero', 'Büroreinigung in Bruchsal, bevor Ihr Team kommt oder nachdem es geht. Nach schriftlichem Reinigungsplan, mit festem Team, auch für Praxen.'),
    'gartenpflege.html': ('garten', 'Gartenpflege in Bruchsal von März bis November: Rasen, Hecken, Beete, Laub, Wege und Höfe. Das Schnittgut nehmen wir mit.'),
    'winterdienst.html': ('winter', 'Winterdienst in Bruchsal vom 1. November bis 31. März. Wir räumen und streuen, Sie bekommen zu jedem Einsatz das Protokoll.'),
    'entruempelung.html': ('keller', 'Entrümpelung in Bruchsal zum Festpreis nach Besichtigung. Keller, Dachboden, Wohnung oder Gewerbefläche, besenrein übergeben. Für kleine Räume reicht oft ein Foto per WhatsApp.'),
    'wohnungsuebergabe.html': ('wohnung', 'Wohnungsübergabe in Bruchsal mit Fotoprotokoll, Zählerständen und Mängelliste. Wir sind vor Ort, wenn Sie es nicht sein können.'),
    'kleinreparaturen.html': ('reparatur', 'Kleinreparaturen in Bruchsal gebündelt: Sie sammeln die Punkte, wir erledigen sie in einem Termin. Lampe, Silikon, Regal, Streichen, Klickvinyl.'),
    'metallarbeiten-schloesser.html': ('metall', 'Metallarbeiten in Bruchsal aus eigener Hand: Zäune, Tore, Geländer und kleinere Schweißarbeiten. Dazu Zylinder, Beschläge und Schließanlagen.'),
}

M = modell.bauen()
PUNKTE = {z: (t, u, x, y) for z, t, u, (x, y) in M['punkte']}

for datei, (zone, einstieg) in SEITEN.items():
    assert len(einstieg.split()) <= 25, (datei, len(einstieg.split()))
    p = os.path.join(WEB, datei)
    s = open(p, encoding='utf-8').read()
    m_sk = re.search(r'<section class="seitenkopf">.*?</section>', s, re.S)
    if 'id="modell"' in m_sk.group(0):
        print(datei, 'schon umgebaut'); continue
    sk = m_sk.group(0)
    krumen = re.search(r'<nav class="brotkrumen".*?</nav>', sk, re.S).group(0)
    h1 = re.search(r'<h1>.*?</h1>', sk, re.S).group(0)
    alt_einstieg = re.search(r'<p class="kurzantwort">(.*?)</p>', sk, re.S).group(1)
    figur = re.search(r'<figure>.*?</figure>', sk, re.S).group(0)
    figur = (figur.replace('<figure>', '<figure class="bild">').replace(' fetchpriority="high"', ' loading="lazy" decoding="async"'))
    figur = re.sub(r'sizes="[^"]*"', 'sizes="(max-width: 1023px) 100vw, 760px"', figur)
    t, u, x, y = PUNKTE[zone]
    svg = M['svg'].replace('aria-label="Modell eines Objekts mit Keller, Treppenhaus, Büro, Wohnungen, Halle, Garten, Gehweg und Gartentor"',
                           f'aria-label="Modell eines Objekts, hervorgehoben: {t}"')
    neu_sk = f'''<section class="seitenkopf"><div class="wrap">
{krumen}
<div class="seitenkopf__raster">
<div>
{h1}
<p class="kurzantwort">{einstieg}</p>
<div class="cta"><a class="btn btn--weiss btn--gross" href="{TEL}" data-pos="hero">{I_TEL}<span class="btn__zwei"><span class="btn__klein">Anrufen</span><span class="btn__gross">0176 74025524</span></span></a><a class="btn btn--wa btn--gross" href="{L.WA}" rel="noopener" target="_blank" data-pos="hero">{L.I_WA}<span class="btn__zwei"><span class="btn__klein">Foto oder Frage</span><span class="btn__gross">WhatsApp</span></span></a></div>
</div>
<div class="modell modell--seite" id="modell" data-fokus="{zone}">
<div class="himmel himmel--schnee" aria-hidden="true"></div>
<div class="himmel himmel--regen" aria-hidden="true"></div>
<div class="himmel himmel--nebel" aria-hidden="true"></div>
{svg}<span class="punkt an punkt--{"links" if x > 60 else "rechts"}" data-zone="{zone}" style="left:{x}%;top:{y}%" aria-hidden="true"><span class="punkt__kern"></span><span class="punkt__label"><b>{t}</b><small>{u}</small></span></span>
</div>
</div>
</div></section>'''
    s = s.replace(sk, neu_sk, 1)
    # bisherigen Einstieg und Foto an den Anfang des ersten Abschnitts
    m1 = re.search(r'(<section class="abschnitt"><div class="wrap inhalt-raster">\s*<div class="fliesstext">\s*<h2[^>]*>.*?</h2>)', s, re.S)
    s = s[:m1.end()] + f'\n<p class="kurzantwort">{alt_einstieg}</p>\n{figur}' + s[m1.end():]
    open(p, 'w', encoding='utf-8', newline='\n').write(s)
    print(datei, 'umgebaut:', len(einstieg.split()), 'Wörter im Einstieg')
