# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RssGUI.ui'
#
# Created: Mon Jun 22 00:18:49 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from VentanaProveedor import VentanaProveedor
from VentanaTools import VentanaTools
import sys, os

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

class RssGUI(QtGui.QWidget):

	def __init__(self, parent = None):
		super(RssGUI, self).__init__(parent)
		self.setupUi(self)

	def setupUi(self, Form):
		Form.setObjectName(_fromUtf8("Form"))
		Form.resize(555, 422)
		palette = QtGui.QPalette()
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
		brush = QtGui.QBrush(QtGui.QColor(246, 244, 242))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
		Form.setPalette(palette)
		self.horizontalLayoutWidget = QtGui.QWidget(Form)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 511, 44))
		self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
		self.horizontalLayout.setMargin(0)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.buttonHome = QtGui.QPushButton(self.horizontalLayoutWidget)
		self.buttonHome.setText(_fromUtf8(""))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/home.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.buttonHome.setIcon(icon)
		self.buttonHome.setIconSize(QtCore.QSize(32, 32))
		self.buttonHome.setObjectName(_fromUtf8("buttonHome"))
		self.horizontalLayout.addWidget(self.buttonHome)
		spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem1)
		self.buttonAdd = QtGui.QPushButton(self.horizontalLayoutWidget)
		self.buttonAdd.setText(_fromUtf8(""))
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.buttonAdd.setIcon(icon1)
		self.buttonAdd.setIconSize(QtCore.QSize(32, 32))
		self.buttonAdd.setObjectName(_fromUtf8("buttonAdd"))
		self.horizontalLayout.addWidget(self.buttonAdd)
		spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem2)
		self.buttonDecrease = QtGui.QPushButton(self.horizontalLayoutWidget)
		self.buttonDecrease.setText(_fromUtf8(""))
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(_fromUtf8("images/decrease.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.buttonDecrease.setIcon(icon2)
		self.buttonDecrease.setIconSize(QtCore.QSize(32, 32))
		self.buttonDecrease.setObjectName(_fromUtf8("buttonDecrease"))
		self.horizontalLayout.addWidget(self.buttonDecrease)
		spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem3)
		self.buttonConfig = QtGui.QPushButton(self.horizontalLayoutWidget)
		self.buttonConfig.setText(_fromUtf8(""))
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap(_fromUtf8("images/config.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.buttonConfig.setIcon(icon3)
		self.buttonConfig.setIconSize(QtCore.QSize(32, 32))
		self.buttonConfig.setObjectName(_fromUtf8("buttonConfig"))
		self.horizontalLayout.addWidget(self.buttonConfig)
		spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem4)
		self.scrollArea = QtGui.QScrollArea(Form)
		self.scrollArea.setGeometry(QtCore.QRect(20, 90, 511, 311))
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
		self.scrollAreaWidgetContents = QtGui.QWidget()
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 509, 309))
		self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
		self.listNews = QtGui.QListView(self.scrollAreaWidgetContents)
		self.listNews.setGeometry(QtCore.QRect(0, 0, 511, 311))
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)
		# conecciones
		self.buttonAdd.pressed.connect(self.openVentanaProveedor)
		self.buttonConfig.pressed.connect(self.openVentanaTools)

	@QtCore.pyqtSlot()
	def openVentanaProveedor(self):
		self.vP = VentanaProveedor(self)
		self.vP.show()

	@QtCore.pyqtSlot()
	def openVentanaTools(self):
		self.vT = VentanaTools(self)
		self.vT.show()

	def retranslateUi(self, Form):
		Form.setWindowTitle(_translate("Form", "RSS Reader", None))

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	app.setApplicationName('RssGUI')
	ex = RssGUI()
	ex.show()
	sys.exit(app.exec_())