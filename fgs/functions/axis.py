"""
Donne la consigne d'axe en fonction de la position actuelle de l'avion et du plan de vol

Méthode de sélection d'axe :
    - Dans le plan de vol, on trouve le point le plus proche de l'avion
    - Si ce point est très proche d'un autre, on sélectionne l'axe suivant 
"""
from math import sqrt, atan, pi, tan
from ivy.std_api import *

import fgs.globals as fg

from fgs.defs import Point, Axis, StateVector

def get_flightplan(path="../../data/flightplan.csv"):
    res = []
    with open(path, "r") as f:
        for line in f:
            t = line.rstrip().split(',')
            res.append(Point(float(t[1]), float(t[2]), t[0]))
    return res

def check_target(fp_path="../../data/flightplan.csv"):
    """
    Le state vector doit avoir été reçu avant de pouvoir lancer cette fonction
    """
    fp = get_flightplan(fp_path)
    current_pos = Point(fg.STATE_VECTOR.x, fg.STATE_VECTOR.y)
    if pf[fg.TARGETED_LAT_WPT] - current_pos <= fg.FLYBY_RADIUS:
        fg.TARGETED_LAT_WPT += 1

def get_axis(fp_path="../../data/flightplan.csv"):
    """
    Le state vector doit avoir été reçu avant de pouvoir donner un axe
    flyby_radius : distance à laquelle l'avion capture l'axe suivant
    """
    if fg.TARGETED_LAT_WPT is None:
        fg.TARGETED_LAT_WPT = 1
    
    fp = get_flightplan(fp_path)
    
    # Rayon de virage
    phimax = 15 #degrés
    R = fg.STATE_VECTOR.Vp**2/(g*tan(phimax*pi/180))

    # Distance au WPT pour entamer le virage
    delta_chi = None
    t_wpt = fg.TARGETED_LAT_WPT

    if fg.TARGETED_LAT_WPT > 1:
        current_axis = Axis(fp[t_wpt-1], fp[t_wpt])
        last_axis = Axis(fp[t_wpt-2], fp[t_wtp-1])
        delta_chi = current_axis.chi - last_axis.chi

        d = R * tan(delta_chi/2) * 1.5

        current_pos = Point(fg.STATE_VECTOR.x, fg.STATE_VECTOR.y)
        # si la distance entre l'avion et le point visé est plus petite que la distance de virage
        if (current_pos - fp[fg.TARGETED_LAT_WPT]) <= d:
            if fg.TARGETED_LAT_WPT + 1 < len(fp): # on ne déborde pas le plan de vol
                fg.TARGETED_LAT_WPT += 1
                # envoyer l'axe suivant
                a = Axis(fp[fg.TARGETED_LAT_WPT-1], fp[fg.TARGETED_LAT_WPT])
                IvySendMsg(f"Axis x={a.p0.x} y={a.p0.y} chi={a.chi}")
                return
    else:
        a = Axis(fp[0], fp[1])
        IvySendMsg(f"Axis x={a.p0.x} y={a.p0.y} chi={a.chi}")
        return

if __name__ == "__main__":
    p1 = Point(.0, .0)
    p2 = Point(2.0, 2.0)
    print(f"||p1 - p2|| = {p1 - p2}")