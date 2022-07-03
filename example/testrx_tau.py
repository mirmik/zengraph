#!/usr/bin/env python3
#coding: utf-8

from zengraph import flowplot, plot, show, observable,subject
from zengraph import interval, range
import reactivex as rx
import threading

A = 0
B = True

xx = subject(rx.subject.Subject())

def sss():
	global B
	while True:
		if B:
			B=False
			xx.on_next(A)

T = 0.3
T2 = 0.4

R = 0.02

def f(a):
	global A, B
	A=a
	B=True

t = range(0,100)*R
e = t.map(lambda a: 1) - xx
s = xx + e*0.1
s.subscribe(f)

plot(t, xx)

thr = threading.Thread(target=sss)
thr.start()

show()