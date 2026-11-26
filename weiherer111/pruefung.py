# Flaechen nach WoFlV und Pruefungen fuer das Umbaumodell. Aufruf: python3 pruefung.py
# Erzeugt flaechen.json (fuer Tabellen) und schreibt Raumnamen mit Flaeche in umbau.json.
import json, math, collections, sys
SRC=sys.argv[1] if len(sys.argv)>1 else 'umbau.json'; OUTF=sys.argv[2] if len(sys.argv)>2 else 'flaechen.json'; INNEN='innen' in SRC
T=math.tan(math.radians(30)); DK=0.55
zN=lambda y:8.90+(y-0.24)*T; zS=lambda y:8.90+(7.86-y)*T; zW=lambda x:8.90+(x-0.24)*T
SS=(10.538-10.25)/(5.915-3.0775); zSch=lambda x:10.538-(x-3.0775)*SS
zZ=lambda y:10.35+(7.86-y)*0.1763; zG=lambda y:10.00+(y-0.24)*0.1763
wg=lambda x: zW(x) if x<=3.0775 else zSch(x)
def decke_dg(x,y):
    if x<5.915:   # W6
        return max(zS(y),wg(x)) if y>=5.02 else min(zN(y),zS(y))
    if 6.155<=x<=8.40 and y>=4.245: return zZ(y)
    if 6.70<=x<=9.20 and y<=2.98: return zG(y)
    return min(zN(y),zS(y))
# Aufmasswerte unveraenderter Raeume (Aufmass Nagel 24.09.2026)
AUFMASS={'W1 Bad':6.04,'W1 Küche':5.51,'W1 Abstellraum':3.14,'W2 Wohnen':16.35,'W2 Schlafen':14.60,'W2 Küche':12.01,
 'W2 Ankleide':9.77,'W2 Bad':3.37,'W3 Zugang':4.43,'W3 Küche':6.68,'W3 Wohnen/Essen':28.25,'W3 Schlafen':16.08,'W3 Bad':6.40,
 'W3 Balkon':23.28,'W4 Schlafen':14.01,'W4 Bad':5.07,'W4 Zimmer':12.71,'W4 Flur':8.79,'W5 Wohnen':16.35,'W5 Schlafen':14.60,'W5 Küche/Essen':12.02}
ABZUG={'W6 Zimmer':0.41*0.43}   # Schacht ehem. Kamin West
def flaeche(name,rects):
    if name in AUFMASS: a=AUFMASS[name]; return (a*0.25 if 'Balkon' in name else a), a, 'Aufmaß'+(' (Balkon 1/4)' if 'Balkon' in name else '')
    tot=0; roh=0; dg=False; ok22=0; ue15=0
    for x0,x1,y0,y1,f in rects:
        roh+=(x1-x0)*(y1-y0)
        if f<7.6: tot+=(x1-x0)*(y1-y0); continue
        dg=True; n=40; dx=(x1-x0)/n; dy=(y1-y0)/n
        for i in range(n):
            for j in range(n):
                h=decke_dg(x0+(i+.5)*dx,y0+(j+.5)*dy)-f; a=dx*dy
                tot+=a if h>=2.0 else (a/2 if h>=1.0 else 0)
                if h>1.5: ue15+=a
                if h>=2.2: ok22+=a
    tot-=ABZUG.get(name,0)
    info='Planmaß'+(', Dachschräge gewichtet (unter 1 m 0, 1 bis 2 m halb)' if dg else '')
    if dg and ue15>0: info+=f', LBO-Anteil h≥2,20 m: {ok22/ue15*100:.0f} %'
    return tot, roh, info
U=json.load(open(SRC))
import re
for r in U['r']: r[0]=re.sub(r' [0-9]+,[0-9]+ m²$','',r[0])
rooms=collections.OrderedDict()
for n,x0,x1,y0,y1,f in U['r']: rooms.setdefault(n,[]).append((x0,x1,y0,y1,f))
F=[]
for n,rs in rooms.items():
    w=n.split(' ')[0]
    if not (len(w)==2 and w[0]=='W' and w[1].isdigit()): continue
    a,roh,info=flaeche(n,rs); F.append({'whg':w,'raum':n[3:],'flaeche':round(a,2),'grund':round(roh,2),'quelle':info})
