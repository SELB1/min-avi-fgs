"""
Helper classes and constants
"""

### HELPER CLASSES ###
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

class Point:
    def __init__(self, x, y, name=""):
        self.x = x
        self.y = y
        self.name = name
    
    def __sub__(self, other):
        """
        Distance entre deux points
        """
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Axis:
    def __init__(self, first:Point, second:Point):
        # x => Nord (vrai)
        # y => Est
        self.chi = atan((second.x - first.x)/(second.y - first.y)) * 180/pi
        self.p0 = first


### CONSTANTS ###
FLYBY_RADIUS = 1852
FLYOVER_RADIUS = 185
MAGNETIC_DEVIATION = 13.59
