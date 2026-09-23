# Portuguese patterns for the chat intents of Project A-Life, added on top of the
# English ones (same ids). Written the way text looks after normalisation: lower case,
# no accents, abbreviations expanded (vc -> voce, pra -> para, ta -> esta, to -> estou,
# q -> que, n -> nao, pq/porque -> por que). "keywords" uses the original format:
# "all=word,word;word,word|none=word" (every "all" group needs one hit; any "none" hit
# vetoes the intent).
INTENTS = []


def i(intent_id, patterns, keywords=''):
    INTENTS.append({'id': intent_id, 'patterns': patterns.split('|'), 'keywords': keywords})


# --- part 1: conversation, feelings, world questions ------------------------------
i('TELL_JOKE', 'conta uma piada|me conta uma piada|fala algo engracado|me faz rir|sabe alguma piada|tem alguma piada|me anima|conta piada',
  'all=piada,piadas,engracado,engracada,rir,me anima,humor,graca;conta,conte,fala,diga,me faz,sabe,tem,alguma,algo|none=nao tem graca,que engracado,muito engracado,cheiro engracado,barulho engracado,voce e engracado,rir de mim')
i('TELL_STORY', 'conta uma historia|me conta uma historia|qual a sua historia|qual e a sua historia|fala de voce|me fala de voce|me conta sobre voce|quem voce era antes|fala comigo',
  'all=historia,historias,sobre voce,de voce,sua vida;conta,conte,fala,qual,tem,sabe,compartilha|none=piada,se identifica')
i('LAUGH', 'haha|hahaha|kkk|rs|que engracado|essa foi boa|muito bom|boa essa')
i('ASK_SING', 'canta uma musica|canta alguma coisa|voce sabe cantar|canta para mim|voce canta|canta uma para a gente|cantarola alguma coisa|sabe alguma musica',
  'all=canta,cantar,cantarola,uma musica,cancao,musicas;voce,para mim,para a gente,alguma,sabe,consegue,canta|none=musica favorita,que musica,escuta,escutar,radio,banda,bandas')
i('ASK_BEFORE', 'como era a vida antes|como era antes|como era a sua vida|como era a vida antes de tudo isso|a vida antes|me fala de antes|como eram as coisas antes|voce lembra do normal',
  'all=antes,antigamente,naquela epoca,tempos normais,velhos tempos,mundo antigo,vida normal;vida,como,coisas,era,eram,lembra|none=trabalho,emprego,fazia antes,voce fazia,antes de escurecer,antes da noite,antes que')
i('ASK_MISS', 'do que voce mais sente falta|do que voce sente falta|sente falta de alguma coisa|sente falta de que|voce sente falta da vida antiga|o que voce mais sente falta|saudade de que',
  'all=falta,saudade,saudades;voce,mais,alguma,de que|none=eu sinto falta,sinto sua falta,errou,errei')
i('ASK_FAVORITE_FOOD', 'qual sua comida favorita|qual e a sua comida favorita|comida favorita|o que voce comeria agora|se pudesse comer qualquer coisa|voce esta com vontade de comer o que|melhor comida que voce ja comeu|prato favorito',
  'all=favorita,favorito,preferida,preferido,vontade de comer,comeria,melhor comida,melhor refeicao;comida,comer,prato,refeicao,lanche,janta,cafe da manha|none=tem comida,tem algo,preciso,sobrando,pode me dar')
i('ASK_SPORTS', 'voce gosta de esporte|voce torce para quem|qual seu time|voce assiste basquete|voce gosta de futebol|voce acompanha beisebol|torce para os wildcats|joga bola',
  'all=esporte,esportes,futebol,basquete,beisebol,time,wildcats,cardinals,corrida,hoquei;gosta,torce,torcedor,assiste,acompanha,favorito,joga,jogava,qual,seu|none=equipe da swat,taco de beisebol,meu time')
i('ASK_MUSIC', 'que musica voce gosta|que tipo de musica voce gosta|banda favorita|musica favorita|o que voce escuta|voce gosta de musica|tem alguma fita|ouviu alguma musica boa',
  'all=musica,musicas,banda,bandas,cantor,cantora,album,fita,fitas,rock,country,rap,walkman,disco,discos,sertanejo;gosta,escuta,ouve,favorita,favorito,tipo,tem,ouviu,curte|none=canta,cantar,fita adesiva')
