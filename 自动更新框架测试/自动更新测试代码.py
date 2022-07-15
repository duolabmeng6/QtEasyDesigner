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


QT_APP = QApplication([])

APPCAST_URL = 'http://127.0.0.1:8000/SampleAppcast.xml'
SPARKLE_PATH = '/Users/chensuilong/Downloads/Sparkle-2.2.0/Sparkle.framework'

from objc import pathForFramework, loadBundle

sparkle_path = pathForFramework(SPARKLE_PATH)
objc_namespace = dict()
loadBundle('Sparkle', objc_namespace, bundle_path=sparkle_path)


def about_to_quit():
    print('about to quit')
    # 见 https://github.com/sparkle-project/Sparkle/issues/839
    objc_namespace['NSApplication'].sharedApplication().terminate_(None)


QT_APP.aboutToQuit.connect(about_to_quit)
sparkle = objc_namespace['SUUpdater'].sharedUpdater()
sparkle.setAutomaticallyChecksForUpdates_(True)
sparkle.setAutomaticallyDownloadsUpdates_(True)
NSURL = objc_namespace['NSURL']
sparkle.setFeedURL_(NSURL.URLWithString_(APPCAST_URL))
sparkle.checkForUpdatesInBackground()

window = MainWin()
window.btn.clicked.connect(about_to_quit)

sys.exit(QT_APP.exec())
