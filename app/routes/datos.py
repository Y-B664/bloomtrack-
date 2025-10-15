from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
import pandas as pd
import os
from analisis import sensores

datos_bluep = Blueprint("datos", __name__)

dataset_path = os.path.join(os.path.dirname(__file__), "../dataset/inventario_plantas.csv")

if not os.path.exists(dataset_path):
    print(" No se encontró el archivo del dataset en la ruta:", dataset_path)
    data = pd.DataFrame()  
else:
    print(" Dataset cargado desde:", dataset_path)
    data = pd.read_csv(dataset_path, encoding="latin-1")
    data = data[['Nombre', 'Temperatura ideal', 'Humedad ideal', 'Luz ideal']]

@datos_bluep.route('/')
def index():
    plantas_lista = sorted(data['Nombre'].dropna().unique().tolist()) if not data.empty else []
    return render_template("comparardatosingresados.html", plantas=plantas_lista)

@datos_bluep.route('/comparar', methods=['GET', 'POST'])
def comparar():
    temp,hum,luz = sensores()
    if request.method == 'POST':
        try:
            planta_nombre = request.form.get('planta')
            if not planta_nombre:
                flash("Por favor, selecciona una planta.")
                return redirect(url_for('index'))
            temp_input = float(request.form.get('temperatura'))
            hum_input = float(request.form.get('humedad'))
            luz_input = float(request.form.get('luz'))

            planta = data[data['Nombre'] == planta_nombre]
            if planta.empty:
                flash("La planta seleccionada no se encontró en el dataset.")
                return redirect(url_for('index'))

            planta = planta.iloc[0]

           
            temp_ideal = planta['Temperatura ideal']
            hum_ideal = planta['Humedad ideal']
            luz_ideal = planta['Luz ideal']

            resultado = {
                "nombre": planta_nombre,
                "temperatura_ideal": temp_ideal,
                "humedad_ideal": hum_ideal,
                "luz_ideal": luz_ideal,
                "temp_diff": round(abs(temp - temp_ideal), 2),
                "humedad_diff": round(abs(hum - hum_ideal), 2),
                "luz_diff": round(abs(luz - luz_ideal), 2)
            }

            plantas_lista = sorted(data['Nombre'].dropna().unique().tolist())
            return render_template("comparardatosingresados.html", plantas=plantas_lista, resultado=resultado,temp=temp, hum=hum, luz=luz)

        except ValueError:
            flash("Por favor, ingresa valores numéricos válidos.")
            return redirect(url_for('index'))
        except Exception as e:
            flash(f"Error inesperado: {str(e)}")
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
