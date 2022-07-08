import sys
import os

# 把当前目录导入到 path
import webbrowser

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("/Users/chensuilong/Desktop/pythonproject/pyqt")
sys.path.append(r"C:/pyefun/pyefun")
sys.path.append(r"C:\pyefun\QtEsayDesigner")

import PySide6
from PySide6.QtCore import Signal
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from pyefun import *

import win_app2
from qtefun.组件.主窗口 import 主窗口
from qtefun.图标 import 获取图标
from qtefun.组件.工具条 import 工具条
from qtefun.组件.系统托盘图标 import 系统托盘图标
from qtefun.组件.菜单 import 菜单
from qtefun.组件.菜单栏 import 菜单栏

import win_设计窗口
import win_属性表格


class MainWin(主窗口):
    插件端口号 = 0
    设计文件路径 = ""  # json文件

    def 初始化命令行参数(self):
        # 设计文件.json 端口号
        self.插件端口号 = 0
        if len(sys.argv) > 1:
            # 写到文件("/Users/chensuilong/Desktop/pythonproject/pyqt/qt_esay_designer/参数.json",
            #      json.dumps(sys.argv, indent=4))
            self.设计文件路径 = 子文本替换(sys.argv[1], "文件路径=", "")
            self.插件端口号 = 子文本替换(sys.argv[2], "port=", "")

    def __init__(self):
        super().__init__()
        self.设计文件路径 = ""
        self.ui = win_app2.Ui_MainWindow()
        self.初始化命令行参数()
        self.初始化菜单()
        self.ui.setupUi(self)
        self.show()
        self.初始化托盘图标()

        self.状态条标签 = QLabel()
        self.状态条标签.setText("欢迎使用 Qt视窗设计器(QtEsayDesigner) 版本: 2022年07月08日")
        self.ui.statusbar.addWidget(self.状态条标签)

        self.状态条标签_文件信息 = QLabel()
        self.状态条标签_文件信息.setText(self.设计文件路径)
        self.ui.statusbar.addWidget(self.状态条标签_文件信息)
        self.大小 = (1200, 600)
        self.标题 = "Qt视窗设计器"
        self.窗口居中()
        self.初始化工具条()

        if self.设计文件路径 == "":
            pass
            # 创建工程新建窗口
            # self.消息框("提示", "请选择一个设计文件")

        self.属性表格窗口 = win_属性表格.MainWin()
        # 配置信息加载
        # 设计文件路径 = "/Users/chensuilong/Desktop/pythonproject/testqtefun/启动窗口.json"
        self.属性表格窗口.设计窗口.可否关闭 = False
        self.属性表格窗口.设计窗口.信号_加载设计文件(self.设计文件路径)
        self.属性表格窗口.设计窗口.插件URL地址 = f"http://127.0.0.1:{self.插件端口号}"
        # 配置信息加载
        self.属性表格窗口.数据刷新()
        self.属性表格窗口.初始化项目管理()

        self.属性表格窗口.设计窗口.信号_代码跳转.connect(self.信号_代码跳转)

        self.ui.horizontalLayout_2.addWidget(self.属性表格窗口)
        self.ui.mdiArea.addSubWindow(self.属性表格窗口.设计窗口)
        self.ui.mdiArea.setBackground(QColor(236, 236, 236))
        self.ui.mdiArea.cascadeSubWindows()

        self.属性表格窗口.show()
        self.属性表格窗口.设计窗口.show()

        # self.属性表格窗口.listWidget
        self.ui.verticalLayout.addWidget(self.属性表格窗口.treeWidget)
        self.ui.verticalLayout.addWidget(self.属性表格窗口.listWidget)
        self.ui.horizontalLayout_5.addWidget(self.属性表格窗口.树形框项目管理)
        self.属性表格窗口.listWidget.setFixedWidth(260)

        # 切换为属性表格窗口
        self.ui.tabWidget.setCurrentIndex(1)

        self.属性表格窗口.信号_项目管理文件被选择.connect(self.信号_项目管理文件被选择)

    def 信号_项目管理文件被选择(self, 文件名):
        pass
        print("信号_项目管理文件被选择", 文件名)
        self.打开设计文件(文件名)

        # self.菜单_打开()

    def 初始化工具条(self):
        toolBar = 工具条(self.addToolBar("工具栏"))
        工具条数据 = 读入文本(路径优化(取运行目录() + r"/resources/toolBarData.json"))
        toolBar.从工具条数据中创建(工具条数据, 16, 16, self.工具条_点击)

    def 工具条_点击(self):
        sender = self.sender()
        名称 = sender.text()
        print("工具条_点击", sender.text())
        if 名称 == "撤销":
            self.消息框("等待开发")

            # self.撤销()
        elif 名称 == "恢复":
            self.消息框("等待开发")

            # self.恢复()
        elif 名称 == "左对齐":
            self.消息框("等待开发")

            # self.左对齐()
        elif 名称 == "右对齐":
            self.消息框("等待开发")

            # self.右对齐()
        elif 名称 == "顶对齐":
            self.消息框("等待开发")

            # self.顶对齐()
        elif 名称 == "底对齐":
            self.消息框("等待开发")

            # self.底对齐()
        elif 名称 == "窗口水平居中":
            self.消息框("等待开发")

            # self.窗口水平居中()
        elif 名称 == "窗口垂直居中":
            self.消息框("等待开发")

            # self.窗口垂直居中()
        elif 名称 == "组件水平居中":
            self.消息框("等待开发")

            # self.组件水平居中()
        elif 名称 == "组件垂直居中":
            self.消息框("等待开发")

            # self.组件垂直居中()
        elif 名称 == "水平平均分布":
            self.消息框("等待开发")

            # self.水平平均分布()
        elif 名称 == "垂直平均分布":
            self.消息框("等待开发")

            # self.垂直平均分布()
        elif 名称 == "等宽":
            self.消息框("等待开发")

            # self.等宽()
        elif 名称 == "等高":
            self.消息框("等待开发")

            # self.等高()
        elif 名称 == "等宽高":
            self.消息框("等待开发")

            # self.等宽高()
        elif 名称 == "运行":
            self.运行()
            # self.消息框("等待开发")

            # self.运行()
        elif 名称 == "停止":
            self.消息框("等待开发")

            # self.停止()
        elif 名称 == "重新运行":
            self.消息框("等待开发")

            # self.重新运行()
        elif 名称 == "编译":
            self.消息框("等待开发")

            # self.编译()

        return True

    def 初始化菜单(self):
        pass

        self.文件菜单 = 菜单(self, "文件")
        self.文件菜单.添加项目("新建", 获取图标("mdi.moon-new", "#FFFFFF"), self.菜单_新建, "Ctrl+N")
        self.文件菜单.添加项目("打开", 获取图标("mdi.moon-new", "#FFFFFF"), self.菜单_打开, "Ctrl+O")
        self.文件菜单.添加项目("保存", 获取图标("mdi.moon-new", "#FFFFFF"), self.菜单_保存, "Ctrl+S")
        self.文件菜单.添加项目("另存为", 获取图标("mdi.moon-new", "#FFFFFF"), self.菜单_另存为, )
        self.文件菜单.添加分隔条()

        self.文件菜单.添加项目("退出", 获取图标("mdi.exit-to-app", "#FFFFFF"), self.退出, "Ctrl+Q")
        self.编译菜单 = 菜单(self, "编辑")
        self.编译菜单.添加项目("撤销", 获取图标("mdi.moon-new", "#FFFFFF"), self.撤销, "Ctrl+Z")
        self.编译菜单.添加项目("恢复", 获取图标("mdi.moon-new", "#FFFFFF"), self.恢复, "Ctrl+Y")
        self.文件菜单.添加分隔条()
        self.编译菜单.添加项目("复制", 获取图标("mdi.moon-new", "#FFFFFF"), self.复制, "Ctrl+C")
        self.编译菜单.添加项目("粘贴", 获取图标("mdi.moon-new", "#FFFFFF"), self.粘贴, "Ctrl+V")

        self.编译菜单 = 菜单(self, "编译")
        self.编译菜单.添加项目("运行", 获取图标("mdi.moon-new", "#FFFFFF"), self.运行)
        self.编译菜单.添加项目("编译为可执行程序", 获取图标("mdi.moon-new", "#FFFFFF"), self.编译为可执行程序)
        self.设置菜单 = 菜单(self, "系统")
        self.设置菜单.添加项目("设置pycharm插件端口", 获取图标("mdi6.eye-outline", "#FFFFFF"), self.设置pycharm插件端口)
        self.设置菜单.添加项目("检查更新", 获取图标("mdi6.eye-outline", "#FFFFFF"), self.检查更新)
        self.设置菜单.添加项目("qtefun 项目地址: https://github.com/duolabmeng6/qtefun", 获取图标("mdi6.eye-outline", "#FFFFFF"),
                       self.打开qtefun网址)
        self.设置菜单.添加项目("qtEsayDesigner 项目地址: https://github.com/duolabmeng6/qtefun",
                       获取图标("mdi6.eye-outline", "#FFFFFF"), self.打开qtEsayDesigner网址)
        self.设置菜单.添加项目("关于", 获取图标("ei.bullhorn", "#FFFFFF"), self.关于)
        self.设置菜单.添加项目("帮助", 获取图标("mdi6.help-circle-outline", "#FFFFFF"))

        self.菜单栏 = 菜单栏(self)  # 菜单栏
        self.菜单栏.添加项目(self.文件菜单.取菜单项目())  # 将菜单添加到菜单栏
        self.菜单栏.添加项目(self.编译菜单.取菜单项目())  # 将菜单添加到菜单栏
        self.菜单栏.添加项目(self.设置菜单.取菜单项目())  # 将菜单添加到菜单栏
        self.设置菜单栏(self.菜单栏)  # 设置菜单栏

    def 打开qtefun网址(self):
        # 在浏览器中打开网址 https://github.com/duolabmeng6/qtefun
        webbrowser.open("https://github.com/duolabmeng6/qtefun")

    def 打开qtEsayDesigner网址(self):
        # 在浏览器中打开网址 https://github.com/duolabmeng6/qtefun
        webbrowser.open("https://github.com/duolabmeng6/qtEsayDesigner")

    def 关于(self):
        self.消息框("QtEsayDesigner 是我揣着情怀的开发~~", "关于", QMessageBox.Ok)

    def 检查更新(self):
        self.消息框("等待开发")

    def 撤销(self):
        self.消息框("等待开发")

    def 恢复(self):
        self.消息框("等待开发")

    def 复制(self):
        self.消息框("等待开发")

    def 粘贴(self):
        self.消息框("等待开发")

    def closeEvent(self, event):
        print("窗口关闭事件 main")
        event.accept()
        sys.exit(0)

    def 菜单_新建(self):
        pass
        self.属性表格窗口.设计窗口.新建()
        self.设计文件路径 = ""
        self.属性表格窗口.设计窗口.加载路径信息("")
        self.状态条标签_文件信息.setText(self.设计文件路径)

    def 菜单_打开(self):
        pass
        文件路径 = self.打开文件选择器("设计文件 (*.json)", "请选择设计文件的路径", 取运行目录())
        print("路径", 文件路径)
        if 文件路径 != "":
            self.设计文件路径 = 文件路径
        else:
            return
        print("设计文件路径", self.设计文件路径)
        self.打开设计文件(self.设计文件路径)

    def 打开设计文件(self, 文件路径):
        self.设计文件路径 = 文件路径
        self.属性表格窗口.设计窗口.新建()
        self.属性表格窗口.设计窗口.信号_加载设计文件(self.设计文件路径)
        self.状态条标签_文件信息.setText(self.设计文件路径)
        self.属性表格窗口.数据刷新()

    def 菜单_保存(self):
        pass
        if self.设计文件路径 == "":
            self.菜单_另存为()
            return
        print("设计文件路径", self.设计文件路径)
        # self.属性表格窗口.设计窗口.加载路径信息(self.设计文件路径)
        self.属性表格窗口.设计窗口.信号_保存组件信息()
        self.状态条标签_文件信息.setText(self.设计文件路径)

    def 菜单_另存为(self):
        pass
        文件路径 = self.打开文件保存选择器("设计文件 (*.json)", "请选择保存设计文件的路径", 取运行目录())
        print("路径", 文件路径)
        if 文件路径[0] != "":
            self.设计文件路径 = 文件路径[0]
        else:
            return
        print("设计文件路径", self.设计文件路径)
        self.属性表格窗口.设计窗口.加载路径信息(self.设计文件路径)
        self.属性表格窗口.设计窗口.信号_保存组件信息()
        self.状态条标签_文件信息.setText(self.设计文件路径)

    def 设置pycharm插件端口(self):
        端口号, _ = self.打开输入框("请输入", "pycharm插件的端口号")
        if 端口号:
            self.插件端口号 = int(端口号)
            self.托盘菜单.取菜单项目对象("设置pycharm插件端口").setText(f"设置pycharm插件端口{self.插件端口号}")
            self.设置菜单.取菜单项目对象("设置pycharm插件端口").setText(f"设置pycharm插件端口{self.插件端口号}")

    def 初始化托盘图标(self):
        self.托盘菜单 = 菜单(self, "托盘的菜单")
        self.托盘菜单.添加项目("显示/隐藏", 获取图标("mdi6.eye-outline", "#FFFFFF"), self.隐藏或隐藏)
        self.托盘菜单.添加项目("设置pycharm插件端口", 获取图标("mdi6.eye-outline", "#FFFFFF"), self.设置pycharm插件端口)
        self.托盘菜单.添加项目("退出", 获取图标("mdi.exit-to-app", "#FFFFFF"), self.退出)

        self.托盘 = 系统托盘图标(self)
        self.托盘.设置托盘菜单(self.托盘菜单)
        self.托盘.设置托盘图标(获取图标("ei.smiley", "#FFFFFF"))
        self.托盘.设置提示文本("我是一个菜单~")
        self.托盘.显示()

        self.托盘菜单.取菜单项目对象("设置pycharm插件端口").setText(f"设置pycharm插件端口{self.插件端口号}")
        self.设置菜单.取菜单项目对象("设置pycharm插件端口").setText(f"设置pycharm插件端口{self.插件端口号}")

    def 隐藏或隐藏(self):
        if self.可视:
            self.隐藏()
        else:
            self.显示()
            # 激活窗口
            self.activateWindow()
            # 设置焦点
            self.setFocus()

    def 退出(self):
        sys.exit(0)

    def 运行(self):
        print("运行python代码")
        运行(f"/usr/local/bin/python3.9 {self.属性表格窗口.设计窗口.写出文件路径AppPy}")

    def 编译为可执行程序(self):
        self.消息框("等待开发")

    def 信号_代码跳转(self, 状态, 错误文本):
        print("信号_代码跳转", 状态, 错误文本)
        if 状态 == True:
            if 系统_是否为mac系统():
                self.hide()
            else:
                # 窗口最小化
                self.setWindowState(Qt.WindowMinimized)
        else:
            self.setWindowTitle(错误文本)


if __name__ == '__main__':
    print(sys.argv)
    # 将命令行参数转换为json保存
    app = QApplication(sys.argv)
    window = MainWin()

    # window.show()
    sys.exit(app.exec())
