# REVISADO POR QA (Luis): Código óptimo y libre de datos sensibles.

# PROYECTO: Análisis de Estadísticas Deportivas (Escenario D)
# ROL: P2 - Desarrollador Técnico (Paco)
# DESCRIPCIÓN: Script reproducible para procesar resultados de un campeonato,
#              calcular tabla de posiciones, goles promedio y generar gráfico.


import csv
import os
import matplotlib.pyplot as plt

# 1. Rutas de archivos (Rutas relativas para asegurar la reproducibilidad)
RUTA_DATOS = os.path.join("datos", "resultados_partidos.csv")
RUTA_RESULTADOS = os.path.join("resultados", "comparativa_rendimiento.png")

def cargar_y_procesar_datos():
    # Diccionario para almacenar las estadísticas de cada equipo
    # Estructura: { "Equipo": {"ganados": 0, "puntos": 0, "goles_favor": 0} }
    equipos = {}
    total_goles = 0
    total_partidos = 0

    # Verificar si el archivo existe antes de abrirlo
    if not os.path.exists(RUTA_DATOS):
        raise FileNotFoundError(f"No se encontró el archivo de datos en: {RUTA_DATOS}")

    # Leer el archivo CSV
    with open(RUTA_DATOS, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        
        for fila in lector:
            local = fila["equipo_local"]
            visitante = fila["equipo_visitante"]
            g_local = int(fila["goles_local"])
            g_visitante = int(fila["goles_visitante"])

            # Inicializar equipos en el diccionario si no existen
            for eq in [local, visitante]:
                if eq not in equipos:
                    equipos[eq] = {"ganados": 0, "puntos": 0, "goles_favor": 0}

            # Acumular goles a favor
            equipos[local]["goles_favor"] += g_local
            equipos[visitante]["goles_favor"] += g_visitante
            
            # Contadores globales para el promedio
            total_goles += (g_local + g_visitante)
            total_partidos += 1

            # Lógica de asignación de puntos y partidos ganados
            if g_local > g_visitante:
                equipos[local]["ganados"] += 1
                equipos[local]["puntos"] += 3
            elif g_visitante > g_local:
                equipos[visitante]["ganados"] += 1
                equipos[visitante]["puntos"] += 3
            else:
                equipos[local]["puntos"] += 1
                equipos[visitante]["puntos"] += 1

    return equipos, total_goles, total_partidos

def mostrar_reporte(equipos, total_goles, total_partidos):
    print("==================================================")
    print("      ESTADÍSTICAS DEL CAMPEONATO DEPORTIVO       ")
    print("==================================================")
    
    # Calcular y mostrar el promedio de goles por partido (Requisito del TP)
    promedio_goles = total_goles / total_partidos if total_partidos > 0 else 0
    print(f"-> Total de partidos analizados: {total_partidos}")
    print(f"-> Promedio de goles por partido: {promedio_goles:.2f}\n")

    print("TABLA DE POSICIONES:")
    print(f"{'Equipo':<15} | {'Puntos':<6} | {'P. Ganados':<10} | {'Goles Favor':<11}")
    print("-" * 55)
    
    # Ordenar la tabla de posiciones por puntos (de mayor a menor)
    tabla_ordenada = sorted(equipos.items(), key=lambda x: x[1]["puntos"], reverse=True)
    
    for eq, stats in tabla_ordenada:
        print(f"{eq:<15} | {stats['puntos']:<6} | {stats['ganados']:<10} | {stats['goles_favor']:<11}")
    
    return tabla_ordenada

def generar_grafico_rendimiento(tabla_ordenada):
    # Extraer datos para el gráfico comparativo (Requisito del TP)
    nombres_equipos = [item[0] for item in tabla_ordenada]
    goles_totales = [item[1]["goles_favor"] for item in tabla_ordenada]

    # Configuración estética del gráfico
    plt.figure(figsize=(8, 5))
    plt.bar(nombres_equipos, goles_totales, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"])
    
    plt.title("Goles Totales a Favor por Equipo", fontsize=14, fontweight='bold')
    plt.xlabel("Equipos", fontsize=12)
    plt.ylabel("Cantidad de Goles", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Asegurar que la carpeta 'resultados' exista antes de guardar
    os.makedirs(os.path.dirname(RUTA_RESULTADOS), exist_ok=True)
    
    # Guardar el gráfico automáticamente
    plt.savefig(RUTA_RESULTADOS, dpi=300, bbox_inches='tight')
    print(f"\n[ÉXITO] Gráfico comparativo guardado en: {RUTA_RESULTS}")
    plt.close()

# Bloque de ejecución principal
if __name__ == "__main__":
    datos_equipos, goles, partidos = cargar_y_procesar_datos()
    tabla = mostrar_reporte(datos_equipos, goles, partidos)
    generar_grafico_rendimiento(tabla)