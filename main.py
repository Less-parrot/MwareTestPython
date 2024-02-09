#!/usr/bin/env python3
from os import system

class Cli:
    
    def Options():
        ask = str(input("Escoja el entirno que desea utilizar [ui/cli]: "))
        if ask == "ui":
            system("cd ui;clear;./bins/UiMainFlet; cd ..")
        elif ask == "cli":
            system("clear")
            print("Bienvenido a la cli")
            exit() 
    
Cli.Options()
