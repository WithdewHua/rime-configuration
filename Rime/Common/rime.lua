-- Rime Lua 扩展 https://github.com/hchunhui/librime-lua
-- 文档 https://github.com/hchunhui/librime-lua/wiki/Scripting
-------------------------------------------------------------
-- 日期时间
date_translator = require("datetime")
-- 以词定字
select_character = require("rime_lua_select_character")
-- 降低部分英语单词在候选项的位置
reduce_english_filter = require("reduce_english_filter")
-- Unicode 输入
unicode = require("unicode")
-- 中英文字符间插入空格
insert_space_between_words = require("insert_space_between_words")
-- 数字大写
number_translator = require("number_translator")
-- 英文输入大写转换
autocap_filter = require("autocap_filter")
-------------------------------------------------------------
