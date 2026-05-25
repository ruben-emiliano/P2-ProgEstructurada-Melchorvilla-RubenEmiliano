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
UMBRAL_ERROR_CRITICO = 0.95

#obtenemos la informacion del dispositivo del usuario mediante la libreria sys
def obtener_info_sistema():
    print("--informacion del sistema del usuario--")
    print("plataforma", sys.platform)
    print("version de python", sys.version)
    print("argumentos recibidos", sys.argv)

def simular_metricas_entrenamiento(cantidad_epochs):

    inicio = datetime.datetime.now()

    print("inicio de simulacion:",
          inicio.strftime("%d/%m/%Y %H:%M:%S"))

    lista_loss = []
    lista_latencia = []

    eventos = [
        "Epoch exitoso",
        "Gradiente inestable",
        "Actualizacion de pesos"
    ]

    contador = 1

    while contador <= cantidad_epochs:

        # random.uniform()
        loss = random.uniform(0.1, 1.0)

        # random.random()
        probabilidad = random.random()

        # random.choice()
        evento = random.choice(eventos)

        latencia = random.uniform(0.5, 2.0)

        lista_loss.append(loss)
        lista_latencia.append(latencia)

        print("epoch:", contador)
        print("loss:", round(loss, 3))
        print("probabilidad:", round(probabilidad, 3))
        print("evento:", evento)
        print("latencia:", round(latencia, 2))
        print("--------------------")

        contador += 1

    fin = datetime.datetime.now()

    print("fin de simulacion:",
          fin.strftime("%d/%m/%Y %H:%M:%S"))

    tiempo_total = fin - inicio

    print("tiempo transcurrido:", tiempo_total)

    return lista_loss, lista_latencia

def analizar_rendimiento(lista_loss, lista_latencia):

    print("analisis de entrenamiento")

    # statistics.mean()
    promedio_loss = statistics.mean(lista_loss)

    # statistics.stdev()
    desviacion = statistics.stdev(lista_loss)

    # statistics.median()
    mediana_latencia = statistics.median(lista_latencia)

    print("promedio de loss:", round(promedio_loss, 3))
    print("desviacion estandar:", round(desviacion, 3))
    print("mediana de latencia:", round(mediana_latencia, 3))

def calcular_rmse(predicciones, reales):

    suma = 0
    contador = 0

    while contador < len(predicciones):

        diferencia = predicciones[contador] - reales[contador]

        # math.pow()
        cuadrado = math.pow(diferencia, 2)

        suma += cuadrado

        contador += 1

    promedio = suma / len(predicciones)

    # math.sqrt()
    rmse = math.sqrt(promedio)

    # math.ceil()
    rmse_final = math.ceil(rmse)

    print("RMSE:", rmse_final)

    return rmse_final

def main():

    obtener_info_sistema()

    lista_loss, lista_latencia = simular_metricas_entrenamiento(MAX_EPOCHS)

    analizar_rendimiento(lista_loss, lista_latencia)

    predicciones = [0.9, 0.8, 0.7, 0.6]
    reales = [1.0, 0.7, 0.8, 0.5]

    calcular_rmse(predicciones, reales)

    if statistics.mean(lista_loss) > UMBRAL_ERROR_CRITICO:
        print("Error critico detectado")
        sys.exit()

if __name__ == "__main__":
    print("=== INICIANDO SIMULADOR DE AGENTES DE IA ===")
    main()