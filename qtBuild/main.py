# -*- coding: UTF-8 -*-
# author:Zhang Lei
# datetime:2022/7/25 19:52
# software: PyCharm

import json
import os
import platform
import subprocess

# yapf: enable
import qtawesome as qta
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QTextCursor
# yapf: disable
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox, QTableWidgetItem
from ui import Ui_MainWindow
APPNAME = 'Auto Py to App'
VERSION = '0.0.1'


class Main_Window(QMainWindow):

    def __init__(self):
        super().__init__()
        # 声明Tools类
        self.useTools = Tools()
        # 声明UI类
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 固定窗口大小
        self.setFixedSize(self.width(), self.height())
        # 设置窗口标题
        self.setWindowTitle(APPNAME + ' ' + VERSION)
        # 绑定源码选择按钮事件
        self.ui.pushButton_5.clicked.connect(self.selectCode)
        self.ui.pushButton_5.setIcon(qta.icon('fa.file-code-o'))
        # 绑定资源文件选择按钮事件
        self.ui.pushButton.clicked.connect(self.selectResourceFile)
        self.ui.pushButton.setIcon(qta.icon('fa.file-o'))
        # 绑定资源文件夹选择按钮事件
        self.ui.pushButton_6.clicked.connect(self.selectResourceFolder)
        self.ui.pushButton_6.setIcon(qta.icon('fa.folder-o'))
        # 绑定资源文件/夹移除按钮事件
        self.ui.pushButton_10.clicked.connect(self.deleteResourceFile)
        self.ui.pushButton_10.setIcon(qta.icon('fa.trash-o'))
        # 绑定编译输出目录按钮事件
        self.ui.pushButton_11.clicked.connect(self.selectBuildPath)
        self.ui.pushButton_11.setIcon(qta.icon('fa.folder-o'))
        # 绑定选择图标按钮事件
        self.ui.pushButton_4.clicked.connect(self.selectIcon)
        self.ui.pushButton_4.setIcon(qta.icon('fa.file-image-o'))
        # 绑定退出按钮事件
        self.ui.pushButton_3.clicked.connect(self.appExit)
        self.ui.pushButton_3.setIcon(qta.icon('fa.sign-out'))
        # 绑定编译按钮事件
        self.ui.pushButton_2.clicked.connect(self.build)
        self.ui.pushButton_2.setIcon(qta.icon('fa.terminal'))
        # 绑定读取配置按钮事件
        self.ui.pushButton_8.clicked.connect(self.readConfig)
        self.ui.pushButton_8.setIcon(qta.icon('fa.file-text-o'))
        # 绑定保存配置按钮事件
        self.ui.pushButton_9.clicked.connect(self.saveConfig)
        self.ui.pushButton_9.setIcon(qta.icon('fa.clipboard'))
        # 绑定生成编译命令按钮事件
        self.ui.pushButton_7.clicked.connect(self.generateBuldCommand)
        self.ui.pushButton_7.setIcon(qta.icon('fa.pencil'))
        # 设置表格列宽
        self.ui.tableWidget.setColumnWidth(0, 200)
        self.ui.tableWidget.setColumnWidth(1, 200)
        # 置状态栏信息
        self.ui.statusbar.showMessage('等待指令...')
        # 置plainTextEdit文本框背景与字体颜色
        # self.ui.plainTextEdit.setStyleSheet("QPlainTextEdit{color: #99ff00;background-color: black;}")
        # 初始化线程
        self.work_thread = None

    # 源码选择按钮
    def selectCode(self):
        # 获取源码路径
        codePath = QFileDialog.getOpenFileName(self, caption='选择Python源码文件', dir=os.getcwd(), filter='*.py')
        # 设置源码路径
        if codePath[0] not in ['', None]:
            self.ui.lineEdit_3.setText(codePath[0])

    # 图标选择按钮
    def selectIcon(self):
        # 获取图标路径
        iconPath = QFileDialog.getOpenFileName(self, caption='选择图标', dir=os.getcwd(), filter='Icon Files (*.ico *.icns)')
        if iconPath[0] not in ['', None]:
            # 设置源码路径
            self.ui.lineEdit_2.setText(iconPath[0])

    # 资源文件选择按钮
    def selectResourceFile(self):
        # 资源文件路径
        resourceFile = QFileDialog.getOpenFileName(self, caption='选择资源文件', dir=os.getcwd(), filter='All Files (*)')
        if resourceFile[0] not in ['', None]:
            # 插入表格内容
            self.ui.tableWidget.insertRow(0)  # 插入到第一行
            self.setTable(0, 0, resourceFile[0])
            self.setTable(0, 1, '.')

    def selectResourceFolder(self):
        # 获取资源文件夹路径
        resourceFolder = QFileDialog.getExistingDirectory(self, caption='选择资源文件夹', dir=os.getcwd(), options=QFileDialog.ShowDirsOnly)
        if resourceFolder not in ['', None]:
            # 插入表格内容
            self.ui.tableWidget.insertRow(0)
            self.setTable(0, 0, resourceFolder)
            self.setTable(0, 1, resourceFolder.split('/')[-1] + '/')

    def deleteResourceFile(self):
        # 删除表格选择的行
        if self.ui.tableWidget.currentRow() == -1:
            QMessageBox.warning(self, '警告', '请选择要删除的资源文件/夹！')
            return
        self.ui.tableWidget.removeRow(self.ui.tableWidget.currentRow())

    def selectBuildPath(self):
        # 获取编译输出文件夹
        buildPath = QFileDialog.getExistingDirectory(self, caption='选择编译输出文件夹', dir=os.getcwd(), options=QFileDialog.ShowDirsOnly)
        if buildPath not in ['', None]:
            # 设置编译输出文件夹
            self.ui.lineEdit_4.setText(buildPath)

    def saveConfig(self):
        if self.formValidation():
            # 保存配置
            config = {
                'codePath': self.ui.lineEdit_3.text(),
                'appName': self.ui.lineEdit.text(),
                'iconPath': self.ui.lineEdit_2.text(),
                'resourceFiles': self.getTable(),
                'buildType': self.ui.radioButton.isChecked(),
                'windowType': self.ui.radioButton_3.isChecked(),
                'buildPath': self.ui.lineEdit_4.text(),
            }
            print(config)
            # 获取选择的配置文件路径
            configPath = QFileDialog.getSaveFileName(self, caption='保存配置文件', dir=os.path.expanduser('~/Documents/config.json'), filter='Json (*.json)')
            if configPath[0] not in ['', None]:
                with open(file=configPath[0], mode='w') as f:
                    json.dump(config, f)
                QMessageBox.information(self, '提示', '配置文件保存成功！')

    def readConfig(self):
        # 读取配置
        configPath = QFileDialog.getOpenFileName(self, caption='读取配置文件', dir=os.path.expanduser('~/Documents'), filter='Json (*.json)')
        if configPath[0] not in ['', None]:
            with open(file=configPath[0], mode='r') as f:
                config = json.load(f)
                self.ui.lineEdit_3.setText(config['codePath'])
                self.ui.lineEdit.setText(config['appName'])
                self.ui.lineEdit_2.setText(config['iconPath'])
                if len(config.get('resourceFiles')) > 0:
                    # 清空表格
                    self.ui.tableWidget.setRowCount(0)
                    for i in range(len(config.get('resourceFiles'))):
                        self.ui.tableWidget.insertRow(0)
                        self.setTable(0, 0, config.get('resourceFiles')[i][0])
                        self.setTable(0, 1, config.get('resourceFiles')[i][1])
                if config.get('buildType'):
                    self.ui.radioButton.setChecked(True)
                else:
                    self.ui.radioButton_2.setChecked(True)
                if config.get('windowType'):
                    self.ui.radioButton_3.setChecked(True)
                else:
                    self.ui.radioButton_4.setChecked(True)
                self.ui.lineEdit_4.setText(config['buildPath'])

    def generateBuldCommand(self):
        if self.formValidation():
            self.ui.statusbar.showMessage('正在生成编译命令...')
            self.ui.plainTextEdit.setPlainText(self.getBuildText())
            self.ui.statusbar.showMessage('生成编译命令完成...')

    # 编译按钮
    def build(self):
        if self.formValidation():
            # 置plainTextEdit文本框空内容
            self.ui.plainTextEdit.setPlainText('')
            # 创建线程并且传递参数
            # self.work_thread = WorkThread(r'ping -c 20 192.168.5.1')
            self.work_thread = WorkThread(r'' + self.getBuildText())
            # 连接线程开始的信号
            self.work_thread.startTrigger.connect(self.buildStart)
            # 连接线程运行中结果的信号
            self.work_thread.cmdResultTrigger.connect(self.cmdUpdateText)
            # 连接线程完成的信号
            self.work_thread.finishTrigger.connect(self.buildFinish)
            # 开始线程
            self.work_thread.start()

    def buildStart(self, text):
        # 置状态栏开始信息
        self.ui.statusbar.showMessage(text)
        # 设置按钮禁止点击
        self.ui.pushButton_2.setEnabled(False)

    def cmdUpdateText(self, text):
        # 由于自定义信号时自动传递一个字符串参数，所以在这个槽函数中要接受一个参数
        self.ui.plainTextEdit.appendPlainText(text)
        self.ui.plainTextEdit.moveCursor(QTextCursor.End)

    def buildFinish(self, text):
        # 置状态栏完成信息
        self.ui.statusbar.showMessage(text)
        # 设置按钮可以点击
        self.ui.pushButton_2.setEnabled(True)

    # 退出按钮
    def appExit(self):
        reply = QMessageBox.question(self, '提示', '是否退出程序？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
        else:
            print("取消退出")

    # 取表格所有内容
    def getTable(self):
        rowCount = self.ui.tableWidget.rowCount()
        # print(rowCount)
        colCount = self.ui.tableWidget.columnCount()
        resultList = []
        for row in range(rowCount):
            results = []
            for col in range(colCount):
                results.append(self.ui.tableWidget.item(row, col).text())
                # print(self.ui.tableWidget.item(row, col).text())
            resultList.append(results)
        return resultList

    # 新增表格内容
    def setTable(self, row, col, text):
        newItem = QTableWidgetItem(text)
        # 居中显示
        newItem.setTextAlignment(Qt.AlignCenter)
        self.ui.tableWidget.setItem(row, col, newItem)

    # 表单验证
    def formValidation(self):
        if self.ui.lineEdit_3.text() == '' or self.ui.lineEdit.text() == '':
            QMessageBox.warning(self, '警告', '请先选择源码文件和设置APP名称！')
            if self.ui.lineEdit_3.text() == '':
                self.ui.lineEdit_3.setFocus()
            else:
                self.ui.lineEdit.setFocus()
            return False
        return True

    # 获取编译命令
    def getBuildText(self):
        # 获取源码路径
        codePath = self.ui.lineEdit_3.text()
        # 获取APP名称
        appName = self.ui.lineEdit.text()
        # 获取图标路径
        iconPath = self.ui.lineEdit_2.text()
        # 获取资源文件路径
        resourceFiles = self.getTable()
        # 获取构建类型
        buildType = self.ui.radioButton.isChecked()
        # 获取窗口类型
        windowType = self.ui.radioButton_3.isChecked()
        # 生成编译命令
        __name = 'pyinstaller --name="' + appName + '"'
        __buildType = '-F' if buildType else '-D'
        __window = '-w' if windowType else '-c'
        __icon = '-i ' + iconPath if iconPath else ''
        __codePath = ' ' + codePath
        __resourceFiles = ''
        if len(resourceFiles) > 0:
            __resourceFiles = ''
            for i in range(len(resourceFiles)):
                if self.useTools.getSystemVersion() in ['Darwin', 'Linux']:
                    __resourceFile = ' --add-data "' + resourceFiles[i][0] + ':' + resourceFiles[i][1] + '"'
                else:
                    __resourceFile = ' --add-data "' + resourceFiles[i][0] + ';' + resourceFiles[i][1] + '"'
                __resourceFiles += __resourceFile
        if self.ui.lineEdit_4.text() == '':
            __outputPath = ' --specpath ' + os.path.dirname(codePath) + ' --workpath ' + os.path.dirname(codePath) + '/build' + ' --distpath ' + os.path.dirname(codePath) + '/dist'
        else:
            __outputPath = ' --specpath ' + self.ui.lineEdit_4.text() + ' --workpath ' + self.ui.lineEdit_4.text() + '/build' + ' --distpath ' + self.ui.lineEdit_4.text() + '/dist'
        return __name + ' ' + __buildType + ' ' + __window + ' ' + __icon + __resourceFiles + __outputPath + __codePath


class WorkThread(QThread):
    # 自定义信号对象,参数str就代表这个信号可以传一个字符串
    startTrigger = Signal(str)
    cmdResultTrigger = Signal(str)
    finishTrigger = Signal(str)

    def __init__(self, cmdText, parent=None):
        super(WorkThread, self).__init__(parent)
        # 执行cmd命令参数变量
        self.cmdText = cmdText
        # 开始信号的触发
        self.started.connect(self.start_function)
        # 结束信号的触发
        self.finished.connect(self.finish)

    def start_function(self):
        print('运行开始')
        self.startTrigger.emit('正在进行源码编译...')

    def finish(self):
        print('运行完成')
        self.finishTrigger.emit('源码编译完成...')

    def run(self):
        """
        开启子进程，执行对应指令，控制台打印执行过程，然后返回子进程执行的状态码和执行返回的数据
        :return: 子进程状态码
        """
        p = subprocess.Popen(self.cmdText, shell=True, close_fds=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while p.poll() is None:
            line = p.stdout.readline().rstrip().decode('utf-8')
            if not line:
                continue
            self.cmdResultTrigger.emit(line)
        last_line = p.stdout.read().rstrip().decode('utf-8')
        if last_line:
            self.cmdResultTrigger.emit(last_line)
        p.stdout.close()
        p.wait()


class Tools:
    # TODO: 工具代码块，所有方法代码都集中写在这里。
    def __init__(self):
        pass

    # 取系统版本
    def getSystemVersion(self):  # Darwin=macOS
        # Windows,Darwin,Linux
        return platform.system()


if __name__ == '__main__':
    app = QApplication([])
    window = Main_Window()
    window.show()
    app.exec()
