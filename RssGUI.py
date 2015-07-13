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
from CargaRss import *
from queue import *
from ProducerThread import *
from Browser import *
from Time import *
import sys, os
import json


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
	StyleSheet = """
	QGroupBox{
		background-color: #0080FB;
	}

	QWidget[contenedor="true"]{
		background-color: #e2e4e6;
		border: 0px;
	}

	QLineEdit{ 
		color: #0080FB; 
		font-size: 22px;
		font-weight:bold;
		margin: 0px;
		padding: 5px;
		border: 0px;
		background-color:#e2e4e6;
	}

	QLabel[noticias="true"]{
		font-size: 30px;
		padding: 1px;
	}

	QTextEdit { 
		background-color:white;
		border-radius: 8px; 
		border: 1px solid white;
		color: black;
		font-size: 18px;
		margin: 0px;
		padding: 5px;
	}
	"""

	def __init__(self, parent = None):
		super(RssGUI, self).__init__(parent)
		self.showMaximized()
		self.setupUi(self)
		self.setStyleSheet(RssGUI.StyleSheet)
		

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
		
		self.verticalLayout = QtGui.QVBoxLayout(Form)#contenedor de todos los elementos de la GUI
		self.verticalLayout.setContentsMargins(0,0,0,0)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
				
		#Barra de Menu
		self.horizontalLayout = QtGui.QHBoxLayout()# contenedor de la barra de opciones
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.horizontalLayout.addItem(
			QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
		
		#Boton Noticias
		self.buttonHome = QtGui.QPushButton(Form)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.buttonHome.sizePolicy().hasHeightForWidth())
		self.buttonHome.setSizePolicy(sizePolicy)
		self.buttonHome.setText(_fromUtf8(""))
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/home.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.buttonHome.setIcon(icon1)#boton de home
		self.buttonHome.setIconSize(QtCore.QSize(35, 35))
		self.buttonHome.setObjectName(_fromUtf8("buttonHome"))
		self.horizontalLayout.addWidget(self.buttonHome)
		self.horizontalLayout.addItem(
			QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum))
		self.connect(self.buttonHome,SIGNAL("clicked()"),self.runThread)

		#Boton Agregar Proveedor
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
		self.horizontalLayout.addItem(
			QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum))
		
		#Boton Quitar Proveedor
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
		self.horizontalLayout.addItem(
			QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
		
		#Grupo de Widgets de la barra
		self.barra=QtGui.QGroupBox()
		self.barra.setLayout(self.horizontalLayout)
		self.barra.setContentsMargins(0,0,0,0)
		self.verticalLayout.addWidget(self.barra)#se agrega la barra a la GUI

		self.scroll = QScrollArea()
		self.verticalLayout.addWidget(self.scroll)

		self.progress = QtGui.QProgressBar(self)
		self.progress.setGeometry(200,80,250,20) 
		
		#self.feeds=QtGui.QGroupBox()
		#self.feeds.setTitle("Noticias")
		self.feeds=QtGui.QWidget()
		self.feeds.setProperty("contenedor",True)
		self.containerFeeds=QVBoxLayout()
		
		noticias=QLabel("Noticias")
		noticias.setProperty("noticias", True)
		self.containerFeeds.addWidget(noticias)
		self.feeds.setLayout(self.containerFeeds)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)
		#hilos proveedores
		self.pool=PoolThreads("threads.json")#carga el pool de hilos
		self.runThread()#manda a descargar informacion a los hilos productores
		self.clock=None
		self.connect(self.pool.getConsumerThread(),SIGNAL("updateNews(PyQt_PyObject)"),self.updateData)
		#cuando el hilo consumidor extraiga datos del buffer se genera un evento que es manejado por la interfaz

		self.vT = VentanaTools(self)
		self.vP = VentanaProveedor(self)

		# conecciones
		self.buttonAdd.pressed.connect(self.openVentanaProveedor)
		self.buttonConfig.pressed.connect(self.openVentanaTools)
		
		self.flagScroll=True
		
		self.loadPage=[False]
		self.browser=Browser(self.loadPage)

		self.manageTime()
		self.center()

	def runThread(self):
		self.pool.startToWork()

	def manageTime(self):
		t=Time()
		if self.clock==None:
			self.clock=ClockThread(t.getCurrentTime(),self.pool.getTime())#obtiene el tiempo actual
			self.connect(self.clock,SIGNAL("timeOver()"),self.timeEnding)
		else:
			self.clock.setStartTime(t.getCurrentTime())

		#manda a ejecutar un hilo que consultara el tiempo
		self.clock.start()
	
	def timeEnding(self):
		print("Time is Over")
		self.pool.startToWork()
		self.manageTime()

	def updateData(self,feedNew):
		containerFeedNew=QGridLayout()
		#containerFeedNew.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
		#title=QLabel(feedNew.getTitle())
		title=FeedTitle(feedNew.getTitle())
		title.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		title.setUrl(feedNew.getLink())
		self.connect(title,SIGNAL("clicked()"),self.showNew)

		description=QTextEdit(feedNew.getDescripcion())
		description.setReadOnly(True)
		containerFeedNew.addWidget(title,0,0)
		containerFeedNew.addWidget(description,1,0)
		self.containerFeeds.addLayout(containerFeedNew)
		if self.flagScroll:
			self.flagScroll=False
			self.scrollOn()

	def showNew(self):
		if not(self.loadPage[0]):
			title=self.sender()
			self.loadPage[0]=True
			url=title.getUrl()
			if len(url)>0:
				self.browser.openPage(url)

	def scrollOn(self):		
		self.scroll.setWidget(self.feeds)
		self.scroll.setWidgetResizable(True)
		

	def center(self):
		frameGm = self.frameGeometry()
		screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
		centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
		frameGm.moveCenter(centerPoint)
		self.move(frameGm.topLeft())

	@QtCore.pyqtSlot()
	def openVentanaProveedor(self):
		self.vP.show()

	@QtCore.pyqtSlot()
	def openVentanaTools(self):
		self.vT.show()

	def retranslateUi(self, Form):
		Form.setWindowTitle(_translate("Form", "RSS Reader", None))

class FeedTitle(QLineEdit):

	def __init__(self, contents, parent = None):
		QLineEdit.__init__(self,contents,parent)
		self.setReadOnly(True)
		self.url=""

	def setUrl(self,url):
		self.url=url

	def getUrl(self):
		return self.url

	def mousePressEvent(self,event):
		self.emit(SIGNAL("clicked()"))#send click signal


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	app.setApplicationName('RssGUI')
	ex = RssGUI()
	ex.show()
	sys.exit(app.exec_())
