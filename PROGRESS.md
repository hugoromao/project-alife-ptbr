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
| barks | 3741 | 3741 | 100.0% |
| code | 1591 | 1591 | 100.0% |
| talk | 7003 | 7191 | 97.4% |
| scenes | 619 | 15198 | 4.1% |
| radio | 14 | 9106 | 0.2% |
<!-- /stats -->

## Etapas

1. [x] Infraestrutura (ganchos, formato do dicionário, build, ferramentas de fila e checagem, `tools/test_runtime.sh`)
2. [x] Chat em português (`translations/chat/intents_ptbr.py`; teste com `tools/chat_try.sh "frase"`)
3. [x] Gritos e comentários (barks, 3.741 frases, 13 lotes)
4. [x] Falas fixas do código (1.591 frases, 6 lotes): vozes por facção, reações, fofoca, módulos
   (pânico, posturas, cautela, assalto, arrombamento), nomes de esconderijo. Ganchos extras:
   `IsoZombie:Say` (as cascas dos NPCs são zumbis), tabelas públicas dos módulos traduzidas no servidor,
   descrições `{den}` do ALifeRumors.describe (`PT.denText`) e frases completadas com valor
   ("[Received: " .. item .. "]", `PT.prefixes`).
5. [ ] Respostas da conversa (talk, cerca de 7,2 mil frases)
6. [ ] (etapa 2) Cenas e rádio

## Próximo passo

Etapa 5: respostas da conversa, em lotes de 250:
`python3 speech_queue.py next talk 250`. As linhas "...continuação" são falas seguintes da mesma resposta.

### Retomar em outro computador

```bash
git clone https://github.com/hugoromao/project-alife-ptbr.git && cd project-alife-ptbr
./tools/update_upstream.sh   # baixa o mod original para upstream/ e gera build/
./tools/test_runtime.sh      # compila o Lua 5.1 local e roda os testes
```

## Tradução em paralelo

A fila de cada fonte é dividida em N partes fixas (blocos de 50 unidades, distribuídos em rodízio),
então tradutores em paralelo nunca pegam a mesma frase. Um lote da parte K de N:

```bash
cd tools
python3 speech_queue.py next talk 200 --part K/N 2>/dev/null | sed 's/\t\[/ [/; s/\]\t/] /' > ../work/fila_talk_pK.txt
# ler ../work/fila_talk_pK.txt e escrever ../work/lote_talk_pK.txt com "id<TAB>tradução"
python3 speech_commit.py ../work/lote_talk_pK.txt --queue work/queue_talk_pK.json
```

O commit usa uma trava (`work/.commit.lock`), então vários tradutores podem salvar ao mesmo tempo.

Automático (4 processos `claude -p --model sonnet`, independentes da conversa; sobrevivem ao fim da sessão
e, se o limite de uso acabar, esperam e tentam de novo; dá para trocar de conta com `/login` no meio):

```bash
setsid nohup python3 tools/parallel_translate.py talk scenes radio > work/parallel.log 2>&1 &
tail -f work/parallel.log      # acompanhar
touch work/STOP                # parar depois do lote atual
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
- 2026-09-23: gritos e comentários completos (3.741).
