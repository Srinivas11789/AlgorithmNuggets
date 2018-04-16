#!/bin/python

import sys

def makingAnagrams(s1, s2):
        
        counts = {}
        for c in s1+s2:
            if c not in counts:
                counts[c] = abs(s1.count(c)-s2.count(c))
        #print counts
        return sum(counts.values())
        
        """
        counts = {}
        for c in s1:
            if c not in counts:
                counts[c] = 0
            counts[c] = s1.counts
        for c in s2:
            if c not in counts:
                counts[c] = 0
            if c not in s1:
                counts[c] += 1
            else:
                if counts[c] > 1:
                    counts[c] -= 1
            
            if c in s1 and counts[c] >= 2:
                counts[c] -= 2
            
        print counts
        return sum(counts.values())
        """
    
s1 = raw_input().strip()
s2 = raw_input().strip()
result = makingAnagrams(s1, s2)
print(result)

