"""Capa do Plantão no padrão 'HUD' (faixa vermelha, selo de data, manchete e 2 painéis).
Fundo procedural por assunto (motif) ou imagem própria (bg). Sem logos nem rostos."""
import math,random,os
from PIL import Image,ImageDraw,ImageFont,ImageFilter
W,H=2000,1114
FD='/usr/share/fonts/truetype/google-fonts/'
def F(s,it=False): return ImageFont.truetype(FD+('Poppins-BoldItalic.ttf' if it else 'Poppins-Bold.ttf'),s)
CY=(70,190,255); YE=(255,214,64); RD=(200,24,32); WH=(255,255,255)
ACC={'futebol':(30,150,70),'dinheiro':(30,140,90),'clima':(40,110,200),'politica':(70,90,170),'mundo':(30,100,200),
 'saude':(40,170,90),'educacao':(200,120,30),'tecnologia':(110,80,200),'energia':(220,150,20),'justica':(120,90,60),'luto':(80,80,90),'agua':(30,120,200),'aviao':(60,110,190),'generico':(50,120,190)}

def glyph(d,motif,cx,cy,s,col=WH):
    """desenha um símbolo simples centrado em (cx,cy) com tamanho s"""
    r=s/2; lw=max(3,int(s/28))
    if motif=='futebol':
        d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=col)
        p=[(cx+r*.34*math.sin(math.radians(a)),cy-r*.34*math.cos(math.radians(a))) for a in range(0,360,72)]
        d.polygon(p,fill=(25,30,45))
        for a in range(0,360,72):
            x=cx+r*.34*math.sin(math.radians(a)); y=cy-r*.34*math.cos(math.radians(a))
            x2=cx+r*.82*math.sin(math.radians(a)); y2=cy-r*.82*math.cos(math.radians(a))
            d.line([(x,y),(x2,y2)],fill=(25,30,45),width=lw)
    elif motif=='dinheiro':
        d.ellipse([cx-r,cy-r,cx+r,cy+r],outline=col,width=lw*2); d.text((cx,cy),'R$',font=F(int(s*.5)),fill=col,anchor='mm')
    elif motif=='clima':
        for (dx,dy,rr) in [(-.28,.05,.3),(.05,-.12,.38),(.33,.08,.28)]:
            d.ellipse([cx+dx*s-rr*s,cy+dy*s-rr*s,cx+dx*s+rr*s,cy+dy*s+rr*s],fill=col)
        d.rectangle([cx-.5*s,cy+.05*s,cx+.58*s,cy+.36*s],fill=col)
        d.polygon([(cx+.02*s,cy+.1*s),(cx-.14*s,cy+.5*s),(cx+.02*s,cy+.46*s),(cx-.06*s,cy+.85*s),(cx+.22*s,cy+.38*s),(cx+.07*s,cy+.4*s)],fill=YE)
    elif motif=='mundo':
        d.ellipse([cx-r,cy-r,cx+r,cy+r],outline=col,width=lw)
        d.ellipse([cx-r*.45,cy-r,cx+r*.45,cy+r],outline=col,width=lw)
        d.line([(cx-r,cy),(cx+r,cy)],fill=col,width=lw); d.line([(cx,cy-r),(cx,cy+r)],fill=col,width=lw)
        d.arc([cx-r,cy-r*.55,cx+r,cy+r*.55],0,360,fill=col,width=lw)
    elif motif=='saude':
        a=r*.28; d.rectangle([cx-a,cy-r,cx+a,cy+r],fill=col); d.rectangle([cx-r,cy-a,cx+r,cy+a],fill=col)
    elif motif=='politica':
        d.polygon([(cx-r,cy-r*.45),(cx,cy-r),(cx+r,cy-r*.45)],fill=col)
        for i in range(4):
            x=cx-r*.8+i*r*.53; d.rectangle([x,cy-r*.3,x+r*.26,cy+r*.55],fill=col)
        d.rectangle([cx-r,cy+r*.65,cx+r,cy+r*.85],fill=col)
    elif motif=='energia':
        d.polygon([(cx+.1*s,cy-r),(cx-.3*s,cy+.08*s),(cx,cy+.08*s),(cx-.12*s,cy+r),(cx+.32*s,cy-.12*s),(cx+.02*s,cy-.12*s)],fill=YE)
    elif motif=='tecnologia':
        d.rounded_rectangle([cx-r*.6,cy-r*.6,cx+r*.6,cy+r*.6],radius=int(r*.12),outline=col,width=lw)
        d.rectangle([cx-r*.25,cy-r*.25,cx+r*.25,cy+r*.25],fill=col)
        for i in (-.35,0,.35):
            d.line([(cx+i*r,cy-r*.6),(cx+i*r,cy-r*.9)],fill=col,width=lw); d.line([(cx+i*r,cy+r*.6),(cx+i*r,cy+r*.9)],fill=col,width=lw)
            d.line([(cx-r*.6,cy+i*r),(cx-r*.9,cy+i*r)],fill=col,width=lw); d.line([(cx+r*.6,cy+i*r),(cx+r*.9,cy+i*r)],fill=col,width=lw)
    elif motif=='justica':
        d.line([(cx,cy-r),(cx,cy+r*.8)],fill=col,width=lw); d.line([(cx-r*.8,cy-r*.6),(cx+r*.8,cy-r*.6)],fill=col,width=lw)
        for sx in (-.8,.8):
            d.line([(cx+sx*r,cy-r*.6),(cx+sx*r,cy-r*.05)],fill=col,width=lw)
            d.pieslice([cx+sx*r-r*.35,cy-r*.3,cx+sx*r+r*.35,cy+r*.4],0,180,fill=col)
        d.rectangle([cx-r*.4,cy+r*.8,cx+r*.4,cy+r*.9],fill=col)
    elif motif=='educacao':
        d.polygon([(cx-r,cy-r*.1),(cx,cy-r*.6),(cx+r,cy-r*.1),(cx,cy+r*.4)],fill=col)
        d.rectangle([cx-r*.5,cy+r*.1,cx+r*.5,cy+r*.55],fill=col)
    elif motif=='agua':
        d.polygon([(cx,cy-r),(cx-r*.62,cy+r*.15),(cx+r*.62,cy+r*.15)],fill=col); d.ellipse([cx-r*.62,cy-r*.2,cx+r*.62,cy+r*.95],fill=col)
    elif motif=='aviao':
        d.ellipse([cx-r,cy-r*.12,cx+r,cy+r*.12],fill=col)
        d.polygon([(cx-r*.1,cy),(cx-r*.5,cy-r*.75),(cx-r*.28,cy-r*.75),(cx+r*.3,cy)],fill=col); d.polygon([(cx-r*.1,cy),(cx-r*.5,cy+r*.75),(cx-r*.28,cy+r*.75),(cx+r*.3,cy)],fill=col)
        d.polygon([(cx-r,cy),(cx-r*.85,cy-r*.35),(cx-r*.7,cy-r*.35),(cx-r*.6,cy)],fill=col)
    else:
        pts=[]
        for i in range(10):
            rr=r if i%2==0 else r*.45; a=math.radians(i*36-90); pts.append((cx+rr*math.cos(a),cy+rr*math.sin(a)))
        d.polygon(pts,fill=col)

