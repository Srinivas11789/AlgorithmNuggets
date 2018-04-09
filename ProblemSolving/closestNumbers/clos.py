#!/bin/python

import sys

def closestNumbers(arr):
    arr = sorted(arr)
    mini = 600000000
    result = []
    for i in range(len(arr)-1):
        value = arr[i+1] - arr[i]
        #print value
        if value < mini:
            mini = value
            result = [arr[i], arr[i+1]]
        elif value == mini:
            result.append(arr[i])
            result.append(arr[i+1])
        else:
            pass
        #print mini
    return result
    

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    result = closestNumbers(arr)
    print " ".join(map(str, result))



