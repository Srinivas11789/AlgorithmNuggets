#!/bin/python

import sys

def commonChild(s1, s2):
    p = len(s1)
    q = len(s2)
    answer = [[0 for r in range(q+1)] for y in range(2)]
    x = bool
    for i in range(p):
        x = i&1
        for j in range(1,q+1):
            if s1[i] == s2[j-1]:
                answer[x][j] = answer[1-x][j-1] + 1
            else:
                if answer[x][j-1] > answer[1-x][j]:
                    answer[x][j] = answer[x][j-1]
                else:
                    answer[x][j] = answer[1-x][j]
    return answer[x][q]
        
s1 = raw_input().strip()
s2 = raw_input().strip()
result = commonChild(s1, s2)
print(result)

