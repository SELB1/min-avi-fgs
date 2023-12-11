"""
Donnne Vi, et l'enveloppe [Vmin, Vmax]
"""
from ivy.std_api import *


def speed_limits(vmin, vmax):
    print(f"Speed limits received: Vmin = {128}, Vmax = {180}")

def managed_speed(vi):
    print(f"Managed speed received: Vi = {140}")

def setup_ivy():
    nh = lambda _x, _y: 1

    IvyInit("Avionique",
        "[%s ready]",
        0,
        nh,
        nh
    )
    IvyBindMsg(speed_limits, '^SpeedLimits vmin=(\S+) vmax=(\S+)') #(*à modifier*)
    IvyBindMsg(managed_speed, '^ManagedSpeed vi=(\S+)') #(*à modifier*)
    
    IvyStart("10.1.127.255:2012")

    Ivystop()



