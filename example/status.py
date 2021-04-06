#!/usr/bin/env python3

from zengraph import *
from zengraph.status import StatusWidget
from zengraph.image import MapImage

import json
import pycrow


def incoming(pack):
    try:
        msg = pack.message()
        dct = json.loads(msg)
        for k, v in dct.items():
            s.set_status(k, v == 1)
            s.update()
    except Exception as ex:
        pass


print("A")
crowker_address = pycrow.address(".12.127.0.0.1:10009")
#ugate = pycrow.udpgate()
# ugate.bind(12)
pycrow.create_udpgate(12, 0)
pycrow.diagnostic_setup(True, False)


print("B")
sub = pycrow.subscriber(incoming)

sub.subscribe(crowker_address, "system_status", 2, 50, 2, 50)


print("C")
pycrow.start_spin()
pycrow.start_resubscribe_thread(1000)

print("D")
s = StatusWidget(["aidan", "base", "zippo"], cols=3)

s.set_status("base", True)

# sub.resubscribe()
print("Display")
disp(s, 1, 1)
print("Show")
show()
