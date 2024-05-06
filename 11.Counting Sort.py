# Define a function named counting_sort that implements the counting sort algorithm.
def counting_sort(arr):
    # Find the maximum value in the array to determine the range of counts needed.
    max_value = max(arr)
    # Initialize a list 'counts' to store the count of occurrences of each value in the input array.
    counts = [0] * (max_value + 1)
    # Count the occurrences of each element in the input array and store the counts in 'counts'.
    for num in arr:
        counts[num] += 1
    # Modify 'counts' to store the cumulative counts of elements up to each index.
    # Calculate the prefix sum of the counts array
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    # Initialize an output array with the same length as the input array.
    output = [0] * len(arr)
    # Iterate over the input array in reverse order to place elements in sorted order.
    for num in reversed(arr):
        # Place the element 'num' at the correct position in the output array based on its count.
        output[counts[num] - 1] = num
        # Decrement the count of 'num' in 'counts' as it has been placed in the output array.
        counts[num] -= 1
    # Return the sorted output array.
    return output

# Example usage:
my_list = [2, 1, 1, 0, 2, 5, 4, 0, 2, 8, 7, 7, 9, 2, 0, 1, 9]  # Define an unsorted array
sorted_list = counting_sort(my_list)  # Sort the array using counting sort
print("Sorted array:", sorted_list)  # Print the sorted array
