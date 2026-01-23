import pandas as pd

def sanitize_text(df, columns):
    """Elimina espacios en blanco y normaliza a formato Título."""
    for col in columns:
        df[col] = df[col].astype(str).str.strip().str.title()
    return df

def format_dates(df, date_column):
    """Convierte strings a objetos datetime para análisis temporal."""
    df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
    return df