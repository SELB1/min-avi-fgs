from fgs.main import bind_messages, init_fgs
from ivy.std_api import *
from colorama import Fore
import argparse

import fgs.globals as fg

parser = argparse.ArgumentParser(
    prog="FGS",
    description="Connects to the Ivy bus and sends the messages according to specs"
)
parser.add_argument('-b', dest="ivy_address", help="Ivy bind adress (127.255.255.255:2010 by default)", default="127.255.255.255:2010")
parser.add_argument('-p', dest="fp_path", help="Path to the CSV flightplan (data/flightplan.csv by default)", default="data/flightplan.csv")
args = parser.parse_args()

def main():
    with open("data/art.txt", "r") as f:
        print(f.read())
        
    IvyInit("AVI_FGS", "Ready", 0, void_function, void_function)
    IvyStart(args.ivy_address)
    fg.FP_PATH = args.fp_path
    print(f"[*] {Fore.LIGHTBLUE_EX}Ivy started on {args.ivy_address}{Fore.RESET}")

    bind_messages()
    init_fgs()
    IvyMainLoop()

if __name__ == "__main__":
    main()