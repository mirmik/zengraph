#!/usr/bin/env python3

from zengraph import *
import zengraph.crow_compat as crow_compat

from PyQt5.QtCore import QPointF
from PyQt5.QtChart import QScatterSeries

disp(crow_compat.flowchart_for_series("test/sinus1", 
	y_name=["x", "y", "z"], 
	x_name="time", 
	y_range=(-1.5,1.5),
	interval = 2
),1,1)

disp(crow_compat.flowchart_for_series("test/sinus2", 
	y_name=["x", "y", "z"], 
	x_name="time", 
	y_range=(-1.5,1.5),
	interval = 2
),2,1)

crow_compat.enable_crow_support()
show()
