-- 修改自 https://github.com/tumuyan/rime-melt/blob/master/lua/melt.lua
-- 输入的内容大写前 2 个字符，自动转全小写词条为全词大写；大写第一个字符，自动转写全小写词条为首字母大写
local function autocap_filter(input, env)
    for cand in input:iter() do
        local text = cand.text
        local context_input = env.engine.context.input
        -- 输入编码首字母大写且候选为字母开头
        if context_input:find("^%u.*") and text:find("^%a.*") then
            -- 输入编码前两个字母均大写，则转换候选为全词大写
            if context_input:find("^%u%u.*") then
                text = text:upper()
            -- 输入编码仅首字母大写，则转换候选为首字母大写
            else
                text = text:sub(1, 1):upper() .. text:sub(2)
            end
            -- 构造候选
            yield(Candidate(cand.type, 0, #context_input, text, cand.comment))
        else
            yield(cand)
        end
    end
end

return autocap_filter