from PyQt5 import QtWidgets, QtCore, QtGui


class DisplayWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self._inited1 = False

        pal = self.palette()
        pal.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setAutoFillBackground(True)
        self.setPalette(pal)
        self.layout = QtWidgets.QGridLayout()
        self.layout.setSpacing(1)
        self.layout.setContentsMargins(1, 1, 1, 1)
        self.setLayout(self.layout)

    def add(self, wdg, row, col, rowSpan=1, colSpan=1):
        self.layout.addWidget(wdg, row, col, rowSpan, colSpan)

    def message_handler(self, data):
        print(data)
        if data["cmd"] == "resize":
            self.resize(*data["size"])


    def paintEvent(self, event):
        if not self._inited1:

            QtGui.QWindow.fromWinId(self.winId()).setFlags(
                QtGui.QWindow.fromWinId(self.winId()).flags() |
                QtCore.Qt.SubWindow)

            self._inited1 = True


DISPLAY = None


def instance():
    global DISPLAY
    if DISPLAY is None:
        DISPLAY = DisplayWidget()
    return DISPLAY
