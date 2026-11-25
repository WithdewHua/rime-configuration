#!/usr/bin/env python3
"""从上游仓库同步词库、OpenCC 数据与语法模型。

upstream_repo.yaml 中的每个条目支持两种同步方式：

- downloads: 从仓库分支或 Release 下载文件；远端以 .gz 结尾时自动解压，
  可用 {file: 远端文件名, local: 本地文件名} 重命名。
- generate: 浅克隆仓库后执行生成脚本，把标准输出写入目标文件
  （用于上游不再提交生成产物的文件，如魔然的 zrmdb.txt / moran_chaifen.txt）。
"""

import gzip
import os
import re
import shutil
import subprocess
import sys
import tempfile

import requests
import yaml

script_dir = os.path.dirname(os.path.abspath(__file__))
local_path_prefix = os.path.join(script_dir, "..")
repo_url = 'https://github.com/{}/{}/raw/{}/{}'
release_url = 'https://github.com/{}/{}/releases{}download{}/{}'
clone_url = 'https://github.com/{}/{}.git'

failures = []


def read_config():
    # 从 yaml 文件中读取文件列表
    with open(os.path.join(script_dir, 'upstream_repo.yaml'), 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def normalize_file(file):
    if isinstance(file, str):
        return {"file": file, "local": None}
    return {"file": file["file"], "local": file.get("local")}


def align_dict_name(path):
    """Rime 要求词库的 name 字段与文件名一致，按本地文件名修正。"""
    if not path.endswith(('.yaml', '.yml')):
        return
    stem = re.sub(r'(\.dict)?\.ya?ml$', '', os.path.basename(path))
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    aligned = re.sub(r'(?m)^name:[ \t]*\S*[ \t]*$', f'name: {stem}', content, count=1)
    if aligned != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(aligned)
        print(f"  -> align dict name: {os.path.relpath(path, local_path_prefix)} (name: {stem})")


def save(dest, content, remote_name, url):
    if remote_name.endswith('.gz'):
        content = gzip.decompress(content)
    if dest.endswith('.gz'):
        dest = dest[:-3]
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, 'wb') as f:
        f.write(content)
    align_dict_name(dest)
    print(f"Downloaded {url} -> {os.path.relpath(dest, local_path_prefix)}")


def download_files(owner, repo, branch, tag, downloads):
    for download in downloads:
        remote_path = download["path"].rstrip("/")
        local_path = download["local_path"].rstrip("/")
        for item in [normalize_file(file) for file in download["files"]]:
            remote_name = item["file"]
            local_name = item["local"] or (remote_name[:-3] if remote_name.endswith(".gz") else remote_name)
            dest = os.path.join(local_path_prefix, local_path, local_name)

            # 构造 请求 URL
            if branch.lower() == "release":
                if tag:
                    url = release_url.format(owner, repo, "/", f"/{tag}", remote_name)
                else:
                    url = release_url.format(owner, repo, "/latest/", "", remote_name)
            else:
                url = repo_url.format(owner, repo, branch, f"{remote_path}/{remote_name}" if remote_path != "." else remote_name)

            response = requests.get(url, timeout=120)
            if response.status_code == 200:
                save(dest, response.content, remote_name, url)
            else:
                message = f"Fail to download {url} (HTTP {response.status_code})"
                failures.append(message)
                print(message)


def run_generate(owner, repo, branch, tasks):
    """浅克隆仓库并执行生成脚本，用于上游不再提交的生成产物。"""
    workdir = tempfile.mkdtemp(prefix=f"{repo}-")
    try:
        subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", branch, clone_url.format(owner, repo), workdir],
            check=True, capture_output=True,
        )
        for task in tasks:
            command = task["command"]
            dest = os.path.join(local_path_prefix, task["local_path"])
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, "wb") as out:
                subprocess.run(command, cwd=workdir, check=True, stdout=out)
            print(f"Generated {' '.join(command)} -> {os.path.relpath(dest, local_path_prefix)}")
    except subprocess.CalledProcessError as e:
        stderr = (e.stderr or b"").decode(errors="replace").strip()
        message = f"Fail to generate {owner}/{repo}: {' '.join(e.cmd)} exited {e.returncode}\n{stderr}"
        failures.append(message)
        print(message)
    finally:
        shutil.rmtree(workdir, ignore_errors=True)


def main():
    for item in read_config():
        owner = item['owner']
        repo = item['repo']
        branch = item.get('branch', 'master')
        tag = item.get('tag')
        if item.get('downloads'):
            download_files(owner, repo, branch, tag, item['downloads'])
        if item.get('generate'):
            run_generate(owner, repo, branch, item['generate'])

    if failures:
        print(f"\n{len(failures)} 项同步失败：")
        for message in failures:
            print(f"- {message.splitlines()[0]}")
        sys.exit(1)
    print("\n上游数据同步完成")


if __name__ == "__main__":
    main()
