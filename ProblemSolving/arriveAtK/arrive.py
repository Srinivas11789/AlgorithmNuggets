# Codility problem - arrive at a k value

def solution(K, A):
    # write your code in Python 3.6
    """
    n = len(A)
    count = 0
    match = []
    for i in range(n):
        if K - A[i] in A[i:]:
            match.append((i,A.index(K-A[i])))
            count += 1
            if i != A.index(K-A[i]):
                count += 1
    #print(match)
    return count"""

    n = len(A)
    count = 0
    for i in range(n):
        for j in range(i,n):
            if A[i] + A[j] == K:
                count += 1
                if i != j:
                    count += 1
    return count

    """
    n = len(A)
    count = 0
    for i in range(n):
        #print(i)
        for j in range(n):
            if A[i] + A[j] == K:
                #print(i,j)
                count += 1
    return count
    """





