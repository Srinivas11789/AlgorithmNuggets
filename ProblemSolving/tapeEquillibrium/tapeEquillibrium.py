# MinimumDifferenceCuttingTape -  Codility Problem
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Solution O(N) passes 
def solution(A):
    # Memoization
    mini = 600000
    n = len(A)
    for i in range(1,n):
        # P value from 1 to n
        if i == 1:
            left = A[i-1]
            right = 0
            breaki = i
            while breaki <= n-1:
                right += A[breaki]
                breaki += 1
        else:
            left = left + A[i-1]
            right = right - A[i-1]
        diff = abs(right - left)
        if diff < mini:
            mini = diff
        #print(right,left)
    return mini

"""
def solution(A):
    # write your code in Python 3.6
    # Iterative Solution O(N*N)
    mini = 600000
    n = len(A)
    for i in range(1,n):
        # P value from 1 to n
        left = 0
        right = 0
        breaki = i
        while breaki <= n-1:
            #print("Hi",A[breaki])
            right += A[breaki]
            breaki += 1
        breaki = i
        while breaki > 0:
            breaki -= 1
            left += A[breaki]
        #print(left)
        diff = abs(right - left)
        if diff < mini:
            mini = diff
        #print(i)
        #print(right,left)
    return mini
"""    
