# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(533, 741)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.label_6, 10, 0, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(True)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 7, 1, 1, 6)

        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout.addWidget(self.radioButton_2, 3, 3, 1, 2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 2)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout.addWidget(self.pushButton_11, 7, 7, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 11, 4, 1, 3)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        font = QFont()
        font.setUnderline(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 6, 1, 1, 7)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.centralwidget)
        self.buttonGroup.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.gridLayout.addWidget(self.radioButton, 3, 1, 1, 2)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 5, 3, 1, 2)

        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout.addWidget(self.pushButton_10, 5, 6, 1, 2)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 0, 7, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 11, 7, 1, 1)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 9, 5, 1, 3)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 6)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 7)

        self.radioButton_4 = QRadioButton(self.centralwidget)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.gridLayout.addWidget(self.radioButton_4, 4, 3, 1, 2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(True)

        self.gridLayout.addWidget(self.lineEdit_3, 0, 1, 1, 6)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 11, 1, 1, 3)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.plainTextEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.plainTextEdit, 10, 1, 1, 7)

        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setChecked(True)

        self.gridLayout.addWidget(self.radioButton_3, 4, 1, 1, 2)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 8)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 2, 7, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 9, 2, 1, 3)


        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.lineEdit_3, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.radioButton)
        QWidget.setTabOrder(self.radioButton, self.radioButton_2)
        QWidget.setTabOrder(self.radioButton_2, self.radioButton_3)
        QWidget.setTabOrder(self.radioButton_3, self.radioButton_4)
        QWidget.setTabOrder(self.radioButton_4, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.pushButton_6)
        QWidget.setTabOrder(self.pushButton_6, self.pushButton_10)
        QWidget.setTabOrder(self.pushButton_10, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.pushButton_11)
        QWidget.setTabOrder(self.pushButton_11, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.pushButton_9)
        QWidget.setTabOrder(self.pushButton_9, self.plainTextEdit)
        QWidget.setTabOrder(self.plainTextEdit, self.pushButton_7)
        QWidget.setTabOrder(self.pushButton_7, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_3)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u4fe1\u606f\u8f93\u51fa\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u76ee\u5f55\uff1a", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u5f55", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8d44\u6e90\u6587\u4ef6\uff1a", None))
        self.pushButton_11.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u7f16\u8bd1", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u539f\u6587\u4ef6\uff08\u5939\uff09", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u6587\u4ef6\uff08\u5939\uff09", None));
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u6e90\u7801\u6587\u4ef6\uff1a", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u5355\u6587\u4ef6", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u79fb\u9664", None))
        self.pushButton_5.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u914d\u7f6e", None))
        self.lineEdit_2.setText("")
        self.lineEdit.setText("")
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"\u6709\u63a7\u5236\u53f0\u7a0b\u5e8f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u6807\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7a97\u53e3\u7c7b\u578b\uff1a", None))
        self.lineEdit_3.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u7f16\u8bd1\u547d\u4ee4", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"APP\u540d\u79f0\uff1a", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u63a7\u5236\u53f0\u7a97\u53e3", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"*\u7559\u7a7a\u5219\u8f93\u51fa\u7f6e\u6e90\u7801\u6240\u5728\u76ee\u5f55\uff0c\u8f93\u51fa\u6587\u4ef6\u4e3abuild\uff0cdist\uff0cspec\u6587\u4ef6\u3002", None))
        self.pushButton_4.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5305\u7c7b\u578b\uff1a", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u914d\u7f6e", None))
    # retranslateUi