def glow(im,layer,rad=18,k=1.0):
    b=layer.filter(ImageFilter.GaussianBlur(rad))
    if k!=1.0: b=Image.eval(b,lambda v:v)
    im.alpha_composite(b); im.alpha_composite(layer)

def background(motif,seed=7,big=True):
    random.seed(seed); acc=ACC.get(motif,ACC['generico'])
    im=Image.new('RGBA',(W,H)); d=ImageDraw.Draw(im)
    for y in range(H):
        t=y/H; d.line([(0,y),(W,y)],fill=(int(4+6*t),int(14+16*(1-t)),int(34+36*(1-abs(t-.35))),255))
    # brilho central na cor do assunto
    gl=Image.new('RGBA',(W,H),(0,0,0,0)); g=ImageDraw.Draw(gl)
    cx,cy=760,480
    for i in range(14,0,-1):
        rr=int(i*50); a=int(11*(15-i)); g.ellipse([cx-rr,cy-rr,cx+rr,cy+rr],fill=acc+(a,))
    im.alpha_composite(gl.filter(ImageFilter.GaussianBlur(40)))
    # anéis e rede
    ov=Image.new('RGBA',(W,H),(0,0,0,0)); o=ImageDraw.Draw(ov)
    for rr in (260,360,470,590,720):
        o.ellipse([cx-rr,cy-rr,cx+rr,cy+rr],outline=CY+(40,),width=3)
    for a in range(0,360,15):
        x=cx+720*math.cos(math.radians(a)); y=cy+720*math.sin(math.radians(a)); o.line([(cx,cy),(x,y)],fill=CY+(14,),width=2)
    for x in range(0,W,100): o.line([(x,0),(x,H)],fill=CY+(10,))
    for y in range(0,H,100): o.line([(0,y),(W,y)],fill=CY+(10,))
    for _ in range(140):
        x,y=random.randint(0,W),random.randint(0,H); r=random.choice((2,2,3,4)); o.ellipse([x-r,y-r,x+r,y+r],fill=(180,225,255,random.randint(70,190)))
    im.alpha_composite(ov)
    # símbolo grande com brilho
    lay=Image.new('RGBA',(W,H),(0,0,0,0)); glyph(ImageDraw.Draw(lay),motif,cx,cy-20,430,col=(235,246,255,235))
    ImageDraw.Draw(lay).ellipse([cx-300,cy-320,cx+300,cy+280],outline=CY+(150,),width=5)
    if big: glow(im,lay,22)
    return im

def para(d,pts,fill,outline=None,w=3):
    d.polygon(pts,fill=fill)
    if outline: d.line(pts+[pts[0]],fill=outline,width=w)

