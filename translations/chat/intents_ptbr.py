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
i('ASK_ZOMBIES_NEARBY', 'tem zumbi por aqui|tem muito zumbi perto daqui|onde estao os mortos|tem zumbi aqui|algum zumbi por perto|tem infectado por aqui|quantos zumbis tem por aqui|tem muitos deles por aqui',
  'all=zumbi,infectado,infectados,morto vivo,mortos,essas coisas,monstros,deles;por aqui,por perto,perto daqui,aqui,nessa area,onde estao,quantos,muitos,muito,na cidade,ali|none=horda,hordas,corpos,queimar,matar,lutar,barulho,noite,escuro,mordido,mordida,cura,voce esta infectado,virus,quantos de voces')
i('ASK_HORDE', 'viu alguma horda|tem um grupo grande deles|alguma horda|tem uma horda|voce viu uma horda|onde esta a horda|um bando enorme deles|tem algum grupo grande de zumbi',
  'all=horda,hordas,manada,enxame,grupo grande,bando enorme,multidao,centenas,milhares,montao;viu,tem,alguma,algum,onde,vindo,deles,de zumbi,ouviu,andando|none=de saqueadores,seu grupo,meu grupo,de pessoas,de sobreviventes,de ladroes')
i('ASK_RAIDERS', 'quem e perigoso|tem saqueadores|tem gente ruim por aqui|quem eu devo evitar|tem saqueador por aqui|tem gangue por aqui|de quem eu devo tomar cuidado|tem bandido por aqui',
  'all=saqueadores,saqueador,ladroes,ladrao,gangue,gangues,gente ruim,bandido,bandidos,vandalos,hostis,fora da lei,motoqueiros,criminosos,presos fugitivos,gente perigosa,evitar,quem e perigoso;tem,algum,alguma,quem,por aqui,devo,viu,la fora,cuidado,perto daqui|none=esconderijo,esconde,covil,onde eles,onde fica a gangue,acampamento deles,base deles')
i('ASK_DEN', 'onde estao os ladroes|onde esses saqueadores se escondem|onde e o esconderijo deles|onde estao os saqueadores|onde os ladroes ficam|onde e o acampamento deles|onde eles se escondem|para onde foram os caras que me roubaram',
  'all=ladroes,saqueadores,gangue,esconderijo deles,acampamento deles,base deles,se escondem,ficam,esconderijo,covil,me roubaram,os caras que;onde,para onde,qual caminho,sabe onde,achar,foram|none=seu acampamento,sua base,seu esconderijo,sua gangue,por que voce me roubou')
i('JOIN_REQUEST', 'posso ir com voce|posso ir com voces|posso entrar no grupo de voces|me leva com voces|posso entrar no seu grupo|me deixa entrar|posso me juntar a voces|me leva com voce|posso ir junto|me deixa ir com voce|tem lugar para mais um',
  'all=ir com voce,ir com voces,ir junto,me leva,entrar no seu grupo,me juntar,juntar a voces,viajar com voce,andar com voce,ficar com o seu grupo,lugar para mais um,fazer parte;posso,me deixa,da para,eu,me,por favor,quero,mais um|none=vem comigo,entra no meu grupo,nosso grupo,meu grupo,voce devia,junta com a gente,vem com a gente')
i('COME_WITH_ME', 'vem comigo|junta comigo|voce devia vir comigo|a gente devia se juntar|vamos nos juntar|quer entrar no meu grupo|vem com a gente|voce pode vir comigo',
  'all=vem comigo,vem com a gente,junta comigo,junta com a gente,entra no meu grupo,se juntar,nos juntar,fica comigo,viaja comigo,anda comigo,nosso grupo,meu grupo,fazer dupla;voce,a gente,devia,quer,vamos,vem,por favor,junto,juntos,pode|none=posso entrar,me deixa entrar,posso ir,me leva,seu grupo,nao me segue,fica longe,quantos')
i('FOLLOW_ME', 'me segue|segue eu|vem ca|vem por aqui|fica perto|me acompanha|segue minha lideranca|vamos embora daqui|vem logo|vem atras de mim',
  'all=me segue,segue,siga,por aqui,acompanha,fica perto,atras de mim,vem ca,vem para ca,comigo;me,aqui,perto,agora,rapido,anda,logo,por|none=nao me segue,para de me seguir,voce esta me seguindo,por que voce esta me seguindo,te seguir,vem comigo,zumbi por aqui')
i('WAIT_HERE', 'espera aqui|fica aqui|segura ai|espera|fica parado ai|aguenta ai|me espera|calma ai|peraí|pera',
  'all=espera,espere,fica,fique,segura,aguenta,aguarda,pera;aqui,por mim,ai,parado,um segundo,um minuto,um momento,quieto|none=posso ficar,ficar com voce,passar a noite,fique seguro,fica vivo,fica longe,fica firme,onde voce fica,esta noite,maos,nao aguento,nao vejo a hora,fica perto,aguenta firme')
i('GO_AWAY', 'vai embora|me deixa em paz|some daqui|cai fora|sai daqui|se afasta|fica longe de mim|vaza|some',
  'all=vai embora,me deixa em paz,deixa a gente em paz,some,cai fora,sai daqui,se afasta,afasta,fica longe,vaza,vai se foder,para de me seguir,nao me segue;me,de mim,daqui,agora,so,por favor,embora,longe|none=como eu saio,como a gente sai,sair do condado,sair de knox,saida,sair da cidade,vamos sair,a gente precisa sair,sair vivo')
i('STOP_FREEZE', 'parado|para ai|para ai mesmo|nao se mexe|alto la|fica onde esta|nem mais um passo|ninguem se mexe|parado ai',
  'all=parado,para ai,alto la,nao se mexe,fica onde esta,nem mais um passo,ninguem se mexe,fica quieto;ai,agora,voce,mesmo,onde esta,passo,quieto,se mexe|none=para de apontar,para de atirar,para de me seguir,por favor para,para o sangramento,ponto de onibus,para de chorar')
