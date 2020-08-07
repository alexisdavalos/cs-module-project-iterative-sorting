arr = [2,6,8,3,4,1,9,5,11,7] 

def insert_sort(nums):
    # 1st element is a sorted sublist
    # loop through unsorted elements
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i
        #  while 'n' > LHS or index of 'n' is NOT 0 
        while j > 0 and temp < nums[j-1]:
            nums[j] = nums[j-1]
            j -= 1
        # swap
        nums[j] = temp
    # return sorted list
    return nums

# Driver Code
print(f'original arr: {arr}')        
print(f'sorted arr: {insert_sort(arr)}')


