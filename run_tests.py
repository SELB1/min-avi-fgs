import argparse
from colorama import Fore

import fgs.tests as t

parser = argparse.ArgumentParser(
    prog="FGS test suite",
    description="Run FGS tests"
)
parser.add_argument('name', help="Test to run", choices=("axis", "alt"), default="axis")
args = parser.parse_args()

match args.name:
    case "axis":
        t.test_axis.run()
    case "alt":
        t.test_alt.run()