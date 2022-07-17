from 组件库.组件列表框 import 组件列表框
from 组件库.组件单行编辑框 import 组件单行编辑框
from 组件库.组件单选框 import 组件单选框
from 组件库.组件复选框 import 组件复选框
from 组件库.组件富文本编辑框 import 组件富文本编辑框
from 组件库.组件按钮 import 组件按钮
from 组件库.组件标签 import 组件标签
from 组件库.组件纯文本编辑框 import 组件纯文本编辑框


class 组件数据:
    组件中英文对照 = {
        "主窗口": "QMainWindow",
        "按钮": "QPushButton",
        "标签": "QLabel",
        "单行编辑框": "QLineEdit",
        "纯文本编辑框": "QPlainTextEdit",
        "富文本编辑框": "QTextEdit",
        "复选框": "QCheckBox",
        "单选框": "QRadioButton",
        "列表框": "QListWidget",
    }


# 互换键值对并且加入
def 取组件名称中英文对照(名称):
    vv = 组件数据.组件中英文对照.copy()
    vv.update({v: k for k, v in vv.items()})
    name = vv.get(名称, False)
    return name


def 取所有组件名称():
    return 组件数据.组件中英文对照.keys()


def 通过组件名称取组件库对象(组件类型, 父容器=None):
    if 组件类型 == "QPushButton":
        组件库对象 = 组件按钮(父容器)
    elif 组件类型 == "QLineEdit":
        组件库对象 = 组件单行编辑框(父容器)
    elif 组件类型 == "QTextEdit":
        组件库对象 = 组件富文本编辑框(父容器)
    elif 组件类型 == "QPlainTextEdit":
        组件库对象 = 组件纯文本编辑框(父容器)
    elif 组件类型 == "QLabel":
        组件库对象 = 组件标签(父容器)
    elif 组件类型 == "QCheckBox":
        组件库对象 = 组件复选框(父容器)
    elif 组件类型 == "QRadioButton":
        组件库对象 = 组件单选框(父容器)
    elif 组件类型 == "QListWidget":
        组件库对象 = 组件列表框(父容器)
    else:
        print(f"======未匹配组件 {组件类型}")
        return None
    return 组件库对象
