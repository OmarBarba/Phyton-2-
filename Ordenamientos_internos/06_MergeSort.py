def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Dividir la lista en dos mitades
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Llamada recursiva para ordenar las mitades
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Combinar las mitades ordenadas
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Ejemplo de uso:
lista = [23, 84, 25, 12, 120, 11, 90]
print("Lista desordenada:", lista)
sorted_list = merge_sort(lista)
print("Lista ordenada:   ", sorted_list)