"""
Helper classes and constants
"""
from math import sqrt, atan2, pi
### HELPER CLASSES ###
class StateVector:
    def __init__(self, x:float, y:float, z:float, Vp:float, fpa:float, psi:float, phi:float):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.Vp = float(Vp)
        self.fpa = float(fpa)
        self.psi = float(psi)
        self.phi = float(phi)

    def __str__(self) -> str:
        return f"StateVector\r\nx={self.x}, y={self.y}, z={self.z}\r\nVp={self.Vp}, fpa={self.fpa}\r\npsi={self.psi}, phi={self.phi}"

    def __format__(self) -> str:
        return self.__str__()

class Point:
    def __init__(self, x, y, fly_over=False, fly_by=True, name=""):
        self.x = float(x)
        self.y = float(y)
        self.name = name
        self.fly_over = fly_over
        self.fly_by = fly_by
    
    def __sub__(self, other):
        """
        Distance entre deux points
        """
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Axis:
    def __init__(self, first:Point, second:Point):
        # x => Nord (vrai)
        # y => Est
        self.chi = atan2((second.y - first.y), (second.x - first.x)) * 180/pi
        self.p0 = first
    def __str__(self):
        return f"Axis x={self.p0.x} y={self.p0.y} chi={self.chi}"
    def __format__(self, _):
        return self.__str__()

### CONSTANTS ###
FLYBY_RADIUS = 1852
FLYOVER_RADIUS = 185
MAGNETIC_DEVIATION = 13.59
