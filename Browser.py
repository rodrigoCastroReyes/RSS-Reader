# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'web.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4 import QtWebKit
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

class Browser(QtGui.QWidget):

    def __init__(self, flag):
        super(Browser, self).__init__(None)
        self.flag=flag
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(990, 702)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.webView = QtWebKit.QWebView(Form)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout.addWidget(self.webView)
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        spacerItem1 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)
        #QtCore.QObject.connect(self.webView, QtCore.SIGNAL(_fromUtf8("loadProgress(int)")), self.progressBar.setValue)
        self.webView.loadProgress.connect(self.progressBar.setValue)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def openPage(self,url):
        self.webView.load(QtCore.QUrl(url))
        self.show()

    def closeEvent(self, event):
        self.flag[0]=False
        event.accept() # let the window close

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Browser", "Browser", None))

