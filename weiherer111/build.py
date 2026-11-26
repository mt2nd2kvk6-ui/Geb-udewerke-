# Baut alles: python3 build.py
import json, subprocess, sys
run=lambda *a: subprocess.run([sys.executable,*a],check=True)
run('generator.py','bestand_geometrie.py','bestand.json'); run('generator.py','umbau_geometrie.py','umbau.json'); run('pruefung.py')
B=open('bestand.json').read(); U=open('umbau.json').read()
t=open('vorlage_rundgang.html',encoding='utf-8').read(); open('bestand.html','w',encoding='utf-8').write(t.replace('__DATA__',B))
t=open('umbau_vorlage.html',encoding='utf-8').read(); open('umbau_rundgang.html','w',encoding='utf-8').write(t.replace('__BESTAND__',B).replace('__UMBAU__',U))
print('umbau_rundgang.html', len(t)+len(B)+len(U), 'Bytes')
