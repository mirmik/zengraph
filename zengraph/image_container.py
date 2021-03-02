#!/usr/bin/env python3
#coding: utf-8

from zengraph import *
from PyQt5 import QtWidgets, QtCore, QtGui

class ImageContainer(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()

    def set_image(self):
        img = QtGui.QImage()
        img.loadFromData(r.content)
        img = img.scaled(self.size())
        self.setPixmap(QtGui.QPixmap.fromImage(img))