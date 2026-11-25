# Estado dos blogs (atualizado 25/11/2026)

## Blogs (Blogger)
- Panorama Brasil Hoje 5969782400997261608: só "Plantão de notícias do dia", capa própria por edição, fatos conferidos, "em apuração" separado, sem notas de editor.
- Bola na Rede 6271299256997450520 | Universo 3D 3336905599622405579 | Lucro Zen 6187271416197924918 (1 post evergreen de finanças por dia, só 1).

## Como publicar (fluxo enxuto)
tools/plantao/README.md. Publicação no Blogger só pelo navegador do app Claude no computador do Flávio (sem API). Marcadores digitados DEPOIS de publicar, depois Atualizar.
Atenção: a URL jsDelivr do HTML deve usar o hash do commit que contém o HTML (conferir tamanho > 5000 antes de salvar).

## Automação
- Tarefa "Plantão Panorama noite" (19h26 BRT): publica sozinha, pula se a edição do dia já existir. Precisa do computador ligado + app aberto.
- Plantão manhã: desligada. Bola na Rede diária só gera .txt. Lucro Zen: sem tarefa.

## Pendências
- Search Console do Flávio precisa ser autorizado (OAuth Windsor) para análise de buscas.
- AdSense: conta em onboarding, sites "Preparando"; ads.txt correto nos 4 blogs.
- Imagem do Bola na Rede 25/11 (Gemini) tem erros: rodada final repetida, "SÃOPACOENSE", fontes. Trocar quando vier nova.
- Imagens: o Flávio gera no Gemini (tecnológicas); eu confiro fatos e aviso erros.
