import heapq

def balanced_multiway_merge(input_files, output_file, block_size):
    # Abrir los archivos de entrada y el archivo de salida
    input_handles = [open(file, 'rb') for file in input_files]
    output_handle = open(output_file, 'wb')

    # Leer el primer bloque de cada archivo y almacenarlos en el montículo
    min_heap = []
    for i, handle in enumerate(input_handles):
        data = handle.read(block_size)
        if data:
            num = int(data)
            min_heap.append((num, i))

    # Convertir la lista en un montículo (heap)
    heapq.heapify(min_heap)

    while min_heap:
        # Obtener el menor valor actual y su índice de archivo asociado
        min_value, file_index = heapq.heappop(min_heap)

        # Escribir el valor mínimo en el archivo de salida
        output_handle.write(str(min_value).encode('utf-8'))
        output_handle.write(b'\n')  # Agregar una nueva línea

        # Leer el siguiente bloque del archivo correspondiente
        data = input_handles[file_index].read(block_size)
        if data:
            num = int(data)
            heapq.heappush(min_heap, (num, file_index))

    # Cerrar todos los archivos
    for handle in input_handles:
        handle.close()
    output_handle.close()

# Generar un archivo de entrada con datos desordenados (puedes reemplazar esto con tus propios datos)
input_data = [8, 2, 6, 1, 4, 7, 5, 3]
with open('input.txt', 'w') as f:
    f.write('\n'.join(map(str, input_data)))

# Archivos de entrada con datos desordenados
input_files = ['input.txt']

# Archivo de salida donde se almacenará la salida ordenada
output_file = 'output.txt'

# Tamaño de bloque en bytes
block_size = 4  # Cada número tiene un tamaño de 4 bytes

# Aplicar el ordenamiento externo por Balanced Multiway Merging
balanced_multiway_merge(input_files, output_file, block_size)

# Leer y mostrar el archivo de salida ordenado
with open(output_file, 'r') as f:
    sorted_data = [int(line.strip()) for line in f.readlines()]
    print("Secuencia ordenada:", sorted_data)
