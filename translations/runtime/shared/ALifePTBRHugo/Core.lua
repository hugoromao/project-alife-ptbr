-- PT-BR speech layer for Project A-Life. Display text only: ids, gates, events and
-- saved data stay English. A line without a translation is shown in English.
local PT = ALifePTBRHugo or { dict = {}, loaded = false, entries = 0 }
ALifePTBRHugo = PT

function PT.load()
    if PT.loaded then return PT.entries end
    PT.loaded = true
    local okIndex, index = pcall(require, "ALifePTBRHugo/Speech/Index")
    local parts = okIndex and type(index) == "table" and tonumber(index.parts) or 0
    for part = 1, parts do
        local ok, fill = pcall(require, "ALifePTBRHugo/Speech/Part" .. part)
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

-- Portuguese contractions that only appear once a placeholder is filled
-- ("em {den}" + "a escola" -> "na escola").
PT.contractions = {
    { " em o ", " no " }, { " em a ", " na " }, { " em os ", " nos " }, { " em as ", " nas " },
    { " em um ", " num " }, { " em uma ", " numa " }, { " de o ", " do " }, { " de a ", " da " },
    { " de os ", " dos " }, { " de as ", " das " }, { " a o ", " ao " }, { " a os ", " aos " },
    { " por o ", " pelo " }, { " por a ", " pela " },
}
function PT.contract(text)
    if type(text) ~= "string" then return text end
    local s = " " .. text .. " "
    for _, pair in ipairs(PT.contractions) do
        s = string.gsub(s, pair[1], pair[2])
        local upperFrom = string.upper(string.sub(pair[1], 2, 2)) .. string.sub(pair[1], 3)
        s = string.gsub(s, "^ " .. upperFrom, " " .. string.upper(string.sub(pair[2], 2, 2)) .. string.sub(pair[2], 3))
    end
    return string.sub(s, 2, -2)
end

-- Den descriptions built by ALifeRumors.describe ("the school on the north side
-- of Riverside"); only rebuilt when the place noun is known.
PT.sides = { north = "norte", south = "sul", east = "leste", west = "oeste", northeast = "nordeste",
    northwest = "noroeste", southeast = "sudeste", southwest = "sudoeste" }
function PT.denText(text)
    local noun, town, side = string.match(text, "^(.-) out past the county road$")
    if noun ~= nil and PT.t(noun) ~= noun then return PT.t(noun) .. " depois da estrada do condado" end
    noun, town = string.match(text, "^(.-) in the middle of (.+)$")
    if noun ~= nil and PT.t(noun) ~= noun then return PT.t(noun) .. " no centro de " .. town end
    noun, side, town = string.match(text, "^(.-) on the (%a+) side of (.+)$")
    if noun ~= nil and PT.t(noun) ~= noun and PT.sides[side] ~= nil then
        return PT.t(noun) .. " no lado " .. PT.sides[side] .. " de " .. town
    end
    return nil
end

-- Placeholder values: known words and den descriptions.
function PT.value(text)
    if type(text) ~= "string" or text == "" then return text end
    local exact = PT.t(text)
    if exact ~= text then return exact end
    return PT.denText(text) or text
end

-- Rendered text whose English template had placeholders: match it against the
-- templates and rebuild the Portuguese one with the captured values.
local MAGIC = "([%^%$%(%)%%%.%[%]%*%+%-%?])"
function PT.buildTemplates()
    if PT.templates ~= nil then return PT.templates end
    if not PT.loaded then PT.load() end
    PT.templates, PT.prefixes = {}, {}
    for en, pt in pairs(PT.dict) do
        if string.sub(en, -1) == " " then
            -- Line the code finishes with a value ("... [Received: " .. label .. "]").
            PT.prefixes[#PT.prefixes + 1] = { en = en, pt = pt }
        elseif string.find(en, "{", 1, true) then
            local keys = {}
            local pattern = string.gsub(en, MAGIC, "%%%1")
            pattern = string.gsub(pattern, "{([a-z]+)}", function(key)
                keys[#keys + 1] = key
                return "(.-)"
            end)
            PT.templates[#PT.templates + 1] = { pattern = "^" .. pattern .. "$", keys = keys, pt = pt }
        end
    end
    return PT.templates
end

function PT.fromTemplate(text)
    for _, template in ipairs(PT.buildTemplates()) do
        local captures = { string.match(text, template.pattern) }
        if #captures > 0 then
            local values = {}
            for index, key in ipairs(template.keys) do values[key] = PT.value(captures[index]) end
            return PT.contract((string.gsub(template.pt, "{([a-z]+)}", function(key) return values[key] or "" end)))
        end
    end
    for _, prefix in ipairs(PT.prefixes) do
        if string.sub(text, 1, #prefix.en) == prefix.en then
            local joint = string.sub(prefix.pt, -1) == " " and "" or " "
            return prefix.pt .. joint .. string.sub(text, #prefix.en + 1)
        end
    end
    return nil
end

-- Display text from any path: exact line first, then templates.
function PT.caption(text)
    if type(text) ~= "string" or text == "" then return text end
    local exact = PT.t(text)
    if exact ~= text then return exact end
    if string.find(text, "%a") == nil then return text end
    return PT.fromTemplate(text) or text
end

return PT
