# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_winUpdate.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)
# import update_image_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(510, 301)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(65, 64))
        self.label.setPixmap(QPixmap(u":/images/icon_128x128.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.label_bbh = QLabel(Form)
        self.label_bbh.setObjectName(u"label_bbh")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_bbh.setFont(font1)

        self.verticalLayout.addWidget(self.label_bbh)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_3.setFont(font2)

        self.verticalLayout.addWidget(self.label_3)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.label_zt = QLabel(Form)
        self.label_zt.setObjectName(u"label_zt")

        self.verticalLayout.addWidget(self.label_zt)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_tgbb = QPushButton(Form)
        self.pushButton_tgbb.setObjectName(u"pushButton_tgbb")

        self.horizontalLayout.addWidget(self.pushButton_tgbb)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_gfwz = QPushButton(Form)
        self.pushButton_gfwz.setObjectName(u"pushButton_gfwz")

        self.horizontalLayout.addWidget(self.pushButton_gfwz)

        self.pushButton_azgx = QPushButton(Form)
        self.pushButton_azgx.setObjectName(u"pushButton_azgx")
        self.pushButton_azgx.setCheckable(False)
        self.pushButton_azgx.setAutoDefault(True)
        self.pushButton_azgx.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton_azgx)

        self.pushButton_ok = QPushButton(Form)
        self.pushButton_ok.setObjectName(u"pushButton_ok")
        self.pushButton_ok.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.pushButton_ok)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        self.pushButton_azgx.setDefault(True)
        self.pushButton_ok.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8f6f\u4ef6\u66f4\u65b0", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u53d1\u73b0\u65b0\u7248\u672c", None))
        self.label_bbh.setText(QCoreApplication.translate("Form", u"\u6700\u65b0\u7248\u672c:2.0 \u5f53\u524d\u7248\u672c:1.0", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u7248\u672c\u63cf\u8ff0", None))
        self.label_zt.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u5927\u5c0f \u4e0b\u8f7d\u901f\u5ea6 \u5269\u4f59\u65f6\u95f4", None))
        self.pushButton_tgbb.setText(QCoreApplication.translate("Form", u"\u8df3\u8fc7\u7248\u672c", None))
        self.pushButton_gfwz.setText(QCoreApplication.translate("Form", u"\u5b98\u65b9\u7f51\u5740", None))
        self.pushButton_azgx.setText(QCoreApplication.translate("Form", u"\u5b89\u88c5\u66f4\u65b0", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
    # retranslateUi

