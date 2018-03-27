# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    # List Method
    n = len(A)
    check = [0]*(n+1) #list(str(0)*(n+1))
    for i in range(1,n+1):
        if i in A:
            check[i] += 1
            if check[i] > 2 or check[i] == 0:
                return 0
        else:
            return 0
    return 1

    """
    # Sum Method
    n = len(A)
    total = n*(n+1)//2
    sum = 0
    for i in range(n):
        sum += A[i]
    if total - sum == 0:
       return 1
    else:
       return 0
    
    # 80 percent pass on everything except 2 antiSum testcases
    A = sorted(A)
    n = len(A)
    if A[0] == 1 and A[n-1] == n:
        return 1
    else:
        return 0
    """
    ### Dictionary method correctness 100 % and performance 45
    """
    n = len(A)
    check = {}
    for i in range(1,n+1):
        if i not in check:
                check[i] = 0
        if i in A:
            check[i] += 1
            if check[i] > 2:
                return 0
    if 0 in check.values():
        return 0
    return 1
    """

    ### Simple logic correct 100 but performance fails
    """
    n = len(A)
    for i in range(1,n+1):
        if i in A:
            pass
        else:
            return 0
    return 1
    """
    
