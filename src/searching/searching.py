def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if(arr[i] == target):
            return arr[i]
    return -1;

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(linear_search(arr1, 2))


# sorted data
arr2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (low+high)//2
        if target < arr[middle]:
            high = middle-1
        elif target > arr[middle]:
            low = middle + 1
        else:
            return middle


    return -1  # not found
print(binary_search(arr2, 9))