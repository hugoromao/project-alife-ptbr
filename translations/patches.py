# Code patches applied by tools/build.py to the translated upstream files, in order.
# Each patch: file (path under the version folder), find (exact text), replace, and
# count (expected number of matches; None = at least one). The build fails when a
# find text is missing, which is the signal that upstream changed that spot.
# Non-ASCII text inside string literals is escaped to \ddd bytes by the build.

CREATOR = 'media/lua/client/ProjectALife/UI/ALifeCreatorScreen.lua'
TALK_MENU = 'media/lua/client/ProjectALife/Talk/ALifeTalkMenu.lua'

CREATOR_HELPERS = '''-- PT-BR: labels are UTF-8 bytes. string.upper only knows ASCII, and Kahlua's
-- toUpperCase would turn the second byte of o-tilde (0xB5, micro sign) into a Greek
-- letter, so upper-case ASCII letters and the two-byte Latin-1 lowercase range by hand.
function Creator.upper(text)
    local s = string.gsub(tostring(text or ""), "[a-z]", string.upper)
    return (string.gsub(s, "\\195([\\160-\\190])", function(c)
        local b = string.byte(c)
        if b == 183 then return nil end
        return "\\195" .. string.char(b - 32)
    end))
end

-- PT-BR: display-only names; page ids and body-location ids stay English.
local PTBR_TAB_LABELS = {
    identity = "IDENTIDADE", appearance = "APARÊNCIA", faces = "ROSTOS", loadout = "EQUIPAMENTO",
    combat = "COMBATE", behavior = "COMPORTAMENTO", modules = "MÓDULOS",
}
function Creator.tabLabel(pageId)
    return PTBR_TAB_LABELS[pageId] or Creator.upper(pageId)
end

local PTBR_SLOT_LABELS = {
    Hat = "Chapéu", Eyes = "Olhos", Mask = "Máscara", Ears = "Orelhas", Faces = "Rosto", Neck = "Pescoço",
    Scarf = "Cachecol", Top = "Blusa", Jacket = "Jaqueta", Vest = "Colete", AmmoStrap = "Bandoleira", Hands = "Mãos",
    Wrist = "Pulso", Fingers = "Dedos", Underwear = "Roupa íntima", Pants = "Calça", Socks = "Meias", Shoes = "Calçados",
    Back = "Costas", LeftArm = "Braço esq.", RightArm = "Braço dir.", LeftForearm = "Antebraço esq.",
    RightForearm = "Antebraço dir.", LeftHand = "Mão esq.", RightHand = "Mão dir.", LeftWrist = "Pulso esq.",
    RightWrist = "Pulso dir.", LeftShin = "Canela esq.", RightShin = "Canela dir.", LeftGaiter = "Polaina esq.",
    RightGaiter = "Polaina dir.", Belt = "Cinto", Holster = "Coldre", ShoulderHolster = "Coldre de ombro",
    AnkleHolster = "Coldre de tornozelo", FannyPackFront = "Pochete (frente)", FannyPackBack = "Pochete (trás)",
    Necklace = "Colar", LongNecklace = "Colar longo", Nose = "Nariz", BellyButton = "Umbigo", LeftRing = "Anel esq.",
    RightRing = "Anel dir.", LeftMiddleRing = "Anel médio esq.", RightMiddleRing = "Anel médio dir.",
    UnderwearTop = "Roupa íntima (cima)", UnderwearBottom = "Roupa íntima (baixo)", LongJohnsTop = "Ceroula (cima)",
    LongJohnsBottom = "Ceroula (baixo)", TankTop = "Regata", Tshirt = "Camiseta", Sweater = "Suéter",
    ShoulderPads = "Ombreiras", Gorget = "Gorjal", Cuirass = "Couraça", Codpiece = "Protetor de virilha", Apron = "Avental",
    Tail = "Cauda", FullSuit = "Macacão", FullRobe = "Túnica", LeftGreave = "Greva esq.", RightGreave = "Greva dir.",
    LeftKnee = "Joelho esq.", RightKnee = "Joelho dir.", LeftThigh = "Coxa esq.", RightThigh = "Coxa dir.",
    LeftShoulder = "Ombro esq.", RightShoulder = "Ombro dir.", LeftElbow = "Cotovelo esq.", RightElbow = "Cotovelo dir.",
    Webbing = "Colete tático", BreathingGear = "Respirador", MakeUpFullFace = "Maquiagem (rosto)",
    MakeUpEyes = "Maquiagem (olhos)", MakeUpEyesShadow = "Sombra", MakeUpLips = "Batom",
}
function Creator.slotLabel(slot)
    return Creator.upper(PTBR_SLOT_LABELS[slot] or tostring(slot or ""):gsub("(%l)(%u)", "%1 %2"))
end

'''

PATCHES = [
    # Creator: helpers go right before the first function that needs them.
    {'file': CREATOR, 'find': 'function Creator.playUiSound(label)',
     'replace': CREATOR_HELPERS + 'function Creator.playUiSound(label)', 'count': 1},
    # Button sounds: also recognise the Portuguese confirm words.
    {'file': CREATOR, 'find': 'or text == "CONFIRM" or text == "YES" or text == "OK")',
     'replace': 'or text == "CONFIRM" or text == "YES" or text == "OK"\n'
                '            or text:find("APLICAR", 1, true) or text:find("CRIAR", 1, true)\n'
                '            or text:find("NOVO", 1, true) or text:find("NOVA", 1, true)\n'
                '            or text:find("CONCLUÍDO", 1, true) or text:find("SALVAR", 1, true)\n'
                '            or text == "CONFIRMAR" or text == "SIM")', 'count': 1},
    {'file': CREATOR, 'find': 'tabW, string.upper(pageId)', 'replace': 'tabW, Creator.tabLabel(pageId)', 'count': 1},
    {'file': CREATOR, 'find': 'string.upper(clothingSlot:gsub("(%l)(%u)", "%1 %2"))',
     'replace': 'Creator.slotLabel(clothingSlot)', 'count': 1},
    {'file': CREATOR, 'find': 'string.upper(clothingSlot)', 'replace': 'Creator.slotLabel(clothingSlot)', 'count': None},
    {'file': CREATOR, 'find': 'string.upper(slot)', 'replace': 'Creator.slotLabel(slot)', 'count': None},
    # Everything else the Creator upper-cases may now carry accents.
    {'file': CREATOR, 'find': 'string.upper(', 'replace': 'Creator.upper(', 'count': None},

    # Conversation window: topic buttons and the stance line.
    {'file': TALK_MENU, 'find': 'ProjectALife = ProjectALife or {}\n',
     'replace': 'ProjectALife = ProjectALife or {}\n\n'
                '-- PT-BR: display-only labels. Topic keys and stance ids stay English because the\n'
                '-- dialogue data and the server match on them.\n'
                'local PTBR_TOPIC_LABELS = { World = "Mundo", Personal = "Pessoal", Supplies = "Suprimentos" }\n'
                'local PTBR_STANCE_LABELS = { careful = "CAUTELOSO", friendly = "AMIGÁVEL", hostile = "HOSTIL", neutral = "NEUTRO" }\n',
     'count': 1},
    {'file': TALK_MENU, 'find': 'self.rowHeight, topic, self, Window.selectTopic)',
     'replace': 'self.rowHeight, PTBR_TOPIC_LABELS[topic] or topic, self, Window.selectTopic)', 'count': 1},
    {'file': TALK_MENU, 'find': 'self:drawText(string.upper(self.stance or ',
     'replace': 'self:drawText(PTBR_STANCE_LABELS[self.stance] or string.upper(self.stance or ', 'count': 1},
]
