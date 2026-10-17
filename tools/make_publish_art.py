from PIL import Image, ImageDraw, ImageFont, ImageFilter
import qrcode, qrcode.image.svg, cv2, numpy as np
Z='/workspace/zyrosfera/'; O='/workspace/s60_deploy/usersite/aspheris/'
F='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
orb=Image.open(Z+'icons/icon-1024.png').convert('RGBA')
g1=Image.open(Z+'shots/local_game.png').convert('RGB'); g2=Image.open(Z+'shots/local_zone2.png').convert('RGB')
def crop(im,w,h,cy=.45):
    s=max(w/im.width,h/im.height); im=im.resize((int(im.width*s),int(im.height*s)),Image.LANCZOS)
    x=(im.width-w)//2; y=int(im.height*cy-h/2); y=max(0,min(y,im.height-h)); return im.crop((x,y,x+w,y+h))
def base(W,H):
    bg=Image.new('RGB',(W,H),'#12002a')
    # gradient
    a=np.zeros((H,W,3),np.uint8); yy,xx=np.mgrid[0:H,0:W]; d=np.sqrt(((xx-W*.3)/W)**2+((yy-H*.5)/H)**2)
    for i,c in enumerate((255,79,216)): a[...,i]=np.clip(c*(1-d*1.6)*.55+np.array([18,0,42])[i],0,255)
    return Image.fromarray(a)
def panel(W,H,title=None,tag=None):
    im=base(W,H); pw=int(W*.24)
    im.paste(crop(g1,pw,H-int(H*.12)),(W-2*pw-int(W*.04),int(H*.06)))
    im.paste(crop(g2,pw,H-int(H*.12)),(W-pw-int(W*.02),int(H*.06)))
    os_=int(H*.62) if title else int(H*.8); o=orb.resize((os_,os_),Image.LANCZOS)
    glow=Image.new('RGBA',im.size,(0,0,0,0)); ImageDraw.Draw(glow).ellipse((int(W*.24)-os_//1.4,int(H*(.42 if title else .5))-os_//1.4,int(W*.24)+os_//1.4,int(H*(.42 if title else .5))+os_//1.4),fill=(120,200,255,110))
    im=Image.alpha_composite(im.convert('RGBA'),glow.filter(ImageFilter.GaussianBlur(40)))
    # mask orb as circle
    m=Image.new('L',(os_,os_),0); ImageDraw.Draw(m).ellipse((os_*.04,os_*.04,os_*.96,os_*.96),fill=255)
    im.paste(o,(int(W*.24)-os_//2,int(H*(.42 if title else .5))-os_//2),m)
    if title:
        d=ImageDraw.Draw(im); f1=ImageFont.truetype(F,64); f2=ImageFont.truetype(F,26)
        d.text((int(W*.24),int(H*.8)),title,font=f1,fill='#ffffff',anchor='mm',stroke_width=3,stroke_fill='#7b2cff')
        d.text((int(W*.24),int(H*.91)),tag,font=f2,fill='#ffe6ff',anchor='mm')
    return im.convert('RGB')
for l,t in [('no','Vipp kula gjennom kosmos'),('pl','Przechylaj kulę przez kosmos'),('en','Tilt the orb through space')]:
    panel(1200,630,'Aspheris',t).save(O+f'og-{l}.jpg',quality=86)
panel(800,420).save(O+'card.jpg',quality=84)
# QR
URL='https://stop60.no/aspheris/?utm_source=qr'
q=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=20,border=4); q.add_data(URL); q.make(fit=True)
qi=q.make_image(fill_color='#12002a',back_color='white').convert('RGB')
n=qi.width; ls=int(n*.22); lo=orb.resize((ls,ls),Image.LANCZOS)
d=ImageDraw.Draw(qi); c=n//2; r=int(ls*.6); d.ellipse((c-r,c-r,c+r,c+r),fill='white')
m=Image.new('L',(ls,ls),0); ImageDraw.Draw(m).ellipse((0,0,ls,ls),fill=255); qi.paste(lo,(c-ls//2,c-ls//2),m)
qi.save(Z+'shots/aspheris_qr.png'); qi.resize((480,480),Image.LANCZOS).save(O+'qr.png',optimize=True)
q.make_image(image_factory=qrcode.image.svg.SvgPathImage).save(Z+'shots/aspheris_qr.svg')
for p in [Z+'shots/aspheris_qr.png',O+'qr.png']:
    print(p, cv2.QRCodeDetector().detectAndDecode(cv2.imread(p))[0])
