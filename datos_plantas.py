import random
import time
def generar_datos():
    temperatura = random.randit(18,30)
    humedad = random.randit(200, 800)
    luz = random.randit(300, 1000)
    tamaño = random.randit(1, 100)
    return temperatura, humedad, luz, tamaño

def mostrar_datos(temperatura, humedad, luz, tamaño):
    print("---Datos de la planta---")
    print("Temperatura ideal:", temperatura, "°C")
    print("Humedad ideal:", humedad, "%")
    print("Luz ideal:", luz)
    print("Tamaño ideal:", tamaño)

def main():
    while True:
        temperatura, humedad, luz, tamaño = generar_datos()
        mostrar_datos(temperatura, humedad, luz, tamaño)
        time.sleep(5)

main()

