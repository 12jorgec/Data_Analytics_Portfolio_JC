from thefuzz import fuzz

class MappingManager:
    def __init__(self, dataframe):
        self.df = dataframe.copy()
        # Diccionario maestro con los nombres exactos de tu CSV
        self.master_dict = {
            "Venta_EUR": ["order_value_eur", "sales", "revenue", "amount", "total"],
            "Pais": ["country", "pais", "territory"],
            "Categoria": ["category", "categoria", "item_type"],
            "ID_Orden": ["order_id", "transaction_id"],
            "ID_Cliente": ["customer_name", "customer", "cliente", "contact_name"],
            "Fecha": ["date", "fecha", "order_date"]
        }

    def standardize_columns(self, threshold=70):
        """Busca y renombra las columnas necesarias."""
        new_cols = {}
        current_columns = self.df.columns.tolist()
        
        for concept, synonyms in self.master_dict.items():
            for actual_col in current_columns:
                clean_col = str(actual_col).strip().lower()
                clean_synonyms = [s.lower() for s in synonyms]
                
                # Match exacto o por similitud
                match = clean_col in clean_synonyms
                if not match:
                    for syn in clean_synonyms:
                        if fuzz.ratio(clean_col, syn) >= threshold:
                            match = True
                            break
                
                if match:
                    new_cols[actual_col] = concept
                    break
            
        self.df = self.df.rename(columns=new_cols)
        return self.df[list(new_cols.values())].copy()