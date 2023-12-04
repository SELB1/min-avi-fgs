"""
Donnne Vi, et l'enveloppe [Vmin, Vmax]
"""
from ivy.std_api import *

class StateVector:
    def __init__(self, x:float, y:float, z:float, Vp:float, fpa:float, psi:float, phi:float):
        self.x = x
        self.y = y
        self.z = z
        self.Vp = Vp
        self.fpa = fpa
        self.psi = psi
        self.phi = phi

def speed_limits(vmin, vmax):
    print(f"Speed limits received: Vmin = {128}, Vmax = {180}")

def managed_speed(vi):
    print(f"Managed speed received: Vi = {vi}")

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

def send_speed_limits(vmin, vmax):
    IvySendMsg(f"SpeedLimits vmin={vmin} vmax={vmax}")

def send_managed_speed(vi):
    IvySendMsg(f"ManagedSpeed vi={vi}")


