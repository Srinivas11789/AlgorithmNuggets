#!/bin/python

import sys

def circularArrayRotation(a, m, k):
    # Complete this function
    
    # 
    n = len(a)
    
    # K value filtering - k can only be within length of the array
    k = k%n
    if k == 0:
        k = n
    else:
        k = k%n
    
    # Rotate the array
    a = a[n-k:]+a[:n-k]
    
    # Return
    result = []
    for i in m:
        result.append(a[i])
    return result
    

if __name__ == "__main__":
    n, k, q = raw_input().strip().split(' ')
    n, k, q = [int(n), int(k), int(q)]
    a = map(int, raw_input().strip().split(' '))
    m = []
    m_i = 0
    for m_i in xrange(q):
        m_t = int(raw_input().strip())
        m.append(m_t)
    result = circularArrayRotation(a, m, k)
    print "\n".join(map(str, result))



