# 实现组件的接口
import abc
from abc import ABCMeta

from PySide6.QtWidgets import QWidget
from qt_esay_model.导出组件事件方法 import 导出类绑定事件函数

class 组件接口类(metaclass=ABCMeta):
    对象: object = None
    parent: QWidget

    事件列表: list = []

    @abc.abstractmethod
    def 创建组件(self):
        pass

    @abc.abstractmethod
    def 修改组件属性(self):
        pass

    # @abc.abstractmethod
    def 导出事件代码(self, 函数名称, 事件名称):
        # 查找事件列表中参数
        # print("导出事件代码")
        # print(函数名称)
        # print(事件名称)
        # print(self.事件列表)

        参数 = ""
        for 事件 in self.事件列表:
            if 事件[0] == 事件名称:
                参数 = 事件[1]
                break
        if 参数 == "":
            参数 = "self"
        else:
            参数 = "self," + 参数

        窗口代码 = f"""
def {函数名称}({参数}):
    print("{函数名称}")
                    """
        return 窗口代码

    @abc.abstractmethod
    def 导出组件属性(self):
        pass

    def 取逻辑值(self, 值):
        if 值 == True:
            return True
        if 值 == "真" or 值 == 'True' or 值 == 'true':
            return True
        if str(值) == '1':
            return True
        return False
