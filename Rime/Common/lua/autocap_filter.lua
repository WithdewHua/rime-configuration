-- 修改自 https://github.com/tumuyan/rime-melt/blob/master/lua/melt.lua
-- 输入的内容大写前 2 个字符，自动转全小写词条为全词大写；大写第一个字符，自动转写全小写词条为首字母大写
local function autocap_filter(input, env)
    for cand in input:iter() do
        local text = cand.text
        local context_input = env.engine.context.input
        if (string.find(text, "^%l%l.*") and string.find(context_input, "^%u%u.*")) then
            if (string.len(text) == 2) then
                yield(Candidate("cap", 0, 2, context_input , "+" ))
            else
                yield(Candidate("cap", 0, string.len(context_input), string.upper(text) , "+" .. string.sub(cand.comment, 2)))
            end
        elseif (string.find(text, "^%l+$") and string.find(context_input, "^%u+")) then
            local suffix = string.sub(text, string.len(context_input) + 1)
            yield(Candidate("cap", 0, string.len(context_input), context_input .. suffix , "+" .. suffix))
        else
            yield(cand)
        end
    end
end

return autocap_filter