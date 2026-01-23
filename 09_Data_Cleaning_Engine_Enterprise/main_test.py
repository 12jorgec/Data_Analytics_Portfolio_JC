import os
from ingestion_manager import leer_datos_robusto
from statistical_transformation import statistical_cleanup_engine
from mapping_manager import mapear_columnas_inteligente
from uniqueness_handler import remove_absolute_duplicates

# 1. Configuración del Diccionario Maestro (Basado en tus proyectos previos)
diccionario_maestro = {
    'ID_UNICO': ['bike number'], # El CSV tiene 'Bike number'
    'PRODUCTO': ['member type'], # El CSV tiene 'Member type'
    'VENTAS': ['duracion']       # El CSV tiene 'Duration' (Fuzzy lo atrapará)
}
def ejecutar_dce_full_pipeline(nombre_archivo):
    # Definimos la ruta usando tu estructura de carpetas
    ruta = os.path.join("DATA", nombre_archivo)
    print(f"\n--- ⚙️ INICIANDO DATA CLEANING ENGINE (DCE) EN: {nombre_archivo} ---")
    
    # 2. Fase de Ingesta: Tu lógica MIME de detección automática
    df = leer_datos_robusto(ruta)
    if df is None: return

    # 3. Fase de Mapeo: Kit de funciones de unicidad
    cols = mapear_columnas_inteligente(df, diccionario_maestro)

    # 4. Fase de Limpieza Estadística: Tu lógica de Imputación (Media/Moda) + IQR
    if 'VENTAS' in cols:
        print(f"🔬 Procesando columna de ventas: {cols['VENTAS']}")
        df = statistical_cleanup_engine(df, cols['VENTAS'])

    # 5. Fase de Unicidad: Eliminación de duplicados absolutos
    df_limpio = remove_absolute_duplicates(df)

    # 6. Guardado de resultados para el Portafolio
    resultado_path = os.path.join("DATA", f"Limpio_{nombre_archivo.split('.')[0]}.csv")
    df_limpio.to_csv(resultado_path, index=False)
    
    print(f"\n✅ PROCESO COMPLETADO EXITOSAMENTE")
    print(f"📊 Filas finales: {len(df_limpio)}")
    print(f"📂 Archivo guardado en: {resultado_path}")

if __name__ == "__main__":
    # Prueba de fuego con tu archivo real
    ejecutar_dce_full_pipeline("capital-onebike.csv")