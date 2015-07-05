# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaTools.ui'
#
# Created: Wed Jun 24 22:48:43 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

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

class VentanaTools(QtGui.QDialog):

    def __init__(self, parent = None):
        super(VentanaTools, self).__init__(parent)
        self.setupUi(self)

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
        self.lcdNumber = QtGui.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(180, 100, 101, 41))
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
        self.RBMinutes = QtGui.QRadioButton(self.groupBox)
        self.RBMinutes.setEnabled(True)
        self.RBMinutes.setGeometry(QtCore.QRect(10, 10, 102, 22))
        self.RBMinutes.setChecked(True)
        self.RBMinutes.setObjectName(_fromUtf8("RBMinutes"))
        self.RBHours = QtGui.QRadioButton(self.groupBox)
        self.RBHours.setGeometry(QtCore.QRect(10, 40, 102, 22))
        self.RBHours.setObjectName(_fromUtf8("RBHours"))
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(70, 30, 301, 51))
        self.stackedWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.stackedWidget.setAcceptDrops(False)
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.stackedWidget.setFrameShadow(QtGui.QFrame.Plain)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.horizontalSlider = QtGui.QSlider(self.page)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 20, 281, 16))
        self.horizontalSlider.setMaximum(180)
        #self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setPageStep(10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.horizontalSlider.setTickInterval(10)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.horizontalSlider_2 = QtGui.QSlider(self.page_2)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(10, 20, 281, 16))
        self.horizontalSlider_2.setMaximum(24)
        self.horizontalSlider_2.setPageStep(1)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setInvertedControls(False)
        self.horizontalSlider_2.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.horizontalSlider_2.setTickInterval(1)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.horizontalSlider.valueChanged.connect(self.lcdNumber.display)
        self.horizontalSlider_2.valueChanged.connect(self.lcdNumber.display)
        self.RBMinutes.toggled.connect(self.RBMinutes_clicked)
        self.RBHours.toggled.connect(self.RBHours_clicked)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Tools", None))
        self.label.setText(_translate("Form", "Time", None))
        self.RBMinutes.setText(_translate("Form", "Minutes", None))
        self.RBHours.setText(_translate("Form", "Hours", None))

    
    def RBHours_clicked(self,activate):
    	if activate:
    		self.stackedWidget.setCurrentIndex(1)

    def RBMinutes_clicked(self,activate):
    	if activate:
    		self.stackedWidget.setCurrentIndex(0)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    vt = VentanaTools()
    vt.show()
    sys.exit(app.exec_())

