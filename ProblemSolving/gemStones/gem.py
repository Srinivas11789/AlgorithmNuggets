#!/bin/python

import sys

def gemstones(arr):

    # 100 pass
    # Find the intersection from array1 over array2 and array3
    count = temp = 0
    
    # Initially only 2 passed and all other failed. Reason being the existence of duplicates in the first array which is taken as reference. Using set to eradicate all the duplicates passes all the test. Good catch!
    for char in set(arr[0]):
        temp = 0
        for i in range(1,len(arr)):
            if char in arr[i]:
                temp += 1
            else:
                break
        if temp == len(arr)-1:
            count += 1
    return count
            

n = int(raw_input().strip())
arr = []
arr_i = 0
for arr_i in xrange(n):
    arr_t = str(raw_input().strip())
    arr.append(arr_t)
result = gemstones(arr)
print(result)

