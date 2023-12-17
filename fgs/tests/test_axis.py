import matplotlib.pyplot as plt
import numpy as np
from math import atan2, degrees, radians, cos, sin, pi
from colorama import Fore

from fgs.defs import Axis, Point, get_flightplan

from ivy.std_api import *
from time import sleep

def plot_flight(flightplan):
    # Tracé du plan de vol et des axes
    plt.figure(figsize=(10, 10))

    # Tracé du plan de vol
    for point in flightplan:
        if point.fly_by:
            plt.plot(point.y, point.x, marker='o', color='red')
        elif point.fly_over:
            plt.plot(point.y, point.x, marker='x', color='blue')
        else:
            plt.plot(point.y, point.x, marker='o', color='black')

    # Tracé des axes
    fp = flightplan
    for i in range(0, len(fp)):
        if i+1 < len(fp):
            plt.plot((fp[i].y, fp[i+1].y), (fp[i].x, fp[i+1].x), marker="", color="red")
        else:
            plt.plot((fp[i].y, fp[0].y), (fp[i].x, fp[0].x), marker="", color="red")

    plt.xlabel('Position Y')
    plt.ylabel('Position X')
    plt.title('Plan de vol avec axe')
    plt.grid(True)

def on_axis(agent, *a):
    """
    Appellé quand un axe de consigne est reçu
    """
    # Longueur représentée de l'axe
    lengh = 2000
    # Angle de l'axe, en degrés et en radians
    cap = float(a[2])
    # Conversion en radians
    if 0 <= cap <= 270:
        chi = 90 - cap
    else:
        chi = 270 + 180 - cap
    chi = chi * pi/180
    print(f"chi={chi}")
    # p0 et p1 sont les deux points qui forment l'axe
    p0 = Point(a[1], a[0])
    p1 = Point(p0.x + lengh*cos(chi), p0.y + lengh*sin(chi))
    print(f"x={p0.x} y={p0.y} cap={cap}")
    # Affichage
    plt.plot((p0.x, p1.x), (p0.y, p1.y), 'bo-', label="Axe envoyé")
    plt.legend()

def run_ivy(p0:Point, fp_path="data/flightplan.csv"):
    # Charger le plan de vol
    flightplan = get_flightplan(fp_path)
    # Afficher le plan de vol
    plot_flight(flightplan)

    plt.plot(p0.y, p0.x, 'go', label="Position de l\'avion")

    IvySendMsg(f"StateVector x={p0.x} y={p0.y} z=0 Vp=69 fpa=0 psi=0 phi=0")
    plt.show()

def run():
    print(f"{Fore.LIGHTWHITE_EX}Test consigne d'axe")

    # Initialisation de Ivy
    IvyInit("AVI_FGS", "Ready", 0, void_function, void_function)
    IvyStart("127.255.255.255:2010")
    IvyBindMsg(on_axis, '^Axis x=(\S+) y=(\S+) chi=(\S+)')
    sleep(0.5) # délai pour Ivy (ne fonctionne pas sans)

    # Cas 1 : avion trop loin d'un point du PDV
    print(f"{Fore.GREEN}Cas 1 :{Fore.RESET} avion trop loin d'un point du PDV")
    input("[enter] pour continuer : ")
    p0 = Point(-3000, -5000)
    run_ivy(p0)
    
    # Cas 2 : Rejointe du premier point du plan de vol
    print(f"{Fore.GREEN}Cas 2 :{Fore.RESET} Rejointe du plan de vol")
    input("[enter] pour continuer : ")
    # p0 = Point(-3000, -580)
    p0 = Point(0,-10600)
    run_ivy(p0)

    # Cas 3 : Envoi de l'axe suivant en anticipation (fly-by)
    print(f"{Fore.GREEN}Cas 3 :{Fore.RESET} Envoi de l'axe suivant pour en anticipation")
    input("[enter] pour continuer : ")
    # -2069,10656
    p0 = Point(-2100, 9800)
    run_ivy(p0)

    # Cas 4 : Envoi de l'axe suivant pour un fly-over
    print(f"{Fore.GREEN}Cas 4 :{Fore.RESET} Envoi de l'axe suivant pour un fly-over")
    input("[enter] pour continuer : ")
    p0 = Point(1824, 10000)
    run_ivy(p0)

    IvyStop()