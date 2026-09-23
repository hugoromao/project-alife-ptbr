# Project A-Life [ALIFE NPCS] — Tradução PT-BR

Antes de qualquer coisa, quero deixar claro que este é um mod 100% vibecodado com o Claude Code. Ou seja, pode haver problemas sérios de tradução ou bugs no decorrer do jogo. UTILIZE POR SUA CONTA E RISCO.

Não sou desenvolvedor de Lua nem de mods do Zomboid (Tenho interesse, inclusive quero começar a estudar Blender no tempo livre). O problema é que atualmente não existe tradução PT-BR, e eu gostaria de poder jogar este mod com meus amigos que não falam inglês. Assim, vamos seguir testando essa implementação gerada pela IA e corrigindo os problemas que encontrarmos no nosso server. Quem sabe quando eu tiver mais tempo e conhecimento da engine do jogo eu faça uma tradução mais minuciosa e 100% feita por humanos.

Com isso claro, segue abaixo os detalhes do mod/tradução.

---

Tradução para português do Brasil do mod [Project A-Life [ALIFE NPCS]](https://steamcommunity.com/sharedfiles/filedetails/?id=3803984183)
(Workshop 3803984183, Mod ID `ProjectALifeNPCs`), feito por Vice e equipe.

Mod ID da tradução: `ProjectALifeNPCs_PTBR`. Exige o mod original.

> **Tradução feita com IA generativa.** Os textos em português, as ferramentas deste repositório e os
> ajustes de código foram produzidos com o modelo **Claude Opus 5.5** (Anthropic), com a tradução espanhola
> da comunidade como referência do que traduzir. Ainda não houve uma revisão humana completa, então
> pode haver termos estranhos ou textos que não cabem na tela. Correções são bem-vindas via issue ou pull request.

Este repositório não inclui o mod original nem outras traduções, que são de outros autores. As
ferramentas baixam o original da Workshop quando precisam.

## Primeiros passos (depois de clonar)

```bash
./tools/update_upstream.sh   # baixa o original para upstream/ e gera build/
```

Requisitos: Python 3, curl e, para as imagens, Pillow (`pip install pillow`).

## O que está traduzido

- Interface: Criador de facções e NPCs, menus de contexto, conversa com NPCs, rádio dos postos avançados,
  mapa de esquadrões, console de encontros, painel de geração (admin) e janela de status.
- Descrições de comportamentos, módulos, encontros, papéis de NPC, estados de arma e mensagens de admin.
- Opções de sandbox (`Translate/PTBR/Sandbox.json`) e nomes dos itens (`ItemName.json`).

Ainda **não** estão traduzidos: as falas dos NPCs (diálogos, gritos de combate, rádio do Condado de Knox),
cerca de 14 mil linhas. E as palavras que o jogador digita no chat para conversar continuam sendo
reconhecidas em inglês.

## Como funciona

O original escreve quase todo o texto direto no código Lua, então a tradução publica cópias traduzidas
desses arquivos. Elas substituem as do original, porque o mod carrega depois dele (`loadModAfter`).
Por isso, **toda atualização do mod original exige atualizar a tradução**. Se isso não for feito, as
cópias antigas passam por cima do código novo.

Nada é editado à mão nos arquivos `.lua`. Cada texto traduzido fica guardado junto com o contexto de
código em volta, e o build aplica tudo sobre os arquivos **atuais** do original.

```
upstream/ProjectALifeNPCs/   cópia do mod original (baixada da Workshop)
translations/lua/**.json     textos: {en, ctx (contexto), pt}, um JSON por arquivo Lua
translations/patches.py      ajustes de código (maiúsculas com acento, rótulos de abas/espaços/tópicos)
translations/Translate/PTBR  Sandbox.json e ItemName.json
translations/Translate/EN_base  inglês usado como base (para detectar textos alterados)
work/pt_batch*.py            lotes de tradução (fonte dos JSON; use merge_batches.py)
art/                         poster, ícone e prévia da Workshop (tools/make_art.py)
tools/                       lexer Lua, build, reancoragem, varredura, atualização
build/Workshop/...           saída pronta para publicar (gerada pelo build)
```

## Atualizar quando o original mudar

```bash
./tools/update_upstream.sh          # baixa o original, mostra o que mudou e roda o build
python3 tools/reanchor.py           # textos que só mudaram de lugar (simulação)
python3 tools/reanchor.py --write   # aplica e remove traduções de textos que sumiram
python3 tools/build.py              # deve terminar com "0 stale entries"
```

Os textos novos aparecem como `MISSING`/`CHANGED` (sandbox). Para achar textos novos no código, use
`python3 tools/scan_candidates.py <caminho do .lua>`. Traduza num lote novo (`work/pt_batchN.py` com
`SCAN = True`) e rode `python3 tools/merge_batches.py` e depois `python3 tools/build.py`. Aumente o
número em `VERSION` antes de reenviar.

Para conferir a sintaxe, rode `luac -p` (Lua 5.1) nos arquivos de `build/`.
