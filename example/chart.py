#!/usr/bin/env python3

from zengraph import *

from PyQt5.QtChart import QLineSeries, QChart, QChartView, QValueAxis, QCategoryAxis, QSplineSeries
from PyQt5.QtCore import QPoint, QPointF
from PyQt5.QtGui import QPainter, QPen, QBrush

import PyQt5.QtCore

import pycrow
import numpy
pycrow.create_udpgate(12, 0)

xmin = None
xmax = None
ymin = None
ymax = None

i = 0
prefix = 0


def incom(pack):
    global i, xmin, xmax, prefix
    data = pack.message()

    arr = numpy.frombuffer(data, dtype=numpy.float64)

    #series.append(arr[0], arr[1])

    if xmin is not None:
        if arr[0] < xmin:
            xmin = arr[0]
        if arr[0] > xmax:
            xmax = arr[0]
    else:
        xmin = arr[0]
        xmax = arr[0]

    i += 1
    if i == 100:
        i = 0

    if arr[0] - prefix > 100:
        prefix += 100
    series.replace(i, QPointF(arr[0] - prefix, 50))

    #axisX.setRange(0, 100)


address = pycrow.address(".12.127.0.0.1:10009")
subscriber = pycrow.subscriber(incom)
subscriber.subscribe(address, "bimanip/manip1", 2, 50, 0, 50)


series = QLineSeries()

data = [QPointF(i, i) for i in range(100)]
series.append(data)

chart = QChart()
axisX = QValueAxis()
# axisX.setTickCount(10)

axisPen = QPen(PyQt5.QtCore.Qt.red)
axisPen.setWidth(4)
axisX.setLinePen(axisPen)

axixBrush = QBrush(PyQt5.QtCore.Qt.green)
axisX.setLabelsBrush(axixBrush)
axisX.setGridLineVisible(True)

chart.legend().hide()
chart.addSeries(series)
chart.setAxisX(axisX, series)
chart.setTitle("Multiaxis chart example")

# axisX.setRange(0,28)

chartview = QChartView(chart)
chartview.setRenderHint(QPainter.Antialiasing)

# series.remove(0)
# axisX.attach(series)


pycrow.start_spin()
# pycrow.join_spin()
# exit(0)


disp(chartview, 1, 1)
show(onclose=[pycrow.stop_spin])
