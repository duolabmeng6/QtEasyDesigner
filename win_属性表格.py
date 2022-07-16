import json
import os

from PySide6.QtCore import Signal, QSize, QMetaObject, Qt
from PySide6.QtGui import QColor, QIntValidator
from PySide6.QtWidgets import QMainWindow, QWidget, QTableWidget, QTreeWidget, QListWidget, QAbstractItemView, \
    QListWidgetItem, QVBoxLayout, QTabWidget, QHBoxLayout, QMdiArea, QTableWidgetItem, QLineEdit, QComboBox, \
    QTreeWidgetItem, QApplication

import pyefun as efun
from pyefun import *
import qt_esay_model.组件库.组件按钮 as 组件按钮
import qt_esay_model.组件库.组件窗口 as 组件窗口
import qt_esay_model.组件树类 as 组件树类
import qt_esay_model.中文对照组件常量 as 中文对照组件常量

# import 组件拖动的测试
import win_设计窗口
from qtefun.图标 import 获取图标


class MainWin(QMainWindow):
    # 定义信号 接收属性框更新
    信号_绘制组件名称 = Signal(str)
    信号_修改组件的属性 = Signal(object, str, str)
    信号_项目管理文件被选择 = Signal(str)

    当前组件库的对象 = None  # type: 组件按钮
    tableWidget = None
    treeWidget = None

    def __init__(self):
        super().__init__()

        self.show()
        self.setWindowTitle("设计器的小部件")
        self.move(300, 100)
        self.resize(1200, 600)
        self.centralWidget = QWidget()
        self.设计窗口 = win_设计窗口.设计窗口()

        self.设计窗口.信号_更新属性框.connect(self.信号_更新属性框)
        self.设计窗口.信号_更新组件树.connect(self.信号_更新组件树)
        # self.设计窗口.信号_代码跳转.connect(self.信号_代码跳转)
        self.设计窗口.信号_双击跳转代码.connect(self.信号_双击跳转代码)
        self.信号_绘制组件名称.connect(self.设计窗口.信号_绘制组件名称)
        self.信号_修改组件的属性.connect(self.设计窗口.信号_修改组件的属性)

        self.tableWidget = QTableWidget(self)
        self.listWidget = QListWidget(self)
        self.treeWidget = QTreeWidget(self)
        self.树形框项目管理 = QTreeWidget(self)
        self.treeWidget.itemClicked.connect(self.树形框被点击)
        self.初始化组件列表()

        # self.初始化布局()
        # self.初始化属性表格()

        self.初始化布局2()

    def 数据刷新(self):
        self.当前组件库的对象 = 组件窗口.组件窗口(self.设计窗口)
        self.初始化属性表格_从数据(self.当前组件库的对象.导出组件属性())
        self.刷新组件树显示()

    def 树形框被点击(self, item):
        组件名称 = item.text(0)
        组件类型 = item.text(1)
        print("组件名称:", 组件名称, "组件类型:", 组件类型)
        if 组件类型 == "QMainWindow":
            pass
            self.设计窗口.当前选中的组件 = []
            self.设计窗口.信号_更新属性框.emit(self.设计窗口.组件窗口库)

        else:
            pass
            # todo 反向选择组件...
            方块id = self.设计窗口.组件id与名称关系.get(组件名称)
            组件, 组件库 = self.设计窗口.组件方块数组.get(方块id)[1], self.设计窗口.组件方块数组.get(方块id)[2]
            if 组件:
                self.设计窗口.当前选中的组件 = [组件]
                self.当前组件库的对象 = 组件库

            self.初始化属性表格_从数据(self.当前组件库的对象.导出组件属性())
            self.设计窗口.方块_刷新显示当前选中()

    def 刷新组件树显示(self):
        if self.treeWidget == None:
            return
        # print("刷新组件树显示 尽量优化一下有数据变更才调用")
        self.treeWidget.clear()
        # 设置  self.treeWidget 为两列内容为 对象 和 类
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setHeaderLabels(["对象", "类"])
        self.treeWidget.setColumnWidth(0, 150)
        self.treeWidget.setColumnWidth(1, 50)
        # self.设计窗口.保存组件信息()

        组件结构数据 = self.设计窗口.组件树.导出组件结构数据_json()
        # print("组件结构数据",组件结构数据)
        组件结构数据 = json.loads(组件结构数据)
        # 递归导入组件数据
        self.递归导入组件树(组件结构数据)
        # 展开所有项目
        self.treeWidget.expandAll()

    def 递归导入组件树(self, 结构数据, 递归深度=False, 窗口项目=None):

        组件名称 = 结构数据['组件名称']
        组件类型 = 结构数据['组件类型']
        组件属性 = 结构数据['组件属性']
        # print("递归导入组件树", 组件名称, 组件类型, 组件属性)
        if 递归深度 == False:
            窗口项目 = QTreeWidgetItem()
            窗口项目.setText(0, 组件名称)
            窗口项目.setIcon(0, 获取图标("fa.window-maximize", "black"))
            窗口项目.setText(1, 组件类型)
            self.treeWidget.addTopLevelItem(窗口项目)

        for 子组件 in 结构数据['子组件']:
            子组件类型 = 子组件['组件类型']
            子组件名称 = 子组件['组件名称']
            子组件属性 = 子组件['组件属性']

            组件项目 = QTreeWidgetItem()
            组件项目.setText(0, 子组件名称)
            组件项目.setIcon(0, 获取图标("mdi.moon-new", "black"))
            组件项目.setText(1, 子组件类型)
            窗口项目.addChild(组件项目)

            self.递归导入组件树(子组件, True, 组件项目)

    def 初始化布局2(self):
        ###
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_2 = QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.horizontalLayout_3.addWidget(self.树形框项目管理)

        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout = QHBoxLayout(self.tab_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_3.addWidget(self.tabWidget)
        self.tabWidget.setTabText(0, "项目管理")
        self.tabWidget.setTabText(1, "组件属性")
        self.tabWidget.setCurrentIndex(1)
        self.tableWidget.setMinimumWidth(300)



        self.mdiArea = QMdiArea()
        self.mdiArea.setBackground(QColor(236, 236, 236))
        self.mdiArea.addSubWindow(self.设计窗口)
        self.mdiArea.setOption(QMdiArea.DontMaximizeSubWindowOnActivation)
        self.mdiArea.setViewMode(QMdiArea.SubWindowView)

        self.从上到下_右边 = QVBoxLayout()
        self.从上到下_右边.setContentsMargins(0, 0, 0, 0)
        self.从上到下_右边.addWidget(self.treeWidget, 1)
        self.从上到下_右边.addWidget(self.listWidget, 1)
        self.listWidget.setMinimumWidth(200)

        self.上下布局 = QHBoxLayout()
        self.上下布局.setContentsMargins(0, 0, 0, 0)
        self.上下布局.addWidget(self.tabWidget, 1)
        self.上下布局.addWidget(self.mdiArea, 2)
        self.上下布局.addLayout(self.从上到下_右边, 1)


        self.centralWidget.setLayout(self.上下布局)
        self.setCentralWidget(self.centralWidget)

    def 初始化布局(self):
        MainWindow = self
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.addWidget(self.tableWidget)
        self.horizontalLayout.addWidget(self.listWidget)
        self.horizontalLayout.addWidget(self.treeWidget)
        self.horizontalLayout.addWidget(self.树形框项目管理)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.addSubWindow(self.设计窗口)
        self.mdiArea.setOption(QMdiArea.DontMaximizeSubWindowOnActivation)
        self.mdiArea.setViewMode(QMdiArea.SubWindowView)
        self.verticalLayout.addWidget(self.mdiArea)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        QMetaObject.connectSlotsByName(MainWindow)

    # def 信号_代码跳转(self, 状态, 错误文本):
    #     print("信号_代码跳转", 状态, 错误文本)
    #     if 状态 == True:
    #         self.hide()
    #     else:
    #         self.setWindowTitle(错误文本)

    # 监听窗口关闭事件
    def closeEvent(self, event):
        print("窗口关闭事件111")
        self.设计窗口.可否关闭 = True
        # G.保存组件信息()
        self.设计窗口.信号_保存组件信息()
        event.accept()
        # sys.exit(0)

    def 初始化项目管理(self):
        # 修改树形框项目的标题
        self.树形框项目管理.clear()
        self.树形框项目管理.setColumnCount(1)
        # self.树形框项目管理.setHeaderLabels(["文件", "文件类型"])
        self.树形框项目管理.setHeaderLabels(["项目管理"])
        self.树形框项目管理.setColumnWidth(0, 150)
        self.树形框项目管理.setColumnWidth(1, 50)

        # 枚举当前运行目录的ui格式和py格式的文件 加入到 self.树形框项目管理 选项中加入图标 图标大小 16x16
        项目目录 = efun.文件_取目录(self.设计窗口.写出文件路径_设计文件json)
        print(项目目录)
        try:
            for 文件名 in os.listdir(项目目录):
                if 文件名.endswith(".ui"):
                    项目 = QTreeWidgetItem()
                    项目.setIcon(0, 获取图标("fa.files-o", "black"))
                    项目.setText(0, 文件名)
                    self.树形框项目管理.addTopLevelItem(项目)
                if 文件名.endswith(".json"):
                    项目 = QTreeWidgetItem()
                    项目.setIcon(0, 获取图标("fa.files-o", "black"))
                    项目.setText(0, 文件名)
                    self.树形框项目管理.addTopLevelItem(项目)
                elif 文件名.endswith(".py"):
                    项目 = QTreeWidgetItem()
                    项目.setIcon(0, 获取图标("fa.file-powerpoint-o", "black"))
                    项目.setText(0, 文件名)
                    self.树形框项目管理.addTopLevelItem(项目)
        except:
            pass
        # self.树形框项目管理被双击
        self.树形框项目管理.itemDoubleClicked.connect(self.项目管理_项目被双击)
        # 排序
        self.树形框项目管理.sortItems(0, Qt.AscendingOrder)

    def 项目管理_项目被双击(self, item):
        # print(item.text(0))
        文件路径 = self.设计窗口.项目目录 + item.text(0)
        # 检查后缀是否为 json
        if 文件路径.endswith(".json"):
            self.信号_项目管理文件被选择.emit(文件路径)

    def 初始化组件列表(self):
        # 创建列表组件
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.listWidget.itemClicked.connect(self.组件列表点击)
        # for 组件 in 取所有组件名称():
        #     self.listWidget.addItem(组件)


        item = QListWidgetItem(获取图标("fa.mouse-pointer", "black"), '指针')
        item.setSizeHint(QSize(32, 32))
        self.listWidget.addItem(item)

        名称s = 中文对照组件常量.取所有组件名称()
        for 名称 in 名称s:
            if 名称 == "主窗口":
                continue
            item = QListWidgetItem(获取图标("mdi.moon-new", "black"), 名称)
            item.setSizeHint(QSize(32, 32))
            self.listWidget.addItem(item)
            self.listWidget.setIconSize(QSize(16, 16))

    def 组件列表点击(self, item):
        print("组件列表点击", item.text())
        # 通知设计窗口绘制的组件名称
        self.信号_绘制组件名称.emit(item.text())

    def 初始化属性表格_从数据(self, 表格属性数据):
        # 表格属性数据 = [
        #     ("组件类型", "文本型", 组件类型),
        #     ("名称", "文本型", 组件.objectName()),
        #     ("顶边", "整数型", 组件.geometry().top()),
        #     ("左边", "整数型", 组件.geometry().left()),
        #     ("宽度", "整数型", 组件.geometry().width()),
        #     ("高度", "整数型", 组件.geometry().height()),
        #     ("可视", "逻辑值", 组件.isVisible() is True),
        #     ("禁用", "逻辑值", 组件.isEnabled() is False),
        #     ("鼠标指针", "选择列表型", ""),
        # ]
        # tableWidget 检查对象是否存在
        if self.tableWidget == None:
            return

        self.tableWidget.clear()
        self.tableWidget.setObjectName("tableWidget")

        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["属性", "值"])
        # 绑定表格的所有信号
        self.tableWidget.cellDoubleClicked.connect(self.表格被双击)
        # 禁止编辑
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置表格的行高和列宽
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 120)
        self.tableWidget.setEnabled(False)
        self.tableWidget.setVisible(False)
        self.tableWidget.setRowCount(len(表格属性数据))

        for i, (属性名称, 属性类型, 属性值) in enumerate(表格属性数据):
            # print("读取配置的", 属性名称, 属性类型, 属性值)
            表格属性数据_name = QTableWidgetItem(属性名称)
            # 禁止编辑 组件类型
            # if 属性名称 == "组件类型":
            #     表格属性数据_name.setFlags(Qt.ItemIsEnabled)

            self.tableWidget.setItem(i, 0, 表格属性数据_name)
            # 根据不同的类型设置不同的编辑器
            if 属性类型 == "文本型":
                inputText = QLineEdit()
                inputText.setProperty("属性名称", 属性名称)
                if 属性名称 == "组件类型":
                    # 设置为只读 禁止编辑
                    inputText.setEnabled(False)
                inputText.setText(属性值)
                inputText.editingFinished.connect(self.表格编辑完成)
                self.tableWidget.setCellWidget(i, 1, inputText)
            elif 属性类型 == "整数型":
                # 创建 QLineEdit 限制输入内容为数字
                inputText = QLineEdit()
                inputText.setProperty("属性名称", 属性名称)
                inputText.setText(str(属性值))
                inputText.setValidator(QIntValidator())
                inputText.editingFinished.connect(self.表格编辑完成)
                self.tableWidget.setCellWidget(i, 1, inputText)

            elif 属性类型 == "逻辑值":
                comboBox = QComboBox()
                comboBox.setProperty("属性名称", 属性名称)
                comboBox.addItem("假")
                comboBox.addItem("真")
                comboBox.setProperty("属性名称", 属性名称)
                self.tableWidget.setCellWidget(i, 1, comboBox)
                comboBox.setCurrentIndex(int(属性值))
                comboBox.currentIndexChanged.connect(self.表格选择框选择完成)

            self.tableWidget.setEnabled(True)
            self.tableWidget.setVisible(True)

    def 初始化属性表格(self):

        # 数据
        表格属性数据 = [
            ("组件类型", "文本型", self.pushButton.metaObject().className()),
            ("名称", "文本型", self.pushButton.objectName()),
            ("左边", "整数型", self.pushButton.geometry().left()),
            ("顶边", "整数型", self.pushButton.geometry().top()),
            ("宽度", "整数型", self.pushButton.geometry().width()),
            ("高度", "整数型", self.pushButton.geometry().height()),
            ("可视", "逻辑值", self.pushButton.isVisible()),
            ("禁用", "逻辑值", self.pushButton.isEnabled()),
            ("鼠标指针", "选择列表型", ""),
            ("事件被点击", "文本型", "事件" + self.pushButton.objectName() + "被点击")
        ]
        # 创建表格
        self.tableWidget = QTableWidget()
        return
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["属性", "值"])
        # 绑定表格的所有信号
        self.tableWidget.cellDoubleClicked.connect(self.表格被双击)
        # 禁止编辑
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置表格的行高和列宽
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setRowCount(len(表格属性数据))

        for i, (属性名称, 属性类型, 属性值) in enumerate(表格属性数据):
            print("读取", 属性名称, 属性类型, 属性值)
            表格属性数据_name = QTableWidgetItem(属性名称)
            # 禁止编辑 组件类型
            # if 属性名称 == "组件类型":
            #     表格属性数据_name.setFlags(Qt.ItemIsEnabled)

            self.tableWidget.setItem(i, 0, 表格属性数据_name)
            # 根据不同的类型设置不同的编辑器
            if 属性类型 == "文本型":
                inputText = QLineEdit()
                inputText.setProperty("属性名称", 属性名称)
                if 属性名称 == "组件类型":
                    # 设置为只读 禁止编辑
                    inputText.setEnabled(False)
                inputText.setText(属性值)
                inputText.editingFinished.connect(self.表格编辑完成)
                self.tableWidget.setCellWidget(i, 1, inputText)
            elif 属性类型 == "整数型":
                # 创建 QLineEdit 限制输入内容为数字
                inputText = QLineEdit()
                inputText.setProperty("属性名称", 属性名称)
                inputText.setText(str(属性值))
                inputText.setValidator(QIntValidator())
                inputText.editingFinished.connect(self.表格编辑完成)
                self.tableWidget.setCellWidget(i, 1, inputText)

            elif 属性类型 == "逻辑值":
                comboBox = QComboBox()
                comboBox.setProperty("属性名称", 属性名称)
                comboBox.addItem("真")
                comboBox.addItem("假")
                comboBox.setProperty("属性名称", 属性名称)
                self.tableWidget.setCellWidget(i, 1, comboBox)
                comboBox.currentIndexChanged.connect(self.表格选择框选择完成)


            elif 属性类型 == "选择列表型":
                comboBox = QComboBox()
                comboBox.setProperty("属性名称", 属性名称)
                鼠标指针选项 = ["默认型", "标准箭头型", "十字型", "文本编辑型", "沙漏型", "箭头及问号型", "箭头及沙漏型", "禁止符型", "四向箭头型", "北东箭头型",
                          "北南箭头型",
                          "北西箭头型", "西东箭头型", "向上箭头", "手型"]
                # 鼠标指针选项加入 comboBox
                for 鼠标指针选项 in 鼠标指针选项:
                    comboBox.addItem(鼠标指针选项)
                self.tableWidget.setCellWidget(i, 1, comboBox)
                comboBox.currentIndexChanged.connect(self.表格选择框选择完成)

    def 信号_更新属性框(self, obj: 组件按钮):
        # print("信号_更新属性框", obj)
        if obj:
            self.初始化属性表格_从数据(obj.导出组件属性())
            # print("信号_更新属性框", obj)
            self.当前组件库的对象 = obj

    def 信号_更新组件树(self, obj: 组件按钮):
        # print("信号_更新属性框", obj)
        if obj:
            self.刷新组件树显示()

    def 表格编辑完成(self):
        当前行 = self.tableWidget.currentRow()
        当前列 = self.tableWidget.currentColumn()
        text = self.sender().text()
        属性名称 = self.sender().property("属性名称")

        print("表格编辑完成 属性名称:{} 输入text:{} x:{} y:{}".format(属性名称, text, 当前行, 当前列))

        # self.当前组件库的对象.修改组件属性(属性名称, text)
        self.信号_修改组件的属性.emit(self.当前组件库的对象, 属性名称, text)

    def 表格复选框编辑完成(self):
        当前行 = self.tableWidget.currentRow()
        当前列 = self.tableWidget.currentColumn()
        选中 = self.sender().isChecked()
        属性名称 = self.sender().property("属性名称")

        print("表格编辑完成 属性名称:{} 选中:{} x:{} y:{}".format(属性名称, 选中, 当前行, 当前列))

    def 表格选择框选择完成(self, index):
        当前行 = self.tableWidget.currentRow()
        当前列 = self.tableWidget.currentColumn()
        text = self.sender().currentText()
        属性名称 = self.sender().property("属性名称")

        print("表格选择框选择完成 属性名称:{} 索引:{} 文本:{} x:{} y:{}".format(属性名称, index, text, 当前行, 当前列))
        # self.当前组件库的对象.修改组件属性(属性名称, text)
        self.信号_修改组件的属性.emit(self.当前组件库的对象, 属性名称, text)

    def 信号_双击跳转代码(self, 组件):
        # 查询属性表格中第一列属性文本前缀为"事件"获取行号
        属性表格行号 = self.tableWidget.findItems("事件*", Qt.MatchWildcard)[0].row()
        # 获取属性表格中第一列属性文本前缀为"事件"的属性名称
        属性名称 = self.tableWidget.item(属性表格行号, 0).text()
        print(属性名称)
        print("信号_双击跳转代码", 属性名称)
        self.表格被双击(属性表格行号, 0)

    def 表格被双击(self, row, column):
        # 当前行 = self.tableWidget.currentRow()
        # 当前列 = self.tableWidget.currentColumn()

        当前行 = row
        当前列 = column
        # 获取第一列文本
        属性名称 = self.tableWidget.item(当前行, 0).text()
        # 判断名称前缀是否有 事件
        if 属性名称.startswith("事件") is False:
            return
        属性值 = self.tableWidget.cellWidget(当前行, 1).text()
        print(f"表格被双击 属性名:{属性名称} 属性值:{属性值} x:{当前行} y:{当前列}")

        # 判断是否是事件
        名称 = self.当前组件库的对象.对象.objectName()
        if 属性值 == "":
            # 属性名称去掉前面2个字
            函数名 = 属性名称[2:]
            属性值 = f"{名称}{函数名}"
            self.tableWidget.cellWidget(当前行, 1).setText(属性值)
        else:
            函数名 = 属性值
        self.当前组件库的对象.修改组件属性(属性名称, 属性值)
        self.设计窗口.信号_保存组件信息()
        # todo 这里需要跳转代码
        self.设计窗口.信号_跳转代码(函数名)

    def 查询所有数据(self):
        for idx in range(self.tableWidget.rowCount()):
            obj = self.tableWidget.cellWidget(idx, 1)
            # print(obj)
            # 判断类型是否为 QLineEdit
            if isinstance(obj, QLineEdit):
                print("行{} 列{} 的值为 {}".format(idx, 0, obj.text()))
            elif isinstance(obj, QCheckBox):
                print("行{} 列{} 的值为 {}".format(idx, 1, obj.isChecked()))
            elif isinstance(obj, QComboBox):
                print("行{} 列{} 的值为 {}".format(idx, 1, obj.currentText()))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWin()

    设计文件路径 = r"C:\pyefun\QtEsayDesigner\test\启动窗口.json"
    window.设计窗口.可否关闭 = False
    window.设计窗口.信号_加载设计文件(设计文件路径)
    window.设计窗口.插件URL地址 = f"http://127.0.0.1:6666"
    # 配置信息加载
    window.数据刷新()
    # window.属性表格窗口.设计窗口.信号_代码跳转.connect()
    window.初始化项目管理()
    # window.初始化布局()

    # window.show()
    sys.exit(app.exec())
