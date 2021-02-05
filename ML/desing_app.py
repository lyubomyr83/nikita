# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(780, 589)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: rgb(171, 88, 92);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 12pt \"Yu Gothic UI Semibold\";\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.load = QPushButton(self.centralwidget)
        self.load.setObjectName(u"load")
        self.load.setGeometry(QRect(530, 20, 231, 71))
        self.find = QPushButton(self.centralwidget)
        self.find.setObjectName(u"find")
        self.find.setGeometry(QRect(530, 110, 231, 71))
        self.photo = QLabel(self.centralwidget)
        self.photo.setObjectName(u"photo")
        self.photo.setGeometry(QRect(20, 20, 481, 551))
        self.photo.setStyleSheet(u"background-color: rgb(143, 144, 149);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Face Detection", None))
        self.load.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044e", None))
        self.find.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 \u043b\u0438\u0446\u0430", None))
        self.photo.setText("")
    # retranslateUi

