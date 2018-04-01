#!/bin/python

import sys

def kangaroo(x1, v1, x2, v2):
    
    # First kangaroo starting point is x1 and it jumps v1 everytime
    
    # point = x1
    # jump = v1
    dest1 = x1 + v1
    
    # Second kangaroo starting point is x2 and it jumps v2 everytime
    dest2 = x2 + v2    
    
    # Brute force method
    count = 0
    while dest1 != dest2:
        dest1 = dest1 + v1
        dest2 = dest2 + v2
        count += 1
        if count > 100000:
            return "NO"
        
    return "YES"
    
x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)

