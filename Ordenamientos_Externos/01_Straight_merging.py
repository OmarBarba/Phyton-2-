import heapq
import tempfile
import shutil
import os

def straight_merging_sort(input_file, output_file, block_size=1024):
    # Crear un directorio temporal para almacenar los bloques
    temp_dir = tempfile.mkdtemp()

    try:
        # Dividir el archivo de entrada en bloques más pequeños
        with open(input_file, 'rb') as f:
            block_count = 0
            while True:
                block = f.read(block_size)
                if not block:
                    break
                block = list(block)
                block.sort()
                block_file = os.path.join(temp_dir, f'block_{block_count}.dat')
                with open(block_file, 'wb') as block_f:
                    block_f.write(bytes(block))
                block_count += 1

        # Fusionar los bloques ordenados en un archivo de salida
        with open(output_file, 'wb') as out:
            blocks = [open(os.path.join(temp_dir, f'block_{i}.dat'), 'rb') for i in range(block_count)]
            min_heap = []

            for i in range(block_count):
                num = int.from_bytes(blocks[i].read(1), byteorder='big')
                min_heap.append((num, i))

            heapq.heapify(min_heap)

            while min_heap:
                min_num, min_block_index = heapq.heappop(min_heap)
                out.write(min_num.to_bytes(1, byteorder='big'))
                next_num = int.from_bytes(blocks[min_block_index].read(1), byteorder='big')
                if next_num:
                    heapq.heappush(min_heap, (next_num, min_block_index))

            # Cerrar todos los bloques
            for block_file in blocks:
                block_file.close()

    finally:
        # Eliminar el directorio temporal y sus archivos
        shutil.rmtree(temp_dir)

# Ejemplo de uso:
input_file = 'input.txt'  # Archivo de entrada no ordenado
output_file = 'output.txt'  # Archivo de salida ordenado
block_size = 1024  # Tamaño del bloque en bytes

# Crear un archivo de entrada con datos desordenados (puedes reemplazar esto con tus propios datos)
with open(input_file, 'wb') as f:
    data = bytearray(range(255, 0, -1))  # Datos desordenados del 1 al 255
    f.write(data)

# Ordenar el archivo utilizando Straight Merging Sort
straight_merging_sort(input_file, output_file)

# Leer y mostrar el archivo ordenado
with open(output_file, 'rb') as f:
    sorted_data = f.read()
    print(sorted_data)
