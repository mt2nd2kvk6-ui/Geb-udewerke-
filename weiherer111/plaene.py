# Erzeugt Grundrisse und Schnitte als SVG aus bestand.json und umbau.json. Aufruf: python3 plaene.py
import json, math, os
os.makedirs('plaene', exist_ok=True)
S=45  # Pixel je Meter (Massstab am Bildschirm, Druck ca. 1:100 bei 45 px = 1 m nicht massgeblich)
WAND={'putz','wdvs','fas','sock','sockD','beton','zink'}
COLF={'glas':'#bfe0ee','rahmen':'#383c42','tuer':'#ffffff','tuerA':'#ffffff','san':'#ffffff','fliW':'#d8d8d4','verz':'#9aa1a6','gitter':'#c9ced2','gitterV':'#c9ced2','stahl':'#555','holz':'#b08a63','dachN':'#4a4e54','dachA':'#8a4232','blech':'#5a5e64','pv':'#24324a','wei':'#ffffff','luft':'#ffffff','wp':'#e3e5e8','terr':'#dad7cf','kies':'#cfcac0','fli':'#e9e9e5','vinyl':'#ead9bf','park':'#e3cfae','fliS':'#cfd3d4','anschl':'#f3c79c','dunk':'#777'}
UNTEN={'vinyl','park','fli','fliS','san','gitter','terr','kies','anschl','beton','fliW','wp','verz','wei'}
def fz(v): return f"{v:+.2f}".replace('.',',') if abs(v)>0.004 else '±0,00'
def fm(v): return f"{v:.2f}".replace('.',',')
def srange(pts,c):   # Bereich der ersten Koordinate eines konvexen Polygons (s,z) auf Hoehe z=c
    ss=[]
    for k in range(len(pts)):
        (a,za),(b,zb)=pts[k],pts[(k+1)%len(pts)]
        if (za-c)*(zb-c)<=0 and za!=zb: ss.append(a+(b-a)*(c-za)/(zb-za))
    return (min(ss),max(ss)) if ss else None
def zrange(pts,c):
    zs=[]
    for k in range(len(pts)):
        (a,za),(b,zb)=pts[k],pts[(k+1)%len(pts)]
        if (a-c)*(b-c)<=0 and a!=b: zs.append(za+(zb-za)*(c-a)/(b-a))
    return (min(zs),max(zs)) if zs else None
class SVG:
    def __init__(s,x0,x1,y0,y1,titel):
        s.x0,s.y0=x0,y0; s.W=(x1-x0)*S+170; s.H=(y1-y0)*S+190; s.o=[]; s.t=titel
    def X(s,x): return 110+(x-s.x0)*S
    def Y(s,y): return 110+(y-s.y0)*S
    def rect(s,x0,x1,y0,y1,fill,stroke='none',sw=0.6,dash=None,op=1):
        d=f' stroke-dasharray="{dash}"' if dash else ''
        s.o.append(f'<rect x="{s.X(x0):.1f}" y="{s.Y(y0):.1f}" width="{(x1-x0)*S:.1f}" height="{(y1-y0)*S:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d} opacity="{op}"/>')
    def poly(s,pts,fill,stroke='none',sw=0.6):
        s.o.append('<polygon points="'+' '.join(f'{s.X(a):.1f},{s.Y(b):.1f}' for a,b in pts)+f'" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
    def line(s,a,b,c,d,col='#222',sw=0.8,dash=None):
        dd=f' stroke-dasharray="{dash}"' if dash else ''
        s.o.append(f'<line x1="{s.X(a):.1f}" y1="{s.Y(b):.1f}" x2="{s.X(c):.1f}" y2="{s.Y(d):.1f}" stroke="{col}" stroke-width="{sw}"{dd}/>')
    def text(s,x,y,t,size=11,anchor='middle',col='#16181b',w='400',rot=0):
        r=f' transform="rotate({rot} {s.X(x):.1f} {s.Y(y):.1f})"' if rot else ''
        s.o.append(f'<text x="{s.X(x):.1f}" y="{s.Y(y):.1f}" font-size="{size}" text-anchor="{anchor}" fill="{col}" font-weight="{w}"{r}>{t}</text>')
    def kette(s,werte,lage,pos):   # Masskette: lage 'h' (x-Werte, y=pos) oder 'v' (y-Werte, x=pos)
        w=sorted(werte)
        for a,b in zip(w,w[1:]):
            if lage=='h': s.line(a,pos,b,pos,'#333',0.7); s.text((a+b)/2,pos-0.12,fm(b-a),10)
            else: s.line(pos,a,pos,b,'#333',0.7); s.text(pos-0.12,(a+b)/2,fm(b-a),10,rot=-90)
        for v in w:
            if lage=='h': s.line(v-0.08,pos+0.08,v+0.08,pos-0.08,'#333',1.2); s.line(v,pos-0.15,v,pos+0.25,'#999',0.5)
            else: s.line(pos-0.08,v+0.08,pos+0.08,v-0.08,'#333',1.2); s.line(pos-0.15,v,pos+0.25,v,'#999',0.5)
    def save(s,fn,unter):
        k=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{s.W:.0f}" height="{s.H:.0f}" viewBox="0 0 {s.W:.0f} {s.H:.0f}" font-family="Archivo, Arial, sans-serif">',
           f'<rect width="100%" height="100%" fill="#fff"/><text x="20" y="34" font-size="20" font-weight="700">{s.t}</text>',
           f'<text x="20" y="56" font-size="12" fill="#555">{unter}</text>']
        k.append(f'<g transform="translate({s.W-70},50)"><polygon points="0,-22 8,6 0,0 -8,6" fill="#16181b"/><text y="22" font-size="12" text-anchor="middle">N</text></g>')
        x=20; y=s.H-26; k.append(f'<rect x="{x}" y="{y}" width="{5*S}" height="6" fill="#16181b"/><text x="{x+5*S+8}" y="{y+7}" font-size="11">5 m</text>')
        open('plaene/'+fn,'w',encoding='utf-8').write('\n'.join(k+s.o+['</svg>']))
