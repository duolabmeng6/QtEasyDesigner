# 实现 按钮组件的构建 包括 创建组件 修改属性 导出属性 删除组件
import json
import sys
import PySide6
from PySide6.QtCore import QRect
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class 组件窗口(object):
    对象: QMainWindow
    parent: QMainWindow

    def __init__(self, parent=None):
        pass
        self.parent = parent
        self.对象 = parent


    def 创建组件(self, 名称, 左边=0, 顶边=0, 宽度=0, 高度=0, 组件属性=None):
        pass


    def 取逻辑值(self, 值):
        if 值 == True:
            return True
        if 值 == "真" or 值 == 'True' or 值 == 'true':
            return True
        if str(值) == '1':
            return True
        return False

    def 修改组件属性(self, 属性名称, 属性值):
        pass
        print("修改组件属性", self.对象.objectName(), 属性名称, 属性值)
        if 属性名称 == "名称":
            self.对象.setObjectName(属性值)
        if 属性名称 == "左边":
            self.对象.setGeometry(int(属性值), self.对象.y(), self.对象.width(), self.对象.height())
        if 属性名称 == "顶边":
            self.对象.setGeometry(self.对象.x(), int(属性值), self.对象.width(), self.对象.height())
        if 属性名称 == "宽度":
            self.对象.setGeometry(self.对象.x(), self.对象.y(), int(属性值), self.对象.height())
        if 属性名称 == "高度":
            self.对象.setGeometry(self.对象.x(), self.对象.y(), self.对象.width(), int(属性值))
        if 属性名称 == "可视":
            pass
            # print("可视", 属性值)
            # 属性值 = self.取逻辑值(属性值)
            # print("可视", 属性值)
            # self.对象.setVisible(属性值)
        if 属性名称 == "禁用":
            print("禁用", 属性值)
            属性值 = self.取逻辑值(属性值)
            print("禁用", 属性值)
            self.对象.setEnabled(属性值 == False)
        if 属性名称 == "标题":
            self.对象.setWindowTitle(属性值)

        # 检查属性名前缀 "事件"
        if 属性名称.startswith("事件"):
            self.对象.setProperty(属性名称, 属性值)

    def 导出组件属性(self):
        pass
        事件被点击 = self.对象.property("事件创建完毕")
        if 事件被点击 is None:
            事件被点击 = ""
        组件属性 = [
            ("组件类型", "文本型", 'QMainWindow'),
            ("名称", "文本型", self.对象.objectName()),
            ("左边", "整数型", 0),
            ("顶边", "整数型", 0),
            ("宽度", "整数型", self.对象.geometry().width()),
            ("高度", "整数型", self.对象.geometry().height()),
            ("可视", "逻辑值", 1 if self.对象.isVisible() else 0),
            ("禁用", "逻辑值", 1 if self.对象.isEnabled() == False else 0),
            ("标题", "文本型", self.对象.windowTitle()),
            ("事件创建完毕", "文本型", 事件被点击)
        ]
        # print("组件属性",组件属性)
        return 组件属性

    def 导出为json属性(self):
        pass
        组件属性 = self.导出组件属性()
        # 将组件属性的第0个和第3个数据导出为 键值对
        组件属性_json = {}
        for i in range(len(组件属性)):
            组件属性_json[组件属性[i][0]] = 组件属性[i][2]

        return 组件属性_json

    def 删除组件(self):
        pass
        # 删除组件
        self.对象.deleteLater()


    def 导出为代码(self, json的数据=None):

        组件名称 = json的数据["组件名称"]
        组件属性 = json的数据["组件属性"]
        父组件 = json的数据["父组件"]
        父组件类型 = json的数据["父组件类型"]

        窗口代码 = f"""
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"{组件名称}")
        MainWindow.resize({组件属性['宽度']}, {组件属性['高度']})
        MainWindow.setWindowTitle(u"{组件属性['标题']}")
                """
        return 窗口代码


if __name__ == "__main__":
    def 测试导出代码():
        组件信息 = 组件窗口()
        json的数据 = """
                {
             "组件名称": "空白窗口",
            "组件类型": "QMainWindow",
            "组件属性": {
                "组件类型": "QMainWindow",
                "名称": "空白窗口",
                "左边": 0,
                "顶边": 0,
                "宽度": 500,
                "高度": 500,
                "可视": 1,
                "禁用": 0,
                "标题": "123",
                "事件创建完毕": "空白窗口创建完毕"
            },
            "父组件": "根组件",
            "父组件类型": "根组件"
                }
            """
        json的数据 = json.loads(json的数据)
        print(组件信息.导出为代码(json的数据))

    # 测试导出代码()
    # sys.exit()

    app = QApplication([])
    # 创建窗口 400x400
    w = QMainWindow()
    w.resize(400, 400)
    w.setWindowTitle("构建组件测试")
    w.setObjectName("构建组件测试")
    w.show()

    # 创建组件
    组件按钮 = 组件窗口(w)

    # 导出组件属性
    # 导出数据 = 组件按钮.导出组件属性()
    导出数据 = 组件按钮.修改组件属性("事件创建完毕", "窗口创建完毕")
    导出数据 = 组件按钮.修改组件属性("宽度", 600)
    导出数据 = 组件按钮.修改组件属性("高度", 500)
    导出数据 = 组件按钮.修改组件属性("标题", "测试")
    导出数据 = 组件按钮.导出为json属性()
    # 导出为 json 格式 打印出来
    print(json.dumps(导出数据, indent=4, ensure_ascii=False))


    # 创建组件库
    sys.exit(app.exec())
