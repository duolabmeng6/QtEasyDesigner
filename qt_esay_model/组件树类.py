# 记录创建组件的层级关系和属性 树状结构
import json
import os
import re
import sys
# 添加当前文件的父目录的父目录
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from qt_esay_model.中文对照组件常量 import 取组件名称中英文对照
from qt_esay_model.组件库.组件单行编辑框 import 组件单行编辑框
from qt_esay_model.组件库.组件富文本编辑框 import 组件富文本编辑框
from qt_esay_model.组件库.组件按钮 import 组件按钮
from qt_esay_model.组件库.组件窗口 import 组件窗口
from qt_esay_model.组件库.组件纯文本编辑框 import 组件纯文本编辑框
from qt_esay_model.代码生成类 import 界面代码生成类


class 组件树类:

    def __init__(self, 组件名称="", 组件类型="", 组件属性=""):
        self.组件名称 = 组件名称
        self.组件类型 = 组件类型
        self.组件属性 = 组件属性
        self.子组件 = []
        self.父组件 = None

    def 添加子组件(self, 子组件):
        self.子组件.append(子组件)
        子组件.父组件 = self

    def 打印组件结构(self, 缩进):
        # 打印组件的结构和属性值
        if self.父组件 is None:
            父组件名称 = "根组件"
        else:
            父组件名称 = self.父组件.组件名称
        print("{}{} 父:{} {}:{}".format(缩进, self.组件名称, 父组件名称, self.组件类型, self.组件属性))
        for 子组件 in self.子组件:
            子组件.打印组件结构(缩进 + '    ')

    def 导出组件结构数据(self):
        if self.父组件 is None:
            父组件名称 = "根组件"
            父组件类型 = "根组件"
        else:
            父组件名称 = self.父组件.组件名称
            父组件类型 = self.父组件.组件类型

        结构数据 = {
            '组件名称': self.组件名称,
            '组件类型': self.组件类型,
            '组件属性': self.组件属性,
            '父组件': 父组件名称,
            '父组件类型': 父组件类型,
            '子组件': [],
        }
        for 子组件 in self.子组件:
            结构数据['子组件'].append(子组件.导出组件结构数据())
        return 结构数据

    def 导出组件结构数据_json(self):
        return json.dumps(self.导出组件结构数据(), indent=4, ensure_ascii=False)


