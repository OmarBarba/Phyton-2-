#Ordenamiento por Tim Sort
def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

def merge(arr, left, middle, right):
    len_left = middle - left + 1
    len_right = right - middle

    left_arr = [0] * len_left
    right_arr = [0] * len_right

    for i in range(len_left):
        left_arr[i] = arr[left + i]

    for i in range(len_right):
        right_arr[i] = arr[middle + 1 + i]

    i = j = 0
    k = left

    while i < len_left and j < len_right:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len_left:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len_right:
        arr[k] = right_arr[j]
        j += 1
        k += 1

def tim_sort(arr):
    min_run = 32
    n = len(arr)

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            middle = min(n - 1, start + size - 1)
            end = min(n - 1, start + size * 2 - 1)
            if middle < end:
                merge(arr, start, middle, end)
        size *= 2

# Ejemplo de uso:
lista = [64, 34, 45, 12, 12, 11, 66]
print("Lista desordenada:", lista)
tim_sort(lista)
print("Lista ordenada:   ", lista)