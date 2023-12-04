import time
from ivy.std_api import *

def callback(agent, *data):
    print(f"Ivy message received: {data}")

def send_bank_angle(state_vector):
    # Extraire la vitesse de manoeuvre et l'angle de braquage du vecteur d'état
    maneuvering_speed = state_vector['maneuvering_speed']
    current_bank_angle = state_vector['bank_angle']
    
    # Calculer l'angle de braquage en fonction des règles spécifiées
    calculated_bank_angle = calculate_bank_angle(maneuvering_speed)
    
    # Vérifier si l'angle de braquage calculé dépasse la limite actuelle
    if calculated_bank_angle > current_bank_angle:
        # Mise à jour de l'angle de braquage maximal dans le vecteur d'état
        state_vector['bank_angle'] = calculated_bank_angle
    
    # Envoyer l'angle de braquage ajusté sur le bus Ivy
    IvySendMsg(f"^Test bank_angle={state_vector['bank_angle']}")

def simulate_flight():
    time_elapsed = 0
    while time_elapsed <= 3600:  # Simulation du vol pendant 1 heure (3600 secondes)
        # Simulation d'un vecteur d'état (à remplacer par vos données réelles)
        state_vector = {'maneuvering_speed': calculate_maneuvering_speed(time_elapsed), 'bank_angle': 25}
        
        # Envoi du vecteur d'état sur le bus Ivy
        send_bank_angle(state_vector)

        time.sleep(10)  # Attente de 10 secondes entre chaque mise à jour
        time_elapsed += 10

def calculate_maneuvering_speed(time_elapsed):
    # Logique de calcul de la vitesse de manoeuvre en fonction du temps
    # Ici, une simple fonction de démonstration est utilisée. Vous devrez adapter cela à votre logique spécifique.
    return 150 + 2 * (time_elapsed / 3600)  # Exemple de variation de la vitesse de manoeuvre au fil du temps

def calculate_bank_angle(maneuvering_speed):
    # Règles spécifiées pour l'angle de braquage en fonction de la vitesse de manoeuvre
    if maneuvering_speed <= 10:
        return 15
    elif maneuvering_speed <= (maneuvering_speed - 3):
        return 25
    else:
        # Choix entre la guidance latérale sélectionnée et gérée
        if selected_lateral_guidance:
            return 25
        else:
            return 30

# Définir la variable pour la guidance latérale sélectionnée (à remplacer par vos données réelles)
selected_lateral_guidance = True

nh = lambda _x, _y: 1

IvyInit("Test",
    "[%s ready]",
    0,
    nh,
    nh
)

IvyBindMsg(callback, '^Test aaa=(\S+')
IvyStart("127.255.255.255:2010")

# Lancer la simulation du vol
simulate_flight()

IvyStop()