def fit_lines(d,t,font_fn,boxw,boxh,size,lh=1.08,minsize=34,maxlines=3):
    while True:
        f=font_fn(size); lines=[]; cur=''
        for w in t.split():
            c=(cur+' '+w).strip()
            if d.textlength(c,font=f)<=boxw: cur=c
            else: lines.append(cur); cur=w
        if cur: lines.append(cur)
        if (len(lines)<=maxlines and len(lines)*size*lh<=boxh) or size<=minsize: return f,lines,size
        size-=3

def shadow_text(d,xy,t,f,fill):
    d.text((xy[0]+4,xy[1]+4),t,font=f,fill=(0,0,0,200)); d.text(xy,t,font=f,fill=fill)

def make(out,date,edition,headline,sides,motif='generico',bg=None,imgdir='.'):
    if bg and os.path.exists(os.path.join(imgdir,bg)):
        im=Image.open(os.path.join(imgdir,bg)).convert('RGBA'); s=max(W/im.width,H/im.height)
        im=im.resize((int(im.width*s)+1,int(im.height*s)+1),Image.LANCZOS); x=(im.width-W)//2; y=(im.height-H)//2; im=im.crop((x,y,x+W,y+H))
    else: im=background(motif)
    # escurece base para a manchete
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(sh)
    for y in range(640,H):
        sd.line([(0,y),(W,y)],fill=(2,8,22,int(235*((y-640)/(H-640))**1.2)))
    im.alpha_composite(sh); d=ImageDraw.Draw(im,'RGBA')
    # faixa vermelha
    para(d,[(0,26),(1590,26),(1520,150),(0,150)],RD,(255,255,255,255),4)
    d.text((60,88),'PANORAMA BRASIL HOJE',font=F(96,True),fill=WH,anchor='lm')
    # selo da data
    para(d,[(1650,40),(1990,40),(1990,120),(1610,120)],(8,22,52,235),CY+(255,),4)
    d.text((1815,80),date,font=F(50,True),fill=WH,anchor='mm')
    ew=d.textlength(edition,font=F(30));
    d.rounded_rectangle([1990-ew-44,134,1990,184],radius=10,fill=(8,22,52,225),outline=YE+(255,),width=3)
    d.text((1990-ew/2-22,159),edition,font=F(30),fill=YE,anchor='mm')
    # painéis laterais
    py=[(250,580),(620,950)]
    for (tag,txt,mt),(y0,y1) in zip(sides[:2],py):
        d.rounded_rectangle([1370,y0,1985,y1],radius=26,fill=(8,24,52,225),outline=CY+(255,),width=4)
        ac=ACC.get(mt,ACC['generico']); sz=190; ix,iy=1405,y0+(y1-y0-sz)//2
        d.rounded_rectangle([ix,iy,ix+sz,iy+sz],radius=30,fill=ac+(255,),outline=(255,255,255,200),width=3)
        glyph(d,mt,ix+sz//2,iy+sz//2,int(sz*.62))
        d.rectangle([ix+sz+22,y0+36,ix+sz+27,y1-36],fill=RD)
        tx=ix+sz+50; d.text((tx,y0+30),tag.upper()+' •',font=F(40),fill=YE)
        f,lines,sz2=fit_lines(d,txt,F,1960-tx-8,y1-y0-120,44,minsize=26,maxlines=4)
        y=y0+88
        for l in lines: d.text((tx,y),l,font=f,fill=WH); y+=int(sz2*1.12)
    # manchete
    d.rectangle([34,730,44,1040],fill=RD)
    wh,_,hl=headline.partition('|'); wh=wh.strip(); hl=hl.strip()
    full=(wh+' '+hl).strip(); BW=1230
    f,lines,sz=fit_lines(d,full,F,BW,300,128,lh=1.06,minsize=60,maxlines=3)
    def wrap(t):
        out=[];cur=''
        for w in t.split():
            c=(cur+' '+w).strip()
            if d.textlength(c,font=f)<=BW: cur=c
            else: out.append(cur); cur=w
        if cur: out.append(cur)
        return out
    items=[(l,WH) for l in wrap(wh)]+[(l,YE) for l in wrap(hl)] if hl else [(l,YE if (i==len(lines)-1 and len(lines)>1) else WH) for i,l in enumerate(lines)]
    while len(items)*sz*1.06>310 and sz>60:
        sz-=4; f=F(sz); items=[(l,WH) for l in wrap(wh)]+[(l,YE) for l in wrap(hl)] if hl else items
    y=max(1040-int(len(items)*sz*1.06),715)
    for l,col in items: shadow_text(d,(76,y),l,f,col); y+=int(sz*1.06)
    # linhas de HUD
    d.line([(0,1086),(1500,1086),(1560,1062),(W,1062)],fill=CY+(220,),width=4)
    d.line([(0,1100),(1000,1100)],fill=CY+(110,),width=2)
    im.convert('RGB').save(out,quality=92)
