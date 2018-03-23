# Codility - maxSliceSum

def solution(A):
    # Reference from codesays blog
    # Setting all param to 0 to start computing in the for loop
    # Slice problem - Keep track of every element addition
    end = A[0]
    # Compare from previous maximum and store the flowing maximum
    slice = A[0]
    for element in A[1:]:
        # calculation at every element addition for consideration
        end = max(element, end+element)
        #print(end)
        # calculation of forever maximum
        slice = max(slice, end)
        #print(slice)
    return slice
    
    """
    n = len(A)
    ans = -100000000
    sumi = 0
    for i in range(1,n):
        sumi = sumi + A[i]
        if sumi > ans:
            ans = sumi
    return ans
    """
    ### Another logic of 2 for loops did not work too
    """
    n = len(A)
    ans = -100000000
    sumi = 0
    for i in range(n):
        sumi = A[i]
        for j in range(i+1,n):
            sumi += A[j]
            if sumi > ans:
                ans = sumi
    return ans
    """    
