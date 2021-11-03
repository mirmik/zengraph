#!/usr/bin/env python3

import zengraph.crow_compat as crow_compat
import time
import math
import pycrow
import json

import sys

theme = sys.argv[1]
mul = float(sys.argv[2])

crow_compat.enable_crow_support()

start_time = time.time()
while 1:
	dct = { 
		"x" : math.sin(time.time()*mul), 
		"y" : math.sin(time.time()*mul+0.333333333),
		"z" : math.sin(time.time()*mul+0.666666666),
		"time" : time.time() - start_time
	}	
	pycrow.publish(pycrow.crowker_address(), theme, json.dumps(dct), ack=0, ackquant=0)
	print(dct)
	time.sleep(0.02)