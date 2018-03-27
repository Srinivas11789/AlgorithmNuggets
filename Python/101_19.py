# Bitwise AND operation - Timeout error
# SOLUTION from Jakus hackerrank passes all the testcase, based on the strucuture of AND logic
#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    # Logic based on Jakus explanation in hackerank 
    # if k is odd, k-1 is even, k-1 & k == k-1 and k-1 | k == k
    # if k is even, k-1 is odd, k-1 can be reached if k-1 | k <= n
    print k-1 if (k-1 | k) <= n else k-2
    """
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
    """
