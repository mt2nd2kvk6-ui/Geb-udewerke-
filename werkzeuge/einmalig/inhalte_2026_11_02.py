#!/usr/bin/env python3
"""Einmalig 02.11.2026: Anrufnummer, Meisterbrief, 'vier Mann' statt Gesellschafter (außer Impressum),
ein Kontaktblock je Seite mit eigener Überschrift, Entrümpelung ausgebaut."""
import glob, os, re
WEB = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'website')
dateien = sorted(glob.glob(WEB + '/*.html') + glob.glob(WEB + '/ratgeber/*.html')) + [WEB + '/llms.txt', WEB + '/ratgeber/index.php']
G = 'https://share.google/v7XolrfYaCO55YrZz'
log = []

def alle(s, datei):
    # --- Anrufnummer (WhatsApp-Links und WhatsApp-Hinweise bleiben)
    s = s.replace('tel:+491637221790', 'tel:+4917674025524')
    s = s.replace('+49 163 7221790', '+49 176 74025524')
    s = s.replace('Telefonisch unter 01637221790', 'Telefonisch unter 0176 74025524')
    s = re.sub(r'(?<!WhatsApp an )0163 7221790', '0176 74025524', s)
    if datei == 'llms.txt':
        s = s.replace('- Telefon: 0176 74025524 (+49 176 74025524)', '- Telefon: 0176 74025524 (+49 176 74025524)\n- WhatsApp-Nummer: 0163 7221790')
    # --- Meisterbrief
    for a, b in [
        ('im eigenen Team mit geprüftem Industriemeister Metall', 'im eigenen Team mit Meisterbrief'),
        ('Im Team arbeiten ein geprüfter Industriemeister Metall und ein gelernter Metallbauer', 'Im Team arbeiten ein Kollege mit Meisterbrief und ein gelernter Metallbauer'),
        ('Im Team arbeiten ein Industriemeister Metall und ein gelernter Metallbauer', 'Im Team arbeiten ein Kollege mit Meisterbrief und ein gelernter Metallbauer'),
        ('Im Team arbeitet ein geprüfter Industriemeister Metall.', 'Im Team arbeitet ein Kollege mit Meisterbrief.'),
        ('Im Team: ein geprüfter Industriemeister Metall.', 'Im Team: ein Kollege mit Meisterbrief.'),
        ('vom Industriemeister Metall:', 'vom Meister mit Meisterbrief:'),
        ('ein geprüfter Industriemeister Metall und ein gelernter Metallbauer mit', 'ein Kollege mit Meisterbrief und ein gelernter Metallbauer mit'),
        ('"credentialCategory":"Meisterbrief","name":"Geprüfter Industriemeister Metall (IHK)"', '"credentialCategory":"Meisterbrief","name":"Meisterbrief"'),
        ('<span>Weiterbildung</span>Geprüfter Industriemeister Metall (IHK)', '<span>Meisterbrief</span>Metallmeister'),
        ('Unser Team kommt aus unterschiedlichen Richtungen: Industriemeister Metall,', 'Wir kommen aus ganz unterschiedlichen Ecken: Meisterbrief,'),
        ('Industriemeister Metall, Metallbauer, Industriemechaniker und Kaufmann: vier Gesellschafter,', 'Metallmeister, Metallbauer, Industriemechaniker und Kaufmann: vier Mann,'),
        ('Fatih Altun (geprüfter Industriemeister Metall IHK,', 'Fatih Altun (Meisterbrief,'),
        ('Geprüfter Industriemeister Metall (IHK)', 'Kollege mit Meisterbrief'),
    ]:
        s = s.replace(a, b)
    s = re.sub(r'geprüfte[rnm]? Industriemeister Metall( \(IHK\)| IHK)?', 'Kollege mit Meisterbrief', s)
    s = s.replace('ein Industriemeister Metall', 'ein Kollege mit Meisterbrief')
    if datei == 'impressum.html':
        return s
    # --- vier Mann statt Gesellschafter
    for a, b in [
        ('Hinter dem Betrieb stehen vier Gesellschafter: Fatih Altun, Enes Yesildag, Burak Kartal und Julian Bender. Jeder ist für einen Leistungsbereich zuständig, und jedes Objekt hat bei uns einen festen Betreuer.',
         'Wir sind vier Mann: Fatih Altun, Enes Yesildag, Burak Kartal und Julian Bender. Jeder von uns kümmert sich um seinen Bereich, und jedes Objekt hat bei uns einen festen Betreuer, der es kennt.'),
        ('Uns verbindet der Anspruch, dass', 'Gemeinsam ist uns, dass'),
        ('vier Gesellschafter aus Metallbau, Industriemechanik und Vertrieb', 'vier Mann aus Metallbau, Industriemechanik und Vertrieb'),
        ('geschrieben von den Gesellschaftern von Gebäudewerke in Bruchsal', 'geschrieben vom Team von Gebäudewerke in Bruchsal'),
        ('Geschrieben von den vier Gesellschaftern von Gebäudewerke, jeweils zu ihrem Fachgebiet.', 'Geschrieben von uns vier bei Gebäudewerke, jeder zu dem Thema, das er im Alltag macht.'),
        ('Fachartikel der Gesellschafter zu', 'Fachartikel aus unserem Team zu'),
        ('<dt>Gesellschafter</dt>', '<dt>Wir vier</dt>'),
        ('<span class="team-karte__rolle">Gesellschafter</span>', ''),
        ('- Gesellschafter: Fatih Altun', '- Team (vier Mann): Fatih Altun'),
    ]:
        s = s.replace(a, b)
    s = re.sub(r'("jobTitle":")Gesellschafter, ', r'\1', s)
    s = re.sub(r'(<p class="steckbrief__rolle">)Gesellschafter, ', r'\1', s)
    return s

