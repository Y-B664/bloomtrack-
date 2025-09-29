import pandas as pd

# Ruta al archivo CSV descargado
df = pd.read_csv("datasets/spotify/Dataset plantas.csv")

# Ver las primeras filas
print(df.head())
print(df.columns)