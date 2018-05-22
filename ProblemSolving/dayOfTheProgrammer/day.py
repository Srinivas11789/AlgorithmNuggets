#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(year):
    # 1700 -> 2700
    # 256th day?
    
    # Months of the year
    months = [31,0,31,30,31,30,31,31,30,31,30,31]

    if year > 1918: # Gregorian Calendar
        
        # Leap year is divisible by 400 or 4 and not 100
        if year%400 == 0 or (year%4 ==0 and year%100 != 0):
            months[1] = 29
        else:
            months[1] = 28
    elif year == 1918: # Transition ==> 1918
        months[1] = 15
    else: # Julian Calendar
        # Leap year is divisible by 400 
        if year%4 == 0:
            months[1] = 29
        else:
            months[1] = 28
            
    # Total number of days calculation
    total = 0
    i = 0 
    while total < 256:
            if total + months[i] > 256:
                break
            total += months[i]
            i += 1
    devDay = 256 - total
    return str(devDay).zfill(2)+"."+str(i+1).zfill(2)+"."+str(year)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(raw_input())

    result = solve(year)

    fptr.write(result + '\n')

    fptr.close()

