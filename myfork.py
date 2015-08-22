#!/usr/bin/env python


import os
from time import *

print os.getpid()

try:
	child = os.fork()
	if child != None:
		print os.getpid()
		f = open("/etc/passwd", "r")
		sleep(120)
except:
	print "you have an error"
	exit()
