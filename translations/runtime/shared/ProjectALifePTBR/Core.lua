-- PT-BR speech layer for Project A-Life. Display text only: ids, gates, events and
-- saved data stay English. A line without a translation is shown in English.
local PT = ProjectALifePTBR or { dict = {}, loaded = false, entries = 0 }
ProjectALifePTBR = PT

function PT.load()
    if PT.loaded then return PT.entries end
    PT.loaded = true
    local okIndex, index = pcall(require, "ProjectALifePTBR/Speech/Index")
    local parts = okIndex and type(index) == "table" and tonumber(index.parts) or 0
    for part = 1, parts do
        local ok, fill = pcall(require, "ProjectALifePTBR/Speech/Part" .. part)
        if ok and type(fill) == "function" then PT.entries = PT.entries + (fill(PT.dict) or 0) end
    end
    return PT.entries
end

function PT.t(text)
    if type(text) ~= "string" or text == "" then return text end
    if not PT.loaded then PT.load() end
    return PT.dict[text] or text
end

PT.months = { "janeiro", "fevereiro", "mar\195\167o", "abril", "maio", "junho", "julho", "agosto",
    "setembro", "outubro", "novembro", "dezembro" }
PT.weekdays = { "domingo", "segunda-feira", "ter\195\167a-feira", "quarta-feira", "quinta-feira",
    "sexta-feira", "s\195\161bado" }

function PT.timeText(hour)
    hour = tonumber(hour) or 12
    if hour == 0 then return "meia-noite" end
    if hour == 12 then return "meio-dia" end
    if hour < 6 then return tostring(hour) .. " da madrugada" end
    if hour < 12 then return tostring(hour) .. " da manh\195\163" end
    if hour < 18 then return tostring(hour - 12) .. " da tarde" end
    return tostring(hour - 12) .. " da noite"
end

-- Fallbacks the English renderer would otherwise fill with English words.
PT.fixed = {
    destination = "algum lugar mais tranquilo",
    den = "um lugar para onde eu n\195\163o volto",
    weapon = "essa arma",
    faction = "um bando qualquer",
    group = "um bando qualquer",
    from = "um lugar estrada abaixo",
    to = "um lugar estrada abaixo",
    count = "alguns",
}

function PT.defaultFor(key, shell)
    if PT.fixed[key] ~= nil then return PT.fixed[key] end
    local speech = ProjectALife and ProjectALife.Speech
    if speech == nil then return nil end
    if key == "town" then
        local sx, sy
        if shell ~= nil then pcall(function() sx, sy = shell:getX(), shell:getY() end) end
        return speech.nearestTown(sx, sy) or "o condado"
    end
    if key == "date" or key == "time" or key == "weekday" then
        local clock = speech.clock()
        if key == "date" then
            return tostring(clock.day) .. " de " .. (PT.months[clock.month] or "julho")
        elseif key == "time" then
            return PT.timeText(clock.hour)
        end
        return PT.weekdays[speech.weekday(clock.year, clock.month, clock.day) + 1]
    end
    return nil
end

-- Returns vars with Portuguese values for the placeholders the caller left empty.
function PT.withDefaults(text, vars, shell)
    local out = nil
    for key in string.gmatch(text, "{([a-z]+)}") do
        if type(vars) ~= "table" or vars[key] == nil then
            local value = PT.defaultFor(key, shell)
            if value ~= nil then
                if out == nil then
                    out = {}
                    if type(vars) == "table" then for k, v in pairs(vars) do out[k] = v end end
                end
                out[key] = value
            end
        end
    end
    return out or vars
end

return PT
