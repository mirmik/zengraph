#!/usr/bin/env python3

from zengraph import *

from PyQt5.QtChart import QLineSeries, QChart, QChartView, QValueAxis, QCategoryAxis, QSplineSeries
from PyQt5.QtCore import QPoint, QPointF
from PyQt5.QtGui import QPainter, QPen, QBrush

import PyQt5.QtCore

from zengraph.realtime_series import FlowSeries

import math
import pycrow
import numpy
import time
pycrow.create_udpgate(12, 0)

xmin = None
xmax = None
ymin = None
ymax = None

i = 0
prefix = 0

ltime = 0


def incom(pack):
    global i, xmin, xmax, prefix, ltime
    if time.time() - ltime < 0.01:
        return

    data = pack.message()

    arr = numpy.frombuffer(data, dtype=numpy.float64)

    series.append(QPointF(arr[0], math.sin(time.time())*10 + 10))

    ltime = time.time()


address = pycrow.address(".12.127.0.0.1:10009")
subscriber = pycrow.subscriber(incom)
subscriber.subscribe(address, "bimanip/manip1", 2, 50, 0, 50)


chart = QChart()
series = FlowSeries(100, 100000, chart)
chart.setTitle("Multiaxis chart example")

chartview = QChartView(chart)
chartview.setRenderHint(QPainter.Antialiasing)


# series.remove(0)
# axisX.attach(series)


pycrow.start_spin()
# pycrow.join_spin()
# exit(0)


disp(chartview, 1, 1)
show(onclose=[pycrow.stop_spin])
