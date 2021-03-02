from zenframe.unbound import unbound_worker_bottom_half
import zengraph.display


def disp(wdg, a, b, c=1, d=1):
    display_widget = zengraph.display.instance()
    display_widget.add(wdg, a, b, c, d)


def show():
    widget = zengraph.display.instance()
    unbound_worker_bottom_half(widget=widget)
