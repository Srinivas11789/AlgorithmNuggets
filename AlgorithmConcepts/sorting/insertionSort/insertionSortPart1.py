# Insertion Sort Part 1 - Perform sort on a already sorted list
# * Take care about the element which is lowest than every other element in the list
# * Take care of properly inserting elements based on the position other elements are being shifted

#!/bin/python
from __future__ import print_function
import sys

def insertionSort1(n, arr):
    # Complete this function
    select = arr[n-1]
    for i in range(n-2,-1,-1):
        if arr[i] > select:
            arr[i+1] = arr[i]
            print(*arr)
            if i == 0:
                arr[i] = select
                print(*arr)
        if arr[i] < select:
            arr[i+1] = select
            select = arr[i]
            print(*arr)
            break
        
if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    insertionSort1(n, arr)

