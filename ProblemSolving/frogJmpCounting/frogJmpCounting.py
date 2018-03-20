# FrogJumpRiver1 problem - took a very long time to solve
### The problem was a little confusing in description took a little time to make it out
### Lesson learnt: 
### * Look at the parameter what was asked? While implementing I always looked for continuous series from 1...N, but what was asked was only the spot where \
### or the index where the match occurs, so negating the value of X would have thrown the solution at a proper index
### * Dont over complicate stuff, the answer was very simple, think in terms of hacking and finding the right solution
### * THought about having a boolean array but what was missing was the idea in the question itself, X a known value

def solution(X, A):
    # Easy solution, every time maintain a boolean array to keep track and subtract X to get 0
    n = len(A)
    map = [0 for i in range(X+1)]
    lend = X
    for i in range(n):
        if map[A[i]] == 0:
            map[A[i]] = 1
            lend -= 1
        if lend == 0: 
            return i
    return -1

    """
    # Optimized but still 50 percent accuracy
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


