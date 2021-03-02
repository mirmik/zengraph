#!/usr/bin/env python3
#coding: utf-8

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from PyQt5 import QtCore, QtWidgets
from zengraph import *
from PyQt5.QtWidgets import QLabel

import matplotlib
matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


sc = MplCanvas(None, width=5, height=4, dpi=100)
sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 10])

sc2 = MplCanvas(None, width=5, height=4, dpi=100)
sc2.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])

disp(sc, 1, 1)
disp(sc2, 2, 1)

show()
