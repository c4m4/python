#!/usr/bin/env python

N = [1, [2, 3], [4, 5, 6]]
Len = N.__len__()
l = 0

Total = list()

while l < Len:
	if type(N[l]) is list: 
		print type(N[l])
		for i in N[l]:
			Total.append(i) 
	else:
		Total.append(N[l])
	l = l + 1

print Total
