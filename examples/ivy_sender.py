from ivy.std_api import *
from time import sleep

IvyInit("Test", "[%s ready]", 0, lambda x,y: 1, lambda x,y: 1)
IvyStart("127.255.255.255:2012")
sleep(0.1)
IvySendMsg("Test aaa=3.2")
IvyStop()