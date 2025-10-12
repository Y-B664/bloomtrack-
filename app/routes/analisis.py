from flask import Blueprint, jsonify
import pandas as pd
import random
import os

analisis_bluep = Blueprint("analisis", __name__)

ruta_dataset = os.path.join(os.path.dirname(__file__), "../dataset/inventario_plantas.csv")

dataset_ref=pd.read_csv(ruta_dataset, encoding="ISO-8859-1",
                     usecols=['Id','Nombre','Temperatura ideal','Humedad ideal','Luz ideal','Tamaño'])

#Llamar las temperaturas ideales
temp_ideal = dataset_ref.loc[0, "Temperatura ideal"]
hum_ideal= dataset_ref.loc[0, "Humedad ideal"]
luz_ideal =dataset_ref.loc[0, "Luz ideal"]
tam_ideal = dataset_ref.loc[0, "Tamaño"]

TOLERANCIA = 20


##datos aleatorios en sensores
def sensores():
    temp = round(random.uniform(15, 35), 2)
    hum = round(random.uniform(200, 800), 2)
    luz = round(random.uniform(200, 1000), 2)
    tam = round(random.uniform(5, 100), 2)
    return temp, hum, luz, tam

#Analisis de lso  datos
def analizar(temp,hum, luz, tam):
    estado = {}
    diferencias ={}

                  ##TEMPERATURA-----------
    dif_temp = temp - temp_ideal
    if abs(dif_temp) <= TOLERANCIA:
        estado["estado_temp"] = f"Temperatura ideal ({temp})"
    elif dif_temp < 0:
        estado["estado_temp"] = f"Temperatura baja ({temp})"
    else:
        estado["estado_temp"] = f"Temperatura alta ({temp})"
    diferencias["diferencia_temp"] =f"{dif_temp:+.2f}  respecto al ideal ({temp_ideal} )"

                   ##HUMEDAD------------
    dif_hum = hum - hum_ideal
    if abs(dif_hum) <= TOLERANCIA:
        estado["estado_hum"] = f"Humedad ideal ({hum})"
    elif dif_hum < 0:
        estado["estado_hum"] = f"Humedad baja ({hum})"
    else:
        estado["estado_hum"] = f"Humedad alta ({hum})"
    diferencias["diferencia_hum"] =f"{dif_hum:+.2f}  respecto al ideal ({hum_ideal})"

                    ##LUZ----------------
    dif_luz = luz - luz_ideal                                        
    if abs(dif_luz) <= TOLERANCIA:
        estado["estado_luz"] = f"Luz ideal ({luz})"
    elif dif_luz < 0:
        estado["estado_luz"] = f"Luz baja ({luz})"
    else:
        estado["estado_luz"] = f"Luz alta ({luz})"
    diferencias["diferencia_luz"] =f"{dif_luz:+.2f} respecto al ideal ({luz_ideal})"

                ##TAMAÑO-------------
    dif_tam=tam - tam_ideal
    if abs(dif_tam) <= TOLERANCIA:
        estado["estado_tam"] = f"Tamano ideal ({tam} cm)"
    elif dif_tam < 0:
        estado["estado_tam"] = f"Tamano bajo ({tam} cm)"
    else:
        estado["estado_tam"] = f"Tamano alto ({tam} cm)"
    diferencias["diferencia_tam"] =f"{dif_tam:+.2f} cm respecto al ideal ({tam_ideal}) cm"

    return estado, diferencias    
    

   ##Obtener datos en tiempo real y monitorearlos------ 
@analisis_bluep.route("/datos")
def datos():
    temp, hum, luz, tam = sensores()
    estado, diferencias = analizar(temp, hum, luz, tam)
    return jsonify({
        "Datos sensor": {
            "temperatura": temp,
            "humedad": hum,
            "luz": luz,
            "tamano": tam
        },
        "estado": estado,
        "diferencias": diferencias
    })
