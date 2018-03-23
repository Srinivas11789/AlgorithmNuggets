# Codility Factors

# Write down the logic of what is being asked, like 1*24, 2*12, 3*4 so you arrive at a particular logic. You already visited all possible factors
# Logic for factor is except square numbers all other factors are already visited hence add 2 for all other combinations eg: 2*6 4*3 all have 2 factors baked already.
# In Reference from Codesays and Martin
def solution(N):
    # initilize count
    count = 0
    # current integer being considered
    current = 1
    # while the square of the current number remains within N, factors are less than N
    while current*current <= N:
        # If divisible
        if N%current == 0:
            # If it is a square number, Add 1 as there is only one possibility 12*12
            if current*current == N:
                #print(current)
                count += 1
            else:
            # If it is not a square number, then Add 2 as 2*6 will add 2 integers 2 and 6
                count += 2
        # Dont forget to increment the current number
        current += 1
    return count
    
    """
    ### O(N) Complexity - Correctness 100percent and Performance 57
    count = 0
    for i in range(1,N+1):
        if N%i == 0:
            count += 1
    return count
    """
