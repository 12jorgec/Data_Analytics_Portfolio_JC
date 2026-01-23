import magic
import pandas as pd
import os

def leer_datos_robusto(ruta_archivo):
    # 1. Intento por tipo MIME
    mime_type = magic.from_file(ruta_archivo, mime=True)
    
    # 2. Plan B: Obtener extensión si el MIME es genérico (text/plain)
    extension = os.path.splitext(ruta_archivo)[1].lower()

    print(f"🔍 [DCE] Ingesta detectada: {mime_type} | Extensión: {extension}")

    # Lógica combinada
    if mime_type == 'text/csv' or extension == '.csv':
        return pd.read_csv(ruta_archivo)
    elif extension in ('.xlsx', '.xls'):
        return pd.read_excel(ruta_archivo)
    elif mime_type == 'application/json' or extension == '.json':
        return pd.read_json(ruta_archivo)
    else:
        print(f"⚠️ Formato no soportado: {mime_type}")
        return None