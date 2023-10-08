# Ordenamiento bubble_sort
def bubble_sort(arr):
    n = len(arr)
    
    # Realizamos n-1 pasadas a través de la lista.
    for i in range(n - 1):
        # En cada pasada, comparamos y, si es necesario, intercambiamos elementos.
        for j in range(0, n - i - 1):
            # Si el elemento actual es mayor que el siguiente elemento, los intercambiamos.
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Ejemplo de uso:
lista = [64, 34, 25, 12, 22, 11, 90]

print("Lista desordenada:", lista)
bubble_sort(lista)
print("Lista ordenada:   ", lista)