"""
Donnne Vi, et l'enveloppe [Vmin, Vmax]
"""
from ivy.std_api import *


def speed_limits(vmin, vmax):
    IvySendMsg(f"v_min={v_min}")
    IvySendMsg(f"v_max={v_max}")

def managed_speed(vi):
    IvySendMsg(f"managed speed vi={vi}")

def setup_ivy():
    nh = lambda _x, _y: 1

    IvyInit("Avionique",
        "[%s ready]",
        0,
        nh,
        nh
    )
    
    IvyStart("10.1.127.255:2012")

    Ivystop()



