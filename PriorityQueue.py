from Queue import *

class Persona(object):
	"""docstring for Persona"""
	def __init__(self,edad):
		self.edad=edad		

	def printPerson(self):
		return str(self.edad)

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


if __name__ == '__main__':
	main()