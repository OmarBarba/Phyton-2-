# Ordenamiento Quick_sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # Elegimos el primer elemento como pivote
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Ejemplo de uso:
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista desordenada:", lista)
sorted_list = quick_sort(lista)
print("Lista ordenada:   ", sorted_list)