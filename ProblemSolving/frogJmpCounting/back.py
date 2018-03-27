# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # Locate the X in A and count from there
    n = len(A)
    ans = 0
    lend = X+1
    check = [0 for i in range(lend)]
    while X in A:
        ind = A.index(X)
        #print(ind)
        #print(A)
        #print(check)
        for i in range(ind,-1,-1):
            if check[A[i]%(lend)] == 0:
                check[A[i]%(lend)] += 1
            elif check[A[i]%(lend)] == 1:
                check = [0 for i in range(lend)]
                break
            if 0 not in check[1:]:
                    ans = ind
                    return ans
        A[ind] = 0
    return -1
    """
    # Count 123...X in sequence - 50% pass rate
    # Bug1 = when the numbers are reset, and counted again proper counting is not done
    # (20, [1,2,3,4,5,6,1,2,4,6,5,4,3,2,1,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    n = len(A)
    ans = 0
    lend = X+1
    check = [0 for i in range(lend)]
    for i in range(n):
        #print(i)
        if check[A[i]%(lend)] == 0:
            check[A[i]%(lend)] += 1
        elif check[A[i]%(lend)] == 1:
            check = [0 for i in range(lend)]
            check[A[i]%(lend)] += 1
        else:
            pass
        if A[i] == X:
            ans = i
            #print(ans)
            #print(check)
            if 0 not in check[1:]:
                return ans
            else:
                check = [0 for i in range(lend)]
    return -1
    """


