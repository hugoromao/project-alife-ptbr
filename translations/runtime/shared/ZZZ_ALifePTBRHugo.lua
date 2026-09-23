-- PT-BR hooks for Project A-Life speech and chat. Loaded after the original
-- (ZZZ_ sorts last); every hook falls back to the original behaviour.
require "ProjectALife/Dialogue/ALifeDialogueData"
require "ProjectALife/Dialogue/ALifeSpeech"
require "ProjectALife/Talk/ALifeTalkIntents"
require "ProjectALife/Audio/ALifeAudioPolicy"
require "ALifePTBRHugo/Core"
require "ALifePTBRHugo/Chat"

local PT = ALifePTBRHugo
if PT.hooked then return PT end
PT.hooked = true

local Data = ProjectALife.DialogueData
local Speech = ProjectALife.Speech
local Intents = ProjectALife.TalkIntents
local t = PT.t

local function translateRecords(list)
    if type(list) ~= "table" then return end
    for _, record in ipairs(list) do
        if type(record) == "table" then
            record.t = t(record.t)
            if type(record.beats) == "table" then
                for _, beat in ipairs(record.beats) do
                    if type(beat) == "table" then beat.t = t(beat.t) end
                end
            end
        end
    end
end

-- Dialogue corpus (barks, talk replies, scenes, radio): translated in place once
-- per loaded data set, so every display path gets Portuguese.
function PT.translateData()
    if Data == nil or not Data.loaded or PT.translatedFor == Data.barks then return end
    PT.translatedFor = Data.barks
    for _, list in pairs(Data.barks or {}) do translateRecords(list) end
    for _, pools in ipairs({ Data.replies or {}, Data.yesPools or {}, Data.noPools or {} }) do
        for _, list in pairs(pools) do translateRecords(list) end
    end
    for _, scene in ipairs(Data.scenes or {}) do translateRecords(scene.turns) end
    for _, segment in ipairs(Data.segments or {}) do translateRecords(segment.lines) end
    Speech.intelCache = {}
    if PT.Chat ~= nil and type(PT.Chat.register) == "function" then PT.Chat.register(Data) end
end

if Data ~= nil and type(Data.load) == "function" then
    local originalLoad = Data.load
    function Data.load()
        local ok = originalLoad()
        PT.translateData()
        return ok
    end
    PT.translateData()
end

if Speech ~= nil then
    -- Templates from any other source ({found}, {town} ...) and Portuguese fallbacks
    -- for placeholders the caller did not fill.
    local originalRender = Speech.render
    function Speech.render(text, vars, shell)
        if type(text) ~= "string" then return originalRender(text, vars, shell) end
        text = t(text)
        if type(vars) == "table" then
            local translated = {}
            for key, value in pairs(vars) do
                translated[key] = type(value) == "string" and PT.value(value) or value
            end
            vars = translated
        end
        vars = PT.withDefaults(text, vars, shell)
        return PT.contract(originalRender(text, vars, shell))
    end

    -- Fixed lines written in the code (robbery, stances, reactions...).
    local originalSay = Speech.say
    function Speech.say(shell, text, options)
        return originalSay(shell, PT.caption(text), options)
    end
end

-- Voice captions and ambient gossip reach the screen through AudioPolicy.caption.
local Policy = ProjectALife.AudioPolicy
if Policy ~= nil and type(Policy.caption) == "function" then
    local originalCaption = Policy.caption
    function Policy.caption(text)
        return originalCaption(PT.caption(text))
    end
end

-- NPC shells are zombies; some modules call shell:Say directly with local line
-- tables (panic, holdout stances), so the Say method itself gets the caption.
local function hookShellSay()
    local ok = pcall(function()
        local meta = __classmetatables ~= nil and IsoZombie ~= nil and __classmetatables[IsoZombie.class] or nil
        local index = meta ~= nil and meta.__index or nil
        if type(index) ~= "table" or type(index.Say) ~= "function" or index.PTBRSay ~= nil then return end
        local originalSay = index.Say
        index.PTBRSay = originalSay
        index.Say = function(self, text, ...)
            return originalSay(self, PT.caption(text), ...)
        end
    end)
    return ok
end
hookShellSay()

if Intents ~= nil then
    local originalNormalize = Intents.normalize
    function Intents.normalize(text)
        return PT.Chat.expand(originalNormalize(PT.Chat.fold(tostring(text or ""))))
    end
    local originalClassify = Intents.classify
    function Intents.classify(text, pending, data)
        return originalClassify(PT.Chat.player(text), pending, data)
    end
    Intents.cache = {}
end

return PT
