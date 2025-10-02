from kaggle.api.kaggle_api_extended import KaggleApi
import os



# Autenticación
api = KaggleApi()
api.authenticate()

# Crear carpeta destino si no existe
os.makedirs('datasets/Inventario plantas', exist_ok=True)

# Descargar y descomprimir el dataset
api.dataset_download_files(
    'benavidesy/dataset-plantas',
    path='datasets/Inventario plantas',
    unzip=True
)

print("Dataset descargado exitosamente.")
