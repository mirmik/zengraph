from zengraph.showapi import *
from zengraph.image_container import ImageContainer

import sys
from PyQt5.QtWidgets import QApplication
import reactivex as rx
from reactivex import operators as ops
from reactivex import Observable
import math
import operator

APP = QApplication.instance()
if APP is None:
    APP = QApplication([])

from zengraph.flowchart import *

class observable:
    def __init__(self, o):
        self.o = o

    def map(self, foo):
        return observable(self.o.pipe(ops.map(foo)))

    def zip(self, oth):
        return observable(rx.zip(self.o, oth.o))        

    def subscribe(self, *args, **kwargs):
        self.o.subscribe(*args, **kwargs)

    def take(self, count):
        return observable(self.o.pipe(ops.take(count)))

    def op(self, p, arg):
        if isinstance(arg, observable):
            z = self.zip(arg)
            return z.map(lambda x: p(x[0], x[1]))

        return self.map(lambda x: p(x, arg))

    def add(self, arg):
        return self.op(operator.add, arg)
    def sub(self, arg):
        return self.op(operator.sub, arg)
    def mul(self, arg):
        return self.op(operator.mul, arg)
    def div(self, arg):
        return self.op(operator.truediv, arg)
    def sin(self):
        return self.map(lambda x: math.sin(x))
    def cos(self):
        return self.map(lambda x: math.cos(x))

    def __add__(self, oth):
        return self.add(oth)
    def __sub__(self, oth):
        return self.sub(oth)
    def __mul__(self, oth):
        return self.mul(oth)
    def __truediv__(self, oth):
        return self.div(oth)

class subject(observable):
    def __init__(self, o):
        super().__init__(o)

    def on_next(self, val):
        self.o.on_next(val)

def interval(d):
    return observable(rx.interval(d))

def range(s,f):
    return observable(rx.range(s,f))