i('HANDS_UP', 'maos para cima|mao para cima|levanta as maos|maos ao alto|mostra as maos|coloca as maos para cima|maos onde eu possa ver|bota a mao na cabeca',
  'all=maos,mao;para cima,ao alto,levanta,mostra,onde eu possa ver,na cabeca,atras da cabeca|none=minhas maos,estou com as maos,mao na roda,lava as maos')
i('DROP_WEAPON', 'larga a arma|abaixa a arma|solta a arma|larga isso|coloca no chao|joga a arma no chao|solta isso|joga fora a arma',
  'all=larga,solta,joga,coloca no chao,no chao,abaixa a arma,poe no chao;arma,rifle,pistola,espingarda,faca,taco,machado,isso,essa,facao|none=larguei,eu solto,me larga,cai morto,abaixa a voz,sua mochila,o zumbi')
i('LOWER_WEAPON', 'abaixa essa arma|abaixa isso|abaixa a sua arma|abaixa o rifle|para de apontar isso para mim|calma com essa arma|aponta isso para outro lado|tira essa arma da minha cara|guarda isso|ei calma com isso|nao aponta para mim',
  'all=abaixa,apontar,apontando,aponta,da minha cara,calma com,cuidado com,guarda isso,guarda essa,mira;arma,rifle,isso,essa,para mim,pistola,espingarda,cano|none=para eles,nos zumbis,onde mirar,mira na cabeca,como eu miro,abaixa a voz')
i('DEMAND_ITEMS', 'isso e um assalto|e um assalto|perdeu perdeu|passa suas coisas|passa tudo|esvazia os bolsos|isso e um assalto|me da tudo|passa a mochila|larga a mochila|me passa tudo que voce tem',
  'all=passa,me da,esvazia,larga a,joga para mim,assalto,perdeu,entrega;suas coisas,tudo,bolsos,mochila,bolsa,dinheiro,equipamento,o que voce tem|none=pode me dar,poderia me dar,por favor me da,me da um,me da uma,me da um pouco,me devolve,sua arma')
i('THREATEN', 'vou te matar|vou atirar em voce|voce esta morto|nao me faz te machucar|eu vou te matar|voce vai morrer|voce ja era|vou acabar com voce',
  'all=matar,atirar em voce,machucar,morto,morrer,acabar com voce,estourar,furar,esfaquear,te bater,te enterrar,ja era;vou,eu vou,voce esta,voce vai,senao,me faz,ou eu|none=eu vou morrer,a gente vai morrer,nao me mata,nao atira,nao me machuca,nao vou te machucar,eu estou morto,voce esta morto?,mata eles,atira neles,como eu mato,estou machucado,os mortos,voce nao vai morrer')
i('INSULT', 'seu idiota|vai se foder|seu babaca|voce e inutil|vai a merda|seu imbecil|seu pedaco de merda|seu otario|seu burro|voce e um lixo')
i('COMPLIMENT', 'bela arma|voce parece durao|voce e gente boa|jaqueta legal|voce e legal|voce esta bem arrumado|gostei da sua jaqueta|belo tiro',
  'all=bela,belo,legal,maneiro,massa,irado,bacana,gostei da,gostei do,curti,durao,firmeza,bom tiro,belo tiro,mandou bem,bom trabalho,impressionante;arma,jaqueta,chapeu,bota,botas,rifle,tiro,roupa,caminhonete,carro,voce,sua,seu,faca,oculos|none=nao e legal,voce e bonita,voce e bonito,dia bonito,prazer em te conhecer,boa tentativa')
i('THANKS', 'obrigado|obrigada|valeu|brigado|muito obrigado|agradeco|te devo uma|obrigadao')
i('SORRY', 'desculpa|foi mal|nao foi por querer|foi sem querer|me desculpa|sinto muito|erro meu|opa')
i('I_AM_FRIENDLY', 'sou amigo|sou amiga|nao quero confusao|nao vou te machucar|venho em paz|sou de paz|nao sou uma ameaca|somos amigos|nao sou hostil',
  'all=amigo,amiga,amigos,em paz,de paz,sem confusao,nao quero confusao,nao vou te machucar,nao sou uma ameaca,nao sou hostil,do seu lado,nao sou saqueador,nao estou com eles;eu,sou,nos,somos,me,venho|none=voce e amigo,voce e amigavel,eles sao amigos,fogo amigo')
i('DONT_SHOOT', 'nao atira|nao atire|segura o fogo|por favor nao atira|cessar fogo|para de atirar|sou amigo nao atira|nao dispara',
  'all=atira,atire,atirar,atirando,fogo,dispara;nao,segura,para,cessar|none=por que voce esta atirando,por que voce atirou,como eu atiro,nao atira neles,devo atirar,atira neles,uma fogueira,acender o fogo')
i('CALM_DOWN', 'calma|relaxa|fica tranquilo|fica tranquila|sossega|calma ai|vai com calma|esfria a cabeca|respira')
i('SURRENDER', 'eu desisto|eu me rendo|ta bom voce venceu|voce venceu|chega|me rendo|bandeira branca|tudo bem voce ganhou',
  'all=me rendo,desisto,voce venceu,voce ganhou,bandeira branca,chega de briga;eu,nos,ta bom,tudo bem,beleza,voce,chega|none=nao desiste,nunca desista,devo desistir,nao vou desistir,se renda,desista de')
