from ivy.std_api import *

IvyInit("Test", "[%s ready]", 0, lambda x,y: 1, lambda x,y: 1)
IvyStart("10.1.127.255:2012")
IvySendMsg("Test aaa=brazil_est_un_crack bbb=azgazdg")
IvyStop()