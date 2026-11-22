"""Miniaturas 'tecnológicas' que mostram os dados da própria notícia (sem logos, sem rostos).
make_card(out, motif, kicker, title, rows, hero=False, bg=None, imgdir='.')
  rows = [(RÓTULO, valor), ...] até 3 linhas. bg = imagem de fundo opcional (ex.: arte de capa fornecida)."""
import os
from PIL import Image,ImageDraw
import cover_hud as C
from cover_hud import F,CY,YE,WH,RD,ACC

def _wrap(d,t,f,w):
    out=[];cur=''
    for x in t.split():
        c=(cur+' '+x).strip()
        if d.textlength(c,font=f)<=w: cur=c
        else: out.append(cur); cur=x
    if cur: out.append(cur)
    return out

def make_card(out,motif,kicker,title,rows,hero=False,bg=None,imgdir='.'):
    W,H=(1280,600) if hero else (640,480); S=2; w,h=W*S,H*S
    if bg:
        im=Image.open(os.path.join(imgdir,bg)).convert('RGBA'); k=max(w/im.width,h/im.height)
        im=im.resize((int(im.width*k)+1,int(im.height*k)+1),Image.LANCZOS); x=(im.width-w)//2; y=(im.height-h)//2; im=im.crop((x,y,x+w,y+h))
    else:
        im=C.background(motif,big=hero); k=max(w/im.width,h/im.height)
        im=im.resize((int(im.width*k)+1,int(im.height*k)+1),Image.LANCZOS); x=(im.width-w)//2; y=(im.height-h)//2; im=im.crop((x,y,x+w,y+h))
    d=ImageDraw.Draw(im,'RGBA'); u=h/480 if not hero else h/600*1.0
    if bg:  # escurece a base para o placar
        sh=Image.new('RGBA',(w,h),(0,0,0,0)); sd=ImageDraw.Draw(sh)
        for y in range(int(h*.55),h): sd.line([(0,y),(w,y)],fill=(2,8,22,int(225*((y-h*.55)/(h*.45))**1.1)))
        im.alpha_composite(sh); d=ImageDraw.Draw(im,'RGBA')
    ac=ACC.get(motif,ACC['generico'])
    # selo do assunto
    f=F(int(26*u)); tw=d.textlength(kicker,font=f)
    d.rounded_rectangle([24*u,22*u,24*u+tw+36*u,22*u+50*u],radius=10*u,fill=(8,22,52,235),outline=YE+(255,),width=int(3*S/2*1.5))
    d.text((42*u,47*u),kicker,font=f,fill=YE,anchor='lm')
    if hero:
        # placar: título à esquerda, linhas à direita
        bar_y=int(h*0.68)
        d.rectangle([0,bar_y,w,h],fill=(4,12,30,190)); d.line([(0,bar_y),(w,bar_y)],fill=CY+(255,),width=int(5*S/2*1.5))
        ft=F(int(42*u)); lines=_wrap(d,title,ft,w*0.43)[:2]; y=bar_y+int(34*u)
        for l in lines: d.text((40*u,y),l,font=ft,fill=WH); y+=int(52*u)
        cx=int(w*0.48); cw=(w-cx-int(30*u))//max(1,len(rows))
        for i,(a,b) in enumerate(rows):
            x=cx+i*cw; d.rectangle([x,bar_y+int(30*u),x+4,h-int(30*u)],fill=RD)
            d.text((x+int(16*u),bar_y+int(34*u)),a,font=F(int(24*u)),fill=CY)
            fb=F(int(50*u)); d.text((x+int(16*u),bar_y+int(78*u)),b,font=fb,fill=YE if i==len(rows)-1 else WH)
    else:
        # símbolo à esquerda, título à direita
        gx,gy,gs=int(125*u),int(190*u),int(88*u)
        lay=Image.new('RGBA',(w,h),(0,0,0,0)); ld=ImageDraw.Draw(lay)
        ld.rounded_rectangle([gx-gs,gy-gs,gx+gs,gy+gs],radius=int(26*u),fill=ac+(255,),outline=(255,255,255,220),width=int(4*S/2*1.5))
        C.glyph(ld,motif,gx,gy,int(gs*1.25)); C.glow(im,lay,int(14*u)); d=ImageDraw.Draw(im,'RGBA')
        ft=F(int(36*u)); tx=int(240*u); lines=_wrap(d,title,ft,w-tx-int(24*u))
        size=36
        while len(lines)>4 and size>24: size-=2; ft=F(int(size*u)); lines=_wrap(d,title,ft,w-tx-int(24*u))
        y=int(100*u)
        for i,l in enumerate(lines[:4]): d.text((tx,y),l,font=ft,fill=WH); y+=int(size*1.18*u)
        py=int(318*u); d.rounded_rectangle([24*u,py,w-24*u,h-22*u],radius=int(18*u),fill=(8,24,52,225),outline=CY+(255,),width=int(3*S/2*1.5))
        n=max(1,len(rows)); rh=(h-22*u-py-12*u)/n
        for i,(a,b) in enumerate(rows[:3]):
            ry=py+int(8*u)+i*rh
            d.text((48*u,ry+rh/2),a,font=F(int(17*u)),fill=CY,anchor='lm')
            fv=F(int(22*u)); vv=b
            while d.textlength(vv,font=fv)>w-(236*u)-30*u and len(vv)>4: vv=vv[:-1]
            d.text((236*u,ry+rh/2),b,font=fv,fill=WH if i<n-1 else YE,anchor='lm')
            if i<n-1: d.line([(44*u,ry+rh),(w-44*u,ry+rh)],fill=CY+(70,),width=2)
    im.convert('RGB').resize((W,H),Image.LANCZOS).save(out,quality=90)
