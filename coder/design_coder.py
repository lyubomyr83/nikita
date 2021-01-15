# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coder.ui'
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
        MainWindow.resize(465, 553)
        MainWindow.setStyleSheet(u"QMainWindow\n"
"{\n"
"	background-color: rgb(85, 0, 0);\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.text_label = QLabel(self.centralwidget)
        self.text_label.setObjectName(u"text_label")
        self.text_label.setGeometry(QRect(20, 10, 111, 41))
        self.text_label.setStyleSheet(u"font: 18pt \"Times New Roman\";")
        self.text = QTextBrowser(self.centralwidget)
        self.text.setObjectName(u"text")
        self.text.setGeometry(QRect(20, 50, 421, 192))
        self.answer_label = QLabel(self.centralwidget)
        self.answer_label.setObjectName(u"answer_label")
        self.answer_label.setGeometry(QRect(20, 250, 111, 41))
        self.answer_label.setStyleSheet(u"font: 18pt \"Times New Roman\";")
        self.answer = QTextBrowser(self.centralwidget)
        self.answer.setObjectName(u"answer")
        self.answer.setGeometry(QRect(20, 290, 421, 192))
        self.encode = QPushButton(self.centralwidget)
        self.encode.setObjectName(u"encode")
        self.encode.setGeometry(QRect(20, 490, 201, 51))
        self.decode = QPushButton(self.centralwidget)
        self.decode.setObjectName(u"decode")
        self.decode.setGeometry(QRect(240, 490, 201, 51))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.text_label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0415\u041a\u0421\u0422", None))
        self.answer_label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0422\u0412\u0415\u0422", None))
        self.encode.setText(QCoreApplication.translate("MainWindow", u"\u041a\u041e\u0414\u0418\u0420\u041e\u0412\u0410\u0422\u042c", None))
        self.decode.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0415\u041a\u041e\u0414\u0418\u0420\u041e\u0412\u0410\u0422\u042c", None))
    # retranslateUi

