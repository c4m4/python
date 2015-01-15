#!/usr/bin/env python

import csv

with open("/etc/passwd", "r") as r:
	reader = csv.reader(r, delimiter=":")
	wvalues = [ row for row in reader ]

with open("/tmp/mycsv.csv", "wb") as f:
	o = csv.writer(f)
	for i in xrange(len(wvalues)): 
		o.writerow(wvalues[i][0] + "\t" + wvalues[i][2])
	f.flush()
	f.close()

for row in csv.reader(open("/tmp/mycsv.csv", "r"), delimiter=','):
		print ''.join(row)

