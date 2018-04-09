#!/bin/python

import sys

# Even and Odd logic - 
# even length string - all count should be even
# odd length string - only one count odd else everything else is even

def gameOfThrones(s):
    char = {}
    for c in s:
        if c not in char:
            char[c] = 0
        char[c] += 1
        if char[c] == 2:
            char[c] = 0

    #print char
    if (len(s)%2 == 0 and char.values().count(0) == len(set(s))) or (len(s)%2 !=0 and char.values().count(0) == len(set(s))-1 and char.values().count(1) == 1):
        return "YES"
    else:
        return "NO"
    

    """
import itertools
# timeout error as it traverses all the elements in the array
def isPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
        

def gameOfThrones(s):
    for comb in itertools.permutations(s):
        if isPalindrome("".join(comb)):
            return "YES"
    return "NO"
    
    """
    """
    # Dictionary Logic - 11/20 pass
    char = {}
    for c in s:
        if c not in char:
            char[c] = 0
        #print char
        char[c] += 1

    for c in s:
        if char[c] > 1 and char[c]%2 == 0:
            return"YES"
    return "NO"            
    """

s = raw_input().strip()
result = gameOfThrones(s)
print(result)

