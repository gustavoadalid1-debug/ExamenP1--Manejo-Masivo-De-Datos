# Las 5 V aplicadas al proyecto

| V del Big Data | Relación con el sistema de sensores | Ejemplo concreto | Estado en el proyecto |
| :--- | :--- | :--- | :--- |
| **Volumen** | Refiere a la cantidad masiva de datos almacenados y generados por la maquinaria. | Pasar de los 100,000 registros actuales a millones de registros diarios al ampliar a miles de sensores. | Futura ampliación |
| **Velocidad** | Refiere a la rapidez con la que se reciben, procesan y analizan los datos. | Recibir y analizar mediciones cada segundo en lugar de procesar un archivo estático. | Futura ampliación |
| **Variedad** | Refiere a la diversidad de formatos y tipos de información recolectada. | Combinar el CSV estructurado actual con fotografías y reportes de texto libre. | Futura ampliación |
| **Veracidad** | Refiere a la confiabilidad, limpieza y calidad de las lecturas. | Filtrar lecturas anómalas causadas por sensores descalibrados antes de disparar una alerta. | CSV actual |
| **Valor** | Refiere a la utilidad práctica y de negocio extraída del análisis de datos. | Identificar qué planta tiene más alertas de temperatura para enfocar el mantenimiento preventivo. | CSV actual |

# Tipos de datos y procesamiento tradicional

**Clasificación de los elementos:**
*   **El CSV de sensores:** Son Datos Estructurados.
*   **Un mensaje JSON enviado por un sensor:** Son Datos Semiestructurados.
*   **Una fotografía de una máquina:** Datos No estructurados.
*   **El texto libre de un reporte de mantenimiento:** Datos No estructurados.

**Justificación sobre el Big Data:**
Un archivo de 100,000 registros no convierte automáticamente el proyecto como tal en Big Data, porque este archivo pues puede ser almacenado facilmente en el disco duro de una computadora personal y procesado en la memoria RAM estándar utilizando herramientas tradicionales en cuestión de milisegundos.

Las limitaciones ya aparecerian al aumentar la escala de los sensores, o si ya llegan a emitir información por segundo e incorporando imágenes, el volumen entonces superaría la capacidad de almacenamiento de un solo servidor, y la velocidad de llegada requerirá arquitecturas mas avanzadas para evitar cuellos de botella y perdidas de datos.


## Batch y Streaming

*   **Tipo de procesamiento realizado:** Se utilizo un procesamiento **Batch**. Esto se justifica porque el programa lee un archivo ya generado (`sensores_industriales.csv`) que ya contiene datos registrados guarados, los carga todos a la vez, realiza los calculos y finaliza su ejecucion.
*   **Enfoque para emitir una alerta en pocos segundos:** Podria servir un enfoque de Streaming, porque las alertas de seguridad son críticas en el tiempo. Procesar los datos en el instante en que se generan permite reaccionar rapidamente, es decir, la baja latencia, para apagar la maquina antes de un daño severo.
*   **Enfoque para generar un resumen al terminar el dia:** Usaria un enfoque **Batch**, ya que los archivos que se generan al final del dia ya no requieren respuestas en milisegundos. Procesar todos los datos juntos al final del dia es mas eficiente y nos permite consolidar la informacion historica de forma precisa.

## 8. Lambda y Kappa

*   **Escenario A (Arquitectura Lambda):**
    *   *Justificación:* La arquitectura Lambda es ideal para este escenario porque mantiene dos rutas separadas: una Capa Batch para recalcular todo el historial garantizando exactitud, y una Capa Speed (el streaming) para dar resultados rapidos de las mediciones recientes.
    *   *Diagrama sencillo:*
        `Sensores -> [ Capa Batch (Historial) / Capa Speed (Reciente) ] -> Capa de Servicio -> Visualización`

*   **Escenario B (Arquitectura Kappa):**
    *   *Justificación:* La arquitectura Kappa está diseñada para manejar todo como un flujo de eventos continuo. Permite usar una sola logica de procesamiento (Streaming) y guarda los datos en un registro inmutable, desde el cual se pueden "reproducir" o volver a procesar todas las mediciones cuando sea necesario sin mantener dos sistemas separados.
    *   *Diagrama sencillo:*
        `Sensores -> Registro Inmutable de Eventos -> Motor de Streaming Unico -> Capa de Servicio -> Visualizacion`



## 9. Analítica descriptiva, predictiva y prescriptiva

*   **Descriptiva:** 
    1. La temperatura maxima registrada fue de **104.99 °C**, detectada por el sensor **S023** el **01/09/26 a las 22:23**.
    2. Se encontraron un total de **6,954 alertas** de temperatura mayores a 85°C en toda la base de datos, siendo la **Planta_3** la que presentó la mayor cantidad de incidentes.

*   **Predictiva:** 
    *   *Pregunta:* ¿Cuál es la probabilidad de que una máquina falle en las próximas 24 horas si su temperatura promedio se ha mantenido sobre los 80 °C durante la última semana?
    *   *Datos adicionales necesarios:* Historial de fallas mecanicas reales etiquetadas con su fecha, registros de mantenimiento preventivo de cada equipo e informacion de la vida util de las piezas del fabricante.

*   **Prescriptiva:** 
    *   *Acción propuesta:* Si el sistema prevé un riesgo inminente de fallo, se debe reducir la velocidad operativa de la maquina a un funcionamiento menor y enviar una notificación urgente al tecnico.
    *   *Información a revisar antes de decidir:* El impacto económico de reducir la producción en esa linea, verificar si el tecnico si esta disponible, y evaluar el costo de reposición del equipo si se permite que llegue a la falla total.