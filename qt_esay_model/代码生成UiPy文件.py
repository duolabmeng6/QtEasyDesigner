# 用于构建界面代码 app_启动窗口.py
import json
import os
import re

from 中文对照组件常量 import 取组件名称中英文对照
from 界面代码生成类 import 界面代码生成类
from 组件库.组件单行编辑框 import 组件单行编辑框
from 组件库.组件富文本编辑框 import 组件富文本编辑框
from 组件库.组件按钮 import 组件按钮
from 组件库.组件窗口 import 组件窗口
from 组件库.组件纯文本编辑框 import 组件纯文本编辑框


class 代码生成UiPy文件(object):
    界面代码生成: 界面代码生成类 = None
    组件数: object = None
    依赖组件列表 = []

    def __init__(self, json界面数据文件: str):
        self.界面代码生成 = 界面代码生成类()
        self.组件树 = json.loads(json界面数据文件)

        self.界面代码生成.加载已存在的文件内容 = ""
        self.界面代码生成.末尾代码 = """
        MainWindow.setCentralWidget(self.centralwidget)
        QMetaObject.connectSlotsByName(MainWindow)

class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWin()
    sys.exit(app.exec())
"""

    def 取头部依赖组件(self, 依赖组件=None):
        return f"""
# -*- coding: utf-8 -*-
import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, {依赖组件})
"""

    def 生成代码(self):
        pass
        self.递归(组件树=self.组件树)
        # set(self.依赖组件列表)
        依赖组件 = ", ".join(set(self.依赖组件列表))
        self.界面代码生成.头部导包代码 = self.取头部依赖组件(依赖组件)

        代码 = self.界面代码生成.生成代码UiPy()
        return 代码

    def 递归(self, 递归深度=0, 组件树=None):
        self.获取代码(组件树)
        for 子组件 in 组件树['子组件']:
            self.递归(递归深度=递归深度 + 1, 组件树=子组件)

    def 获取代码(self, 组件对象):
        窗口代码 = ""
        组件名称 = 组件对象['组件名称']
        组件类型 = 组件对象['组件类型']
        组件属性 = 组件对象['组件属性']
        # print(组件名称, 组件类型, 组件属性)
        self.依赖组件列表.append(组件类型)  # 依赖列表

        if 组件类型 == "QMainWindow":
            组件信息 = 组件窗口()
            窗口代码 = 组件信息.导出为代码(组件对象)
            self.界面代码生成.类初始化代码 = 窗口代码
            return ""

        父组件 = 组件对象['父组件']
        父组件类型 = 组件对象['父组件类型']
        if 组件类型 == "QWidget":  # 窗口组件
            self.界面代码生成.加入事件绑定代码(f"""
self.{组件名称} = QWidget(MainWindow)
self.{组件名称}.setObjectName(u"{组件名称}")
""")
        if 父组件类型 == "QTabWidget" and 组件类型 == "QWidget":  # 选择夹 组件
            self.界面代码生成.加入事件绑定代码(f"""
self.{组件名称} = QWidget()
self.{组件名称}.setObjectName(u"{组件名称}")
                               """)
            self.界面代码生成.加入事件绑定代码(f"""
self.{父组件}.addTab(self.{组件名称}, "")
        """, True)

            self.界面代码生成.加入事件绑定代码(f"""
self.{父组件}.setTabText(self.tabWidget.indexOf(self.{组件名称}), u"{组件属性['标题']}")
                """)

        if 组件类型 == "QTabWidget":  # 选项卡组件
            self.界面代码生成.加入事件绑定代码(f"""
self.{组件名称} = QTabWidget(self.{父组件})
self.{组件名称}.setObjectName(u"{组件名称}")
self.{组件名称}.setGeometry(QRect({组件属性['左边']}, {组件属性['顶边']}, {组件属性['宽度']}, {组件属性['高度']}))
                     """)
            self.界面代码生成.加入事件绑定代码(f"""
self.{组件名称}.setCurrentIndex(1)
            """, True)

        if 组件类型 == "QPushButton":  # 按钮组件
            组件信息 = 组件按钮()
            窗口代码 = 组件信息.导出为代码(组件对象)
        if 组件类型 == "QLineEdit":  # 组件单行编辑框
            组件信息 = 组件单行编辑框()
            窗口代码 = 组件信息.导出为代码(组件对象)
        if 组件类型 == "QPlainTextEdit":  # 组件单行编辑框
            组件信息 = 组件纯文本编辑框()
            窗口代码 = 组件信息.导出为代码(组件对象)
        if 组件类型 == "QTextEdit":  # 组件单行编辑框
            组件信息 = 组件富文本编辑框()
            窗口代码 = 组件信息.导出为代码(组件对象)

        if 组件名称 == "centralwidget":
            pass
        elif 窗口代码 == "":
            raise Exception("未知组件类型", 组件对象)

        self.界面代码生成.加入事件绑定代码(窗口代码)


if __name__ == "__main__":
    数据文件路径 = r"C:\pyefun\QtEsayDesigner\QtEsayDesigner\qt_esay_model\测试代码生成的目录\启动窗口.json"
    # 数据文件路径 = r"C:\pyefun\QtEsayDesigner\test\启动窗口.json"

    # os 取文件路径的目录
    项目目录 = os.path.dirname(数据文件路径)
    # 获取文件名不要扩展名
    窗口名称 = os.path.splitext(os.path.basename(数据文件路径))[0]

    with open(f"{项目目录}/{窗口名称}.json", "r", encoding="utf-8") as f:
        导入数据 = f.read()

    # 生成入口文件绑定事件
    python = 代码生成UiPy文件(导入数据).生成代码()
    print("生成的代码：", python)
    with open(f"{项目目录}/ui_{窗口名称}.py", "w", encoding="utf-8") as f:
        f.write(python)
