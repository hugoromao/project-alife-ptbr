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

## Situação

<!-- stats -->
| Fonte | Traduzidas | Total | % |
|---|---:|---:|---:|
| barks | 3550 | 3741 | 94.9% |
| talk | 0 | 7191 | 0.0% |
| scenes | 2 | 15198 | 0.0% |
| radio | 0 | 9106 | 0.0% |
<!-- /stats -->

## Etapas

1. [x] Infraestrutura (ganchos, formato do dicionário, build, ferramentas de fila e checagem, `tools/test_runtime.sh`)
2. [x] Chat em português (`translations/chat/intents_ptbr.py`; teste com `tools/chat_try.sh "frase"`)
3. [ ] Gritos e comentários (barks, cerca de 3,7 mil frases)
4. [ ] Falas fixas do código: assalto, pânico, posturas, arrombamento, reações e vozes; nomes de
   esconderijo `{den}` em `server/ProjectALife/Talk/ALifeRumors.lua` ("the motel", "a house"...)
5. [ ] Respostas da conversa (talk, cerca de 7,2 mil frases)
6. [ ] (etapa 2) Cenas e rádio

## Próximo passo

Etapa 3: continuar os gritos (`cd tools && python3 speech_queue.py next barks 300`); faltam cerca de 2 mil.

### Retomar em outro computador

```bash
git clone https://github.com/hugoromao/project-alife-ptbr.git && cd project-alife-ptbr
./tools/update_upstream.sh   # baixa o mod original para upstream/ e gera build/
./tools/test_runtime.sh      # compila o Lua 5.1 local e roda os testes
```

## Guia de estilo das falas

- Português do Brasil falado e informal: "tá", "pra", "tô", "né", "a gente" quando soar natural.
- Palavrões com o peso equivalente: fuck → porra/caralho, shit → merda, damn → droga, bitch → vadia/desgraçado(a).
- Manter exatamente as marcações `{town}`, `{name}` etc. Nomes próprios (cidades, pessoas, marcas) não mudam;
  Knox County → Condado de Knox; Kentucky, Louisville, West Point etc. iguais.
- Zumbis: zombies/zeds → zumbis; biters → mordedores; the dead → os mortos; infected → infectados.
- Gênero: quem fala segue o `role`/`sex` do contexto (family_woman, civilian_woman → feminino); o
  jogador é tratado de forma neutra sempre que possível ("você", evitar adjetivos com gênero).
- Tom por grupo: outlaw/raider/gang/club/crime/prison → rude e ameaçador; military/police → seco,
  jargão ("positivo", "câmbio"); family/civilian → comum; rescue → profissional e cansado.
- Linhas curtas continuam curtas (aparecem em cima da cabeça do NPC).

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
- 2026-09-23: chat em português completo (141 entradas, todas as intenções).
