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

def nx_control(nx):
    print(f"NxControl received: nx = {nx}")

def nx_AP_control(nxAP):
    print(f"NxAPControl received: nxAP = {nxAP}")

def nz_control(nz):
    print(f"NzControl received: nz = {nz}")

def nz_AP_control(nzAP):
    print(f"NzAPControl received: nzAP = {nzAP}")

def setup_ivy():
    nh = lambda _x, _y: 1

    IvyInit("Avionique",
        "[%s ready]",
        0,
        nh,
        nh
    )

    IvyBindMsg(nx_control, '^APNxControl nx=(\S+)')
    IvyBindMsg(nz_control, '^APNzControl nz=(\S+)')
    IvyBindMsg(nx_AP_control, '^APNzControl nx=(\S+)')
    IvyBindMsg(nz_AP_control, '^APNzControl nz=(\S+)')
    
    IvyStart("10.1.127.255:2012")

    IvyStop()
    
