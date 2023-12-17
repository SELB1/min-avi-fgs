from ivy.std_api import *
from time import sleep
from colorama import Fore
import matplotlib.pyplot as plt

from fgs.defs import Point, get_flightplan, M_TO_FT

def plot_flight(flightplan):
    # Tracé du plan de vol et des axes
    plt.figure(figsize=(10, 10))

    # Tracé du plan de vol
    for point in flightplan:
        if point.z>0:
            plt.plot(point.y, point.x, marker='o', color='blue')
            plt.annotate(f"{point.z}m", (point.y, point.x))
        else:
            plt.plot(point.y, point.x, marker='x', color='black')

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

def run_ivy(p0:Point, fp_path="data/flightplan.csv"):
    # Charger le plan de vol
    flightplan = get_flightplan(fp_path)
    # Afficher le plan de vol
    plot_flight(flightplan)

    plt.plot(p0.y, p0.x, 'go', label="Position de l\'avion")

    IvySendMsg(f"StateVector x={p0.x} y={p0.y} z=0 Vp=69 fpa=0 psi=0 phi=0")
    plt.show()

def on_alts(agent, *data):
  plt.annotate(f"Consigne : {float(data[0])/M_TO_FT}", (-1500, -2000))

def run():
    IvyInit("Altitudes", "[%s ready]", 0, void_function, void_function)
    IvyStart("127.255.255.255:2010")
    sleep(0.1)
    IvyBindMsg(on_alts, '^ManagedAlt alt=(\S+) Q=(\S+)')

    # Cas 1 : Avion trop loin du point du plan de vol
    print(f"{Fore.GREEN}Cas 1 :{Fore.RESET} avion trop loin d'un point du PDV")
    input("[enter] pour continuer : ")
    p0 = Point(-2000, 5000)
    run_ivy(p0)

    # Cas 2 : Avion près d'un point avec une altitude négative
    print(f"{Fore.GREEN}Cas 2 :{Fore.RESET} avion près d\'un point avec une altitude non saisie")
    input("[enter] pour continuer : ")
    p0 = Point(350, -3500)
    run_ivy(p0)

    # Cas 3 : Rejointe du plan de vol
    print(f"{Fore.GREEN}Cas 3 :{Fore.RESET} Rejointe du plan de vol")
    input("[enter] pour continuer : ")
    p0 = Point(-2000, 10000)
    run_ivy(p0)

    # Cas 4 : Dernier point
    print(f"{Fore.GREEN}Cas 4 :{Fore.RESET} Dernier point")
    input("[enter] pour continuer : ")
    p0 = Point(1200, 2500)
    run_ivy(p0)

    IvyStop()
