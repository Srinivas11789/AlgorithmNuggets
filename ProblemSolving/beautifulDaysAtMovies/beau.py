####### is_integer is a good extension of float to verify whether the float number is integer or not

#!/bin/python

import sys

def beautifulDays(i, j, k):
    # Complete this function
    count = 0
    for i in range(i,j+1):
        if (abs(i-int(str(i)[::-1]))/float(k)).is_integer():
            count += 1
    return count
        

if __name__ == "__main__":
    i, j, k = raw_input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    result = beautifulDays(i, j, k)
    print result

