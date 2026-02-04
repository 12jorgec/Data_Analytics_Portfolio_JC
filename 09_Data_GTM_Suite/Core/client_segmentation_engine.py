import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

class SegmentationEngine:
    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def ejecutar_rfm(self, id_cliente, fecha_factura, valor_monetario):
        """Calcula métricas y scores RFM basados en quintiles."""
        self.df[fecha_factura] = pd.to_datetime(self.df[fecha_factura])
        ultima_fecha = self.df[fecha_factura].max()
        
        rfm = self.df.groupby(id_cliente).agg({
            fecha_factura: lambda x: (ultima_fecha - x.max()).days,
            id_cliente: 'count',
            valor_monetario: 'sum'
        })
        rfm.columns = ['Recency', 'Frequency', 'Monetary']
        
        # Scoring dinámico por quintiles (1-5)
        rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1])
        rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])
        rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5])
        
        return rfm

    def ejecutar_clustering_kmeans(self, rfm_df, n_clusters=4):
        """Aplica K-Means para encontrar patrones ocultos en el comportamiento del cliente."""
        # 1. Preparación: Logaritmo para normalizar sesgos y Escalado
        # Usamos log1p para manejar posibles ceros en Monetary
        rfm_log = np.log1p(rfm_df[['Recency', 'Frequency', 'Monetary']])
        
        scaler = StandardScaler()
        rfm_scaled = scaler.fit_transform(rfm_log)
        
        # 2. Algoritmo K-Means (Usando tu configuración de n_init y random_state)
        model = KMeans(n_clusters=n_clusters, init='k-means++', n_init=10, random_state=42)
        rfm_df['Cluster_ID'] = model.fit_predict(rfm_scaled)
        
        return rfm_df