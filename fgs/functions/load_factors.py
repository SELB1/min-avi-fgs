"""
Donne nx, nz et nx_AP, nz_AP
"""
from ivy.std_api import *

def nx_control(nx):
    print(f"NxControl received: nx = {nx}")

def nz_control(nz):
    print(f"NzControl received: nz = {nz}")

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
    
    IvyStart("10.1.127.255:2012")

def send_nx_control(nx):
    IvySendMsg(f"NxControl nx={nx}")

def send_nz_control(nz):
    IvySendMsg(f"NzControl nz={nz}")
