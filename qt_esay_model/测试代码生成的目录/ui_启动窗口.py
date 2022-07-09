
# -*- coding: utf-8 -*-
import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QLineEdit, QPushButton)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"启动窗口")
        MainWindow.resize(400, 400)
        MainWindow.setWindowTitle(u"启动窗口")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.按钮1 = QPushButton(self.centralwidget)
        self.按钮1.setObjectName(u"按钮1")
        self.按钮1.setGeometry(QRect(38, 38, 138, 69))
        self.按钮1.setText("按钮1")
        self.单行编辑框1 = QLineEdit(self.centralwidget)
        self.单行编辑框1.setObjectName(u"单行编辑框1")
        self.单行编辑框1.setGeometry(QRect(253, 38, 121, 68))
        self.单行编辑框1.setText("单行编辑框1")
        self.按钮2 = QPushButton(self.centralwidget)
        self.按钮2.setObjectName(u"按钮2")
        self.按钮2.setGeometry(QRect(83, 66, 138, 69))
        self.按钮2.setText("按钮1")
        self.按钮3 = QPushButton(self.centralwidget)
        self.按钮3.setObjectName(u"按钮3")
        self.按钮3.setGeometry(QRect(154, 100, 138, 69))
        self.按钮3.setText("按钮1")
        self.按钮4 = QPushButton(self.centralwidget)
        self.按钮4.setObjectName(u"按钮4")
        self.按钮4.setGeometry(QRect(103, 86, 138, 69))
        self.按钮4.setText("按钮1")
        self.按钮5 = QPushButton(self.centralwidget)
        self.按钮5.setObjectName(u"按钮5")
        self.按钮5.setGeometry(QRect(58, 158, 138, 69))
        self.按钮5.setText("按钮1")
        self.按钮6 = QPushButton(self.centralwidget)
        self.按钮6.setObjectName(u"按钮6")
        self.按钮6.setGeometry(QRect(103, 86, 138, 69))
        self.按钮6.setText("按钮1")
        self.按钮7 = QPushButton(self.centralwidget)
        self.按钮7.setObjectName(u"按钮7")
        self.按钮7.setGeometry(QRect(188, 183, 138, 69))
        self.按钮7.setText("按钮1")
        self.按钮8 = QPushButton(self.centralwidget)
        self.按钮8.setObjectName(u"按钮8")
        self.按钮8.setGeometry(QRect(120, 90, 138, 69))
        self.按钮8.setText("按钮1")
        self.按钮9 = QPushButton(self.centralwidget)
        self.按钮9.setObjectName(u"按钮9")
        self.按钮9.setGeometry(QRect(82, 231, 138, 69))
        self.按钮9.setText("按钮1")
        MainWindow.setCentralWidget(self.centralwidget)
        QMetaObject.connectSlotsByName(MainWindow)

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
