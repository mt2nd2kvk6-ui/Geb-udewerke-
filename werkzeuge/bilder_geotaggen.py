#!/usr/bin/env python3
"""Schreibt GPS-Koordinaten (Bruchsal) als EXIF in alle WebP-Fotos, ohne neu zu komprimieren.

Aufruf: python3 werkzeuge/bilder_geotaggen.py
Koordinaten: Mittelpunkt des Einsatzgebiets im Google-Unternehmensprofil (Bruchsal).
Mehrfach ausführbar: ein vorhandener EXIF-Block wird ersetzt.
"""
import glob, os, struct
from PIL import Image, ExifTags

BREITE, LAENGE = 49.1291927, 8.5914434
BASIS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'website', 'assets', 'img', 'fotos')

def dms(wert):
    g = int(wert); m_f = (wert - g) * 60; m = int(m_f); s = round((m_f - m) * 60 * 10000)
    return ((g, 1), (m, 1), (s, 10000))

def exif_bytes():
    from PIL import TiffImagePlugin as T
    ex = Image.Exif()
    gps = {1: 'N', 2: tuple(T.IFDRational(*x) for x in dms(BREITE)),
           3: 'E', 4: tuple(T.IFDRational(*x) for x in dms(LAENGE)),
           0: b'\x02\x03\x00\x00', 18: 'WGS-84'}
    ex[ExifTags.IFD.GPSInfo] = gps
    ex[0x010E] = 'Bruchsal, Landkreis Karlsruhe'   # ImageDescription
    b = ex.tobytes()
    return b[6:] if b.startswith(b'Exif\x00\x00') else b

def chunks(daten):
    i = 12
    while i + 8 <= len(daten):
        art, groesse = daten[i:i+4], struct.unpack('<I', daten[i+4:i+8])[0]
        yield art, daten[i+8:i+8+groesse]
        i += 8 + groesse + (groesse & 1)

def chunk(art, inhalt):
    return art + struct.pack('<I', len(inhalt)) + inhalt + (b'\x00' if len(inhalt) & 1 else b'')

def masse(art, d):
    if art == b'VP8 ':
        w, h = struct.unpack('<HH', d[6:10]); return w & 0x3fff, h & 0x3fff, False
    if art == b'VP8L':
        bits = struct.unpack('<I', d[1:5])[0]
        return (bits & 0x3fff) + 1, ((bits >> 14) & 0x3fff) + 1, bool((bits >> 28) & 1)
    raise ValueError(art)

def taggen(pfad, exif):
    daten = open(pfad, 'rb').read()
    assert daten[:4] == b'RIFF' and daten[8:12] == b'WEBP'
    teile = [(a, d) for a, d in chunks(daten) if a != b'EXIF']
    if teile[0][0] == b'VP8X':
        kopf = bytearray(teile[0][1]); kopf[0] |= 0x08
        teile[0] = (b'VP8X', bytes(kopf))
    else:
        w, h, alpha = masse(*teile[0])
        flags = 0x08 | (0x10 if alpha else 0)
        vp8x = bytes([flags, 0, 0, 0]) + (w - 1).to_bytes(3, 'little') + (h - 1).to_bytes(3, 'little')
        teile.insert(0, (b'VP8X', vp8x))
    inhalt = b'WEBP' + b''.join(chunk(a, d) for a, d in teile) + chunk(b'EXIF', exif)
    open(pfad, 'wb').write(b'RIFF' + struct.pack('<I', len(inhalt)) + inhalt)

if __name__ == '__main__':
    ex = exif_bytes(); n = 0
    for p in sorted(glob.glob(os.path.join(BASIS, '*.webp'))):
        taggen(p, ex); n += 1
    print(n, 'Fotos mit GPS Bruchsal versehen')
