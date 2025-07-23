import csv

def analyze_csv(file_path, column_to_analyze=None):
    """
    Lee un archivo CSV, cuenta las filas y opcionalmente
    encuentra el valor máximo y mínimo en una columna numérica.
    """
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)  # Lee la primera fila como encabezado
            
            row_count = 0
            
            # Inicializar para encontrar max/min
            max_value = float('-inf') # Número muy pequeño
            min_value = float('inf')  # Número muy grande
            
            column_index = -1 # Para guardar el índice de la columna a analizar
            if column_to_analyze:
                try:
                    column_index = header.index(column_to_analyze)
                except ValueError:
                    print(f"Error: La columna '{column_to_analyze}' no se encontró en el archivo CSV.")
                    return

            for row in reader:
                row_count += 1
                
                if column_index != -1 and column_index < len(row):
                    try:
                        value = float(row[column_index]) # Intenta convertir a número
                        if value > max_value:
                            max_value = value
                        if value < min_value:
                            min_value = value
                    except ValueError:
                        # Ignorar filas donde el valor no es numérico en la columna deseada
                        pass 

            print(f"\n--- Análisis del Archivo: {file_path} ---")
            print(f"Número total de filas de datos (sin encabezado): {row_count}")

            if column_to_analyze and column_index != -1:
                if max_value != float('-inf') and min_value != float('inf'): # Solo si se encontraron números válidos
                    print(f"Columna analizada: '{column_to_analyze}'")
                    print(f"Valor máximo: {max_value}")
                    print(f"Valor mínimo: {min_value}")
                else:
                    print(f"No se encontraron valores numéricos válidos en la columna '{column_to_analyze}'.")

    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# --- Ejecución del Programa ---
if __name__ == "__main__":
    # Prueba 1: Contar solo filas
    analyze_csv('datos.csv')
    
    print("\n" + "="*40 + "\n") # Separador para claridad

    # Prueba 2: Contar filas y analizar la columna 'Puntuacion'
    analyze_csv('datos.csv', column_to_analyze='Puntuacion')

    print("\n" + "="*40 + "\n") # Separador para claridad

    # Prueba 3: Intentar analizar una columna que no existe
    analyze_csv('datos.csv', column_to_analyze='Salario')

    print("\n" + "="*40 + "\n") # Separador para claridad

    # Prueba 4: Intentar analizar una columna no numérica
    analyze_csv('datos.csv', column_to_analyze='Nombre')

    print("\n" + "="*40 + "\n") # Separador para claridad
    
    # Prueba 5: Intentar con un archivo que no existe
    analyze_csv('archivo_inexistente.csv')