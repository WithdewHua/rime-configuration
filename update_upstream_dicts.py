#!/usr/bin/env python3

import os
import requests
import yaml
import base64


# GitHub API url
api_url = 'https://api.github.com'

# 从 yaml 文件中读取文件列表
with open('upstream_repo.yaml', 'r') as f:
    file_list = yaml.safe_load(f)

# 循环下载文件并保存到本地
for item in file_list:
    # 获取文件的所有者、仓库名和文件列表
    owner = item['owner']
    repo = item['repo']
    files = item['files']
    
    # 循环下载文件并保存到本地
    for file in files:
        # 构造 API 请求 URL
        url = f'{api_url}/repos/{owner}/{repo}/contents/{file["path"]}'
    
        # 发送 API 请求
        response = requests.get(url)

        # 获取文件内容并保存到本地文件
        if response.status_code == 200:
            print(f"Downloaded {url} to {file['local_path']}")
            content = response.json()['content']
            content = base64.b64decode(content)  # GitHub API 返回的是 base64 编码的文件内容，需要解码
            with open(file['local_path'], 'wb') as f:
                f.write(content)
        else:
            print(f"Fail to download {url}")

