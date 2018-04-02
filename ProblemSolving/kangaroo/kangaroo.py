#!/bin/python

import sys

def kangaroo(x1, v1, x2, v2):
    
    # First kangaroo starting point is x1 and it jumps v1 everytime
    
    # point = x1
    # jump = v1
    dest1 = x1 + v1
    
    # Second kangaroo starting point is x2 and it jumps v2 everytime
    dest2 = x2 + v2    
    
    """
    # Brute force method
    count = 0
    while dest1 != dest2:
        dest1 = dest1 + v1
        dest2 = dest2 + v2
        count += 1
        if count > 100000:
            return "NO"
    return "YES"
    """
    
    # Optimized method
    
    """
    # Eliminating the condition when kang1 cannot reach kan2   
    if x2 > x1 and v2 >= v1:
        return "NO"
    # Eliminating even odd contition when they wont reach each other
    dest1_type = "odd"
    dest2_type = "odd"
    if (dest1%2 != 0 and v1%2 == 0): 
        dest1_type = "odd"
    else:
        dest1_type = "even"
    if (dest2%2 != 0 and v1%2 == 0):
        dest1_type = "odd"
    else:
        dest1_type = "even"
    """
    
    # Using Arithmetic Progression -- Nice idea to solve it.... good thinking
    # nth term formula is a+(n-1)d, both the nth term should be same, hence solve for n 
    # negative n results in NO
    
    # Subtract equation 1 and equation 2
    suba = x2 - x1
    subn = v2 - v1
    sub1 = -v2 + v1
    n = -(suba+sub1)
    
    if subn < 0:
        subn = -subn
        n = -n
        
    #print n,subn
    if n > 0 and n%subn == 0:
        return "YES"
    else:
        return "NO"
  
    
x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)

