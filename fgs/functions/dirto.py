from math import sqrt, atan2, degrees, pi, tan
from ivy.std_api import *

__FGS_TARGETED_WPT = None

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
    def __init__(self, first: Point, second: Point):
        # x => Nord (vrai)
        # y => Est
        self.chi = atan2(second.x - first.x, second.y - first.y) * 180/pi
        self.p0 = first

def get_flightplan(path="../../data/flightplan.csv"):
    res = []
    with open(path, "r") as f:
        for line in f:
            t = line.rstrip().split(',')
            res.append(Point(float(t[1]), float(t[2]), t[0]))
    return res

def calculate_direction_to_waypoint(current_position, waypoint):
    # Calcul de la direction vers le waypoint en degrés
    direction = atan2(waypoint.x - current_position.x, waypoint.y - current_position.y) * 180/pi
    return direction

def send_dirto_command(direction):
    IvySendMsg(f"DIRTO {direction}")

def get_axis(StateVector: object, fp_path="../../data/flightplan.csv"):
    global __FGS_TARGETED_WPT
    if __FGS_TARGETED_WPT is None:
        __FGS_TARGETED_WPT = 0
    
    SV = StateVector
    fp = get_flightplan(fp_path)
    
    # Rayon de virage
    phimax = 15  # degrés
    R = SV.Vp**2 / (g * tan(phimax * pi / 180))

    # Calcul de la direction vers le waypoint cible
    if __FGS_TARGETED_WPT < len(fp):
        waypoint = fp[__FGS_TARGETED_WPT]
        direction_to_waypoint = calculate_direction_to_waypoint(Point(SV.x, SV.y), waypoint)
        send_dirto_command(direction_to_waypoint)

if __name__ == "__main__":
    p1 = Point(0.0, 0.0)
    p2 = Point(2.0, 2.0)
    print(f"||p1 - p2|| = {p1 - p2}")


