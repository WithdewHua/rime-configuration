-- 中英文字符间插入空格

local function insert_space_between_words(input, env)
    for cand in input:iter() do
        -- input:inter() 中 cand 为 Phrase，无法修改 cand.text
        -- 在英文或者数字字符前后之间插入空格
        local text
        text = cand.text:gsub("([%a%d]+)", " %1 ")
        -- 去除候选词首尾空格
        text = cand.text:gsub("^%s*(.-)%s*$", "%1")
        log.info(text)
        cand = cand:to_shadow_candidate(cand.type, text, cand.comment)
        log.info(cand.text)
        yield(cand)
    end 
end

return insert_space_between_words
