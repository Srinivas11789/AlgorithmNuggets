#!/bin/python

# Greedy problem
# Solve in the manner of making the number large supporting the 3rd rule, 5*n and then chaning 3 at every character to gain the 3 to 5 divisibiility and 5 to 3 divisibility

import sys

def sherlock(n):
    # Decent number should be
    # divided into multiple of 5 and multiple of 2
    # Largest would always be "All 5s" and lowest would be "All 3s"
    dn = list("5"*n)
    if dn.count("5")%3 == 0 and dn.count("5") != 1:
        return int("".join(dn))
    for i in range(len(dn),-1,-1):
        if dn.count("5")%3 == 0 and dn.count("3")%5 == 0:
            return int("".join(dn))
            break
        if dn.count("5")%3 == 0 and dn.count("3") == 0:
            return int("".join(dn))
            break
        if dn.count("3")%5 == 0 and dn.count("5") == 0:
            return int("".join(dn))
            break
        dn[i-1] = "3"
    return -1

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print sherlock(n)

