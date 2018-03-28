#!/bin/python

import sys

def lonely_integer(a):
    
    # 100 percent pass
    # Logic1: Easiest and out of the box would be to follow dictionary method
    measure = {}
    for i in range(len(a)):
        if a[i] not in measure:
            measure[a[i]] = 0
        measure[a[i]] += 1
    
    for key, value in measure.items():
        if value == 1:
            return key
    return 0
    
    
    """
    # Not so good logic
    # Logic2: Else track the method with O(N) loop measuring the existence in the array
    for i in range(len(a)):
        new = a[i+1:]
        print new, a[i]
        #if len(new) == 1:
        #   return 
        if a[i] not in new:
            return a[i]
        else:
            new = a[i+]
    return 0
    """
    

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print lonely_integer(a)

