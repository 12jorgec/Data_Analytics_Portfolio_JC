from thefuzz import process
import pandas as pd

def mapear_columnas_inteligente(df, diccionario_maestro, umbral_similitud=80):
    """
    Mapea las columnas del DataFrame usando coincidencia exacta y Fuzzy Matching.
    """
    columnas_archivo = df.columns.tolist()
    mapeo_final = {}
    
    print("\n--- [KLO] Iniciando Mapeo Inteligente ---")
    
    for concepto, sinonimos in diccionario_maestro.items():
        encontrado = False
        
        # 1. Intento de coincidencia exacta (rápido)
        for col in columnas_archivo:
            if col.lower() in [s.lower() for s in sinonimos]:
                mapeo_final[concepto] = col
                print(f"✅ Exacto: {concepto} -> '{col}'")
                encontrado = True
                break
        
        # 2. Si no hubo exacta, usamos Fuzzy Matching
        if not encontrado:
            # Comparamos cada columna del archivo contra la lista de sinónimos
            # Buscamos la mejor coincidencia para cualquier sinónimo de este concepto
            mejor_match_global = None
            mejor_score_global = 0
            
            for col in columnas_archivo:
                match, score = process.extractOne(col.lower(), sinonimos)
                if score > mejor_score_global:
                    mejor_score_global = score
                    mejor_match_global = col
            
            # Si la mejor coincidencia supera el umbral, la aceptamos
            if mejor_score_global >= umbral_similitud:
                mapeo_final[concepto] = mejor_match_global
                print(f"🤖 Fuzzy ({mejor_score_global}%): {concepto} -> '{mejor_match_global}'")
            else:
                print(f"⚠️ Alerta: No se encontró coincidencia confiable para '{concepto}'")
                
    return mapeo_final