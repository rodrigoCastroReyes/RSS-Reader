# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaProveedor.ui'
#
# Created: Wed Jun 24 22:20:00 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from CargaRss import *
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

class VentanaProveedor(QtGui.QDialog):

    def __init__(self, parent = None):
        self.listNewFeeds= []
        self.newsProviders= []
        super(VentanaProveedor, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(716, 480)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(198, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setMargin(10)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 694, 423))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.addButton = QtGui.QPushButton(Form)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.verticalLayout.addWidget(self.addButton)
        self.loadNewProviders()
        self.showNewsProviders(Form)
        self.addButton.pressed.connect(self.addButton_clicked)

        self.retranslateUi(Form)

    def addButton_clicked(self):
        self.listNewFeeds= []
        for i in range (1, len(self.checks)):
            if (self.checks[i-1].isChecked()):
                self.listNewFeeds.append(self.newsProviders[i-1])
                self.newsProviders.remove(self.newsProviders[i-1])
                print("Se ha añadido el proveedor: " + self.newsProviders[i-1].getName())
        #self.refreshNewProvidersFile()


    def refreshNewProvidersFile(self):
        c=1
        self.list=[]
        outFile = open("newsProviders.json","w")
        for i in range (1, len(self.newsProviders)):
            dato = {"id":c,"name":self.newsProviders[i-1].getName(),"url":self.newsProviders[i-1].getUrl(),"maxFeeds":"5"},
            json.dump(dato,outFile,indent=4)
            #print(dato)
            c+=1
        outFile.close()


    def deleteProvider(self):

        for i in range (1, len(self.listNewFeeds)):
            print(self.listNewFeeds[i-1].printAllProvider())



    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Agregar Proveedor", None))
        self.addButton.setText(_translate("Form", "Add", None))

#Permite cargar lista de nuevos proveedores para que el usuairo se pueda suscribir

    def loadNewProviders(self):#leeer el archivo ubicado en filePath y crea los hilos en base a esa informacion
        with open("newsProviders.json", encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
        self.time=int(data['time'])
        providers=data['threads']
        for dataProv in providers:
            self.prov = Provider(dataProv["id"], dataProv["name"], dataProv["url"], int(dataProv["maxFeeds"]))
            self.newsProviders.append(self.prov)
        #self.printNewsProviders()

    def showNewsProviders(self, Form):
        self.checks = []
        for i in range (1, len(self.newsProviders)):
            newProviderBOX = QtGui.QHBoxLayout()
            cB = QtGui.QCheckBox(self.newsProviders[i-1].printAllProvider())
            self.checks.append(cB)
            newProviderBOX.addWidget(cB)
            self.verticalLayout_2.addLayout(newProviderBOX)

    def printNewsProviders(self):
        for i in range (1, len(self.newsProviders)):
            print(self.newsProviders[i-1].printAllProvider())

