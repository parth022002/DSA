# Define a function named binary_search that performs binary search on a sorted array.
def binary_search(arr, target):
    left = 0  # Initialize the left pointer to the first index of the array
    right = len(arr) - 1  # Initialize the right pointer to the last index of the array

    # Perform binary search until left pointer is less than or equal to right pointer
    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index

        if arr[mid] == target:  # If the middle element is equal to the target
            return mid  # Return the index of the target element
        elif arr[mid] < target:  # If the middle element is less than the target
            left = mid + 1  # Update the left pointer to search in the right half
        else:  # If the middle element is greater than the target
            right = mid - 1  # Update the right pointer to search in the left half
    
    return -1  # Return -1 if the target element is not found

# Define an unsorted list
my_list = [10, 2, 9, 7, 5, 6, 4, 8, 3, 1]
target_element = 7  # Define the target element to search for

my_list.sort()  # Sort the list before performing binary search
result = binary_search(my_list, target_element)  # Call the binary_search function

# Check if the target element is found or not and print the result accordingly
if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")
