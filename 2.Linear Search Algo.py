# Define a function named search that takes an array, its length, and a target element as input.
def search(arr, N, target):
    # Iterate through the array
    for i in range(0, N):
        # Check if the current element is equal to the target element
        if (arr[i] == target):
            # If found, return the index of the target element
            return i
    # If the target element is not found, return -1
    return -1

# Driver code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]  # Define an array
    target = 10  # Define the target element to search for
    N = len(arr)  # Get the length of the array

    # Call the search function to find the target element in the array
    result = search(arr, N, target)
    if(result == -1):
        print("Element is not present in array")  # If result is -1, element is not present
    else:
        print("Element is present at index", result)  # If result is not -1, element is present at index 'result'
