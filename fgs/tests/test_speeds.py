from ivy.std_api import IvyInit, IvyStart, IvyBindMsg, IvyMainLoop, IvyStop

def null_cb(*a):
    pass

def on_speeds(agent, *data):
    print("Speeds received: {}".format(data))

if __name__ == "__main__":
    IvyInit("TestSpeeds", "[%s ready]", 0, null_cb, null_cb)
    IvyStart("10.1.127.255:2012")

    IvyBindMsg(on_speeds, "^SpeedLimits vmin=(\S+) vmax=(\S+)")

    IvyMainLoop()
