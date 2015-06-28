import sys
import json
from PyQt4 import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from CargaRss import *
from queue import *
from ProducerThread import *


class Window(QWidget):

    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setWindowTitle(self.tr("RSS Reader"))
        self.showMaximized()
        self.startButton = QPushButton(self.tr("&Start"))
        layout = QGridLayout()
        layout.addWidget(self.startButton, 0,0)

        self.showDataButton=QPushButton(self.tr("&Show"))

        layout.addWidget(self.showDataButton,1,0)

        self.textArea = QTextEdit(parent)
       	self.textArea.setReadOnly(True)
       	self.textArea.setLineWrapMode(QTextEdit.NoWrap)
       	layout.addWidget(self.textArea,2,0)

       	self.pool=PoolThreads("threads.json")
        self.connect(self.startButton, SIGNAL("clicked()"), self.runThread)
        self.connect(self.showDataButton,SIGNAL("clicked()"),self.showData)
       	
        self.connect(self.pool.getConsumerThread(),SIGNAL("updateNews(QString)"),self.updateData)
       	
        self.setLayout(layout)

    def runThread(self):
    	self.pool.startToWork()

    def showData(self):
      self.pool.printBuffer()

    def updateData(self,news):
    	self.textArea.append(news)


def main():
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec_()) 

if __name__ == '__main__':
  main()