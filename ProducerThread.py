import sys
from PyQt4 import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from CargaRss import *

class ProducerThread(QThread):

	def __init__(self,buffer=None,parent = None):
		QThread.__init__(self, parent)
		self.provider=None

	def setProvider(self,url,maxFeeds):
		self.provider=Provider(0,url,maxFeeds)

	def fetchData(self):
		self.start()#llama al metodo run para traer los feeds desde el proveedor

	def run(self):
		self.provider.cargaFeeds()#descarga las noticias de internet y carga en memoria
		news=self.provider.getNews()#obtiene el texto de una noticia
		self.emit(SIGNAL("updateNews(QString)"),news)#genera un evento que sera manejado en la ventana para actualizarla

	def showData(self):
		self.provider.printFeedsList()

class Window(QWidget):

    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setWindowTitle(self.tr("RSS Reader"))
        self.showMaximized()
        self.startButton = QPushButton(self.tr("&Start"))
        layout = QGridLayout()
        layout.addWidget(self.startButton, 0,0)

        self.textArea = QTextEdit(parent)
       	self.textArea.setReadOnly(True)
       	self.textArea.setLineWrapMode(QTextEdit.NoWrap)
       	layout.addWidget(self.textArea,1,0)

       	self.thread=ProducerThread()
        self.thread.setProvider('http://www.elcomercio.com/rss/tendencias',5)
        self.connect(self.startButton, SIGNAL("clicked()"), self.runThread)
       	self.connect(self.thread,SIGNAL("updateNews(QString)"),self.updateData)
       	self.setLayout(layout)

    def runThread(self):
    	self.thread.fetchData()

    def updateData(self,news):
    	self.textArea.append(news)

class PriorityQueue():

	def __init__(self):
		pass

	def enQueue(self):
		pass

	def deQueue(self):
		pass

def main():
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())	

if __name__ == '__main__':
	main()