i('BEG', 'por favor nao me mata|por favor me deixa ir|eu tenho familia|nao me mata|por favor nao me machuca|eu tenho filhos|me poupa|me deixa viver',
  'all=nao me mata,nao me mate,me deixa ir,me deixa viver,me poupa,poupa minha vida,nao me machuca,piedade,misericordia,eu tenho familia,eu tenho filhos,te imploro;por favor,me,eu,minha|none=me deixa ir primeiro,me deixa ir com,me deixa ir buscar,me deixa ir ver')
i('NEGOTIATE', 'vamos conversar|a gente pode resolver isso|ninguem precisa morrer|podemos conversar sobre isso|nao precisa de violencia|da para conversar|ninguem precisa se machucar|vamos fazer um acordo',
  'all=conversar,resolver isso,resolver,ninguem precisa,acordo,trato,negociar,entrar num acordo,chegar num acordo,ser razoavel;a gente,vamos,podemos,da para,ninguem,nos,sobre isso,so|none=me conta uma historia,me fala de,papo furado,fala de voce,depois a gente conversa,com quem eu falo,para de falar,falar com seu lider')
i('BRIBE', 'eu te pago|te dou o que voce quiser|pega minhas coisas e me deixa ir|pode levar o que quiser|eu posso pagar|pode ficar com minhas coisas|leva tudo so me deixa ir|te dou dinheiro',
  'all=te pago,pagar,o que voce quiser,minhas coisas,leva tudo,pode levar,pode ficar com,dinheiro,grana;eu,te dou,posso,so,leva,me deixa ir,pode|none=me paga,voce paga,devolver,prestar atencao,o que voce quer')
i('GIVE_BACK', 'devolve minhas coisas|isso e meu|devolve minhas coisas agora|me devolve|devolve isso|voce roubou minhas|eu quero minhas coisas de volta|isso me pertence',
  'all=devolve,devolva,de volta,e meu,e minha,roubou,roubaram,pegou meu,pegou minha,me pertence;minhas,meu,minha,isso,quero,voce|none=por que voce,o que eu fiz,volta aqui,ja volto,para tras,cuidado atras,voltar ao normal,voltar para casa')
i('ASK_WHY_HOSTILE', 'por que voce esta atirando em mim|por que voce me roubou|o que eu te fiz|por que voce esta me atacando|por que voce atirou em mim|qual e o seu problema|por que voce esta fazendo isso|por que tanta hostilidade',
  'all=por que,o que eu fiz,o que eu te fiz,qual e o seu problema,qual o seu problema;atirando,atirou,roubou,roubando,atacando,atacou,machucar,bateu,fazendo isso,problema,hostil,bravo comigo,com raiva,me odeia,mirando em mim|none=como eu atiro,por que eles,por que tem')
i('ASK_WILL_ROB', 'voce vai me roubar|voce vai me matar|voce esta me roubando|voce vai me machucar|voce vai atirar em mim|vai me assaltar|voces vao me roubar|voces vao me matar',
  'all=roubar,roubando,assaltar,matar,machucar,atirar;voce vai,vai me,voce esta,voces vao,vao me;me,mim,a gente|none=eu vou,como eu,nao,atira neles,passa,assalto')
i('WARN_ZOMBIES', 'cuidado|atras de voce|zumbis vindo|eles estao aqui|eles estao vindo|la vem eles|estao chegando|eles estao bem atras da gente',
  'all=atras de voce,atras da gente,cuidado,vindo,chegando,la vem,em cima da gente,bem ali,estao aqui,olha atras,na sua esquerda,na sua direita,na janela,na porta,invadindo;zumbi,mortos,infectados,eles,essas coisas,horda,um,atras|none=o exercito,militares,a guarda,ajuda vindo,resgate,helicoptero,vindo de,vem comigo,estao vindo?,quando')
i('WARN_DANGER', 'corre|abaixa|tem atiradores|se protege|atirador|se abaixa|foge|corre que da tempo|procura cobertura|emboscada',
  'all=corre,corram,abaixa,se abaixa,cobertura,se protege,atirador,atiradores,tiroteio,estao atirando,emboscada,foge,fujam;agora,vai,ali,eles,atirando,vindo,para,cobertura,que|none=cuidado com,acabou,acabando,quem corre,loja de armas,tem saqueadores,calma,arma,abaixa isso,abaixa a voz')
i('ASK_SAFE_PLACE', 'onde posso dormir em seguranca|onde eu me escondo|tem algum abrigo por perto|onde posso dormir|tem uma casa segura|onde e seguro para dormir|onde posso descansar|algum lugar para eu me esconder',
  'all=dormir,esconder,escondo,casa segura,abrigo,descansar,passar a noite,me abrigar,ficar escondido;onde,algum lugar,lugar,algum,por perto,conhece,tem,bom lugar|none=seu acampamento,com voce,na sua,sua casa,voce dorme,esconderijo deles,eles,o resto,onde voce')
i('ASK_DIRECTIONS', 'onde fica muldraugh|como eu chego em|qual o caminho para|onde fica west point|que distancia fica|onde fica riverside|onde fica rosewood|qual o caminho para louisville|como eu chego a fort knox|onde fica march ridge',
  'all=onde fica,onde e,como eu chego,como a gente chega,como chegar,qual caminho,qual o caminho,que distancia,e longe,direcao,rota para,estrada para,caminho para,chegar em,chegar a,ir para;muldraugh,west point,riverside,rosewood,march ridge,louisville,brandenburg,irvington,ekron,valley station,fallas lake,echo creek,fort knox|none=o que aconteceu,e a,sobrou alguem,ainda existe,voce e de,voce veio de,cresceu,cidade natal')
i('ASK_WHERE_AM_I', 'onde eu estou|que cidade e essa|onde a gente esta|que lugar e esse|em que cidade a gente esta|que condado e esse|onde diabos eu estou|que rua e essa',
  'all=onde,que,qual;eu estou,a gente esta,estamos,cidade e essa,lugar e esse,condado e esse,rua e essa,estrada e essa,que cidade,essa cidade|none=indo,vai,chegar,como,aconteceu,seu acampamento')
