
def insertion_sort(arr):
    # Comenzamos desde el segundo elemento (índice 1) hasta el final de la lista.
    for i in range(1, len(arr)):
        # Guardamos el valor actual que estamos considerando.
        current_value = arr[i]
        # Inicializamos un índice para recorrer hacia la izquierda.
        j = i - 1
        
        # Movemos los elementos mayores que el valor actual hacia la derecha.
        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Colocamos el valor actual en su posición correcta.
        arr[j + 1] = current_value

# Ejemplo de uso:

lista = [12, 11, 13, 5, 6]
print("Lista desordenada:", lista)
insertion_sort(lista)
print("Lista ordenada:", lista)
