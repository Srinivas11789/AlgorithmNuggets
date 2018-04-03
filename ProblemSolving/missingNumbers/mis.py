#!/bin/python
# Missing number between 2 arrays - 100 pass

import sys

def missingNumbers(arr, brr):
    # Brute force with brr length which is greater
    freq = {}
    for i in range(len(brr)):
        if brr[i] not in freq:
            freq[brr[i]] = 1
        else:
            freq[brr[i]] += 1
        if i < len(arr):
            if arr[i] not in freq:
                freq[arr[i]] = -1
            else:
                freq[arr[i]] -= 1
    result = []
    for key, value in freq.items():
        if value > 0:
            result.append(key)
    return result
    
        

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    m = int(raw_input().strip())
    brr = map(int, raw_input().strip().split(' '))
    result = missingNumbers(arr, brr)
    print " ".join(map(str, result))



