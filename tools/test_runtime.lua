-- Runs the original Project A-Life speech/chat modules with the PT-BR hooks from
-- build/ on stock Lua 5.1. Usage: tools/test_runtime.sh
local build, upstream = arg[1], arg[2]
package.path = build .. "/media/lua/shared/?.lua;" .. upstream .. "/media/lua/shared/?.lua;" .. package.path
local failures = 0
local function check(name, got, want)
    if got == want then print("ok   " .. name)
    else failures = failures + 1; print("FAIL " .. name .. "\n     got:  " .. tostring(got) .. "\n     want: " .. tostring(want)) end
end

-- test dictionary and chat patterns, installed before the hooks load
package.preload["ProjectALifePTBR/Speech/Index"] = function() return { parts = 1 } end
package.preload["ProjectALifePTBR/Speech/Part1"] = function() return function(D)
    D["First quiet all day. I don't trust it, but I'll take it."] = "Primeiro sil\195\170ncio do dia. N\195\163o confio, mas aceito."
    D["Stay right there. Don't move a muscle."] = "Fica a\195\173 mesmo. N\195\163o mexe um m\195\186sculo."
    D["Saw a crew near {town} on {date}, around {time}."] = "Vi um bando perto de {town} em {date}, l\195\161 pelas {time}."
    D["Grabbing this {found}."] = "Vou pegar {found}."
    D["The robbers sleep at {den}."] = "Os ladr\195\181es dormem em {den}."
    D["the school"] = "a escola"
    D["He's got a gun -- move!"] = "Ele t\195\161 armado -- corre!"
    return 8 end end
package.preload["ProjectALifePTBR/ChatIntents"] = function() return {
    { "ASK_FOOD", "voce tem comida|tem comida sobrando|tem algo para comer", "" },
    { "YES", "sim|claro|pode ser", "" }, { "NO", "nao|agora nao", "" } } end

require "ZZZ_ProjectALifePTBR"
local Data, Speech, Intents = ProjectALife.DialogueData, ProjectALife.Speech, ProjectALife.TalkIntents
Speech.adapters.clock = function() return { year = 1993, month = 7, day = 9, hour = 15, daysSurvived = 3 } end
Speech.adapters.isServer = function() return false end
local drawn
Speech.adapters.draw = function(shell, text) drawn = text; return true end
local shell = { isDead = function() return false end, getX = function() return 0 end, getY = function() return 0 end }

check("data loads", Data.load(), true)
local found
for _, r in ipairs(Data.barks.SAFE_MOMENT or {}) do if string.find(r.t, "Primeiro", 1, true) then found = r.t end end
check("bark translated in place", found, "Primeiro sil\195\170ncio do dia. N\195\163o confio, mas aceito.")
check("render template + PT date/time", Speech.render("Saw a crew near {town} on {date}, around {time}.", { town = "Riverside" }, shell),
    "Vi um bando perto de Riverside em 9 de julho, l\195\161 pelas 3 da tarde.")
check("render untranslated stays English", Speech.render("Totally new line.", nil, shell), "Totally new line.")
Speech.say(shell, "Stay right there. Don't move a muscle.", {})
check("say translates fixed code line", drawn, "Fica a\195\173 mesmo. N\195\163o mexe um m\195\186sculo.")
check("caption template with filled placeholder", ProjectALife.AudioPolicy.caption("Grabbing this canned beans."), "Vou pegar canned beans.")
check("caption bracketed stays hidden", ProjectALife.AudioPolicy.caption("[static]"), nil)
check("render translates var values + contraction", Speech.render("The robbers sleep at {den}.", { den = "the school" }, shell),
    "Os ladr\195\181es dormem na escola.")
check("caption template with contraction", ProjectALife.AudioPolicy.caption("The robbers sleep at the school."),
    "Os ladr\195\181es dormem na escola.")
package.path = arg[1] .. "/media/lua/server/?.lua;" .. arg[2] .. "/media/lua/server/?.lua;" .. package.path
ProjectALife.ModuleRegistry = ProjectALife.ModuleRegistry or { register = function() return true end }
require "ZZZ_ProjectALifePTBR_Server"
local okPanic, Panic = pcall(require, "ProjectALife/Modules/ALifeModulePanic")
check("server hook translates panic lines", okPanic and Panic.gunFearLines[1], "Ele t\195\161 armado -- corre!")
check("chat PT with accents (bytes)", Intents.classify("Voc\195\170 tem comida?"), "ASK_FOOD")
check("chat PT abbreviation", Intents.classify("vc tem comida??"), "ASK_FOOD")
check("chat PT yes pending", Intents.classify("claro", true), "YES")
check("chat PT no pending (bytes)", Intents.classify("n\195\163o", true), "NO")
check("chat PT 'no' is not a refusal", (Intents.classify("voc\195\170 tem comida no carro?", true)), "ASK_FOOD")
check("chat lone English no", (Intents.classify("no", true)), "NO")
check("chat English still works", Intents.classify("got any food?"), "ASK_FOOD")
print(failures == 0 and "ALL OK" or (failures .. " FAILED"))
os.exit(failures == 0 and 0 or 1)
