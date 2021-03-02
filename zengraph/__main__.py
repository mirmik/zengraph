#!/usr/bin/env python3
# coding:utf-8

import os
import sys
import time

import psutil
import traceback
import runpy
import signal

from zenframe.util import print_to_stderr, create_temporary_file
import zenframe.starter as frame
import zenframe.argparse

from PyQt5 import QtWidgets

from zenframe.configuration import Configuration

Configuration.TEMPLATE = \
    """#!/usr/bin/env python3
#coding: utf-8

from zengraph import *

show()
"""


def console_options_handle():
    parser = zenframe.argparse.ArgumentParser()
    pargs = parser.parse_args()
    return pargs


def top_half(communicator):
    print_to_stderr("top_half")
    pass


def bottom_half(communicator, widget):
    communicator.newdata.connect(widget.message_handler)
    return widget


def frame_creator(openpath, initial_communicator, norestore, unbound):
    from zengraph.mainwindow import MainWindow

    if openpath is None:
        openpath = create_temporary_file(
            template=Configuration.TEMPLATE)
    mainwindow = MainWindow(
        title="zengraph",
        initial_communicator=initial_communicator,
        restore_gui=not norestore)

    return mainwindow, openpath


def main():
    pargs = console_options_handle()

    frame.invoke(
        pargs,
        frame_creator=frame_creator,
        exec_top_half=top_half,
        exec_bottom_half=bottom_half)


if __name__ == "__main__":
    main()
