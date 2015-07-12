from datetime import *
from PyQt4 import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class Time():

	def getCurrentTime(self):
		now=datetime.now()
		hour=now.hour
		minute=now.minute
		second=now.second
		totalTime=hour*3600+minute*60+second
		return totalTime

class ClockThread(QThread):

	def __init__(self,time,maxTime,parent=None):
		QThread.__init__(self, parent)
		self.startTime=time
		self.maxTime=maxTime
		self.clock=Time()

	def run(self):
		while True:
			currentTime=self.clock.getCurrentTime()
			elapse=currentTime-self.startTime
			if elapse>self.maxTime:
				self.emit(SIGNAL("timeOver()"))
				break

	def setStartTime(self,startTime):
		self.startTime=startTime

	def __del__(self):
		print("Clock Thread have ended!")
		self.wait()