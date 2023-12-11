import time
from ivy.std_api import *
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
clear



def send_bank_angle(state_vector):
    # Règles spécifiées pour l'angle de braquage en fonction de la vitesse de manoeuvre
    maneuvering_speed = state_vector.Vp
    if maneuvering_speed <= maneuvering_speed -10:
        bank_angle_max = 15
    elif maneuvering_speed <= (maneuvering_speed - 3):
        bank_angle_max = 20
    else:
        # Choix entre la guidance latérale sélectionnée et gérée
        if selected_lateral_guidance:
            bank_angle_max = 25
        else:
            bank_angle_max = 30
    IvySendMsg(f"^phimax={bank_angle_max}")
    
# Définir la variable pour la guidance latérale sélectionnée (à remplacer par vos données réelles)
selected_lateral_guidance = True

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

