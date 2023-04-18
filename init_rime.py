#!/usr/bin/env python3

import platform
import shutil
import os
from pathlib import Path


def copytree(src, dst, dirs_exist_ok=True):
    for dir in [src, dst]:
        if not isinstance(dir, Path):
            dir: Path = Path(dir)
    # 创建目标文件夹
    dst.mkdir(parents=True, exist_ok=True)
    for path in src.iterdir():
        src_path = src / path.name
        dst_path = dst / path.name
        print(path, src_path, dst_path)
        # 文件夹递归处理
        if path.is_dir():
            copytree(src_path, dst_path, dirs_exist_ok=dirs_exist_ok)
        # 复制文件
        else:
            shutil.copy2(src_path, dst_path)


def main():
    # 获取当前系统平台
    current_platform = platform.system()

    # 根据不同平台设置相应的路径
    if current_platform == "Windows":
        rime_path = Path(os.getenv("APPDATA")) / "Rime"

    elif current_platform == "Linux":
        rime_path = Path("~/.local/share/fcitx5/rime").expanduser()

    elif current_platform == "Darwin":
        rime_path = Path("~/Library/Rime").expanduser()

    else:
        print("Unsupported platform")
        exit(1)

    common_source_path = Path.cwd() / "Rime" / "Common"
    plat_source_path = Path.cwd() / "Rime" / current_platform

    for source_path in [common_source_path, plat_source_path]:
        # 复制文件
        print(f"Copying {source_path} to {rime_path}")
        shutil.copytree(source_path, rime_path, dirs_exist_ok=True)


if __name__ == "__main__":
    main()