i('ASK_ROAD_SAFE', 'a estrada e segura|a rodovia esta livre|da para passar de carro|a estrada esta livre|a 31w esta livre|a dixie highway e segura|da para passar pela estrada|a interestadual esta bloqueada',
  'all=estrada,estradas,rodovia,interestadual,31w,dixie,rua,passar de carro;segura,livre,bloqueada,aberta,passar,congestionada,perigosa,carros|none=posto de controle,bloqueio,soldados,exercito,qual caminho,como eu chego,onde fica')
i('ASK_WEATHER', 'vai chover|esta quente hoje|como esta o tempo|vem tempestade|vai ter tempestade|que calor|faz frio a noite|como vai estar o tempo amanha',
  'all=chuva,chover,chovendo,tempo,tempestade,trovao,quente,frio,calor,previsao,sol,nuvens,vento,tornado;vai,esta,como,hoje,esta noite,amanha,parece,vem|none=cachorro quente,sangue frio,voce e quente,quanto tempo,tempo livre')
i('ASK_TIME', 'que horas sao|que hora e|tem horas|sabe que horas sao|que horas sao agora|ja e tarde|quantas horas',
  'all=horas,hora;que,quantas,sabe,tem,e|none=faz horas,hora de,muito tempo,ultima vez,proxima vez,que dia,data')
i('ASK_DATE', 'que dia e hoje|qual a data|que data e hoje|que mes e esse|que dia da semana e hoje|ainda e julho|hoje e que dia',
  'all=data,dia,hoje,mes,segunda,terca,quarta,quinta,sexta,sabado,domingo,julho,agosto,calendario;que,qual,e,sabe|none=quantos dias,bom dia,dia bonito,dia longo,todo dia,um dia,que horas,fazendo hoje,chuva,quente,tempo,perigoso')
i('ASK_NIGHT', 'e seguro a noite|eles saem a noite|e o escuro|eles ficam piores a noite|devo viajar a noite|o que acontece a noite|eles enxergam no escuro|e perigoso depois que escurece',
  'all=noite,escuro,escurece,anoitecer,por do sol;seguro,perigoso,saem,piores,viajar,acontece,enxergam,e o,andar,sair,cacam,ativos,rapidos|none=boa noite,ontem a noite,ficar com voce,dormir no seu,passar a noite')
i('ASK_HOW_KILL', 'como mata eles|como eu luto com eles|tiro na cabeca|como eu mato eles|tiro na cabeca funciona|qual o melhor jeito de matar eles|como derruba eles|onde eu miro',
  'all=matar,mata,mato,lutar,luto,derrubar,derruba,acabar com,tiro na cabeca,mirar,miro,atirar neles;como,qual,melhor jeito,funciona,onde;eles,zumbi,infectados,mortos,essas coisas,cabeca,um|none=te matar,me matar,vou matar,lutar com voce,atirar em voce,abaixa a arma')
i('ASK_ADVICE', 'alguma dica|algum conselho|como eu fico vivo|tem algum conselho|o que eu devo fazer|me da um conselho|como eu sobrevivo|dicas de sobrevivencia',
  'all=dica,dicas,conselho,conselhos,ficar vivo,fico vivo,sobreviver,sobrevivo,o que eu devo fazer,o que eu faco,sugestao,licao;algum,alguma,tem,me da,como,o que,voce tem,devo,ensina|none=como voce,como voce ainda,com os corpos')
i('ASK_FOOD', 'voce tem comida|tem comida sobrando|preciso de comida|tem algo para comer|tem alguma coisa para comer|posso pegar um pouco de comida|me arruma comida|tem comida|me da comida',
  'all=comida,comer,rango,lanche,refeicao,enlatado,feijao,lata de,bolacha,biscoito,pao,racao,alguma coisa para comer,algo para comer;voce tem,tem,sobrando,posso,preciso,me da,me arruma,divide,algum,alguma,poderia|none=eu tenho comida,eu trouxe,para voce,toma isso,pega isso,aqui esta,voce quer,voce esta com fome,eu posso te dar,favorita,favorito,comeria,vontade de comer,onde posso,onde tem,onde fica,plantar,trocar')
i('ASK_WATER', 'voce tem agua|a agua e segura|onde eu consigo agua|tem agua|posso pegar um pouco de agua|a agua da torneira e segura|a agua ainda esta saindo|tem agua sobrando',
  'all=agua,cantil,agua potavel,algo para beber;voce tem,tem,sobrando,posso,onde,a,segura,preciso,saindo,limpa,ferver,beber,achar|none=eu tenho agua,para voce,toma isso,aqui esta,voce quer,rio,barco,nadar,whisky,cerveja,cachaca')
i('ASK_MEDS', 'voce tem remedio|tem atadura|voce tem antibiotico|tem analgesico|tem algum comprimido|voce tem kit de primeiros socorros|preciso de atadura|pode me arrumar algum remedio',
  'all=remedio,remedios,medicamento,suprimentos medicos,atadura,ataduras,bandagem,curativo,antibiotico,antibioticos,analgesico,comprimido,comprimidos,aspirina,primeiros socorros,desinfetante,gaze,tala,pontos,morfina;voce tem,tem,algum,alguma,sobrando,preciso,posso,pode,me da,me arruma|none=eu tenho remedio,para voce,toma isso,aqui esta,voce quer,onde fica,onde posso,hospital,medico')
