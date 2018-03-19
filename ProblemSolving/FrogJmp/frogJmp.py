# Codility Problem - FrogJumps
# (X,Y,D) - Frog can jump D at a time, starting from X and goal is to reach Y or greater than Y. 
# Solution Logic:
#    Y-X as X is the starting point
#    Y-X // D to get the quotient or number of times to divide it by D
#    Y-X % D to get the reminder if any
#    Until reminder is 0 or lesser add jumps and subtract D every time

def solution(X, Y, D):

    ### Solution passed all the cases with complexity O(N)
    value = Y-X
    jumps = value//D
    reminder = value%D
    while reminder > 0:
        jumps += 1
        reminder = reminder - value
    return jumps
    
    #### Only 11% Pass    
    """
    jumps = Y//D
    reminder = (Y-X)%D 
    value = reminder//D
    #print(jumps,reminder,value)
    if reminder > 0 and reminder < D:
        value = 1
    return jumps + value
    """
    
