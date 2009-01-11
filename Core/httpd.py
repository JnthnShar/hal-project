#!/usr/bin/env python
# encoding: utf-8
"""
main.py

Created by Jonathan Sharer on 2008-11-21.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import web
import hald
from threading import Thread

urls = ('/', 'index', '/switchOn/(\S*)', 'switchOn', '/switchOff/(\S*)', 'switchOff')
app = web.application(urls, globals())
running = False
hald = hald.hald()
IP = "10.0.0.1"

class httpd(Thread):
	def __init__(self, myhald):
		self.hald = myhald
		self.running = True
		Thread.__init__(self)
		
	def stop(self):
		self.running = False

	def run(self):
		app.run()
	
	def stop(self):
		raise SystemExit()
				
class index:
    def GET(self):
        return "<h1><a href=\"http://10.0.0.1:8080/switchOn/cfan\">ON</a> <a href=\"http://10.0.0.1:8080/switchOff/cfan\">OFF</a> <br><a href=\"http://10.0.0.1:8080/switchOn/sfan\">ON</a> <a href=\"http://10.0.0.1:8080/switchOff/sfan\">OFF</a></h1>"

class switchOn:
	def GET(self, id):
		hald.setSwitch(id, 1)
		return "<script type=\"text/javascript\">window.location = \"http://10.0.0.1:8080/\"</script>"
		

class switchOff:
	def GET(self, id):
		hald.setSwitch(id, 0)
		return "<script type=\"text/javascript\">window.location = \"http://10.0.0.1:8080/\"</script>"
		

#if __name__ == '__main__':
	#app.run()