import os
import pandas as pd

# Rutas de los archivos CSV y su origen (rutas relativas desde la ubicación del script)
csv_files = {
    'bahia_mansa': 'Data/bahia_mansa.csv',
    'bahia_brava': 'Data/bahia_brava.csv'
}

# Lista para almacenar todos los DataFrames con la columna de origen
dfs = []

# Obtener la ruta absoluta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Leer cada archivo CSV, agregar la columna de origen y almacenar en la lista dfs
for origen, file_name in csv_files.items():
    file_path = os.path.join(current_dir, file_name)
    try:
        df = pd.read_csv(file_path)
        df['Origen'] = origen
        dfs.append(df)
        print(f"Leyendo: {file_path}")
    except FileNotFoundError:
        print(f"¡Error! Archivo no encontrado: {file_path}")

# Concatenar todos los DataFrames en uno solo si hay DataFrames cargados
if dfs:
    combined_df = pd.concat(dfs, ignore_index=True)

    # Guardar el DataFrame combinado en un nuevo archivo CSV
    combined_csv_path = os.path.join(current_dir, 'Data/tiktok_data.csv')
    combined_df.to_csv(combined_csv_path, index=False)

    print(f"Datos combinados guardados en: {combined_csv_path}")
else:
    print("No se encontraron archivos CSV para procesar.")

