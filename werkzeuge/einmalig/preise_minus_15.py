#!/usr/bin/env python3
"""Einmalig 02.11.2026: alle Netto-Preise minus 15 %, auf volle Euro gerundet (kaufmännisch),
Brutto = Netto x 1,19 auf volle Euro gerundet (wie bisher auf der Website)."""
import glob, os, re
from decimal import Decimal, ROUND_HALF_UP
WEB = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'website')
r = lambda x: int(Decimal(x).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
neu_netto = lambda n: r(Decimal(n) * Decimal('0.85'))
brutto = lambda n: r(Decimal(n) * Decimal('1.19'))
def fmt(n): return f'{n:,}'.replace(',', '.')
def zahl(t): return int(t.replace('.', ''))

# 1) Tabellen der Preisseite: Spalten aus der Kopfzeile (netto/brutto)
p = os.path.join(WEB, 'preise.html'); s = open(p, encoding='utf-8').read()
NETTO, BRUTTO = {}, {}            # alter Wert -> neuer Wert
def tabelle(m):
    t = m.group(0)
    kopf = [re.sub(r'<[^>]+>', '', c).lower() for c in re.findall(r'<th\b[^>]*>(.*?)</th>', t.split('</tr>')[0], re.S)]
    def zeile(z):
        zellen = re.findall(r'(<t[hd]\b[^>]*>)(.*?)(</t[hd]>)', z.group(0), re.S)
        if not zellen or '<th scope="col"' in z.group(0): return z.group(0)
        aus = z.group(0); netto_neu = None
        for i, (a, inhalt, e) in enumerate(zellen):
            if i >= len(kopf) or not re.search(r'\d ?€', inhalt): continue
            mm = re.search(r'(\d{1,3}(?:\.\d{3})?)(\s?€)', inhalt); alt = zahl(mm.group(1))
            if 'netto' in kopf[i]:
                n = neu_netto(alt); NETTO[alt] = n; netto_neu = n; wert = n
            elif 'brutto' in kopf[i]:
                b = brutto(netto_neu); BRUTTO[alt] = b; wert = b
            else: continue
            neu = inhalt[:mm.start(1)] + fmt(wert) + inhalt[mm.end(1):]
            aus = aus.replace(a + inhalt + e, a + neu + e, 1)
        return aus
    return re.sub(r'<tr\b.*?</tr>', zeile, t, flags=re.S)
s = re.sub(r'<table\b.*?</table>', tabelle, s, flags=re.S)
open(p, 'w', encoding='utf-8').write(s)

# Weitere Netto-Werte, die nur im Text stehen
for alt in (90,): NETTO[alt] = neu_netto(alt)
BRUTTO_ZU_NETTO = {107: 90}
for b, n in BRUTTO_ZU_NETTO.items(): BRUTTO[b] = brutto(NETTO[n])
# Brutto-Werte im Fließtext, die zu Tabellen-Netto gehören
for n_alt in list(NETTO): BRUTTO.setdefault(brutto(n_alt), brutto(NETTO[n_alt]))
JAHR = {1560: NETTO[130] * 12, 2280: NETTO[190] * 12}

# 2) Fließtext und JSON-LD auf allen Seiten (Tabellen der Preisseite sind schon erledigt)
def text_ersetzen(t, datei):
    def preis(m):
        v = zahl(m.group(2)); kontext = t[max(0, m.start() - 60):m.end() + 25].lower()
        if v in JAHR and 'jahr' in kontext: return m.group(1) + fmt(JAHR[v]) + m.group(3)
        ist_brutto = 'brutto' in t[max(0, m.start() - 25):m.start()].lower() or re.match(r'\s?€\s*(brutto|beziehungsweise)', t[m.end(2):m.end(2) + 25].lower()) is not None
        if v == 280:                     # einzige Doppelbelegung: im Fließtext immer Netto (großes Objekt)
            ist_brutto = False
        if ist_brutto and v in BRUTTO: return m.group(1) + fmt(BRUTTO[v]) + m.group(3)
        if v in NETTO and v not in BRUTTO: return m.group(1) + fmt(NETTO[v]) + m.group(3)
        if v in BRUTTO and v not in NETTO: return m.group(1) + fmt(BRUTTO[v]) + m.group(3)
        if v in NETTO: return m.group(1) + fmt(NETTO[v]) + m.group(3)
        return m.group(0)
    teile = re.split(r'(<table\b.*?</table>)', t, flags=re.S) if datei == 'preise.html' else [t]
    aus = []
    for i, teil in enumerate(teile):
        if teil.startswith('<table'): aus.append(teil); continue
        t = teil
        teil = re.sub(r'(^|[^\d.])(\d{1,3}(?:\.\d{3})?)(\s?€)', preis, teil)
        teil = re.sub(r'("(?:price|lowPrice|highPrice|minPrice|maxPrice)":"?)(\d+)', lambda m: m.group(1) + str(NETTO.get(int(m.group(2)), int(m.group(2)))), teil)
        aus.append(teil)
    return ''.join(aus)

geaendert = []
for p in sorted(glob.glob(WEB + '/*.html') + glob.glob(WEB + '/ratgeber/*.html')) + [WEB + '/llms.txt', WEB + '/ratgeber/index.php']:
    s = open(p, encoding='utf-8').read(); n = text_ersetzen(s, os.path.basename(p))
    if n != s: open(p, 'w', encoding='utf-8').write(n); geaendert.append(os.path.relpath(p, WEB))
print('Netto alt->neu:', dict(sorted(NETTO.items())))
print('Brutto alt->neu:', dict(sorted(BRUTTO.items())))
print('Jahr:', JAHR); print('geändert:', len(geaendert), 'Dateien')
