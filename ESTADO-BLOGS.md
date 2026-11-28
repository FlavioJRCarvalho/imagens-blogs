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

## Atualização 26–28/11/2026
- 26/11: Plantão noite, Bola na Rede (Atlético-MG x Corinthians), Lucro Zen (reserva de emergência).
- 27/11: Plantão noite (Trabuco/STF/Black Friday), Bola na Rede (São Paulo 3x1 Remo), Lucro Zen (rotativo do cartão), Universo 3D (blobs e zits).
- 28/11: Plantão tarde (Lula defende Trabuco; STF), Bola na Rede (Cruzeiro 1x0 Fluminense), Lucro Zen (juros compostos), Universo 3D (pillowing).
- Arquivos: tmp-*-2711/2811.html; imagens 2026-11-27-* e 2026-11-28-*.
- Publicação: editor HTML (CodeMirror) via jsDelivr no hash do commit; "Confirmar" por JS (regex /confirmar/i); marcadores pela lista de postagens (ícone de etiqueta ao passar o mouse).
- Pendente: 2 rascunhos "Pauta:" no Panorama (Descartar é permanente); tarefas automáticas Bola na Rede e Lucro Zen; Search Console e AdSense.
