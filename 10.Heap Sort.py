def heapify(arr, n, i):
    largest = i  # Initialize the largest as the root
    left = 2 * i + 1  # Calculate the index of the left child
    right = 2 * i + 2  # Calculate the index of the right child

    # Check if left child exists and is greater than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the root, swap it with the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap elements
        # Recursively heapify the affected subtree
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)  # Get the length of the array

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)  # Heapify starting from the last non-leaf node

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root (max element) with the last element
        heapify(arr, i, 0)  # Heapify the reduced heap

# Example usage:
my_list = [12, 11, 13, 5, 6, 7]  # Define an unsorted array
heap_sort(my_list)  # Sort the array using heap sort
print("Sorted array:", my_list)  # Print the sorted array