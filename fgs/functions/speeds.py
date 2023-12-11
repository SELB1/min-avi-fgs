"""
Donnne Vi, et l'enveloppe [Vmin, Vmax]
"""
from ivy.std_api import *


def speed_limits():
    vmin = 110
    vmax = 180
    IvySendMsg(f"v_min={vmin}")
    IvySendMsg(f"v_max={vmax}")

def managed_speed():
    vi = 150
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



