"""Miniaturas de assunto (sem logos, sem fotos de terceiros). Uso: make_thumb(motif, label, out, hero=False)
motifs: futebol, dinheiro, clima, politica, mundo, saude, educacao, tecnologia, energia, justica, luto, generico"""
from PIL import Image, ImageDraw, ImageFont
import math
S=2
FB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
PAL={'futebol':((20,60,40),(60,140,80)),'dinheiro':((20,50,40),(70,150,110)),'clima':((25,50,90),(120,170,220)),'politica':((25,40,80),(90,120,190)),
'mundo':((15,35,70),(60,120,180)),'saude':((20,70,80),(100,190,200)),'educacao':((60,40,90),(150,110,200)),'tecnologia':((15,25,50),(40,110,190)),
'energia':((40,30,20),(190,120,50)),'justica':((50,35,25),(170,130,90)),'luto':((25,25,35),(90,90,110)),'generico':((25,40,70),(80,120,170))}
def make_thumb(motif,label,out,hero=False):
    W,H=(1280,600) if hero else (640,480)
    c1,c2=PAL.get(motif,PAL['generico']); im=Image.new('RGB',(W*S,H*S)); d=ImageDraw.Draw(im)
    for y in range(H*S):
        t=y/(H*S); d.line([(0,y),(W*S,y)],fill=tuple(int(c1[i]+(c2[i]-c1[i])*t) for i in range(3)))
    k=W/640; cx,cy=W/2*S,H*0.42*S; r=min(W,H)*0.26*S
    WH=(255,255,255); DK=(30,35,45)
    def E(b,**kw): d.ellipse([v*S for v in b],**kw)
    def R(b,**kw): d.rectangle([v*S for v in b],**kw)
    def P(pts,**kw): d.polygon([(x*S,y*S) for x,y in pts],**kw)
    x0,y0=W/2,H*0.42; u=min(W,H)/480
    if motif=='futebol':
        R([0,H*0.7,W,H],fill=(40,125,65)); E([x0-90*u,y0-90*u,x0+90*u,y0+90*u],fill=WH,outline=DK,width=6*S)
        P([(x0,y0-35*u),(x0+33*u,y0-10*u),(x0+20*u,y0+30*u),(x0-20*u,y0+30*u),(x0-33*u,y0-10*u)],fill=DK)
    elif motif=='dinheiro':
        R([x0-120*u,y0-60*u,x0+120*u,y0+60*u],fill=(235,225,170),outline=DK,width=5*S); E([x0-40*u,y0-40*u,x0+40*u,y0+40*u],outline=DK,width=5*S)
    elif motif=='clima':
        E([x0-110*u,y0-40*u,x0-10*u,y0+50*u],fill=WH); E([x0-60*u,y0-80*u,x0+60*u,y0+30*u],fill=WH); E([x0+0*u,y0-30*u,x0+120*u,y0+55*u],fill=WH)
        for i in range(5): d.line([((x0-80*u+i*45*u)*S,(y0+70*u)*S),((x0-95*u+i*45*u)*S,(y0+115*u)*S)],fill=(150,200,255),width=6*S)
    elif motif=='politica':
        R([x0-130*u,y0+60*u,x0+130*u,y0+90*u],fill=(230,232,240)); [R([x0-110*u+i*44*u,y0-40*u,x0-90*u+i*44*u,y0+60*u],fill=(240,242,250)) for i in range(6)]
        P([(x0-140*u,y0-40*u),(x0,y0-110*u),(x0+140*u,y0-40*u)],fill=(225,228,240))
    elif motif=='mundo':
        E([x0-100*u,y0-100*u,x0+100*u,y0+100*u],fill=(40,110,190),outline=WH,width=5*S); d.arc([v*S for v in (x0-45*u,y0-100*u,x0+45*u,y0+100*u)],0,360,fill=WH,width=4*S); d.line([(x0-100*u)*S,y0*S,(x0+100*u)*S,y0*S],fill=WH,width=4*S)
    elif motif=='saude':
        R([x0-30*u,y0-100*u,x0+30*u,y0+100*u],fill=WH); R([x0-100*u,y0-30*u,x0+100*u,y0+30*u],fill=WH)
    elif motif=='educacao':
        P([(x0-110*u,y0-20*u),(x0,y0-70*u),(x0+110*u,y0-20*u),(x0,y0+30*u)],fill=WH); R([x0-60*u,y0+10*u,x0+60*u,y0+60*u],fill=(235,235,245))
    elif motif=='tecnologia':
        R([x0-80*u,y0-80*u,x0+80*u,y0+80*u],fill=(25,35,60),outline=(120,200,255),width=5*S); R([x0-40*u,y0-40*u,x0+40*u,y0+40*u],fill=(120,200,255))
        for i in range(5): d.line([((x0-80*u+i*40*u)*S,(y0-80*u)*S),((x0-80*u+i*40*u)*S,(y0-110*u)*S)],fill=(120,200,255),width=4*S)
    elif motif=='energia':
        P([(x0,y0-100*u),(x0+70*u,y0+20*u),(x0,y0+90*u),(x0-70*u,y0+20*u)],fill=(30,30,35)); E([x0-70*u,y0-10*u,x0+70*u,y0+90*u],fill=(30,30,35))
    elif motif=='justica':
        d.line([(x0*S,(y0-90*u)*S),(x0*S,(y0+80*u)*S)],fill=WH,width=7*S); d.line([((x0-100*u)*S,(y0-60*u)*S),((x0+100*u)*S,(y0-60*u)*S)],fill=WH,width=7*S)
        E([x0-130*u,y0-30*u,x0-70*u,y0+0*u],fill=WH); E([x0+70*u,y0-30*u,x0+130*u,y0+0*u],fill=WH)
    elif motif=='luto':
        E([x0-70*u,y0-70*u,x0+70*u,y0+70*u],fill=(235,235,240)); R([x0-8*u,y0-60*u,x0+8*u,y0+60*u],fill=DK)
    else:
        E([x0-90*u,y0-90*u,x0+90*u,y0+90*u],fill=(230,235,245))
    f=ImageFont.truetype(FB,int(34*u*S) if not hero else int(48*S))
    if hero: d.text((W/2*S,(H-48*u if not hero else H-50)*S),label.upper()[:26],font=f,fill=WH,anchor='mm')
    im.resize((W,H),Image.LANCZOS).save(out,quality=90)