CTA = {  # Seite: Überschrift des einen Kontaktblocks
    'index.html': 'Lernen Sie uns beim Ortstermin kennen',
    'hausmeisterservice.html': 'Ihr Hausmeisterservice aus Bruchsal',
    'treppenhausreinigung.html': 'Ihre Treppenhausreinigung aus Bruchsal',
    'gebaeudereinigung.html': 'Ihr Gebäudereiniger aus Bruchsal',
    'bueroreinigung.html': 'Ihre Büroreinigung aus Bruchsal',
    'gartenpflege.html': 'Ihre Gartenpflege aus Bruchsal',
    'winterdienst.html': 'Ihr Winterdienst aus Bruchsal',
    'entruempelung.html': 'Ihre Entrümpelung in Bruchsal zum Festpreis',
    'wohnungsuebergabe.html': 'Ihre Wohnungsübergabe in Bruchsal mit Protokoll',
    'kleinreparaturen.html': 'Ihr Handwerker für Kleinreparaturen in Bruchsal',
    'metallarbeiten-schloesser.html': 'Ihre Metallarbeiten aus Bruchsal',
    'preise.html': 'Ihr Festpreis nach dem Ortstermin',
    'einsatzgebiet.html': 'Ein Ansprechpartner für Ihr Objekt im Landkreis Karlsruhe',
    'ueber-uns.html': 'Lernen Sie uns beim Ortstermin kennen',
}
STERNE = f'<p class="cta-sterne"><a class="google-hinweis" href="{G}" rel="noopener" target="_blank">5,0 Sterne auf Google</a></p>'

def cta(s, datei):
    if datei not in CTA: return s
    if datei == 'index.html':
        m = re.search(r'(<section class="abschnitt abschnitt--blau"[^>]*>.*?<h2[^>]*>)(.*?)(</h2>)', s, re.S)
    else:
        m = re.search(r'(<section class="cta-band"[^>]*>.*?<h2[^>]*>)(.*?)(</h2>)', s, re.S)
    if not m: log.append(f'{datei}: Kontaktblock nicht gefunden'); return s
    s = s[:m.start(2)] + CTA[datei] + s[m.end(2):]
    ende = s.find('</h2>', m.start(2)) + 5
    if 'cta-sterne' not in s[ende:ende + 400]:
        p = s.find('</p>', ende)          # nach dem Einleitungssatz des Blocks
        if p != -1 and p - ende < 600: s = s[:p + 4] + STERNE + s[p + 4:]
        else: s = s[:ende] + STERNE + s[ende:]
    return s

ENTR_NEU = '''
<h3>Haushaltsauflösung nach einem Todesfall oder beim Umzug ins Heim</h3>
<p>Bei einer Haushaltsauflösung geht es selten nur um Möbel. Oft müssen Angehörige eine Wohnung in Bruchsal räumen lassen, während sie selbst weiter weg wohnen. Wir besichtigen die Wohnung, schicken Ihnen das Angebot schriftlich und stimmen alles per Telefon, E-Mail oder WhatsApp ab. Den Schlüssel bekommen wir von Ihnen, Ihrer Verwaltung oder einer Vertrauensperson. Vor und nach der Räumung machen wir Fotos, damit Sie sehen, wie die Wohnung übergeben wird.</p>
<h3>Wertsachen, Dokumente und Erinnerungsstücke</h3>
<p>Was Sie behalten möchten, markieren Sie vorher oder nennen es uns bei der Besichtigung. Wertgegenstände und Dokumente sprechen wir vor dem Termin ab und legen sie beim Ausräumen zur Seite. Verwertbares sortieren wir aus, statt es wegzuwerfen.</p>
<h3>Was wir mitnehmen und was nicht</h3>
<p>Möbel, Sperrmüll, Hausrat und Kellerinhalte räumen wir komplett und entsorgen sie getrennt nach Fraktionen. Gefährliche Abfälle sind ausgenommen. Was genau dazugehört, klären wir bei der Besichtigung, damit am Räumungstag nichts offen bleibt.</p>
<h3>Entrümpelung in Bruchsal und den Ortsteilen</h3>
<p>Wir räumen in der Bruchsaler Kernstadt, in Büchenau, Heidelsheim, Helmsheim, Obergrombach und Untergrombach, in Hambrücken und im übrigen Landkreis Karlsruhe. Für Keller und Garagen reichen oft Fotos per WhatsApp, bei Wohnungen kommen wir kostenlos vorbei. Nach der Räumung schließen sich auf Wunsch Reinigung, kleine Reparaturen und die <a href="wohnungsuebergabe.html">Wohnungsübergabe mit Protokoll</a> an. Für Häuser, die wir danach laufend betreuen, übernimmt unser <a href="hausmeisterservice.html">Hausmeisterservice</a> die Kontrollgänge.</p>
'''

def entruempelung(s):
    if 'Haushaltsauflösung nach einem Todesfall' in s: return s
    a = 'Für laufend betreute Objekte stellen wir die Mülltonnen raus, holen sie wieder rein und halten den Müllplatz sauber.</p>'
    assert s.count(a) == 1
    return s.replace(a, a + ENTR_NEU, 1)

for p in dateien:
    d = os.path.relpath(p, WEB); s = open(p, encoding='utf-8').read(); n = alle(s, d)
    n = cta(n, d)
    if d == 'entruempelung.html': n = entruempelung(n)
    if n != s: open(p, 'w', encoding='utf-8').write(n)
print('\n'.join(log) or 'ok')
