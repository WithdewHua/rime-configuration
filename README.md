## Rime Configuraion

本仓库用于存放自用 Rime 配置

### 文件说明

```bash
Rime
├── Android
│  ├── backgrounds
│  ├── trime.yaml
│  ├── 单静.trime.custom.yaml
│  └── 单静.trime.yaml
├── Common
│  ├── custom_phrase_double_pinyin.txt
│  ├── default.custom.yaml
│  ├── default.yaml
│  ├── dictionary
│  ├── double_pinyin.custom.yaml
│  ├── double_pinyin.schema.yaml
│  ├── liangfen.dict.yaml
│  ├── liangfen.schema.yaml
│  ├── melt_eng.custom.yaml
│  ├── melt_eng.schema.yaml
│  ├── opencc
│  ├── rime.lua
│  ├── rime_cn.dict.yaml
│  ├── rime_en.dict.yaml
│  ├── symbols.custom.yaml
│  └── zh-hans-t-essay-bgw.gram
├── Darwin
│  └── squirrel.custom.yaml
├── Linux
│  └── anran.tar.gz
└── Windows
   └── weasel.custom.yaml
```

仓库中 `Rime` 目录下为 Rime 所有配置文件，其中：

  - `Common` 目录为所有平台共享内容；
  - 其余指定平台类型文件夹内容为该平台独享

### 输入方案

本仓库中文输入方案仅包含[自然码双拼](https://github.com/iDvel/rime-ice/blob/main/double_pinyin.schema.yaml)，中英文混输采用 [melt_eng](https://github.com/tumuyan/rime-melt)。

### 使用说明

#### 桌面平台

```python
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

将仓库 `Rime/Common` 及 `Rime/<平台类型>` 文件夹内容复制到 Rime 用户文件夹中，重新部署即可。

### 更多

增加输入方案、添加词库、设置同步等自定义配置可参考 [Rime 输入法配置记录](https://www.10101.io/2019/01/30/rime-configuration)

### 感谢

- [rime](https://github.com/rime/home)
- [ssnhd/rime](https://github.com/ssnhd/rime)
- [iDvel/rime-ice](https://github.com/iDvel/rime-ice)
- [scomper/Rime](https://github.com/scomper/rime)
- [scomper/rime-ice](https://github.com/scomper/rime-ice)
- [felixonmars/fcitx5-pinyin-zhwiki](https://github.com/felixonmars/fcitx5-pinyin-zhwiki)
