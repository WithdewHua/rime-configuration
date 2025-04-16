#!/usr/bin/env python3

import os
import requests
import yaml


local_path_prefix = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
repo_url = 'https://github.com/{}/{}/raw/{}/{}'
release_url = 'https://github.com/{}/{}/releases{}download{}/{}'

# 从 yaml 文件中读取文件列表
with open('upstream_repo.yaml', 'r') as f:
    file_list = yaml.safe_load(f)

# 循环下载文件并保存到本地
for item in file_list:
    # 获取文件的所有者、仓库名和文件列表
    owner = item['owner']
    repo = item['repo']
    branch = item['branch']
    tag = item.get("tag")
    downloads = item['downloads']
    
    # 循环下载文件并保存到本地
    for download in downloads:
        remote_path = download["path"].rstrip("/")
        local_path = download["local_path"].rstrip("/")
        files = download["files"]
        for file in files:
            # 构造 请求 URL
            if branch.lower() == "release":
                if tag:
                    url = release_url.format(owner, repo, "/", f"/{tag}", file)
                else:
                    url = release_url.format(owner, repo, "/latest/", "", file)
            else:
                url = repo_url.format(owner, repo, branch, f"{remote_path}/{file}" if remote_path != "." else file)
            # 发送 请求
            response = requests.get(url)

            # 获取文件内容并保存到本地文件
            if response.status_code == 200:
                print(f"Downloaded {url} to {os.path.join(local_path_prefix, local_path, file)}")
                with open(os.path.join(local_path_prefix, local_path, file), 'wb') as f:
                    f.write(response.content)
            else:
                print(f"Fail to download {url}")

