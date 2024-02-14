import os
import shutil
from datetime import datetime

# Define el directorio que quieres organizar
directorio = 'C:\\Users\\danny\\Documents'

# Obtén una lista de todos los archivos en el directorio
archivos = [f for f in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, f))]

for archivo in archivos:
    # Obtén la ruta completa del archivo
    ruta_archivo = os.path.join(directorio, archivo)
    
    # Obtén la fecha de última modificación del archivo
    tiempo_modificacion = os.path.getmtime(ruta_archivo)
    fecha = datetime.fromtimestamp(tiempo_modificacion)
    
    # Formato de nombre de carpeta: Año-Mes_TipoDeArchivo
    nombre_carpeta = fecha.strftime('%Y-%m') + '_' + archivo.split('.')[-1]
    
    # Crea la ruta completa de la carpeta
    ruta_carpeta = os.path.join(directorio, nombre_carpeta)
    
    # Crea la carpeta si no existe
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
    
    # Mueve el archivo a la carpeta
    shutil.move(ruta_archivo, os.path.join(ruta_carpeta, archivo))

print("Archivos organizados con éxito.")