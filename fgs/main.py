"""
Fichier principal
"""
from ivy.std_api import *
from math import *
from colorama import Fore
# Prefixed variables
import fgs.globals as fg
import fgs.defs as fd

import fgs.functions as fn

def on_state_vector(agent, *a):
    # Store state vector
    fg.STATE_VECTOR = fd.StateVector(a[0], a[1], a[2], a[3], a[4], a[5], a[6])
    if fg.LOG:
        print("[*] " + Fore.LIGHTBLACK_EX + str(fg.STATE_VECTOR) + Fore.RESET)
    # Call axis capture functions
    fn.axis.join_FLPN(fp_path="data/flightplan.csv")
    fn.axis.get_axis(fp_path="data/flightplan.csv")

def on_test(agent, *a):
    print("Test received!")

def on_DIRTO(agent, *a):
    to_point = Point(a[0], a[1])
    fn.dirto.get_DIRTO_axis(to_point)

def on_configuration(agent, *a):
    fn.speeds.speed_limits(a[0])
    fn.speeds.managed_speed(a[0])

def bind_messages():
    """
    Bind all Ivy messages
    """
    IvyBindMsg(on_state_vector, '^StateVector x=(\S+) y=(\S+) z=(\S+) Vp=(\S+) fpa=(\S+) psi=(\S+) phi=(\S+)')
    IvyBindMsg(on_configuration, '^MancheFlap f=(\S+)')
    IvyBindMsg(on_test, '^Test a=(\S+)')
    IvyBindMsg(on_DIRTO, '^DIRTO x=(\S+) y=(\S+)')

    print("[-] " + Fore.LIGHTBLUE_EX + "Ivy binds ok" + Fore.RESET)

def init_fgs():
    DirWind = 15*180/pi
    VWind =  10
    route = 14
    d = asin(VWind*sin(route - DirWind)/128)
    IvySendMsg(f'InitStateVector x=0 y=0 z=0 Vp=128 fpa=0 psi={route-d} phi=0')
    IvySendMsg(f'MagneticDeclination={fd.MAGNETIC_DEVIATION}')
    IvySendMsg('WindComponent VWind=10 dirWind=15')
