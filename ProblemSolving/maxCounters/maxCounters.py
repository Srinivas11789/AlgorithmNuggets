# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Full Stack Dev Lesson: AVOID USING A RESERVED KEYWORD WHILE WRITING PROGRAM - BE CAUTIOUS FOR DIFFERENT PROG LANG

### Possible Solution from reading -- Lazy write to the array

def solution(N, A):
   
    c = [0]*(N+1)
    for item in A:
        if item > 0 and item <= N:
            c[item] += 1
        else:
            if item == N+1:
                c = [max(c)]*(N+1)
    return c[1:N+1]
    
    """
    #Tracking max and applying changes - doesnt work 
    c = [0]*(N)
    # To keep track of max hit at N+1
    maxi = 0
    # Total maximum that occurred in the list
    total_maxi = 0
    for i in range(len(A)):
        if A[i] == N+1:
            # If hit maximum
            if (i < len(A)-1 and A[i+1] != N+1) or i ==len(A)-1:
                total_maxi += maxi
                maxi = 0
                c[:] = [total_maxi]*N
        else:
            c[A[i]-1] += 1
            if maxi < c[A[i]-1]:
                maxi = c[A[i]-1]
    for i in range(len(c)):
        c[i] += total_maxi
    return c
"""        

""" Still not working proper - 
# Solution using N rather than maintaining a N+1 array after hitting maximum
def solution(N, A):
    c = [0]*(N)
    # To keep track of the previous maximum to change entries based on N+1 hit
    maxi = 0
    # To keep track of current maximum for future N+1 hit
    current_maxi = 0
    for item in A:
        if item >= 1 and item <= N:
            # If the item is less than past maximum update it
            if c[item-1] < maxi:
                    c[item-1] = maxi
            # Increment number based on current hit
            c[item-1] += 1
            # keeping track of the current maximum for future N+1 hit
            if c[item-1] > maxi:
                current_maxi = c[item-1]
        else:
            # N+1 hit, set maximum to current maximum
            maxi = current_maxi
    
    # items that were not present in A
    for i in range(0,N) :
        if c[i] < maxi:
            c[i] = maxi
    return c
"""
"""
### Solution correct 100 percent but performance upto 75 only - Using max function rather than tracking max variable
def solution(N, A):
    c = [0]*(N+1)
    for item in A:
        if item > 0 and item <= N:
            c[item] += 1
        else:
            if item == N+1:
                c = [max(c)]*(N+1)
    return c[1:N+1]
"""


"""
### solution workd 75 percent correctness and performance
def solution(N, A):
    n = len(A)
    c = [0]*(N+1)
    maxi = 0
    for item in A:
        #print(c[item])
        if item > 0 and item <= N:
            c[item] += 1
            if c[item] > maxi:
                maxi = c[item]
        else:
            if item == N+1:
                # Using max which is a reserved keyword in python will throw unnecessary errors
                c = [maxi]*(n+1)
    #print(c[1:N+1])
    return c[1:N+1]
    """
