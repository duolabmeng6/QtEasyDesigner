# ==导入模块==
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
import ui_启动窗口
from qtefun.组件.主窗口 import 主窗口
from qtefun.组件.按钮 import 按钮
from qtefun.组件.单行编辑框 import 单行编辑框
# ==导入模块===
class MainWin(主窗口):
    def __init__(self):
        super().__init__()
        # ==绑定事件==
        self.ui = ui_启动窗口.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show() 
        self.启动窗口 = self 
        self.按钮1 = 按钮(self.ui.按钮1)
        self.单行编辑框1 = 单行编辑框(self.ui.单行编辑框1)
        self.按钮2 = 按钮(self.ui.按钮2)
        self.按钮3 = 按钮(self.ui.按钮3)
        self.按钮4 = 按钮(self.ui.按钮4)
        self.按钮5 = 按钮(self.ui.按钮5)
        self.按钮6 = 按钮(self.ui.按钮6)
        self.按钮7 = 按钮(self.ui.按钮7)
        self.按钮8 = 按钮(self.ui.按钮8)
        self.按钮9 = 按钮(self.ui.按钮9)
        self.按钮1.绑定事件被点击(self.按钮1被点击)
        self.按钮2.绑定事件被点击(self.按钮1被点击)
        self.按钮3.绑定事件被点击(self.按钮1被点击)
        self.按钮4.绑定事件被点击(self.按钮1被点击)
        self.按钮5.绑定事件被点击(self.按钮5被点击)
        self.按钮6.绑定事件被点击(self.按钮1被点击)
        self.按钮7.绑定事件被点击(self.按钮1被点击)
        self.按钮8.绑定事件被点击(self.按钮1被点击)
        self.按钮9.绑定事件被点击(self.按钮1被点击)
        self.启动窗口创建完毕()
        # ==绑定事件===            
    def 启动窗口创建完毕(self):
        print("启动窗口创建完毕")
    def 按钮1被点击(self):
        print("按钮1被点击")
    def 按钮5被点击(self):
        print("按钮5被点击")
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWin()
    sys.exit(app.exec())
                