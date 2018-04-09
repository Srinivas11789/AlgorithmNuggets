#!/bin/python

import sys

def isValid(s):
    
    occur = {}
    
    # Reduce the combination of iterations
    for c in set(s):
        count = s.count(c)
        if count not in occur:
            occur[count] = []
        occur[count].append(c)
    
    result = occur.keys()
    if len(result) > 2:
        return "NO"
    else: 
        if len(result) == 2: # Some testcase failed due to runtime error - correct the assumptions you are making like lenght being 2 and then use absolute difference 
        #if abs(result[0] - result[1]) != 1: # what if the value is {1:[n] , 111:[a,b,c,d]}
            if len(occur[result[0]]) > len(occur[result[1]]):
                select = result[1]
            else:
                select = result[0]
            if select == 1 and len(occur[select]) == 1:
                return "YES"
            if len(occur[select]) > 1 or abs(result[0]-result[1]) != 1:
                return "NO"
                
                
                
        
    return "YES"
        
    
    """
    # Timeout and failures
    occur = {}
    for c in s:
        if c not in occur:
            occur[c] = 0
        occur[c] += 1
    result = list(set(occur.values()))
    if len(result) > 2:
        return "NO"
    if abs(result[0]-result[1]) != 1:
        return "NO"
    if (result[0] > result[1] and occur.values().count(result[0]) > 1) or (result[1] > result[0] and occur.values().count(result[1]) > 1):
        return "NO"
    return "YES"
    """

s = raw_input().strip()
result = isValid(s)
print(result)