i('ASK_PRESIDENT', 'quem e o presidente|e o clinton|o presidente esta vivo|cade o presidente|onde esta o presidente|o que o clinton esta fazendo|bill clinton|o presidente morreu',
  'all=presidente,clinton,vice presidente,al gore;quem,onde,cade,esta,vivo,morto,morreu,fazendo,sobre,e o')
i('FLIRT', 'voce e bonita|voce e bonito|voce e fofa|voce e fofo|quer sair comigo|voce e solteira|voce e solteiro|voce e linda|voce e lindo|voce e gostosa|voce e gostoso|quer namorar comigo',
  'all=bonita,bonito,linda,lindo,fofa,fofo,gata,gato,gostosa,gostoso,solteira,solteiro,namorar,namorada,namorado,casar comigo,beijo,me beija,charmosa,charmoso;voce,comigo,e,esta|none=minha namorada,meu namorado,bonito dia,dia bonito')
i('ASK_SLEEP', 'voce dorme|como voce dorme|quando voce descansa|voce dorme alguma vez|quando voce dorme|voces fazem turnos|quem vigia a noite|voce consegue dormir',
  'all=dorme,dormir,dormindo,descansa,descansar,cochilo,turno,turnos,vigia,pesadelos;voce,voces,como,quando,quem,consegue|none=onde eu durmo,posso dormir,dormir com voce,ficar com voce,preciso dormir,preciso descansar')
i('ASK_NOISE', 'eles ouvem barulho|eu devo ficar quieto|tiro atrai eles|barulho atrai eles|eles escutam a gente|eles sao atraidos pelo som|devo fazer silencio|atirar chama eles',
  'all=barulho,barulhos,som,sons,alto,silencio,quieto,tiro,tiros,escutam,ouvem,atrai,atraidos,chama eles;eles,devo,deveria,a gente,isso|none=ouviu isso,que barulho,que som,foi isso,para de atirar,nao atira,cala a boca')
i('ASK_CORPSES', 'o que voce faz com os corpos|eu devo queimar eles|a gente devia queimar os corpos|e os corpos|como se livrar dos corpos|voce enterra eles|devo enterrar os mortos|queimar os cadaveres',
  'all=corpos,corpo,cadaveres,cadaver,queimar,queima,enterrar,enterra,covas,cova;o que,devo,deveria,voce,como,a gente,eles,os mortos|none=colete,armadura,alguem,ninguem,todo mundo')
i('ASK_WHAT_IS_THAT', 'que barulho e esse|ouviu isso|o que foi isso|que som e esse|que diabos foi isso|voce ouviu isso|o que e isso|que porra foi essa',
  'all=esse barulho,esse som,ouviu isso,escutou isso,foi isso,foi essa,esse estrondo,esse grito,esse tiro,essa explosao,esse cheiro;o que,que,voce|none=o que voce disse,helicoptero')
i('ASK_ALONE_NIGHT', 'posso ficar com voce esta noite|posso dormir no seu acampamento|posso passar a noite|posso ficar com voces|posso dormir na sua casa|me deixa passar a noite|tem lugar para mim esta noite|posso ficar com voce',
  'all=ficar,dormir,passar a noite,pousar,lugar para mim;esta noite,hoje,com voce,com voces,seu acampamento,sua casa,sua base,a noite;posso,me deixa,da para,tem lugar|none=posso ir com voce,entrar no seu grupo,fica longe,fique seguro,fica para tras')
i('ASK_REAL', 'voce e de verdade|eu estou sonhando|isso esta acontecendo mesmo|isso e real|isso nao pode ser real|me diz que isso e um sonho|isso e um pesadelo|estou ficando louco',
  'all=real,verdade,sonhando,sonho,pesadelo,acontecendo mesmo,me belisca,ficando louco,ficando louca,alucinando;isso,voce,eu,estou,nao pode ser,me diz|none=nome verdadeiro,arma de verdade,voce sonha')
