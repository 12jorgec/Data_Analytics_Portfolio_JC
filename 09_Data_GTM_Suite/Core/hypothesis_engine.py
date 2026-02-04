from scipy import stats

class HypothesisEngine:
    def __init__(self, alpha=0.05):
        self.alpha = alpha

    def ejecutar_prueba(self, grupo1, nombre1, grupo2, nombre2, diagnostico):
        """Ejecuta la prueba y genera una narrativa dinámica para cualquier dataset."""
        g1, g2 = grupo1.dropna(), grupo2.dropna()
        
        # SELECCIÓN DINÁMICA DEL MÉTODO
        if diagnostico['is_normal']:
            stat, p_value = stats.ttest_ind(g1, g2)
            metodo = "Prueba T de Student (Paramétrica)"
            rec = f"La distribución es normal. Se recomienda una prueba Paramétrica como {metodo}."
        else:
            stat, p_value = stats.mannwhitneyu(g1, g2)
            metodo = "Prueba de Mann-Whitney U (No Paramétrica)"
            rec = f"Dado que la distribución encontrada no es normal, se recomienda efectuar una prueba de hipótesis No Paramétrica como {metodo}."
        
        # CONCLUSIÓN DINÁMICA POR GRUPOS
        rechazar_nula = p_value < self.alpha
        if rechazar_nula:
            concl = f"✅ Encontramos evidencia estadística suficiente para afirmar que el cambio es real entre los grupos: '{nombre1}' vs '{nombre2}'."
            status = "Diferencia Significativa"
        else:
            concl = f"❌ No hay suficiente evidencia para afirmar que el cambio es real entre los grupos: '{nombre1}' vs '{nombre2}'."
            status = "Sin Diferencia Significativa"
            
        return {
            "comparacion": f"{nombre1} vs {nombre2}",
            "metodo": metodo,
            "recomendacion": rec,
            "p_valor": round(p_value, 4),
            "resultado_texto": status,
            "conclusion_negocio": concl
        }
        