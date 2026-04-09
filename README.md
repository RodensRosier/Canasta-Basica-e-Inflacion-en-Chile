# Canasta Básica e Inflación en Chile 
Análisis de la variación de la canasta básica y ajuste de la inflación (2016-2026).

### Stack Tecnológico
**• Lenguaje de programación:** Python 3.10 <br>
**• Librerías de Análisis:** Pandas, NumPy <br>
**• Visualización:** Tableau <br>
**• Entorno Cloud:** Google BigQuery (para el procesamiento masivo).

### Metodología (Pipeline ETL)
**• Extracción:** Obtención de microdatos desde el portal de datos abiertos del INE Chile. <br>
**• Transformación (Limpieza):** Tratamiento de valores nulos y registros atípicos (outliers) y normalización de variables de ingresos y categorías de ocupación. <br>
**Análisis:** Cálculo de la brecha salarial bruta y ajustada por horas trabajadas y nivel de instrucción. <br>
**Carga/Visualización:** Exportación de resultados a un Dashboard interactivo en Tableau.

### Hallazgos Claves
**• Brecha Promedio:** Se identificó una brecha salarial del XX% a nivel nacional. <br>
**• Sectores Críticos:** El sector de Minería presenta la brecha más alta, mientras que Tecnología muestra una tendencia a la reducción. <br>
**• Efecto Educación:** A mayor nivel educativo, la brecha tiende a [aumentar/disminuir] según los datos procesados.

### Estructura del Repositorio
**• /data:** Diccionarios de datos y fuentes. <br>
**• /notebooks:** Jupyter Notebooks con el Análisis Exploratorio (EDA). <br>
**• /scripts:** Scripts de Python para la automatización del proceso. <br>

### Dashboard y gráficos estadísticos.
<br>

### Cómo Ejecutar el Proyecto
```
    git clone https://github.com
    cd brecha-salarial-chile
    pip install -r requirements.txt
    python script.py
```
### Fuentes
**• INE Chile:** . <br>
**• ...** <br>
**• ...**