i('ASK_AMMO', 'tem municao|pode me arrumar umas balas|alguma municao|voce tem municao|preciso de municao|tem cartucho|me da umas balas|tem bala sobrando',
  'all=municao,balas,bala,cartucho,cartuchos,pente,pentes,carregador,carregadores,9mm,chumbo;tem,algum,alguma,sobrando,voce tem,preciso,posso,me da,me arruma,divide,pouca,acabou|none=eu tenho municao,para voce,toma isso,aqui esta,voce quer,onde posso achar,onde fica,loja de armas,quantas balas voce')
i('ASK_WEAPON', 'posso pegar uma arma|voce tem uma arma para mim|me da uma arma|tem uma arma sobrando|pode me emprestar uma arma|preciso de uma arma|tem algo para eu lutar|pode me dar uma faca',
  'all=arma,rifle,pistola,espingarda,faca,taco,machado,facao,revolver,algo para lutar;posso pegar,voce tem,sobrando,me da,me empresta,emprestar,preciso,tem uma,tem alguma,para mim,pode me dar|none=larga,abaixa,no chao,bela arma,loja de armas,onde posso achar,onde fica,municao,balas,aponta,apontando,eu tenho uma arma,para voce,toma isso,sua arma,seu rifle,sua faca')
i('ASK_SMOKE', 'tem um cigarro|tem cigarro|tem fogo|me arruma um cigarro|voce fuma|tem isqueiro|tem fosforo|me da um cigarro',
  'all=cigarro,cigarros,fumo,fumar,fuma,isqueiro,fosforo,fosforos,tabaco,charuto,maco,fogo;tem,sobrando,me arruma,me da,voce,algum,posso|none=vi fumaca,fumaca subindo,a fumaca,incendio,queimando,fogo na')
i('ASK_DRINK', 'tem bebida|quer uma cerveja|tem whisky|tem uma cerveja|voce bebe|tem alcool|quer beber alguma coisa|tem algo mais forte|tem cachaca',
  'all=bebida,cerveja,cervejas,whisky,uisque,bourbon,licor,alcool,cachaca,pinga,vodka,vinho,gelada,beber,algo mais forte,rum;tem,quer,voce,algum,alguma,divide,sobrando,bora|none=agua,alcool em gel,refrigerante,cafe')
i('ASK_CAR_FUEL', 'voce tem carro|tem gasolina|onde eu acho combustivel|tem combustivel|voce tem um carro|onde eu consigo gasolina|voce tem caminhonete|tem posto de gasolina',
  'all=carro,caminhonete,caminhao,veiculo,gasolina,combustivel,diesel,posto de gasolina,galao,van;voce tem,tem,algum,onde,preciso,posso,acho,consigo,sabe,funcionando|none=mascara de gas,gas lacrimogeneo,no carro com voce,carona,porta,trancado')
i('ASK_TRADE', 'quer trocar|podemos trocar|tenho coisas para trocar|vamos trocar|voce faz troca|voce negocia|quer fazer uma troca|voce vende alguma coisa',
  'all=trocar,troca,escambo,negocia,negociar,comerciante,vender,vende,comprar,compra;quer,podemos,voce,tenho,vamos,fazer,alguma,coisas')
i('OFFER_ITEM', 'vou te dar comida|toma isso|posso te dar alguma coisa|pega isso|aqui esta|isso e para voce|tenho comida para voce|quer um pouco de comida|toma',
  'all=toma isso,pega isso,toma,aqui esta,para voce,te dou,te dar,fica com isso,pode ficar,quer um pouco,trouxe para voce,voce precisa disso;comida,agua,isso,um pouco,municao,remedio,atadura,arma,alguma coisa,cerveja,cigarro,lata|none=o que eu posso fazer por voce,te ajudar,me devolve,me da,devolver,vai com calma,voce quer morrer,o que voce quer,trocar,vou te matar,vou atirar')
i('ASK_NEED', 'do que voce precisa|voce precisa de alguma coisa|precisa de algo|o que voce esta procurando|tem algo que voce precise|esta faltando o que|voce precisa de algo|o que eu posso te arrumar',
  'all=precisa,precise,procurando,faltando,acabando;o que voce,voce,alguma coisa,algo,do que|none=ajuda,eu preciso,precisa de medico,precisa que eu,a gente precisa,precisa saber,procurando meu,procurando minha')
i('OFFER_HELP', 'voce precisa de ajuda|posso te ajudar|eu posso ajudar|quer uma mao|deixa eu te ajudar|quer ajuda|eu posso te ajudar|como eu posso ajudar',
  'all=ajuda,ajudar,uma mao,dar uma mao;posso,eu posso,deixa eu,voce precisa,precisa de,quer,como eu posso,eu vou|none=me ajuda,ajuda a gente,pode me ajudar,por favor ajuda,eu preciso,preciso da sua ajuda,alguem ajuda,nao posso ajudar')
i('ASK_HELP', 'voce pode me ajudar|preciso de ajuda|por favor ajuda|me ajuda|socorro|alguem me ajuda|preciso da sua ajuda|poderia me ajudar',
  'all=ajuda,ajudar,socorro,uma mao;me,eu preciso,por favor,a gente,poderia,pode,preciso da sua,alguem|none=posso ajudar,deixa eu ajudar,eu posso ajudar,te ajudar,voce precisa de ajuda,como posso ajudar,quer ajuda')
i('ASK_TOOLS', 'tem ferramenta|preciso de um martelo|onde eu acho um pe de cabra|voce tem martelo|tem pe de cabra|onde acho ferramentas|preciso de um serrote|voce tem caixa de ferramentas',
  'all=ferramenta,ferramentas,martelo,pe de cabra,chave inglesa,chave de fenda,caixa de ferramentas,pregos,alicate,pa,marreta,furadeira,fita silver tape,parafusos,alicate de corte,serra,serrote,macarico;tem,preciso,voce tem,onde,acho,algum,alguma,empresta,sobrando|none=para voce,toma isso,aqui esta')
