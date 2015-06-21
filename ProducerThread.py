import sys
import json
from PyQt4 import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from CargaRss import *


class PoolThreads():

	def __init__(self,filePath):
		self.threads=[]
		self.time=None
		self.filePath=filePath
		self.createThreads()
		self.printThreadsInformation()

	def createThreads(self):#leeer el archivo ubicado en filePath y crea los hilos en base a esa informacion
		with open(self.filePath, encoding='utf-8') as data_file:
			data = json.loads(data_file.read())
		time=int(data['time'])
		listThread=data['threads']
		for dataThreads in listThread:
			id=dataThreads["id"]
			name=dataThreads["name"]
			url=dataThreads["url"]
			maxFeeds=int(dataThreads["maxFeeds"])
			thread=ProducerThread()
			thread.setProvider(id,name,url,maxFeeds)
			self.threads.append(thread)

	def printThreadsInformation(self):
		for thread in self.threads:
			thread.printInfo()



class ProducerThread(QThread):

	def __init__(self,buffer=None,parent = None):
		QThread.__init__(self, parent)
		self.provider=None

	def setProvider(self,id,name,url,maxFeeds):
		self.provider=Provider(id,name,url,maxFeeds)

	def fetchData(self):
		self.start()#llama al metodo run para traer los feeds desde el proveedor

	def run(self):
		print("aqui en el metodo run")
		self.provider.cargaFeeds()#descarga las noticias de internet y carga en memoria
		news=self.provider.getNews()#obtiene el texto de una noticia
		self.emit(SIGNAL("updateNews(QString)"),news)#genera un evento que sera manejado en la ventana para actualizarla

	def __del__(self):
		self.wait()

	def showData(self):
		self.provider.printFeedsList()

	def printInfo(self):
		print("url:" +self.provider.getUrl())


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

       	self.pool=PoolThreads("threads.json")
       	self.thread=self.pool.threads[0]
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