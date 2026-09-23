-- PT-BR, server side: module line tables that are shown with shell:Say directly,
-- bypassing Speech/AudioPolicy. Translated in place once the modules are loaded.
require "ZZZ_ProjectALifePTBR"
local PT = ProjectALifePTBR

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
