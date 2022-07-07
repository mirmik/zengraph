#!/usr/bin/env python3
#coding: utf-8

from zengraph import flowplot, plot, show
import threading
from rxsignal import *

t = range(0, 100) * 0.01
g = t.map(lambda x: 1) 
s1 = aperiodic_filter(g, 0.1, 0.01)
s2 = aperiodic_filter(g, 0.2, 0.01)
s3 = aperiodic_filter(g, 0.3, 0.01)

plot(t, s1, s2, s3)
show()