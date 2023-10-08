def selection_sort(arr):
    # Recorremos la lista desde el inicio hasta el penúltimo elemento.
    for i in range(len(arr) - 1):
        # Suponemos que el elemento actual es el más pequeño.
        min_index = i
        
        # Buscamos el índice del elemento más pequeño en el resto de la lista.
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Intercambiamos el elemento actual con el elemento más pequeño encontrado.
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Ejemplo de uso:
lista = [64, 25, 12, 22, 11]
print("Lista ordenada:", lista)
selection_sort(lista)
print("Lista ordenada:", lista)
