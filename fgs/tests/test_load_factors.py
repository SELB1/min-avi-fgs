from ivy.std_api import IvyInit, IvyStart, IvyBindMsg, IvyMainLoop, IvyStop

def null_cb(*a):
    pass

def on_loadfactors(agent, *data):
    print("Load factors received: {}".format(data))

if __name__ == "__main__":
    IvyInit("TestLoadFactors", "[%s ready]", 0, null_cb, null_cb)
    IvyStart("10.1.127.255:2012")

    IvyBindMsg(on_loadfactors, "^NxControl nx_max=(\S+) nx_min=(\S+) nz_max=(\S+) nz_min=(\S+)")

    IvyMainLoop()
