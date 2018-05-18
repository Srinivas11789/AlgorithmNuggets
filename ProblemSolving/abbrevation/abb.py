# Pending - 4 tcs to pass yet - hr medium
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    
    # First check if all the characters in A exist in B
    a = list(a)
    for char in b:
        # Check if all the characters in b exist in a
        if char.upper() in a:
            del a[a.index(char.upper())]
        elif char.lower() in a:
            del a[a.index(char.lower())]
        else:
            #print char
            return "NO"
        
    # Check for the condition with the remaining characters
    #print a
    for char in a:
        if char.isupper():
            return "NO"
        
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        a = raw_input()

        b = raw_input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()

