-- 中英文字符间插入空格

local function insert_space_between_words(input, env)
    for cand in input:iter() do
        -- input:inter() 中 cand 为 Phrase，无法修改 cand.text
        -- 在英文或者数字字符前后之间插入空格
        local text = cand.text
        text = text:gsub("([%a%d]+)", " %1 ")
        -- 去除候选词首尾空格
        text = text:gsub("^%s*(.-)%s*$", "%1")
        -- 多个空格替换为一个空格
        text = text:gsub("%s%s+", " ")
        cand = cand:to_shadow_candidate(cand.type, text, cand.comment)
        yield(cand)
    end 
end

return insert_space_between_words
