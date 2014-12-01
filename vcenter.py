#!/usr/bin/python

name = raw_input("Enter the VM name to search:")

import sys, time

try:
        from pysphere import VIServer
	def descon(vc):
		if server.is_connected() == True:
			print "Disconnecting from " + str(vc)
			server.disconnect()
		else:
			print "cannot to vc " + i
except ImportError:
        print "try to install pysphere module"
        sys.exit(1)

vcenters = [ ]

for i in vcenters:
        try:
                try:
                        server = VIServer()
                        server.connect(i, "SDA\user01", "password")
			if server.is_connected() == True:
                        	vm = server.get_vm_by_name(name.upper())
                        	if vm is not None:
                                	print "Found " + name.upper() + " on " + i
					#descon(i)
				#	break
                except:
			descon(i)
                        pass
        except:
                pass
