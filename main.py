#!/usr/bin/env python3

import argparse
import flet as ft

from controllers.NavHostController import main
from cliTest.clientSocket import ClientSocketConnection
from os import system

def parse_arguments():
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-ip', '--parameter', help='Description of parameter')
    return parser.parse_args()

if __name__ == "__main__":
    try:
        args = parse_arguments()


        if args.parameter:
            ipServerConnection = args.parameter
            ClientSocketConnection(ipServerConnection)

        else:
            args.parameter = "192.168.100.242"
            ipServerConnection = args.parameter
            ClientSocketConnection(ipServerConnection)

        ft.app(target=main, assets_dir="assets") # Iniciamos la UI y ponemos la carpeta assets
        system("./bins/cleanProject.sh")
        
    except KeyboardInterrupt:

        system("./bins/cleanProject.sh")