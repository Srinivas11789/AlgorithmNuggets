#!/bin/python

import sys

def countingSort(arr):
    
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

    # Trying to use a list and perform the operation - pass 100
    n = len(arr)
    counts = [0]*100
    for i in range(n):
        counts[arr[i]] += 1
    return counts

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    result = countingSort(arr)
    print " ".join(map(str, result))