i('SWEAR_VENT', 'que merda|isso e um inferno|porra|caralho|puta que pariu|droga|merda|que saco|isso e uma bosta|vai tomar no cu esse mundo')
i('SMALL_TALK', 'dia bonito|esta tranquilo hoje|esta quente aqui|vamos falar de outra coisa|que dia lindo|que calor|vamos so conversar|esse calor hein',
  'all=dia bonito,dia lindo,tranquilo hoje,calor,abafado,conversar,bater papo,mosquito,mosquitos,pernilongo,falar de outra coisa;esta,hoje,que,aqui,isso,so,vamos,esse|none=me fala de,e o,vai chover')
i('PLAYER_BITTEN', 'fui mordido|fui mordida|me morderam|acho que estou infectado|acho que estou infectada|um deles me mordeu|ele me mordeu|eles me morderam|levei uma mordida',
  'all=mordido,mordida,mordeu,morderam,infectado,infectada,arranhado,arranhada,arranhao,arranhou;eu,fui,me,acho,estou,levei,um deles|none=voce foi,voce esta,te morderam,te mordeu,seu,sua,mordida de comida')
i('PLAYER_HURT', 'estou ferido|estou ferida|preciso de um medico|estou sangrando|me ajuda estou machucado|estou machucado|estou machucada|levei um tiro|fui baleado|fui baleada',
  'all=ferido,ferida,sangrando,machucado,machucada,baleado,baleada,levei um tiro,quebrei,quebrado,esfaqueado,cortado,dor,medico,socorro;eu,estou,fui,levei,meu,minha,me,preciso|none=voce esta,voce se machucou,nao vou te machucar,te machucar,atirei,nao atira,mordido,mordeu,eu sou medico,eu era medico,bom tiro')
i('PLAYER_SAD', 'perdi minha familia|minha esposa morreu|meu marido morreu|todo mundo se foi|perdi todo mundo|minha familia morreu|pegaram minha esposa|meu marido virou',
  'all=perdi,morreu,morreram,se foi,se foram,mataram,pegaram,virou,viraram,faleceu,nao sobreviveu,enterrei;minha esposa,meu marido,minha mulher,minha familia,meus filhos,meu filho,minha filha,minha mae,meu pai,meu irmao,minha irma,meu amigo,minha amiga,meu bebe,meus pais,todo mundo,todos,minha namorada,meu namorado,minha avo,meu avo|none=voce,sua familia,seu,sua,onde esta,voce viu,procurando')
i('PLAYER_SCARED', 'estou com medo|eu nao consigo|nao aguento mais|estou apavorado|estou apavorada|estou morrendo de medo|eu nao quero morrer|estou surtando',
  'all=medo,apavorado,apavorada,assustado,assustada,surtando,nao consigo,nao aguento,nao quero morrer,tremendo,desesperado,desesperada;eu,estou,me,to|none=voce esta,voce tem medo,nao tenha medo,sem medo,me assustou,nao tenho medo')
i('PLAYER_TIRED_HUNGRY', 'estou cansado|estou cansada|estou com fome|estou morrendo de fome|estou exausto|estou exausta|preciso descansar|preciso dormir|nao comi nada|estou com sede',
  'all=cansado,cansada,fome,faminto,faminta,exausto,exausta,sede,morto de cansaco,sono,nao comi,preciso descansar,preciso dormir;eu,estou,to,muito,preciso,me|none=voce esta,voce tem fome,cansado de voce,cansado disso,posso dormir,onde posso')
i('ENCOURAGE', 'vai dar tudo certo|a gente vai conseguir|nao desiste|aguenta firme|vai ficar tudo bem|vai ficar bem|cabeca erguida|nos vamos sair dessa|forca',
  'all=vai dar certo,dar tudo certo,conseguir,desiste,desista,aguenta,aguente,firme,ficar bem,ficar tudo bem,cabeca erguida,sair dessa,passar por isso,nao esta sozinho,nao esta sozinha,forca;a gente,nos,voce,vai,vamos,nao,fica,tudo|none=eu nao consigo,eu desisto,sera que,como voce conseguiu,me rendo')
