from flask import Blueprint, request, jsonify
import  pandas as pd
import os

datasets_bluep = Blueprint("datasets", __name__)

@datasets_bluep.route("/cargar_dataset", methods=['POST'])

def cargar_dataset():
    info= request.get_json()
    print(info)
    Nombre = info.get("Nombre")


    if not Nombre:
        return jsonify({"Error": "Falta colocar el nombre de la planta"}), 400
    
    ruta = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "dataset", "inventario_plantas.csv"))
    print(f"Buscando dataset en: ", ruta)

    
    if not os.path.exists(ruta):
        return jsonify({"error": f"No se encontro el archivo inventario_plantas.csv"}), 404
    
    df = pd.read_csv(ruta, encoding='latin1')
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    df_filtrado =df[df["Nombre"].str.lower() ==Nombre.lower()]
    
    if df_filtrado.empty:
        return jsonify({"error": f"No se encontró información para la planta '{Nombre}'"}), 404
    

    return jsonify({
        "Mensaje":f"Datos de la planta {Nombre} cargado correctamente",
        "datos": df_filtrado.to_dict(orient="records")
    }), 200

    