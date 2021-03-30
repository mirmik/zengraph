from PyQt5 import QtWidgets, QtCore, QtGui
import math

class StatusWidget(QtWidgets.QWidget):
	class Record:
		def __init__(self, state):
			self.state = state

	def __init__(self, fields, cols=8, maxheight = 50, maxwidth = 100):
		super().__init__()
		self.maxheight = maxheight
		self.maxwidth = maxwidth
		self.fwidth = cols
		self.fields = { k : self.Record(False) for k in fields }
		self.state = False

		self.fheight = math.ceil(len(fields) / self.fwidth)

	def set_status(self, name, state):
		self.fields[name].state = state

	def paintEvent(self, ev):
		painter = QtGui.QPainter(self)
		painter.setFont(QtGui.QFont("Ubuntu Mono", 13))

		ceil_width = self.width() / self.fwidth - 5
		ceil_height = self.height() / self.fheight - 5

		if (ceil_height > self.maxheight) : ceil_height = self.maxheight
		if (ceil_width > self.maxwidth) : ceil_width = self.maxwidth

		col = 0
		row = 0
		for k, v in self.fields.items():
			if v.state:
				painter.setBrush(QtGui.QColor(0,255,0))
			else:
				painter.setBrush(QtGui.QColor(255,0,0))
			
			rect = QtCore.QRectF(ceil_width*col, ceil_height*row, ceil_width, ceil_height)
			painter.drawRect(rect)
			painter.drawText(rect, QtCore.Qt.AlignCenter, k)

			col+=1
			if col == self.fwidth:
				col = 0
				row += 1

		painter.end()

