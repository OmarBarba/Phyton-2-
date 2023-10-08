import heapq

def natural_merge_sort(input_file, output_file):
    # Leer el archivo de entrada y dividirlo en secuencias ordenadas
    with open(input_file, 'rb') as f:
        sequences = []
        current_sequence = []
        prev_value = None

        while True:
            byte = f.read(1)
            if not byte:
                break

            value = int.from_bytes(byte, byteorder='big')

            if prev_value is None or prev_value <= value:
                current_sequence.append(value)
            else:
                sequences.append(current_sequence)
                current_sequence = [value]

            prev_value = value

        sequences.append(current_sequence)

    # Fusionar las secuencias ordenadas hasta que quede una sola secuencia
    while len(sequences) > 1:
        sequences = [list(heapq.merge(seq1, seq2)) for seq1, seq2 in zip(sequences[::2], sequences[1::2])]
    
    # Escribir la secuencia ordenada en el archivo de salida
    with open(output_file, 'wb') as f:
        for value in sequences[0]:
            f.write(value.to_bytes(1, byteorder='big'))

# Ejemplo de uso:
input_file = 'input.txt'  # Archivo de entrada con datos desordenados
output_file = 'output.txt'  # Archivo de salida ordenado

# Crear un archivo de entrada con datos desordenados (puedes reemplazar esto con tus propios datos)
with open(input_file, 'wb') as f:
    data = bytearray([5, 3, 7, 1, 8, 2, 4, 6])  # Datos desordenados
    f.write(data)

# Ordenar el archivo utilizando Natural Merge Sort
natural_merge_sort(input_file, output_file)

# Leer y mostrar el archivo ordenado
with open(output_file, 'rb') as f:
    sorted_data = f.read()
    print(sorted_data)