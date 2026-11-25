#!/usr/bin/env python3
"""把仓库里的 Rime 配置同步到本机 Rime 用户目录。

--os   目标系统：windows / linux / darwin / ios，默认当前系统
--ime  macOS 上的输入法框架：squirrel（鼠须管）或 fcitx5；
       默认自动判断，装了 fcitx5 就用 fcitx5，否则用鼠须管
"""

import argparse
import os
import platform
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent

# 各系统的 Rime 用户目录；darwin 按输入法框架区分
RIME_USER_DIRS = {
    "windows": Path(os.getenv("APPDATA", default="%APPDATA%")) / "Rime",
    "linux": Path("~/.local/share/fcitx5/rime").expanduser(),
    "ios": Path("~/Library/Mobile Documents/iCloud~dev~fuxiao~app~hamsterapp/Documents/RIME/Rime").expanduser(),
}
DARWIN_RIME_USER_DIRS = {
    "fcitx5": Path("~/.local/share/fcitx5/rime").expanduser(),
    "squirrel": Path("~/Library/Rime").expanduser(),
}

# 与目标平台/输入法对应的平台独享目录（仓库内大小写不统一，这里按小写匹配）
PLATFORM_DIR_NAMES = {
    "windows": "windows",
    "linux": "linux",
    "darwin": "darwin",
    "ios": "ios",
}
DARWIN_IME_DIR_NAMES = {
    "fcitx5": None,          # fcitx5 不需要鼠须管那套 custom.yaml
    "squirrel": "darwin",
}


def parse():
    parser = argparse.ArgumentParser(description="RimeConfigHelper")
    parser.add_argument("--os", default="", help="目标系统：windows / linux / darwin / ios")
    parser.add_argument("--ime", default="", choices=["", "squirrel", "fcitx5"], help="macOS 上的输入法框架")
    return parser.parse_args()


def detect_ime():
    """macOS 上装了 fcitx5 就用 fcitx5，否则用鼠须管。"""
    if DARWIN_RIME_USER_DIRS["fcitx5"].exists():
        return "fcitx5"
    if Path("~/Library/fcitx5/lib/fcitx5/librime.so").expanduser().exists():
        return "fcitx5"
    return "squirrel"


def find_platform_dir(name):
    """在 Rime 目录下按小写名匹配平台独享目录（Linux/darwin 大小写不一致）。"""
    if not name:
        return None
    for path in (REPO_ROOT / "Rime").iterdir():
        if path.is_dir() and path.name.lower() == name.lower():
            return path
    return None


def copytree(src: Path, dst: Path):
    dst.mkdir(parents=True, exist_ok=True)
    copied = 0
    for path in src.iterdir():
        dst_path = dst / path.name
        if path.is_dir():
            copied += copytree(path, dst_path)
        else:
            shutil.copy2(path, dst_path)
            copied += 1
    return copied


def main(os_name="", ime=""):
    current_platform = (os_name or platform.system()).lower()
    ime = ime or (detect_ime() if current_platform == "darwin" else "")

    if current_platform == "darwin":
        rime_path = DARWIN_RIME_USER_DIRS[ime]
        platform_dir_name = DARWIN_IME_DIR_NAMES[ime]
    else:
        rime_path = RIME_USER_DIRS.get(current_platform)
        platform_dir_name = PLATFORM_DIR_NAMES.get(current_platform)

    if not rime_path:
        print(f"Unsupported platform: {current_platform}")
        raise SystemExit(1)

    print(f"目标系统: {current_platform}" + (f"，输入法框架: {ime}" if ime else ""))
    source_dirs = [REPO_ROOT / "Rime" / "Common", find_platform_dir(platform_dir_name)]
    for source_path in source_dirs:
        if not source_path or not source_path.exists():
            continue
        copied = copytree(source_path, rime_path)
        print(f"同步 {source_path.relative_to(REPO_ROOT)} -> {rime_path}（{copied} 个文件）")


if __name__ == "__main__":
    args = parse()
    main(os_name=args.os, ime=args.ime)
