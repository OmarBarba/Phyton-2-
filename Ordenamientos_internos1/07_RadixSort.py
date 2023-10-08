def radix_sort(arr):
    # Encontrar el número máximo para saber cuántos dígitos tiene
    max_num = max(arr)
    exp = 1
    
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Contar la frecuencia de cada dígito en el rango [0-9]
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Calcular las posiciones finales de los elementos ordenados
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construir el array de salida
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copiar el array de salida al array original
    for i in range(n):
        arr[i] = output[i]

# Ejemplo de uso:
lista = [170, 45, 75, 90, 802, 24, 2, 66]
print("Lista desordenada:", lista)
radix_sort(lista)
print("Lista ordenada:   ", lista)
