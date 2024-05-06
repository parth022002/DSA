# Define a function named counting_sort that performs counting sort on a given array based on a specific exponent.
def counting_sort(arr, exp):
    n = len(arr)  # Get the length of the array
    output = [0] * n  # Initialize an output array with the same length as the input array
    count = [0] * 10  # Initialize a count array to count occurrences of digits (0 to 9)
    
    # Count the occurrences of each digit in the array
    for i in range(n):
        index = arr[i] // exp  # Get the index of the digit based on the current exponent
        count[index % 10] += 1  # Increment the count for the corresponding digit
    
    # Calculate the cumulative sum of counts
    for i in range(1, 10):
        count[i] += count[i - 1]  # Add the previous count to the current count
    
    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp  # Get the index of the digit based on the current exponent
        output[count[index % 10] - 1] = arr[i]  # Place the element in the correct position in the output array
        count[index % 10] -= 1  # Decrement the count for the corresponding digit
        i -= 1
    
    # Copy the sorted elements back to the original array
    for i in range(n):
        arr[i] = output[i]

# Define a function named radix_sort that performs radix sort on a given array.
def radix_sort(arr):
    max_value = max(arr)  # Find the maximum value in the array
    exp = 1  # Initialize the exponent to 1
    while max_value // exp > 0:  # Continue sorting until all digits have been considered
        counting_sort(arr, exp)  # Perform counting sort based on the current exponent
        exp *= 10  # Move to the next digit position by multiplying the exponent by 10

# Example usage:
my_list = [432, 8, 530, 90, 88, 231, 11, 45, 677, 199]  # Define an unsorted array
radix_sort(my_list)  # Sort the array using radix sort
print("Sorted array:", my_list)  # Print the sorted array
