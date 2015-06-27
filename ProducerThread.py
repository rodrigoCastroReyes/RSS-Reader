import sys
import json
from PyQt4 import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from CargaRss import *
from queue import *


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
       	self.thread=self.pool.threads[random.randrange(0,len(self.pool.threads)-1)]

        self.connect(self.startButton, SIGNAL("clicked()"), self.runThread)
       	self.connect(self.thread,SIGNAL("updateNews(QString)"),self.updateData)
       	self.setLayout(layout)

    def runThread(self):
    	self.thread.fetchData()

    def updateData(self,news):
    	self.textArea.append(news)


class PoolThreads():

	def __init__(self,filePath):
		self.threads=[]
		self.buffer=Buffer()#inicializa el buffer que guardara las noticias: coleccion compartida
		self.time=None#define el tiempo en el los hilos hacen la consulta
		self.filePath=filePath#directorio del archivo que tiene informacion sobre los hilos
		self.createThreads()#crea el pool de threads

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
			thread=ProducerThread(self.buffer)
			thread.setProvider(id,name,url,maxFeeds)
			self.threads.append(thread)


class ProducerThread(QThread):

	def __init__(self,buffer,parent = None):
		QThread.__init__(self, parent)
		self.provider=None
		self.buffer=buffer

	def setProvider(self,id,name,url,maxFeeds):
		self.provider=Provider(id,name,url,maxFeeds)

	def fetchData(self):
		self.start()#llama al metodo run para traer los feeds desde el proveedor

	def run(self):
		#sincronizar el ingreso al buffer
		self.provider.cargaFeeds()#descarga las noticias de internet y carga en memoria
		news=self.provider.getNews()#obtiene el texto de una noticia
		self.emit(SIGNAL("updateNews(QString)"),news)#genera un evento que sera manejado en la ventana para actualizarla

	def __del__(self):
		print("ha finalizado")
		self.wait()

	def showData(self):
		self.provider.printFeedsList()

	def printInfo(self):
		print("url:" +self.provider.getUrl())


class Buffer():

	def __init__(self):
		self.data=Queue()
		self.access=True
		
	def enQueue(self,element):
		self.data.put(element)

	def deQueue(self):
		return self.data.get()

	def isEmpty(self):
		return self.data.empty()

def main():
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())	

if __name__ == '__main__':
	main()