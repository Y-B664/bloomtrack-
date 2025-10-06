import pandas as pd  
df = pd.read_csv("datasets/Inventario plantas/Dataset plantas.csv", encoding="ISO-8859-1",usecols=['Id','Nombre','Temperatura ideal','Humedad ideal','Luz ideal','Tamaño'])
def buscarPlanta(nombrePlanta):
    planta=df[df["Nombre"]==nombrePlanta]
    print(planta)


buscarPlanta("Aglonema Silver")



def nombre_planta():
    nombre=input("Ingresa el nombre de la planta: "))
    return nombre

def recoger_datos():
    datos=generar_datos()
    entradas=tuples(datos)
    return entradas 


def comparar_datos():
    comparar=recoger_datos()
    



