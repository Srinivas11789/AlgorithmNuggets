# Codility Problem - MaxProfit - Slicing Technique
#

def solution(A):
    
    # Slicing the array into 2 pairs each
    # Slice solution in reference to codesays
    
    # length of the array
    n = len(A)
    
    # Days being 0 or 1, there is no solution
    if n < 2:
        return 0
        
    # Maximum at the current location, iterating array backwards for max
    # Setting the curr max to last index
    max_here = A[n-1]
    
    # Flowing max to zero
    maxi = 0
    
    # Iterate array backwards leaving the n-1 index, hence n-2 is starting point
    for i in range(n-2, -1,-1):
        # flowing max as we progress through array, compare with maxi already and subracting for profit
        maxi = max(maxi,max_here-A[i])
        # current max update as we progress through the array
        max_here = max(A[i],max_here)
        #print(maxi,max_here)
    return maxi
        
    # Worst case logic of using 2 for loops - 60/40 percent
    """
    n = len(A)
    max = -6000000
    for i in range(n-1):
        for j in range(i+1,n):
            profit = A[j]-A[i]
            if profit > max:
                #print(i,j)
                max = profit
    return max
    """
    
    # Calculating the lowest and highest and difference gives highest profit
    # Possible problem overseen - lowest occuring at the last 
    # Wrong logic think properly
    """
    n = len(A)
    lowest = A[0]
    highest = A[1]
    low_ind = 0
    high_ind = 1
    for i in range(1,n):
        if low_ind > high_ind:
            lowest = 0
            low_ind = 0
            if A[i] < lowest:
                lowest = A[i]
                low_ind = i
        if high_ind < low_ind:
            highest = 0
            high_ind = 0
            if A[i] > highest:
                highest = A[i]
                high_ind = i
    print(highest, lowest)
    return highest-lowest
    """
        
        
