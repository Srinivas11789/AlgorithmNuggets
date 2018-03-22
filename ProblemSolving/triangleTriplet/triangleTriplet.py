### Codility - Triplet Triangular problem
#
#

def solution(A):
    # Sorted logic makes it easier
    A = sorted(A)
    # Length computation
    n = len(A)
    # Less than three logic, consider these type everytime
    if n < 3:
        return 0
    # Iterate till n-2 with taking care of i+1 and i+2
    for i in range(0,n-2):
        if A[i]+A[i+1] > A[i+2]:
            return 1
    return 0

""" 
# Same complexity as the last logic
# Modified O(N3)
def solution(A):
    n = len(A)
    for i in range(n):
            for j in range(i,n):
                if i<j:
                    for k in range(j,n):
                        if i<j<k and A[i] + A[j] > A[k] and A[j]+A[k] > A[i] and A[i]+A[k]>A[j]:
                            return 1
    return 0
"""
"""
## O(N3) - 100 percent correct but fails timeout,  75 percent perf
def solution(A):
    n = len(A)
    for i in range(n):
        for j in range(i,n):
            for k in range(j,n):
                if i<j<k and A[i] + A[j] > A[k] and A[j]+A[k] > A[i] and A[i]+A[k]>A[j]:
                    return 1
    return 0
"""
    
