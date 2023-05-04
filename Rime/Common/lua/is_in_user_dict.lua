-- 若候选词为用户词，则加上 * 作为提示
local function is_in_user_dict(input,env)
    for cand in input:iter() do
        if(string.find(cand.type,"user"))then cand.comment=cand.comment..'*'end
        yield(cand)
    end 
end

return is_in_user_dict