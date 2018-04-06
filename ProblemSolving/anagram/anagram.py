#!/bin/python

import sys

def anagaram(s):
    
    # convert string to list and length
    s = list(s)
    n = len(s)
    
    # odd condition
    if n%2 != 0:
        return -1
    
    # even condition - split
    mid = n//2
    left = s[:mid]
    right = s[mid:]
    
    # O(N)
    # remove all similar elements from the array
    # remaining is the one to be changed!
    for i in range(len(left)):
        if left[i] in right:
            right.pop(right.index(left[i]))
    
    return len(right)
    
    
    """
    # only a few passes O(N2)
    count = 0
    for i in range(len(left)):
        for j in range(len(right)):
            if left[i] == right[j]:
                count += 1
                break
    
    return len(left) - count
    """         

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = anagaram(s)
    print(result)


