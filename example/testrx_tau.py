#!/usr/bin/env python3
#coding: utf-8

from zengraph import flowplot, plot, show
import threading
from rxsignal import *

t = range(0, 100) * 0.01
g = t.map(lambda x: 1) 
s = [aperiodic_filter(g, 0.1*i, 0.01) for i in range(10)]

plot(t, *s)
show()