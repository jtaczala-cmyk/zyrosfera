# Procedural app icon for Aetheris: the radiant guardian deity of the station
# cradling the Heart of Balance (glass energy sphere). Output: icons/icon-1024.png
import numpy as np, math
from PIL import Image, ImageDraw, ImageFilter
N=1024; S=2  # supersample masks
rng=np.random.default_rng(11)
yy,xx=np.mgrid[0:N,0:N].astype(np.float32)
def rad(cx,cy): return np.sqrt((xx-cx)**2+(yy-cy)**2)
def C(*c): return np.array(c,np.float32)/255
def blur(a,r):
    im=Image.fromarray(np.clip(a*255,0,255).astype(np.uint8)) if a.dtype!=np.uint8 else Image.fromarray(a)
    return np.asarray(im.filter(ImageFilter.GaussianBlur(r)),np.float32)/255
def blurf(a,r):  # float blur keeping HDR via scaling
    m=max(a.max(),1e-6); return blur(a/m,r)*m
def mask(draw_fn):
    im=Image.new('L',(N*S,N*S),0); draw_fn(ImageDraw.Draw(im),S)
    return np.asarray(im.resize((N,N),Image.LANCZOS),np.float32)/255
def noise(scale,seed):
    g=np.random.default_rng(seed).random((N//scale+3,N//scale+3)).astype(np.float32)
    im=Image.fromarray((g*255).astype(np.uint8)).resize((N+3*scale,N+3*scale),Image.BICUBIC).crop((scale,scale,N+scale,N+scale))
    return np.asarray(im,np.float32)/255
def fbm(seed,base=128,oct=5):
    t=0;a=1;s=0
    for o in range(oct): t+=a*noise(max(base>>o,4),seed+o); s+=a; a*=0.55
    return t/s
def catmull(pts,n=24):
    out=[];P=[pts[0]]+pts+[pts[-1]]
    for i in range(1,len(P)-2):
        p0,p1,p2,p3=map(np.array,P[i-1:i+3])
        for t in np.linspace(0,1,n,endpoint=False):
            out.append(0.5*((2*p1)+(-p0+p2)*t+(2*p0-5*p1+4*p2-p3)*t*t+(-p0+3*p1-3*p2+p3)*t**3))
    out.append(np.array(pts[-1])); return [tuple(p) for p in out]
def taper(pts,w0,w1):
    pts=np.array(pts); L=[];R=[]
    for i,p in enumerate(pts):
        d=pts[min(i+1,len(pts)-1)]-pts[max(i-1,0)]; d=d/ (np.linalg.norm(d)+1e-6); nrm=np.array([-d[1],d[0]])
        w=w0+(w1-w0)*i/(len(pts)-1); L.append(tuple(p+nrm*w)); R.append(tuple(p-nrm*w))
    return L+R[::-1]
def sc(pts,s): return [(x*s,y*s) for x,y in pts]

img=np.zeros((N,N,3),np.float32)
# ---------- background: deep cosmos ----------
r=rad(512,430)/N
img+=C(10,3,32)[None,None]*np.ones((N,N,1))
img+=np.exp(-(r/0.55)**2)[...,None]*C(80,18,150)
neb=fbm(3,256,6)
img+=(np.clip((neb-0.48)*3,0,1)*np.exp(-(rad(150,250)/420)**2))[...,None]*C(255,40,170)*0.6
img+=(np.clip((fbm(9,256,6)-0.47)*3,0,1)*np.exp(-(rad(900,620)/420)**2))[...,None]*C(30,200,255)*0.55
stars=np.zeros((N,N),np.float32)
for _ in range(320):
    x,y=rng.integers(0,N,2); stars[y,x]=rng.random()**2.5*6
img+=blurf(stars,1.2)[...,None]*C(255,245,255)
HX,HY=512,318
# ---------- god rays ----------
ang=np.arctan2(yy-HY,xx-HX); rr=rad(HX,HY)
rays=(0.5+0.5*np.cos(ang*18))**8+0.6*(0.5+0.5*np.cos(ang*31+1))**14
img+=(rays*np.exp(-(rr/430)**2)*np.clip((rr-150)/80,0,1))[...,None]*C(255,180,90)*0.38
img+=np.exp(-(rr/300)**2)[...,None]*C(255,140,60)*0.3
# ---------- halo: crisp ring + dial ring ----------
ring=lambda R,w: np.exp(-((rr-R)/w)**2)
img+=ring(188,5)[...,None]*C(255,236,190)*2.2+ring(188,22)[...,None]*C(255,160,50)*0.9
dial=ring(232,2.2)*0.9+ring(232,2.2)*0
ticks=((0.5+0.5*np.cos(ang*48))**40)*np.exp(-((rr-232)/9)**2)
img+=(dial+ticks*1.2)[...,None]*C(255,200,140)*0.9
# ---------- veil / hair filaments ----------
fil=np.zeros((N,N),np.float32)
for side in (-1,1):
  for k in range(34):
    t0=rng.uniform(0,1); spread=rng.uniform(0.2,1.0)
    pts=[]
    for j,t in enumerate(np.linspace(0,1,9)):
        x=HX+side*(40+t*(230+spread*230))+side*28*math.sin(t*4+k)*t
        y=HY-40+t*(520+spread*240)-150*spread*math.sin(t*math.pi)*0.6
        pts.append((x,y))
    cur=catmull(pts,10)
    m=mask(lambda d,s,cur=cur: d.line(sc(cur,s),fill=255,width=int(s*rng.choice([2,3,4]))))
    fade=np.clip(1-rad(HX,HY)/(620+spread*200),0,1)**1.3
    fil+=m*fade*rng.uniform(0.4,1.0)
img+=blurf(fil,10)[...,None]*C(180,40,255)*0.9+fil[...,None]*C(255,120,240)*0.85
# ---------- deity body (being of light) ----------
right=[(512,240),(560,256),(588,300),(596,360),(612,420),(660,470),(760,520),(810,600),(830,760),(850,1030)]
outline=catmull(right,20); full=outline+[(1024-x,y) for x,y in outline[::-1]]
B=mask(lambda d,s: d.polygon(sc(full,s),fill=255))
face=mask(lambda d,s: d.ellipse((s*(HX-48),s*(HY-62),s*(HX+48),s*(HY+66)),fill=255))
core=blur(B,46)
vert=np.clip((yy-HY)/680,0,1)
bodycol=(C(100,36,160)*(1-vert)[...,None]+C(22,6,55)*vert[...,None])
emis=bodycol*(0.55+0.5*core[...,None])+np.exp(-(rad(512,640)/260)**2)[...,None]*C(150,80,255)*0.25*B[...,None]
img=img*(1-B[...,None]*0.95)+B[...,None]*emis
rim=np.clip(B-blur(B,7)*1.0,0,1)*0+np.clip(B-np.minimum(B,blur(B,6))*1.0,0,1)
edge=np.clip(B*(1-blur(B,9))*2.2,0,1)
img+=edge[...,None]*C(255,200,110)*2.0*(1-0.5*vert[...,None])
# robe folds (soft vertical light lines)
folds=(0.5+0.5*np.cos((xx-512)/38+np.sin(yy/90)*0.8))**10*np.clip((yy-560)/200,0,1)*B
img+=folds[...,None]*C(255,180,255)*0.25
# face: luminous, featureless veiled face + crown jewel
fg=blur(face,6)
img=img*(1-fg[...,None]*0.9)+fg[...,None]*0.9*(C(255,215,150)*(0.7+0.6*blur(face,30)[...,None]))
img+=np.exp(-(rad(HX,HY-34)/8)**2)[...,None]*C(255,255,255)*2.0+np.exp(-(rad(HX,HY-34)/26)**2)[...,None]*C(60,230,255)*0.9
shade=np.exp(-((yy-(HY+18))/14)**2)*np.exp(-((xx-HX)/40)**2)*face
img*=1-shade[...,None]*0.18
# ---------- arms embracing the sphere ----------
SX,SY,SR=512,676,168
arms=np.zeros((N,N),np.float32)
for s in (-1,1):
    path=catmull([(512+s*120,520),(512+s*225,585),(512+s*262,660),(512+s*238,750),(512+s*150,850),(512+s*55,872)],14)
    def dr(d,sc_,p=path):
        d.polygon(sc(taper(p,36,20),sc_),fill=255); x,y=p[-1]; d.ellipse((sc_*(x-22),sc_*(y-20),sc_*(x+22),sc_*(y+20)),fill=255)
    arms=np.maximum(arms,mask(dr))
arms*=np.clip((yy-560)/150,0,1)**1.5
# ---------- the Heart of Balance (sphere) ----------
sr=rad(SX,SY); rn=np.clip(sr/SR,0,1)
inside=np.clip((SR-sr)/1.5,0,1)
a=np.arctan2(yy-SY,xx-SX)
w=fbm(21,64,4)
sw=0.5+0.5*np.sin(a*2+rn*10+w*6)
sw2=0.5+0.5*np.sin(a*3-rn*7+w*9+2)
fil2=(np.abs(np.sin(a*4+rn*12+w*10))<0.12).astype(np.float32)
orb=C(40,10,120)+sw[...,None]*C(40,210,255)*0.9+(sw2**4)[...,None]*C(255,70,230)*0.9
orb=orb*(0.55+0.8*rn[...,None])+blur(fil2,1.5)[...,None]*C(200,250,255)*0.9
orb+=np.exp(-(rn/0.15)**2)[...,None]*C(255,255,255)*2.4+np.exp(-(rn/0.4)**2)[...,None]*C(60,220,255)*0.7
orb+=(np.clip((rn-0.80)/0.2,0,1)**2)[...,None]*C(190,160,255)*1.4
img=img*(1-inside[...,None])+inside[...,None]*orb
spec=mask(lambda d,s: d.ellipse((s*(SX-112),s*(SY-138),s*(SX-24),s*(SY-96)),fill=255))
img+=blur(spec,10)[...,None]*C(255,255,255)*0.6
img+=(np.exp(-(np.clip(sr-SR,0,None)/38)**2)*(1-inside))[...,None]*C(150,130,255)*1.1
# orbit ring (front half drawn over sphere, back half hidden)
def ell(d,s,w): 
    d.ellipse((s*(SX-275),s*(SY-56),s*(SX+275),s*(SY+56)),outline=255,width=int(w*s))
O=np.asarray(Image.fromarray((mask(lambda d,s: ell(d,s,5))*255).astype(np.uint8)).rotate(-12,center=(SX,SY),resample=Image.BICUBIC),np.float32)/255
cosr,sinr=math.cos(math.radians(12)),math.sin(math.radians(12))
front=((yy-SY)*cosr-(xx-SX)*sinr>0)|(inside<0.5)
O=O*front
img+=O[...,None]*C(255,230,170)*1.8+blurf(O,10)[...,None]*C(255,150,60)*1.0
# arms over sphere edges / hands
armcol=C(70,24,125)*(0.75+0.3*blur(arms,10)[...,None])
img=img*(1-arms[...,None]*0.92)+arms[...,None]*0.92*armcol
img+=np.clip(arms*(1-blur(arms,5))*2.2,0,1)[...,None]*C(255,205,120)*1.8
# rising light motes
mot=np.zeros((N,N),np.float32)
for _ in range(90):
    x=rng.normal(512,190); y=rng.uniform(520,1000); 
    if 0<x<N: mot[int(y),int(x)]=rng.random()*10
img+=blurf(mot,2.5)[...,None]*C(255,210,140)
# ---------- bloom + tonemap ----------
lum=img.max(2); br=np.clip(lum-0.75,0,None)[...,None]*img/np.maximum(lum[...,None],1e-4)
bl=np.stack([blurf(br[...,i],18) for i in range(3)],2)+np.stack([blurf(br[...,i],55) for i in range(3)],2)
img+=bl*0.6
img*=np.clip(1.08-((rad(512,500)/N)**2)*1.5,0.35,1)[...,None]
img=np.clip(img-0.03,0,None); img=1-np.exp(-img*1.2)
l=img.mean(2,keepdims=True); img=np.clip(l+(img-l)*1.5,0,1)
Image.fromarray((img**0.92*255).astype(np.uint8)).save('/workspace/zyrosfera/icons/icon-1024.png')
