"""
Donne nx, nz et nx_AP, nz_AP
"""
from ivy.std_api import *

from fgs.defs import StateVector
        
def callback(agent, *data):
    print(f"Ivy message received: {data}")


def loadfactors():
    nx_pos, nx_pos_AP= (2.5, 2.5)
    nx_neg, nx_neg_AP= (-1, -1)
    nz_pos, nz_pos_AP= (2.5, 2.5)
    nz_neg, nz_neg_AP= (-1, -1)
    IvySendMsg(f"LimitsNAP nx_neg_AP={nx_neg_AP} nx_pos_AP={nx_pos_AP} nz_neg_AP={nz_neg_AP} nz_pos_AP={nz_pos_AP}")
    IvySendMsg(f"LimitsN nx_neg={nx_neg} nx_pos={nx_pos} nz_neg={nz_neg} nz_pos={nz_pos}")

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
    
