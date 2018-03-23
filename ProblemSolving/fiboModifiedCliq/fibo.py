
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





    # you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

fibo = [0,1]
def solution(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    elif len(fibo)>N:
        return fibo[N]
    else:
         value = solution(N-1) + solution(N-2)
         fibo.append(value)
         return value%1000000

