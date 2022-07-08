#!/usr/bin/env python3

from PyQt5.QtChart import (
    QChart, QChartView, QValueAxis, QCategoryAxis, 
    QLineSeries, QSplineSeries
)
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtCore import QPoint, QPointF
import PyQt5.QtCore

import sys
from zengraph.showapi import disp
import reactivex as rx
from reactivex import operators as ops
import rxsignal


class FlowSeries:
    def __init__(self, maxinterval, maxpoints=5000, type=QLineSeries):
        self.maxpoints = maxpoints
        self.maxinterval = maxinterval

        self.data = []
        self.ymin = 0
        self.ymax = 0

        self.series = type()
        self.series.setUseOpenGL(True)
        self.series.append(self.data)

        self.last_timestamp = 0

    def attachAxes(self, x, y):
        self.series.attachAxis(x)
        self.series.attachAxis(y)

    def append(self, point, timestamp):
        if len(self.data) != 0 and timestamp < self.last_timestamp:
            self.data.clear()

        self.data.append(point)

        if self.maxinterval != -1:
            while len(self.data) > self.maxpoints or self.data[-1].x() - self.data[0].x() > self.maxinterval:
                del self.data[0]

        else:
            while len(self.data) > self.maxpoints:
                del self.data[0]

        if point.y() < self.ymin:
            self.ymin = point.y()
        if point.y() > self.ymax:
            self.ymax = point.y()

        self.last_timestamp = timestamp

    def append_xy(self, point):
        self.data.append(point)

        if point.y() < self.ymin:
            self.ymin = point.y()
        if point.y() > self.ymax:
            self.ymax = point.y()

        if self.maxinterval != -1:
            while len(self.data) > self.maxpoints or self.data[-1].x() - self.data[0].x() > self.maxinterval:
                del self.data[0]

        else:
            while len(self.data) > self.maxpoints:
                del self.data[0]

    def xrange(self):
        if len(self.data) == 0:
            return 0, 0

        first_x = self.data[0].x()
        last_x = self.data[-1].x()
        return first_x, last_x

    def yrange(self):
        return self.ymin, self.ymax

    def replace(self):
        self.series.replace(self.data)


class FlowChart(QChart):
    def __init__(self, yautoscale=True):
        super().__init__()
        self.series_list = []

        self.ymin = 0
        self.ymax = 0
        self.yautoscale = yautoscale

        self.axisX = QValueAxis()
        self.axisY = QValueAxis()

        self.axisPen = QPen(PyQt5.QtCore.Qt.red)
        self.axisPen.setWidth(4)
        self.axisX.setLinePen(self.axisPen)
        self.axisY.setLinePen(self.axisPen)

        self.axixBrush = QBrush(PyQt5.QtCore.Qt.green)
        self.axisX.setLabelsBrush(self.axixBrush)
        self.axisX.setGridLineVisible(True)
        self.axisY.setLabelsBrush(self.axixBrush)
        self.axisY.setGridLineVisible(True)

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
        
    def set_yrange(self, ymin, ymax):
        self.axisY.setRange(ymin, ymax)

    def update(self):
        xmin = None
        xmax = None
        ymin = None
        ymax = None

        for s in self.series_list:
            r = s.xrange()
            if xmin is None or xmin > r[0]:
                xmin = r[0]
            if xmax is None or xmax < r[1]:
                xmax = r[1]

        for s in self.series_list:
            r = s.yrange()
            if ymin is None or ymin > r[0]:
                ymin = r[0]
            if ymax is None or ymax < r[1]:
                ymax = r[1]

        self.axisX.setRange(xmin, xmax)
        self.axisY.setRange(ymin, ymax)

        for s in self.series_list:
            s.replace()

LineSeries = QLineSeries
SplineSeries = QSplineSeries

class StaticSeries(QLineSeries):
    def __init__(self):
        super().__init__()
        self.setUseOpenGL(True)
        self.last_time_coord = 0

    def append(self, point, timestamp):
        if timestamp < self.last_time_coord:
            self.clear()

        super().append(point)
        self.last_time_coord = timestamp

    def append_xy(self, point):
        super().append(point)
        
    def series(self):
        return self


class StaticChart(QChart):
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

    def add_xyseries(self, type=StaticSeries):
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


def create_chart(xobservable, *yobservable, position=(1,1,1,1)):
    yobservable2 = []    
    if isinstance(xobservable, rxsignal.observable.observable):
        xobservable = xobservable.o
    for i in range(len(yobservable)):
        if isinstance(yobservable[i], rxsignal.observable.observable):
            yobservable2.append(yobservable[i].o)

    serieses = []
    l = len(yobservable)

    def update(x):
        for i in range(l):
            serieses[i].append_xy(QPointF(x[0], x[1+i]))
        chart.autoscale()

    chart = StaticChart()
    for y in yobservable:
        serieses.append(chart.add_xyseries())
    view = ChartView(chart)

    a = rx.zip(xobservable, *yobservable)
    a.subscribe(update)
    chart.autoscale()

    disp(view, *position)

def create_flowchart(xobservable, *yobservable, position=(1,1,1,1), interval=100):
    yobservable2 = []    
    if isinstance(xobservable, rxsignal.observable):
        xobservable = xobservable.o
    for i in range(len(yobservable)):
        if isinstance(yobservable[i], rxsignal.observable):
            yobservable2.append(yobservable[i].o)

    serieses = []
    l = len(yobservable)
        
    def update(x):
        for i in range(l):
            serieses[i].append_xy(QPointF(x[0], x[1+i]))
        chart.update()

    chart = FlowChart()
    for y in yobservable:
        serieses.append(chart.add_xyseries(maxinterval=interval))
    view = ChartView(chart)
    chart.set_yrange(-1,1)

    a = rx.zip(xobservable, *yobservable2)
    a.subscribe(update)

    disp(view, *position)

def plot(*args, **kwargs):
    return create_chart(*args, **kwargs)

def flowplot(*args, **kwargs):
    return create_flowchart(*args, **kwargs)