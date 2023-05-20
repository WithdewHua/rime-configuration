-- 候选词中英文字符间插入空格
local utf8 = require("utf8")

local function has_mixed_chars(str)
    local has_cn = false
    local has_asc = false
    for _, char in utf8.codes(str) do
        if char >= 19968 and char <= 40869 then
            has_cn = true
        elseif char >= 0 and char <= 127 then
            has_asc = true
        end
        if has_cn and has_asc then
            return true
        end
    end
    return false
end

local function insert_space_between_words(input, env)
    for cand in input:iter() do
        -- input:inter() 中 cand 为 Phrase，无法修改 cand.text
        local text = cand.text
        -- 含有中文及 ASCII 字符时才做处理
        if has_mixed_chars(text) then
            -- 在英文或者数字字符前后之间插入空格
            text = text:gsub("([%a%d]+)", " %1 ")
            -- 去除候选词首尾空格
            text = text:gsub("^%s*(.-)%s*$", "%1")
            -- 多个空格替换为一个空格
            text = text:gsub("%s%s+", " ")
            cand = cand:to_shadow_candidate(cand.type, text, cand.comment)
        end
        yield(cand)
    end 
end

return insert_space_between_words
