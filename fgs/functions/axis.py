"""
Donne la consigne d'axe en fonction de la position actuelle de l'avion et du plan de vol

Méthode de sélection d'axe :
    - Dans le plan de vol, on trouve le point le plus proche de l'avion
    - Si ce point est très proche d'un autre, on sélectionne l'axe suivant 
"""
from math import sqrt, atan, pi, tan

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
    def __init__(self, first:Point, second:Point):
        # x => Nord (vrai)
        # y => Est
        self.chi = atan((second.x - first.x)/(second.y - first.y)) * 180/pi
        self.p0 = first

def get_flightplan(path="../../data/flightplan.csv"):
    res = []
    with open(path, "r") as f:
        for line in f:
            t = line.rstrip().split(',')
            res.append(Point(float(t[1]), float(t[2]), t[0]))
    return res

def get_axis(StateVector:object, fp_path="../../data/flightplan.csv"):
    """
    flyby_radius : distance à laquelle l'avion capture l'axe suivant
    """
    global __FGS_TARGETED_WPT
    if __FGS_TARGETED_WPT is None:
        __FGS_TARGETED_WPT = 0
    
    SV = StateVector
    fp = get_flightplan(fp_path)
    
    # Rayon de virage
    phimax = 15 #degrés
    R = SV.Vp**2/(g*tan(phimax*pi/180))

    # Distance au WPT pour entamer le virage
    delta_chi = None
    t_wpt = __FGS_TARGETED_WPT
    
    if __FGS_TARGETED_WPT > 1:
        current_axis = Axis(fp[t_wpt-1], fp[t_wpt])
        last_axis = Axis(fp[t_wpt-2], fp[t_wtp-1])
        delta_chi = current_axis.chi - last_axis.chi
    else:


    d = R * tan()

    IvySendMsg(f"Axis x={a.p0.x} y={a.p0.y} chi={a.chi}")

if __name__ == "__main__":
    p1 = Point(.0, .0)
    p2 = Point(2.0, 2.0)
    print(f"||p1 - p2|| = {p1 - p2}")