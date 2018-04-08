#!/bin/python

import sys

def migratoryBirds(n, ar):
    arr = {}
    for item in ar:
        if item not in arr:
            arr[item] = 0
        arr[item] += 1
        
    maxi = max(arr.values())
    select = 60000000
    
    for key, value in arr.items():
        if value == maxi:
            if key < select:
                select = key
    return select

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = migratoryBirds(n, ar)
print(result)

