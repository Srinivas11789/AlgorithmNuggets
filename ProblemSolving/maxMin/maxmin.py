#!/bin/python

import math
import os
import random
import re
import sys

# Complete the angryChildren function below.
def angryChildren(k, arr):
    
    
    # Sort Logic - 100 pass
    # taking initial and final numbers k length and finding the minimum doesnt work - 4/16
    arr.sort()
    result = 600000000000000
    # 1. No need to calculate max, min as the array is already sorted
    # 2. Consecutive sub arrays will only work as others mixes wont have minimum difference
    # print arr
    # The length of the array should be properly set, as the last 3 k numbers were not calculated due to range setting
    # which failed the 16 th case
    for i in range((len(arr)-k)+1):
        print arr[i+k-1],arr[i]
        if arr[i+k-1] - arr[i] < result:
            result = arr[i+k-1] - arr[i]
    return result
    
    """
    # BruteForce Solution - Timeout, passed only 5/16
    import itertools
    result = 6000000000
    for item in itertools.combinations(arr, r=k):
        #print item
        value = max(item) - min(item)
        if value < result:
            result = value
    return result
    """ 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    k = int(raw_input())

    arr = []

    for _ in xrange(n):
        arr_item = int(raw_input())
        arr.append(arr_item)

    result = angryChildren(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

