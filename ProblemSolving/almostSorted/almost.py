#!/bin/python

import math
import os
import random
import re
import sys

# 100 pass
# Complete the almostSorted function below.
def almostSorted(arr):
    n = len(arr)
    sort_arr = sorted(arr)
    # Swap 2 elements
    diff = 0
    result = []
    if arr == sort_arr:
        print "yes"
    for i in range(n):
        if arr[i] != sort_arr[i]:
            result.append(i)
            diff += 1
    if diff == 2:
        arr[result[0]],arr[result[1]] = arr[result[1]], arr[result[0]]
        if sort_arr == arr:
            print "yes\n"+"swap "+str(result[0]+1)+" "+str(result[1]+1)
        else:
            print "no"
    elif diff > 2:
        if sort_arr == arr[:result[0]]+arr[result[0]:result[-1]+1][::-1]+arr[result[-1]+1:]:
            print "yes\n"+"reverse "+str(result[0]+1)+" "+str(result[-1]+1)
        else:
            print "no"
    else:
        print "no"
if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    almostSorted(arr)

