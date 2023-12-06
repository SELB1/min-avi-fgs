from fgs.main import bind_messages, init_fgs
from ivy.std_api import *

def main():
    IvyInit("AVI_FGS", "Ready", 0, void_function, void_function)
    IvyStart("127.255.255.255:2010")

    bind_messages()
    init_fgs()
    IvyMainLoop()



if __name__ == "__main__":
    main()