#!/bin/python

import sys

def solve(n):
    count = 0
    # Xor is sum without carry 
    # Solution - count the number of zeros and raise it to the power of 2
    # because, we got to search of addition of numbers without occurence of a carry to make them equal, for example with     # 0 exist then we need 1 to be added, same vice versa. Ultimately this reduces to the count of the zeros or combinations that can occur with zeros. hence count of zeros raised to the power of 2
    #  Even after all pass testcase 1 failed, as usual the zero condition where the n=0 failed
    if n == 0:
    # When n is 0, then there is one possibility
        return 1
    binary = bin(n)
    #print binary - remember to eliminate 0b string of binary in python
    count = binary[2:].count('0')
    #print count
    return 2**count
    
    """
    # 3 testcase fail with runtime error - use bit manipulation to your advantage
    # Good decision on n+1 to pass all the testcases 
    # Runtime Error -> Memory error when running with large number - 
    for i in range(n+1):
        sumi = i + n
        xori = i ^ n
        if sumi == xori:
            count += 1
    return count
    """
    
n = long(raw_input().strip())
result = solve(n)
print(result)