i('ASK_LOOT_SPOT', 'onde eu acho suprimentos|tem algum lugar bom para saquear|onde tem uma loja|onde eu posso saquear|onde fica o mercado|algum lugar bom para vasculhar|onde eu acho comida|onde fica a loja mais perto',
  'all=suprimentos,saquear,saque,vasculhar,loja,lojas,mercado,supermercado,armazem,farmacia,posto de gasolina,loja de ferragens,achar comida,achar coisas,casas para vasculhar,lanchonete;onde,algum lugar,bom,conhece,mais perto,qual,tem|none=loja de armas,hospital,seu acampamento,acampamento deles,voce tem,tem algum')
i('ASK_GUN_STORE', 'onde fica a loja de armas|onde eu acho armas|tem loja de armas por aqui|onde eu consigo uma arma|tem alguma loja de armas|onde voce arrumou sua arma|onde eu acho um rifle|onde tem arma',
  'all=loja de armas,armeria,armas,arsenal,artigos esportivos,loja de penhores,rifles,estande de tiro;onde,tem,alguma,acho,consigo,sabe,mais perto|none=larga,abaixa,no chao')
i('ASK_HOSPITAL', 'onde fica o hospital|tem medico|tem algum medico por aqui|tem clinica|onde eu acho um medico|o hospital ainda funciona|onde fica o hospital mais perto|tem farmacia',
  'all=hospital,medico,medicos,clinica,enfermeira,enfermeiro,pronto socorro,posto de saude,enfermaria,farmacia,ambulancia;onde,tem,algum,acho,mais perto,funciona,aberto,por aqui,sabe|none=eu preciso de um medico,eu sou medico,eu era medico,eu sou enfermeiro,voce e medico,voce era medico')

# --- part 3: places, answers, greetings, personal questions -----------------------
i('ASK_CHURCH', 'tem igreja|alguem rezando junto|onde fica a igreja|tem alguma igreja por aqui|onde eu posso rezar|as pessoas ainda vao na igreja|alguem esta fazendo culto|cade a igreja',
  'all=igreja,igrejas,capela,culto,missa,congregacao,rezar junto,rezando junto,pastor,padre,ministro;tem,onde,alguma,alguem,sabe,ainda,achar,posso|none=posto de gasolina,voce vai na igreja,voce reza')
i('ASK_FARM', 'tem fazenda por aqui|da para plantar comida|tem alguma fazenda|onde ficam as fazendas|da para plantar|alguem plantando por aqui|voce planta sua comida|tem criacao de animal por aqui',
  'all=fazenda,fazendas,sitio,plantar,plantando,plantacao,colheita,horta,sementes,gado,vacas,galinhas,celeiro,milharal;tem,onde,da para,posso,voce,alguem,por aqui,como|none=cresci,crescer,usina')
i('ASK_RIVER', 'e o rio|da para sair de barco|tem barco|da para atravessar o rio|e o rio ohio|da para nadar ate o outro lado|o rio esta vigiado|alguem atravessando o rio',
  'all=rio,rio ohio,barco,barcos,canoa,balsa,jangada,nadar,atravessar,cais,marina,caiaque;e o,da para,posso,tem,sair,atravessando,de,vigiado,algum,como,seguro|none=riverside')
i('ASK_OUTPOST', 'tem algum acampamento por aqui|tem algum assentamento|tem algum lugar murado|existe alguma comunidade|tem algum complexo perto|alguem fortificado por aqui|tem acampamento de sobreviventes|tem alguma colonia',
  'all=acampamento,acampamentos,assentamento,assentamentos,murado,murada,complexo,fortificado,comunidade,colonia,posto avancado,fortaleza,barricada;tem,algum,alguma,por aqui,perto,existe,sabe,onde|none=seu acampamento,acampamento deles,saqueadores,ladroes,refugiados,fort knox,zona segura,fema,dormir no seu')
i('ASK_CHECKPOINT', 'e esse posto de controle|a ponte esta bloqueada|quem esta no bloqueio|quem esta no posto de controle|da para passar pelo posto de controle|a ponte esta aberta|o que tem no bloqueio|por que tem um bloqueio',
  'all=posto de controle,bloqueio,bloqueios,barricada,barreira,ponte;o que,quem,esta,da para,bloqueada,aberta,passar,vigiando,por que,e esse|none=como eu chego,o que aconteceu em louisville')
i('ASK_LOCKED_DOOR', 'voce consegue abrir isso|voce tem a chave|tem a chave|consegue destrancar isso|abre a porta|consegue arrombar essa fechadura|essa porta esta trancada|como eu abro isso',
  'all=chave,chaves,tranca,trancada,trancado,destrancar,abrir isso,abre a porta,abrir a porta,arrombar,fechadura,porta,portao;voce consegue,consegue,voce tem,tem,como eu,essa,ajuda,abre,abrir|none=chave do carro,bate,batendo,na porta,invadindo,fecha a porta,fala baixo')
