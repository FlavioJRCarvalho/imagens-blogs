# Fluxo enxuto do Plantão (Panorama Brasil Hoje)

1. Escrever `edition.json` (itens verificados; ver /ed exemplo no commit) — só texto, sem HTML.
2. `python3 tools/plantao/build.py edition.json --imgdir <repo>` → gera `plantao.html`, a capa própria da edição e miniaturas faltantes.
3. Commit + push das imagens novas; colocar o hash em `commit` do JSON e rodar build de novo.
4. Subir `plantao.html` como `tmp-plantao-<data>-<ed>.html` (commit fixo) e no editor do Blogger fazer `fetch` da URL jsDelivr com `@hash` e injetar no CodeMirror.
5. Título, marcadores, Publicar → Confirmar; checar no feed JSON uma vez.

Economia: sem reextrair template pelo navegador, sem reescrever o layout, uma injeção e uma publicação por post, sem capturas repetidas. Panorama = somente Plantão. Universo 3D = 1.200–1.900 palavras.


## Miniaturas tecnológicas (preferidas)
Em cada item do edition.json, adicione `"card": {"kicker": "CÂMARA • SEG 23/11", "title": "título curto", "rows": [["RÓTULO","valor"],[...],[...]]}` com dados reais da notícia (até 3 linhas curtas). O build gera a miniatura em estilo HUD (infocards.py) em vez do ícone simples. Item 1 (hero) pode ter `"bg": "arquivo.jpg"` (imagem de fundo enviada pelo Flavio). O Flavio NÃO gosta das miniaturas de ícone simples: use sempre `card`.
