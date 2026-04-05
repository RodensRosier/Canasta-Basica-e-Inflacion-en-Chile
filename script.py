import pandas as pd
import requests
import matplotlib.pyplot as plt

# 1. Configuración de fuentes oficiales (Observatorio Social Chile)
# Nota: En un entorno real, automatizamos la descarga del último Excel publicado
URL_CBA = "https://ministeriodesarrollosocial.gob.cl"

def descargar_y_limpiar_datos(url):
    print("Accediendo a los datos del Ministerio de Desarrollo Social...")
    # Simulamos la carga del dataset oficial
    # df = pd.read_excel(url, sheet_name='Serie_Mensual')
    
    # Estructura técnica esperada para tu repositorio:
    data = {
        'Mes': pd.date_range(start='2024-01-01', periods=24, freq='ME'),
        'Valor_CBA': [67200, 68100, 69050, 68500, 69200, 70065, 70200, 70500, 70804, 71200, 71500, 72100] * 2,
        'IPC_General': [102.1, 102.5, 103.0, 103.2, 103.5, 104.0, 104.2, 104.5, 104.8, 105.1, 105.5, 106.0] * 2
    }
    df = pd.DataFrame(data)
    
    # 2. Cálculo de Variación Porcentual (Habilidad de Analista)
    df['Var_Mensual_CBA'] = df['Valor_CBA'].pct_change() * 100
    return df

# 3. Análisis Comparativo: Canasta vs Inflación
df_cba = descargar_y_limpiar_datos(URL_CBA)

# Visualización para el Repositorio
plt.figure(figsize=(12,6))
plt.plot(df_cba['Mes'], df_cba['Valor_CBA'], label='Valor Canasta Básica ($)', color='red', marker='o')
plt.title('Evolución del Costo de la Canasta Básica de Alimentos en Chile')
plt.xlabel('Periodo')
plt.ylabel('Pesos Chilenos (CLP)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()

print("Análisis completado. Datos listos para exportar a SQL/Tableau.")
