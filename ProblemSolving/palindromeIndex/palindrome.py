#!/bin/python

import sys

def palindromeIndex(s):
    occur = {}
    for c in s:
        if c not in occur:
            occur[c] = 0
        occur[c] += 1
    
    for key, value in occur.items():
        if value == 1:
            return s.index(key)
    return -1
    

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = palindromeIndex(s)
    print(result)


