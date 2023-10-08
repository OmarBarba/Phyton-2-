#Ordenamiento por Heap Sort
def heapify(arr, n, i):
    # Inicializamos el índice más grande como la raíz del heap
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Comparamos con el hijo izquierdo
    if left_child < n and arr[i] < arr[left_child]:
        largest = left_child

    # Comparamos con el hijo derecho
    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child

    # Si el índice más grande no es la raíz, intercambiamos y continuamos heapify
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Llamada recursiva a heapify en el subárbol afectado
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Construimos un max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraemos elementos uno por uno del heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambiamos el máximo (en la raíz) con el último elemento
        heapify(arr, i, 0)

# Ejemplo de uso:
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista desordenada:", lista)
heap_sort(lista)
print("Lista ordenada:   ", lista)
