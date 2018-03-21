### Codility Problem Missing Integer
# * Always consider a dictionary or list !!!!!!!!!!!!!!(Add SET to the list)!!!!!!!!!!!!!!!! method of solving
# * when using python try to use inbuild data structures like list, set and dictionary to perform operation making it simple
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


# Strategy:
# * Use native datastrcutures like set, list and dictionary to solve, think in those manner
# * There are 2 methods for this problem:
#   * one is calculating the total sum and minus the sum of consecutive integer formula which is n(n+1)/2
#   * two is the method of using set when repetitive elements are found in the list.
#   * n+1 at both the solutions denotes the list of integers is always one greater as one remains missing a list of length 5 (1,2,3,4,6) has 5 missing and we need to check n+1



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
