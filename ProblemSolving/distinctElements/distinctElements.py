### Codility Sorting - Distinct elements
def solution(A):
    
    # Dictionary Method - 100 percent on everything
    # create a new key for every distinct element in the list and return keys
    count = {}
    n = len(A)
    for item in A:
        if item not in count:
            count[item] = 1
    return len(count.keys())
    
    # Sort Method - Sort the list and have a counter to increment at various new values
    # List Method - Append new distinct elements to list and return the len of the list
    
