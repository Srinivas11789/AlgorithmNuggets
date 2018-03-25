# Codility Problem - stringSymmetry - 100 percent
# Reference to code says
  
# Go to the details, 
## 1. The string has to be of odd length for it to work

## Got locked up in comparing string and the reverse all the time
## Or comparing the string ends up equally ending up succesfully as the copies of string always match

def solution(S):
    n = len(S)
    
    # Length of string being 1
    if n == 1:
        return 0
        
    # Length of string being 0
    if n == 0:
        return 0
        
    # Length of string being odd
    if n%2 == 0:
        return -1
    
    # Create begin and end string
    begin, end = 0, n-1
    
    # Get the mid element which is the possible candidate
    mid = n//2
    
    # Loop until mid, every time incrementing and decrementing first and last respectively.
    
    while begin < mid:
        if S[begin] != S[end]:
            return -1
        begin += 1
        end -= 1
    return mid
    
    """ 
    # Increases the complexity (length(S)**2)
    for i in range(n):
        #print(S[:i],S[i+1:])
        if S[:i] == S[i+1:][::-1]:
            return i
    return -1
    """

