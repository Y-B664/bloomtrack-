from flask import Flask, render_template
from routes.datasets import datasets_bluep
from routes.analisis import analisis_bluep
from routes.datos import datos_bluep
import pandas as pd
import random
import os

app=Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'

app.register_blueprint(datasets_bluep)
app.register_blueprint(analisis_bluep)
app.register_blueprint(datos_bluep)

ruta_csv = os.path.join(os.path.dirname(__file__), "..", "app", "dataset", "inventario_plantas.csv")
data = pd.read_csv(ruta_csv, encoding="latin-1")


data = data.dropna(axis=1, how='all')


print("Columnas del dataset:", list(data.columns))
print("Primeras filas:")
print(data.head())


@app.route("/comparar")
def comparar_datos():
    resultados = []

    for _, fila in data.iterrows():
        nombre = fila["Nombre"]

        temp_ideal = fila["Temperatura ideal"]
        hum_ideal = fila["Humedad ideal"]
        luz_ideal = fila["Luz ideal"]


        temp_sim = random.uniform(temp_ideal - 18, temp_ideal + 30)
        hum_sim = random.uniform(hum_ideal - 200, hum_ideal + 800)
        luz_sim = random.uniform(luz_ideal - 300, luz_ideal + 1000)


        if (
            abs(temp_sim - temp_ideal) <= 2 and
            abs(hum_sim - hum_ideal) <= 5 and
            abs(luz_sim - luz_ideal) <= 50
        ):
            condicion = "Ideal"
        else:
            condicion = "Fuera de rango"

        resultados.append({
            "Nombre": nombre,
            "Temperatura simulada": round(temp_sim, 2),
            "Humedad simulada": round(hum_sim, 2),
            "Luz simulada": round(luz_sim, 2),
            "Condición": condicion
        })

    return render_template("comparar.html", resultados=resultados)

if __name__ == "__main__":
    app.run(debug=True)


