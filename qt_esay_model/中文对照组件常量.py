class 组件数据:
    组件中英文对照 = {
        "主窗口": "QMainWindow",
        "按钮": "QPushButton",
        "单行编辑框": "QLineEdit",
        "纯文本编辑框": "QPlainTextEdit",
        "富文本编辑框": "QTextEdit",
    }


# 互换键值对并且加入

def 取组件名称中英文对照(名称):
    vv = 组件数据.组件中英文对照.copy()
    vv.update({v: k for k, v in vv.items()})
    name = vv.get(名称, False)
    return name


def 取所有组件名称():
    return 组件数据.组件中英文对照.keys()
