# Primer Parcial: Análisis de Sensores Industriales

Repositorio del primer examen parcial sobre manejo y análisis de datos de sensores industriales.

---

##  Información General

| Concepto | Detalle |
| :--- | :--- |
| **Integrantes** | • Germán Eduardo Ruiz Zúñiga<br>• Gustavo Adalid Catalán Carmen |
| **Modalidad** | Parejas (en computadora) |
| **Duración** | 120 minutos |
| **Valor** | 40 puntos (40% de la calificación parcial) |

---

# Análisis de Sensores Industriales — Monitoreo de Temperatura y Vibración

##  Objetivo del Proyecto
El objetivo de este proyecto es analizar y procesar lecturas de sensores industriales distribuidos en distintas plantas operativas. 

> [!NOTA]
> **Aviso de datos:** Los datos contenidos en este repositorio son **simulados** con fines académicos y de demostración de arquitectura de datos. No corresponden a sensores ni plantas industriales reales.

---

##  Descripción de los Datos

El conjunto de datos principal se encuentra en el archivo `data/sensores_industriales.csv` y consta de 100,000 registros generados por 40 sensores distintos repartidos en 4 plantas operativas.

### Estructura del dataset (`sensores_industriales.csv`)

| Columna | Significado |
| :--- | :--- |
| `id_registro` | Identificador de la medición |
| `fecha_hora` | 	Fecha y hora de la lectura |
| `id_sensor` | 	Identificador del sensor |
| `planta` | Planta donde está instalado |
| `temperatura_c` | Temperatura en grados Celsius |
| `vibracion_mm_s` | Vibración en milímetros por segundo |

### Resultados
Los respectivos resultados del codigo se encuentran en la carpeta "resultados"

# INSTALACION:
**1. Clonar el repositorio**
Descarga el código a tu computadora y entra al directorio del proyecto:
```
git clone https://github.com/gustavoadalid1-debug/ExamenP1--Manejo-Masivo-De-Datos
cd ExamenP1--Manejo-Masivo-De-Datos
```

**2. Crea el entorno virtual**
En windows:
```
python -m venv .venv
```

En Linux:
```
python3 -m venv .venv
```

**3. Activa el entorno virtual**
En Linux:
```
source venv/bin/activate
```

En Windows:
```
venv\Scripts\activate
```

**4. Instala las dependencias**
Ejecuta el siguiente comando para instalar las librerias necesarias para ejecutar el proyecto.

```
pip install -r requirements.txt
```

**5. Ejecución del programa**
Asegurate de estar en la carpeta 'ExamenP1--Manejo-Masivo-De-Datos'
En la terminal ejecuta el siguiente comando:

```
python analisis.py
```

# Resultados Esperados
Al ejecutar el script principal, la consola arrojará un resumen descriptivo calculado al vuelo a partir del dataset, incluyendo:

El conteo total de registros y sensores únicos.

El promedio de temperatura agrupado por planta.

La temperatura máxima histórica junto con el sensor y la fecha en que ocurrió.

La suma de registros que sobrepasan la alerta de 85 °C y la planta más afectada.

Archivos exportados: Adicionalmente, el programa generará de forma automática el archivo resultados/alertas.csv, el cual contendrá exclusivamente las filas donde las lecturas de temperatura hayan superado el umbral crítico.

# CONCLUSIONES:
Se encontraron un total de 6,954 alertas de temperatura mayores a 85°C en toda la base de datos, siendo la Planta 3 la que presentó la mayor cantidad de incidentes.
La temperatura maxima registrada fue de 104.99 °C, detectada por el sensor S023 el 01/09/26 a las 22:23.
Con este proyecto se logró realiza un analisis de una base de datos dada por el profesor, el cual si tuviera un avance tecnológico en cuestion de sensores y registros de datos en tiempo real, podría ocnvertirse en un ejemplo de big data, de momento estos registros se pudieron procesar de forma Batch, ya que son registros ya guardados y ya existentes, no va a haber que procesar en tiempo real.

Esto nos genera una estadística sobre los sensores y que maquinas generan una alerta y conviene revisar.

