from thefuzz import process
import pandas as pd
def fix_fuzzy_names(df, column, master_list, threshold=80):
    """Corrige errores de escritura comparando con una lista maestra."""
    def get_match(name):
        # Si el valor es nulo o no es string, devolverlo igual
        if pd.isna(name) or not isinstance(name, str):
            return name
        match, score = process.extractOne(name, master_list)
        return match if score >= threshold else name
    
    df[column] = df[column].apply(get_match)
    return df

def remove_absolute_duplicates(df):
    """Elimina filas que son exactamente iguales."""
    return df.drop_duplicates()