from colorama import Fore

import fgs.globals as fg 
import fgs.defs as fd
from fgs.defs import Point, get_flightplan

from ivy.std_api import *

def join_hgt_FLPN(fp_path="../../data/flightplan.csv"):
    """
    Rejoint le plan de vol vertical si l'avion est à au plus FLPN_JOIN_RADIUS d'un point et que l'avion est à -+3000ft de l'altitude du point
    """
    fp = get_flightplan(fp_path)
    current_pos = Point(fg.STATE_VECTOR.x, fg.STATE_VECTOR.y)
    for i in range(fg.TARGETED_HGT_WPT, len(fp)):
        if fp[i] - current_pos <= fd.FLPN_JOIN_RADIUS and abs(fp[i].z - current_pos.z) <= fd.FLPN_JOIN_HEIGHT:
            if fg.LOG:
                print(f"[*] On vertical FLPN{Fore.LIGHTBLACK_EX} TARGETED_HGT_WPT={fg.TARGETED_HGT_WPT}{Fore.RESET}")
            fg.TARGETED_HGT_WPT = i

def get_alt(fp_path="../../data/flightplan.csv"):
    """
    Envoie la consigne d'altitude au cas ou l'avion est près d'un point du plan de vol
    """
    fp = get_flightplan(fp_path)
    t_wpt = fg.TARGETED_HGT_WPT
    current_pos = Point(fg.STATE_VECTOR.x, fg.STATE_VECTOR.y)
    # Si l'avion est dans le rayon de rejointe et que son altitude est suffisement proche de celle du point
    if fp[t_wpt] - current_pos <= fd.FLPN_JOIN_RADIUS and abs(fp[t_wpt].z - current_pos.z) <= fd.FLPN_JOIN_HEIGHT:
        # Si l'altitude est valide
        if fp[t_wpt].z > 0:
            # Si l'avion est en dessous de l'altitude de transition
            if fp[t_wpt].z <= fd.TRANSITION_ALTITUDE:
                height_QNH = ((fd.STD_ATM - fd.QNH)*28/fd.M_TO_FT + fp[t_wpt].z) * fd.M_TO_FT
                IvySendMsg(f"ManagedAlt alt={height_QNH} Q={fd.QNH}")
            else: 
                # sans doute faux
                fl = fp[t_wpt].z * 3.28
                IvySendMsg(f"ManagedAlt alt={fl} Q={fd.STD_ATM}")
        fg.TARGETED_HGT_WPT += 1
