#!/usr/bin/env python3

from PyQt5 import QtWidgets, QtCore, QtGui
import sys


class Axis:
    def __init__(self, min, max):
        self.set_minmax(min, max)

    def set_minmax(self, min, max):
        self.min = min
        self.max = max


class Chart2d:
    def __init__(self, x_axis=None, y_axis=None):
        if x_axis is None:
            x_axis = Axis(0, 20)

        if y_axis is None:
            y_axis = Axis(0, 10)

        self.set_axes(x_axis, y_axis)
        self.set_series([0, 10, 20], [10, 0, 10])

    def set_axes(self, xaxis, yaxis):
        self.xaxis = xaxis
        self.yaxis = yaxis

    def set_series(self, xdata, ydata):
        self.xdata = xdata
        self.ydata = ydata

    def prepare_xdata(self, area):
        lo = self.xaxis.min
        hi = self.xaxis.max
        interval = hi - lo

        ret = []
        for x in self.xdata:
            ret.append(((x - lo) / interval) * area)

        return ret

    def prepare_ydata(self, area):
        lo = self.yaxis.min
        hi = self.yaxis.max
        interval = hi - lo

        ret = []
        for y in self.ydata:
            ret.append(((y - lo) / interval) * area)

        return ret

    def points(self):
        return len(self.xdata)


class Plot2d(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.charts = []

        self.attach_chart(Chart2d())

    def attach_chart(self, chart):
        self.charts.append(chart)

    def paintEvent(self, ev):
        print("paintEvent")

        painter = QtGui.QPainter(self)

        for chart in self.charts:
            xdata = chart.prepare_xdata(self.width())
            ydata = chart.prepare_ydata(self.height())
            for i in range(chart.points() - 1):
                print("HERE")
                painter.drawLine(
                    QtCore.QPointF(xdata[i],   ydata[i]),
                    QtCore.QPointF(xdata[i+1], ydata[i+1]))

        painter.end()


if __name__ == "__main__":
    QAPP = QtWidgets.QApplication(sys.argv[1:])

    plt = Plot2d()

    plt.show()

    QAPP.exec()
