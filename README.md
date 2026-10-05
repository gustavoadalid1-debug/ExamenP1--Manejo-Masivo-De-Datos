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

> [!NOTE]
> **Aviso de datos:** Los datos contenidos en este repositorio son **simulados** con fines académicos y de demostración de arquitectura de datos. No corresponden a sensores ni plantas industriales reales.

---

##  Descripción de los Datos

El conjunto de datos principal se encuentra en el archivo `data/sensores_industriales.csv` y consta de 100,000 registros generados por 40 sensores distintos repartidos en 4 plantas operativas.

### Estructura del dataset (`sensores_industriales.csv`)

| Columna | Significado |
| :--- | :--- |
| `id_registro` | 	
Identificador de la medición |
| `fecha_hora` | 	
Fecha y hora de la lectura |
| `id_sensor` | 	
Identificador del sensor |
| `planta` | Planta donde está instalado |
| `temperatura_c` | 	
Temperatura en grados Celsius |
| `vibracion_mm_s` | Vibración en milímetros por segundo |

### Resultados
Los respectivos resultados del codigo se encuentran en la carpeta "resultados"
