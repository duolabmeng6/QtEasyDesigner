
# -*- coding: utf-8 -*-
import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPlainTextEdit, QMainWindow, QLineEdit, QPushButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"窗口3")
        MainWindow.resize(400, 400)
        MainWindow.setWindowTitle(u"窗口3")
                
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
                     
        self.按钮1 = QPushButton(self.centralwidget)
        self.按钮1.setObjectName(u"按钮1")
        self.按钮1.setGeometry(QRect(79, 164, 112, 63))
        self.按钮1.setText("窗口3")
                
        self.单行编辑框2 = QLineEdit(self.centralwidget)
        self.单行编辑框2.setObjectName(u"单行编辑框2")
        self.单行编辑框2.setGeometry(QRect(232, 166, 128, 70))
        self.单行编辑框2.setText("单行编辑框2")
                
        self.纯文本编辑框3 = QPlainTextEdit(self.centralwidget)
        self.纯文本编辑框3.setObjectName(u"纯文本编辑框3")
        self.纯文本编辑框3.setGeometry(QRect(164, 270, 114, 61))
        self.纯文本编辑框3.setPlainText("纯文本编辑框3")
                
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)


        
    def retranslateUi(self,MainWindow):
        pass

    # retranslateUi
        
class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWin()
    sys.exit(app.exec())
        
        