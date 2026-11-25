#!/usr/bin/env python3
"""Einmalig Relaunch 12/2026, Schritt 1: Seiten aus drei Ständen zusammenführen.

Quellen (feste Commits, damit der Lauf reproduzierbar bleibt):
  G = f38d527  claude/gallant-einstein-ossqki    07.11.2026  Gestaltung, Interaktion, Seitenkopf, Preisangleichung
  V = 0638e7d  claude/vertrauen-menue-2026-11-16 16.11.2026  Texte, Telefon, Bewertungen, Trust, Barrierefreiheit
  N = 5b9d09e  claude/nice-planck-khtul6         06.11.2026  Consent Mode v2, tracking.js

Regel: Gestaltung, CSS, JavaScript und Aufbau aus G. Kopfdaten (Title, Metas, JSON-LD) und alle
Änderungen vom 16.11. aus V. Der Inhalt in <main> von V entspricht nachweislich dem Stand vor dem 07.11.
plus den Änderungen vom 16.11. (Vergleich in projekt/relaunch-2026-12/konflikte.md), deshalb wird
der Inhalt aus G genommen und die Änderungen vom 16.11. werden gezielt übertragen.

Die Startseite (index.html) wird nicht hier, sondern in relaunch_2026_12_startseite.py zusammengeführt.
Aufruf: python3 werkzeuge/einmalig/relaunch_2026_12_zusammenfuehren.py"""
import os, re, subprocess

BASIS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WEB = os.path.join(BASIS, 'website')
G, V, N = 'f38d527', '0638e7d', '5b9d09e'
protokoll = []


def git(rev, pfad):
    r = subprocess.run(['git', 'show', f'{rev}:{pfad}'], cwd=BASIS, capture_output=True)
    return r.stdout.decode('utf-8') if r.returncode == 0 else None


def dateien(rev):
    r = subprocess.run(['git', 'ls-tree', '-r', '--name-only', rev, '--', 'website'], cwd=BASIS, capture_output=True, text=True)
    return [x[len('website/'):] for x in r.stdout.split()]


def kopf(s):
    return s[:s.index('</head>')]


def rumpf(s):
    return s[s.index('</head>'):]


def abschnitt(s, muster):
    """Liefert die ganze <section …>…</section>, deren Starttag auf muster passt (ohne Verschachtelung)."""
    m = re.search(r'<section\b[^>]*' + muster + r'[^>]*>.*?</section>', s, re.S)
    return m.group(0) if m else None


# 16.11.: Telefonnummer
TELEFON = [('0176 74025524', '0163 7221790'), ('+4917674025524', '+491637221790'), ('+49 176 74025524', '+49 163 7221790'),
           ('017674025524', '01637221790')]
# 16.11.: seitlich scrollbare Tabellen per Tastatur erreichbar (Site-Audit)
TABELLE_ALT = '<div class="tabellen-rahmen">'
TABELLE_NEU = '<div class="tabellen-rahmen" tabindex="0" role="region" aria-label="Tabelle, seitlich scrollbar">'


def trust_abschnitt(v_seite):
    """Abschnitt „Geprüft gelistet und bewertet“ vom 16.11. Klassen umbenannt, weil .vertrauen im
    Gestaltungssystem vom 07.11. der Vertrauensstreifen ist (Texte und Links unverändert)."""
    t = abschnitt(v_seite, r'aria-labelledby="vertrauen-titel"')
    if t is None:
        return None
    return umbenennen(t)


def umbenennen(t):
    t = re.sub(r'<section class="abschnitt(?: abschnitt--kalk)? vertrauen(?: presse-hinweis)?"',
               lambda m: m.group(0).replace(' vertrauen presse-hinweis', ' verzeichnisse verzeichnisse--presse').replace(' vertrauen', ' verzeichnisse'), t)
    for alt, neu in (('vertrauen__kopf', 'verzeichnisse__kopf'), ('vertrauen__raster', 'verzeichnisse__raster'),
                     ('vertrauen__presse', 'verzeichnisse__presse'), ('vertrauen-titel', 'verzeichnisse-titel')):
        t = t.replace(alt, neu)
    return t


def seite_zusammenfuehren(name, g, v):
    s = kopf(v) + rumpf(g)            # Kopfdaten vom 16.11., Aufbau vom 07.11.
    for a, b in TELEFON:
        s = s.replace(a, b)
    s = s.replace(TABELLE_ALT, TABELLE_NEU)
    # Kontaktdaten wie am 16.11. zusammengefasst
    s = s.replace('<div><dt>Telefon</dt><dd><a href="tel:+491637221790"', '<div><dt>Telefon und WhatsApp</dt><dd><a href="tel:+491637221790"')
    if name in ('ueber-uns.html', 'kontakt.html'):
        t = trust_abschnitt(v)
        if name == 'ueber-uns.html':
            i = s.index('<section class="cta-band"')
        else:
            i = s.index('</main>')
        s = s[:i] + t + '\n' + s[i:]
        protokoll.append(f'{name}: Abschnitt „Geprüft gelistet und bewertet“ vom 16.11. eingefügt')
    if name == 'winterdienst.html':
        p = umbenennen(abschnitt(v, r'class="abschnitt vertrauen presse-hinweis"'))
        i = s.index('<section class="abschnitt abschnitt--kalk" id="kurz-beantwortet"')
        s = s[:i] + p + '\n' + s[i:]
        protokoll.append(f'{name}: Presse-Hinweis (openPR) vom 16.11. eingefügt')
    return s


def main():
    g_dateien, v_dateien = set(dateien(G)), set(dateien(V))
    seiten = sorted(x for x in v_dateien if x.endswith('.html') or x == 'ratgeber/index.php')
    for name in seiten:
        if name == 'index.html':
            continue
        v = git(V, 'website/' + name)
        g = git(G, 'website/' + name) if name in g_dateien else None
        if g is None:
            protokoll.append(f'{name}: nur im Stand 16.11. vorhanden, unverändert übernommen')
            neu = v
        else:
            neu = seite_zusammenfuehren(name, g, v)
        open(os.path.join(WEB, name), 'w', encoding='utf-8', newline='\n').write(neu)
    # Gestaltung und Interaktion vom 07.11.
    for a in ('assets/css/style.css', 'assets/js/main.js'):
        open(os.path.join(WEB, a), 'w', encoding='utf-8', newline='\n').write(git(G, 'website/' + a))
        protokoll.append(f'{a}: Stand 07.11. (G)')
    # Tracking vom 06.11.
    for a in ('assets/js/consent.js', 'assets/js/tracking.js'):
        open(os.path.join(WEB, a), 'w', encoding='utf-8', newline='\n').write(git(N, 'website/' + a))
        protokoll.append(f'{a}: Stand 06.11. (N)')
    # Archivo wird nach dem Relaunch von keiner Seite mehr geladen
    alt = os.path.join(WEB, 'assets/fonts/archivo-var.woff2')
    if os.path.exists(alt):
        os.remove(alt)
        protokoll.append('assets/fonts/archivo-var.woff2: entfernt (nur vom Live-Design 10.11. genutzt)')
    print('\n'.join(protokoll))


if __name__ == '__main__':
    main()
