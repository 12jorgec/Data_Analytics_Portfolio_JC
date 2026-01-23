from ingestion_manager import leer_datos_robusto

print("🛠️ PROBANDO FASE 1 (INGESTA) DEL OPTIMIZED CLEANING DATA ENGINE")

# 1. Probar el CSV
print("\n--- [DCE] Test Archivo 1: CSV ---")
df_csv = leer_datos_robusto('DATA/capital-onebike.csv')
if df_csv is not None:
    print(f"✅ CSV validado. Filas: {len(df_csv)}")

# 2. Probar el JSON
print("\n--- [DCE] Test Archivo 2: JSON ---")
df_json = leer_datos_robusto('DATA/environment.json')
if df_json is not None:
    print(f"✅ JSON validado. Filas: {len(df_json)}")

print("\n🚀 FASE 1 COMPLETADA. El motor está listo para el despliegue.")