#!/bin/python

import sys

def super_reduced_string(s):
    
    # Iterative delete method
    n = len(s)
    result = list(s)
    i = 0
    while i < len(result)-1:
        #print result,result[i], result[i+1]
        if result[i] == result[i+1]:
            del result[i:i+2]
            i = 0
        else:
            i += 1
    if result:
        return "".join(result)
    else:
        return "Empty String"

s = raw_input().strip()
result = super_reduced_string(s)
print(result)

