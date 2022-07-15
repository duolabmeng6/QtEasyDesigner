# 查询github上最新的版本
import requests
from pyefun import *


def 获取最新版本号和下载地址(project_name):
    url = f"https://green-sound-d020.duolabmeng.workers.dev/repos/{project_name}/releases/latest"
    # print(url)
    jsondata = requests.get(url)
    jsondata = jsondata.json()
    版本号 = jsondata['tag_name']
    body = jsondata['body']
    urls = jsondata['assets']
    created_at = jsondata['created_at']
    发布日期 = 到时间(created_at).到文本("YYYY年MM月DD日")

    # print(tag_name, body)
    下载地址列表 = []
    for url in urls:
        fileUrl = url['browser_download_url']
        下载地址列表.append(fileUrl)
    return 版本号, 下载地址列表, 发布日期


if __name__ == '__main__':
    最新版本号, 下载地址, 发布时间 = 获取最新版本号和下载地址("duolabmeng6/QtEsayDesigner")
    print(最新版本号, 下载地址, 发布时间)
