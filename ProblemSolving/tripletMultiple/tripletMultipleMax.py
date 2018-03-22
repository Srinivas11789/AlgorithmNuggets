# Codility Triplet Maximum Multiple

def solution(A):
    # write your code in Python 3.6
    A = sorted(A)
    n = len(A)
    if n < 3:
        return 0
    #### Multiplying 2 negative becomes a positive number
    # hence taking first 2 possible -ve numbers 
    prod = max(A[0]*A[1]*A[-1],A[-1]*A[-2]*A[-3])
    return prod
        
