import numpy as np
from PIL import Image, ImageFilter
N=1024
def noise(seed,octs=5):
    rng=np.random.default_rng(seed);out=np.zeros((N,N))
    for o in range(octs):
        s=4*2**o;g=rng.random((s+1,s+1))
        img=Image.fromarray((g*255).astype(np.uint8)).resize((N,N),Image.BICUBIC)
        out+=np.asarray(img)/255/(2**o)
    return out/out.max()
def render(ring=False,t=0.0,R=0.36,palette=0,seed=3):
    y,x=np.mgrid[0:N,0:N]/N-0.5
    r=np.hypot(x,y);a=np.arctan2(y,x)
    # background
    bg=np.zeros((N,N,3));bg[...,0]=0.03;bg[...,1]=0.02;bg[...,2]=0.09
    neb=noise(seed+10,6);bg+=np.dstack([0.18*neb**3,0.03*neb**3,0.28*neb**3])*(1-np.clip(r*1.4,0,1))[...,None]
    rng=np.random.default_rng(1);st=np.zeros((N,N))
    for _ in range(220):
        i,j=rng.integers(0,N,2);st[i,j]=rng.random()**2
    st=np.asarray(Image.fromarray((st*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.0)))/255*4
    bg+=st[...,None]
    c1=np.array([0.1,0.95,1.0]);c2=np.array([0.62,0.25,1.0]) if palette==0 else np.array([1.0,0.25,0.85])
    # outer glow
    glow=(np.exp(-np.clip(r-R,0,None)/0.012)*0.9+np.exp(-np.clip(r-R,0,None)/0.06)*0.35)*(r>R)
    mix=(0.5+0.5*np.cos(a-2.3))[...,None]
    gcol=c1*mix+c2*(1-mix)
    img=bg+glow[...,None]*gcol*0.9
    # sphere interior
    inside=r<R
    z=np.sqrt(np.clip(R*R-r*r,0,None))/R
    sw=noise(seed,5)
    # swirl: rotate sampling by radius-dependent angle
    ang=a+3.0*(1-r/R)+t*2*np.pi
    rr=r/R
    u=(np.cos(ang)*rr*0.5+0.5)*(N-1);v=(np.sin(ang)*rr*0.5+0.5)*(N-1)
    swv=sw[v.astype(int).clip(0,N-1),u.astype(int).clip(0,N-1)]
    fil=np.clip(1-np.abs(np.sin(swv*14+ang*2))*1.6,0,1)**2
    m2=(0.5+0.5*np.sin(ang*1+1.0))[...,None]
    col=c1*m2+c2*(1-m2)
    body=np.array([0.02,0.02,0.1])*(0.6+0.4*z[...,None])+col*(0.08+1.8*fil[...,None]**1.5)*(0.5+0.5*z[...,None])
    core=np.exp(-(r/(R*0.3))**2)[...,None]*np.array([0.35,0.85,1.0])*0.9
    fres=((1-z)**3)[...,None]*gcol*2.2
    body=body+core+fres
    # specular
    hx,hy=x+R*0.38,y+R*0.45
    spec=np.exp(-((hx/(R*0.22))**2+(hy/(R*0.10))**2)**2*3)
    rot=np.exp(-(((x*np.cos(.6)+y*np.sin(.6))+R*0.6)/(R*0.3))**2 - ((-x*np.sin(.6)+y*np.cos(.6))/(R*0.12))**2)
    body+=spec[...,None]*2.0
    aa=np.clip((R-r)*N/1.5,0,1)[...,None]
    img=img*(1-aa)+body*aa
    if ring:
        # tilted ellipse ring: in rotated frame
        th=-0.35;xr=x*np.cos(th)-y*np.sin(th);yr=x*np.sin(th)+y*np.cos(th)
        e=np.hypot(xr/(R*1.42),yr/(R*0.42))
        d=np.abs(e-1)*R*0.5
        ringI=np.exp(-(d/0.0035)**2)+0.5*np.exp(-(d/0.014)**2)
        front=(yr>0)|(r>R)
        ringI=ringI*front
        rc=c1*(0.5+0.5*np.cos(np.arctan2(yr,xr)))[...,None]+c2*(0.5-0.5*np.cos(np.arctan2(yr,xr)))[...,None]
        img=img+ringI[...,None]*(rc*0.8+0.4)
    img=1-np.exp(-img*1.25)  # tonemap
    return Image.fromarray((np.clip(img,0,1)**0.9*255).astype(np.uint8))
# Build all game icons from orb_1 (Jacek's choice, 2026-10-17):
#   python3 tools/make_orb_icon.py --icons .   (run from repo root)
def build_icons(root):
    import os
    os.makedirs(f"{root}/icons",exist_ok=True)
    full=render(False,palette=0)              # == orb_1.png
    full.save(f"{root}/icons/icon-1024.png",optimize=True)
    def sz(im,s): return im.resize((s,s),Image.LANCZOS)
    a180=sz(full,180);a180.save(f"{root}/apple-touch-icon.png",optimize=True);a180.save(f"{root}/icons/apple-touch-icon-180.png",optimize=True)
    for s in (192,512): sz(full,s).save(f"{root}/icons/icon-{s}.png",optimize=True)
    # maskable: smaller orb (glow inside the 80% safe circle), same seamless background
    mask=render(False,palette=0,R=0.29)
    for s in (192,512): sz(mask,s).save(f"{root}/icons/icon-maskable-{s}.png",optimize=True)
    # favicon: crop tighter so the orb reads at 16/32 px
    c=int(1024*0.10);tight=full.crop((c,c,1024-c,1024-c))
    sz(tight,32).save(f"{root}/icons/favicon-32.png",optimize=True)
    sz(tight,64).save(f"{root}/favicon.ico",sizes=[(16,16),(32,32),(48,48),(64,64)])

if __name__=="__main__":
    import sys
    if sys.argv[1]=="--icons":
        build_icons(sys.argv[2] if len(sys.argv)>2 else "."); sys.exit()
    o=sys.argv[1]
    render(False,palette=0).save(f"{o}/orb_1.png")
    render(True,palette=1,R=0.31).save(f"{o}/orb_2.png")
    render(False,palette=0,R=0.40).save(f"{o}/orb_3.png")
