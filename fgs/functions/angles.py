"""
Donne phi_max et p_max
"""

import time
from ivy.std_api import *

def callback(agent, *data):
    print(f"Ivy message received: {data}")

def send_angle_max(state_vector):
    # Extraire l'angle de votre vecteur d'état
    angle_max = state_vector['angle']
    
    # Envoyer l'angle_max sur le bus Ivy
    IvySendMsg(f"^Test angle_max={angle_max}")

def simulate_flight():
    time_elapsed = 0
    while time_elapsed <= 3600:  # Simulation du vol pendant 1 heure (3600 secondes)
        # Simulation d'un vecteur d'état (à remplacer par vos données réelles)
        state_vector = {'angle': calculate_angle_max(time_elapsed)}
        
        # Envoi du vecteur d'état sur le bus Ivy
        send_angle_max(state_vector)

        time.sleep(10)  # Attente de 10 secondes entre chaque mise à jour
        time_elapsed += 10

def calculate_angle_max(time_elapsed):
    # Logique de calcul de l'angle_max en fonction du temps et de la position de l'avion
    # Ici, une simple fonction de démonstration est utilisée. Vous devrez adapter cela à votre logique spécifique.
    return 15 + 5 * (time_elapsed / 3600)  # Exemple de variation de l'angle_max au fil du temps

nh = lambda _x, _y: 1

IvyInit("Test",
    "[%s ready]",
    0,
    nh,
    nh
)

IvyBindMsg(callback, '^Test aaa=(\S+)')
IvyStart("127.255.255.255:2011")

# Lancer la simulation du vol
simulate_flight()

IvyStop()
