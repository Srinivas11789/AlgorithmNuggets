#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    #
    # Write your code here.
    #
    
    # Find LCM
    # prod = A number which is a factor of all the elements of a 
    # testcase 3 fails because max is assumed to be the lcm of the array, tc3 has 3 6 9 such that 6 is the LCM
    prod = 1
    #for num in a:
    #    prod *= num
    prod = max(a)
    
    # Find GCD
    result = []
    i = 1
    curr = prod
    while curr <= min(b):
        factor = 1
        for num in b:
            if num%curr == 0:
                factor = factor & 1
            else:
                factor = factor & 0
        
        print (factor,curr)
        if factor == 1:
            result.append(curr)
        i += 1
        curr = prod * i
    
    return len(result)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = map(int, raw_input().rstrip().split())

    b = map(int, raw_input().rstrip().split())

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()

