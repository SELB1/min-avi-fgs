from fgs.main import bind_messages, init_fgs
from ivy.std_api import *
from colorama import Fore
import argparse

parser = argparse.ArgumentParser(
    prog="FGS",
    description="Connects to the Ivy bus and sends the messages according to specs"
)
parser.add_argument('-b', dest="ivy_address", help="Ivy bind adress", default="127.255.255.255:2010")
args = parser.parse_args()

def main():
    IvyInit("AVI_FGS", "Ready", 0, void_function, void_function)
    IvyStart(args.ivy_address)
    print(f"[*] {Fore.LIGHTBLUE_EX}Ivy started on {args.ivy_address}{Fore.RESET}")

    bind_messages()
    init_fgs()
    IvyMainLoop()

if __name__ == "__main__":
    main()