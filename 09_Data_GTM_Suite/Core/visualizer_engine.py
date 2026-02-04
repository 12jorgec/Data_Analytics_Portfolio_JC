import os
from fpdf import FPDF
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
from pypdf import PdfReader, PdfWriter

class VisualizerEngine:
    def __init__(self, reports_dir):
        self.reports_dir = reports_dir
        self.assets_dir = os.path.join(reports_dir, "Assets")
        if not os.path.exists(self.assets_dir): 
            os.makedirs(self.assets_dir)

    def crear_graficas(self, rfm_df, file_name):
        """Genera las visualizaciones necesarias para el reporte ejecutivo."""
        # 1. Cluster Scatter Plot
        plt.figure(figsize=(10, 6))
        ax = sns.scatterplot(
            data=rfm_df, 
            x='Frequency', 
            y='Monetary', 
            hue='Cluster_ID', 
            palette='viridis', 
            s=100
        )
        plt.title('Strategic Customer Segmentation (K-Means)', fontsize=14, pad=15)
        plt.ylabel('Total Revenue (EUR)')
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f'{x:,.0f}'))
        
        p_clusters = os.path.join(self.assets_dir, f"Clusters_{file_name.split('.')[0]}.png")
        plt.savefig(p_clusters, bbox_inches='tight')
        plt.close()

        # 2. RFM Profiles Bar Chart (Log Scale para mejor visibilidad)
        plt.figure(figsize=(12, 6))
        cluster_avg = rfm_df.groupby('Cluster_ID')[['Recency', 'Frequency', 'Monetary']].mean()
        ax_bar = cluster_avg.plot(
            kind='bar', 
            color=['#3498db', '#e67e22', '#2ecc71'], 
            edgecolor='black'
        )
        plt.title('Average RFM Profile by Segment', fontsize=14, pad=15)
        plt.yscale('log')
        plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f'{x:,.0f}'))
        plt.legend(
            ["Recency (Days)", "Frequency (Orders)", "Monetary (EUR)"], 
            loc='upper left', 
            bbox_to_anchor=(1, 1)
        )
        
        p_perfil = os.path.join(self.assets_dir, f"Perfil_{file_name.split('.')[0]}.png")
        plt.savefig(p_perfil, bbox_inches='tight')
        plt.close()
        
        return p_clusters, p_perfil

    def generar_pdf_ejecutivo(self, rfm_df, file_name, p_clusters, p_perfil):
        """Genera el contenido dinámico y lo fusiona con la plantilla JCCN."""
        temp_pdf = os.path.join(self.reports_dir, "temp_to_merge.pdf")
        pdf = FPDF()
        avg_aov = rfm_df['Monetary'].mean()
        
        # --- PÁGINA 1: Segmentación General ---
        pdf.add_page()
        pdf.ln(55)  # Espacio de seguridad para el encabezado de la plantilla
        pdf.set_font('Arial', 'B', 16)
        pdf.set_text_color(44, 62, 80)
        pdf.cell(0, 10, 'STRATEGIC SEGMENTATION REPORT Q4', 0, 1)
        
        pdf.ln(5)
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, '1. Portfolio Health Status', 0, 1)
        
        pdf.set_font('Arial', '', 11)
        analysis_text = (
            f"The analysis identifies an Average Order Value (AOV) of {avg_aov:,.2f} EUR. "
            f"The K-Means model has categorized 4 high-impact segments for ROI optimization."
        )
        pdf.multi_cell(0, 7, analysis_text)
        
        pdf.ln(10)
        pdf.image(p_clusters, x=25, w=150)

        # --- PÁGINA 2: Distribución RFM ---
        pdf.add_page()
        pdf.ln(55) # Margen superior para consistencia visual
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, '2. Average RFM Distribution', 0, 1)
        
        pdf.ln(5)
        pdf.image(p_perfil, x=25, w=150)
        
        pdf.output(temp_pdf)

        # --- FUSIÓN MAESTRA CON PLANTILLA ---
        # Localiza la plantilla en la raíz del proyecto
        base_path = os.path.dirname(os.path.dirname(__file__))
        template_path = os.path.join(base_path, "reports_template_jccn.pdf")
        final_path = os.path.join(self.reports_dir, f"REPORT_JCCN_{file_name.split('.')[0]}.pdf")
        
        if os.path.exists(template_path):
            writer = PdfWriter()
            content_reader = PdfReader(temp_pdf)
            template_reader = PdfReader(template_path)
            
            for i in range(len(content_reader.pages)):
                # Si el template tiene solo una página, la reusamos; si tiene más, seguimos el orden
                t_idx = 0 if len(template_reader.pages) == 1 else i
                page = template_reader.pages[t_idx]
                
                # Fusionamos la capa de contenido sobre la capa de la plantilla
                page.merge_page(content_reader.pages[i])
                writer.add_page(page)
            
            with open(final_path, "wb") as f:
                writer.write(f)
            
            os.remove(temp_pdf) # Limpieza de archivo temporal
            return final_path
        else:
            print(f"⚠️ Alerta: No se encontró {template_path}. Generando PDF sin plantilla.")
            return temp_pdf