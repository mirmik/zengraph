#!/usr/bin/env python3

from PyQt5 import QtWidgets, QtCore, QtGui, QtChart

import pycrow
import json
import zenframe.finisher
import zenframe.util
from zengraph.flowchart import FlowChart, StaticChart
import time

from zenframe.util import print_to_stderr

subscribers = []

def bind_series(theme, x_name, y_name, y_series, timestamp="time", chart=None, format="json"):
	last_update = 0
	def handle(pack):
		nonlocal last_update

		msg = pack.message().decode("utf-8")
		dct = json.loads(msg)

		x = dct[x_name]

		for k, v in dct.items():
			try:
				idx = y_name.index(k)
			except:
				continue

			y_series[idx].append(QtCore.QPointF(x, v), timestamp=dct[timestamp])


		if chart:
			curtime = time.time()
			if curtime - last_update > 0.025:
				chart.update()
				last_update = curtime
	
	sub = pycrow.subscriber(handle)
	subscribers.append(sub)

	sub.subscribe(pycrow.crowker_address(), theme, ack=2, ackquant=50, rack=0, rackquant=0)

def flowchart_for_series(theme, x_name, y_name, y_range, timestamp="time", interval=5):
	chart = FlowChart()
	series = [ chart.add_xyseries(maxinterval=interval, type=QtChart.QLineSeries) for i in range(len(y_name)) ]
	
	chart.set_yrange(*y_range)
	chartview = QtChart.QChartView(chart)
	chartview.setRenderHint(QtGui.QPainter.Antialiasing)

	bind_series(format="json", theme=theme, timestamp=timestamp,
	    y_name=y_name, y_series=series, x_name=x_name, chart = chart)

	return chartview


def plane_chart(theme, x_name, y_name, x_range, y_range, timestamp="time"):	
	chart = StaticChart()
	series0 = chart.add_xyseries()
	chart.set_xrange(*x_range)
	chart.set_yrange(*y_range)

	chartview = QtChart.QChartView(chart)
	chartview.setRenderHint(QtGui.QPainter.Antialiasing)

	bind_series(format="json", theme=theme, timestamp=timestamp,
	    y_name=[y_name], y_series=[series0], x_name=x_name, chart = chart)

	return chartview

def enable_crow_support():
	pycrow.create_udpgate()	
	pycrow.start_spin()

	zenframe.finisher.register_destructor(None, lambda: pycrow.stop_spin)
