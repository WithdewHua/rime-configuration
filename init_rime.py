#!/usr/bin/env python3

import platform
import shutil
import os

# 获取当前系统平台
current_platform = platform.system()

# 根据不同平台设置相应的路径
if current_platform == "Windows":
    rime_path = r"%APPDATA%\Rime"

elif current_platform == "Linux":
    rime_path = "~/.local/share/fcitx5/rime"

elif current_platform == "Darwin":
    rime_path = "~/Library/Rime"

else:
    print("Unsupported platform")
    exit(1)

common_source_path = os.path.join(os.getcwd(), "Rime/Common")
plat_source_path = os.path.join(os.getcwd(), f"Rime/{current_platform}")

for source_path in [common_source_path, plat_source_path]:
    # 复制文件
    print(f"Copying {source_path} to {rime_path}")
    shutil.copytree(source_path, os.path.expanduser(rime_path), dirs_exist_ok=True)