class 组件树生成代码类:

    def __init__(self, json数据):
        # print(json数据)
        self.组件树 = json.loads(json数据)

    依赖组件列表 = []  # 头部的依赖组件 也就是 组件类型
    retranslateUi = []
    循环结束补充代码 = []
    qtefun依赖列表 = []

    def 添加循环结束补充代码(self, 补充代码):
        self.循环结束补充代码.append(补充代码)

    def 获取代码(self, 组件对象):
        窗口代码 = ""
        组件名称 = 组件对象['组件名称']
        组件类型 = 组件对象['组件类型']
        组件属性 = 组件对象['组件属性']
        父组件 = 组件对象['父组件']
        父组件类型 = 组件对象['父组件类型']
        self.依赖组件列表.append(组件类型)  # 依赖列表
        # 代码 += '{} = {}({})'.format(组件名称, 组件类型, 组件属性)
        if 组件类型 == "QMainWindow":  # 窗口
            组件信息 = 组件窗口()
            窗口代码 = 组件信息.导出为代码(组件对象)
        #
        #             窗口代码 = f"""
        # class Ui_MainWindow(object):
        #     def setupUi(self, MainWindow):
        #         if not MainWindow.objectName():
        #             MainWindow.setObjectName(u"{组件名称}")
        #         MainWindow.resize({组件属性['宽度']}, {组件属性['高度']})
        #         MainWindow.setWindowTitle(u"{组件属性['标题']}")
        #             """
        #             更新界面代码 = f"""
        #         MainWindow.setWindowTitle(u"{组件属性['标题']}")
        #             """
        #             self.retranslateUi.append(更新界面代码)

        if 组件类型 == "QWidget":  # 窗口组件
            窗口代码 = f"""
        self.{组件名称} = QWidget(MainWindow)
        self.{组件名称}.setObjectName(u"{组件名称}")
                     """

        if 父组件类型 == "QTabWidget" and 组件类型 == "QWidget":  # 选择夹 组件
            窗口代码 = f"""
        self.{组件名称} = QWidget()
        self.{组件名称}.setObjectName(u"{组件名称}")
                               """
            self.添加循环结束补充代码(f"""
        self.{父组件}.addTab(self.{组件名称}, "")
        """)

            更新界面代码 = f"""
        self.{父组件}.setTabText(self.tabWidget.indexOf(self.{组件名称}), u"{组件属性['标题']}")
                """
            self.retranslateUi.append(更新界面代码)

        if 组件类型 == "QTabWidget":  # 选项卡组件
            窗口代码 = f"""
        self.{组件名称} = QTabWidget(self.{父组件})
        self.{组件名称}.setObjectName(u"{组件名称}")
        self.{组件名称}.setGeometry(QRect({组件属性['左边']}, {组件属性['顶边']}, {组件属性['宽度']}, {组件属性['高度']}))
                     """
            self.添加循环结束补充代码(f"""
        self.{组件名称}.setCurrentIndex(1)
            """)

        if 组件类型 == "QPushButton":  # 按钮组件
            组件信息 = 组件按钮()
            窗口代码 = 组件信息.导出为代码(组件对象)
            # print(窗口代码)
        #     窗口代码 = f"""
        # self.{组件名称} = QPushButton(self.{父组件})
        # self.{组件名称}.setObjectName(u"{组件名称}")
        # self.{组件名称}.setGeometry(QRect({组件属性['左边']}, {组件属性['顶边']}, {组件属性['宽度']}, {组件属性['高度']}))
        #              """
        #     更新界面代码 = f"""
        # self.{组件名称}.setText("{组件属性['标题']}")
        #         """
        #     self.retranslateUi.append(更新界面代码)
        if 组件类型 == "QLineEdit":  # 组件单行编辑框
            组件信息 = 组件单行编辑框()
            窗口代码 = 组件信息.导出为代码(组件对象)
        if 组件类型 == "QPlainTextEdit":  # 组件单行编辑框
            组件信息 = 组件纯文本编辑框()
            窗口代码 = 组件信息.导出为代码(组件对象)
        if 组件类型 == "QTextEdit":  # 组件单行编辑框
            组件信息 = 组件富文本编辑框()
            窗口代码 = 组件信息.导出为代码(组件对象)

        if 窗口代码 == "":
            raise Exception("未知组件类型", 组件对象)
        return 窗口代码

    def 末尾代码(self):
        return """
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)


        """

    def 界面文本生成(self):

        return f"""
    def retranslateUi(self,MainWindow):
        pass
{"".join(self.retranslateUi)}
    # retranslateUi
        """

    def 调用函数代码(self):
        return """
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

    def 头部代码(self, 依赖组件):
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

    def 填充循环后的代码(self):
        if len(self.循环结束补充代码) == 0:
            return ""
        return self.循环结束补充代码.pop()

    def 生成代码(self):
        代码 = self.头部代码("")
        代码 = 代码 + self.获取代码(self.组件树)
        for 子组件 in self.组件树['子组件']:
            代码 = 代码 + self.获取代码(子组件)
            for 子组件2 in 子组件['子组件']:
                代码 = 代码 + self.获取代码(子组件2)
                for 子组件3 in 子组件2['子组件']:
                    代码 = 代码 + self.获取代码(子组件3)
                    for 子组件4 in 子组件3['子组件']:
                        代码 = 代码 + self.获取代码(子组件4)
                    # ---
                    代码 = 代码 + self.填充循环后的代码()
                # ---
                代码 = 代码 + self.填充循环后的代码()
            # ---
            代码 = 代码 + self.填充循环后的代码()
        # ---
        代码 = 代码 + self.填充循环后的代码()

        代码 = 代码 + self.末尾代码()
        代码 = 代码 + self.界面文本生成()
        代码 = 代码 + self.调用函数代码()

        return 代码

    def 生成代码2(self):

        代码 = ""
        代码 = self.递归(组件树=self.组件树)
        依赖组件 = ", ".join(set(self.依赖组件列表))
        头部代码 = self.头部代码(依赖组件)
        代码 = 头部代码 + 代码

        代码 = 代码 + self.末尾代码()
        代码 = 代码 + self.界面文本生成()
        代码 = 代码 + self.调用函数代码()
        return 代码

    def 递归(self, 递归深度=0, 组件树=None, 代码=""):
        代码 = 代码 + self.获取代码(组件树)
        for 子组件 in 组件树['子组件']:
            代码 = self.递归(递归深度=递归深度 + 1, 组件树=子组件, 代码=代码)
        代码 = 代码 + self.填充循环后的代码()
        return 代码

    def 删除空行(self, 文本):
        pass
        代码 = re.sub(r"\n\s*\n", "\n", 文本)
        # print(代码)
        return 代码

    def 取qtefun依赖组件(self):
        self.qtefun依赖列表 = set(self.qtefun依赖列表)
        代码 = ""
        for 导包名称 in self.qtefun依赖列表:
            # if 导包名称 == None:
            #     continue
            # if 导包名称 == "None":
            #     continue
            # if 导包名称 == "":
            #     continue
            代码 = 代码 + f"""
