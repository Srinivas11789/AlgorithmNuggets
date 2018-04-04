#!/bin/python

import sys

def hackerrankInString(s):
    n = len(s)
    h = list('hackerrank')
    k =0
    select = h[k]
    for i in range(n): 
        if s[i] == select and k < len(h)-1:
            k += 1
            select = h[k]
    if h[k] == "k" and k == len(h)-1:
        return "YES"
    else:
        return "NO"
        

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        s = raw_input().strip()
        result = hackerrankInString(s)
        print result


