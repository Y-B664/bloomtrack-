from flask import Blueprint, request, jsonify
import  pandas as pd
import os

datasets_bluep = Blueprint("datasets", __name__)

@datasets_bluep.route("/cargar_dataset", methods=['POST'])

def cargar_dataset():
    #recibir el nombre de la planta
    info= request.get_json()
    Nombre = info.get("Nombre")


    if not Nombre:
        return jsonify({"Error": "Falta colocar el nombre de la planta"}), 400
    
    #Buscar el dataset 
    ruta = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "dataset", "inventario_plantas.csv"))
    print(f"Buscando planta en: ", ruta)

    
    if not os.path.exists(ruta):
        return jsonify({"error": f"No se encontro el archivo de las plantas"}), 404
    
    #Cargar lso datos correspondientes

    df = pd.read_csv(ruta, encoding='latin1')

    #Eliminar las comulas con datos vacios 
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    #Buscar por el nombre de la planta
    df_planta =df[df["Nombre"].str.lower() ==Nombre.lower()]
    
    if df_planta.empty:
        return jsonify({"error": f"No se encontro informacion de la planta '{Nombre}'"}), 404
    
    #Mostrar lso daots de la planta correspondiente
    return jsonify({
        "Mensaje":f"Datos de la planta {Nombre} cargado correctamente",
        "datos": df_planta.to_dict(orient="records")
    }), 200

    