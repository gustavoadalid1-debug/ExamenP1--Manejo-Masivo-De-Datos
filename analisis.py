import pandas as pd
import os

# Para abrir un csv:
df = pd.read_csv('data/sensores_industriales.csv')

print("== Analisis ==")

# Registros:
total_registros = len(df)
sensores_distintos = df['id_sensor'].nunique()
print(f"\n Cantidad de registros: {total_registros}")
print(f"Cantidad de sensores distintos: {sensores_distintos}")

# Temp ede cada planta
temp_promedio = df.groupby('planta')['temperatura_c'].mean()
print("\n Temperatura promedio por planta:")
print(temp_promedio.to_string())

# Temp Maxima cno los sensores:
idx_max = df['temperatura_c'].idxmax() 
temp_max = df.loc[idx_max, 'temperatura_c']
sensor_max = df.loc[idx_max, 'id_sensor']
fecha_max = df.loc[idx_max, 'fecha_hora']
    
print(f"\n La Temperatura maxima encontrada es: {temp_max} °C")
print(f"   Sensor: {sensor_max}")
print(f"   Fecha y hora: {fecha_max}")

# Mayor a 85°C
alertas_df = df[df['temperatura_c'] > 85]
total_alertas = len(alertas_df)
print(f"\n Lecturas con alerta (temperatura > 85 °C): {total_alertas}")

# Planta con mas alertas de temperatura
if total_alertas > 0:
    planta_mas_alertas = alertas_df['planta'].value_counts().idxmax()
    print(f"\n La Planta con mas alertas de temperatura: {planta_mas_alertas}")
else:
    print("\n No hay alertas de temperatura.")
    
# Exportacion :
if total_alertas > 0:
    alertas_df.to_csv('resultados/alertas.csv', index=False)
    print("\n Las lecturas con alerta se han exportado exitosamente a 'resultados/alertas.csv'.")
else:
    print("\n No hay alertas como tal")