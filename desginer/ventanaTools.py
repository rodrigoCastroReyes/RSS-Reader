# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaTools.ui'
#
# Created: Sat Jul  4 00:30:21 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 200)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(400, 200))
        Form.setMaximumSize(QtCore.QSize(400, 200))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 50, 41, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalSlider = QtGui.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(80, 50, 281, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.lcdNumber = QtGui.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(160, 100, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setFrameShape(QtGui.QFrame.Box)
        self.lcdNumber.setFrameShadow(QtGui.QFrame.Raised)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 90, 120, 80))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setEnabled(True)
        self.radioButton.setGeometry(QtCore.QRect(10, 10, 102, 22))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 40, 102, 22))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Tools", None))
        self.label.setText(_translate("Form", "Time", None))
        self.radioButton.setText(_translate("Form", "Minutes", None))
        self.radioButton_2.setText(_translate("Form", "Hours", None))