lab={(e['whg']+' '+e['raum']):e['flaeche'] for e in F}
for r in U['r']:
    if r[0] in lab: r[0]=r[0]+' '+f"{lab[r[0]]:.2f}".replace('.',',')+' m²'
json.dump(U,open(SRC,'w'),separators=(',',':'))
sumw=collections.OrderedDict()
for e in F: sumw[e['whg']]=sumw.get(e['whg'],0)+e['flaeche']
json.dump({'raeume':F,'summen':sumw},open(OUTF,'w'),ensure_ascii=False,indent=1)
print('Wohnflaechen:',{k:round(v,2) for k,v in sumw.items()},'gesamt',round(sum(sumw.values()),2))
for e in F:
    if 'LBO' in e['quelle']: print('  ',e['whg'],e['raum'],e['flaeche'],e['quelle'].split('LBO-')[1])
# ---------------- Hoehenraster aus der Geometrie ----------------
G=0.1; X0,X1,Y0,Y1=-4.0,16.6,-4.2,29.0; NX=int((X1-X0)/G); NY=int((Y1-Y0)/G)
col=collections.defaultdict(list)
def cells(xa,xb,ya,yb):
    i0=max(0,int(math.ceil((xa-X0)/G-0.5))); i1=min(NX-1,int(math.floor((xb-X0)/G-0.5)))
    j0=max(0,int(math.ceil((ya-Y0)/G-0.5))); j1=min(NY-1,int(math.floor((yb-Y0)/G-0.5)))
    for i in range(i0,i1+1):
        for j in range(j0,j1+1): yield i,j
def zr(pts,s):   # z-Bereich eines konvexen Polygons (s,z) an Stelle s
    zs=[]
    for k in range(len(pts)):
        (a,za),(b,zb)=pts[k],pts[(k+1)%len(pts)]
        if (a-s)*(b-s)<=0 and a!=b: zs.append(za+(zb-za)*(s-a)/(b-a))
        elif a==b==s: zs+= [za,zb]
    return (min(zs),max(zs)) if zs else None
for x0,x1,y0,y1,z0,z1,m,l in U['b']:
    if m in ('anschl',): continue
    for c in cells(x0,x1,y0,y1): col[c].append((z0,z1,m))
for ax,a0,a1,pts,m,l in U['p']:
    if ax=='z': continue
    ss=[p[0] for p in pts]; lo,hi=min(ss),max(ss)
    if ax=='x':
        for i,j in cells(a0,a1,lo,hi):
            r=zr(pts,Y0+(j+.5)*G)
            if r: col[(i,j)].append((r[0],r[1],m))
    else:
        for i,j in cells(lo,hi,a0,a1):
            r=zr(pts,X0+(i+.5)*G)
            if r: col[(i,j)].append((r[0],r[1],m))
STAND={}   # (i,j) -> Liste der begehbaren Hoehen mit lichter Hoehe >= 2,00
for c,iv in col.items():
    iv.sort(); mer=[]
    for a,b,m in iv:
        if mer and a<=mer[-1][1]+0.005: mer[-1][1]=max(mer[-1][1],b)
        else: mer.append([a,b])
    tops=[]
    for k,(a,b) in enumerate(mer):
        nxt=mer[k+1][0] if k+1<len(mer) else 99
        if nxt-b>=1.995 and b>0.3: tops.append(round(b,3))
    if tops: STAND[c]=tops
def frei(i,j,z):   # Koerperbreite: Umgebung 0,2 m muss auf aehnlicher Hoehe begehbar sein
    for di in (-2,-1,0,1,2):
        for dj in (-2,-1,0,1,2):
            t=STAND.get((i+di,j+dj))
            if not t or min(abs(q-z) for q in t)>0.25: return False
    return True
def knoten(x,y,z):
    i,j=int((x-X0)/G),int((y-Y0)/G); t=STAND.get((i,j),[])
    if not t: return None
    q=min(t,key=lambda q:abs(q-z)); return (i,j,q) if abs(q-z)<0.3 else None
