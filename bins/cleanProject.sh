#!/bin/bash

# Define el directorio actual como el directorio base del proyecto.
PROYECTO_RUTA="."

find "$PROYECTO_RUTA" -type d -name "__pycache__" -exec rm -rf {} +

