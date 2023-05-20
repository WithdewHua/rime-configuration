#!/usr/bin/env python3

import platform
import shutil
import os
import argparse
from pathlib import Path


def parse():
    parser = argparse.ArgumentParser(description="RimeConfigHelper")
    parser.add_argument("--os", default="", help="Specify the platform")

    return parser.parse_args()


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


def main(os_name=""):
    # platform 对应的 rime 用户目录路径
    platform_rime_userpath_mapping = {
        "windows": Path(os.getenv("APPDATA", default="%APPDATA%")) / "Rime",
        "linux": Path("~/.local/share/fcitx5/rime").expanduser(),
        "darwin": Path("~/Library/Rime").expanduser(),
        "ios": Path("~/Library/Mobile Documents/iCloud~dev~fuxiao~app~hamsterapp/Documents/RIME/Rime").expanduser(),
    }

    # 获取当前系统平台
    current_platform = platform.system() if not os_name else os_name

    # 根据不同平台设置相应的路径
    rime_path = platform_rime_userpath_mapping.get(current_platform.lower(), "")
    if not rime_path:
        print("Unsupported platform")
        exit(1)

    # 公共文件目录
    common_source_path = Path.cwd() / "Rime" / "Common"
    # 平台独有文件目录
    plat_source_path = Path.cwd() / "Rime" / current_platform

    print(f"Current platform: {current_platform}")
    for source_path in [common_source_path, plat_source_path]:
        if not source_path.exists():
            continue
        # 复制文件
        print(f"Copying {source_path} to {rime_path}")
        shutil.copytree(source_path, rime_path, dirs_exist_ok=True)


if __name__ == "__main__":
    args = parse()
    main(os_name=args.os)