def grundriss(D,fn,titel,cut,layers,flo,fhi,ext,ketten,extra=None,unter=''):
    g=SVG(*ext,titel)
    for x0,x1,y0,y1,z0,z1,m,l in D['b']:   # Ansicht unterhalb der Schnittebene
        if l in layers and m in UNTEN and fhi-2.6<z1<cut and z0<cut:
            g.rect(x0,x1,y0,y1,COLF.get(m,'#eee'),'#8a8f94',0.5)
    for ax,a0,a1,pts,m,l in D['p']:
        if l not in layers or ax=='z': continue
        r=srange(pts,cut)
        if r and m!='gitterV': (g.rect(a0,a1,r[0],r[1],'#3b3f45' if m in WAND else COLF.get(m,'#888')) if ax=='x' else g.rect(r[0],r[1],a0,a1,'#3b3f45' if m in WAND else COLF.get(m,'#888')))
    for x0,x1,y0,y1,z0,z1,m,l in D['b']:   # geschnittene Bauteile
        if l in layers and z0<=cut<=z1 and m not in ('gras','pfl'):
            g.rect(x0,x1,y0,y1,'#3b3f45' if m in WAND else COLF.get(m,'#888'),'#16181b' if m in ('tuer','tuerA','san') else 'none',0.6)
        elif l=='A' and cut<z0<cut+3.2 and m in ('gitter','terr'): g.rect(x0,x1,y0,y1,'none','#555',0.8,'5,4')
    if extra: extra(g)
    seen=set()
    for n,x0,x1,y0,y1,f in sorted(D['r'],key=lambda r:-(r[2]-r[1])*(r[4]-r[3])):
        if not (flo<=f<=fhi): continue
        base=n.rsplit(' ',2)[0] if n.endswith('m²') else n
        if base in seen: continue
        seen.add(base); cx,cy=(x0+x1)/2,(y0+y1)/2
        teile=n.split(' ')
        if n.endswith('m²'): l1=' '.join(teile[:-2]); l2=teile[-2]+' m²'
        else: l1=n; l2=''
        g.text(cx,cy-0.05,l1,10.5,w='600');
        if l2: g.text(cx,cy+0.28,l2,10.5)
        g.text(cx,cy+0.58,'OKFF '+fz(f),9,col='#666')
    for werte,lage,pos in ketten: g.kette(werte,lage,pos)
    g.save(fn,unter)
def schnitt(D,fn,titel,achse,c,ext,koten,unter=''):
    g=SVG(ext[0],ext[1],-ext[3],-ext[2],titel)   # vertikal: y_svg = -z
    def R(h0,h1,z0,z1,m):
        col='#3b3f45' if m in WAND else COLF.get(m,'#9a9a9a')
        if m in ('gras','pfl'): col='#b9c9a5' if m=='gras' else '#c8c5bd'
        g.rect(h0,h1,-z1,-z0,col,'#16181b' if m in ('holz','dachN','blech') else 'none',0.4)
    for x0,x1,y0,y1,z0,z1,m,l in D['b']:
        if achse=='y' and y0<=c<=y1: R(x0,x1,max(z0,-0.4),z1,m)
        if achse=='x' and x0<=c<=x1: R(y0,y1,max(z0,-0.4),z1,m)
    for ax,a0,a1,pts,m,l in D['p']:
        if m=='gitterV' or ax=='z': continue
        if (achse=='y' and ax=='y') or (achse=='x' and ax=='x'):
            if a0<=c<=a1: g.poly([(p[0],-p[1]) for p in pts],'#3b3f45' if m in WAND else COLF.get(m,'#888'),'#16181b' if m in ('holz','dachN','blech') else 'none',0.4)
        else:
            r=zrange(pts,c)
            if r: R(a0,a1,r[0],r[1],m)
    lz=-9
    for z,t in sorted(koten):
        zt=max(z,lz+0.32); lz=zt
        h=ext[1]-0.3; g.line(h-0.25,-z,h+0.6,-z,'#d9531e',0.8); g.poly([(h,-z),(h-0.12,-z-0.18),(h+0.12,-z-0.18)],'#d9531e'); g.text(h+0.65,-zt+0.1,fz(z)+' '+t,10,'start','#d9531e')
    g.save(fn,unter)
