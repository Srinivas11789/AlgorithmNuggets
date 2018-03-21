### Codility Problem Missing Integer
# * Always consider a dictionary or list method of solving

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    
    
    
    # Boolean array technique
    # After correcting negative - 40 percent correct
    
    n = len(A)
    check = [0 for i in range(n)]
    small = 600000
    for i in range(n):
        if A[i] < 0:
            for j in range(1,n):
                if j not in A:
                    return j
        if A[i]-1 not in A:
            if A[i]-1 != 0:
                if A[i]-1 < small:
                   small = A[i]-1 
        if A[i]+1 not in A:
            if A[i]+1 != 0:
                if A[i]+1 < small:
                   small = A[i]+1 
    return small