i('ASK_HOPE', 'vai melhorar|ainda tem esperanca|e o fim do mundo|existe esperanca|isso vai acabar algum dia|as coisas vao melhorar|a gente vai ficar bem|as coisas vao voltar ao normal',
  'all=esperanca,melhorar,fim do mundo,acabar,voltar ao normal,ficar bem,passar logo,durar para sempre,fim dos tempos;vai,vao,sera,ainda,existe,tem,voce acha,a gente,isso|none=espero que voce,melhor que,melhor nao,sentir melhor,fim da estrada')
i('ASK_GOD', 'voce acredita em deus|voce reza|isso e castigo de deus|deus existe|voce e religioso|voce e religiosa|voce vai na igreja|isso e o arrebatamento|isso e o apocalipse',
  'all=deus,reza,rezar,ora,orar,religioso,religiosa,jesus,senhor,fe,ceu,arrebatamento,apocalipse,julgamento,biblia,acredita em,castigo,pecados;voce,isso,e,existe|none=meu deus,ai meu deus,graças a deus,gracas a deus,pelo amor de deus,juro por deus,deus me livre,deus abencoe,onde fica a igreja')
i('ASK_WHAT_HAPPENED', 'o que aconteceu|o que esta acontecendo|que diabos aconteceu aqui|o que aconteceu aqui|que porra esta acontecendo|o que aconteceu com todo mundo|o que houve|que merda aconteceu',
  'all=aconteceu,acontecendo,houve,rolou;o que,que|none=com voce,com ele,com ela,louisville,fort knox,a base,com meu,com minha')
i('ASK_CAUSE', 'de onde veio isso|o que causou isso|e um virus|como isso comecou|o que esta causando isso|e uma doenca|foi um experimento|de onde veio essa praga',
  'all=causou,causa,causando,comecou,virus,doenca,veio,quimico,praga,infeccao,surto,germe,raiva,experimento;o que,como,e um,e uma,de onde,quem,isso,foi|none=voce veio,cura,vacina,tratamento,barulho,som,quanto tempo,comecou um fogo,ligar o carro,o gerador')
i('ASK_CURE', 'existe cura|tem cura|tem vacina|da para curar|voce consegue curar|existe tratamento|vai ter cura|alguem esta trabalhando numa cura',
  'all=cura,curar,curado,vacina,antidoto,tratamento,imune,imunidade,soro;existe,tem,da para,consegue,vai,alguem,como,e')
i('ASK_GOVERNMENT', 'cade o governo|onde esta o governo|o que o governo esta fazendo|o governo abandonou a gente|e o governo|washington sabe disso|tem alguem no comando|o governo acabou',
  'all=governo,washington,federal,federais,fema,congresso,casa branca,governador,cdc,frankfort;cade,onde,o que,esta,abandonou,e o,sabe,fazendo,acabou')
i('ASK_MILITARY', 'cade o exercito|o exercito esta vindo|e a guarda nacional|onde estao os soldados|os soldados estao vindo|a guarda vem|o exercito vai salvar a gente|os militares estao vindo',
  'all=exercito,militares,militar,guarda nacional,a guarda,soldados,tropas,fuzileiros,forca aerea;cade,onde,vindo,vem,e a,e o,esta,estao,resgate,salvar|none=fort knox,knox,posto de controle,bloqueio,ponte,eu era do exercito,a base,helicoptero')
i('ASK_POLICE', 'cade a policia|o xerife esta por ai|ainda tem policia|onde estao os policiais|tem algum policial sobrando|tem alguma lei por aqui|da para chamar a policia|cade os tiras',
  'all=policia,policial,policiais,tira,tiras,xerife,delegado,patrulha rodoviaria,a lei,911,oficiais;cade,onde,esta,estao,tem,ainda,chamar,sobrou,sobrando|none=voce e policial,voce e da policia,eu sou policial,eu era policial,voce e a lei')
i('ASK_HELICOPTER', 'voce viu o helicoptero|que helicoptero e esse|o que e esse helicoptero|voce ouviu o helicoptero|por que tem um helicoptero|helicopteros|o helicoptero',
  'all=helicoptero,helicopteros,heli,black hawk;viu,vi,ouviu,ouvi,o que,por que,onde,esse,o,tem')
