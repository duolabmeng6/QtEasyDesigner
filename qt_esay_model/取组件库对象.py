from 组件库.组件单行编辑框 import 组件单行编辑框
from 组件库.组件富文本编辑框 import 组件富文本编辑框
from 组件库.组件按钮 import 组件按钮
from 组件库.组件标签 import 组件标签
from 组件库.组件纯文本编辑框 import 组件纯文本编辑框

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
    else:
        print(f"======未匹配组件 {组件类型}")
        return None
    return 组件库对象
