import pandas as pd
import numpy as np

def handle_outliers_iqr(df, column):
    """Filtra valores extremos usando el Rango Intercuartílico (IQR)."""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

def imputar_segun_distribucion(df, column):
    """Lógica de Jorge: Imputación inteligente basada en simetría."""
    media = df[column].mean()
    mediana = df[column].median()
    
    # Si la diferencia es mínima, es simétrica -> Media
    if abs(media - mediana) < 0.001:
        print(f"📊 [DCE] Simetría detectada. Imputando con MEDIA.")
        df[column] = df[column].fillna(media)
    else:
        # Si hay sesgo -> Moda (el valor que más se repite)
        moda = df[column].mode()[0]
        print(f"📉 [DCE] Sesgo detectado. Imputando con MODA.")
        df[column] = df[column].fillna(moda)
    return df

def statistical_cleanup_engine(df, column):
    """Ejecuta el flujo completo: Imputación + Remoción de Outliers."""
    df = imputar_segun_distribucion(df, column)
    df = handle_outliers_iqr(df, column)
    return df