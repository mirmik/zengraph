#!/usr/bin/env python3

from PyQt5.QtChart import QLineSeries, QChart, QChartView, QValueAxis, QCategoryAxis, QSplineSeries
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtCore import QPoint
import PyQt5.QtCore


class FlowSeries:
    def __init__(self, maxpoints, maxinterval, chart):
        self.maxpoints = maxpoints
        self.maxinterval = maxinterval
        self.first_x = 0
        self.last_x = 0

        self.data = []

        self.series = QLineSeries()
        self.series.setUseOpenGL(True)
        self.series.append(self.data)

        self.axisX = QValueAxis()
        self.axisY = QValueAxis()

        self.axisPen = QPen(PyQt5.QtCore.Qt.red)
        self.axisPen.setWidth(4)
        self.axisX.setLinePen(self.axisPen)

        self.axixBrush = QBrush(PyQt5.QtCore.Qt.green)
        self.axisX.setLabelsBrush(self.axixBrush)
        self.axisX.setGridLineVisible(True)

        chart.addSeries(self.series)
        chart.setAxisX(self.axisX)
        chart.setAxisY(self.axisY)

        self.series.attachAxis(self.axisX)
        self.series.attachAxis(self.axisY)

        self.axisY.setRange(0, 20)

    def append(self, point):
        count = self.series.count()
        self.data.append(point)

        if len(self.data) > self.maxpoints:
            del self.data[0]

        self.first_x = self.data[0].x()
        self.last_x = self.data[-1].x()

        self.series.replace(self.data)
        self.axisX.setRange(*self.range())

    def range(self):
        return self.first_x, self.last_x
