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

urls = ('/', 'index')
app = web.application(urls, globals())

class index:
    def GET(self):
        return "Hello, world!"

if __name__ == '__main__':
	app.run()