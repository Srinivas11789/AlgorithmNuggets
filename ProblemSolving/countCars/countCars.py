# Codility Problem - countCars

def solution(A):
    # Logic: Find the element 0 and pair the zero with all one indexes
    # * Only the number of pairs is required   
    # Dictionary method - wont be feasible as the indexes get messed up
    
    n = len(A)
    noz = 0
    prev_count = 0
    count = 0
    for i in range(n):
        if prev_count > 1000000000:
            return -1
        if A[i] == 0:
            prev_count = prev_count + noz*count
            if prev_count > 1000000000:
                return -1
            count = 0
            noz += 1
        else:
            count += 1
        if i == n-1:
            prev_count = prev_count + noz*count
            if prev_count > 1000000000:
                return -1
	    ## Had 90 percent success rate, as was returning prev_count *noz which became more than 1000000000, look at what you are returning before proceeding
            return prev_count
    
    """ Raw logic frame
    n = len(A)
    zero_check = 0
    prev_count = 0
    count = 0
    noz = 0
    for i in range(n):
        if A[i] == 0 or i == n-1:
            print(count, noz, prev_count)
            prev_count = prev_count + noz*count
            # Track number of zeros
            noz += 1
            # Reset count to zero for the new zero 
            count = 0
            # Record the zero hit 
            zero_check = i
        else:
            if i > zero_check:
                count += 1
    return prev_count
    """    

