"""
Nombre del Alumno: Rubén Emiliano Melchor Villa
Matricula: UX25II324
Fecha: 25/05/26
Examen segundo parcial-Programacion Estructurada
"""

#importacion de las 5 librerias a uso del examen 

import datetime
import math
import random
import statistics
import sys

#definicion de constantes 
MAX_EPOCHS = 10
UMBRAL_ERROR_CRITICO =0.95

def obtener_info_sistema():
    print("--informacion del sistema del usuario--")
    print("plataforma" , sys.platform)
    print("version de python", sys.version)
    print("argumentos recibidos", sys.argv)
    print("salida", sys.exit(1))
    