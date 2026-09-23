# Progresso — falas dos NPCs e chat em PT-BR

Arquivo de retomada. Se a sessão acabar, leia isto primeiro e continue do "Próximo passo".
Todo lote traduzido é salvo em `translations/speech/` e vai para um commit no GitHub.

## Arquitetura (decidida)

- Nenhum arquivo do original é substituído para as falas. Arquivos novos do mod:
  - `42/media/lua/shared/ProjectALifePTBR/Core.lua`: dicionário (inglês → português), busca e valores
    padrão em PT para `{date}`, `{time}`, `{count}` etc.
  - `42/media/lua/shared/ProjectALifePTBR/Speech/*.lua`: dicionário gerado pelo build a partir de
    `translations/speech/**/*.json`.
  - `42/media/lua/shared/ZZZ_ProjectALifePTBR.lua`: ganchos.
    - `DialogueData.load`: traduz na memória os registros (talk/barks/scenes/radio), depois de carregados.
    - `Speech.render`: traduz o modelo antes de preencher as `{marcações}`.
    - `Speech.say`: traduz falas fixas do código (assalto, pânico, reações etc.) por texto exato.
    - Chat: `Intents.normalize` (acentos e abreviações PT) e intenções PT registradas no `Data.load`.
- Fala sem tradução aparece em inglês (não quebra nada).

## Etapas

1. [x] Infraestrutura (ganchos, formato do dicionário, build, ferramentas de fila e checagem, `tools/test_runtime.sh`)
2. [ ] Chat em português (intenções e normalização)
3. [ ] Gritos e comentários (barks, cerca de 3,7 mil frases)
4. [ ] Falas fixas do código: assalto, pânico, posturas, arrombamento, reações e vozes
5. [ ] Respostas da conversa (talk, cerca de 7,2 mil frases)
6. [ ] (etapa 2) Cenas e rádio

## Próximo passo

Etapa 2: escrever `translations/chat/intents.json` (frases PT para as 150 intenções de
`upstream/.../Dialogue/Data/ALifeDialogue_intents_1.lua`) e rodar `tools/test_runtime.sh`.

## Como traduzir um lote (ciclo)

```bash
cd tools
python3 speech_queue.py stats                 # situação
python3 speech_queue.py next barks 150 > ../work/fila.txt   # próximo lote (grava work/queue_current.json)
# escrever ../work/lote.txt com linhas "id<TAB>tradução" (uma por linha da fila)
python3 speech_commit.py ../work/lote.txt     # valida, salva em translations/speech/, commit e push
```

Se a sessão cair no meio de um lote, rode `speech_queue.py next` de novo: ele só lista o que ainda falta.

## Registro

- 2026-09-23: plano definido; medido o volume (cerca de 443 mil palavras no total).
- 2026-09-23: infraestrutura pronta e testada (ganchos em DialogueData.load, Speech.render/say, chat).
