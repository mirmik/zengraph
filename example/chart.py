#!/usr/bin/env python3

from zengraph import *

from PyQt5.QtChart import QLineSeries, QChart, QChartView, QValueAxis, QCategoryAxis, QSplineSeries
from PyQt5.QtCore import QPoint, QPointF
from PyQt5.QtGui import QPainter, QPen, QBrush

import PyQt5.QtCore

from zengraph.realtime_series import FlowSeries, FlowChart
from zenframe.animate import AnimateThread

import math
import pycrow
import numpy
import threading
import time
pycrow.create_udpgate(12, 0)


i = 0
prefix = 0

ltime = 0


def incom(pack):
    global i, xmin, xmax, prefix, ltime
    return

    if time.time() - ltime < 0.01:
        return

    data = pack.message()

    arr = numpy.frombuffer(data, dtype=numpy.float64)

    series.append(QPointF(arr[0], math.sin(time.time())*5 + 10))

    ltime = time.time()


address = pycrow.address(".12.127.0.0.1:10009")
subscriber = pycrow.subscriber(incom)
subscriber.subscribe(address, "bimanip/manip1", 2, 50, 0, 50)


chart = FlowChart()
series0 = chart.add_xyseries(maxinterval=1)
series1 = chart.add_xyseries(maxinterval=1)

chart.setTitle("Multiaxis chart example")

chartview = QChartView(chart)
chartview.setRenderHint(QPainter.Antialiasing)


# series.remove(0)
# axisX.attach(series)


# pycrow.start_spin()
# pycrow.join_spin()
# exit(0)

stime = None


def lalala():
    global stime
    if not stime:
        stime = time.time()

    series0.append(QPointF(time.time() - stime,
                           math.sin(time.time()*10)*10+10))
    series1.append(QPointF(time.time() - stime,
                           math.cos(time.time()*10)*10+10))

    chart.update()


AnimateThread(lalala, 0.01).start()

disp(chartview, 1, 1)
show(onclose=[pycrow.stop_spin])