start=knoten(-1.0,20.0,0.41); seen={start}; dq=collections.deque([start]); maxstep=0
while dq:
    i,j,z=dq.popleft()
    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
        for q in STAND.get((i+di,j+dj),[]):
            if abs(q-z)<=0.205 and (i+di,j+dj,q) not in seen and frei(i+di,j+dj,q):
                seen.add((i+di,j+dj,q)); dq.append((i+di,j+dj,q))
                if abs(q-z)>0.03: maxstep=max(maxstep,abs(q-z))
ZIELE=[('Hof',-1.0,20.0,0.41),('Straße vor W1',5.2,-4.0,0.41),('Hausflur',7.5,9.0,2.25),]+([('Treppenhaus Podest 1',7.0,13.0,3.918),('Treppenhaus OG',7.0,9.0,5.40),('Treppenhaus Podest 2',7.0,13.0,6.675),('Treppenhaus DG',7.0,9.0,7.95)] if INNEN else
 [('Laubengang',12.0,8.9,4.98),('Podest P1',7.0,15.5,5.40),('Podest P2',7.0,8.8,7.95)])
for n,rs in rooms.items():
    if n.startswith('W') and n[1].isdigit() and 'Balkon' not in n and 'Abstell' not in n:
        x0,x1,y0,y1,f=max(rs,key=lambda r:(r[1]-r[0])*(r[3]-r[2])); ZIELE.append((n,(x0+x1)/2,(y0+y1)/2,f))
fehl=[]
for n,x,y,z in ZIELE:
    k=knoten(x,y,z)
    best=None
    if k:   # naechster erreichter Knoten im Raum (Mitte kann unter Schraege liegen)
        for di in range(-12,13):
            for dj in range(-12,13):
                for q in STAND.get((k[0]+di,k[1]+dj),[]):
                    if abs(q-z)<0.3 and (k[0]+di,k[1]+dj,q) in seen: best=1;break
                if best:break
            if best:break
    if not best: fehl.append(n)
print('Laufweg: Ziele',len(ZIELE),'nicht erreichbar:',fehl if fehl else 'keine','| groesste Stufe im Netz:',round(maxstep,3),'m')
# ---------------- Durchdringungen: Bauteile ueber Dachoberkante ----------------
def dachok(x,y):
    if -0.56<=x<6.155 and 5.02<=y<=14.43:
        w=wg(x); m=zS(y) if y<=8.66 else -9
        return w+(DK if x<=3.0775 else 0.30) if w>=m else m+DK
    if 6.155<=x<=(8.89 if INNEN else 6.555) and (8.12 if INNEN else 8.26)<=y<=14.43: return zSch(x)+0.30
    if -0.56<=x<=15.085 and -0.56<=y<=8.66:
        o=decke_dg(min(max(x,0.24),14.845),min(max(y,0.24),7.86))+DK
        if 6.155<=x<=8.88 and y>=4.245: o=zZ(y)+0.30
        if 6.22<=x<=9.68 and y<=2.98: o=zG(y)+0.30
        return o
    if -0.56<=x<=6.555 and 8.26<=y<=14.43: return max(zW(x)+DK if x<=3.0775 else zSch(x)+0.30,0)
    return None
stoss=[]
for x0,x1,y0,y1,z0,z1,m,l in U['b']:
    if l not in ('DG','OG','EG') or z1<7.5: continue
    for x,y in ((x0,y0),(x0,y1),(x1,y0),(x1,y1),((x0+x1)/2,(y0+y1)/2)):
        o=dachok(x,y)
        if o is not None and z1>o+0.02: stoss.append((l,m,round(x,2),round(y,2),z1,round(o,2))); break
print('Bauteile durch die Dachhaut:',len(stoss),stoss[:6])
lo=min(decke_dg(0.24+i*0.05,0.24+j*0.05)-(7.95 if 0.24+i*0.05<5.915 else 7.70) for i in range(292) for j in range(152))
print('kleinste Hoehe Dachunterseite ueber DG-Fussboden innen:',round(lo,2),'m (Kniestock)')
