#!/usr/bin/env python3
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from os import system
from scriptsDB.createTableAndDB import createTable

try:
    print("Bienvenido a la cli")
    
except Exception as e:
    system("./uiMware/bins/cleanProject.sh")
    