i('ASK_SAFE_ZONE', 'tem uma zona segura|algum lugar e seguro|tem abrigo|tem alguma zona segura|existe algum lugar seguro|onde e a zona segura|tem abrigos|tem campo de refugiados',
  'all=zona segura,abrigo,abrigos,refugiados,lugar seguro,centro de evacuacao,campo da fema,cruz vermelha;tem,existe,algum,onde,sabe|none=dormir,esta noite,esconder,esconderijo,seu acampamento')
i('ASK_EVACUATION', 'tem evacuacao|como a gente sai daqui|a quarentena continua|como eu saio daqui|como a gente sai do condado|estao evacuando|tem algum jeito de fugir|como a gente escapa',
  'all=evacuacao,evacuar,evacuando,quarentena,cordao,sair do condado,escapar,fugir,sair de knox,saida,sair do kentucky,bloqueio,sair daqui;tem,como,estao,ainda,onde,da para,a gente,eu|none=rio,barco,posto de controle,ponte,fugir de voce,me deixa em paz')
i('ASK_LOUISVILLE', 'e louisville|louisville esta segura|o que aconteceu em louisville|o que aconteceu com louisville|como esta louisville|louisville ainda existe|sobrou alguem em louisville|louisville',
  'all=louisville,a cidade grande;e,segura,aconteceu,ainda,sobrou,como esta,caiu,queimando,bombardearam,noticias,tomada|none=como eu chego,como a gente chega,que distancia,qual caminho,onde fica louisville')
i('ASK_FORT_KNOX', 'e fort knox|a base ainda esta de pe|fort knox ainda existe|o que aconteceu em fort knox|o exercito esta em fort knox|fort knox|sobrou alguem na base',
  'all=fort knox,base de knox,a base,o forte,o ouro;e,ainda,aconteceu,esta,de pe,alguem,exercito,segura,soldados,sobrou|none=como eu chego,como a gente chega,qual caminho,sua base,nossa base,minha base')
i('ASK_NEWS', 'alguma novidade|ouviu alguma coisa|quais as noticias|algum boato|quais sao os boatos|o que voce ouviu|alguma noticia|o que andam dizendo|o que se fala por ai',
  'all=novidade,novidades,noticia,noticias,boato,boatos,fofoca,ouviu falar,andam dizendo,se fala;alguma,algum,quais,o que,voce,tem|none=radio,helicoptero,o que voce disse,esse barulho,ouviu isso')
i('ASK_RADIO', 'voce ouviu o radio|tem alguma coisa no radio|qual frequencia|alguma transmissao|o que esta passando no radio|qual canal|voce tem um radio|o radio esta funcionando',
  'all=radio,radios,frequencia,transmissao,transmissoes,canal,radioamador,walkie talkie,rádio;ouviu,no,qual,alguma,tem,passando,escuta,funcionando|none=canal de tv,televisao')
i('ASK_OTHER_SURVIVORS', 'tem outros sobreviventes|voce viu mais alguem|tem gente por aqui|tem outras pessoas|voce viu alguem|mais alguem esta vivo|algum sobrevivente|tem mais alguem por ai',
  'all=sobreviventes,sobrevivente,mais alguem,outras pessoas,gente por aqui,pessoas por aqui,alguem vivo,gente viva,outros;tem,viu,algum,alguem,sabe,por ai,por aqui,existe|none=saqueadores,ladroes,perigosos,gente ruim,evitar,quantos de voces,seu grupo,mortos,infectados')
i('ASK_DANGER', 'e perigoso por aqui|tem algo que eu deva saber|o que tem la fora|esta seguro por aqui|essa area e segura|tem algo para eu tomar cuidado|esta feio la fora|e perigoso aqui',
  'all=perigoso,perigo,seguro por aqui,area segura,la fora,devo saber,deva saber,tomar cuidado,ameacas,arriscado,feio la fora,seguro aqui;e,o que,algo,algum,como,esta,tem|none=estrada,rodovia,noite,escuro,saqueadores,ladroes,horda,zumbi,dormir,rio,ponte,posto de controle,dirigir,quem,sobreviventes,alguem')
