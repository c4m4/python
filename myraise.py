#!/usr/bin/env python

def print(self):
	print "i am an intruder"

class Error(Exception):
	print "i am emmanuel"
	exit()
def myfoo():
	print "Hello world"

try:
	open("/etc/booooo") 
except:
	raise Error
