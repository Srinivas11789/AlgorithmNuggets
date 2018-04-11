#!/bin/python

import sys

def isPalin(s):
    if s == s[::-1]:
        return True
    else:
        return False

def theLoveLetterMystery(s):
    
    n = len(s)
    s = list(s)
    count = 0
    
    for i in range(n):
        
        while s[i] != s[-i-1]:
            
            if ord(s[i]) > ord(s[-i-1]):
                select = ord(s[i])
                ind = i
            else:
                select = ord(s[-i-1])
                ind = -i-1+n
            
            if select > 97:
                s[ind] = chr(ord(s[ind])-1)
                count += 1
                
    if isPalin(s):
        return count
    else:
        return -1

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = theLoveLetterMystery(s)
    print(result)


