#!/bin/python

import sys

def beautifulPairs(A, B):
    
    # Calculate number of beautiful pairs
    # Sort both the arrays
    #A = sorted(A)
    #B = sorted(B)
    #print A
    #print B
    
    # Simple logic that passes, logic by ccordero from hr discuss but ON2
    res = 0
    #Iterate the full array A
    for i in range(len(A)):
        # Iterate B such that its length is updated every time
        for j in range(len(B)):
            # If beautiful pair remove from B
            if A[i] == B[j]:
                #print j
                B.pop(j)
                # Update the result everytime and break to reload B after pop
                res += 1
                break
        #print A
        #print B
    #print A
    #print B
    
    # If result is equal to N all the elements have been exhausted
    if res == len(A):
        return res - 1
    else:
        return res + 1
                
    """
    pairs = 0
    change = {}
    count = 0
    for i in range(len(A)):
        if A[i] == B[i]:
            pairs += 1
            if A[i] not in change:
                change[A[i]] = 0
        else:
            #if A[i] not in change:
            #    change[A[i]] = 0
            #change[A[i]] += 1
            if B[i] not in change:
                change[B[i]] = 0
            change[B[i]] += 1
    maxi = 0
    for key, value in change.items():
        if value > maxi:
            maxi = value
    return pairs + maxi
    #return pairs + count
    """
    
if __name__ == "__main__":
    n = int(raw_input().strip())
    A = map(int, raw_input().strip().split(' '))
    B = map(int, raw_input().strip().split(' '))
    result = beautifulPairs(A, B)
    print result

