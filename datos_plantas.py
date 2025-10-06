import random
import time
def generar_datos():
    datos = {'Temperatura ideal' : random.randint(18,30),
    'Humedad ideal':  random.randint(200, 800),
    'Luz ideal' : random.randint(300, 1000),
    'Tamaño' : random.randint(1, 100)}
    
    return datos

def mostrar_datos(temperatura, humedad, luz, tamaño):
    print("---Datos de la planta---")
    print("Temperatura ideal:", temperatura, "°C")
    print("Humedad ideal:", humedad, "%")
    print("Luz ideal:", luz)
    print("Tamaño ideal:", tamaño)

def main():
    while True:
        temperatura, humedad, luz, tamaño = generar_datos()
     #   mostrar_datos(temperatura, humedad, luz, tamaño)
        time.sleep(1200)



