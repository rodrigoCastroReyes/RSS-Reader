import sys
from PyQt4 import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import QWebView


class Browser(QWebView):

    def __init__(self,flag):
        QWebView.__init__(self)
        self.flag=flag
        self.loadFinished.connect(self._result_available)

    def _result_available(self, ok):
        frame = self.page().mainFrame()

    def openPage(self,url):
        self.load(QUrl(url))
        self.show()

    def closeEvent(self, event):
        self.flag[0]=False
        event.accept() # let the window close