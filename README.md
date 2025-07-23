# Python CSV Analyzer (Herramienta Simple de Análisis de CSV)

## Descripción
Este es un script de Python sencillo diseñado para leer archivos CSV y realizar operaciones básicas de análisis de datos. Actualmente, permite contar el número total de filas de datos y, opcionalmente, encontrar los valores máximos y mínimos en una columna numérica específica.

## Habilidades Demostradas
-   **Manejo de Archivos:** Lectura segura de archivos CSV.
-   **Procesamiento de Datos:** Extracción y conversión de datos por columna.
-   **Lógica de Programación:** Uso de bucles (`for`), condicionales (`if/else`) y manejo básico de excepciones (`try/except`).
-   **Uso del Módulo `csv`:** Familiaridad con la librería estándar de Python para CSV.

## Cómo Usar
1.  Asegúrate de tener Python 3 instalado.
2.  Guarda el archivo `analyzer.py` y tu archivo CSV (por ejemplo, `datos.csv`) en la misma carpeta.
3.  Abre tu terminal/símbolo del sistema y navega hasta esa carpeta.
4.  Ejecuta el script con el siguiente comando:
    ```bash
    python analyzer.py
    ```
5.  Para analizar una columna específica (ej. 'Puntuacion'):
    ```python
    # Dentro de analyzer.py, modifica la línea de ejecución principal
    # o puedes modificar el script para que tome argumentos de línea de comandos (más avanzado)
    # Por ahora, simplemente descomenta/modifica en el código el llamado a la función:
    analyze_csv('datos.csv', column_to_analyze='Puntuacion')
    ```

## Ejemplo de Salida (usando `datos.csv` y analizando 'Puntuacion')
--- Análisis del Archivo: datos.csv ---
Número total de filas de datos (sin encabezado): 5
Columna analizada: 'Puntuacion'
Valor máximo: 95.0
Valor mínimo: 78.0

## Futuras Mejoras (Ideas)
-   Agregar un promedio de columna.
-   Permitir al usuario especificar la columna a analizar desde la línea de comandos.
-   Manejo de más tipos de datos.
