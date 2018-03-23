# Codility - maxSliceSum

def solution(A):
    n = len(A)
    ans = -100000000
    sumi = 0
    for i in range(n):
        sumi = sumi + A[i]
        if sumi > ans:
            ans = sumi
    return ans
    
    ### Another logic of 2 for loops did not work too
