from ivy.std_api import *

def null_cb(*a):
  pass

def on_alts(agent, *data):
  #global recorded data
  #recorded_data = data[0]
  print("alt={}".format(data[0]))

IvyInit("Altitudes", "[%s ready]", 0, null_cb, null_cb)
IvyStart("10.1.127.255:2012")

IvyBindMsg(on_alts, "^Altitudes are (\S+)")
IvyMainLoop()
