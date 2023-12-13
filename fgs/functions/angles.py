import time
from ivy.std_api import *

import fgs.globals as fg

maneuvering_speed = 128 #internet

def callback(agent, *data):
    print(f"Ivy message received: {data}")

def send_bank_angle():
    # Règles spécifiées pour l'angle de braquage en fonction de la vitesse de manoeuvre
    vp = fg.STATE_VECTOR.Vp
    bank_angle_max = 67 #p1003
    pmax, pmax_AP = (15, 15)
    if vp <= maneuvering_speed -10:
        bank_angle_max_AP= 15
    else:
        bank_angle_max_AP = 25
        # Choix entre la guidance latérale sélectionnée et gérée
    IvySendMsg(f"RollLimits phimax={bank_angle_max} pmax={pmax}")
    IvySendMsg(f"RollLimitsAP phimax_AP={bank_angle_max_AP} pmax_AP={pmax_AP}")

if __name__ == "__main__":
    nh = lambda _x, _y: 1

    IvyInit("Test",
        "[%s ready]",
        0,
        nh,
        nh
    )

    IvyBindMsg(callback, '^Test aaa=(\S+')
    IvyStart("127.255.255.255:2010")

    IvyStop()

