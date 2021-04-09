#!/usr/bin/env python3

from PyQt5.QtChart import QLineSeries, QChart, QChartView, QValueAxis, QCategoryAxis, QSplineSeries
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtCore import QPoint
import PyQt5.QtCore

import sys


class FlowSeries:
    def __init__(self, maxinterval, maxpoints=5000, type=QLineSeries):
        self.maxpoints = maxpoints
        self.maxinterval = maxinterval

        self.data = []

        self.series = type()
        self.series.setUseOpenGL(True)
        self.series.append(self.data)

    def attachAxes(self, x, y):
        self.series.attachAxis(x)
        self.series.attachAxis(y)

    def append(self, point):
        self.data.append(point)

        while len(self.data) > self.maxpoints or self.data[-1].x() - self.data[0].x() > self.maxinterval:
            del self.data[0]

    def range(self):
        if len(self.data) == 0:
            return 0, 0

        first_x = self.data[0].x()
        last_x = self.data[-1].x()
        return first_x, last_x

    def replace(self):
        self.series.replace(self.data)


class FlowChart(QChart):
    def __init__(self):
        super().__init__()
        self.series_list = []

        self.axisX = QValueAxis()
        self.axisY = QValueAxis()

        self.axisPen = QPen(PyQt5.QtCore.Qt.red)
        self.axisPen.setWidth(4)
        self.axisX.setLinePen(self.axisPen)

        self.axixBrush = QBrush(PyQt5.QtCore.Qt.green)
        self.axisX.setLabelsBrush(self.axixBrush)
        self.axisX.setGridLineVisible(True)

        self.axisY.setRange(0, 28)

        self.setAxisX(self.axisX)
        self.setAxisY(self.axisY)

    def add_xyseries(self, maxinterval, maxpoints=5000, type=QLineSeries):
        series = FlowSeries(
            maxinterval=maxinterval, maxpoints=maxpoints, type=type)
        self.addSeries(series.series)
        series.attachAxes(self.axisX, self.axisY)
        self.series_list.append(series)
        return series

    def update(self):
        xmin = None
        xmax = None

        for s in self.series_list:
            r = s.range()
            if xmin is None or xmin > r[0]:
                xmin = r[0]
            if xmax is None or xmax < r[1]:
                xmax = r[1]

        self.axisX.setRange(xmin, xmax)

        for s in self.series_list:
            s.replace()
