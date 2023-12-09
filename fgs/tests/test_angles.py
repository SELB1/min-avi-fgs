from ivy.std_api import IvyInit, IvyStart, IvyBindMsg, IvyMainLoop, IvyStop

def null_cb(*a):
    pass

def on_dirto(agent, *data):
    print("DIRTO received: {}".format(data[0]))

if __name__ == "__main__":
    IvyInit("TestDirto", "[%s ready]", 0, null_cb, null_cb)
    IvyStart("10.1.127.255:2012")

    IvyBindMsg(on_dirto, "^DIRTO x=(\S+) y=(\S+)")

    IvyMainLoop()
