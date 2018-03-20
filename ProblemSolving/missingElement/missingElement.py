#############
# Codility Problems
# PermMissingElement
# - Find the missing element in the array of elements forming a consecutive series

# Thoughts Logic 1
# Put all elements into a dictionary, sort the keys and then try to find missing

# Thoughts Logic 2
# Iterate all the elements in the array to find min and the max 
# 

# Thoughts Logic 3
# Find the length and iterate through the length

# Tip - distinct elements are present
# The sepaation between the number could be 1 or more?

# Thouhgts - sort and go through the array by the diff

# Testcase failes:
# * think about array empty case
# * think about array with one element
# * think about array with two element

def solution(A):
    n = len(A)
    if n == 0 or n == 1:
        return 0
    for i in range(1,n+1):
        #if one element is missing the diff should be 1 for sure, also in order 1...N+1 hence the elements are always in order where one of them is missing
        #print(i)
        if i in A:
            pass
        else:
            #print(i)
            return i
    """
    n = len(A)
    seen = []
    min = 600000
    max = -600000
    diff = 600000
    for i in range(n-1):
        seen.append(A[i])
        if A[i] < min:
            min = A[i]
        if A[i] > max:
            max = A[i]
        differ = abs(A[i+1] - A[i])
        if differ < diff:
            diff = differ
        if A[i]+diff not in A:
            return A[i]+diff
        if A[i]-diff not in A:
            return A[i]+diff
    """    
        
