import json
BX=[];PR=[];L=['G']
def r3(v): return round(v,3)
def B(E,x0,x1,y0,y1,z0,z1,m,nm='b'):
    if x1-x0<0.004 or y1-y0<0.004 or z1-z0<0.004: return
    BX.append([r3(x0),r3(x1),r3(y0),r3(y1),r3(z0),r3(z1),m,L[0]])
def PX(E,x0,x1,pts,m): PR.append(['x',r3(x0),r3(x1),[[r3(a),r3(b)] for a,b in pts],m,L[0]])
def PY(E,y0,y1,pts,m): PR.append(['y',r3(y0),r3(y1),[[r3(a),r3(b)] for a,b in pts],m,L[0]])
def WL(E,x0,x1,y0,y1,z0,z1,ops=(),m='putz'):
    ax=(x1-x0)>=(y1-y0)
    s,e=(x0,x1) if ax else (y0,y1)
    def sg(a,b,za,zb):
        if ax: B(E,a,b,y0,y1,za,zb,m)
        else: B(E,x0,x1,a,b,za,zb,m)
    c=s
    for a,b,zb,zt,k in sorted(ops):
        sg(c,a,z0,z1); sg(a,b,z0,zb); sg(a,b,zt,z1)
        if k=='w':
            if ax: B(E,a,b,(y0+y1)/2-0.012,(y0+y1)/2+0.012,zb,zt,'glas')
            else: B(E,(x0+x1)/2-0.012,(x0+x1)/2+0.012,a,b,zb,zt,'glas')
        c=b
    sg(c,e,z0,z1)
def FL(E,x0,x1,y0,y1,f,m): B(E,x0,x1,y0,y1,f-0.02,f,m)
def BED(E,x0,x1,y0,y1,f,h):
    B(E,x0,x1,y0,y1,f,f+0.28,'holz'); B(E,x0+0.03,x1-0.03,y0+0.03,y1-0.03,f+0.28,f+0.5,'bett')
    hb={'N':(x0,x1,y0,y0+0.06),'S':(x0,x1,y1-0.06,y1),'W':(x0,x0+0.06,y0,y1),'E':(x1-0.06,x1,y0,y1)}[h]
    B(E,*hb,f+0.5,f+1.0,'holz')
def SOFA(E,x0,x1,y0,y1,f,bk):
    B(E,x0,x1,y0,y1,f,f+0.44,'stoff')
    hb={'N':(x0,x1,y0,y0+0.22),'S':(x0,x1,y1-0.22,y1),'W':(x0,x0+0.22,y0,y1),'E':(x1-0.22,x1,y0,y1)}[bk]
    B(E,*hb,f+0.44,f+0.85,'stoff')
def TAB(E,x0,x1,y0,y1,f):
    B(E,x0,x1,y0,y1,f+0.72,f+0.76,'holz')
    for xa in (x0+0.05,x1-0.1):
        for ya in (y0+0.05,y1-0.1): B(E,xa,xa+0.05,ya,ya+0.05,f,f+0.72,'dunk')
def KU(E,x0,x1,y0,y1,f,w,up=True):
    B(E,x0,x1,y0,y1,f,f+0.88,'wei'); B(E,x0,x1,y0,y1,f+0.88,f+0.92,'dunk')
    if up:
        r={'N':(x0,x1,y0,y0+0.35),'S':(x0,x1,y1-0.35,y1),'W':(x0,x0+0.35,y0,y1),'E':(x1-0.35,x1,y0,y1)}[w]
        B(E,*r,f+1.45,f+2.15,'wei')
def SCH(E,x0,x1,y0,y1,f): B(E,x0,x1,y0,y1,f,f+2.1,'wei')
def DU(E,x0,x1,y0,y1,f): B(E,x0,x1,y0,y1,f,f+0.04,'san')
def WC(E,x0,x1,y0,y1,f): B(E,x0,x1,y0,y1,f,f+0.42,'san')
def WT(E,x0,x1,y0,y1,f): B(E,x0,x1,y0,y1,f+0.8,f+0.88,'san')
def RL(E,x0,y0,x1,y1,z):
    if abs(y1-y0)<1e-6:
        a,b=min(x0,x1),max(x0,x1)
        B(E,a,b,y0-0.03,y0+0.03,z+0.95,z+1.0,'stahl'); B(E,a,b,y0-0.01,y0+0.01,z+0.1,z+0.92,'glas')
        n=max(1,int((b-a)/1.2)+1)
        for i in range(n+1):
            x=min(max(a+(b-a)*i/n,a+0.025),b-0.025); B(E,x-0.025,x+0.025,y0-0.025,y0+0.025,z,z+0.95,'stahl')
    else:
        a,b=min(y0,y1),max(y0,y1)
        B(E,x0-0.03,x0+0.03,a,b,z+0.95,z+1.0,'stahl'); B(E,x0-0.01,x0+0.01,a,b,z+0.1,z+0.92,'glas')
        n=max(1,int((b-a)/1.2)+1)
        for i in range(n+1):
            y=min(max(a+(b-a)*i/n,a+0.025),b-0.025); B(E,x0-0.025,x0+0.025,y-0.025,y+0.025,z,z+0.95,'stahl')
def STY(E,x0,x1,yb,dr,z0,z1,n,g):
    r=(z1-z0)/n
    for i in range(n-1):
        ya=yb+dr*i*g; yc=yb+dr*(i+1)*g; zt=z0+(i+1)*r
        B(E,x0,x1,min(ya,yc),max(ya,yc),zt-0.05,zt,'stahl')
    yt=yb+dr*(n-1)*g
    for xa,xb in ((x0-0.06,x0),(x1,x1+0.06)):
        PX(E,xa,xb,[(yb,z0-0.05),(yt,z1-0.05),(yt,z1+0.15),(yb,z0+0.15)],'stahl')
        PX(E,xa,xb,[(yb,z0+0.95),(yt,z1+0.95),(yt,z1+1.0),(yb,z0+1.0)],'stahl')
        for y in (yb,yt): B(E,xa,xb,min(y,y+dr*0.05),max(y,y+dr*0.05),z0 if y==yb else z1,(z0 if y==yb else z1)+1.0,'stahl')
def STX(E,y0,y1,xb,dr,z0,z1,n,g):
    r=(z1-z0)/n
    for i in range(n-1):
        xa=xb+dr*i*g; xc=xb+dr*(i+1)*g; zt=z0+(i+1)*r
        B(E,min(xa,xc),max(xa,xc),y0,y1,zt-0.05,zt,'stahl')
    xt=xb+dr*(n-1)*g
    for ya,yc in ((y0-0.06,y0),(y1,y1+0.06)):
        PY(E,ya,yc,[(xb,z0-0.05),(xt,z1-0.05),(xt,z1+0.15),(xb,z0+0.15)],'stahl')
        PY(E,ya,yc,[(xb,z0+0.95),(xt,z1+0.95),(xt,z1+1.0),(xb,z0+1.0)],'stahl')
E=None
import sys
RM=[]
exec(open(sys.argv[1]).read())
json.dump({'b':BX,'p':PR,'r':RM},open(sys.argv[2],'w'),separators=(',',':'))
print(len(BX),len(PR))
