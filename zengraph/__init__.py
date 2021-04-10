from zengraph.showapi import *
from zengraph.image_container import ImageContainer

import sys
from PyQt5.QtWidgets import QApplication

APP = QApplication.instance()
if APP is None:
    APP = QApplication([])

from zengraph.flowchart import *