import time
from ivy.std_api import *
maneuvering_speed = 128 #internet
class StateVector:
    def __init__(self, x:float, y:float, z:float, Vp:float, fpa:float, psi:float, phi:float):
        self.x = x
        self.y = y
        self.z = z
        self.Vp = Vp
        self.fpa = fpa
        self.psi = psi
        self.phi = phi

def callback(agent, *data):
    print(f"Ivy message received: {data}")




def send_bank_angle(state_vector):
    # Règles spécifiées pour l'angle de braquage en fonction de la vitesse de manoeuvre
    vp = state_vector.Vp
    bank_angle_max = 67 #p1003
    pmax, pmax_AP = 15
    if vp <= maneuvering_speed -10:
        bank_angle_max_AP= 15
    else:
        bank_angle_max_AP = 25
        # Choix entre la guidance latérale sélectionnée et gérée
    IvySendMsg(f"RollLimits phimax={bank_angle_max} pmax={pmax}")
    IvySendMsg(f"RollLimitsAP phimax_AP={bank_angle_max_AP} pmax_AP={pmax_AP}")



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

