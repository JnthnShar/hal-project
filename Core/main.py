#!/usr/bin/env python
# encoding: utf-8
"""
main.py

Created by Jonathan Sharer on 2008-11-21.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import arduino
import hald
import timed
import time
import httpd

if __name__ == '__main__':
	# setup and connect to the hardware
	print "Finding hardware..."
	myArduino = arduino.Arduino("/dev/tty.usbserial-A80081qe")
	
	# start the hal
	print "Starting HALD..."
	myhald = hald.hald()
	myhald.addArduino("A", myArduino)
	myArduino.writeLine("R00")
	
	# start web server
	print "Starting HTTPD..."
	myhttpd = httpd.httpd(myhald)
	myhttpd.start()
	
	# start timer
	print "Starting TIMED..."
	myTimer = timed.eventTimer(myhald)
	myTimer.start()	
	
	# The enviroment is now setup
	# Put code here now
	running = True
	print "Home Automation Terminal v0.1"
	while running:
		print "Main Menu"
		print "---------"
		print " 1. Set Module"
		print " 2. Read Module"
		print " 0. Exit"
		usrInput = sys.stdin.readline().rstrip()
		
		if usrInput == '1':
			print myhald.getModuleList()
			print "Enter module name"
			usrInput = sys.stdin.readline().rstrip()
			print "Enter module value"
			state = sys.stdin.readline().rstrip()
			if myhald.getModuleType(usrInput) == "S":
				myhald.setSwitch(usrInput, state)
		elif usrInput == '2':
			print myhald.getModuleList()
			print "Enter module name"
			usrInput = sys.stdin.readline().rstrip()
			if myhald.getModuleType(usrInput) == "S":
				print myhald.readSwitch(usrInput)
			elif myhald.getModuleType(usrInput) == "A":
				print myhald.readAnalog(usrInput)
		elif usrInput == '0':
			running = False
	#Stop the HTTP server
	myhttpd.stop()
	#Stop the timer to kill the app
	myTimer.stop()
	