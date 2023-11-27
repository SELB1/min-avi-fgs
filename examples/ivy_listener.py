from ivy.std_api import *

def callback(agent, *data):
    print(f"ivy message received : {data}")

nh = lambda _x,_y: 1

IvyInit("Test",
    "[%s ready]",
    0,
    nh,
    nh
)
IvyBindMsg(callback, '^Test aaa=(\S+)')
IvyStart("127.255.255.255:2010")
IvyMainLoop()
IvyStop()