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
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/rss.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		Form.setWindowIcon(icon)
		self.verticalLayout = QtGui.QVBoxLayout(Form)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
		self.verticalLayout.addItem(spacerItem)
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem1)
		self.buttonHome = QtGui.QPushButton(Form)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.buttonHome.sizePolicy().hasHeightForWidth())
		self.buttonHome.setSizePolicy(sizePolicy)
		self.buttonHome.setText(_fromUtf8(""))
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/home.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.buttonHome.setIcon(icon1)
		self.buttonHome.setIconSize(QtCore.QSize(32, 32))
		self.buttonHome.setObjectName(_fromUtf8("buttonHome"))
		self.horizontalLayout.addWidget(self.buttonHome)
		spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem2)
		self.buttonAdd = QtGui.QPushButton(Form)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.buttonAdd.sizePolicy().hasHeightForWidth())
		self.buttonAdd.setSizePolicy(sizePolicy)
		self.buttonAdd.setText(_fromUtf8(""))
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(_fromUtf8("images/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.buttonAdd.setIcon(icon2)
		self.buttonAdd.setIconSize(QtCore.QSize(32, 32))
		self.buttonAdd.setObjectName(_fromUtf8("buttonAdd"))
		self.horizontalLayout.addWidget(self.buttonAdd)
		spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem3)
		self.buttonDecrease = QtGui.QPushButton(Form)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.buttonDecrease.sizePolicy().hasHeightForWidth())
		self.buttonDecrease.setSizePolicy(sizePolicy)
		self.buttonDecrease.setText(_fromUtf8(""))
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap(_fromUtf8("images/decrease.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.buttonDecrease.setIcon(icon3)
		self.buttonDecrease.setIconSize(QtCore.QSize(32, 32))
		self.buttonDecrease.setObjectName(_fromUtf8("buttonDecrease"))
		self.horizontalLayout.addWidget(self.buttonDecrease)
		spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem4)
		self.buttonConfig = QtGui.QPushButton(Form)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.buttonConfig.sizePolicy().hasHeightForWidth())
		self.buttonConfig.setSizePolicy(sizePolicy)
		self.buttonConfig.setText(_fromUtf8(""))
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap(_fromUtf8("images/config.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.buttonConfig.setIcon(icon4)
		self.buttonConfig.setIconSize(QtCore.QSize(32, 32))
		self.buttonConfig.setObjectName(_fromUtf8("buttonConfig"))
		self.horizontalLayout.addWidget(self.buttonConfig)
		spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem5)
		self.verticalLayout.addLayout(self.horizontalLayout)
		spacerItem6 = QtGui.QSpacerItem(20, 45, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
		self.verticalLayout.addItem(spacerItem6)
		self.textEdit = QtGui.QTextEdit(Form)
		self.textEdit.setObjectName(_fromUtf8("textEdit"))
		self.verticalLayout.addWidget(self.textEdit)
		spacerItem7 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
		self.verticalLayout.addItem(spacerItem7)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)
		# conecciones
		self.buttonAdd.pressed.connect(self.openVentanaProveedor)
		self.buttonConfig.pressed.connect(self.openVentanaTools)

		self.center()

	def center(self):
		frameGm = self.frameGeometry()
		screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
		centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
		frameGm.moveCenter(centerPoint)
		self.move(frameGm.topLeft())

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
