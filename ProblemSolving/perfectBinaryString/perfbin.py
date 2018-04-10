#!/bin/python

import sys

def beautifulBinaryString(b):
    
    b = list(b)
    n = len(b)
    count = 0
    for i in range(len(b)):
        if i+3 <= n:
            if "".join(b[i:i+3]) == "010":
                b[i+2] = "1"
                count += 1
    return count
    
        
if __name__ == "__main__":
    n = int(raw_input().strip())
    b = raw_input().strip()
    result = beautifulBinaryString(b)
    print result

