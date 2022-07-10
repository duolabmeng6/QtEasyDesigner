""" 加入菜单栏以后设计窗口最大化会bug 待修复"""
import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import win_属性表格

class 主窗口(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Qt视窗设计器")
        self.resize(1200, 600)
        self.小部件 = win_属性表格.MainWin()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        lay = QVBoxLayout(central_widget)
        lay.addWidget(self.小部件)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = 主窗口()
    win.show()
    sys.exit(app.exec())
