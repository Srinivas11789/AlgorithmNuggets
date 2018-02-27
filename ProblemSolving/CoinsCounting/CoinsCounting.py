#!/bin/python

import sys

def getWays(n, c):
    # Complete this function
    rows = len(c)
    cols = n+1
    result = [[1 if i == 0 else 0 for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if j >= c[i]:
                result[i][j] = result[i-1][j] + result[i][j-c[i]]
            else:
                result[i][j] = result[i-1][j]
    print result[len(c)-1][cols-1]

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
c = map(long, raw_input().strip().split(' '))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)

