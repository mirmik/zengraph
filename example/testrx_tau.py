#!/usr/bin/env python3
#coding: utf-8

from zengraph import flowplot, plot, show
import threading
from rxsignal import *

t = rxrange(0, 100) * 0.01
g = t.map(lambda a: 1)

B = numpy.array([0,1])
A = numpy.array([
	[0,1],
	[0.1,0.1]
])

out = dynsystem(g, A, B)

x = out.map(lambda a: a[1])

plot(t, x)
show()