import json
import os
import platform
import shutil
import sys

from PySide6 import QtCore
from PySide6.QtCore import *
from PySide6.QtWidgets import *

from 自动更新模块.压缩包文件处理 import zip解压2
from 自动更新模块.文件下载模块 import 下载文件
from 自动更新模块.自动更新读取版本模块 import 获取最新版本号和下载地址


def 系统_是否为window系统():
    return platform.system().lower() == 'windows'


def 系统_是否为linux系统():
    return platform.system().lower() == 'linux'


def 系统_是否为mac系统():
    return platform.system().lower() == 'darwin'


def 取自身路径Window():
    # 如果不处于编译状态反馈空
    try:
        编译后路径 = sys._MEIPASS
        return sys.argv[0]
    except Exception:
        return ""


def 取自身MacOs应用路径():
    # 如果不处于编译状态反馈空
    try:
        编译后路径 = sys._MEIPASS
    except Exception:
        编译后路径 = os.path.abspath(".")
        # 调试的
        # 编译后路径 = "/Users/chensuilong/Desktop/pythonproject/autotest/dist/my_app.app/Contents/MacOS"
    app目录 = 编译后路径[:编译后路径.rfind('/')]
    app目录 = app目录[:app目录.rfind('/')]
    父目录名称 = 编译后路径[编译后路径.rfind('/') + 1:]
    if 父目录名称 == "MacOS":
        return app目录
    else:
        return ""


def 更新自己MacOS应用(资源压缩包, 应用名称="my_app.app"):
    # 资源压缩包 = "/Users/chensuilong/Desktop/pythonproject/autotest/dist/my_app.2.0.zip"
    # 应用名称 例如 my_app.app 这你的压缩包里面压缩的应用文件夹名称
    MacOs应用路径 = 取自身MacOs应用路径()
    if MacOs应用路径 != "":
        app目录父目录 = MacOs应用路径[:MacOs应用路径.rfind('/')]
        print(f"资源压缩包 {资源压缩包} app目录父目录{app目录父目录} MacOs应用路径{MacOs应用路径}")
        if MacOs应用路径 != "":
            zip解压2(资源压缩包, app目录父目录, [应用名称 + '/Contents/'])
            MacOs应用路径 = os.path.join(app目录父目录, 应用名称)
            # QApplication.quit()
            应用名称 = 应用名称[:应用名称.rfind('.')]
            运行命令 = f"killall {应用名称} && open -n -a {MacOs应用路径}"
            # 消息框提示运行命令
            # QMessageBox.information(None, "提示", f"运行命令 {运行命令}")
            os.system(运行命令)
            return True, MacOs应用路径
    else:
        print("非MacOS编译环境")
        return False, ""


def 检查文件是否存在_存在则删除():
    自身路径Window = 取自身路径Window()
    if 自身路径Window == "":
        print("非Window编译环境")
        return False, ""
    # 检查文件是否存在
    旧的文件名 = 自身路径Window + ".old.bak"
    if os.path.exists(旧的文件名):
        # 删除文件
        os.remove(旧的文件名)


def 更新自己Window应用(exe资源文件路径):
    # window更新方法
    # exe资源文件路径 = r"C:\Users\csuil\.virtualenvs\QtEasyDesigner\Scripts\dist\my_app1.0.exe"
    自身路径Window = 取自身路径Window()
    if 自身路径Window == "":
        print("非Window编译环境")
        return False, ""
    文件名 = os.path.basename(自身路径Window)

    # 检查文件是否存在
    旧的文件名 = 自身路径Window + ".old.bak"
    if os.path.exists(旧的文件名):
        # 删除文件
        os.remove(旧的文件名)

    os.rename(自身路径Window, 旧的文件名)
    shutil.move(exe资源文件路径, 自身路径Window)
    # 删除文件 这步放到启动时检查删除就好
    # os.remove(自身路径Window + ".old.bak") 这个运行中是无法删除的

    # 结束自身运行 然后重启自己
    os.execv(自身路径Window, sys.argv)
    os.system(f"taskkill /f /im {文件名}")
    return True, ""


class 下载文件线程类(QThread):
    刷新进度条 = QtCore.Signal(int, str)  # 进度 提示文本

    def __init__(self, *args, **kwargs):
        super(下载文件线程类, self).__init__()
        self.窗口 = kwargs.get('窗口')
        self.下载地址 = kwargs.get('下载地址')
        self.保存地址 = kwargs.get('保存地址')
        self.编辑框 = kwargs.get('编辑框')
        self.进度条 = kwargs.get('进度条')
        self.应用名称 = kwargs.get('应用名称')
        self.回调函数 = kwargs.get('回调函数')

        self.刷新进度条.connect(self.刷新界面)

        # 绑定线程开始事件
        self.started.connect(self.ui_开始)
        # 绑定线程结束事件
        self.finished.connect(self.ui_结束)

    def run(self):
        if self.下载地址 == None:
            print("请传入下载地址")
            return

        def 进度(进度百分比, 已下载大小, 文件大小, 下载速率, 剩余时间):
            信息 = f"文件大小 {文件大小}MB 速度 {下载速率}MB 剩余时间 {剩余时间}秒"
            self.刷新进度条.emit(进度百分比, 信息)

        try:
            下载结果 = 下载文件(self.下载地址, self.保存地址, 进度)
            self.下载结果 = True
        except:
            self.下载结果 = False

    def ui_开始(self):
        self.编辑框.setText(f'开始下载')

    def ui_结束(self):
        print("下载结果", self.下载结果)
        print("保存地址", self.保存地址)
        self.回调函数(self.下载结果, self.保存地址)
        self.编辑框.setText(f"下载完成 {self.保存地址}")

    def 刷新界面(self, 进度, 信息):
        if self.编辑框:
            self.编辑框.setText(str(信息))
        if self.进度条:
            self.进度条.setValue(int(进度))


class 检查更新线程(QThread):
    def __init__(self, Github项目名称="duolabmeng6/qtAutoUpdateApp", 回调函数=None):
        super(检查更新线程, self).__init__()
        # 绑定线程开始事件
        self.started.connect(self.ui_开始)
        # 绑定线程结束事件
        self.finished.connect(self.ui_结束)
        self.Github项目名称 = Github项目名称
        self.回调函数 = 回调函数

    def run(self):
        data = 获取最新版本号和下载地址(self.Github项目名称)
        self.数据 = data

    def ui_开始(self):
        print("开始检查更新")

    def ui_结束(self):
        # data = json.dumps(self.数据, indent=4, ensure_ascii=False)
        # print("检查更新结果", data)
        self.回调函数(self.数据)
