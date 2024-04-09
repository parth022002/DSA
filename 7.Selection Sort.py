def selection_sort(arr):
    # Get the length of the array.
    n = len(arr)
    # Iterate over the array, excluding the last element.
    for i in range(n - 1):
        # Assume the current index is the index of the minimum element.
        min_index = i
        # Iterate over the unsorted part of the array to find the minimum element.
        for j in range(i + 1, n):
            # If the current element is smaller than the current minimum element,
            # update the index of the minimum element.
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the minimum element with the element at index i,
        # effectively placing the minimum element at its correct position.
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Example usage:
my_list = [64, 25, 12, 22, 11]
selection_sort(my_list)
print("Sorted array:", my_list)