from zengraph.showapi import *
from zengraph.image_container import ImageContainer

import sys
from PyQt5.QtWidgets import QApplication

APP = QApplication.instance()
if APP is None:
    APP = QApplication([])

# def start_crow_spin():
#	import pycrow
#	import zenframe.finisher

#	if udp_port and pycrow.get_gateway(12) is None:
#		create_udp_gate(12, udp_port)

#	if

#	pycrow.start_spin()
#	zenframe.finisher.register_destructor("pycrow", pycrow.stop_spin())
