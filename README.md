# Canasta Básica e Inflación en Chile 
### Análisis de la variación de la canasta básica y ajuste de la inflación (2016-2026)

### Descripción del Proyecto

### Stack Tecnológico
Lenguaje: Python 3.10 <br>
• Librerías de Análisis: Pandas, NumPy <br>
• Visualización: Tableau <br>
• Entorno Cloud: Google Cloud Platform (GCP) <br>
• BigQuery (Para procesamiento masivo)

### Metodología (Pipeline ETL)
• Extracción: Obtención de microdatos desde el portal de datos abiertos del INE Chile. <br>
• Transformación (Limpieza): <br>
Tratamiento de valores nulos y registros atípicos (outliers). <br>
Normalización de variables de ingresos y categorías de ocupación. <br>
Análisis: Cálculo de la brecha salarial bruta y ajustada por horas trabajadas y nivel de instrucción. <br>
Carga/Visualización: Exportación de resultados a un Dashboard interactivo en Tableau.

### Hallazgos Claves
• Brecha Promedio: Se identificó una brecha salarial del XX% a nivel nacional. <br>
• Sectores Críticos: El sector de Minería presenta la brecha más alta, mientras que Tecnología muestra una tendencia a la reducción. <br>
• Efecto Educación: A mayor nivel educativo, la brecha tiende a [aumentar/disminuir] según los datos procesados.

### Estructura del Repositorio
• /data: Diccionarios de datos y fuentes. <br>
• /notebooks: Jupyter Notebooks con el Análisis Exploratorio (EDA). <br>
• /scripts: Scripts de Python para la automatización del proceso. <br>

### Dashboard y gráficos estadísticos.

### Cómo Ejecutar el Proyecto
### bash
```
    git clone https://github.com
    cd brecha-salarial-chile
    pip install -r requirements.txt
    python main.py
    Use code with caution.
```
### Fuentes
•  <br>
•  <br>
• 