from qtefun.组件.{导包名称} import {导包名称}
            """
        return 代码

    def 生成代码4_入口函数(self, 加载已存在的文件内容=""):
        # self.代码生成类 = 代码生成
        self.界面代码生成 = 界面代码生成类()
        self.加载已存在的文件内容 = 加载已存在的文件内容
        self.界面代码生成.加载已存在的文件内容 = 加载已存在的文件内容
        self.界面代码生成.末尾代码 = """
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWin()
    sys.exit(app.exec())
            """
        self.递归4(组件树=self.组件树)
        代码 = self.界面代码生成.生成代码()
        return 代码

    def 递归4(self, 递归深度=0, 组件树=None):
        self.获取代码4(组件树)
        for 子组件 in 组件树['子组件']:
             self.递归4(递归深度=递归深度 + 1, 组件树=子组件)
        return

    def 获取代码4(self, 组件对象):
        窗口代码 = ""
        组件名称 = 组件对象['组件名称']
        组件类型 = 组件对象['组件类型']
        组件属性 = 组件对象['组件属性']
        # print(组件名称, 组件类型, 组件属性)
        if 组件类型 == "QMainWindow":
            self.界面代码生成.加入导包模块头部代码("import sys")
            self.界面代码生成.加入导包模块头部代码("from PySide6.QtWidgets import QApplication")
            self.界面代码生成.加入导包模块头部代码("from PySide6.QtWidgets import QMainWindow")
            self.界面代码生成.加入导包模块头部代码(f"""import ui_{组件名称}""")
            self.界面代码生成.加入事件绑定代码(f"""
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
            self.界面代码生成.加入事件绑定代码(f"self.{组件名称} = {导包名称}(self.ui.{组件名称})")
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
            self.界面代码生成.加入函数定义代码(f"""
def {组件属性[属性]}(self):
    print("{组件属性[属性]}")
            """)

    def 生成代码3_入口函数(self, 加载已存在的文件内容=""):
        self.加载已存在的文件内容 = 加载已存在的文件内容

        self.导包 = ""
        self.定义def = ""
        绑定事件 = self.删除空行(self.递归2(组件树=self.组件树))

        if 加载已存在的文件内容 == "":
            # 导入依赖组件

            代码 = "# ==导入模块==\n" + self.删除空行(self.头部代码入口()) + self.删除空行(self.导包) + self.取qtefun依赖组件() + "\n# ==导入模块==="
            代码 = 代码 + self.删除空行(self.类定义代码入口())
            代码 = 代码 + "# ==绑定事件==\n" + self.删除空行(self.定义入口代码 + 绑定事件) + "\n        # ==绑定事件==="
            代码 = 代码 + self.定义def
            代码 = 代码 + self.删除空行(self.末尾代码入口())
            代码 = self.删除空行(代码)
            return 代码
        # 处理已经存在的文件插入函数的话需要做替换
        # 替换的点位导包部分 # ==导入模块开始== # ==导入模块结束==
        导包部分代码 = self.头部代码入口() + self.导包 + self.取qtefun依赖组件()
        t = self.替换导入模块(加载已存在的文件内容, 导包部分代码, "导入模块", "")

        绑定事件部分代码 = self.定义入口代码 + 绑定事件
        t = self.替换导入模块(t, 绑定事件部分代码, "绑定事件", "        ")

        # 找到 "# ==绑定事件===" 的位置
        开始位置 = t.find("# ==绑定事件===") + len("# ==绑定事件===")
        # 从 开始位置这里插入文本 hello
        t = t[:开始位置] + self.定义def + t[开始位置:]

        return t

    def 替换导入模块(self, 代码, 替换内容, 模块名称, 缩进):
        # 使用正则表达式替换 "# ==导入模块开始==" 和 "# ==导入模块结束==" 之间的所有内容
        v = 代码
        开始 = f"# =={模块名称}=="
        结束 = f"# =={模块名称}==="

        替换内容 = 开始 + "\n" + 替换内容 + "\n" + 缩进 + 结束
        替换内容 = self.删除空行(替换内容)

        v = re.sub(开始 + r'.*' + 结束, 替换内容, v, flags=re.DOTALL)
        return v

    def 头部代码入口(self):
        return """
import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
        """

    def 末尾代码入口(self):
        return """
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWin()
    sys.exit(app.exec())
        """

    def 类定义代码入口(self):
        return """
class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()

        
        """

    def 递归2(self, 递归深度=0, 组件树=None, 代码=""):
        代码 = 代码 + self.获取代码2(组件树)
        for 子组件 in 组件树['子组件']:
            代码 = self.递归2(递归深度=递归深度 + 1, 组件树=子组件, 代码=代码)
        return 代码

    def 插入def并且检查是否存在(self, 函数名: str, 代码):
        # 检查 加载已存在的文件内容 是否存在 函数名 存在不累加到 定义def中
        if re.search(f"def {函数名}", self.加载已存在的文件内容):
            pass
            print(f"插入def并且检查是否存在 {函数名} 已存在")
        else:
            self.定义def = self.定义def + 代码

    def 获取代码2(self, 组件对象):
        窗口代码 = ""
        组件名称 = 组件对象['组件名称']
        组件类型 = 组件对象['组件类型']
        组件属性 = 组件对象['组件属性']
        # print(组件名称, 组件类型, 组件属性)

        if 组件类型 == "QMainWindow":
            self.导包 = f"""
import ui_{组件名称}
            """
            self.定义入口代码 = f"""
        self.ui = ui_{组件名称}.Ui_MainWindow()
        self.ui.setupUi(self)
        self.{组件名称}创建完毕()
        self.show() 
        self.{组件名称} = self 
        """
            self.插入def并且检查是否存在(f"{组件名称}创建完毕", f"""
    def {组件名称}创建完毕(self):
        print("{组件名称}创建完毕")
            """)
            self.qtefun依赖列表.append("主窗口")

            return ""

        父组件 = 组件对象['父组件']
        父组件类型 = 组件对象['父组件类型']
        # 遍历所有的  判断组件属性前缀是否有 "事件"

        导包名称 = 取组件名称中英文对照(组件类型)
        #         导包x = f"""
        # from qtefun.组件.{导包名称} import {导包名称}
        #         """

        汉化代码 = ""
        if 导包名称:
            self.qtefun依赖列表.append(导包名称)
            汉化代码 = f"""
        self.{组件名称} = {导包名称}(self.ui.{组件名称})
            """
        else:
            pass

        绑定事件 = ""
        保留代码 = False
        for 属性 in 组件属性:
            # print(属性)
            if 属性.startswith("事件") and 组件属性[属性] != "" and 组件属性[属性] != "None" and 组件属性[属性] != None:
                保留代码 = True
                # 如果有  则添加事件代码
                print(组件名称, 组件类型, 组件属性)
                绑定事件 = 绑定事件 + f"""
        self.{组件名称}.绑定{属性}(self.{组件属性[属性]})
                """
                self.插入def并且检查是否存在(f"{组件属性[属性]}", f"""
    def {组件属性[属性]}(self):
        print("{组件属性[属性]}")
                """)

        # if 保留代码:
        #     pass
        #     # 检查导包中是否已经存在了导包x
        #     # if 导包x not in self.导包:
        #     #     self.导包 = self.导包 + 导包x
        # else:
        #     汉化代码 = ""
        #     绑定事件 = ""

        return 汉化代码 + 绑定事件


