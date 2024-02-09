#!/usr/bin/env python3
from os import system

class Cli:
    
    def Options():
        ask = str(input("Escoja el entirno que desea utilizar [ui/cli]: "))
        if ask == "ui":
            system("clear;./uiMware/UiMware.py")
        elif ask == "cli":
            system("clear;./cliMware/CliMware.py")
        else:
            exit() 
    
Cli.Options()
