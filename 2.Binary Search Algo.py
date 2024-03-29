def binary_search(arr,target):
    left = 0
    right = len(arr) -1

    while left <= right:
        mid = (left+right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid -1
    return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_element = 7
result = binary_search(my_list, target_element)
if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")