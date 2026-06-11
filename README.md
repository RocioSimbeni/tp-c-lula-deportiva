# Análisis de Estadísticas de Resultados Deportivos
## Célula de Desarrollo Ágil - Trabajo Práctico (Escenario D)

Este proyecto implementa un flujo de trabajo ágil y reproducible para procesar los resultados de un campeonato deportivo. A través de este desarrollo, se calculan métricas clave del torneo y se genera un reporte visual de rendimiento.

---

## Integrantes del Equipo 

* **P1 - Líder y Organizador (Hugo):**  
  *Responsable de la gobernanza del repositorio, estructura inicial y control de versiones.*
* **P2 - Desarrollador Técnico (Paco):** 
  *Responsable de la lógica algorítmica, procesamiento de datos y generación de gráficos.*
* **P3 - Revisor y QA (Luis):**   
  *Responsable del Peer Review, calidad del código, documentación interna y seguridad.*

---

##  Objetivos del Proyecto

1. **Ingesta de Datos:** Importar un archivo estructurado con los resultados históricos de los partidos.
2. **Procesamiento Estadístico:**
   * Calcular la cantidad de partidos ganados por cada equipo.
   * Construir la tabla de posiciones oficial.
   * Determinar el promedio de goles por partido del torneo.
3. **Visualización:** Generar un gráfico comparativo del rendimiento ofensivo de los equipos.

---

##  Estructura del Repositorio

* `/datos`: Contiene el archivo fuente `resultados_partidos.csv`.
* `/scripts`: Aloja el archivo ejecutable de análisis estadístico (`analisis_deportivo.py`).
* `/resultados`: Carpeta de salida donde se almacena el gráfico comparativo generado.

---

## Trazabilidad y Gobernanza (Jira + Git)

Para garantizar la conexión estricta entre la gestión del proyecto y el código, el equipo utiliza **Conventional Commits** vinculados a los IDs de Jira. Cada confirmación de cambios sigue la estructura:

`CLAVE-ID: [tipo]: descripción corta`

*Ejemplo:* `DEP-1: feat: inicialización de estructura de carpetas /scripts y /datos.`

---

## Instrucciones de Reproducción (Google Colab)

El análisis está diseñado para ser ejecutado directamente en entornos en la nube como **Google Colab**. 

1. Clonar el repositorio.
2. Asegurar la presencia de los datos en la carpeta `/datos`.
3. Ejecutar el script ubicado en `/scripts`. El programa generará las tablas en consola y exportará el gráfico a la carpeta `/resultados` de forma automática.