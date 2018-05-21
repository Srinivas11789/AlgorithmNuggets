### Pending problem

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the largestPermutation function below.
def largestPermutation(k, arr):
    
    # 10/15 test cases passed
    i = 0
    arr1 = sorted(arr)
    
    if k >= len(arr):
        return arr1[::-1]
    
    while k > 0:
        maxi = max(arr[i:])
        index = arr.index(maxi)
        arr[index], arr[i] = arr[i], arr[index]
        if arr == arr1[::-1]:
            return arr
        i += 1
        k -= 1
    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = map(int, raw_input().rstrip().split())

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

