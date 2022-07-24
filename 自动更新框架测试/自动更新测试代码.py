import sys

from PySide6.QtCore import QRect
from PySide6.QtWidgets import *



class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(QRect(100, 100, 400, 300))
        self.setWindowTitle('Sparkle Test')
        # 创建按钮
        self.btn = QPushButton(self)
        self.btn.setText('Check for Updates')
        self.btn.setGeometry(QRect(20, 20, 200, 40))
        self.btn.show()
        # self.aboutToQuit.connect(about_to_quit)

        self.show()


app = QApplication([])
#
APPCAST_URL = 'https://ydjisi.com/test/SampleAppcast.xml'
SPARKLE_PATH = '/Users/chensuilong/Downloads/Sparkle-1.27.1/Sparkle.framework'
import updater
updater.get_updater()

window = MainWin()
# window.btn.clicked.connect(about_to_quit)


sys.exit(app.exec())
