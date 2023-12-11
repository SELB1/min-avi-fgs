"""
Fichier principal
"""
from ivy.std_api import *
from math import *
from colorama import Fore
# Prefixed variables
import fgs.globals as fg
import fgs.defs as fd

import fgs.functions.axis as axis

def on_state_vector(agent, *a):
    # Store state vector
    fg.STATE_VECTOR = fd.StateVector(a[0], a[1], a[2], a[3], a[4], a[5], a[6])
    if fg.LOG:
        print("[*] " + Fore.LIGHTBLACK_EX + str(fg.STATE_VECTOR) + Fore.RESET)
    # Call axis capture functions
    axis.join_FLPN(fp_path="data/flightplan.csv")
    axis.get_axis(fp_path="data/flightplan.csv")

def on_test(agent, *a):
    print("Test received!")

def bind_messages():
    """
    Bind all Ivy messages
    """
    IvyBindMsg(on_state_vector, '^StateVector x=(\S+) y=(\S+) z=(\S+) Vp=(\S+) fpa=(\S+) psi=(\S+) phi=(\S+)')
    IvyBindMsg(on_test, '^Test a=(\S+)')
    print("[-] " + Fore.LIGHTBLUE_EX + "Ivy binds ok" + Fore.RESET)

def init_fgs():
    DirWind = 15*180/pi
    VWind =  10
    route = 14
    d = asin(VWind*sin(route - DirWind)/128)
    IvySendMsg(f'InitStateVector x=0 y=0 z=0 Vp=128 fpa=0 psi={route-d} phi=0')
    IvySendMsg(f'MagneticDeclination={fd.MAGNETIC_DEVIATION}')
    IvySendMsg('WindComponent VWind=10 dirWind=15')