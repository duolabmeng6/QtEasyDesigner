import sys

from PySide6.QtWidgets import QApplication

import app_启动窗口
import app_窗口1

# 加载 两个窗口


app = QApplication([])
启动窗口 = app_启动窗口.MainWin()
窗口1 = app_窗口1.MainWin()

启动窗口.show()
窗口1.show()
sys.exit(app.exec())