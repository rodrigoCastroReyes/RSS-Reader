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
		self.time=None#define el tiempo en el que los hilos deben volver a hacer una consulta
		self.filePath=filePath#directorio del archivo que tiene informacion sobre los hilos
		self.mutex=QMutex()
		self.condition=QWaitCondition()
		self.create()#crea el pool de threads
		
	def create(self):#leeer el archivo ubicado en filePath y crea los hilos en base a esa informacion
		with open(self.filePath, encoding='utf-8') as data_file:
			data = json.loads(data_file.read())
		self.time=int(data['time'])
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

	def getTime(self):
		return self.time

	def setTime(self,time):
		self.time=time

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
		if not(self.isRunning()):
			self.start()#llama al metodo run para traer los feeds desde el proveedor
		else:
			print("Producer Thread "+str(self.id) + "already is running")

	def run(self):
		#sincronizar el ingreso al buffer
		self.provider.cargaFeeds()#descarga las noticias de internet y carga en memoria
		for feed in self.provider.getFeeds():
			self.mutex.lock()#bloquea el mutex para guardar datos en el buffer
			self.buffer.enQueue(feed)#ingresa un feed al buffer 
			self.condition.wakeOne()#informa al consumerthread que hay datos que consumir
			self.mutex.unlock()#desbloquea el mutex para que otros hilos puedan usar el buffer
		print("Thread "+ str(self.id) + " have done your work!")

	def __del__(self):
		print("Producer Thread "+str(self.id) + " have ended!")
		self.wait()

	def showData(self):
		self.provider.printFeedsList()

class ConsumerThread(QThread):

	def __init__(self,mutex,condition,buffer,parent = None):
		QThread.__init__(self, parent)
		self.buffer=buffer
		self.mutex=mutex
		self.condition=condition

	def run(self):
		while True:
			#consumidor duerme cuando el buffer esta vacio
			self.mutex.lock()
			while(self.buffer.isEmpty()):#si el buffer esta vacio se debe esperar hasta que hayan datos
				self.condition.wait(self.mutex)#espera hasta que un producer thread informe que hay noticias nuevas
			self.mutex.unlock()
			self.mutex.lock()#accede al buffer para leer datos
			#se extraen todos los feeds del buffer
			while not(self.buffer.isEmpty()):#saca los feeds disponibles y los envia a la interfaz
				feed=self.buffer.deQueue()
				self.emit(SIGNAL("updateNews(PyQt_PyObject)"),feed)#genera un evento que sera manejado en la ventana para actualizarla
				#el evento almacena una referencia al feed que se acaba de extraer del buffer
			self.mutex.unlock()#permite que el resto de hilos use el buffer

	def readData(self):
		if not(self.isRunning()):#si el productor no esta corriendo, se ejecuta
			self.start()
		else:
			print("Thread Consumer already is running")

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

