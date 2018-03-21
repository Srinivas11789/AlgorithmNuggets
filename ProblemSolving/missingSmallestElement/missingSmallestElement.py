### Codility Problem Missing Integer
# * Always consider a dictionary or list !!!!!!!!!!!!!!(Add SET to the list)!!!!!!!!!!!!!!!! method of solving
# * when using python try to use inbuild data structures like list, set and dictionary to perform operation making it simple
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    check = set(A)
    for i in range(1,n+2):
        #print(i)
        if i not in check:
            return i
    return -1
    """
    # Boolean array technique
    # After correcting negative - 40 percent correct

    n = len(A)
    check = [0 for i in range(n)]
    small = 600000
    for i in range(n):
        if A[i] < 0:
            for j in range(1,n):
                if j not in A:
                    return j
        if A[i]-1 not in A:
            if A[i]-1 != 0:
                if A[i]-1 < small:
                   small = A[i]-1
        if A[i]+1 not in A:
            if A[i]+1 != 0:
                if A[i]+1 < small:
                   small = A[i]+1
    return small
~   """           
