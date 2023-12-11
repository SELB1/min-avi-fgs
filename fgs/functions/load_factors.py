"""
Donne nx, nz et nx_AP, nz_AP
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
        
def callback(agent, *data):
    print(f"Ivy message received: {data}")
clear

def loadfactors():
    nx_max=2.5
    nx_min=-1
    nz_max=2.5
    nz_min=2.5
    nx_AP=2.5
    nz_AP=2.5
    IvySendMsg(f"NxControl nx_max={nx_max}")
    IvySendMsg(f"NxControl nx_min={nx_min}")
    IvySendMsg(f"NxControl nz_max={nz_max}")
    IvySendMsg(f"NxControl nz_min={nz_min}")
    IvySendMsg(f"NxAPControl nxAP={nx_AP}")
    IvySendMsg(f"NzAPControl nzAP={nz_AP}")
          

def setup_ivy():
    nh = lambda _x, _y: 1

    IvyInit("Avionique",
        "[%s ready]",
        0,
        nh,
        nh
    )

    IvyStart("10.1.127.255:2012")
    
    IvyStop()