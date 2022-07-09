import json
import random
import sys
import PySide6
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Signal
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from qt_esay_model.代码生成AppPy文件 import 代码生成AppPy文件
from qt_esay_model.代码生成UiPy文件 import 代码生成UiPy文件
from qt_esay_model.组件名称管理类 import 组件名称管理类
from qt_esay_model.中文对照组件常量 import 取组件名称中英文对照
from qt_esay_model.组件库.组件单行编辑框 import 组件单行编辑框
from qt_esay_model.组件库.组件富文本编辑框 import 组件富文本编辑框
from qt_esay_model.组件库.组件按钮 import 组件按钮
from qt_esay_model.组件库.组件窗口 import 组件窗口
from qt_esay_model.组件库.组件纯文本编辑框 import 组件纯文本编辑框
from qt_esay_model.组件树类 import 组件树类, 导入导出组件结构数据, 组件树生成代码类
from pyefun import *

from qt_esay_model.辅助函数 import 发送给ide插件

from qtefun.组件.主窗口 import 主窗口
from qt_esay_model.历史记录类 import 历史记录类

# class 子窗口(QMdiSubWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('sub')
#         self.setWidget(QPushButton('sub'))
#         self.show()
#         self.resize(500, 500)

class 设计窗口(QMdiSubWindow):
    信号_更新属性框 = Signal(object)  # 请订阅这个消息
    信号_代码跳转 = Signal(bool, str)  # 请订阅这个消息
    信号_双击跳转代码 = Signal(object)  # 请订阅这个消息
    信号_更新组件树 = Signal(object)
    rect = (0, 0, 0, 0)  # 第一个组件的rect数据
    rects = []  # 多个㢟的rect绘制数据
    组件方块数组 = {}  # 组件对应的方向跳转方块 0 是方块 1 是组件对象 2 是组件库对象
    调整尺寸 = False
    移动组件 = False
    设计组件被按下 = False
    当前选中的组件 = []
    当前创建组件名称 = ""
    # 组件库列表 = []
    绘制虚线和方块颜色值 = QColor(64, 136, 247)
    写出文件路径_设计文件json = "启动窗口.json"  # 例如 启动窗口.py
    写出文件路径_uipy = "ui_启动窗口.py"  # 例如 ui_启动窗口.py
    写出文件路径AppPy = "app_启动窗口.py"  # 例如 app.py
    可否关闭 = True
    组件窗口库 = None  # :type 组件窗口
    插件URL地址 = ""
    组件树 = None  # :type 组件树类
    组件id与名称关系 = {}  # 组件id与名称关系
    项目目录 = ""
    组件名称管理 = None
    操作记录: 历史记录类 = None
    开始x = 0
    开始y = 0
    结束x = 0
    结束y = 0
    窗口被按下 = False

    def __init__(self, parent=None):
        super().__init__()
        # 隐藏窗口的最大化按钮
        self.setWindowTitle('sub')
        self.resize(500, 500)

        self.窗口被按下 = False
        self.结束x = 0
        self.结束y = 0
        self.开始x = 0
        self.开始y = 0
        self.新建()

        self.容器 = QWidget(self)
        self.容器.mousePressEvent = self.窗口鼠标按下事件
        self.容器.mouseReleaseEvent = self.窗口鼠标放开事件
        self.容器.mouseMoveEvent = self.窗口鼠标移动事件
        self.容器.paintEvent = self.窗口绘制
        # QPushButton(self.容器).setText('点击')
        self.setWidget(self.容器)
        # self.mousePressEvent = self.窗口鼠标按下事件
        # self.mouseReleaseEvent = self.窗口鼠标放开事件
        # self.mouseMoveEvent = self.窗口鼠标移动事件
        # self.paintEvent = self.窗口绘制

        # todo : 双击事件bug没效果
        # 绑定窗口鼠标双击事件
        # self.doubleClickEvent = self.窗口鼠标双击事件

        # 监听窗口大小和位置移动
        self.容器.resizeEvent = self.窗口大小改变事件
        # self.容器.moveEvent = self.窗口位置改变事件
        self.当前选中的组件 = []

        self.shortcut = QShortcut(QKeySequence("Ctrl+z"), self)
        self.shortcut.activated.connect(self.撤消)
        self.shortcut = QShortcut(QKeySequence("Ctrl+y"), self)
        self.shortcut.activated.connect(self.恢复)

    def closeEvent(self, e: QCloseEvent):
        print("窗口关闭事件")
        if self.可否关闭:
            e.accept()
        else:
            e.ignore()

    def 信号_保存组件信息(self):
        print("信号_保存组件信息")
        self.保存组件信息()

    def 信号_加载设计文件(self, 文件路径):
        self.加载路径信息(文件路径)
        self.读取组件信息()

    def 加载路径信息(self, 文件路径):
        项目目录 = 文件_取目录(文件路径)
        窗口名称 = 文件_取文件名(文件路径, False)
        print("信号_加载设计文件", 文件路径, 项目目录, 窗口名称)
        self.项目目录 = 项目目录 + "/"
        self.写出文件路径_设计文件json = 项目目录 + f"/{窗口名称}.json"  # 例如 启动窗口.py
        self.写出文件路径_uipy = 项目目录 + f"/ui_{窗口名称}.py"  # 例如 ui_启动窗口.py
        self.写出文件路径AppPy = 项目目录 + f"/app_{窗口名称}.py"  # 例如 app.py
        if 文件路径 == "":
            self.写出文件路径_设计文件json = ""
            self.写出文件路径_uipy = ""
            self.写出文件路径AppPy = ""
        print("写出文件路径_设计文件json", self.写出文件路径_设计文件json)
        print("写出文件路径_uipy", self.写出文件路径_uipy)
        print("写出文件路径AppPy", self.写出文件路径AppPy)

    def 保存组件信息(self):
        窗口属性 = self.组件窗口库.导出为json属性()
        self.组件树 = 组件树类(窗口属性["名称"], 'QMainWindow', self.组件窗口库.导出为json属性())
        容器 = 组件树类('centralwidget', 'QWidget', {})
        self.组件树.添加子组件(容器)
        for 组件Arr in self.组件方块数组:  # type: 组件按钮
            组件 = self.组件方块数组[组件Arr][2]
            组件属性 = 组件.导出为json属性()
            组件名称 = 组件属性.get("名称")
            组件类型 = 组件属性.get("组件类型")

            容器.添加子组件(组件树类(组件名称, 组件类型, 组件属性))
        导出数据 = self.组件树.导出组件结构数据_json()
        # print("导出数据", 导出数据)
        if self.写出文件路径_设计文件json == "":
            return
        # 写出文件
        print("写出文件=======================")
        文件_写出(self.写出文件路径_设计文件json, 导出数据)
        python代码_ui = 代码生成UiPy文件(导出数据).生成代码()
        文件_写出(self.写出文件路径_uipy, python代码_ui)
        主窗口py的文件内容 = 读入文本(self.写出文件路径AppPy)
        python代码_app = 代码生成AppPy文件(导出数据, 主窗口py的文件内容).生成代码()
        文件_写出(self.写出文件路径AppPy, python代码_app)

    def 信号_跳转代码(self, 函数名):
        print(f"调用pycharm代码跳转: {self.写出文件路径AppPy}, {函数名}")
        文件名 = 文件_取文件名(self.写出文件路径AppPy)

        def 延迟调用():
            代码位置 = 寻找文本(读入文本(self.写出文件路径AppPy), "def %s" % 函数名)
            if 代码位置 != -1:
                状态, 错误文本 = 发送给ide插件(self.插件URL地址, 文件名, 代码位置)
                # 延时(1)
                # 状态, 错误文本 = 发送给ide插件(self.插件URL地址, 文件名, 代码位置)
                # todo让主窗口隐藏自己
                self.信号_代码跳转.emit(状态, 错误文本)
            else:
                print("没有找到函数")
                return f"{self.写出文件路径AppPy} 中没有找到函数 {函数名} 跳转失败"

        启动线程(延迟调用)

    def 读取组件信息(self):
        print("读取组件信息")
        try:
            导入数据 = 读入文本(self.写出文件路径_设计文件json)
            导入数据 = json.loads(导入数据)
        except:
            print("没有组件信息")
            窗口宽度 = 400
            窗口高度 = 400
            窗口标题 = "祖国,您好!"
            self.组件树 = 组件树类('启动窗口', 'QMainWindow',
                            {"左边": 0, "顶边": 0, "宽度": 窗口宽度, "高度": 窗口高度, "可视": 1, "禁止": 0, "标题": 窗口标题, "事件窗口创建完毕": ""})
            容器 = 组件树类('centralwidget', 'QWidget', {})
            self.组件树.添加子组件(容器)
            return
        self.组件树 = 导入导出组件结构数据(导入数据)
        # 组件结构数据 = G.组件树.导出组件结构数据_json()
        self.递归创建组件(导入数据)
        self.当前选中的组件 = []
        self.方块_刷新显示当前选中()

    def 递归创建组件(self, 结构数据, 递归深度=False):
        组件名称 = 结构数据['组件名称']
        组件类型 = 结构数据['组件类型']
        组件属性 = 结构数据['组件属性']
        print("递归创建组件", 组件名称, 组件类型, 组件属性)
        if 组件类型 == "QMainWindow":
            左边, 顶边, 宽度, 高度 = 组件属性['左边'], 组件属性['顶边'], 组件属性['宽度'], 组件属性['高度']
            self.resize(宽度, 高度)
            组件名称 = 文件_取文件名(self.写出文件路径_设计文件json, False)
            self.setObjectName(组件名称)
            self.setWindowTitle(组件属性['标题'])

            for key in 组件属性:
                self.组件窗口库.修改组件属性(key, 组件属性[key])

        if 递归深度 == False:
            pass
        else:
            # 左边, 顶边, 宽度, 高度 = 组件属性['左边'], 组件属性['顶边'], 组件属性['宽度'], 组件属性['高度']
            self.创建组件(组件类型, 组件属性=组件属性)

        for 子组件 in 结构数据['子组件']:
            # 子组件类型 = 子组件['组件类型']
            # 子组件名称 = 子组件['组件名称']
            # 子组件属性 = 子组件['组件属性']
            self.递归创建组件(子组件, True)

    def 信号_修改组件的属性(self, 当前组件库的对象, 属性名称, 属性值):
        def _修改组件属性(传递参数):
            # 记录选来组件的 rect
            组件库, 属性名称, 属性值 = 传递参数['组件库'], 传递参数['属性名称'], 传递参数['属性值']  # type:组件按钮
            传递参数['原属性值'] = 组件库.导出为json属性()[属性名称]
            组件库.修改组件属性(属性名称, 属性值)
            return 传递参数

        def _修改组件属性恢复(传递参数):
            组件库, 属性名称, 属性值, 原属性值 = 传递参数['组件库'], 传递参数['属性名称'], 传递参数['属性值'], 传递参数['原属性值']  # type:组件按钮
            组件库.修改组件属性(属性名称, 原属性值)
            return 传递参数

        if self.当前选中的组件 == []:
            # 证明是窗口
            # self.组件窗口库.修改组件属性(属性名称, 属性值)
            self.操作记录.开始记录()
            self.操作记录.添加("修改组件属性", {"组件库": self.组件窗口库, "属性名称": 属性名称, "属性值": 属性值}, _修改组件属性, _修改组件属性恢复)
            self.操作记录.提交记录()
            return
        # 当前组件库的对象.修改组件属性(属性名称, 属性值)
        for 组件 in self.当前选中的组件:
            件库 = self.组件方块数组[组件.property("_方块id")][2]
            # 组件库 = self.组件方块数组[组件.property["_方块id"]][2]
            # 检查一下 组件名称 是否重复确认生效
            if 属性名称 == "名称":
                if 组件.objectName() != 属性值:
                    if self.组件名称管理.检查重复(属性值, self.取所有组件的组件名称()):
                        self.消息框("你输入的名称有冲突请修改")
                        return
            # 组件库.修改组件属性(属性名称, 属性值) # 原来的代码

            self.操作记录.开始记录()
            for 组件 in self.当前选中的组件:  # type: QPushButton
                组件库 = self.组件方块数组[组件.property("_方块id")][2]
                self.操作记录.添加("修改组件属性", {"组件库": 组件库, "属性名称": 属性名称, "属性值": 属性值}, _修改组件属性, _修改组件属性恢复)
            self.操作记录.提交记录()

        self.方块_刷新显示当前选中()

    def 新建(self):
        self.组件窗口库 = 组件窗口(self)
        self.setObjectName("启动窗口")
        self.setWindowTitle("启动窗口")
        self.resize(400, 360)

        for i in self.组件方块数组:
            组件 = self.组件方块数组[i][1]
            self.清理一个组件的数据(组件)

        self.调整组件 = None
        self.rect = (0, 0, 0, 0)  # 第一个组件的rect数据
        self.rects = []  # 多个㢟的rect绘制数据
        self.组件方块数组 = {}  # 组件对应的方向跳转方块 0 是方块 1 是组件对象 2 是组件库对象
        self.调整尺寸 = False
        self.移动组件 = False
        self.设计组件被按下 = False
        self.当前选中的组件 = []
        self.当前创建组件名称 = ""
        self.绘制虚线和方块颜色值 = QColor(64, 136, 247)
        self.写出文件路径_设计文件json = ""  # 例如 启动窗口.py
        self.写出文件路径_uipy = ""  # 例如 ui_启动窗口.py
        self.写出文件路径AppPy = ""  # 例如 app.py
        self.可否关闭 = True
        self.插件URL地址 = ""
        self.组件树 = None  # :type 组件树类
        self.组件id与名称关系 = {}  # 组件id与名称关系
        # self.项目目录 = ""
        self.组件名称管理 = 组件名称管理类()
        self.操作记录 = 历史记录类()

    def 窗口鼠标双击事件(self):
        print("窗口鼠标双击事件")
        self.信号_双击跳转代码.emit()

    def 撤消(self):
        print("撤消")
        self.操作记录.撤消记录()

    def 恢复(self):
        print("恢复")
        self.操作记录.恢复记录()

    def 窗口大小改变事件(self, event):
        print("窗口大小改变事件")
        self.信号_更新属性框.emit(self.组件窗口库)

    def 窗口位置改变事件(self, event):
        print("窗口位置改变事件")
        # self.信号_更新属性框.emit(self.组件窗口库)

    def 信号_绘制组件名称(self, name):
        self.调整尺寸 = False
        self.移动组件 = False
        print("信号_绘制组件名称:", name)
        self.当前创建组件名称 = name

    def 窗口鼠标按下事件(self, e: QMouseEvent):
        x = e.position().x()
        y = e.position().y()
        print("窗口鼠标按下事件", x, y)
        # self.rect = (x, y, 0, 0) # 初始化矩形
        self.窗口被按下 = True
        self.开始x = x
        self.开始y = y

    def 窗口鼠标放开事件(self, e: QMouseEvent):
        x = e.position().x()
        y = e.position().y()
        print("窗口鼠标放开事件", x, y)
        self.窗口被按下 = False

        # 重新计算组件的位置和大小
        左边, 顶边, 宽度, 高度 = self.rect
        print("窗口鼠标放开事件", 左边, 顶边, 宽度, 高度)
        # if self.测试变量:
        #     self.测试变量 = False
        if self.当前创建组件名称 != "":
            self.窗口鼠标松开创建组件()
        else:
            self.当前选中的组件 = []
            self.检查框选范围()
            self.保存组件信息()
            self.信号_更新属性框.emit(self.组件窗口库)
            self.调整组件 = None

        self.方块_刷新显示当前选中()
        self.绘制矩形清除()
        # todo 通知属性框更新 窗口的属性
        if self.调整组件:
            self.信号_更新属性框.emit(self.组件方块数组.get(self.调整组件.property('_方块id'))[2])

    def 绘制矩形清除(self):
        self.rect = (0, 0, 0, 0)
        self.rects = []
        self.update()

    def 检查框选范围(self):
        for i in self.组件方块数组:
            组件 = self.组件方块数组[i][1]  # type: QPushButton
            左边, 顶边, 宽度, 高度 = self.rect  # 框选的范围
            矩形 = (左边, 顶边, 左边 + 宽度, 顶边 + 高度)
            左边, 顶边, 宽度, 高度 = 组件.geometry().getRect()  # 组件的范围
            组件矩形 = [左边, 顶边, 左边 + 宽度, 顶边 + 高度]  # 左边 顶边 右边 底边
            新组件矩形 = [左边, 顶边, 左边 + 宽度, 顶边 + 高度]
            范围矩形 = [矩形[0], 矩形[1], 矩形[2], 矩形[3]]  # 左边 顶边 右边 底边
            新范围矩形 = [矩形[0], 矩形[1], 矩形[2], 矩形[3]]
            if 范围矩形[0] > 组件矩形[2]:
                新组件矩形[0], 新范围矩形[2] = 新范围矩形[2], 新组件矩形[0]
            if 范围矩形[1] > 组件矩形[3]:
                新组件矩形[1], 新范围矩形[3] = 新范围矩形[3], 新组件矩形[1]
            if 组件矩形[1] > 范围矩形[3]:
                新范围矩形[1], 新组件矩形[3] = 新组件矩形[3], 新范围矩形[1]
            if 组件矩形[0] > 范围矩形[2]:
                新组件矩形[0], 新范围矩形[2] = 新范围矩形[2], 新组件矩形[0]
            if 范围矩形 == 新范围矩形:
                self.当前选中的组件.append(组件)

    def 窗口鼠标移动事件(self, e: QMouseEvent):
        # print("窗口鼠标移动事件", e.x(), e.y())
        x = e.position().x()
        y = e.position().y()

        if self.窗口被按下:
            self.结束x = x
            self.结束y = y

            print("窗口鼠标移动事件", x, y)
            self.计算矩形()
            self.update()

    def 窗口鼠标松开创建组件(self):
        print("窗口鼠标松开创建组件")
        左边, 顶边, 宽度, 高度 = self.rect

        # 创建组件
        if self.当前创建组件名称:
            self.操作记录.开始记录()

            def 创建组件(传递数据):
                名称, 左边, 顶边, 宽度, 高度 = 传递数据['名称'], 传递数据['左边'], 传递数据['顶边'], 传递数据['宽度'], 传递数据['高度']
                组件对象 = self.创建组件(名称, 左边, 顶边, 宽度, 高度)
                传递数据['组件对象'] = 组件对象
                return 传递数据

            def 创建组件恢复(传递数据):
                print("恢复组件", 传递数据)
                组件 = 传递数据['组件对象']

                self.清理一个组件的数据(组件)
                return 传递数据

            名称 = 取组件名称中英文对照(self.当前创建组件名称)
            记录对象 = self.操作记录.添加("创建组件", {"名称": 名称, "左边": 左边, "顶边": 顶边, "宽度": 宽度, "高度": 高度}, 创建组件, 创建组件恢复)
            self.操作记录.提交记录()

            组件对象 = 记录对象['组件对象']
            # 组件对象 = self.创建组件(取组件名称中英文对照(self.当前创建组件名称), 左边, 顶边, 宽度, 高度) # 封装操作历史
            self.调整组件 = 组件对象
            self.当前选中的组件 = [组件对象]
            self.刷新数据_属性框和组件树()

        self.当前创建组件名称 = ""

    def 取所有组件的组件名称(self):
        组件名称 = []
        for i in self.组件方块数组:
            组件名称.append(self.组件方块数组[i][1].objectName())
        return 组件名称

    def 创建组件(self, 组件类型="QPushButton", 左边=0, 顶边=0, 宽度=0, 高度=0, 组件属性=None):
        # print("创建组件")
        中文名称 = 取组件名称中英文对照(组件类型)
        if 组件属性 is None:
            组件属性 = {}
            组件名称 = self.组件名称管理.取新名称(中文名称)
        else:
            组件名称 = 组件属性.get("名称", "")
            print("创建组件 坐标信息", 左边, 顶边, 宽度, 高度)
        # 组件类型前缀检查是否匹配
        if 组件类型 == "QPushButton":
            组件库对象 = 组件按钮(self.容器)
        elif 组件类型 == "QLineEdit":
            组件库对象 = 组件单行编辑框(self.容器)
        elif 组件类型 == "QTextEdit":
            组件库对象 = 组件富文本编辑框(self.容器)
        elif 组件类型 == "QPlainTextEdit":
            组件库对象 = 组件纯文本编辑框(self.容器)
        else:
            print("位置类型不匹配", 组件类型)
            return

        名称列表 = self.取所有组件的组件名称()
        # print("名称列表", 名称列表, "组件名称", 组件名称)
        while self.组件名称管理.检查重复(组件名称, 名称列表):
            组件名称 = self.组件名称管理.取新名称(中文名称)
            if 组件属性:
                组件属性["名称"] = 组件名称

        组件库对象.创建组件(组件名称, 左边, 顶边, 宽度, 高度, 组件属性)
        # # 记录组件信息到组件列表中
        # self.组件库列表.append(组件库对象)

        组件 = 组件库对象.对象
        组件.keyReleaseEvent = lambda e, obj=组件库对象: self.事件_设计组件键盘开放(e, obj)
        组件.mousePressEvent = lambda e, obj=组件: self.事件_设计组件被按下(e, obj)
        组件.mouseReleaseEvent = lambda e, obj=组件: self.事件_设计组件被放开(e, obj)
        组件.mouseMoveEvent = lambda e, obj=组件: self.事件_设计组件被移动(e, obj)
        组件.mouseDoubleClickEvent = lambda e, obj=组件: self.事件_设计组件被双击(e, obj)
        self.绘制矩形清除()

        self.创建方块(组件, 组件库对象)
        # self.保存组件信息()
        return 组件

    def 事件_设计组件键盘开放(self, e, 组件库对象: 组件按钮):
        # 检查是否按下 del 键盘 和 退格键
        print("事件_设计组件键盘开放", e.key())
        if e.key() == Qt.Key_Delete or e.key() == Qt.Key_Backspace:
            # 删除组件
            self.删除组件()

        # 检查是否按下复制键 ctrl+c
        elif e.key() == Qt.Key_C and e.modifiers() == Qt.ControlModifier:
            # 复制组件
            self.复制组件()
        # 检查是否按下粘贴键 ctrl+v
        elif e.key() == Qt.Key_V and e.modifiers() == Qt.ControlModifier:
            # 粘贴组件
            self.粘贴组件()
        # 检查是否按下剪切键 ctrl+x
        elif e.key() == Qt.Key_X and e.modifiers() == Qt.ControlModifier:
            pass
            # 剪切组件 pass
            self.剪切组件()
        # 检查是否按下撤消 ctrl+z
        elif e.key() == Qt.Key_Z and e.modifiers() == Qt.ControlModifier:
            pass
            # 剪切组件 pass
            self.撤消()
        elif e.key() == Qt.Key_Y and e.modifiers() == Qt.ControlModifier:
            pass
            # 剪切组件 pass
            self.恢复()

    def 清理一个组件的数据(self, 组件):
        方块数组, 组件库对象, 对象 = self.组件方块数组[组件.property("_方块id")][0], self.组件方块数组[组件.property("_方块id")][1], \
                          self.组件方块数组[组件.property("_方块id")][2]
        for 组件2 in 方块数组:  # type: QLabel
            组件2.deleteLater()
        # self.组件库列表.remove(组件库对象)
        组件库对象.deleteLater()
        # 移除 组件方块数组 的对象
        self.组件方块数组.pop(组件.property("_方块id"))
        del 对象

    def 删除组件(self):

        self.操作记录.开始记录()
        for 组件 in self.当前选中的组件:
            def _删除对象(传递参数):
                print("_删除对象")
                组件库对象 = self.组件方块数组[传递参数['组件对象'].property("_方块id")][2]  # type: 组件按钮
                传递参数['组件的数据'] = 组件库对象.导出为json属性()

                self.清理一个组件的数据(传递参数['组件对象'])  # 删除对象操作

                self.当前选中的组件 = []
                self.刷新数据_属性框和组件树()
                return 传递参数

            def _删除对象恢复(传递参数):
                print("_删除对象恢复")
                组件类型 = 传递参数['组件的数据']['组件类型']
                组件对象 = self.创建组件(组件类型, 组件属性=传递参数['组件的数据'])
                传递参数['组件对象'] = 组件对象  # 把对象重新放回传递参数

                self.调整组件 = 组件对象
                # self.当前选中的组件 = [组件对象]
                self.刷新数据_属性框和组件树()
                return 传递参数

            记录对象 = self.操作记录.添加("创建组件", {"组件对象": 组件}, _删除对象, _删除对象恢复)
        self.操作记录.提交记录()

        # for 组件 in self.当前选中的组件:
        #     self.清理一个组件的数据(组件)
        self.当前选中的组件 = []
        # self.刷新数据_属性框和组件树()

    def 复制组件(self):
        # print("复制组件")
        # for 组件 in self.当前选中的组件:
        #     组件库对象 = self.组件方块数组[组件.property("_方块id")][2] # type: 组件按钮
        #     组件的属性 = 组件库对象.导出组件属性()
        #     print("????????",组件的属性)
        self.复制模式 = "复制"
        self.当前复制组件的数据 = self.当前选中的组件.copy()

    def 剪切组件(self):
        self.复制模式 = "剪切"
        self.当前复制组件的数据 = self.当前选中的组件.copy()

        # 隐藏
        for 组件 in self.当前选中的组件:
            方块数组, 组件库对象 = self.组件方块数组[组件.property("_方块id")][0], self.组件方块数组[组件.property("_方块id")][1]
            for 组件2 in 方块数组:  # type: QLabel
                组件2.hide()
            组件库对象.hide()

    def 粘贴组件(self):
        print("粘贴组件")
        新增组件 = []
        if self.复制模式 == "复制":
            for 组件 in self.当前复制组件的数据:
                组件库对象 = self.组件方块数组[组件.property("_方块id")][2]  # type: 组件按钮
                组件的属性 = 组件库对象.导出为json属性()
                print("????????", 组件的属性)
                # 给组件的属性 左边和 顶边 增加20
                组件的属性["左边"] += 20
                组件的属性["顶边"] += 20
                组件的属性["可视"] = 1
                新组件 = self.创建组件(组件的属性['组件类型'], 组件属性=组件的属性)
                新增组件.append(新组件)
        if self.复制模式 == "剪切":
            for 组件 in self.当前复制组件的数据:
                组件库对象 = self.组件方块数组[组件.property("_方块id")][2]  # type: 组件按钮
                组件的属性 = 组件库对象.导出为json属性()
                print("????????", 组件的属性)
                # 给组件的属性 左边和 顶边 增加20
                # 组件的属性["左边"] += 20
                # 组件的属性["顶边"] += 20
                组件的属性["可视"] = 1
                新组件 = self.创建组件(组件的属性['组件类型'], 组件属性=组件的属性)
                新增组件.append(新组件)

                # 删除旧的
                self.清理一个组件的数据(组件)

            self.当前复制组件的数据 = []

        self.当前选中的组件 = 新增组件
        self.刷新数据_属性框和组件树()

    def 刷新数据_属性框和组件树(self):
        self.方块_刷新显示当前选中()
        self.保存组件信息()
        self.信号_更新属性框.emit(self.组件窗口库)
        self.信号_更新组件树.emit(self.组件窗口库)
        self.update()

    def 事件_设计组件被按下(self, e: QMouseEvent, 组件: QPushButton):
        x = e.position().x()
        y = e.position().y()
        print("事件_设计组件被按下", x, y)
        self.绘制矩形清除()
        self.设计组件被按下 = True
        # self.移动组件 = True
        self.调整组件 = 组件
        self.开始x = x
        self.开始y = y
        if e.modifiers() == Qt.ShiftModifier:
            print("shift键被按下")
            if not 组件 in self.当前选中的组件:
                self.当前选中的组件.append(组件)
            else:
                self.当前选中的组件.remove(组件)
        else:
            if len(self.当前选中的组件) <= 1:
                self.当前选中的组件 = [组件]

        self.方块_刷新显示当前选中()

    def 方块_刷新显示当前选中(self):
        self.方块_隐藏()
        for 组件 in self.当前选中的组件:
            # print("方块_刷新显示当前选中", 组件)
            self.方块_显示(组件.property('_方块id'))

    def 事件_设计组件被放开(self, e: QMouseEvent, 组件: QPushButton):
        x = e.position().x()
        y = e.position().y()
        print("事件_设计组件被放开", x, y)
        self.设计组件被按下 = False

        if self.移动组件:
            print("注意这里调整1")
            左边, 顶边, 宽度, 高度 = self.rect

            # # 组件.setGeometry(左边, 顶边, 宽度, 高度) # 这是修改单个
            # print("事件_设计组件被放开", 左边, 顶边, 宽度, 高度)
            # for 组件 in self.当前选中的组件:  # 这里是批量修改
            #     # 计算组件位置差距
            #     左边x, 顶边x, 宽度x, 高度x = 组件.geometry().getRect()
            #     左边n = 左边x + x - self.开始x
            #     顶边n = 顶边x + y - self.开始y
            #     print("事件_设计组件被放开", 左边n, 顶边n, 宽度, 高度)
            #     组件.setGeometry(左边n, 顶边n, 宽度, 高度)

            def _修改组件属性(传递参数):
                # 记录选来组件的 rect
                组件 = 传递参数['组件对象']
                传递参数['原左边'], 传递参数['原顶边'], 传递参数['原宽度'], 传递参数['原高度'] = 组件.geometry().getRect()
                self.调整组件 = 组件
                左边x, 顶边x, 宽度x, 高度x = 组件.geometry().getRect()
                左边n = 左边x + x - self.开始x
                顶边n = 顶边x + y - self.开始y
                组件.setGeometry(左边n, 顶边n, 宽度, 高度)
                # self.方块_调整位置(组件.property('_方块id'))
                self.方块_刷新显示当前选中()
                return 传递参数

            def _修改组件属性恢复(传递参数):
                组件 = 传递参数['组件对象']
                左边, 顶边, 宽度, 高度 = 传递参数['原左边'], 传递参数['原顶边'], 传递参数['原宽度'], 传递参数['原高度']
                self.调整组件 = 组件
                组件.setGeometry(左边, 顶边, 宽度, 高度)
                # self.方块_调整位置(组件.property('_方块id'))
                self.方块_刷新显示当前选中()
                return 传递参数

            self.操作记录.开始记录()
            for 组件对象 in self.当前选中的组件:  # type: QPushButton
                self.操作记录.添加("移动位置", {"组件对象": 组件对象}, _修改组件属性, _修改组件属性恢复)
            self.操作记录.提交记录()

        # self.方块_刷新显示当前选中()
        self.移动组件 = False

        # todo: 调整尺寸需要发送事件更新属性框
        self.信号_更新属性框.emit(self.组件方块数组.get(self.调整组件.property('_方块id'))[2])

    def 事件_设计组件被移动(self, e: QMouseEvent, 组件: QPushButton):
        x = e.position().x()
        y = e.position().y()
        # print("事件_设计组件被移动", x, y)
        if self.设计组件被按下:
            self.移动组件 = True
            # 记录第一个react
            左边, 顶边, 宽度, 高度 = 组件.geometry().getRect()
            左边 += x - self.开始x
            顶边 += y - self.开始y
            self.rect = (左边, 顶边, 宽度, 高度)
            # 记录一组react
            self.rects = []
            for 组件 in self.当前选中的组件:  # 这里是批量修改
                左边, 顶边, 宽度, 高度 = 组件.geometry().getRect()
                左边 += x - self.开始x
                顶边 += y - self.开始y
                self.rects.append((左边, 顶边, 宽度, 高度))

            self.update()

    def 事件_设计组件被双击(self, e: QMouseEvent, 组件: QPushButton):
        x = e.position().x()
        y = e.position().y()
        print("事件_设计组件被双击", x, y)
        # todo: 更新属性框第一个事件并进入代码编辑器 发送事件处理
        self.信号_双击跳转代码.emit(组件)

    def 创建方块(self, 组件: QPushButton, 组件库对象: 组件按钮):
        左边, 顶边, 宽度, 高度 = 组件.geometry().getRect()
        size = 5
        方块_左上 = QLabel(self.容器)
        方块_左上.setCursor(Qt.SizeFDiagCursor)
        方块_左 = QLabel(self.容器)
        方块_左.setCursor(Qt.SizeHorCursor)
        方块_左下 = QLabel(self.容器)
        方块_左下.setCursor(Qt.SizeBDiagCursor)
        方块_中上 = QLabel(self.容器)
        方块_中上.setCursor(Qt.SizeVerCursor)
        方块_中下 = QLabel(self.容器)
        方块_中下.setCursor(Qt.SizeVerCursor)
        方块_右上 = QLabel(self.容器)
        方块_右上.setCursor(Qt.SizeBDiagCursor)
        方块_右 = QLabel(self.容器)
        方块_右.setCursor(Qt.SizeHorCursor)
        方块_右下 = QLabel(self.容器)
        方块_右下.setCursor(Qt.SizeFDiagCursor)
        方块数组 = (方块_左上, 方块_左, 方块_左下, 方块_中上, 方块_中下, 方块_右上, 方块_右, 方块_右下)

        # 将标签绑定设计组件按下和放开事件
        i = 0

        组件.setProperty("_方块id", random.Random().randint(0, 99999))

        for 标签组件 in range(8):
            标签组件 = 方块数组[i]
            # print(f"方块标签_{i}")
            标签组件.setObjectName(f"方块标签_{i}")
            标签组件.setProperty("_方向", i)
            标签组件.setProperty("_方块id", 组件.property('_方块id'))
            i = i + 1
            标签组件.setFixedWidth(size)
            标签组件.setFixedHeight(size)
            颜色值 = self.绘制虚线和方块颜色值.getRgb()
            # print(f"background-color: rgba{颜色值}")
            标签组件.setStyleSheet(f"background-color: rgba{颜色值}")
            标签组件.show()
            # 标签组件.hide()
            标签组件.mousePressEvent = lambda e, obj=标签组件, obj2=组件: self.事件_方块被按下(e, obj, obj2)
            标签组件.mouseReleaseEvent = lambda e, obj=标签组件, obj2=组件: self.事件_方块被放开(e, obj, obj2)
            标签组件.mouseMoveEvent = lambda e, obj=标签组件, obj2=组件: self.事件_方块被移动(e, obj, obj2)

        self.组件方块数组[组件.property('_方块id')] = (方块数组, 组件, 组件库对象)
        self.方块_调整位置(组件.property('_方块id'))
        self.组件id与名称关系[组件.objectName()] = 组件.property('_方块id')

    def 事件_方块被按下(self, e: QMouseEvent, 标签组件: QLabel, 组件: QPushButton):
        x = e.scenePosition().x()
        y = e.scenePosition().y()
        self.调整尺寸 = True
        self.调整方向 = 标签组件.property('_方向')
        self.调整组件 = 组件
        self.开始x = x
        self.开始y = y

        print("事件_方块被按下 调整尺寸", x, y, self.调整方向)

    def 事件_方块被放开(self, e: QMouseEvent, 标签组件: QLabel, 组件: QPushButton):
        x = e.scenePosition().x()
        y = e.scenePosition().y()
        print("事件_方块被放开", x, y)
        if self.调整尺寸:
            self.调整尺寸 = False
            print("注意这里1")

            # 左边, 顶边, 宽度, 高度 = self.rect # 单个调整
            # print("事件_方块被放开", 左边, 顶边, 宽度, 高度)
            # 组件.setGeometry(左边, 顶边, 宽度, 高度)
            # self.方块_调整位置(组件.property('_方块id'))
            # for 组件 in self.当前选中的组件:  # 这里是批量修改
            #     self.调整组件 = 组件
            #     self.rect = self.计算矩形2(组件)
            #     左边, 顶边, 宽度, 高度 = self.rect
            #     print("事件_方块被放开11", 左边, 顶边, 宽度, 高度)
            #     组件.setGeometry(左边, 顶边, 宽度, 高度)
            #     self.方块_调整位置(组件.property('_方块id'))

            def _修改组件属性(传递参数):
                # 记录选来组件的 rect
                组件 = 传递参数['组件对象']
                左边, 顶边, 宽度, 高度 = 组件.geometry().getRect()
                传递参数['原左边'], 传递参数['原顶边'], 传递参数['原宽度'], 传递参数['原高度'] = 左边, 顶边, 宽度, 高度
                self.调整组件 = 组件
                左边, 顶边, 宽度, 高度 = self.计算矩形2(组件)
                组件.setGeometry(左边, 顶边, 宽度, 高度)
                # self.方块_调整位置(组件.property('_方块id'))
                self.方块_刷新显示当前选中()
                return 传递参数

            def _修改组件属性恢复(传递参数):
                组件 = 传递参数['组件对象']
                左边, 顶边, 宽度, 高度 = 传递参数['原左边'], 传递参数['原顶边'], 传递参数['原宽度'], 传递参数['原高度']
                self.调整组件 = 组件
                组件.setGeometry(左边, 顶边, 宽度, 高度)
                # self.方块_调整位置(组件.property('_方块id'))
                self.方块_刷新显示当前选中()
                return 传递参数

            self.操作记录.开始记录()
            for 组件对象 in self.当前选中的组件:  # type: QPushButton
                self.操作记录.添加("修改尺寸", {"组件对象": 组件对象}, _修改组件属性, _修改组件属性恢复)
            self.操作记录.提交记录()

            self.绘制矩形清除()

    def 方块_隐藏(self, 组件名称=None, 隐藏=True):
        print("方块_隐藏", 组件名称, 隐藏)
        if 组件名称 is None:
            for 所有组件的方块数组 in self.组件方块数组.values():
                for 方块标签 in 所有组件的方块数组[0]:
                    方块标签.hide()
        else:
            所有组件的方块数组 = self.组件方块数组[组件名称][0]
            for 方块标签 in 所有组件的方块数组:
                if 隐藏:
                    方块标签.hide()
                else:
                    方块标签.show()

    def 方块_显示(self, 组件名称=None):
        所有组件的方块数组 = self.组件方块数组[组件名称][0]
        for 方块标签 in 所有组件的方块数组:
            self.方块_调整位置(方块标签.property('_方块id'))
            方块标签.show()

    def 方块_调整位置(self, 组件名称):
        # print("方块_调整位置", 组件名称)
        方块, 组件 = self.组件方块数组[组件名称][0], self.组件方块数组[组件名称][1]
        左边, 顶边, 宽度, 高度 = 组件.geometry().getRect()
        size = 5
        方块[0].move(左边 - size, 顶边)
        方块[1].move(左边 - size, int(顶边 + 高度 / 2))
        方块[2].move(左边 - size, 顶边 + 高度 - size)
        方块[3].move(int(左边 + 宽度 / 2), 顶边)
        方块[4].move(int(左边 + 宽度 / 2), 顶边 + 高度 - size)
        方块[5].move(左边 + 宽度, 顶边)
        方块[6].move(左边 + 宽度, int(顶边 + 高度 / 2))
        方块[7].move(左边 + 宽度, 顶边 + 高度 - size)

    def 事件_方块被移动(self, e: QMouseEvent, 标签组件: QLabel, 组件: QPushButton):
        x = e.scenePosition().x()
        y = e.scenePosition().y()
        print("事件_方块被移动", x, y)
        self.结束x = x
        self.结束y = y
        self.rect = self.计算矩形2(self.调整组件)

        # 记录一组react
        self.rects = []
        for 组件 in self.当前选中的组件:  # 这里是批量修改
            self.rects.append(self.计算矩形2(组件))

        self.update()

    def 计算矩形2(self, 调整组件):
        x1, y1, x, y = self.开始x, self.开始y, self.结束x, self.结束y
        方向 = self.调整方向
        左边, 顶边, 宽度, 高度 = 调整组件.geometry().getRect()
        if 方向 == 0:
            左边 += x - x1
            顶边 += y - y1
            宽度 += x1 - x
            高度 += y1 - y
        elif 方向 == 1:
            左边 += x - x1
            宽度 += x1 - x
        elif 方向 == 2:
            左边 += x - x1
            宽度 += x1 - x
            高度 += y - y1
        elif 方向 == 3:
            顶边 += y - y1
            高度 += y1 - y
        elif 方向 == 4:
            高度 += y - y1
        elif 方向 == 5:
            顶边 += y - y1
            宽度 += x - x1
            高度 += y1 - y
        elif 方向 == 6:
            宽度 += x - x1
        elif 方向 == 7:
            宽度 += x - x1
            高度 += y - y1

        # 反方向处理
        if 宽度 < 0:
            宽度 = abs(宽度)
            左边 -= 宽度
        if 高度 < 0:
            高度 = abs(高度)
            顶边 -= 高度
        左边 = 左边 if 左边 != -1 else 0
        顶边 = 顶边 if 顶边 != -1 else 0
        return (int(左边), int(顶边), int(宽度), int(高度))

    def 计算矩形(self):
        x1, y1, x2, y2 = self.开始x, self.开始y, self.结束x, self.结束y
        左边 = x1 if x1 < x2 else x2
        顶边 = y1 if y1 < y2 else y2
        宽度 = abs(x2 - x1)
        高度 = abs(y2 - y1)
        self.rect = (左边, 顶边, 宽度, 高度)
        print("重新计算矩形的位置和大小", 左边, 顶边, 宽度, 高度)

    def 窗口绘制(self, event):
        # print("绘制事件")
        # 初始化绘图工具
        qp = QPainter(self.容器)
        qp.begin(self.容器)
        if self.rect:
            self.绘制矩形(qp)
        qp.end()

    def 绘制矩形(self, qp):
        # 创建蓝色画笔，画笔粗细2个像素 虚线
        pen = QPen(self.绘制虚线和方块颜色值, 2, Qt.DotLine)
        # print("绘制矩形")
        qp.setPen(pen)
        qp.drawRect(*self.rect)
        for rect in self.rects:
            qp.drawRect(*rect)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = 设计窗口()

    window.show()
    sys.exit(app.exec())
