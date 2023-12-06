import matplotlib.pyplot as plt
import numpy as np
from math import atan2, degrees, radians

class Point:
    def __init__(self, x, y, fly_by=False, fly_over=False):
        self.x = x
        self.y = y
        self.fly_by = fly_by
        self.fly_over = fly_over

class Axis:
    def __init__(self, first: Point, second: Point):
        self.chi = atan2(second.x - first.x, second.y - first.y)
        self.p0 = first

def get_flightplan(path="./../../data/flightplan.csv"):
    res = []
    with open(path, "r") as f:
        for line in f:
            t = line.rstrip().split(',')
            res.append(Point(float(t[1]), float(t[2]), t[0]))
    return res

def get_closest_axis(current_position, axes):
    # Trouve l'axe le plus proche de la position actuelle de l'avion
    closest_axis = min(axes, key=lambda axis: (axis.p0.x - current_position.x)**2 + (axis.p0.y - current_position.y)**2)
    return closest_axis

def check_alignment(current_axis, current_position, tolerance=5.0):
    # Vérifie si l'avion est aligné avec l'axe de consigne
    angle_difference = abs(current_axis.chi - atan2(current_position.x - current_axis.p0.x, current_position.y - current_axis.p0.y))
    return angle_difference < radians(tolerance)

def plot_flight(flightplan, axes, current_position):
    # Tracé du plan de vol et des axes
    plt.figure(figsize=(10, 10))

    # Tracé du plan de vol
    for point in flightplan:
        if point.fly_by:
            plt.plot(point.x, point.y, marker='o', color='red', label='Fly By')
        elif point.fly_over:
            plt.plot(point.x, point.y, marker='x', color='blue', label='Fly Over')
        else:
            plt.plot(point.x, point.y, marker='o', color='black')

    # Tracé des axes
    for axis in axes:
        plt.plot([axis.p0.x, axis.p0.x + np.cos(axis.chi)], [axis.p0.y, axis.p0.y + np.sin(axis.chi)], label=f'Axe {axis.p0.x}-{axis.p0.y}')

    # Marquer la position actuelle de l'avion
    plt.scatter([current_position.x], [current_position.y], color='green', label='Position actuelle')

    plt.legend()
    plt.xlabel('Position X')
    plt.ylabel('Position Y')
    plt.title('Plan de vol avec axes')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Charger le plan de vol et les axes de consigne
    flightplan = get_flightplan()
    axes = [Axis(flightplan[i], flightplan[i+1]) for i in range(len(flightplan)-1)]

    # Position actuelle de l'avion (à remplacer par les données de votre simulation)
    current_position = Point(-3552, -9204)

    # Vérifier l'alignement et afficher le tracé
    closest_axis = get_closest_axis(current_position, axes)
    if check_alignment(closest_axis, current_position):
        print("L'avion est aligné avec l'axe de consigne.")
    else:
        print("L'avion n'est pas aligné avec l'axe de consigne.")

    # Afficher le tracé
    plot_flight(flightplan, axes, current_position)
