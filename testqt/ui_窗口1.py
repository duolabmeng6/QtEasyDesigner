
# -*- coding: utf-8 -*-
import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QMainWindow, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"窗口1")
        MainWindow.resize(400, 400)
        MainWindow.setWindowTitle(u"窗口1")
                
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
                     
        self.按钮3 = QPushButton(self.centralwidget)
        self.按钮3.setObjectName(u"按钮3")
        self.按钮3.setGeometry(QRect(107, 91, 179, 118))
        self.按钮3.setText("窗口1")
                
        self.按钮1 = QPushButton(self.centralwidget)
        self.按钮1.setObjectName(u"按钮1")
        self.按钮1.setGeometry(QRect(152, 232, 79, 66))
        self.按钮1.setText("按钮1")
                
        self.按钮2 = QPushButton(self.centralwidget)
        self.按钮2.setObjectName(u"按钮2")
        self.按钮2.setGeometry(QRect(285, 218, 64, 61))
        self.按钮2.setText("按钮2")
                
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
        
        