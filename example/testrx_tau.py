#!/usr/bin/env python3
#coding: utf-8

from zengraph import flowplot, plot, show
from rxsignal import *

step = 0.1
t = rxrange(0, 100) * step 
g = t.map(lambda a: 1)

A = numpy.array([
	[0, 1],
	[-1, -1]
])

B = numpy.array([
	[0],
	[-1]
])

I = numpy.array([
	[0],
	[0]
])

ds = DynamicSystem(g=g, A=A, B=B, step=step, init=I)

x = ds.out().map(lambda a: a[0])
v = ds.out().map(lambda a: a[1])

plot(t, x, v)
show()