#!/usr/bin/env python3
"""Monta o Plantão do Panorama a partir de edition.json (sem reler o template no navegador).
Uso: python3 build.py edition.json [--imgdir PASTA_DO_REPO]
Gera: <out>/plantao.html (HTML completo para colar no Blogger), miniaturas que faltarem e a capa da edição."""
import json,sys,os,html,argparse
HERE=os.path.dirname(os.path.abspath(__file__))
def rd(n): return open(os.path.join(HERE,n),encoding='utf-8').read()
def esc(t): return t  # textos já vêm em HTML simples (acentos ok)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('edition'); ap.add_argument('--imgdir',default='.'); a=ap.parse_args()
    E=json.load(open(a.edition,encoding='utf-8')); it=E['items']; C=E['commit']  # C = hash do commit com as imagens
    B=f"https://cdn.jsdelivr.net/gh/FlavioJRCarvalho/imagens-blogs@{C}/"
    pre=E['prefix']  # ex.: 2026-11-16-noite-
    sys.path.insert(0,HERE); import thumbs,cover
    cover.set_dir(a.imgdir)
    for i,x in enumerate(it):  # miniaturas que faltarem (assunto literal, sem logos)
        x.setdefault('img',f"{pre}{x['id']}.jpg")
        p=os.path.join(a.imgdir,x['img'])
        if not os.path.exists(p): thumbs.make_thumb(x.get('motif','generico'),x.get('label',x['tag']),p,hero=(i==0))
    covname=E.get('cover') or f"{E['prefix'][:10]}-plantao-capa-{E['slug']}.jpg"
    cp=os.path.join(a.imgdir,covname)
    if not os.path.exists(cp):
        short=lambda x: x.get('short',x['title'])
        if E.get('cover_style','hud')=='hud':
            import cover_hud
            dt=E['prefix'][:10].split('-'); dt='/'.join([dt[2],dt[1],dt[0]])
            cover_hud.make(cp,dt,E['label_cover'].split('•')[0].strip(),E.get('cover_headline') or short(it[0]),
                [(x['tag'],short(x),x.get('motif')) for x in it[1:3]],it[0].get('motif','generico'),it[0].get('bg'),a.imgdir)
        else: cover.make(cp,E['label_cover'],(it[0]['img'],it[0]['tag'],short(it[0])),
            [(x['img'],f"{x['tag']}: {short(x)}") for x in it[1:3]],
            [(x['img'],x['tag'],short(x)) for x in it[3:6]],[short(x) for x in it[6:11]] or [short(x) for x in it[3:6]])
    im=lambda f: B+f
    h=['<style>\n'+rd('template.css')+'</style>\n<div class="pl">\n']
    h.append('<div class="hd"><a class="bt" href="/">&#9776; Menu</a><a class="logo" href="/">Panorama<span>Brasil Hoje</span></a><a class="bt" href="/search">Buscar</a></div>\n')
    h.append(f'<img src="{im(covname)}" alt="Panorama Brasil Hoje: Plantão de notícias do dia" style="width:100%;height:auto;border-radius:10px;margin:0 0 14px;display:block">\n')
    pv=E.get('prev'); prev=f' Veja também a <a href="{pv["url"]}" target="_blank" rel="noopener">{pv["label"]}</a>.' if pv else ''
    h.append(f'<p><strong>Plantão Panorama, {E["weekday"]}, {E["date_long"]}, edição {E["edition"]}.</strong> As notícias do dia, com resumo, fonte e o que ainda não está confirmado. Atualizado às {E["time"]}.{prev}</p>\n')
    x=it[0]
    h.append(f'<div class="grid">\n<div class="card hero"><img class="big" src="{im(x["img"])}" alt="{x["title"]}" style="max-width:520px;width:100%;margin:0 auto 10px"><span class="tag">{x["tag"]}</span><h2><a href="#{x["id"]}">{x["title"]}</a></h2><p>{x["summary"]}</p><span class="meta">{x["meta"]}</span></div>\n<div class="side">\n')
    for x in it[1:3]: h.append(f'<div class="card"><img class="th" src="{im(x["img"])}" alt="{x["title"]}"><span class="tag">{x["tag"]}</span><h3><a href="#{x["id"]}">{x["title"]}</a></h3></div>\n')
    h.append('</div>\n</div>\n<div class="cols">\n<div>\n<h2>Últimas notícias</h2>\n')
    for x in it[3:]: h.append(f'<div class="item"><img class="th" src="{im(x["img"])}" alt="{x["title"]}"><span class="tag">{x["tag"]}</span><h3><a href="#{x["id"]}">{x["title"]}</a></h3><p>{x["summary"]}</p></div>\n')
    h.append('</div>\n<div class="leia">\n<strong>Leia também</strong>\n<ul>\n')
    for x in (it[3:] or it[1:3]): h.append(f'<li><img src="{im(x["img"])}" alt="{x["title"]}"><a href="#{x["id"]}">{x["title"]}</a></li>\n')
    h.append('</ul>\n</div>\n</div>\n')
    for x in it:
        src='; '.join(f'<a href="{s["url"]}" target="_blank" rel="noopener">{s["label"]}</a> ({s["date"]})' for s in x['sources'])
        lab='Fontes' if len(x['sources'])>1 else 'Fonte'
        body=''.join(f'<p>{p}</p>\n' for p in x['body'])
        em=f'<p><strong>Em apuração:</strong> {x["pending"]}</p>\n' if x.get('pending') else ''
        h.append(f'<div class="sec" id="{x["id"]}"><h2>{x["title"]}</h2>\n{body}{em}<p><strong>Por que importa:</strong> {x["why"]}</p>\n<p><strong>{lab}:</strong> {src}.</p></div>\n')
    h.append(f'<p><em>Plantão apurado em {E["date"]}, às {E["time"]}, com base nas fontes citadas. Veja a nossa política editorial e de correções.</em></p>\n')
    h.append(rd('template_footer.html')+rd('template_signature.html'))
    out=os.path.join(os.path.dirname(os.path.abspath(a.edition)),'plantao.html'); open(out,'w',encoding='utf-8').write(''.join(h))
    words=len(html.unescape(''.join(h)).split())
    print('OK',out,'| capa:',covname,'| itens:',len(it),'| imagens a enviar ao repo:',[x['img'] for x in it]+[covname])
main()
