#!/bin/python

import sys

def countingSort(arr):
    #!/bin/python
    
    #
    # List Method 
    # Trying to use a list and perform the operation - pass 100
    # we have the count of each integer from 1 to 100 placed in the array with 
    # * key or index of the array 0-100 being the value
    # * value being the number of times it occured
    # * when you want the sorted array, just going through the count array and printing the indexes* number of occurence of the value will return the sorted array
    #
    # same as counting sort 1
    n = len(arr)
    counts = [0]*100
    for i in range(n):
        counts[arr[i]] += 1
    #return counts
    #print counts
    
    # logic to print the index(which is the element) * number of times of occurences
    result = []
    for i in range(100):
        if i in arr:
            # Observe the diff between append and extend - extend extends the list with elements from another list while append add the list to the list element creating a list of lists
            result.extend([i for j in range(counts[i])])
    return result
    
    """
    # 100 pass, using counts
    n = len(arr)
    result = []
    for i in range(100):
        result.append(arr.count(i))
    return result
    """
    
    """
    # Trying using dictionary if 100 pass possible - pass 100
    n = len(arr)
    counts = {}
    for i in range(100):
        counts[i] = 0
    for i in range(n):
        if arr[i] in counts:
            counts[arr[i]] += 1
    return counts.values()
    """

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    result = countingSort(arr)
    print " ".join(map(str, result))



if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    result = countingSort(arr)
    print " ".join(map(str, result))



