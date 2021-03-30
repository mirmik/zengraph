from PyQt5 import QtWidgets, QtCore, QtGui
import requests

class ImageContainer(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()

    def set_image(self, img):
        self.setPixmap(QtGui.QPixmap.fromImage(img))

class MapImage(ImageContainer):
    def __init__(self):
        super().__init__()
        href = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/OrteliusWorldMap.jpeg/800px-OrteliusWorldMap.jpeg"
        r = requests.get(href, stream=True)
    
        img = QtGui.QImage()
        img.loadFromData(r.content)
        img = img.scaled(self.size())
    
        self.set_image(img)