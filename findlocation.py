#!/usr/bin/env python

import sys
try:
	import xlrd
except:
	print "you need to install xrld python module"
	exit()

wb=xlrd.open_workbook("/home/c0m0/winshare/repe/this/Server_report_so_location.xls")
sh = wb.sheet_by_index(0)
for rownum in range(sh.nrows):
    if sys.argv[1] in sh.row_values(rownum):
           print sh.row_values(rownum)
