#!/bin/python

import sys

def pairs(k, arr):
    # Complete this function
    counts  = 0
    for i in range(len(arr)):
        value = k - arr[i]
        if value in arr[i+1:]:
            counts += 1
    return counts
    """
    # Timeout 
    counts = {}
    pairs = 0
    for item in arr:
        if item not in counts:
            counts[item] = 0
        counts[item] = abs(k-item)
    #print(counts)
    for key, value in counts.items():
        if key in arr and value in arr and abs(key-value) == k:
            #print(key,value)
            pairs += 1
    return pairs
    """     

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = map(int, raw_input().strip().split(' '))
    result = pairs(k, arr)
    print result

