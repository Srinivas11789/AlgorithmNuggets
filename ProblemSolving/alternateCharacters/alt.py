#!/bin/python

import sys

def alternatingCharacters(s):
    
    s = list(s)
    prev = s[0]
    i = 1
    count = 0
    while i < len(s):
        
        if s[i] == prev:
            del s[i]
            count += 1
        else:
            prev = s[i]
            i += 1        
    
    return count


q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = alternatingCharacters(s)
    print(result)


