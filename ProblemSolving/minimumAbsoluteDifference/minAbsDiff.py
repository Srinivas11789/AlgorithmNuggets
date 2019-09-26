#!/bin/python

import sys

def minimumAbsoluteDifference(n, arr):
    # Complete this function
    # O(N2)
    """
    min = 100
    for i in range(n):
        for j in range(i+1,n):
            diff = abs(arr[i] - arr[j])
            if diff < min:
                min = diff
    return min
    """

    # O(N)
    """
    min = 10 ** 10 # or float('inf')
    arr = sorted(arr)
    for i in range(n-1):
        diff = abs(arr[i] - arr[i+1])
        if diff < min:
            min = diff
    return min
    """

    # O(logN) assuming sorted or sort() uses best sorting
    arr.sort()
    return arr[1]-arr[0]
        

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    result = minimumAbsoluteDifference(n, arr)
    print result
