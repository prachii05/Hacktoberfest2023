def heapify(arr, n, i):
    largest = i  # Initialize the largest element as the root
    left = 2 * i + 1
    right = 2 * i + 2

    # If the left child exists and is greater than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If the right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change the root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap the root (max element) with the last element
        heapify(arr, i, 0)

# Example usage
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array is:", arr)
