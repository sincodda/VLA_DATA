import nbformat
from nbclient import NotebookClient
import subprocess
import os  # Importa el módulo os

def ejecutar_notebook(notebook_path):
    try:
        # Construye la ruta completa al archivo notebook
        notebook_full_path = os.path.abspath(notebook_path)

        if not os.path.exists(notebook_full_path):
            raise FileNotFoundError(f"No se encontró el archivo: {notebook_full_path}")

        with open(notebook_full_path, 'r', encoding='utf-8') as f:
            notebook_content = nbformat.read(f, as_version=4)
        
        client = NotebookClient(nb=notebook_content)
        client.execute()

        print(f"Ejecución exitosa del notebook: {notebook_path}")
    except Exception as e:
        print(f"Error al ejecutar el notebook {notebook_path}: {e}")

# Ruta a los notebooks que deseas ejecutar en orden
notebook1_path = "Scrap/main_bahiaBrava.ipynb"
notebook2_path = "Scrap/main_bahiaMansa.ipynb"
print(f"Ruta del notebook 1: {notebook1_path}")
print(f"Ruta del notebook 2: {notebook2_path}")

# Ejecutar el primer notebook
ejecutar_notebook(notebook1_path)

# Ejecutar el segundo notebook
ejecutar_notebook(notebook2_path)

# Ruta del script a ejecutar
script_path = "Scrap/union.py"
script_full_path = os.path.abspath(script_path)
print(f"Ruta absoluta del script: {script_full_path}")

try:
    # Ejecutar el script usando subprocess y la ruta absoluta del script
    completed_process = subprocess.run(["python", script_full_path], capture_output=True, text=True)
    print("Resultado de la ejecución del script:")
    print(completed_process.stdout)
except Exception as e:
    print(f"Error al ejecutar el script: {e}")

