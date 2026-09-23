-- Classify sample phrases with the built PT-BR chat. Usage: tools/chat_try.sh "frase" ...
local build, upstream = arg[1], arg[2]
package.path = build .. "/media/lua/shared/?.lua;" .. upstream .. "/media/lua/shared/?.lua;" .. package.path
require "ZZZ_ALifePTBRHugo"
local Intents = ProjectALife.TalkIntents
ProjectALife.DialogueData.load()
for i = 3, #arg do
    local id, score = Intents.classify(arg[i], false)
    print(string.format("%-45s -> %s (%s)", arg[i], tostring(id), tostring(score)))
end
