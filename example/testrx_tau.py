#!/usr/bin/env python3
#coding: utf-8

from zengraph import flowplot, plot, show
import threading
from rxsignal import *

t = rxrange(0, 100) * 0.01
g = t.map(lambda x: 1) 
s = [aperiodic_filter(g, 0.05*i, 0.01) for i in range(1, 40)]

plot(t, *s)
show()