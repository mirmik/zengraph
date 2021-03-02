#!/usr/bin/env python3
#coding: utf-8

import threading
import requests
import time
from zengraph import *
from PyQt5 import QtWidgets, QtCore, QtGui

href = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/OrteliusWorldMap.jpeg/800px-OrteliusWorldMap.jpeg"
r = requests.get(href, stream=True)

class ImageContainer(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()

    def set_image(self):
        img = QtGui.QImage()
        img.loadFromData(r.content)
        img = img.scaled(self.size())
        self.setPixmap(QtGui.QPixmap.fromImage(img))

img = ImageContainer()
img.set_image()

disp(img,1,1)

def animate():
	while True:
		img.set_image()
		time.sleep(0.1)

thr = threading.Thread(target=animate)
thr.start()

show()
