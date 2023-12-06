"""
Fichier principal
"""
from ivy.std_api import *

# Prefixed variables
from fgs.globals import __FGS_STATE_VECTOR

def on_state_vector(agent, *a):
    global __FGS_STATE_VECTOR
    __FGS_STATE_VECTOR = StateVector(a[0], a[1], a[2], a[3], a[4], a[5], a[6])

def bind_messages():
    """
    Bind all Ivy messages
    """
    IvyBindMsg(on_state_vector, '^StateVector x=(\\S+) y=(\\S+) z=(\\S+) Vp=(\\S+) fpa=(\\S+) psi=(\\S+) phi=(\\S+)')