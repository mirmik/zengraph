#!/usr/bin/env python3

from zengraph import *

from PyQt5.QtChart import QLineSeries, QChart, QChartView, QValueAxis, QCategoryAxis, QSplineSeries
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QPen, QBrush

import PyQt5.QtCore

series = QLineSeries()

data = [
    QPoint(0, 6),
    QPoint(9, 4),
    QPoint(15, 20),
    QPoint(18, 12),
    QPoint(28, 25)
]

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

series.remove(0)
# axisX.attach(series)

disp(chartview, 1, 1)
show()
