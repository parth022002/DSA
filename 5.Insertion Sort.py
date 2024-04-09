def insertion_sort(arr):
    # Iterate over the array starting from the second element (index 1).
    for i in range(1, len(arr)):
        # Store the current element as the key.
        key = arr[i]
        # Initialize a variable `j` to the index just before the key.
        j = i - 1
        # Iterate backwards through the sorted portion of the array and shift elements greater than the key to the right.
        while j >= 0 and key < arr[j]:
            # Shift the element at index `j` one position to the right.
            arr[j + 1] = arr[j]
            # Move to the previous element in the sorted portion.
            j -= 1
        # Insert the key into its correct position in the sorted portion.
        arr[j + 1] = key


# Testing the function
numbers = [64, 25, 12, 22,  11]
insertion_sort(numbers)
print("Sorted array is:", numbers)