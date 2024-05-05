# Define the merge_sort function that takes an array as input and returns the sorted array.
def merge_sort(arr):
    # Check if the array length is 1 or less, which means it's already sorted.
    if len(arr) <= 1:
        return arr
    
    # Divide the array in two halves.
    mid = len(arr) // 2
    left_half = arr[:mid]  # Left half of the array
    right_half = arr[mid:]  # Right half of the array

    # Recursively sort each half of the array.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves using the merge function.
    return merge(left_half, right_half)

# Define the merge function that merges two sorted arrays into one sorted array.
def merge(left, right):
    result = []  # Initialize an empty array to store the merged result
    i = j = 0  # Initialize variables to track the indices of left and right arrays
    
    # Move through the lists until we have run out of elements in either list.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:  # Compare elements from left and right arrays
            result.append(left[i])  # Append the smaller element to the result array
            i += 1  # Move to the next element in the left array
        else:
            result.append(right[j])  # Append the smaller element to the result array
            j += 1  # Move to the next element in the right array
    
    # Append any remaining elements from the left list, if any.
    result += left[i:]
    
    # Append any remaining elements from the right list, if any.
    result += right[j:]
    
    return result  # Return the merged and sorted array

# Testing the function
my_list = [12, 11, 13, 5, 6, 7]  # Define an unsorted array
sorted_list = merge_sort(my_list)  # Sort the array using merge sort
print("Sorted array:", sorted_list)  # Print the sorted array
