import os
import pandas as pd
from Core.visualizer_engine import VisualizerEngine
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# --- CONFIGURACIÓN DE RUTAS ---
DATA_DIR = "DATA"
REPORTS_DIR = "Reports"
for d in [DATA_DIR, REPORTS_DIR]:
    if not os.path.exists(d): os.makedirs(d)

def run_gtm_pipeline():
    print("="*80)
    print("🚀      JCCN GTM DATA SUITE - STRESS TEST EDITION (100K ROWS)")
    print("="*80)

    # Buscamos archivos CSV en la carpeta DATA
    files = [f for f in os.listdir(DATA_DIR) if f.endswith('.csv')]
    
    if not files:
        print("❌ No se encontraron archivos en la carpeta /DATA.")
        return

    for file_name in files:
        print(f"\n📦 PROCESSING: {file_name}")
        path = os.path.join(DATA_DIR, file_name)
        df = pd.read_csv(path)

        # --- CAPA DE BLINDAJE Y MAPEADOR INTELIGENTE ---
        # Detectamos columnas dinámicamente
        cols = {
            'ID': ['customer_id', 'User ID', 'id', 'Customer ID'],
            'Date': ['invoice_date', 'date', 'InvoiceDate', 'OrderDate'],
            'Monetary': ['price', 'amount', 'Monetary', 'TotalAmount']
        }
        
        # Mapeo automático
        found_cols = {}
        for key, possible_names in cols.items():
            for name in possible_names:
                if name in df.columns:
                    found_cols[key] = name
                    break
        
        if len(found_cols) < 3:
            print(f"⚠️ Saltando {file_name}: No cumple con el formato RFM (faltan columnas de ID, Fecha o Monto).")
            continue

        # Limpieza básica
        df = df.dropna(subset=[found_cols['ID'], found_cols['Date'], found_cols['Monetary']])
        
        # Conversión de Fechas (Blindaje para formato D/M/Y y M/D/Y)
        df[found_cols['Date']] = pd.to_datetime(df[found_cols['Date']], dayfirst=True, errors='coerce')
        df = df.dropna(subset=[found_cols['Date']])

        # --- FASE 1: MOTOR RFM ---
        print("⚙️  Calculating RFM Metrics...")
        snapshot_date = df[found_cols['Date']].max() + pd.Timedelta(days=1)
        
        rfm = df.groupby(found_cols['ID']).agg({
            found_cols['Date']: lambda x: (snapshot_date - x.max()).days,
            found_cols['ID']: 'count',
            found_cols['Monetary']: 'sum'
        }).rename(columns={
            found_cols['Date']: 'Recency',
            found_cols['ID']: 'Frequency',
            found_cols['Monetary']: 'Monetary'
        })

        # --- FASE 2: MOTOR ML (K-MEANS) ---
        print(f"🎯 Clustering {len(rfm)} unique customers...")
        scaler = StandardScaler()
        rfm_scaled = scaler.fit_transform(rfm)
        
        # OMP_NUM_THREADS=1 para evitar saturar la CPU en Windows
        os.environ["OMP_NUM_THREADS"] = "1"
        kmeans = KMeans(n_clusters=4, n_init=10, random_state=42)
        rfm['Cluster_ID'] = kmeans.fit_predict(rfm_scaled)

        # --- FASE 3: REPORTE VISUAL CON PLANTILLA JCCN ---
        print("🎨 Generating High-Fidelity Executive Report...")
        viz = VisualizerEngine(REPORTS_DIR)
        p_clusters, p_perfil = viz.crear_graficas(rfm, file_name)
        pdf_path = viz.generar_pdf_ejecutivo(rfm, file_name, p_clusters, p_perfil)
        
        print(f"✨ SUCCESS! Report generated at: {pdf_path}")

    print("\n" + "="*80)
    print("🏁 PROCESS COMPLETED")
    print("="*80)

if __name__ == "__main__":
    run_gtm_pipeline()