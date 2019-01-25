# Binary Search

# Recursive
def binary_search(array, target, start_index):

    n = len(array)
    mid = n//2

    if n == 0:
        return "Not Found!"

    #print start_index, mid, target, array
    
    if array[mid] == target:
        return "Found! at " + str(mid + start_index)
    elif array[mid] > target:
        if start_index > 0:
            return binary_search(array[:mid], target, start_index)
        else:
            return binary_search(array[:mid], target, 0)
    else:
        return binary_search(array[mid+1:], target, start_index+mid+1)

# 2 pointer
def binary_search2(array, target):

    # Initial values
    left = 0
    right = len(array)

    # Iterate until left < right
    while left < right:
        # Mid point
        mid = (left + right)//2
        #print left, right, mid, array
        if array[mid] == target:
            return "Found! at " + str(mid)
        elif array[mid] > target:
            right = mid
        else:
            left = mid+1
    return "Not Found!"

array = [1,2,3,4,5,6,7,8,9]
print binary_search(array, 1, 0), binary_search(array, 9, 0), binary_search(array, 10, 0)
print binary_search2(array, 1), binary_search2(array, 9), binary_search2(array, 10)

