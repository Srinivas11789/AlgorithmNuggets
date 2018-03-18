# Bitwise AND operation - Timeout error

#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    maxi = 0
    initk = k
    for i in range(1,n):
        k = initk+1
        while k <= n:
                value = i&k
                if value > maxi and value < initk:
                    maxi = value
                    break
                k += 1
    print maxi
