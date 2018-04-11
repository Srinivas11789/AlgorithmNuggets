#!/bin/python

import sys

def funnyString(s):
    
    s = list(s)
    s1 = s[::-1]
    n = len(s)
    
    for i in range(n-1):
        
        if abs(ord(s[i+1])-ord(s[i])) == abs(ord(s1[i+1])-ord(s1[i])):
            pass
        else:
            return "Not Funny"
        
    return "Funny"

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = funnyString(s)
    print(result)


