#!/bin/python

import sys

def stringConstruction(s):
    # Set eliminates all the repeated characters hence the no cost need not be calculated
    # only the cost of 1 dollar can be added up
    s = set(s)
    return len(s)
    
if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        s = raw_input().strip()
        result = stringConstruction(s)
        print result


