import matplotlib.pyplot as plt
import numpy as np
from math import atan2, degrees, radians, cos, sin, pi
from colorama import Fore

from fgs.defs import Axis, Point

from ivy.std_api import *
from time import sleep

def get_flightplan(path="./../../data/flightplan.csv"):
    res = []
    with open(path, "r") as f:
        for line in f:
            t = line.rstrip().split(',')
            res.append(Point(float(t[1]), float(t[2]), t[0]))
    return res

def plot_flight(flightplan):
    # Tracé du plan de vol et des axes
    plt.figure(figsize=(10, 10))

    # Tracé du plan de vol
    for point in flightplan:
        if point.fly_by:
            plt.plot(point.x, point.y, marker='o', color='red')
        elif point.fly_over:
            plt.plot(point.x, point.y, marker='x', color='blue')
        else:
            plt.plot(point.x, point.y, marker='o', color='black')

    # Tracé des axes
    fp = flightplan
    for i in range(0, len(fp)):
        if i+1 < len(fp):
            plt.plot((fp[i].x, fp[i+1].x), (fp[i].y, fp[i+1].y), 'ro-')
        else:
            plt.plot((fp[i].x, fp[0].x), (fp[i].y, fp[0].y), 'ro-')

    plt.xlabel('Position X')
    plt.ylabel('Position Y')
    plt.title('Plan de vol avec axe')
    plt.grid(True)

def on_axis(agent, *a):
    """
    Appellé quand un axe de consigne est reçu
    """
    lengh = 2000
    chi_deg = float(a[2])
    chi = chi_deg * pi/180
    p0 = Point(a[0], a[1])
    p1 = Point(p0.x + lengh*cos(chi), p0.y + lengh*sin(chi))
    print(f"x={p0.x} y={p0.y} chi={chi_deg}")
    plt.plot((p0.x, p1.x), (p0.y, p1.y), 'bo-', label="Axe envoyé")
    plt.legend()

def run_ivy(p0:Point, fp_path="data/flightplan.csv"):
    # Charger le plan de vol
    flightplan = get_flightplan(fp_path)
    # Afficher le plan de vol
    plot_flight(flightplan)

    plt.plot(p0.x, p0.y, 'go', label="Position de l\'avion")
    sleep(0.5)
    IvySendMsg(f"StateVector x={p0.x} y={p0.y} z=0 Vp=69 fpa=0 psi=0 phi=0")
    plt.show()

def run():
    print(f"{Fore.LIGHTWHITE_EX}Test consigne d'axe")

    IvyInit("AVI_FGS", "Ready", 0, void_function, void_function)
    IvyStart("127.255.255.255:2010")
    IvyBindMsg(on_axis, '^Axis x=(\S+) y=(\S+) chi=(\S+)')

    # Cas 1 : avion trop loin d'un point du PDV
    print(f"{Fore.GREEN}Cas 1 :{Fore.RESET} avion trop loin d'un point du PDV")
    input("[enter] pour continuer : ")
    p0 = Point(-3000, -5000)
    run_ivy(p0)
    
    # Cas 2 : Rejointe du plan de vol
    print(f"{Fore.GREEN}Cas 2 :{Fore.RESET} Rejointe du plan de vol")
    input("[enter] pour continuer : ")
    p0 = Point(-3000, -2000)
    run_ivy(p0)

    # Cas 3 : Envoi de l'axe suivant pour en anticipation
    print(f"{Fore.GREEN}Cas 2 :{Fore.RESET} Envoi de l'axe suivant pour en anticipation")
    input("[enter] pour continuer : ")
    p0 = Point(-3000, -1500)
    run_ivy(p0)

    IvyStop()

def test():
    IvyInit("AVI_FGS", "Ready", 0, void_function, void_function)
    IvyStart("127.255.255.255:2010")
    sleep(0.1)
    IvySendMsg("StateVector x=-3000 y=-5000 z=0 Vp=69 fpa=0 psi=0 phi=0")
    IvySendMsg("Test a=5.3")
    IvyStop()