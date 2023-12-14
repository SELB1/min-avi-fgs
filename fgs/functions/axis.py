"""
Donne la consigne d'axe en fonction de la position actuelle de l'avion, du plan de vol et du point visé

Méthode de sélection d'axe :
    - On sélectionne par défault l'axe formé par les points d'indice fg.TARGETED_LAT_WPT-1 et fg.TARGETED_LAT_WPT
    - Si l'avion est suffisement proche du point d'indice fg.TARGETED_LAT_WPT, on envoie l'axe suivant et on incrémente fg.TARGETED_LAT_WPT
"""
from math import sqrt, atan, pi, tan
from ivy.std_api import *
from colorama import Fore

import fgs.globals as fg
import fgs.defs as fd

from fgs.defs import Point, Axis, StateVector, get_flightplan

def join_lat_FLPN(fp_path="../../data/flightplan.csv"):
    """
    Rejoint le plan de vol latéral si l'avion est à au plus FLPN_JOIN_RADIUS d'un point
    """
    fp = get_flightplan(fp_path)
    current_pos = Point(fg.STATE_VECTOR.x, fg.STATE_VECTOR.y)
    for i in range(fg.TARGETED_LAT_WPT, len(fp)):
        if fp[i] - current_pos <= fd.FLPN_JOIN_RADIUS:
            if fg.LOG:
                print(f"[*] On lateral FLPN{Fore.LIGHTBLACK_EX} TARGETED_LAT_WPT={fg.TARGETED_LAT_WPT}{Fore.RESET}")
            fg.TARGETED_LAT_WPT = i

def get_axis(fp_path="../../data/flightplan.csv"):
    """
    Le state vector doit avoir été reçu avant de pouvoir donner un axe
    flyby_radius : distance à laquelle l'avion capture l'axe suivant
    """
    fp = get_flightplan(fp_path)
    
    # Rayon de virage
    phimax = 15 #degrés
    R = fg.STATE_VECTOR.Vp**2/(9.81*tan(phimax*pi/180))

    # Distance au WPT pour entamer le virage
    delta_chi = None
    t_wpt = fg.TARGETED_LAT_WPT
    a = None
    if fg.TARGETED_LAT_WPT > 1:
        current_axis = Axis(fp[t_wpt-1], fp[t_wpt])
        last_axis = Axis(fp[t_wpt-2], fp[t_wpt-1])
        delta_chi = current_axis.chi - last_axis.chi

        d = R * tan(delta_chi/2) * 1.5
        if fg.LOG:
            print("[*] " + Fore.LIGHTBLACK_EX + f"d = {d}" + Fore.RESET)

        current_pos = Point(fg.STATE_VECTOR.x, fg.STATE_VECTOR.y)
        
        # distance entre l'avion et le point visé
        distance = current_pos - fp[fg.TARGETED_LAT_WPT]

        # si la distance entre l'avion et le point visé est plus petite que la distance de virage et que le point visé est un fly-by
        # ou que la distance entre l'avion et le point visé est plus petite que le rayon de flyover et que le point visé est un fly-over
        if distance <= d and fp[fg.TARGETED_LAT_WPT].fly_by or distance <= fd.FLYOVER_RADIUS and fp[fg.TARGETED_LAT_WPT].fly_over:
            if fg.TARGETED_LAT_WPT + 1 < len(fp): # on ne déborde pas le plan de vol
                # envoyer l'axe suivant
                fg.TARGETED_LAT_WPT += 1
        
        a = Axis(fp[fg.TARGETED_LAT_WPT-1], fp[fg.TARGETED_LAT_WPT])
    else:
        a = Axis(fp[0], fp[1])

    IvySendMsg(f"Axis x={a.p0.x} y={a.p0.y} chi={a.cap}")
    if fg.LOG:
        print(f"[*]{Fore.LIGHTBLACK_EX} {a}{Fore.RESET}")

if __name__ == "__main__":
    p1 = Point(.0, .0)
    p2 = Point(2.0, 2.0)
    print(f"||p1 - p2|| = {p1 - p2}")