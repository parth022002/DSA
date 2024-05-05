# Define the partition function that partitions the array around a pivot element.
def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1  # Initialize the index of the smaller element
    
    # Iterate through the array from 'low' to 'high-1'
    for j in range(low, high):
        if arr[j] < pivot:  # If current element is smaller than the pivot
            i += 1  # Increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap arr[i] and arr[j]
    
    # Swap the pivot element with the element at the partition index
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1  # Return the partition index

# Define the quick_sort function that implements the quicksort algorithm recursively.
def quick_sort(arr, low, high):
    if low < high:  # If there are more than one element to be sorted
        pivot_index = partition(arr, low, high)  # Get the partition index
        # Recursively sort elements before and after the partition index
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

# Example usage:
my_list = [10, 7, 8, 9, 1, 5]  # Define an unsorted array
quick_sort(my_list, 0, len(my_list) - 1)  # Sort the array using quicksort
print("Sorted array:", my_list)  # Print the sorted array
