#!/usr/bin/env python3
"""Einmalig 07.11.2026: veraltete Preise im Fließtext an die Preistabellen angleichen.
Hintergrund: preise_minus_15.py (02.11.2026) hat Tabellen und JSON-LD gesenkt, einige Sätze aber nicht.
Jeder Altwert entspricht dem heutigen Tabellenwert vor dem Abschlag (netto x 0,85, kaufmännisch gerundet).
Ersetzt nur „Zahl + €“ außerhalb von <table>, protokolliert jede Stelle. Nichts wird neu berechnet."""
import glob, os, re

WEB = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'website')
ALT_NEU = {  # alter Text -> Wert aus der Preistabelle (preise.html)
    '130': '111', '190': '162', '226': '193', '280': '238', '150': '128', '175': '149', '235': '200',
    '449': '382', '705': '599', '1.049': '892', '2.075': '1.764',
    '1.435': '1.220', '1.708': '1.452', '2.100': '1.785', '2.499': '2.124', '90': '77', '107': '92',
}
muster = re.compile(r'(?<![\d.,])(' + '|'.join(re.escape(k) for k in sorted(ALT_NEU, key=len, reverse=True)) + r')((?:&nbsp;| | )?€)')
protokoll = []
for p in sorted(glob.glob(WEB + '/*.html') + glob.glob(WEB + '/ratgeber/*.html') + [WEB + '/llms.txt']):
    s = open(p, encoding='utf-8').read()
    teile = re.split(r'(<table\b.*?</table>|<script\b.*?</script>|<style\b.*?</style>)', s, flags=re.S)
    neu = []
    for i, t in enumerate(teile):
        if i % 2 == 0:
            def ersetzen(m):
                a = max(0, m.start() - 50)
                protokoll.append(f'{os.path.relpath(p, WEB)}: {m.group(1)} € -> {ALT_NEU[m.group(1)]} €  …{re.sub(r"<[^>]+>|&nbsp;", " ", t[a:m.end()+10])}…')
                return ALT_NEU[m.group(1)] + m.group(2)
            t = muster.sub(ersetzen, t)
        neu.append(t)
    n = ''.join(neu)
    if n != s:
        open(p, 'w', encoding='utf-8', newline='\n').write(n)
print('\n'.join(protokoll))
print(len(protokoll), 'Stellen angeglichen')
