"""
Fonction DIRect TO
"""
from ivy.std_api import *
from math import sqrt, atan, pi, tan

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

def dirto(sv, point):
    #to do penser à modifier la variable globale



