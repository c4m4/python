#!/usr/bin/env python

import os, time

with open("passwd","w") as f:
        #os.lseek(f.fileno(),os.SEEK_END, 0)
	f.seek(0)
        for x in xrange(1,1000):
                f.write("hello world \n" + time.ctime() + "\n")
                f.flush()
                time.sleep(2)
