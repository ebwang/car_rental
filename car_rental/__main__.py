# Arquivo de entrada principal
import os
import sys

from car_rental.cli import main

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Incializador principal #
if __name__ == "__main__":
    main()
