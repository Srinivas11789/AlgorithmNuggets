#!/bin/python

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    
    # 100 pass - Optimized Manner - Use Math instead of plotting
    
    cycle = 3
    while t > cycle:
        t -= cycle
        cycle = 2*cycle
    return cycle - t + 1
    
    """
    #BruteForce - Memory Error - optimization required
    cycle = 3
    current = 3
    for i in range(1,t):
        print i, cycle, current
        if current == 1:
            cycle = 2*cycle
            current = cycle
        else:
            current -= 1
        
    return current
    """
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()

