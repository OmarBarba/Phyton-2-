import os
import heapq

def distribution_of_initial_runs(input_file, output_file, block_size=1024):
    # Crear una lista para almacenar los runs iniciales
    runs = []

    # Leer el archivo de entrada y dividirlo en runs iniciales
    with open(input_file, 'rb') as f:
        while True:
            block = f.read(block_size)
            if not block:
                break
            run = list(block)
            run.sort()
            runs.append(run)

    # Fusionar los runs iniciales en el archivo de salida
    with open(output_file, 'wb') as f:
        while runs:
            min_run = min(runs, key=lambda run: run[0])
            min_value = min_run.pop(0)
            f.write(bytes([min_value]))

            # Eliminar el run vacío
            if not min_run:
                runs.remove(min_run)

# Ejemplo de uso:
input_file = 'input.txt'  # Archivo de entrada no ordenado
output_file = 'output.txt'  # Archivo de salida ordenado
block_size = 1024  # Tamaño del bloque en bytes

# Crear un archivo de entrada con datos desordenados (puedes reemplazar esto con tus propios datos)
with open(input_file, 'wb') as f:
    data = bytearray(range(255, 0, -1))  # Datos desordenados del 1 al 255
    f.write(data)

# Ordenar el archivo utilizando Distribution of Initial Runs
distribution_of_initial_runs(input_file, output_file)

# Leer y mostrar el archivo ordenado
with open(output_file, 'rb') as f:
    sorted_data = f.read()
    print(sorted_data)

