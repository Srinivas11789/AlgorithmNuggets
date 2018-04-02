#!/bin/python

import sys

def maximizingXor(l, r):
    
    # Direct Brute force method - 100
    maxi = -600000
    for i in range(l,r+1):
        for j in range(l,r+1):
            value = i^j
            if value > maxi:
                maxi = value
    return maxi

    
                

if __name__ == "__main__":
    l = int(raw_input().strip())
    r = int(raw_input().strip())
    result = maximizingXor(l, r)
    print result