i('YES', 'sim|claro|pode ser|com certeza|bora|fechado|positivo|demorou|por que nao|claro que sim|conta comigo|pode crer|sim senhor|sim por favor|beleza entao vamos|vamos nessa')
i('NO', 'nao obrigado|agora nao|de jeito nenhum|negativo|nem pensar|nao quero|nem a pau|estou fora|nunca|nao valeu|dispenso|melhor nao|claro que nao|nao nao|nao senhor|acho que nao|nao da')
i('MAYBE', 'talvez|sei la|nao sei|pode ser que sim|vou pensar|nao tenho certeza|depende|quem sabe|veremos|acho que sim')
i('REPEAT', 'repete|repete ai|fala de novo|nao entendi|o que voce disse|nao ouvi|como assim|fala mais alto|hein|como e que e|pode repetir')
i('OK_ACK', 'entendi|entendido|certo entao|esta certo|beleza entao|esta bom entao|saquei|faz sentido|anotado|copiado|positivo e operante|justo')
i('GREETING', 'oi|ola|opa|e ai|salve|bom dia|boa tarde|boa noite amigo|fala ai|eai|oi amigo|ola amigo|tudo bem')
i('FAREWELL', 'tchau|ate mais|ate logo|falou|flw|se cuida|fica bem|fica seguro|boa sorte|ate a proxima|preciso ir|tenho que ir|adeus')
i('THANKS', 'muito obrigado mesmo|valeu mesmo|deus te abencoe|voce salvou minha vida|agradeco muito|obrigadao|brigadao|valeu cara')
i('LAUGH', 'hehe|hahahaha|muito engracado|voce e engracado|hilario|morri de rir|kkkkkk|kkkkkkk')
i('INSULT', 'cala a boca|perdedor|voce e um lixo|vai para o inferno|voce e um idiota|covarde|voce e burro|seu inutil|vai se ferrar|arrombado')
i('SWEAR_VENT', 'filho da puta|inferno na terra|que se dane|pelo amor de deus|eu odeio isso|isso e uma merda|que se foda|puta merda|meu deus do ceu|ai meu deus')
i('CALM_DOWN', 'respira|todo mundo calmo|so relaxa|respira fundo|calma calma|nao precisa entrar em panico|mantem a calma|pega leve|sem panico')
i('SORRY', 'peco desculpas|me perdoa|desculpa por isso|foi um acidente|nao quis te acertar|nao foi de proposito|acidente|culpa minha|mil desculpas')
i('HOW_ARE_YOU', 'como voce esta|como voce esta aguentando|como vai|tudo bem com voce|como vao as coisas|como voce tem passado|voce esta bem|beleza com voce|tudo certo',
  'all=como,tudo bem,tudo certo,beleza;voce esta,vai,vao as coisas,voce tem passado,aguentando,com voce,voce se sente|none=velho,vivo,sobreviveu,quanto tempo,quantos,longe,chego,matar,dormir,medo')
i('ASK_NAME', 'qual e o seu nome|qual o seu nome|seu nome|como voce se chama|como te chamam|como eu te chamo|tem nome|qual e a sua graca',
  'all=nome,se chama,te chamam,te chamo;seu,sua,voce,qual,como|none=meu nome,me chamo,me chamam,nome dessa cidade,nome da cidade,nome da rua')
i('TELL_NAME', 'meu nome e|eu me chamo|me chama de|me chamam de|pode me chamar de|o nome e|sou o|sou a',
  'all=nome,me chamo,me chama,me chamam,chamar de;meu,me,eu,pode|none=seu nome,qual,como voce,te chamam,chama ajuda,chama a policia')
i('WHO_ARE_YOU', 'quem e voce|quem diabos e voce|quem sao voces|quem esta ai|quem porra e voce|se identifica|quem vem la|voce e o que',
  'all=quem;e voce,sao voces,esta ai,vem la,e esse,e essa|none=com quem,trabalha para,no comando,lider,chefe,anda com,amigo de,se chama')
i('ASK_GROUP', 'com quem voce anda|que grupo e esse|de que faccao voce e|para quem voce trabalha|com quem voce esta|voce e de que grupo|com quem voce roda|voce esta com alguem',
  'all=grupo,faccao,bando,equipe,turma,trabalha para,de que lado,unidade,anda com,esta com alguem,faz parte;quem,que,qual,voce|none=entrar,vem comigo,meu grupo,nosso grupo,lider,chefe,no comando,quantos,onde,tamanho')
i('ASK_LEADER', 'quem manda aqui|quem esta no comando|quem e o seu chefe|me leva ao seu lider|quem comanda isso|quem e o lider|quem da as ordens|quem e o seu lider',
  'all=manda,comando,chefe,lider,comanda,da as ordens,patrao;quem,me leva,onde esta,cade,posso falar|none=eu sou o,eu mando,meu chefe,eu comando,eu era')
i('ASK_HOW_MANY', 'quantos voces sao|quantos de voces tem|quantas pessoas tem no seu grupo|quantos sao|qual o tamanho do seu grupo|quantos tem no grupo|quantos caras voce tem|quanta gente voces tem',
  'all=quantos,quantas,quanta,tamanho;voces,seu,sua,grupo,pessoas,caras,membros,gente,turma,sao|none=balas,municao,zumbi,infectados,mortos,dias,semanas,criancas,filhos,anos,matou,horda,corpos')
i('ASK_BASE', 'onde fica o seu acampamento|onde e o seu acampamento|onde voce mora|onde fica a sua base|onde voce fica|onde voces estao entocados|onde voce dorme|onde e a sua casa',
  'all=onde;acampamento,base,mora,moram,entocados,fica,ficam,casa,esconderijo,dorme,dormem,complexo;voce,voces,seu,sua|none=de onde,cidade natal,cresceu,nasceu,esta noite,posso ficar,posso dormir,deles,saqueadores,ladroes,indo,vai')
i('ASK_PLANS', 'qual e o plano|qual o plano|o que voce esta fazendo|o que voce anda aprontando|o que voce esta fazendo aqui|e agora|qual e o seu plano|o que voces estao planejando',
  'all=plano,planos,planejando,aprontando,fazendo aqui,fazendo por aqui,proximo passo,vai fazer,e agora;o que,qual,entao,seu,sua,o|none=onde,como eu,antes,trabalho,vida,costumava,corpos,com essa arma,dormir')
i('ASK_DESTINATION', 'para onde voce vai|para onde voce esta indo|aonde voce vai|onde voce esta indo|para onde voces vao|para onde e a viagem|voce vai para onde|vai para onde',
  'all=onde,aonde;vai,vao,indo,rumo,viajando,caminhando,dirigindo,seguindo;voce,voces,seu,grupo,a gente|none=devo,eu vou,como eu,eu estou indo,chegar,vai chover,esta acontecendo')
