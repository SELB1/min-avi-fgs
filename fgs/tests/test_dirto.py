from ivy.std_api import IvyInit, IvyStart, IvyBindMsg, IvyMainLoop, IvyStop

def null_cb(*a):
    pass

def on_dirto(agent, *data):
    print("DIRTO received: {}".format(data[0]))

def test_dirto():
    # Initialisation Ivy avec des fonctions de rappel vides
    IvyInit("TestDirto", "[%s ready]", 0, null_cb, null_cb)
    IvyStart("10.1.127.255:2012")

    # Liaison de la fonction de rappel à un motif de message Ivy correspondant à la fonction on_dirto
    IvyBindMsg(on_dirto, "^DIRTO x=(\S+) y=(\S+)")

    # Boucle principale Ivy pour attendre les messages
    IvyMainLoop()

    # Arrêt d'Ivy après la boucle principale
    IvyStop()

if __name__ == "__main__":
    test_dirto()
