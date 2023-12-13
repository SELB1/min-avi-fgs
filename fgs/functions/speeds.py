"""
Donnne Vi, et l'enveloppe [Vmin, Vmax]

^SpeedLimits vmin=(\S+) vmax=(\S+)
^ManagedSpeed vi=(\S+) 
"""
from ivy.std_api import *
import fgs.globals as fg

def speed_limits():
    ldg = fg.LDG
    flap = fg.FLAP
    if ldg == 0 :
        if flap == 0 :
            vmax = 350
        elif flap == 1 :
            vmax = 230
        else :
            vmax = 200
    else :
        if flap == 0 :
            vmax = 250
        elif flap == 1 :
            vmax = 230
        else :
            vmax = 200

    vmin = 80
    IvySendMsg(f"SpeedLimits vmin={vmin} vmax={vmax}")

def managed_speed():
    ldg = fg.LDG
    flap = fg.FLAP
    if ldg == 0 :
        if flap == 0 :
            vmax = 350
        elif flap == 1 :
            vmax = 230
        else :
            vmax = 200
    else :
        if flap == 0 :
            vmax = 250
        elif flap == 1 :
            vmax = 230
        else:
            vmax = 200
    IvySendMsg(f"ManagedSpeed vi={vmax}")

def setup_ivy():
    nh = lambda _x, _y: 1

    IvyInit("Avionique",
        "[%s ready]",
        0,
        nh,
        nh
    )
    
    IvyBindMsg(speed_limits, '^MancheFlap f=(\S+)')

    IvyStart("10.1.127.255:2012") 

    Ivystop()
