#!/usr/bin/env python3
from os import system
from cliMware.CliMware import main

class Cli:
    
    def Options():
        ask = str(input("Escoja el entirno que desea utilizar [ui/cli]: "))
        if ask == "ui":
            system("cd uiMware;clear;./bins/uiMware; cd ..")
        elif ask == "cli":
            system("clear")
            main()
            exit() 
    
Cli.Options()
