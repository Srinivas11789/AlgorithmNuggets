# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    maxi = 0
    i = 0
    jump = 0
    visit = [0 for i in range(n)]
    while maxi < n:
        maxi = A[i] + i
        if maxi < n:
            visit[maxi] += 1
            if visit[maxi] > 5:
                return -1
        i = maxi
        jump += 1
    return jump
    """
    pawn = A[0]
    i = 0
    dist = pawn + i
    """
    """
    jump = 0
    sumi = A[0]
    while sumi < n:
        i = sumi
        sumi = i + A[i]
        i += 1
        jump += 1
    return jump
    """
    """
    while dist < n:
        i = dist
        jump += 1
        dist = A[i] + i
    return jump+1
    """


