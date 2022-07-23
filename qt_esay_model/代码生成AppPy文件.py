# 用于构建界面代码 app_启动窗口.py
import json
import os
import re

from 中文对照组件常量 import 取组件名称中英文对照
from 中文对照组件常量 import 通过组件名称取组件库对象
from 界面代码生成类 import 界面代码生成类
from 组件库.组件单行编辑框 import 组件单行编辑框
from 组件库.组件富文本编辑框 import 组件富文本编辑框
from 组件库.组件按钮 import 组件按钮
from 组件库.组件纯文本编辑框 import 组件纯文本编辑框


class 代码生成AppPy文件(object):
    界面代码生成: 界面代码生成类 = None
    组件数: object = None

    def __init__(self, json界面数据文件: str, 已有数据: str = ""):
        self.界面代码生成 = 界面代码生成类()
        self.组件树 = json.loads(json界面数据文件)

        self.界面代码生成.加载已存在的文件内容 = 已有数据
        self.界面代码生成.末尾代码 = """
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWin()
    sys.exit(app.exec())
                """

    def 生成代码(self):
        pass
        self.递归(组件树=self.组件树)
        代码 = self.界面代码生成.生成代码()
        return 代码

    def 递归(self, 递归深度=0, 组件树=None):
        self.获取代码(组件树)
        for 子组件 in 组件树['子组件']:
            self.递归(递归深度=递归深度 + 1, 组件树=子组件)
        return

    def 获取代码(self, 组件对象):
        窗口代码 = ""
        组件名称 = 组件对象['组件名称']
        组件类型 = 组件对象['组件类型']
        组件属性 = 组件对象['组件属性']
        # print(组件名称, 组件类型, 组件属性)
        if 组件类型 == "QMainWindow":
            self.界面代码生成.加入导包模块头部代码("import sys")
            self.界面代码生成.加入导包模块头部代码("from PySide6.QtWidgets import *")
            self.界面代码生成.加入导包模块头部代码("from PySide6.QtGui import *")
            self.界面代码生成.加入导包模块头部代码("from PySide6.QtCore import *")
            self.界面代码生成.加入导包模块头部代码(f"""import ui_{组件名称}""")
            self.界面代码生成.加入组件汉化代码(f"""
self.ui = ui_{组件名称}.Ui_MainWindow()
self.ui.setupUi(self)
self.show() 
self.{组件名称} = self 
        """)
            self.界面代码生成.加入事件绑定代码(f"""self.{组件名称}创建完毕()""", True)

            self.界面代码生成.加入函数定义代码(f"""
def {组件名称}创建完毕(self):
    print("{组件名称}创建完毕")
            """)

            self.界面代码生成.类名 = "MainWin(主窗口)"
            self.界面代码生成.加入导包模块头部代码("""from qtefun.组件.主窗口 import 主窗口""")
            return ""

        父组件 = 组件对象['父组件']
        父组件类型 = 组件对象['父组件类型']

        导包名称 = 取组件名称中英文对照(组件类型)
        if 导包名称:
            self.界面代码生成.加入导包模块头部代码(f"""from qtefun.组件.{导包名称} import {导包名称}""")
            self.界面代码生成.加入组件汉化代码(f"self.{组件名称} = {导包名称}(self.ui.{组件名称})")
        else:
            pass
        for 属性 in 组件属性:
            # print(属性)
            是否存在属性 = 属性.startswith("事件") and 组件属性[属性] != "" and 组件属性[属性] != "None" and 组件属性[属性] != None
            if not 是否存在属性:
                continue
            print(组件名称, 组件类型, 组件属性)
            self.界面代码生成.加入事件绑定代码(
                f"""
self.{组件名称}.绑定{属性}(self.{组件属性[属性]})
                """
            )
            函数名称 = f"{组件属性[属性]}"
            事件名称 = 属性
            # if 组件类型 == "QPushButton":  # 按钮组件
            #     组件信息 = 组件按钮()
            #     函数定义代码 = 组件信息.导出事件代码(函数名称, 事件名称)
            # if 组件类型 == "QLineEdit":  # 组件单行编辑框
            #     组件信息 = 组件单行编辑框()
            #     函数定义代码 = 组件信息.导出事件代码(函数名称, 事件名称)
            # if 组件类型 == "QPlainTextEdit":  # 组件单行编辑框
            #     组件信息 = 组件纯文本编辑框()
            #     函数定义代码 = 组件信息.导出事件代码(函数名称, 事件名称)
            # if 组件类型 == "QTextEdit":  # 组件单行编辑框
            #     组件信息 = 组件富文本编辑框()
            #     函数定义代码 = 组件信息.导出事件代码(函数名称, 事件名称)

            组件库对象 = 通过组件名称取组件库对象(组件类型, None)
            if 组件库对象 is None:
                print("请补充组件 " + 组件类型)
                return
            函数定义代码 = 组件库对象.导出事件代码(函数名称, 事件名称)


            self.界面代码生成.加入函数定义代码(函数定义代码)


#             self.界面代码生成.加入函数定义代码(f"""
# def {组件属性[属性]}(self):
#     print("{组件属性[属性]}")
#             """)


if __name__ == "__main__":
    # 数据文件路径 = r"C:\pyefun\QtEasyDesigner\QtEasyDesigner\qt_esay_model\测试代码生成的目录\启动窗口.json"
    数据文件路径 = r"/Users/chensuilong/Desktop/pythonproject/pythonProject3/main.json"

    # os 取文件路径的目录
    项目目录 = os.path.dirname(数据文件路径)
    # 获取文件名不要扩展名
    窗口名称 = os.path.splitext(os.path.basename(数据文件路径))[0]

    with open(f"{项目目录}/{窗口名称}.json", "r", encoding="utf-8") as f:
        导入数据 = f.read()
    try:
        with open(f"{项目目录}/app_{窗口名称}.py", "r", encoding="utf-8") as f:
            已有数据 = f.read()
    except:
        已有数据 = ""

    # 生成入口文件绑定事件
    python = 代码生成AppPy文件(导入数据, 已有数据).生成代码()
    print("生成的代码：", python)
    with open(f"{项目目录}/app_{窗口名称}.py", "w", encoding="utf-8") as f:
        f.write(python)
