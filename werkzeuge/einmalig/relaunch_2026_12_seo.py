#!/usr/bin/env python3
"""Einmalig Relaunch 12/2026, Schritt 3: Korrekturen aus dem SEO-Scan vom 25.11.2026.

5. Titles: treppenhausreinigung.html auf höchstens 60 Zeichen und 575 px, winterdienst.html
   Title und Description auf Klicks (Hauptkeyword vorn, Saisonpreis aus preise.html, Einsatzprotokoll).
7. Geplante Ratgeber, die am Tag der Veröffentlichung noch nicht erschienen sind, auf den 15.01.2027.
   [PRÜFEN: Inhaber bestätigt Datum]. Geändert werden meta artikel-datum und, damit die Seite nichts
   Falsches behauptet, artikel-aktualisiert, datePublished/dateModified und die Zeile „veröffentlicht am“
   dieser vier Beiträge (Konflikt K15). Erschienene Beiträge bleiben unverändert.
Ersetzt jeweils alle Kopien (title, JSON-LD). Aufruf: python3 werkzeuge/einmalig/relaunch_2026_12_seo.py"""
import datetime, json, os, re

BASIS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WEB = os.path.join(BASIS, 'website')

TITEL = {
    'treppenhausreinigung.html': ('Treppenhausreinigung Bruchsal | Fester Plan, fester Wochentag',
                                  'Treppenhausreinigung Bruchsal | Plan und fester Wochentag'),
    'winterdienst.html': ('Winterdienst Bruchsal mit Einsatzprotokoll | Gebäudewerke',
                          'Winterdienst Bruchsal ab 1.220 € netto/Saison | Einsatzprotokoll'),
}
BESCHREIBUNG = {
    'winterdienst.html': ('Winterdienst in Bruchsal: Räumen und Streuen von Gehwegen, Zufahrten und Parkplätzen, Saison November bis März, jeder Einsatz protokolliert.',
                          'Winterdienst in Bruchsal: Saisonpauschale ab 1.220 € netto bis 120 m², 1. November bis 31. März. Zu jedem Einsatz ein Protokoll. Ortstermin kostenlos.'),
}
VERSCHIEBEN = ['kosten-hausmeisterservice-bruchsal', 'hausmeisterservice-weg-bruchsal',
               'dienstleister-wechseln-hausmeister', 'treppenhaus-rettungsweg']
NEU_DATUM = '2027-01-15'


def lesen(n):
    return open(os.path.join(WEB, n), encoding='utf-8').read()


def schreiben(n, s):
    open(os.path.join(WEB, n), 'w', encoding='utf-8', newline='\n').write(s)


def json_text(t):
    return json.dumps(t, ensure_ascii=False)[1:-1]


for seite, (alt, neu) in TITEL.items():
    s = lesen(seite)
    if alt in s or json_text(alt) in s:
        s = s.replace(f'<title>{alt}</title>', f'<title>{neu}</title>').replace('"' + json_text(alt) + '"', '"' + json_text(neu) + '"')
        print(f'{seite}: Title → {neu}')
    schreiben(seite, s)
for seite, (alt, neu) in BESCHREIBUNG.items():
    s = lesen(seite)
    if alt in s:
        s = s.replace(f'<meta name="description" content="{alt}">', f'<meta name="description" content="{neu}">').replace('"' + json_text(alt) + '"', '"' + json_text(neu) + '"')
        print(f'{seite}: Description → {neu}')
    schreiben(seite, s)

heute = datetime.date.today().isoformat()
for slug in VERSCHIEBEN:
    n = f'ratgeber/{slug}.html'
    s = lesen(n)
    alt = re.search(r'<meta name="artikel-datum" content="(\d{4}-\d{2}-\d{2})">', s).group(1)
    if alt == NEU_DATUM:
        continue
    if alt <= heute:
        print(f'{n}: bereits erschienen ({alt}), bleibt unverändert')
        continue
    alt_de, neu_de = f'{alt[8:10]}.{alt[5:7]}.{alt[:4]}', f'{NEU_DATUM[8:10]}.{NEU_DATUM[5:7]}.{NEU_DATUM[:4]}'
    s = s.replace(f'<meta name="artikel-datum" content="{alt}">', f'<meta name="artikel-datum" content="{NEU_DATUM}">')
    s = s.replace(f'<meta name="artikel-aktualisiert" content="{alt}">', f'<meta name="artikel-aktualisiert" content="{NEU_DATUM}">')
    s = s.replace(f'"datePublished":"{alt}"', f'"datePublished":"{NEU_DATUM}"').replace(f'"dateModified":"{alt}"', f'"dateModified":"{NEU_DATUM}"')
    s = re.sub(r'(<p class="beitrag-meta">[^<]*veröffentlicht am )' + re.escape(alt_de), r'\g<1>' + neu_de, s)
    # Jahreszahl im Title folgt dem Erscheinungsjahr (Konvention der Ratgeber-Titles, seo_pruefen.py)
    t = re.search(r'<title>(.*?)</title>', s).group(1)
    if alt[:4] in t and alt[:4] != NEU_DATUM[:4]:
        t_neu = t.replace(alt[:4], NEU_DATUM[:4])
        s = s.replace(f'<title>{t}</title>', f'<title>{t_neu}</title>').replace('"' + json_text(t) + '"', '"' + json_text(t_neu) + '"')
    schreiben(n, s)
    print(f'{n}: {alt} → {NEU_DATUM}')
