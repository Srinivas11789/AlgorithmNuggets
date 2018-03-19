#### Codility Problems
## They test the ability to create testcase, write code and performance ---- think think think, after submission you cannot change!!!!!!!!!
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    n = len(A)
    if n == 0:
        return A
    rotation = K%n
    #print(rotation)
    rotated = [0 for i in range(n)]
    for i in range(n):
        if i+rotation >= n:
            rotated[i+rotation-n] = A[i]
        else:
            rotated[i+rotation] = A[i]

    # Logic doesnt work when K > n that is a big k like 10, 11,12 for example ([1,2,3],10) - good catch on the case and rectification
    # Logic also doesnt work when K%n is very much greater than n -> rotation was necessary when rotation+i was greater than n -- good catch on this one too
    # Failed only one testcase, which was empty array testcase -----> please anticipate all the possible scenarios like empty array cases
    # Logic doesnt work for K>n
    #n = len(A)
    #rotation = K%n
    #rotated = [0 for i in range(n)]
    #for i in range(n):
    #    rotated[i+rotation] = A[i]
    return rotated
        
    
    # Initial Logic	
    # Logic doesnt work for K>n
    #n = len(A)
    #rotation = K%n
    #rotated = [0 for i in range(n)]
    #for i in range(n):
    #    rotated[i+rotation] = A[i]
    return rotated
        
    
    
