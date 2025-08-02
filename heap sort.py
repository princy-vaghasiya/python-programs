def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
        
def heap_sort(arr):
    n = len(arr)
    for i in reversed(range(n // 2)):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)

arr = [3,4,1,6,8,5]
print("Original array:", arr)
heap_sort(arr)
print("Sorted array(ascending):", arr)
