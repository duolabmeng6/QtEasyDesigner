# ==导入模块==
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
import ui_窗口3
from qtefun.组件.单行编辑框 import 单行编辑框
from qtefun.组件.按钮 import 按钮
# ==导入模块===

class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        # ==绑定事件==
        self.ui = ui_窗口3.Ui_MainWindow()
        self.ui.setupUi(self)
        self.窗口3创建完毕()
        self.show() 
        self.ui.按钮1 = 按钮(self.ui.按钮1)
        self.ui.按钮1.绑定事件被点击(self.按钮1被点击)
        self.ui.单行编辑框2 = 单行编辑框(self.ui.单行编辑框2)
        self.ui.单行编辑框2.绑定事件内容被改变(self.单行编辑框2内容被改变)
        # ==绑定事件===
    def 窗口3创建完毕(self):
        print("窗口3创建完毕")
            
    def 按钮1被点击(self):
        print("按钮1被点击")
                
    def 单行编辑框2内容被改变(self):
        print("单行编辑框2内容被改变")
                

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWin()
    sys.exit(app.exec())
        