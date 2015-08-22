#!/usr/bin/env python

import dis

def myfunc(wid="Emmanuel", name="silvia"):
	print locals()['wid']

dis.dis(myfunc)

myfunc()
