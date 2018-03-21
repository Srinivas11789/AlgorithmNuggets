# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
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
    n = len(A)
    for i in range(1,n+1):
        if i in A:
            pass
        else:
            return 0
    return 1
    """
