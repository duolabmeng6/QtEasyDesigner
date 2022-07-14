
# -*- coding: utf-8 -*-
import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QMainWindow, QLineEdit, QWidget)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"启动窗口")
        MainWindow.resize(400, 360)
        MainWindow.setWindowTitle(u"启动窗口")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.按钮18 = QPushButton(self.centralwidget)
        self.按钮18.setObjectName(u"按钮18")
        self.按钮18.setGeometry(QRect(41, 57, 109, 71))
        self.按钮18.setText("按钮29")
        self.按钮19 = QPushButton(self.centralwidget)
        self.按钮19.setObjectName(u"按钮19")
        self.按钮19.setGeometry(QRect(116, -5, 86, 52))
        self.按钮19.setText("按钮29")
        self.按钮20 = QPushButton(self.centralwidget)
        self.按钮20.setObjectName(u"按钮20")
        self.按钮20.setGeometry(QRect(117, 122, 109, 71))
        self.按钮20.setText("按钮29")
        self.按钮21 = QPushButton(self.centralwidget)
        self.按钮21.setObjectName(u"按钮21")
        self.按钮21.setGeometry(QRect(39, 128, 109, 71))
        self.按钮21.setText("按钮29")
        self.按钮22 = QPushButton(self.centralwidget)
        self.按钮22.setObjectName(u"按钮22")
        self.按钮22.setGeometry(QRect(53, 198, 109, 71))
        self.按钮22.setText("按钮7")
        self.单行编辑框3 = QLineEdit(self.centralwidget)
        self.单行编辑框3.setObjectName(u"单行编辑框3")
        self.单行编辑框3.setGeometry(QRect(190, 48, 109, 71))
        self.单行编辑框3.setText("单行编辑框1")
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