def 导入导出组件结构数据(结构数据, 递归深度=False, 递归导入对象=None):
    组件名称 = 结构数据['组件名称']
    组件类型 = 结构数据['组件类型']
    组件属性 = 结构数据['组件属性']
    # print("导入组件结构数据", 组件名称, 组件类型, 组件属性)
    if 递归深度 == False:
        递归导入对象 = 组件树类(组件名称, 组件类型, 组件属性)
    for 子组件 in 结构数据['子组件']:
        子组件类型 = 子组件['组件类型']
        子组件名称 = 子组件['组件名称']
        子组件属性 = 子组件['组件属性']
        容器 = 组件树类(子组件名称, 子组件类型, 子组件属性)
        递归导入对象.添加子组件(容器)
        导入导出组件结构数据(子组件, True, 容器)
    return 递归导入对象


if __name__ == "__main__":
    # 窗口 = 组件树类('主窗口', 'QMainWindow', {"左边": 0, "顶边": 0, "宽度": 800, "高度": 600, "可视": 1, "禁止": 0, "标题": "窗口"})
    # 容器 = 组件树类('centralwidget', 'QWidget', {})
    # 窗口.添加子组件(容器)
    # 选择夹 = 组件树类('tabWidget', 'QTabWidget', {"左边": 50, "顶边": 30, "宽度": 291, "高度": 281, "可视": 1, "禁止": 0})
    # 容器.添加子组件(选择夹)
    # 选择夹项目1 = 组件树类('项目1', 'QWidget', {"标题": "项目1"})
    # 选择夹.添加子组件(选择夹项目1)
    # 选择夹项目2 = 组件树类('项目2', 'QWidget', {"标题": "项目2"})
    # 选择夹.添加子组件(选择夹项目2)
    #
    # 选择夹项目1.添加子组件(
    #     组件树类('按钮_1', "QPushButton", {"左边": 120, "顶边": 50, "宽度": 113, "高度": 32, "可视": 1, "禁止": 0, "标题": "按钮1"}))
    #
    # 选择夹项目2.添加子组件(
    #     组件树类('按钮_2', "QPushButton", {"左边": 90, "顶边": 60, "宽度": 113, "高度": 32, "可视": 1, "禁止": 0, "标题": "按钮1"}))
    #
    # # 窗口.打印组件结构("--")
    # 导出数据 = 窗口.导出组件结构数据_json()
    # # 写到文件
    # with open("test.json", "w", encoding="utf-8") as f:
    #     f.write(导出数据)

    # python = 组件树生成代码类(窗口.导出组件结构数据_json()).生成代码()
    # print(python)
    # # 写出文件
    # with open("test.py", "w", encoding="utf-8") as f:
    #     f.write(python)
    #
    # with open("test.json", "r", encoding="utf-8") as f:
    #     数据 = f.read()
    #
    # python = 组件树生成代码类(数据).生成代码2()
    # print(python)
    # # 写出文件
    # with open("test.py", "w", encoding="utf-8") as f:
    #     f.write(python)

    # 导入数据
    # with open("test.json", "r", encoding="utf-8") as f:
    #     导入数据 = f.read()

    # 导入数据 = json.loads(导入数据)
    # 窗口 = 导入导出组件结构数据(导入数据)

    # 导出数据 = 窗口.导出组件结构数据_json()
    # # 写到文件
    # with open("test2.json", "w", encoding="utf-8") as f:
    #     f.write(导出数据)
    #
    # python = 组件树生成代码类(导出数据).生成代码2()
    # # 写出文件
    # with open("test2.py", "w", encoding="utf-8") as f:
    #     f.write(python)

    # python入口 = 组件树生成代码类(导入数据).生成代码3_入口函数()
    # with open("test3.py", "w", encoding="utf-8") as f:
    #     f.write(python入口)

    # 重新测试
    窗口名称 = "启动窗口"
    dirpath = r"C:/pyefun/QtEsayDesigner/test"
    with open(f"{dirpath}/{窗口名称}.json", "r", encoding="utf-8") as f:
        导入数据 = f.read()
        # 导入数据 = json.loads(导入数据)

    print(导入数据)
    # 生成ui的代码 ui组件文件禁止修改的
    python = 组件树生成代码类(导入数据).生成代码2()
    with open(f"{dirpath}/ui_{窗口名称}.py", "w", encoding="utf-8") as f:
        f.write(python)

    # 文件存在则读入不存在创建

    # #
    # try:
    #     加载已存在的文件内容 = open(f"{dirpath}/app_{窗口名称}.py", "r", encoding="utf-8").read()
    # except:
    #     pass
    加载已存在的文件内容 = ""

    # 生成入口文件绑定事件
    python = 组件树生成代码类(导入数据).生成代码4_入口函数(加载已存在的文件内容)
    print(python)
    with open(f"{dirpath}/app_{窗口名称}.py", "w", encoding="utf-8") as f:
        f.write(python)
