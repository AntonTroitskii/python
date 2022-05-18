# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(419, 85)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.le_c = QLineEdit(self.centralwidget)
        self.le_c.setObjectName(u"le_c")
        self.le_c.setGeometry(QRect(10, 20, 113, 21))
        self.lbl_plus = QLabel(self.centralwidget)
        self.lbl_plus.setObjectName(u"lbl_plus")
        self.lbl_plus.setGeometry(QRect(130, 20, 16, 16))
        self.le_d = QLineEdit(self.centralwidget)
        self.le_d.setObjectName(u"le_d")
        self.le_d.setGeometry(QRect(150, 20, 113, 21))
        self.le_result = QLineEdit(self.centralwidget)
        self.le_result.setObjectName(u"le_result")
        self.le_result.setGeometry(QRect(290, 20, 113, 21))
        self.lbl_equal = QLabel(self.centralwidget)
        self.lbl_equal.setObjectName(u"lbl_equal")
        self.lbl_equal.setGeometry(QRect(270, 20, 16, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 419, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.lbl_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
    # retranslateUi
