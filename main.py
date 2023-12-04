"""
Fichier principal
"""
from ivy.std_api import *

# Prefixed variables
__FGS_STATE_VECTOR = None

class StateVector:
    def __init__(self, x:float, y:float, z:float, Vp:float, fpa:float, psi:float, phi:float):
        self.x = x
        self.y = y
        self.z = z
        self.Vp = Vp
        self.fpa = fpa
        self.psi = psi
        self.phi = phi

    def __str__(self) -> str:
        f"StateVector\r\nx={self.x}, y={self.y}, z={self.z}\r\nVp={self.Vp}, fpa={self.fpa}\r\npsi={self.psi}, phi={self.phi}"

    def __format__(self) -> str:
        return self.__str__()

def on_state_vector(agent, *a):
    global __FGS_STATE_VECTOR
    __FGS_STATE_VECTOR = StateVector(a[0], a[1], a[2], a[3], a[4], a[5], a[6])

def bind_messages():
    """
    Bind all Ivy messages
    """
    IvyBindMsg(on_state_vector, '^StateVector x=(\\S+) y=(\\S+) z=(\\S+) Vp=(\\S+) fpa=(\\S+) psi=(\\S+) phi=(\\S+)')

def main():
    IvyInit("AVI_FGS", "Ready", 0, void_function, void_function)
    IvyStart("127.255.255.255:2010")

    bind_messages()
    
    IvyMainLoop()

if __name__ == "__main__":
    main()