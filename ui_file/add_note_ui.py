# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_note.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(280, 349)
        MainWindow.setStyleSheet("background-color: transparent;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("QWidget#widget {\n"
"    border-radius: 20px;\n"
"    background-color: rgba(66, 2, 157);\n"
"}\n"
"\n"
"#button_Save {\n"
"    background-color: rgba(255, 255, 255,.7);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#lineTheme {\n"
"    background-color: rgba(255, 255, 255, .7);\n"
"    border-radius: 5px;\n"
"    color: rgb(105, 0, 255);\n"
"}\n"
"\n"
"#time_label, #theme_label {\n"
"\n"
"    \n"
"    color: rgba(255, 255, 255);\n"
"}\n"
"\n"
"#note_edit {\n"
"\n"
"    color: rgb(66, 2, 157);\n"
"    border-radius: 10px;\n"
"    background-color: rgba(255, 255, 255, .7);\n"
"}\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 6)
        self.gridLayout_2.setHorizontalSpacing(4)
        self.gridLayout_2.setVerticalSpacing(7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.theme_label = QtWidgets.QLabel(self.widget)
        self.theme_label.setMinimumSize(QtCore.QSize(55, 20))
        self.theme_label.setMaximumSize(QtCore.QSize(55, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.theme_label.setFont(font)
        self.theme_label.setStyleSheet("")
        self.theme_label.setObjectName("theme_label")
        self.gridLayout_2.addWidget(self.theme_label, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(145, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 3)
        self.button_Save = QtWidgets.QPushButton(self.widget)
        self.button_Save.setMinimumSize(QtCore.QSize(110, 30))
        self.button_Save.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_Save.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_Save.setIcon(icon)
        self.button_Save.setIconSize(QtCore.QSize(20, 20))
        self.button_Save.setObjectName("button_Save")
        self.gridLayout_2.addWidget(self.button_Save, 3, 3, 1, 2)
        self.note_edit = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.note_edit.setFont(font)
        self.note_edit.setStyleSheet("")
        self.note_edit.setObjectName("note_edit")
        self.gridLayout_2.addWidget(self.note_edit, 2, 0, 1, 5)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMaximumSize(QtCore.QSize(30, 30))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/image/images/logo_main.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 2, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.time_label = QtWidgets.QLabel(self.widget)
        self.time_label.setMinimumSize(QtCore.QSize(0, 20))
        self.time_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("")
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        self.gridLayout_2.addWidget(self.time_label, 1, 3, 1, 2)
        self.lineTheme = QtWidgets.QLineEdit(self.widget)
        self.lineTheme.setMinimumSize(QtCore.QSize(80, 0))
        self.lineTheme.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineTheme.setFont(font)
        self.lineTheme.setStyleSheet("")
        self.lineTheme.setObjectName("lineTheme")
        self.gridLayout_2.addWidget(self.lineTheme, 1, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(16, 16))
        self.pushButton.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButton.setSizeIncrement(QtCore.QSize(16, 16))
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icon/x-circle 1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 4, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.theme_label.setText(_translate("MainWindow", "Theme:"))
        self.button_Save.setText(_translate("MainWindow", "Save note"))
        self.time_label.setText(_translate("MainWindow", "20:20 Jun 21"))

import static.resources_rc
