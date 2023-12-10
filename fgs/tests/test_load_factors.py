from ivy.std_api import IvyInit, IvyStart, IvyBindMsg, IvyMainLoop, IvyStop

def null_cb(*a):
    pass

def on_loadfactors(agent, *data):
    print("Load factors received: {}".format(data))

def test_loadfactors():
    # Initialisation Ivy avec des fonctions de rappel vides
    IvyInit("TestLoadFactors", "[%s ready]", 0, null_cb, null_cb)
    IvyStart("10.1.127.255:2012")

    # Liaison de la fonction de rappel à un motif de message Ivy correspondant à loadfactors.py
    IvyBindMsg(on_loadfactors, "^NxControl nx_max=(\S+) nx_min=(\S+) nz_max=(\S+) nz_min=(\S+) NxAPControl nxAP=(\S+) NzAPControl nzAP=(\S+)")

    # Appel de la fonction à tester
    loadfactors()

    # Boucle principale Ivy pour attendre les messages
    IvyMainLoop()

    # Arrêt d'Ivy après la boucle principale
    IvyStop()

if __name__ == "__main__":
    test_loadfactors()
