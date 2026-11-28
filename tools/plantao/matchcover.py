"""Capa de resultado de jogo: placar gigante, duas metades nas cores dos times (sem escudos)."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
F='/usr/share/fonts/opentype/inter/'
def font(w,s): return ImageFont.truetype(F+f'Inter-{w}.otf',s)
def grad(w,h,c1,c2):
    im=Image.new('RGB',(w,h)); px=im.load()
    for y in range(h):
        for x in range(w):
            t=(x/w*0.5+y/h*0.5); px[x,y]=tuple(int(c1[i]+(c2[i]-c1[i])*t) for i in range(3))
    return im
def make(out,home,away,hs,as_,hc,ac,kicker,foot,note,S=2,W=1280,H=640):
    w,h=W*S,H*S
    L=grad(w//4,h//4,hc[0],hc[1]).resize((w,h)); R=grad(w//4,h//4,ac[0],ac[1]).resize((w,h))
    m=Image.new('L',(w,h),0); d=ImageDraw.Draw(m)
    sk=int(90*S); d.polygon([(w//2+sk,0),(w,0),(w,h),(w//2-sk,h)],fill=255)
    im=Image.composite(R,L,m); d=ImageDraw.Draw(im,'RGBA')
    # faixa luminosa na divisão
    d.line([(w//2+sk,0),(w//2-sk,h)],fill=(255,255,255,235),width=6*S)
    # vinheta
    v=Image.new('L',(w,h),0); ImageDraw.Draw(v).ellipse([-w*.1,-h*.3,w*1.1,h*1.3],fill=255)
    v=v.filter(ImageFilter.GaussianBlur(120*S)); dark=Image.new('RGB',(w,h),(0,0,0))
    im=Image.composite(im,dark,v.point(lambda p:int(120+p*0.53)))
    d=ImageDraw.Draw(im,'RGBA')
    def ctext(cx,y,t,f,fill=(255,255,255),sh=True):
        b=d.textbbox((0,0),t,font=f); x=cx-(b[2]-b[0])/2-b[0]
        if sh: d.text((x+4*S,y+4*S),t,font=f,fill=(0,0,0,120))
        d.text((x,y),t,font=f,fill=fill)
    # kicker
    kf=font('Bold',27*S); b=d.textbbox((0,0),kicker,font=kf); kw=b[2]-b[0]+56*S
    d.rounded_rectangle([w/2-kw/2,34*S,w/2+kw/2,86*S],radius=26*S,fill=(255,213,74),)
    ctext(w/2,44*S,kicker,kf,fill=(20,20,30),sh=False)
    # nomes
    nf=font('ExtraBold',54*S)
    ctext(w*0.25,150*S,home.upper(),nf); ctext(w*0.75,150*S,away.upper(),nf)
    # placar
    sf=font('Black',250*S)
    ctext(w*0.25,200*S,str(hs),sf); ctext(w*0.75,200*S,str(as_),sf)
    ctext(w/2,265*S,'×',font('Bold',120*S),fill=(255,213,74))
    # nota
    d.rectangle([0,h-130*S,w,h],fill=(8,10,22,225))
    ctext(w/2,h-118*S,note,font('ExtraBold',40*S),sh=False)
    ctext(w/2,h-58*S,foot,font('Medium',28*S),fill=(190,200,225),sh=False)
    im.resize((W,H),Image.LANCZOS).save(out,quality=92)
if __name__=='__main__':
    make('/tmp/claude-0/-home-claude/eaebc631-5a81-50e9-abc1-33ef66d46ded/scratchpad/capa-cruzeiro-flu.jpg',
      'Fluminense','Cruzeiro',0,1,((150,18,58),(96,10,38)),((8,40,130),(20,90,200)),
      'BRASILEIRÃO • 37ª RODADA','Maracanã  •  28 de novembro de 2026',
      'Kaio Jorge decide e Cruzeiro assume o 3º lugar')
