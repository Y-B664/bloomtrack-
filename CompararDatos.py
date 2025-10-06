import pandas as pd  
df = pd.read_csv("datasets/Inventario plantas/Dataset plantas.csv", encoding="ISO-8859-1",usecols=['Id','Nombre','Temperatura ideal','Humedad ideal','Luz ideal','Tamaño'])
def buscarPlanta(nombrePlanta):
    planta=df[df["Nombre"]==nombrePlanta]
    print(planta)


buscarPlanta("Aglonema Silver")