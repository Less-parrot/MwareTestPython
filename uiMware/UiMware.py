#!/usr/bin/env python3
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

import flet as ft

from controllers.NavHostController import main
from os import system
from scriptsDB.createTableAndDB import createTable

try:
    ft.app(target=main, assets_dir="assets") # Iniciamos la UI y ponemos la carpeta assets        
except KeyboardInterrupt:
    system("./uiMware/bins/cleanProject.sh")
        