-- 这是用户词吗？
-- 非常简单的lua滤镜，为所有用户词都加上*作为提示
local function is_that_a_user_dict(input,env)
    for cand in input:iter() do
        if(string.find(cand.type,"user"))then cand.comment=cand.comment..'*'end
        yield(cand)
    end 
end

return is_that_a_user_dict