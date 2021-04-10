#!/usr/bin/env python3

from PyQt5.QtChart import (
    QChart, QChartView, QValueAxis, QCategoryAxis, 
    QLineSeries, QSplineSeries
)
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

LineSeries = QLineSeries
SplineSeries = QSplineSeries

class Chart(QChart):
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

        self.setAxisX(self.axisX)
        self.setAxisY(self.axisY)

    def add_xyseries(self, type=LineSeries):
        series = type()
        self.addSeries(series)
        series.attachAxis(self.axisX)
        series.attachAxis(self.axisY)
        self.series_list.append(series)
        return series

    def set_xrange(self, xmin, xmax):
        self.axisX.setRange(xmin, xmax)

    def set_yrange(self, ymin, ymax):
        self.axisY.setRange(ymin, ymax)

    def autoscale(self):
        xmax = ymax = float("-inf")
        xmin = ymin = float("+inf")

        for s in self.series_list:
            points = s.pointsVector()

            for p in points:
                if p.x() < xmin: xmin = p.x() 
                if p.x() > xmax: xmax = p.x()
                if p.y() < ymin: ymin = p.y() 
                if p.y() > ymax: ymax = p.y()


        self.set_xrange(xmin, xmax)
        self.set_yrange(ymin, ymax)

ChartView = QChartView

#Chart = QChart