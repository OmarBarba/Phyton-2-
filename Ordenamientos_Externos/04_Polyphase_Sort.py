import os
import shutil
import heapq
import glob

def polyphase_sort(input_file, output_file, block_size=1024):
    # Crear un directorio temporal para almacenar los bloques y fases
    temp_dir = "temp"
    os.makedirs(temp_dir, exist_ok=True)

    try:
        # Dividir el archivo de entrada en bloques y crear fases iniciales
        with open(input_file, 'rb') as f:
            block_count = 0
            while True:
                block = f.read(block_size)
                if not block:
                    break
                block = list(block)
                block.sort()
                phase_file = os.path.join(temp_dir, f'phase_0_{block_count}.dat')
                with open(phase_file, 'wb') as phase_f:
                    phase_f.write(bytes(block))
                block_count += 1

        # Realizar las fases de Polyphase Sort
        phase = 0
        while block_count > 1:
            # Determinar el nombre de los archivos de entrada y salida para esta fase
            input_phase_pattern = os.path.join(temp_dir, f'phase_{phase}*.dat')
            output_phase_pattern = os.path.join(temp_dir, f'phase_{phase + 1}_*.dat')
            input_phase_files = sorted(glob.glob(input_phase_pattern))
            output_phase_files = [os.path.join(temp_dir, f'phase_{phase + 1}_{i}.dat') for i in range(block_count // 2)]

            # Fusionar y distribuir los bloques en esta fase
            polyphase_merge(input_phase_files, output_phase_files)

            # Actualizar el contador de bloques y la fase
            block_count = len(output_phase_files)
            phase += 1

        # Mover el archivo final ordenado a la ubicación de salida especificada
        final_sorted_file = os.path.join(temp_dir, output_phase_files[0])
        shutil.move(final_sorted_file, output_file)

    finally:
        # Eliminar el directorio temporal y sus archivos
        shutil.rmtree(temp_dir)

def polyphase_merge(input_files, output_files):
    # Crear montículos (heaps) para cada archivo de entrada
    input_heaps = [HeapFile(file) for file in input_files]

    # Abrir los archivos de salida para escritura
    output_handles = [open(file, 'wb') for file in output_files]

    while any(input_heaps):
        min_heap = min(input_heaps, key=lambda heap: heap.peek())
        min_value = min_heap.pop()

        # Escribir el valor mínimo en el archivo de salida correspondiente
        output_index = input_heaps.index(min_heap)
        output_handles[output_index].write(min_value.to_bytes(1, byteorder='big'))

    # Cerrar todos los archivos de salida
    for handle in output_handles:
        handle.close()

class HeapFile:
    def __init__(self, file):
        self.file = open(file, 'rb')
        self.buffer = []
        self.read_block()

    def read_block(self):
        self.buffer = list(self.file.read(block_size))
        self.buffer.reverse()

    def peek(self):
        if not self.buffer:
            self.read_block()
        return self.buffer[-1]

    def pop(self):
        if not self.buffer:
            self.read_block()
        return self.buffer.pop()

# Ejemplo de uso:
input_file = 'input.txt'  # Archivo de entrada no ordenado
output_file = 'output.txt'  # Archivo de salida ordenado
block_size = 1024  # Tamaño del bloque en bytes

# Crear un archivo de entrada con datos desordenados (puedes reemplazar esto con tus propios datos)
with open(input_file, 'wb') as f:
    data = bytearray(range(255, 0, -1))  # Datos desordenados del 1 al 255
    f.write(data)

# Ordenar el archivo utilizando Polyphase Sort
polyphase_sort(input_file, output_file)

# Leer y mostrar el archivo ordenado
with open(output_file, 'rb') as f:
    sorted_data = f.read()
    print(sorted_data)
