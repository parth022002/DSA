def search(arr, N, target):
    for i in range(0, N):
        if (arr[i] == target):
            return i
    return -1


# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    target = 10
    N = len(arr)

    # Function call
    result = search(arr, N, target)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)
