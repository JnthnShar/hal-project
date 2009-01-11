#!/usr/bin/env python
# encoding: utf-8
"""
eventtimer.py

Created by Jonathan Sharer on 2008-11-24.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from threading import Thread
import time

class eventTimer(Thread):
	TIMER_DELAY = 1
	eventTime = ["23:11", "23:12"]
	eventModule = ["11", "11"]
	eventCommand = ["1", "0"]
	
	def __init__ (self, newHald):
		self.hald = newHald
		self.running = True
		Thread.__init__(self)
	
	def run(self):
		while self.running:			
			currentTime = time.localtime()
			year = currentTime[0]
			month = currentTime[1]
			day = currentTime[2]
			hour = currentTime[3]
			minuites = currentTime[4]
			seconds = currentTime[5]
			dayOfWeek = currentTime[6]
			dayOfYear = currentTime[7]
			daylightSavings = currentTime[8]
			
			if minuites < 10:
				minuites = "0" + str(minuites)
			currentTime = str(hour) + ":" + str(minuites)
			
			# causes timer to execute at the top of the minuite
			if seconds == 0:
				self.TIMER_DELAY = 1	#set this back to 60 when done debugging!
			
			for i in range(len(self.eventTime)):
				if self.eventTime[i] == currentTime:
					if self.hald.getModuleType(self.eventModule[i]) == "S":
						self.hald.setSwitch(self.eventModule[i], self.eventCommand[i])
					
			time.sleep(self.TIMER_DELAY)
	
	def addEvent(self,eventTime,moduleName,moduleValue):
		print "added event"
		self.eventTime.append(eventTime)
		self.eventModule.append(moduleName)
		self.eventCommand.append(moduleValue)
	
	def stop(self):
		self.running = False

if __name__ == '__main__':
	main()