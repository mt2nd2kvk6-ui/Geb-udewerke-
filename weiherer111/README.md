# Weiherer Straße 111: Umbau zu 7 Wohnungen

* `umbau_rundgang.html`: begehbares 3D-Modell (Bestand, Umbau A Außentreppe, Umbau B Innentreppe umschaltbar). Braucht Internet für three.js.
* `variante_innentreppe.md`: Variante B mit innenliegendem Treppenhaus, Vergleich mit A.
* `bestand.html`: korrigierter Bestandsrundgang (Gelände +0,41, Hauseingangstreppe 10 Steigungen).
* `plaene/`: Grundrisse EG, OG, DG (Bestand, Umbau) und Schnitte A-A, B-B als SVG.
* `flaechen_und_mieten.xlsx`, `massnahmen_und_kosten.xlsx`, `modernisierungsplan.md`, `pruefliste.md`.

Neu erzeugen (Python 3 mit openpyxl):

    python3 build.py      # JSON beider Varianten (B wird mit variante_innen.py aus A erzeugt), Flächen, Prüfungen, HTML
    python3 plaene.py     # SVG-Pläne
    python3 tabellen.py   # Excel (Formeln; zum Speichern der Werte einmal in Excel oder LibreOffice öffnen)

Quellen der Geometrie: `bestand_geometrie.py`, `umbau_geometrie.py`, Generator `generator.py`, Prüfskript `pruefung.py`.
