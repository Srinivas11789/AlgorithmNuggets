# Codility Problem - MaxProfit - Slicing Technique
#

def solution(A): 
    
    # Slice problem of considering 2 elements at a time in an array, keep track of current_maximum and the flowing maximum
    # Iterate the array backwards as we are interested in the profit
    # Setting the current maximum to the last integer in the array for easy of tracking and iteration
    # backwards loop from integer before the last integer which is n-2
    # Keep track of the profit and the flowing maximum
    # Update the current maximum everytime a higher number is being hit
    n = len(A)
    if n < 2:
        return 0
    ## Keep the n < 2 logic above the current maximum setting, as the current maximum will throw error when array is empty, easy testcase - check for empty
    ## 
    curr_max = A[n-1]
    maxi = 0
    profit = 0
    #if n < 2:
    #    return 0
    for i in range(n-2,-1,-1):
        profit = curr_max - A[i]
        if profit > maxi:
            maxi = profit
        if A[i] > curr_max:
            curr_max = A[i]
    return maxi
            
    

	
    """
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
    """
        
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
        
        
