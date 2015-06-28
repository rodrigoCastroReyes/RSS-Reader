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
		self.condition=QWaitCondition()
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
			thread=ProducerThread(self.mutex,self.condition,self.buffer)
			thread.setProvider(id,name,url,maxFeeds)
			self.threads.append(thread)
		self.consumerThread=ConsumerThread(self.mutex,self.condition,self.buffer)

	def startToWork(self):
		self.consumerThread.readData()
		for thread in self.threads:
			thread.fetchData()
		print("Pool threads is working!")

	def getConsumerThread(self):
		return self.consumerThread

	def printBuffer(self):
		self.buffer.printData()


class ProducerThread(QThread):

	def __init__(self,mutex,condition,buffer,parent = None):
		QThread.__init__(self, parent)
		self.provider=None
		self.buffer=buffer
		self.mutex=mutex
		self.condition=condition

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
			self.buffer.enQueue(feed)#ingresa un feed al buffer 
			self.condition.wakeOne()#informa al consumerthread que hay datos que consumir
			self.mutex.unlock()#desbloquea el mutex para que otros hilos puedan usar el buffer
		print("Thread "+ str(self.id) + "have ended")

	def __del__(self):
		print("Producer Thread have ended")
		self.wait()

	def showData(self):
		self.provider.printFeedsList()

class ConsumerThread(QThread):

	def __init__(self,mutex,condition,buffer,parent = None):
		QThread.__init__(self, parent)
		self.provider=None
		self.buffer=buffer
		self.mutex=mutex
		self.condition=condition

	def run(self):
		while True:
			if not(self.buffer.isEmpty()):
				self.mutex.lock()#accede al buffer para leer datos
				self.condition.wait(self.mutex)#espera hasta que un producer thread informe que hay noticia nueva
				self.mutex.unlock()

				self.mutex.lock()#accede al buffer para leer datos
				feed=self.buffer.deQueue()#saca un feed
				print("Nuevo feed")
				print(feed.getAlltoPrint())

				self.mutex.unlock()
				self.emit(SIGNAL("updateNews(QString)"),feed.getAlltoPrint())#genera un evento que sera manejado en la ventana para actualizarla
				#permite que el resto de hilos use el buffer

	def readData(self):
		self.start()

	def __del__(self):
		print("Consumer Thread have ended")
		self.wait()


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
		if self.isEmpty():
			print("No feeds")
		while not(self.isEmpty()):
			feed=self.deQueue()
			print(feed.getAlltoPrint())

