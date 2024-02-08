#!/usr/bin/env python3

import flet as ft

from controllers.NavHostController import main
from os import system
from db.createTableAndDB import createTable


if __name__ == "__main__":
    try:
        ft.app(target=main, assets_dir="assets") # Iniciamos la UI y ponemos la carpeta assets        
    except KeyboardInterrupt:
        system("./bins/cleanProject.sh")