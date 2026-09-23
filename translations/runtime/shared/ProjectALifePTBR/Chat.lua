-- PT-BR chat: lets NPCs understand what the player types in Portuguese.
-- The English matcher keeps working; this folds accents, expands common chat
-- abbreviations and registers Portuguese patterns on the existing intent ids.
local PT = ProjectALifePTBR
local Chat = PT.Chat or {}
PT.Chat = Chat

-- Latin-1 letters -> ASCII, keyed by the code point (0xC0-0xFF).
local FOLD = {}
local function map(chars, letter) for _, code in ipairs(chars) do FOLD[code] = letter end end
map({ 192, 193, 194, 195, 196, 197, 224, 225, 226, 227, 228, 229 }, "a")
map({ 199, 231 }, "c")
map({ 200, 201, 202, 203, 232, 233, 234, 235 }, "e")
map({ 204, 205, 206, 207, 236, 237, 238, 239 }, "i")
map({ 209, 241 }, "n")
map({ 210, 211, 212, 213, 214, 242, 243, 244, 245, 246 }, "o")
map({ 217, 218, 219, 220, 249, 250, 251, 252 }, "u")
map({ 221, 253, 255 }, "y")

-- Works whether the engine hands Lua UTF-8 bytes or one char per code point.
function Chat.fold(text)
    text = string.gsub(text, "\195([\128-\191])", function(c)
        return FOLD[string.byte(c) + 64] or " "
    end)
    text = string.gsub(text, "[\192-\255][\128-\191]+", " ")
    text = string.gsub(text, "[\192-\255]", function(c)
        return FOLD[string.byte(c)] or " "
    end)
    return text
end

Chat.expansions = {
    vc = "voce", vcs = "voces", ce = "voce", oce = "voce", tb = "tambem", tbm = "tambem",
    pq = "por que", porque = "por que", q = "que", oq = "o que", n = "nao", s = "sim", ss = "sim",
    blz = "beleza", vlw = "valeu", obg = "obrigado", brigado = "obrigado", td = "tudo", tds = "todos",
    cmg = "comigo", ctg = "contigo", msm = "mesmo", hj = "hoje", qdo = "quando", qnd = "quando",
    kd = "cade", pra = "para", pro = "para o", pras = "para as", pros = "para os", ta = "esta",
    to = "estou", tou = "estou", tamo = "estamos", tamos = "estamos", nd = "nada", ngm = "ninguem",
    mt = "muito", mto = "muito", agr = "agora", dps = "depois", flw = "falou", tmj = "tamo junto",
    mano = "cara", vei = "cara", velho = "cara", parca = "cara", uhum = "sim", aham = "sim",
    zumbis = "zumbi", mortos = "zumbi", mortosvivos = "zumbi", podres = "zumbi",
    kk = "haha", kkk = "haha", kkkk = "haha", kkkkk = "haha", rs = "haha", rsrs = "haha", huehue = "haha",
}

function Chat.expand(value)
    local words = {}
    for word in string.gmatch(value, "%S+") do
        words[#words + 1] = Chat.expansions[word] or word
    end
    return table.concat(words, " ")
end

-- In a Portuguese sentence "no" is "em + o", but the English matcher reads it as a
-- refusal. Only the player's text is rewritten (patterns go through normalize too),
-- and a lone "no" keeps meaning no.
function Chat.player(text)
    local s = " " .. string.lower(Chat.fold(tostring(text or ""))) .. " "
    local words = 0
    for _ in string.gmatch(s, "%a+") do words = words + 1 end
    if words < 2 then return text end
    for _ = 1, 2 do s = string.gsub(s, "([^%a])no([^%a])", "%1em o%2") end
    return s
end

-- Adds the Portuguese patterns once per loaded intent table.
function Chat.register(data)
    if data == nil or type(data.intent) ~= "function" or Chat.registeredFor == data.intents then return end
    local ok, intents = pcall(require, "ProjectALifePTBR/ChatIntents")
    if ok and type(intents) == "table" then
        for _, entry in ipairs(intents) do
            if data.intentById[entry[1]] ~= nil then
                data.intent(entry[1], 50, entry[2], entry[3] or "")
            end
        end
    end
    Chat.registeredFor = data.intents
end

return Chat
