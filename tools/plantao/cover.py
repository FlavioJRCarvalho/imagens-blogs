from PIL import Image, ImageDraw, ImageFont, ImageFilter
import textwrap
R='./'  # pasta das imagens (ajustada por set_dir)
FB='/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf'
def F(s): return ImageFont.truetype(FB,s)
W,H=2000,1091
def bg():
    im=Image.new('RGB',(W,H)); d=ImageDraw.Draw(im)
    for y in range(H):
        t=y/H; d.line([(0,y),(W,y)],fill=(int(6+8*t),int(24+22*(1-abs(t-.45)*1.6)),int(48+40*(1-abs(t-.4)))))
    # grade tecnológica leve
    ov=Image.new('RGBA',(W,H),(0,0,0,0)); o=ImageDraw.Draw(ov)
    for x in range(0,W,80): o.line([(x,0),(x,H)],fill=(80,170,255,14))
    for y in range(0,H,80): o.line([(0,y),(W,y)],fill=(80,170,255,14))
    o.ellipse([620,180,1380,900],outline=(80,180,255,30),width=3)
    im.paste(ov,(0,0),ov); return im
def panel(im,b,r=22):
    d=ImageDraw.Draw(im,'RGBA'); d.rounded_rectangle(b,radius=r,fill=(8,22,44,215),outline=(70,170,255,255),width=3)
def thumb(im,path,b):
    t=Image.open(R+path).convert('RGB'); x0,y0,x1,y1=b; w,h=x1-x0,y1-y0
    s=max(w/t.width,h/t.height); t=t.resize((int(t.width*s)+1,int(t.height*s)+1),Image.LANCZOS)
    cx,cy=(t.width-w)//2,(t.height-h)//2; t=t.crop((cx,cy,cx+w,cy+h)); im.paste(t,(x0,y0))
    ImageDraw.Draw(im).rectangle(b,outline=(90,185,255),width=3)
def txt(im,xy,t,size,fill=(255,255,255),width=30,maxlines=3,lh=1.12):
    d=ImageDraw.Draw(im); f=F(size); y=xy[1]
    lines=textwrap.wrap(t.upper(),width=width)[:maxlines]
    for l in lines:
        d.text((xy[0]+2,y+2),l,font=f,fill=(0,0,0)); d.text((xy[0],y),l,font=f,fill=fill); y+=int(size*lh)
    return y
def fit(im,box,t,size,fill=(255,255,255),minsize=20,lh=1.12):
    x0,y0,x1,y1=box; d=ImageDraw.Draw(im); t=t.upper()
    while True:
        f=F(size); lines=[]; cur=''
        for w in t.split():
            c=(cur+' '+w).strip()
            if d.textlength(c,font=f)<=x1-x0: cur=c
            else: lines.append(cur); cur=w
        lines.append(cur)
        if len(lines)*size*lh<=y1-y0 or size<=minsize: break
        size-=2
    y=y0
    for l in lines:
        d.text((x0+2,y+2),l,font=f,fill=(0,0,0)); d.text((x0,y),l,font=f,fill=fill); y+=int(size*lh)
    return y
def make(out,ed,hero,sides,lasts,leia):
    im=bg(); d=ImageDraw.Draw(im,'RGBA')
    # título
    d.rounded_rectangle([70,40,930,135],radius=14,fill=(185,28,28),outline=(255,120,120),width=3)
    d.text((100,58),'PANORAMA BRASIL HOJE',font=F(62),fill=(255,255,255))
    d.rounded_rectangle([960,52,1700,122],radius=35,fill=(8,22,44,230),outline=(255,170,60),width=3)
    d.text((990,60),ed,font=F(44),fill=(255,190,80))
    # hero
    panel(im,[70,160,1355,470]); thumb(im,hero[0],[100,190,540,440])
    d=ImageDraw.Draw(im,'RGBA'); d.rounded_rectangle([570,195,570+len(hero[1])*22+36,243],radius=10,outline=(90,185,255),width=3,fill=(10,40,80))
    d.text((588,200),hero[1].upper(),font=F(32),fill=(255,255,255))
    fit(im,(570,262,1330,455),hero[2],52)
    # laterais
    y=150
    for p in sides:
        panel(im,[1380,y+10,1930,y+160]); thumb(im,p[0],[1395,y+25,1535,y+145]); fit(im,(1555,y+28,1915,y+150),p[1],27); y+=165
    # últimas
    panel(im,[70,490,1355,1010]); d=ImageDraw.Draw(im); d.text((100,510),'ÚLTIMAS NOTÍCIAS',font=F(40),fill=(255,255,255))
    n=len(lasts); cw=(1355-70-60-(n-1)*25)//n
    for i,l in enumerate(lasts):
        x=100+i*(cw+25); thumb(im,l[0],[x,575,x+cw,800]); d=ImageDraw.Draw(im); d.text((x,815),l[1].upper()+':',font=F(28),fill=(80,200,255))
        fit(im,(x,850,x+cw,1000),l[2],32)
    # leia também
    panel(im,[1380,520+ (len(sides)-2)*0,1930,1010]); d=ImageDraw.Draw(im); d.text((1410,545),'LEIA TAMBÉM',font=F(40),fill=(255,255,255))
    y=605
    for i,l in enumerate(leia[:5]):
        d.text((1410,y+8),f'{i+1}.',font=F(44),fill=(60,180,255)); y2=fit(im,(1470,y+6,1910,y+6+66),l,27); d.line([(1410,y+76),(1905,y+76)],fill=(70,120,170),width=2); y=y+80
    d.text((1000,1050),'@ FK3D Prints',font=F(30),fill=(170,190,215),anchor='mm')
    im.save(out,quality=92)

def set_dir(p):
    global R; R=p if p.endswith('/') else p+'/'
