#!/usr/bin/env python3
"""Erzeugt das isometrische Objektmodell der Startseite (SVG + Hotspots), mit Wetterzuständen.
Wird von werkzeuge/einmalig/startseite_2026_11_07.py genutzt. Nach Änderungen dort erneut ausführen.
Alles wird aus Quadern berechnet: Erdreich mit Keller, Wohn- und Geschäftshaus, Halle,
Garten mit Hecke und Bäumen, Gehweg, Zaun mit Gartentor, Mülltonnen.
Jede Zone entspricht einer Leistung. Ausgabe: dict mit 'svg' und 'punkte'."""
import math

S = 22.0                      # Pixel je Einheit
C30 = math.cos(math.radians(30))


def iso(x, y, z):
    return ((x - y) * C30 * S, (x + y) * 0.5 * S - z * S)


class Szene:
    def __init__(self):
        self.teile = []        # (tiefe, zone, svg)
        self.xs, self.ys = [], []

    def poly(self, pts, fill, zone, tiefe, extra=''):
        p = [iso(*q) for q in pts]
        for a, b in p:
            self.xs.append(a); self.ys.append(b)
        d = ' '.join(f'{a:.1f},{b:.1f}' for a, b in p)
        rand = '' if 'stroke=' in extra else f' stroke="{fill}" stroke-width=".6" stroke-linejoin="round"'
        self.teile.append((tiefe, zone, f'<polygon points="{d}" fill="{fill}"{rand}{extra}/>'))

    def roh(self, svg, zone, tiefe):
        self.teile.append((tiefe, zone, svg))

    def quader(self, x0, y0, z0, x1, y1, z1, farben, zone, tiefe=None, seiten='tlr'):
        t, l, r = farben
        tiefe = (x0 + y0) if tiefe is None else tiefe
        if 'l' in seiten:
            self.poly([(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)], l, zone, tiefe)
        if 'r' in seiten:
            self.poly([(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)], r, zone, tiefe + 0.001)
        if 't' in seiten:
            self.poly([(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], t, zone, tiefe + 0.002)

    # Rechteck auf der linken Fassade (y = konstant), Breite entlang x
    def fl(self, y, x0, x1, z0, z1, fill, zone, tiefe, extra=''):
        self.poly([(x0, y, z0), (x1, y, z0), (x1, y, z1), (x0, y, z1)], fill, zone, tiefe, extra)

    # Rechteck auf der rechten Fassade (x = konstant), Breite entlang y
    def fr(self, x, y0, y1, z0, z1, fill, zone, tiefe, extra=''):
        self.poly([(x, y0, z0), (x, y1, z0), (x, y1, z1), (x, y0, z1)], fill, zone, tiefe, extra)


# Farben: weißes Architekturmodell auf Nachtblau, Licht in Signalgelb
WEISS = ('#F4F7FB', '#DCE4EE', '#B4C3D5')
HALLE = ('#EEF2F7', '#D3DCE7', '#A9B9CC')
ERDE = ('#E4EAF1', '#16355A', '#112C4C')
HECKE = ('#A9CDB2', '#8CB898', '#74A183')
GLAS, GLAS_R, LICHT = '#2C4C73', '#24426A', '#FFD21E'
LINIE = '#8FA3BA'


def bauen():
    s = Szene()
    # Erdreich als Schnittmodell, links vorne der Keller im Schnitt
    s.quader(0, 0, -2.4, 16, 11, 0, ERDE, 'grund', tiefe=-100)
    for z in (-0.8, -1.6):   # Erdschichten
        a, b = iso(0, 11, z), iso(16, 11, z)
        s.roh(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#2A4C74" stroke-width="1" stroke-dasharray="3 5"/>', 'grund', -99)
    # Keller: dunkler Raum im Schnitt mit Regal und Kisten
    s.fl(11, 4.2, 10.4, -2.15, -0.25, '#0A1C33', 'keller', -98)
    s.fl(11, 4.2, 10.4, -2.15, -2.0, '#1E3C62', 'keller', -97.9)
    for xa, za, w, h in ((4.7, -2.0, 1.1, 0.75), (6.0, -2.0, 0.8, 1.05), (6.05, -0.95, 0.7, 0.45), (9.0, -2.0, 1.0, 0.6), (9.15, -1.4, 0.7, 0.4)):
        s.fl(11, xa, xa + w, za, za + h, '#C9A06A', 'keller', -97.8, ' stroke="#8A6A40" stroke-width=".6"')
    for (xa, xb, za, zb) in ((7.2, 8.6, -1.25, -1.25), (7.2, 8.6, -0.6, -0.6), (7.2, 7.2, -2.0, -0.4), (8.6, 8.6, -2.0, -0.4)):
        a, b = iso(xa, 11, za), iso(xb, 11, zb)
        s.roh(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#7F95AE" stroke-width="1.4"/>', 'keller', -97.7)
    # Rasen links vorne, Hof rechts
    s.poly([(0.15, 2.4, 0.01), (3.7, 2.4, 0.01), (3.7, 9.2, 0.01), (0.15, 9.2, 0.01)], '#C9DFCF', 'garten', -90)
    s.poly([(11.0, 0.3, 0.01), (15.9, 0.3, 0.01), (15.9, 9.4, 0.01), (11.0, 9.4, 0.01)], '#D7DFE9', 'gewerbe', -89)
    for x in (13.0, 14.6):
        a, b = iso(x, 7.9, 0.02), iso(x, 9.3, 0.02)
        s.roh(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#FFFFFF" stroke-width="1.6"/>', 'gewerbe', -88)
    # Gehweg: Pflaster grau, bei Frost oder Schnee weiß mit Streugut (Ebene .schnee-belag)
    s.quader(0, 9.6, 0, 16, 11, 0.16, ('#C9D3DE', '#AEBBCA', '#97A6B8'), 'winter', tiefe=-80)
    import random
    random.seed(7)
    weiss = [iso(0, 9.6, 0.161), iso(16, 9.6, 0.161), iso(16, 11, 0.161), iso(0, 11, 0.161)]
    d = ' '.join(f'{a:.1f},{b:.1f}' for a, b in weiss)
    punkte = f'<polygon points="{d}" fill="#FFFFFF"/>'
    for _ in range(70):
        x, y = random.uniform(0.3, 15.7), random.uniform(9.75, 10.9)
        a = iso(x, y, 0.16)
        punkte += f'<circle cx="{a[0]:.1f}" cy="{a[1]:.1f}" r="{random.choice((0.9, 1.1, 1.3))}" fill="{random.choice(("#9AA9BB", "#B8892F", "#7C8DA2"))}"/>'
    s.roh('<g class="schnee-belag">' + punkte + '</g>', 'winter', -79)
    # Garten: Hecke und zwei Bäume links vom Haus
    s.quader(0.3, 2.6, 0, 1.0, 9.0, 1.35, HECKE, 'garten', tiefe=1.0)
    k = [iso(0.3, 2.6, 1.36), iso(1.0, 2.6, 1.36), iso(1.0, 9.0, 1.36), iso(0.3, 9.0, 1.36)]
    s.roh('<polygon class="schnee-kappe" points="' + ' '.join(f'{a:.1f},{b:.1f}' for a, b in k) + '" fill="#FFFFFF"/>', 'garten', 1.01)
    for i, (bx, by, r) in enumerate(((1.9, 5.5, 1.0), (2.5, 8.0, 1.2))):
        a = iso(bx, by, 0); k = iso(bx, by, 2.4)
        s.roh(f'<g class="baum"><rect x="{a[0] - 2.5:.1f}" y="{k[1]:.1f}" width="5" height="{a[1] - k[1]:.1f}" fill="#8A6F55"/>'
              f'<circle cx="{k[0]:.1f}" cy="{k[1] - r * S * 0.35:.1f}" r="{r * S:.1f}" fill="#8DBB9A"/>'
              f'<circle cx="{k[0] - r * S * 0.25:.1f}" cy="{k[1] - r * S * 0.55:.1f}" r="{r * S * 0.62:.1f}" fill="#A6CDB0"/></g>',
              'garten', 1.5 + i * 0.1)
    # Haus: 4 Geschosse
    X0, Y0, X1, Y1, H = 4, 0.8, 10.5, 6.4, 10
    s.quader(X0, Y0, 0, X1, Y1, H, WEISS, 'haus', tiefe=5)
    s.poly([(X0 + .25, Y0 + .25, H + .01), (X1 - .25, Y0 + .25, H + .01), (X1 - .25, Y1 - .25, H + .01), (X0 + .25, Y1 - .25, H + .01)], '#E6ECF3', 'haus', 5.4)
    s.quader(7.6, 1.4, H, 9.0, 2.8, H + 0.9, WEISS, 'haus', tiefe=5.5)
    T = 5.1
    # linke Fassade (y = Y1): Treppenhaus-Glasband, Eingang, Büro im EG, Fenster
    s.fl(Y1, 4.5, 5.6, 2.6, 9.6, GLAS, 'treppenhaus', T)
    for i in range(7):
        z0 = 2.75 + i * 1.0
        a, b, c = iso(4.6, Y1, z0), iso(5.5, Y1, z0 + 0.5), iso(4.6, Y1, z0 + 1.0)
        s.roh(f'<polyline points="{a[0]:.1f},{a[1]:.1f} {b[0]:.1f},{b[1]:.1f} {c[0]:.1f},{c[1]:.1f}" fill="none" stroke="#7FA6D6" stroke-width="1.2"/>', 'treppenhaus', T + .01)
    s.fl(Y1, 4.5, 5.6, 0, 2.25, '#173A63', 'hausmeister', T)
    s.fl(Y1, 4.4, 5.7, 2.25, 2.45, LICHT, 'hausmeister', T + .01)
    s.fl(Y1, 6.1, 8.1, 0.35, 2.05, GLAS, 'buero', T)
    s.fl(Y1, 8.35, 10.15, 0.35, 2.05, GLAS, 'buero', T)
    s.fl(Y1, 6.1, 10.15, 2.12, 2.32, '#0D2B4F', 'buero', T + .01)
    licht_an = {(1, 1), (2, 3), (3, 0), (1, 2)}
    for g in range(1, 4):
        for j, xa in enumerate((6.2, 7.4, 8.6, 9.6)):
            an = (g, j) in licht_an
            s.fl(Y1, xa, xa + 0.7, g * 2.5 + 0.7, g * 2.5 + 1.9, GLAS, 'wohnung', T)
            if an:
                s.fl(Y1, xa, xa + 0.7, g * 2.5 + 0.7, g * 2.5 + 1.9, LICHT, 'wohnung', T + .005, ' class="licht"')
    # rechte Fassade (x = X1)
    s.fr(X1, 1.3, 3.1, 0.35, 2.05, GLAS_R, 'buero', T)
    s.fr(X1, 3.5, 5.9, 0.35, 2.05, GLAS_R, 'buero', T)
    for g in range(1, 4):
        for j, ya in enumerate((1.3, 2.5, 3.7, 4.9)):
            rep = (g, j) == (3, 3)
            an = (g, j) in {(2, 1), (1, 3), (3, 0)}
            zone = 'reparatur' if rep else 'wohnung'
            s.fr(X1, ya, ya + 0.8, g * 2.5 + 0.7, g * 2.5 + 1.9, GLAS_R, zone, T)
            if an or rep:
                s.fr(X1, ya, ya + 0.8, g * 2.5 + 0.7, g * 2.5 + 1.9, LICHT, zone, T + .005, ' class="licht"')
    # Halle rechts
    s.quader(12, 1.0, 0, 15.8, 5.8, 4.4, HALLE, 'gewerbe', tiefe=13.0)
    for i in range(3):
        y0 = 1.5 + i * 1.45
        s.poly([(12.5, y0, 4.41), (15.3, y0, 4.41), (15.3, y0 + 0.6, 4.41), (12.5, y0 + 0.6, 4.41)], '#B9CBE0', 'gewerbe', 13.1)
    s.fl(5.8, 12.7, 15.1, 0, 3.1, '#C2CEDC', 'gewerbe', 13.11)
    for k in range(1, 7):
        a, b = iso(12.7, 5.8, k * 0.44), iso(15.1, 5.8, k * 0.44)
        s.roh(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{LINIE}" stroke-width="1"/>', 'gewerbe', 13.12)
    s.fr(15.8, 1.6, 3.2, 2.4, 3.6, GLAS_R, 'gewerbe', 13.11)
    s.fr(15.8, 3.7, 5.3, 2.4, 3.6, GLAS_R, 'gewerbe', 13.11)
    for (x0, y0, x1, y1, z) in ((12.05, 1.05, 15.75, 5.75, 4.42), (4.3, 1.1, 10.2, 6.1, 10.02)):
        k = [iso(x0, y0, z), iso(x1, y0, z), iso(x1, y1, z), iso(x0, y1, z)]
        s.roh('<polygon class="schnee-kappe" points="' + ' '.join(f'{a:.1f},{b:.1f}' for a, b in k) + '" fill="#FFFFFF"/>',
              'gewerbe' if z < 5 else 'haus', 13.13 if z < 5 else 5.41)
    # Mülltonnen vor der Halle
    for i, deckel in enumerate(('#FFD21E', '#3C82D6', '#8B5E3C', '#5F6B78')):
        x0 = 11.5 + i * 0.85
        s.quader(x0, 6.6, 0, x0 + 0.66, 7.3, 1.0, ('#6E7F93', '#5B6B7E', '#4C5B6D'), 'hausmeister', tiefe=x0 + 6.6)
        s.poly([(x0 - .04, 6.56, 1.0), (x0 + .7, 6.56, 1.0), (x0 + .7, 7.34, 1.0), (x0 - .04, 7.34, 1.0)], deckel, 'hausmeister', x0 + 6.61)
    # Zaun mit Gartentor vor dem Garten
    zaun = ''
    yz = 9.35
    for i in range(19):
        x = 0.3 + i * 0.19
        if 1.55 < x < 2.65:
            continue
        a, b = iso(x, yz, 0), iso(x, yz, 1.15)
        zaun += f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#C9D4E0" stroke-width="1.6"/>'
    for zr in (0.35, 1.05):
        for xa, xb in ((0.3, 1.5), (2.7, 3.7)):
            a, b = iso(xa, yz, zr), iso(xb, yz, zr)
            zaun += f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#C9D4E0" stroke-width="1.6"/>'
    tor = [iso(1.6, yz, 0), iso(2.6, yz, 0), iso(2.6, yz, 1.3), iso(1.6, yz, 1.3)]
    d = ' '.join(f'{a:.1f},{b:.1f}' for a, b in tor)
    zaun += f'<polygon points="{d}" fill="none" stroke="#FFD21E" stroke-width="2"/>'
    for k in range(1, 5):
        a, b = iso(1.6 + k * 0.2, yz, 0.05), iso(1.6 + k * 0.2, yz, 1.25)
        zaun += f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#FFD21E" stroke-width="1.2" opacity=".8"/>'
    s.roh(zaun, 'metall', 12.0)

    # Zeichnen: nach Tiefe, Zonen als Gruppen in Zeichenreihenfolge
    s.teile.sort(key=lambda t: t[0])
    gruppen, aktuell = [], None
    for tiefe, zone, svg in s.teile:
        if aktuell is None or aktuell[0] != zone:
            aktuell = [zone, []]; gruppen.append(aktuell)
        aktuell[1].append(svg)
    minx, maxx, miny, maxy = min(s.xs) - 24, max(s.xs) + 24, min(s.ys) - 34, max(s.ys) + 16
    w, h = maxx - minx, maxy - miny
    reihenfolge = {}
    inhalt = ''
    for zone, teile in gruppen:
        n = reihenfolge.setdefault(zone, len(reihenfolge))
        inhalt += f'<g class="zone" data-zone="{zone}" style="--n:{n}">' + ''.join(teile) + '</g>'
    svg = (f'<svg class="modell__svg" viewBox="{minx:.0f} {miny:.0f} {w:.0f} {h:.0f}" role="img" '
           f'aria-label="Modell eines Objekts mit Keller, Treppenhaus, Büro, Wohnungen, Halle, Garten, Gehweg und Gartentor" '
           f'focusable="false"><g class="welt">{inhalt}</g><g class="spot"></g></svg>')

    def pct(x, y, z):
        a, b = iso(x, y, z)
        return round((a - minx) / w * 100, 2), round((b - miny) / h * 100, 2)

    punkte = [
        ('keller', 'Entrümpelung', 'Keller, Dachboden, Wohnung', pct(7.3, 11, -1.15)),
        ('treppenhaus', 'Treppenhausreinigung', 'fester Wochentag, Aushang mit Datum', pct(5.05, 6.4, 7.0)),
        ('buero', 'Büro- und Praxisreinigung', 'vor Arbeitsbeginn oder nach Feierabend', pct(9.3, 6.4, 1.2)),
        ('wohnung', 'Wohnungsübergabe', 'Fotoprotokoll, Zähler, Schlüssel', pct(10.5, 2.9, 6.3)),
        ('reparatur', 'Kleinreparaturen', 'Lampe, Silikon, Montage in einem Termin', pct(10.5, 5.3, 8.8)),
        ('gewerbe', 'Gebäudereinigung', 'Hallen, Keller, Tiefgarage, Glas', pct(15.8, 3.45, 3.0)),
        ('hausmeister', 'Hausmeisterservice', 'Kontrollgang, Mülltonnen, Schlüssel', pct(12.8, 7.3, 1.25)),
        ('winter', 'Winterdienst', 'Gehweg, Zufahrt, Parkplatz', pct(13.4, 10.3, 0.2)),
        ('metall', 'Metallarbeiten und Schlösser', 'Tore, Zäune, Geländer, Zylinder', pct(2.1, 9.35, 1.35)),
        ('garten', 'Gartenpflege', 'Rasen, Hecken, Beete, Laub', pct(0.65, 5.4, 1.5)),
    ]
    return {'svg': svg, 'punkte': punkte, 'verhaeltnis': w / h}


if __name__ == '__main__':
    d = bauen()
    print(len(d['svg']) // 1024, 'KB', round(d['verhaeltnis'], 3))
    for p in d['punkte']:
        print(p)
