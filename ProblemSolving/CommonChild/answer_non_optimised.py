#!/bin/python

import sys

def commonChild(s1, s2):
    answer = [[None]*(len(s2)+1) for y in range(len(s1)+1)] 
    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i == 0 or j == 0 :
                answer[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                answer[i][j] = answer[i-1][j-1] + 1
            else:
                answer[i][j] = max(answer[i][j-1],answer[i-1][j])
    return answer[len(s1)][len(s2)]
        
s1 = raw_input().strip()
s2 = raw_input().strip()
result = commonChild(s1, s2)
print(result)
