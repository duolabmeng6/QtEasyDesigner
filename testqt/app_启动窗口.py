# ==导入模块==
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
import ui_启动窗口
from qtefun.组件.按钮 import 按钮
# ==导入模块===
class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        # ==绑定事件==
        self.ui = ui_启动窗口.Ui_MainWindow()
        self.ui.setupUi(self)
        self.启动窗口创建完毕()
        self.show() 
        self.ui.按钮1 = 按钮(self.ui.按钮1)
        self.ui.按钮1.绑定事件被点击(self.按钮1被点击)
        # ==绑定事件===
    def 按钮1被点击(self):
        print("按钮1被点击")
                
    def 启动窗口创建完毕(self):
        print("启动窗口创建完毕")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWin()
    sys.exit(app.exec())
        