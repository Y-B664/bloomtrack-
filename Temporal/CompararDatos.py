import pandas as pd  
import datos_plantas
df = pd.read_csv("datasets/Inventario plantas/Dataset plantas.csv", encoding="ISO-8859-1",usecols=['Id','Nombre','Temperatura ideal','Humedad ideal','Luz ideal','Tamaño'])
def buscar_planta(nombrePlanta):
    planta=df[df["Nombre"]==nombrePlanta]
    print(planta)
    if planta.empty:
        return None
    else:
        return planta.iloc[0]


def nombre_planta():
    nombre=input("Ingresa el nombre de la planta: ")
    return nombre

def recoger_datos():
    datos=datos_plantas.generar_datos()
    print("datos traidos",datos)
    return datos

def comparar_datos():
    planta=buscar_planta(nombre_planta())
    comparar=recoger_datos()
    
    if planta is None:
        return
    else:
        for clave in comparar:
            print(clave)
            if comparar[clave] == planta[clave]:
                print("Tu planta crece muy bien!")
            else:
                print("Ten cuidado!")    



comparar_datos()

