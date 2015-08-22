#!/usr/bin/env python

import os

for i in os.walk("."):
    print i
    for x in i:
        print x
