from zenframe.unbound import (
    unbound_worker_bottom_half,
    unbound_frame_summon,
    is_unbound_mode
)
import zengraph.display
import zenframe.finisher
import os


def disp(wdg, a=1, b=1, c=1, d=1):
    display_widget = zengraph.display.instance()
    display_widget.add(wdg, a, b, c, d)


def widget_creator(communicator):
    widget = zengraph.display.instance()
    communicator.bind_handler(widget.message_handler)
    return widget


def show(onclose=[]):
    for d in onclose:
        zenframe.finisher.register_destructor(None, d)

    zenframe.finisher.register_destructor(None, lambda: os._exit)

    if is_unbound_mode():
        widget = zengraph.display.instance()
        unbound_worker_bottom_half(widget=widget)

    else:
        unbound_frame_summon(widget_creator, "zengraph")

