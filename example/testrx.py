#!/usr/bin/env python3
#coding: utf-8

from zengraph import flowplot, plot, show
from rxsignal import *

T = 0.3
T2 = 0.4
R = 0.02
z = rxinterval(R)
t = z*R
s = (t/T).sin()
c = (t/T).cos()
c2 = (t/T2).cos()

flowplot(t, s, c, position=(1,1,1,1),interval=5)
flowplot(t, c, position=(2,1,1,1),interval=5)
flowplot(t, s*c2, position=(3,1,1,2),interval=5)
plot(t*c, t*s, position=(1,2,2,1))

show()
