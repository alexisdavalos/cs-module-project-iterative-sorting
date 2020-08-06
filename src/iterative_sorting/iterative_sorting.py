# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range (cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        # Your code here
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # compare first and second items. swap items if first item is bigger than second
    for element in arr:
        for i in range (0, len(arr) -1):
            next_item = i + 1
            if arr[i] > arr[next_item]:
                #swap current and next
                arr[i], arr[next_item] = arr[next_item], arr[i]
            # move on to next item and compare again in loop
    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7, 6]
print(bubble_sort(arr1))
# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
