# PT-BR translations, batch 5: text added or reworded by the upstream update of 2026-09-23
# (version folder 42.18 -> 42.20). Multi-piece tooltips built with `..` carry the whole
# Portuguese text in the first piece and empty strings in the rest.
SCAN = True

DIAG_TIP = ('Mostra as ferramentas de depuração do A-Life neste menu -- o painel de geração, o catálogo de '
            'encontros, o construtor de postos avançados, o configurador de invasões, Remover NPCs e os '
            'despejos -- e deixa esta máquina enviar esses comandos. Desligado por padrão. Fica salvo na sua '
            'pasta Zomboid, não no save, então continua ligado entre mundos. Só modo solo e admins de servidor.')
RECORDER_TIP = ("Registra o que cada NPC estava fazendo para que um travamento possa ser analisado depois, e é o "
                "que alimenta 'Despejar caixa-preta dos NPCs' e 'Despejar QA dos módulos'. Custa cerca de quatro "
                "chamadas protegidas por NPC a cada 100 ms, por isso fica desligado a menos que você esteja caçando "
                "um bug -- ligue, reproduza o problema e depois despeje. Exige Diagnósticos.")

PT = {
'ALifeCreatorScreen.lua': {
    'Road blockade': 'Bloqueio na estrada', 'Decision module': 'Módulo de decisão',
    'Full face': 'Rosto inteiro', 'Eyes||, { "MakeUpEyes" ,': 'Olhos', 'Eyeshadow': 'Sombra', 'Lips': 'Lábios',
    ' makeup': ' - maquiagem', 'CHOOSE': 'ESCOLHER',
    'Makeup for the outfit set selected below. The swatch is the shade itself: the game ships every lipstick and eyeshadow colour as its own item, and the face paints as textures, so there is no tint to pick. A beard is a model and makeup is a skin texture: the game always draws the beard over it.':
        'Maquiagem do conjunto de roupas selecionado abaixo. A amostra é o próprio tom: o jogo traz cada cor de batom e de sombra como um item separado, e as pinturas de rosto como texturas, então não há cor para escolher. A barba é um modelo e a maquiagem é uma textura de pele: o jogo sempre desenha a barba por cima.',
    "' and everything in it?\n": "' e tudo o que há nela?\n", ' factions and all their NPCs will be deleted.': ' facções e todos os NPCs delas serão excluídos.',
    'SHARE CODE': 'COMPARTILHAR CÓDIGO', 'enter a value.': 'digite um valor.', 'use ||return': 'use ',
    'whole numbers ': 'números inteiros ', ' to ||. floor ) ..': ' a ', 'from ': 'a partir de ',
    'maximum must be at least the minimum.': 'o máximo precisa ser pelo menos igual ao mínimo.',
    'Folder||folder . name or': 'Pasta', 'Imported folder': 'Pasta importada',
    'SHARE FAILED - THE FOLDER HAS NO FACTIONS': 'FALHA AO COMPARTILHAR - A PASTA NÃO TEM FACÇÕES',
    'FOLDER CODE COPIED - FACTIONS: ': 'CÓDIGO DA PASTA COPIADO - FACÇÕES: ', ' - PASTE IT ON DISCORD': ' - COLE NO DISCORD',
    'TOO LONG TO COPY - FOLDER CODE SAVED TO ZOMBOID/LUA/ALIFE_FACTION_CODE.TXT': 'LONGO DEMAIS PARA COPIAR - CÓDIGO DA PASTA SALVO EM ZOMBOID/LUA/ALIFE_FACTION_CODE.TXT',
    'SHARE FAILED: CODE COULD NOT BE COPIED OR SAVED': 'FALHA AO COMPARTILHAR: NÃO FOI POSSÍVEL COPIAR NEM SALVAR O CÓDIGO',
    'FOLDER IMPORTED - FACTIONS: ': 'PASTA IMPORTADA - FACÇÕES: ', 'FOLDER DELETED - FACTIONS DELETED: ': 'PASTA EXCLUÍDA - FACÇÕES EXCLUÍDAS: ',
    'FOLDER DELETE FAILED - COULD NOT SAVE (': 'FALHA AO EXCLUIR PASTA - NÃO FOI POSSÍVEL SALVAR (', ' FACTIONS DELETED)': ' FACÇÕES EXCLUÍDAS)',
    'Base HP, 1-200; the world health multiplier applies on spawn. Default: ': 'PV base, 1-200; o multiplicador de vida do mundo se aplica ao surgir. Padrão: ',
    ' HP. Other skills use 1-10 ratings.': ' PV. As outras habilidades usam notas de 1 a 10.',
    'Relative faction selection weight, 0 to ': 'Peso relativo na escolha da facção, de 0 a ',
    ', not a percentage. Zero disables natural spawning. Sandbox settings control overall encounter frequency.': ', não é uma porcentagem. Zero desativa a geração natural. As opções de sandbox controlam a frequência geral de encontros.',
    'Day 0': 'Dia 0', 'No end': 'Sem fim',
    'Inclusive first and last day; day 0 is the first. Leave either blank to keep that end open.': 'Primeiro e último dia, inclusive; o dia 0 é o primeiro. Deixe qualquer um em branco para não ter limite naquela ponta.',
    'Lone size (1-': 'Tamanho solo (1-', 'Group size (': 'Tamanho do grupo (',
    'Camo pickup': 'Picape camuflada', 'Step van': 'Furgão de entregas', 'Station wagon': 'Perua', 'Off-roader': 'Utilitário 4x4',
    ' FAILED||( failed ) ..': ' FALHARAM', ' OF ||( removed ) ..': ' DE ',
    'None||74 , y ,': 'Nenhuma', 'None||then name =': 'Nenhuma',
    'Lone survivors: ': 'Solitários: ', 'Lone ||or (': 'Solitários ', ' / Groups ': ' / Grupos ',
},
'ALifeContextMenu.lua': {
    'Diagnostics||{ label =': 'Diagnósticos', 'Flight recorder (blackbox)': 'Gravador de voo (caixa-preta)',
    "Shows A-Life's debug tooling on this menu -- the spawn ": DIAG_TIP,
    'panel, the encounter catalogue, the outpost builder, the ': '', 'raid configurator, Remove NPCs and the dumps -- and lets ': '',
    'this machine send those commands. Off by default. Saved ': '', 'in your Zomboid folder, not in the save, so it stays on ': '',
    'across worlds. Singleplayer and server admins only.': '',
    'Records what every NPC was doing so a freeze can be read ': RECORDER_TIP,
    "out afterwards, and is what fills 'Dump NPC blackbox' and ": '', "'Dump module QA'. Costs about four protected calls per NPC ": '',
    'every 100 ms, so it is off unless you are chasing a bug -- ': '', 'switch it on, reproduce the fault, then dump. Needs ': '',
    'Diagnostics.': '', ' on||state and': ' ligado', ' off||" on" or': ' desligado',
},
'ALifeDebugSpawner.lua': {'Any hostile faction': 'Qualquer facção hostil', 'Roaming squad (no encounter)': 'Esquadrão errante (sem encontro)',
    ', flight recorder ': ', gravador de voo ', 'Diagnostics ||activeWindow (': 'Diagnósticos ',
    'on||enabled and': 'ligado', 'on||recorder and': 'ligado', 'off||"on" or': 'desligado'},
'ALifeModuleRadioman.lua': {"An actor allowed to call backup goes to the group's radio on contact (running while the threat can see or reach him), works it for static and a short talk, then calls the faction's support. Kill him mid-call and none comes.":
    'Um ator autorizado a chamar reforços vai até o rádio do grupo no contato (correndo enquanto a ameaça pode vê-lo ou alcançá-lo), mexe nele entre estática e uma conversa curta e então chama o apoio da facção. Mate-o no meio da chamada e ninguém vem.'},
'ALifeModuleBreach.lua': {
    'A fireteam stacks on a door, holds fire on the wall, opens it, checks the doorway, and flows in to fanned corners.':
        'Uma equipe se enfileira numa porta, segura o fogo junto à parede, abre, confere a entrada e entra se abrindo para os cantos.',
    'Indoors with nothing in sight the squad clears the floor room by room: doorway, the far side of the room, a look round, and never two men in one room.':
        'Dentro de casa e sem nada à vista, o esquadrão limpa o andar cômodo por cômodo: a porta, o fundo do cômodo, uma olhada em volta, e nunca dois homens no mesmo cômodo.',
},
}
