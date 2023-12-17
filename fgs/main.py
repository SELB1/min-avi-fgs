"""
Fichier principal
"""
from ivy.std_api import *
from math import *
from colorama import Fore
from time import sleep
# Prefixed variables
import fgs.globals as fg
import fgs.defs as fd

import fgs.functions as fn
from time import sleep

def on_state_vector(agent, *a):
    # Store state vector
    fg.STATE_VECTOR = fd.StateVector(a[0], a[1], a[2], a[3], a[4], a[5], a[6])
    if fg.LOG:
        print("[*] " + Fore.LIGHTBLACK_EX + str(fg.STATE_VECTOR) + Fore.RESET)
    # Send limits FIRST
    # Send speed limits
    fn.speeds.speed_limits()
    fn.speeds.managed_speed()
    # Send load factors
    fn.load_factors.loadfactors()
    # Send angle limits
    fn.angles.send_bank_angle()
    # Call vertical FLPN capture functions
    fn.altitude.join_hgt_FLPN(fp_path=fg.FP_PATH)
    fn.altitude.get_alt(fp_path=fg.FP_PATH)
    # Call lateral FLPN capture functions
    fn.axis.join_lat_FLPN(fp_path=fg.FP_PATH)
    fn.axis.get_axis(fp_path=fg.FP_PATH)

def on_test(agent, *a):
    print("Test received!")

def on_DIRTO(agent, *a):
    to_point = fd.Point(a[0], a[1])
    fn.dirto.get_DIRTO_axis(to_point)

def on_ldg(agent, *a):
    fg.LDG = int(a[0])

def on_flap(agent, *a):
    fg.FLAP = int(a[0])

def bind_messages():
    """
    Bind all Ivy messages
    """
    IvyBindMsg(on_state_vector, '^StateVector x=(\S+) y=(\S+) z=(\S+) Vp=(\S+) fpa=(\S+) psi=(\S+) phi=(\S+)')
    IvyBindMsg(on_flap, '^MancheFlap f=(\S+)')
    IvyBindMsg(on_ldg, '^MancheLdg ldg=(\S+)')
    IvyBindMsg(on_test, '^Test a=(\S+)')
    IvyBindMsg(on_DIRTO, '^DIRTO x=(\S+) y=(\S+)')

    sleep(0.1)
    print("[-] " + Fore.LIGHTBLUE_EX + "Ivy binds ok" + Fore.RESET)

def init_fgs():
    """
    TODO : corriger la trajectoire de l'avion
    """
    sleep(0.1)
    DirWind = 15*pi/180
    VWind =  10
    route = 14*pi/180
    d = asin(VWind*sin(route - DirWind)/128)
    IvySendMsg(f'InitStateVector x=0 y=0 z=100 Vp=128 fpa=0 psi={route-d} phi=0')
    IvySendMsg(f'MagneticDeclination={fd.MAGNETIC_DEVIATION*pi/180}')
    IvySendMsg(f'WindComponent VWind=10 dirWind={DirWind}')