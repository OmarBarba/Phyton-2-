#Ordenamiento por Shell Sort

def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Comenzamos con un espacio grande y lo reducimos gradualmente

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Realizamos la inserción de manera similar al Insertion Sort
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2  # Reducimos el espacio en cada iteración

# Ejemplo de uso:
lista = [64, 94, 25, 12, 34, 12, 90]
print("Lista desordenada:", lista)
shell_sort(lista)
print("Lista ordenada:   ", lista)