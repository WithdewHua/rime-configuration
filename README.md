## Rime Configuraion

本仓库用于存放自用 Rime 配置

### 文件说明

```shell
rime
├── Android
│  ├── backgrounds
│  ├── trime.yaml
│  ├── 单静.trime.custom.yaml
│  └── 单静.trime.yaml
├── Common
│  ├── build
│  ├── custom_phrase_double_pinyin.txt
│  ├── default.yaml
│  ├── dictionary
│  ├── double_pinyin.custom.yaml
│  ├── double_pinyin.schema.yaml
│  ├── key_bindings.yaml
│  ├── lua
│  ├── melt_eng.custom.yaml
│  ├── melt_eng.schema.yaml
│  ├── opencc
│  ├── punctuation.yaml
│  ├── radical_pinyin.custom.yaml
│  ├── radical_pinyin.dict.yaml
│  ├── radical_pinyin.schema.yaml
│  ├── rime.lua
│  ├── rime_cn.dict.yaml
│  ├── rime_en.dict.yaml
│  ├── symbols.yaml
│  ├── zh-hans-t-essay-bgc.gram
│  └── zh-hans-t-essay-bgw.gram
├── Darwin
│  └── squirrel.custom.yaml
├── iOS
├── Linux
└── Windows
   └── weasel.custom.yaml
```

仓库中 `Rime` 目录下为 Rime 所有配置文件，其中：

  - `Common` 目录为所有平台共享内容；
  - 其余指定平台类型文件夹内容为该平台独享

### 配置说明

#### 输入方案

- 自然码双拼
  - [雾凇拼音简体词库版](https://github.com/iDvel/rime-ice/blob/main/double_pinyin.schema.yaml)
  - [魔然辅筛](https://github.com/ksqsf/rime-moran)
  - [melt_eng](https://github.com/tumuyan/rime-melt) 英文输入方案

#### 输入扩展功能

- 反查：[radical-pinyin](https://github.com/mirtlecn/rime-radical-pinyin) (`L` 触发)
- Emoji 输入: [雾凇拼音 Emoji 方案](https://github.com/iDvel/rime-ice/blob/main/opencc/emoji.json)
- 符号输入：基于 [scomper/Rime](https://github.com/scomper/rime) 自调整的符号输入 (`V` 触发)
- [以词定字](https://github.com/BlindingDark/rime-lua-select-character)：快捷键 `[ ]`
- [Unocode 输入](https://github.com/shewer/librime-lua-script/blob/main/lua/component/unicode.lua)：`U` 触发
- [数字中文大写输入](https://github.com/yanhuacuo/98wubi-tables)：`R` 触发

##### Lua 脚本说明

| 脚本名 | 脚本说明 |
| --- | --- |
| `datetime` | 用于输入日期、星期、时间 |
| `unicode` | 用于输入 unicode |
| `rime_lua_select_character` | 以词定字 |
| `reduce_english_filter` | 用于降低部分英语单词的权重 |
| `insert_space_between_words` | 候选词中英文间增加空格 |
| `number_translator` | 对输入的数字进行大写转换 |
| `autocap_filter` | 英文大写转换，首字符大写转换小写单词为首字母大写，前 2 个字符大写转换小写单词为全大写 |
| `moran*` | [魔然](https://github.com/ksqsf/rime-moran) 方案相关 lua 脚本 |

#### 词库

- [雾凇拼音词库](https://github.com/iDvel/rime-ice)
  - `8105` 字表
  - `41448` 字表
  - `base` 基础词库
  - `ext` 扩展词库
  - `tencent` 腾讯词向量
- [`zhwiki` 百万维基词库](https://github.com/felixonmars/fcitx5-pinyin-zhwiki)
- [`moegirl` 维基词库](https://github.com/outloudvi/mw2fcitx/)
- 自维护 `cn_en` 中英文混合词条

### 使用说明

#### 桌面平台

```shell
# 克隆当前项目
git clone https://github.com/WithdewHua/rime-configuration.git

# 复制所有文件至 Rime 用户目录
# 注意：
#   - Windows 平台需注意先退出算法服务
#   - Linux 适配 fcitx5
python3 init_rime.py

# deploy&enjoy!
```

#### 移动平台

##### 通用

将仓库 `Rime/Common` 及 `Rime/<平台类型>` 文件夹内容复制到 Rime 用户文件夹中，重新部署即可。

##### 仓 (Hamster)

前提条件：

- 仓中启用 iCloud
- 联网的 Mac

使用方法：

```shell
# 在 Mac 上克隆当前项目
git clone https://github.com/WithdewHua/rime-configuration.git

# 复制 rime 配置文件到仓的 iCloud 目录中
python3 init_rime.py --os ios

# 确认 iCloud 文件同步至手机后，进入仓中重新部署即可
```

### 更多

增加输入方案、添加词库、设置同步等自定义配置可参考 [Rime 输入法配置记录](https://www.10101.io/2019/01/30/rime-configuration)

### 感谢

#### Rime

- [rime](https://github.com/rime/home)
- [ssnhd/rime](https://github.com/ssnhd/rime)
- [iDvel/rime-ice](https://github.com/iDvel/rime-ice)
- [scomper/Rime](https://github.com/scomper/rime)
- [rime-melt](https://github.com/tumuyan/rime-melt)
- [rime-radical-pinyin](https://github.com/mirtlecn/rime-radical-pinyin)
- [felixonmars/fcitx5-pinyin-zhwiki](https://github.com/felixonmars/fcitx5-pinyin-zhwiki)

#### 字体

- [霞鹜文楷](https://github.com/lxgw/LxgwWenKai)
- [花园明朝](http://fonts.jp/hanazono/)
- [謎乃明朝](https://github.com/ge9/NazonoMincho)
