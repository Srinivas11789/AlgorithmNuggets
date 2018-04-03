#!/bin/python

import sys

def bigSorting(arr):
    
    # built in sort with key
    # Sorted function built in python is of complexity O(nlogn) which passes all the tests
    return sorted(arr, key = int)
    
    """
    # Timeout in certain testcases
    # Built In Sort
    for i in range(n):
        arr[i] = int(arr[i])
    return sorted(arr)
    """
    
    """
    # Bubble Sort - Timeout last 3 cases
    n = len(arr)
    a = arr
    temp = None
    for i in range(n):
        for j in range(n-1):
            if int(a[j]) > int(a[j+1]):
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    return a
    """
    
    """
    # Timeout for last 3 testcases
    # Insertion sort
    n = len(arr)
    a = arr
    temp = None
    for i in range(n):
        select = a[i]
        for j in range(i+1,n):
            #print i, j
            if int(a[i]) > int(a[j]):
                temp = a[j]
                a[j] = a[i]
                a[i] = temp
            #print select, a
    return a
    """
            

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = []
    arr_i = 0
    for arr_i in xrange(n):
        arr_t = str(raw_input().strip())
        arr.append(arr_t)
    result = bigSorting(arr)
    print "\n".join(map(str, result))



