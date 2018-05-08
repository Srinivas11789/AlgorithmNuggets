#!/bin/python

import sys

def saveThePrisoner(n, m, s):
    # Complete this function
    
    # n - no of prisoner
    # m - no of sweets
    # s - where to start
    
    """
    # Memory Error - Optimize
    # Naive - Brute force approach
    j = s
    for i in range(m-1):
        j += 1
        if j >= n:
            j = j%n
        #print j,
    return j
    """
    
    # Figure out the formula and try using that
    # n=5 m=2 s=1 ===> start+sweets = 1+2-1 = 2 (because 1 is given the sweet first it is also counted)
    # n=5 m=2 s=2 ===> start+sweets = 2+2-1 = 3 
    # If the result is lesser than n then return result else return n%result 
    
    result = s+m-1
    if result > n:
        if result%n == 0: # Dividing with multiples of n it is always 0 but the location is n, visualize and include such a case
            return n
        
        # When result is > than n then take the modulo
        return result%n
    
    # Plain case, when result is lesser than n
    return result
    
    

t = int(raw_input().strip())
for a0 in xrange(t):
    n, m, s = raw_input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)


