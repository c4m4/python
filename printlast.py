#!/usr/bin/env python

import os

print open("/etc/passwd","r").readlines()[-1],

for i in os.environ.iteritems():
	if '/home/c0m0' in i[1]:
		print i[1]

