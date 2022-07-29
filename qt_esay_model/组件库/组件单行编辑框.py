# 实现 单行编辑框组件的构建 包括 创建组件 修改属性 导出属性 删除组件
import json
import sys
import PySide6
from PySide6.QtCore import QRect
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from 导出组件事件方法 import *
from 组件库.组件接口类 import *
from qtefun.组件.单行编辑框 import 单行编辑框


class 组件单行编辑框(组件接口类):
    对象: QLineEdit
    parent: QWidget
    事件列表: list = []

    def __init__(self, parent=None):
        pass
        self.parent = parent
        # 事件格式 (事件[事件名称], 回调函数参数)])
        # 最终生成格式 def 单行编辑框1内容被改变(self,内容):
        self.事件列表 = [
            # ("事件内容被改变", "内容"),
            # ("事件编辑完成", ""),
            # ("事件输入被拒绝", ""),
            # ("事件回车键被按下", ""),
            # ("事件选择区域发生变化", ""),
            # ("事件文本被编辑", "内容"),
        ]

        self.事件列表 = 导出类绑定事件函数(单行编辑框, '事件内容被改变')
        # print("事件列表",self.事件列表)

    def 创建组件(self, 名称, 左边=0, 顶边=0, 宽度=0, 高度=0, 组件属性=None):
        if 组件属性 is None:
            组件属性 = {}
        # 根据配置信息创建单行编辑框
        self.对象 = QLineEdit(self.parent)
        self.对象.setGeometry(QRect(左边, 顶边, 宽度, 高度))
        self.对象.setObjectName(名称)
        self.对象.setText(名称)
        self.对象.show()
        # def 内容被改变():
        #     print("内容被改变")
        #     组件单行编辑框.对象.text()
        # self.对象.textChanged.connect(内容被改变)
        # 设置组件属性
        for key in 组件属性:
            self.修改组件属性(key, 组件属性[key])
        return self.对象

    def 修改组件属性(self, 属性名称, 属性值):
        pass
        # print("修改组件属性", self.对象.objectName(), 属性名称, 属性值)
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
            print("可视", 属性值)
            属性值 = self.取逻辑值(属性值)
            print("可视", 属性值)
            self.对象.setVisible(属性值)
        if 属性名称 == "禁用":
            print("禁用", 属性值)
            属性值 = self.取逻辑值(属性值)
            print("禁用", 属性值)
            self.对象.setEnabled(属性值 == False)
        # 检查属性名前缀 "事件"
        if 属性名称.startswith("事件"):
            self.对象.setProperty(属性名称, 属性值)

        if 属性名称 == "内容":
            self.对象.setText(属性值)

    def 导出组件属性(self):
        pass
        组件类型 = self.对象.metaObject().className()
        组件属性 = [
            ("组件类型", "文本型", 组件类型),
            ("名称", "文本型", self.对象.objectName()),
            ("左边", "整数型", self.对象.geometry().left()),
            ("顶边", "整数型", self.对象.geometry().top()),
            ("宽度", "整数型", self.对象.geometry().width()),
            ("高度", "整数型", self.对象.geometry().height()),
            ("可视", "逻辑值", 1 if self.对象.isVisible() else 0),
            ("禁用", "逻辑值", 1 if self.对象.isEnabled() == False else 0),
            ("内容", "文本型", self.对象.text()),
            # ("事件内容被改变", "文本型", self.对象.property("事件内容被改变")),
        ]
        # 添加事件属性
        for 事件 in self.事件列表:
            组件属性.append((事件[0], "文本型", self.对象.property(事件[0])))
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
        self.{组件名称} = QLineEdit(self.{父组件})
        self.{组件名称}.setObjectName(u"{组件名称}")
        self.{组件名称}.setGeometry(QRect({组件属性['左边']}, {组件属性['顶边']}, {组件属性['宽度']}, {组件属性['高度']}))
        self.{组件名称}.setText("{组件属性['内容']}")
                """
        return 窗口代码


if __name__ == "__main__":
    def 测试导出代码():
        组件信息 = 组件单行编辑框()
        json的数据 = """
                  {
                    "组件名称": "单行编辑框2",
                    "组件类型": "QLineEdit",
                    "组件属性": {
                        "组件类型": "QLineEdit",
                        "名称": "单行编辑框2",
                        "左边": 193,
                        "顶边": 84,
                        "宽度": 111,
                        "高度": 93,
                        "可视": 1,
                        "禁用": 0,
                        "内容": "单行编辑框2"
                    },
                    "父组件": "centralwidget",
                    "父组件类型": "QWidget",
                    "子组件": []
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
    w.show()

    # 创建组件
    组件单行编辑框 = 组件单行编辑框(w)
    组件单行编辑框.创建组件("单行编辑框", 顶边=10, 左边=100, 宽度=100, 高度=100)
    组件单行编辑框.修改组件属性("事件被点击", "事件" + 组件单行编辑框.对象.objectName() + "被点击")
    组件单行编辑框.修改组件属性("内容", "事件" + 组件单行编辑框.对象.objectName() + "被点击")
    # 绑定内容被改变事件

    # 导出组件属性
    # 导出数据 = 组件单行编辑框.导出组件属性()
    导出数据 = 组件单行编辑框.导出为json属性()
    # 导出为 json 格式 打印出来
    print(json.dumps(导出数据, indent=4, ensure_ascii=False))
    # 删除组件
    组件单行编辑框.删除组件()

    组件单行编辑框.创建组件("单行编辑框", 组件属性=导出数据)

    print("事件代码", 组件单行编辑框.导出事件代码("xxx", "事件内容被改变"))

    # 创建组件库
    sys.exit(app.exec())
