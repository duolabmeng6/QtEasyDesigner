from pyefun import *


def 获取该类的所有方法(self):
    return (list(filter(lambda m: not m.startswith("_") and callable(getattr(self, m)),
                        dir(self))))


def 导出类绑定事件函数(类, 排第一位的事件名称=""):
    # 获取该类的所有方法
    方法列表 = 获取该类的所有方法(类)
    # print(方法列表)
    # 获取方法的注释
    事件列表 = []
    for 方法 in 方法列表:
        if 判断文本(方法, "绑定事件") is False:
            continue
        事件名称 = 方法.replace("绑定事件", "事件")
        回调函数参数解析 = getattr(类, 方法).__doc__
        # 回调函数(是否选择文本)
        回调参数 = strCut(回调函数参数解析, "回调函数($)")
        # print(事件名称, 回调函数参数解析, 回调参数)
        事件列表.append((事件名称, 回调参数))
    # 排序
    事件列表.sort(key=lambda x: x[0] != 排第一位的事件名称)

    return 事件列表


def 合并列表(列表1, 列表2):
    合并列表 = []
    for 列表 in [列表1, 列表2]:
        for 元素 in 列表:
            if 元素 not in 合并列表:
                合并列表.append(元素)
    return 合并列表


if __name__ == "__main__":
    from qtefun.组件.富文本编辑框 import 富文本编辑框
    from qtefun.组件.单行编辑框 import 单行编辑框

    事件列表 = [
        # ("事件内容被改变", ""),
        # ("事件字符格式更改", ""),
        # ("事件光标位置被改变", ""),
        # ("事件选择文本", ""),
        # ("事件文本可复制", "是否选择文本"),
        # ("事件文本可重做", ""),
        # ("事件文本可撤销", "是否可撤销"),
    ]
    事件列表 = 导出类绑定事件函数(富文本编辑框, '事件内容被改变')
    print(事件列表)
