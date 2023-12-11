"""
Donne nx, nz et nx_AP, nz_AP
"""
from ivy.std_api import *

from fgs.defs import StateVector
        
def callback(agent, *data):
    print(f"Ivy message received: {data}")
clear

def loadfactors():
    nx_pos, nx_pos_AP=2.5
    nx_neg, nx_neg_AP=-1
    nz_pos, nz_pos_AP=2.5
    nz_neg, nz_neg_AP=-1
    IvySendMsg(f"LimitsNAP nx_neg_AP=(\S+) nx_pos_AP=(\S+) nz_neg_AP=(\S+) nz_pos_AP=(\S+)")
    IvySendMsg(f"LimitsN nx_neg=(\S+) nx_pos=(\S+) nz_neg=(\S+) nz_pos=(\S+)")
    
          

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
    
