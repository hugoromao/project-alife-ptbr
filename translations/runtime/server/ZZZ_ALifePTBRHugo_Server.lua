-- PT-BR, server side: module line tables that are shown with shell:Say directly,
-- bypassing Speech/AudioPolicy. Translated in place once the modules are loaded.
require "ZZZ_ALifePTBRHugo"
local PT = ALifePTBRHugo

local function translateList(list)
    if type(list) ~= "table" then return end
    for index, line in ipairs(list) do
        if type(line) == "string" then list[index] = PT.t(line) end
    end
end

local ok, Panic = pcall(require, "ProjectALife/Modules/ALifeModulePanic")
if ok and type(Panic) == "table" then
    translateList(Panic.gunFearLines)
    translateList(Panic.shotFearLines)
end

local function translateMap(map)
    if type(map) ~= "table" then return end
    for key, line in pairs(map) do
        if type(line) == "string" then map[key] = PT.caption(line) end
    end
end

local okCareful, Careful = pcall(require, "ProjectALife/Modules/ALifeModuleCareful")
if okCareful and type(Careful) == "table" then
    translateMap(Careful.fallbackWords)
    translateMap(Careful.heardWords)
end

local okRobbery, Robbery = pcall(require, "ProjectALife/Modules/ALifeModuleRobbery")
if okRobbery and type(Robbery) == "table" then
    translateMap(Robbery.fallbackWords)
    translateList(Robbery.standDownLines)
    translateList(Robbery.walkAwayLines)
end

local okStances, Stances = pcall(require, "ProjectALife/Modules/ALifeModuleStances")
if okStances and type(Stances) == "table" and type(Stances.holdoutLine) == "function" then
    local originalHoldoutLine = Stances.holdoutLine
    function Stances.holdoutLine(cue)
        return PT.caption(originalHoldoutLine(cue))
    end
end
