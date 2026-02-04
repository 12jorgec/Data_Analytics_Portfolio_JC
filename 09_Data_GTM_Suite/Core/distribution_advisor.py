import numpy as np
from scipy import stats

class DistributionAdvisor:
    def __init__(self, alpha=0.05):
        self.alpha = alpha

    def analizar_distribucion(self, data):
        """Diagnostica si la data es normal para decidir el camino estadístico."""
        clean_data = np.array(data.dropna())
        
        # Test de Normalidad de D'Agostino's K^2 (el que usabas en tu motor original)
        stat, p_value = stats.normaltest(clean_data)
        is_normal = p_value > self.alpha
        
        return {
            "is_normal": is_normal,
            "p_value": p_value,
            "test_name": "D'Agostino's K^2",
            "decision": "Paramétrica (Normal)" if is_normal else "No Paramétrica (No Normal)"
        }