# Codility Problem
# Dictionary Logic Passes the test with complexity O(N)or(NlogN) while the list logic takes O(N2) or greater than 6 seconds

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    # Dictionary Logic
    
    count = {}
    for i in range(len(A)):
        if A[i] not in count.keys():
            count[A[i]] = 0
        count[A[i]] += 1
    for key, value in count.items():
        if value%2 != 0:
            return key
    
    """
    # List Logic
    count = []
    for i in range(len(A)):
        if len(count) == 0:
            count.append(A[i])
        elif A[i] in count:
            del count[count.index(A[i])]
        else:
            count.append(A[i])
        #print(count)
    return count[0]
    """
        
