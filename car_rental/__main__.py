# Arquivo de entrada principal
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from car_rental.cli import main

# Incializador principal #
if __name__ == '__main__':
    main()
