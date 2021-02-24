import sys
import os
import time
import signal
import json

from PyQt5 import QtCore, QtGui, QtWidgets, QtOpenGL

from zenframe.mainwindow import ZenFrame
from zenframe.util import print_to_stderr

import zengraph.settings

class MainWindow(ZenFrame):
    def __init__(self,
                 title="zengraph",
                 initial_communicator=None,
                 restore_gui=True
                 ):

        super().__init__(
            title=title,
            application_name = "zengraph",
            initial_communicator=initial_communicator,
            restore_gui=restore_gui)


