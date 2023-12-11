from ivy.std_api import IvyInit, IvyStart, IvyBindMsg, IvyMainLoop, IvyStop
from fgs.defs import StateVector

def null_cb(*a):
    pass

def on_roll_limits(agent, *data):
    print("Roll limits received: {}".format(data))

def test_send_bank_angle():
    # Simuler un StateVector pour tester la fonction send_bank_angle
    test_state_vector = StateVector(x=0.0, y=0.0, z=0.0, Vp=150.0, fpa=0.0, psi=0.0, phi=0.0)

    # Initialisation Ivy avec des fonctions de rappel vides
    IvyInit("TestSendBankAngle", "[%s ready]", 0, null_cb, null_cb)
    IvyStart("127.255.255.255:2010")

    # Liaison de la fonction de rappel à un motif de message Ivy
    IvyBindMsg(on_roll_limits, "^RollLimits phimax=(\S+) pmax=(\S+)")

    # Appel de la fonction à tester
    send_bank_angle(test_state_vector)

    # Boucle principale Ivy pour attendre les messages
    IvyMainLoop()

    # Arrêt d'Ivy après la boucle principale
    IvyStop()

if __name__ == "__main__":
    test_send_bank_angle()
