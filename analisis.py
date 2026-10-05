import pandas as pd
import os

# Para abrir un csv:
df = pd.read_csv('data/sensores_industriales.csv')

print("== Analisis ==")

# Registros:
total_registros = len(df)
sensores_distintos = df['id_sensor'].nunique()
print(f"\n1. Cantidad de registros: {total_registros}")
print(f"Cantidad de sensores distintos: {sensores_distintos}")

# Temp ede cada planta
temp_promedio = df.groupby('planta')['temperatura_c'].mean()
print("\n2. Temperatura promedio por planta:")
print(temp_promedio.to_string())

# Temp Maxima cno los sensores:
idx_max = df['temperatura_c'].idxmax() 
temp_max = df.loc[idx_max, 'temperatura_c']
sensor_max = df.loc[idx_max, 'id_sensor']
fecha_max = df.loc[idx_max, 'fecha_hora']
    
print(f"\n3. Temperatura máxima encontrada: {temp_max} °C")
print(f"   Sensor: {sensor_max}")
print(f"   Fecha y hora: {fecha_max}")

# Mayor a 85°C
alertas_df = df[df['temperatura_c'] > 85]
total_alertas = len(alertas_df)
print(f"\n4. Lecturas con alerta (temperatura > 85 °C): {total_alertas}")

# Planta con mas alertas de temperatura
if total_alertas > 0:
    planta_mas_alertas = alertas_df['planta'].value_counts().idxmax()
    print(f"\n5. Planta con más alertas de temperatura: {planta_mas_alertas}")
else:
    print("\n5. No se registraron alertas de temperatura.")
# Exportacion :
if total_alertas > 0:
    alertas_df.to_csv('resultados/alertas.csv', index=False)
    print("\nLas lecturas con alerta se han exportado exitosamente a 'resultados/alertas.csv'.")
else:
    print("\n6. No hay alertas para exportar.")