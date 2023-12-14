from math import sqrt, atan2, degrees, pi, tan
from ivy.std_api import *
from colorama import Fore

from fgs.defs import Point, Axis, get_flightplan
import fgs.globals as fg

def get_DIRTO_axis(to_point:Point):
    if fg.LOG:
        print(f"[*]{Fore.LIGHTCYAN_EX} DIRTO x={to_point.x} y={to_point.y} {Fore.RESET}")
    
    current_pos = Point(fg.STATE_VECTOR.x, fg.STATE_VECTOR.y)
    a = Axis(current_pos, to_point)
    IvySendMsg(f"Axis x={a.p0.x} y={a.p0.y} chi={a.cap}")

