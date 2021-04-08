from zenframe.unbound import (
    unbound_worker_bottom_half,
    unbound_frame_summon,
    is_unbound_mode
)
import zengraph.display
import zenframe.finisher


def disp(wdg, a, b, c=1, d=1):
    display_widget = zengraph.display.instance()
    display_widget.add(wdg, a, b, c, d)


def widget_creator(self):
    widget = zengraph.display.instance()
    return widget


def show(onclose):
    for d in onclose:
        zenframe.finisher.register_destructor(d, d)

    if is_unbound_mode():
        print("unbound_worker_bottom_half")
        widget = zengraph.display.instance()
        unbound_worker_bottom_half(widget=widget)

    else:
        print("unbound_frame_summon")
        unbound_frame_summon(widget_creator, "zengraph")
