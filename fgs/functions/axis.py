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
            if fg.TARGETED_LAT_WPT + 2 < len(fp):
                fg.TARGETED_LAT_WPT = i+1
            if fg.LOG:
                print(f"[*] On lateral FLPN{Fore.LIGHTBLACK_EX} TARGETED_LAT_WPT = {fg.TARGETED_LAT_WPT}{Fore.RESET}")

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
    current_pos = Point(fg.STATE_VECTOR.x, fg.STATE_VECTOR.y)
    a = None
    if 0 < fg.TARGETED_LAT_WPT < len(fp)-1:
        next_axis = Axis(fp[t_wpt], fp[t_wpt+1])
        current_axis = Axis(fp[t_wpt-1], fp[t_wpt])
        delta_chi = next_axis.chi - current_axis.chi

        # Si delta_chi=0, d = 0, et le FGS n'envoie pas l'axe suivant, d'ou la borne inf
        d = max(R * tan(delta_chi/2) * 1.5, fd.MIN_FLYBY_RADIUS)
        if fg.LOG:
            print("[*] " + Fore.LIGHTBLACK_EX + f"d = {d}" + Fore.RESET)
        
        # distance entre l'avion et le point visé
        distance = current_pos - fp[fg.TARGETED_LAT_WPT]

        # si la distance entre l'avion et le point visé est plus petite que la distance de virage et que le point visé est un fly-by
        # ou que la distance entre l'avion et le point visé est plus petite que le rayon de flyover et que le point visé est un fly-over
        if distance <= d and fp[fg.TARGETED_LAT_WPT].fly_by or distance <= fd.FLYOVER_RADIUS and fp[fg.TARGETED_LAT_WPT].fly_over:
            if fg.TARGETED_LAT_WPT + 1 < len(fp): # on ne déborde pas du plan de vol, +2 cf ligne 49
                fg.TARGETED_LAT_WPT += 1 # on sélectionne le point suivant
        if fg.TARGETED_LAT_WPT < len(fp):
            a = Axis(fp[fg.TARGETED_LAT_WPT-1], fp[fg.TARGETED_LAT_WPT])
    elif fg.TARGETED_LAT_WPT == len(fp)-1:
        a = Axis(fp[fg.TARGETED_LAT_WPT-1], fp[fg.TARGETED_LAT_WPT])
    else:
        print(f"{Fore.RED}t_wpt={fg.TARGETED_LAT_WPT}{Fore.RESET}")

    IvySendMsg(f"Axis x={a.p0.x} y={a.p0.y} chi={a.cap}")
    if fg.LOG:
        print(f"[*]{Fore.LIGHTBLACK_EX} {a}{Fore.RESET}")

if __name__ == "__main__":
    p1 = Point(.0, .0)
    p2 = Point(2.0, 2.0)
    print(f"||p1 - p2|| = {p1 - p2}")