B=json.load(open('bestand.json')); U=json.load(open('umbau.json'))
KX_B=[0,5.915,6.155,8.475,11.365,15.085]; KY_B=[0,8.10,12.21,13.865,21.20,28.25]
KX_U=[-0.16,5.915,6.255,8.315,11.365,15.085]; KY_U=[-0.16,8.10,12.21,14.025,21.36,28.25]
T='Weiherer Straße 111, Ubstadt-Weiher'
for D,tag,KX,KY in ((B,'bestand',KX_B,KY_B),(U,'umbau',KX_U,KY_U)):
    st='Bestand (Aufmaß Nagel 24.09.2026)' if tag=='bestand' else 'Umbau 7 Wohnungen (Planungsstudie)'
    grundriss(D,f'{tag}_EG.svg',f'{T}: Erdgeschoss, {st}',4.1,{'EG','A','G'},0.3,3.3,(-4.2,16.2,-4.4,29.0),
              [([KX[0],KX[-1]],'h',-3.9),(KX,'h',-3.3),([KY[0],KY[-1]],'v',-3.9),(KY,'v',-3.3)],unter='Schnittebene +4,10. Höhen ab OKFF Keller ±0,00, Gelände +0,41. Flächen nach WoFlV, Balkon zu 1/4 in der Wohnungssumme.')
    grundriss(D,f'{tag}_OG.svg',f'{T}: Obergeschoss, {st}',6.4,{'OG','A','EG'},4.8,5.6,(-1.6,16.2,-1.6,17.0),
              [([KX[0],KX[-1]],'h',-1.2),(KX[:3]+[15.085],'h',-0.7),([KY[0],KY[3]],'v',-1.2),(KY[:4],'v',-0.7)],unter='Schnittebene +6,40. Gestrichelt: Podeste und Treppen oberhalb der Schnittebene.')
    def hl(g,tag=tag):
        if tag!='umbau': return
        for y in (0.24+0.80/math.tan(math.radians(30)),7.86-0.80/math.tan(math.radians(30))): g.line(9.72 if y<4 else 8.64,y,14.845,y,'#d9531e',0.9,'6,4')
        y=0.24+1.05/math.tan(math.radians(30)); g.line(0.24,y,5.915,y,'#d9531e',0.9,'6,4'); x=y; g.line(x,8.10-x+0.04 if x<3 else 8.1,x,13.625,'#d9531e',0.9,'6,4')
        g.text(12.0,1.45,'h = 2,00 m',9,col='#d9531e'); g.text(3.0,1.85,'h = 2,00 m',9,col='#d9531e')
        g.rect(-0.56,15.085,-0.56,8.66,'none','#777',0.7,'3,3'); g.rect(-0.56,6.555,8.26,14.43,'none','#777',0.7,'3,3')
    grundriss(D,f'{tag}_DG.svg',f'{T}: Dachgeschoss, {st}',8.62,{'DG','A'},7.5,8.1,(-1.6,16.2,-1.6,15.4),
              [([KX[0],KX[-1]],'h',-1.2),([KY[0],KY[3]],'v',-1.2)],extra=hl,unter='Schnittebene +8,62 (Kniestock geschnitten). Orange gestrichelt: Linie lichte Höhe 2,00 m (WoFlV). Grau gestrichelt: Dachrand.')
KOT_U=[(0.41,'Gelände'),(2.25,'EG'),(3.15,'EG W3'),(5.00,'OG Altbau'),(5.40,'OG West'),(7.70,'DG Ost'),(7.95,'DG West, P2'),(11.65,'First')]
KOT_B=[(0.41,'Gelände'),(2.25,'EG'),(5.00,'OG Altbau'),(5.40,'OG West'),(7.60,'Dachboden'),(10.72,'First')]
schnitt(U,'umbau_Schnitt_A-A.svg',f'{T}: Schnitt A-A (y = 6,10 m, Blick nach Norden), Umbau','y',6.1,(-1.2,16.6,-0.6,12.6),KOT_U,'Schnitt durch Anbau West und Altbau. OG West mit lichter Höhe 2,27 m bleibt, DG West auf vorhandener Decke.')
schnitt(B,'bestand_Schnitt_A-A.svg',f'{T}: Schnitt A-A (y = 6,10 m, Blick nach Norden), Bestand','y',6.1,(-1.2,16.6,-0.6,12.6),KOT_B,'Bestand zum Vergleich.')
schnitt(U,'umbau_Schnitt_B-B.svg',f'{T}: Schnitt B-B (x = 7,80 m, Blick nach Westen), Umbau','x',7.8,(-1.8,17.4,-0.6,12.6),KOT_U+[(4.98,'Laubengang')],'Schnitt durch Hauseingang, Laubengang, Podeste P1 und P2, Treppe zum DG und Zwerchhaus.')
print(sorted(os.listdir('plaene')))
