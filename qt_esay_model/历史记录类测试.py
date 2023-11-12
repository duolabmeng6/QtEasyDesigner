# PySide6 创建一个空白窗口 400x400 标题为 测试窗口
import sys

from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from qt_esay_model import 历史记录类


class Example(QWidget):
    操作记录: 历史记录类

    def __init__(self):
        super().__init__()
        self.setWindowTitle("测试窗口")
        self.resize(400, 400)
        self.show()
        # 监听键盘是否按下 ctrl+z 快捷键 撤消
        self.shortcut = QShortcut(QKeySequence("Ctrl+z"), self)
        self.shortcut.activated.connect(self.撤消)
        # 监听键盘是否按下 ctrl+y 快捷键 恢复
        self.shortcut = QShortcut(QKeySequence("Ctrl+y"), self)
        self.shortcut.activated.connect(self.恢复)
        self.操作记录 = 历史记录类.历史记录类()

        # 创建一个按钮

        # self.button.deleteLater()

        self.操作记录.开始记录()

        def 创建组件(传递数据):
            print("恢复组件", 传递数据)
            button = QPushButton(self)
            button.setGeometry(传递数据['左边'], 传递数据['顶边'], 100, 100)
            button.show()
            传递数据['组件对象'] = button
            return 传递数据

        def 创建组件恢复(传递数据):
            print("恢复组件", 传递数据)
            组件 = 传递数据['组件对象']
            组件.deleteLater()
            del 传递数据['组件对象']
            return 传递数据

        self.操作记录.开始记录()
        self.操作记录.添加("创建组件", {"左边": 0, "顶边": 0}, 创建组件, 创建组件恢复)
        self.操作记录.提交记录()

        self.操作记录.开始记录()
        self.操作记录.添加("创建组件", {"左边": 100, "顶边": 100}, 创建组件, 创建组件恢复)
        self.操作记录.提交记录()

        self.操作记录.开始记录()
        记录对象 = self.操作记录.添加("创建组件", {"左边": 200, "顶边": 200}, 创建组件, 创建组件恢复)
        self.操作记录.提交记录()

        #
        def 修改属性(传递数据):
            print("修改属性", 传递数据)
            组件对象 = 记录对象['组件对象']
            传递数据["原左边"] = 组件对象.geometry().left()
            传递数据["原顶边"] = 组件对象.geometry().top()
            组件对象.setGeometry(传递数据['左边'], 传递数据['顶边'], 100, 100)
            return 传递数据

        def 修改属性恢复(传递数据):
            print("修改属性恢复", 传递数据)
            组件对象.setGeometry(传递数据['原左边'], 传递数据['原顶边'], 100, 100)
            return 传递数据

        组件对象 = 记录对象['组件对象']
        self.操作记录.开始记录()
        self.操作记录.添加("修改属性", {"组件对象": 组件对象, "左边": 300, "顶边": 300}, 修改属性, 修改属性恢复)
        self.操作记录.提交记录()

    def 撤消(self):
        print("撤消")
        # 删除按钮
        self.操作记录.撤消记录()

    def 恢复(self):
        print("恢复")
        self.操作记录.恢复记录()


app = QApplication(sys.argv)
window = Example()

sys.exit(app.exec_())
