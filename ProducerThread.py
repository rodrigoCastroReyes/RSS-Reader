import sys
import json
from PyQt4 import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from CargaRss import *
from queue import *


class PoolThreads():

	def __init__(self,filePath):
		self.threads=[]
		self.buffer=Buffer()#inicializa el buffer que guardara las noticias: coleccion compartida
		self.time=None#define el tiempo en el los hilos hacen la consulta
		self.filePath=filePath#directorio del archivo que tiene informacion sobre los hilos
		self.mutex=QMutex()
		self.create()#crea el pool de threads
		
	def create(self):#leeer el archivo ubicado en filePath y crea los hilos en base a esa informacion
		with open(self.filePath, encoding='utf-8') as data_file:
			data = json.loads(data_file.read())
		time=int(data['time'])
		listThread=data['threads']
		for dataThreads in listThread:
			id=dataThreads["id"]
			name=dataThreads["name"]
			url=dataThreads["url"]
			maxFeeds=int(dataThreads["maxFeeds"])
			thread=ProducerThread(self.mutex,self.buffer)
			thread.setProvider(id,name,url,maxFeeds)
			self.threads.append(thread)

	def startToWork(self):
		for thread in self.threads:
			thread.fetchData()
		print("Pool threads is working!")

	def printBuffer(self):
		self.buffer.printData()



class ProducerThread(QThread):

	def __init__(self,mutex,buffer,parent = None):
		QThread.__init__(self, parent)
		self.provider=None
		self.buffer=buffer
		self.mutex=mutex

	def setProvider(self,id,name,url,maxFeeds):
		self.id=id
		self.provider=Provider(id,name,url,maxFeeds)

	def fetchData(self):
		self.start()#llama al metodo run para traer los feeds desde el proveedor

	def run(self):
		#sincronizar el ingreso al buffer
		self.provider.cargaFeeds()#descarga las noticias de internet y carga en memoria
		for feed in self.provider.getFeeds():
			self.mutex.lock()#bloquea el mutex para guardar datos en el buffer
			self.buffer.enQueue(feed)
			self.mutex.unlock()#desbloquea el mutex para que otros hilos puedan usar el buffer
		print("Thread "+ str(self.id) + "have ended");
		#self.emit(SIGNAL("updateNews(QString)"),news)#genera un evento que sera manejado en la ventana para actualizarla

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

	def printData(self):
		while not(self.isEmpty()):
			feed=self.deQueue()
			print(feed.getAlltoPrint())

