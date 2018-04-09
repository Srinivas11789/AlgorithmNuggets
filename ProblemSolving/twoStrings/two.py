#!/bin/python

import sys

def twoStrings(s1, s2):
    
    # 4 and 5 timeout, all other pass... Using set() eradicates the duplicates hence passes everything
    for c in set(s1):
        if c in s2:
            return "YES"
    return "NO"


q = int(raw_input().strip())
for a0 in xrange(q):
    s1 = raw_input().strip()
    s2 = raw_input().strip()
    result = twoStrings(s1, s2)
    print(result)


