# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/caesar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
os.environ ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 459)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 130, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 200, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 290, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 30, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txt_plain = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_plain.setGeometry(QtCore.QRect(230, 130, 381, 41))
        self.txt_plain.setObjectName("txt_plain")
        self.txt_key = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_key.setGeometry(QtCore.QRect(230, 200, 151, 41))
        self.txt_key.setObjectName("txt_key")
        self.txt_cipher = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_cipher.setGeometry(QtCore.QRect(230, 290, 381, 41))
        self.txt_cipher.setObjectName("txt_cipher")
        self.btn_enc = QtWidgets.QPushButton(self.centralwidget)
        self.btn_enc.setGeometry(QtCore.QRect(230, 380, 75, 23))
        self.btn_enc.setObjectName("btn_enc")
        self.btn_dec = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dec.setGeometry(QtCore.QRect(530, 380, 75, 23))
        self.btn_dec.setObjectName("btn_dec")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Plain Text:"))
        self.label_2.setText(_translate("MainWindow", "Key"))
        self.label_3.setText(_translate("MainWindow", "Cipher Text"))
        self.label_4.setText(_translate("MainWindow", "Caesar"))
        self.btn_enc.setText(_translate("MainWindow", "Encrypt"))
        self.btn_dec.setText(_translate("MainWindow", "Decrypt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