i('ASK_ORIGIN_TODAY', 'de onde voce veio|onde voce estava|de onde voce esta vindo|voce veio de onde|de onde voces vieram|onde voce andou|voce estava onde|veio por qual caminho',
  'all=onde,qual caminho;veio,vieram,vindo,estava,estavam,andou,chegou de|none=nasceu,cresceu,cidade natal,originalmente,isso veio,eles vieram,barulho,som')
i('ASK_HOMETOWN', 'de onde voce e|voce e daqui|voce e de onde|onde e sua casa|voce e de onde originalmente|voce e daqui mesmo|onde voce cresceu|voce e da regiao',
  'all=de onde,daqui,da regiao,cresceu,nasceu,cidade natal,terra natal;voce,e,originalmente,mesmo|none=veio,vieram,vindo,hoje,agora,helicoptero,barulho,som')
i('ASK_JOB_BEFORE', 'o que voce fazia antes de tudo isso|qual era o seu trabalho|o que voce fazia antes|voce trabalhava com o que|qual era a sua profissao|voce tinha emprego|voce trabalhava onde|o que voce fazia da vida',
  'all=trabalho,trabalhava,emprego,profissao,carreira,fazia antes,fazia da vida,ganhava a vida,era policial,era soldado,era enfermeira,era professor,era fazendeiro,era caminhoneiro,era mecanico,era medico;o que,voce,qual,seu,sua|none=eu trabalhava,meu trabalho,eu era,funciona,vai funcionar')
i('ASK_FAMILY', 'voce tem familia|onde esta sua familia|voce esta sozinho|voce esta sozinha|tem familia|e so voce|cade sua familia|onde estao seus pais',
  'all=familia,esposa,marido,mulher,pais,mae,pai,irmao,irma,sozinho,sozinha,parentes,so voce;voce,sua,seu,seus,tem|none=minha esposa,meu marido,minha familia,minha mae,meu pai,meus pais,eu tenho familia,eu perdi,estou sozinho,me deixa em paz,filhos,filho,filha,criancas')
i('ASK_KIDS', 'voce tem filhos|tem criancas|voce tem filho|cade seus filhos|onde estao seus filhos|voce tem criancas|voce tem neto',
  'all=filhos,filho,filha,filhas,criancas,crianca,bebe,netos,neto;voce,seus,sua,seu,tem|none=meus filhos,meu filho,minha filha,meu bebe,eu tenho filhos,brincadeira')
i('ASK_PETS', 'voce tem cachorro|viu algum cachorro|tem bicho de estimacao|voce tem gato|voce viu um cachorro|viu meu cachorro|tem algum animal|voce tem um cao',
  'all=cachorro,cachorros,cao,caes,gato,gatos,filhote,bicho de estimacao,animal,cavalo,cavalos;voce,seu,tem,viu,meu,algum|none=cachorro quente,filho da puta,cansado,racao')
i('ASK_AGE', 'quantos anos voce tem|qual a sua idade|voce e velho|voce e velha|quando voce nasceu|em que ano voce nasceu|que idade voce tem|quantos anos',
  'all=anos,idade,velho,velha,nasceu;quantos,qual,quando,que,sua,voce|none=anos de idade,eu tenho,velho demais,velhos tempos,mundo antigo,vida antiga,onde')
i('ASK_HOW_SURVIVED', 'como voce sobreviveu|como voce ainda esta vivo|como voce ainda esta viva|como voce conseguiu|como voce chegou ate aqui|como voce saiu|como voce aguentou|como voces sobreviveram',
  'all=sobreviveu,sobreviveram,sobreviver,vivo,viva,conseguiu,conseguiram,aguentou,chegou ate aqui,saiu;como;voce,voces|none=a gente vai,eu consigo,como eu,ficar vivo,eu vou')
i('ASK_HOW_LONG', 'faz quanto tempo que voce esta aqui|quanto tempo faz|quanto tempo ja|quantos dias ja|faz quanto tempo que isso comecou|ha quanto tempo voce esta por ai|quantos dias faz|desde quando',
  'all=quanto tempo,quantos dias,quantas semanas,desde quando,ha quanto tempo;faz,ja,esta,comecou,passou,atras,por ai,aqui|none=leva para,para chegar,andar,dirigir,ate,vai durar,esperar')
i('ASK_SCARED', 'voce esta com medo|voce nao tem medo|voce tem medo|isso te assusta|voce fica com medo|voce nao fica com medo|esta com medo|voces estao com medo',
  'all=medo,assusta,assustado,assustada,apavorado,nervoso,nervosa;voce,voces,te|none=eu estou com medo,eu tenho medo,estou com medo,estou apavorado,me assustou,nao tenha medo,sem medo')
i('ASK_OKAY', 'voce esta bem|voce se machucou|tudo bem com voce|voce esta ferido|voce esta ferida|voce esta machucado|voce esta ok|ta tudo bem',
  'all=machucou,machucado,machucada,ferido,ferida,sangrando,bem,ok;voce esta,voce se,com voce,esta tudo,voces estao|none=estou machucado,estou sangrando,estou ferido,nao vou te machucar,eu estou bem')
i('ASK_BITTEN', 'voce foi mordido|voce foi mordida|voce esta infectado|voce esta infectada|eles te morderam|mostra seus bracos|voce levou mordida|te morderam',
  'all=mordido,mordida,morderam,mordeu,infectado,infectada,arranhado,arranhada,febre,bracos;voce,te,mostra,voces|none=fui mordido,me mordeu,estou infectado,meu braco,minha perna,mordida de comida,maos para cima,tem infectado,infectados por perto')
