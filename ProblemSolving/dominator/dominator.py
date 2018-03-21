# Codility Dominator -
# Lessons learnt: 
## Easy testcase failed - test for empty array!!!!!!!!
## 100 percent pass
# A Linear Time Majority Vote Algorithm - Good exaplanation at http://www.cs.utexas.edu/~moore/best-ideas/mjrty/

#### Take care of all possible sceanrios when writing the logic
#### * Conditions handled were count == 0, else if not element then count--, what about count++ when the same element appears again. Costed 2 testcases in the solution. 
#### * Lesson: Reason why some case is missed and handle them as well, when element is not present, when it is present, same element visited again and different element visited.


def solution(A):

    ## Majority Vote Problem Idea - Count the element which already occured logic
    def solution(A):
    
    ## Majorioty Vote Problem Idea
    ## Have two variables one ind keeps track of the element and other the occurence, iterate the array one time and increment for occurence and decrement for not occuring scenario
    
    n = len(A)
    ind = 0
    count = 0
    last_ind = 0
    maxi = 0
    
    if n == 0:
        return -1
    
    for i in range(n):
    # This logic will work according to the explanation, This will give the max element for sure  
        if count == 0:
            count += 1
            ind = A[i]
            last_ind = i
        else:
            # Count for same number again
            if A[i] == ind:
                count += 1
            else:    
                count -= 1
    # we got to find whether the given element is greater than half the array length
    for i in range(n):
        if A[i] == ind:
            maxi += 1
            #last_ind = i
            
    #if float(max) > n/2.0:
    if maxi > n//2:
        return last_ind
    else:
        return -1

    """	
    ## Two testcases keep failing for random and large number 85+ all param pass
    ## Majorioty Vote Problem Idea
    ## Have two variables one ind keeps track of the element and other the occurence, iterate the array one time and increment for occurence and decrement for not occuring scenario
    
    n = len(A)
    ind = 0
    count = 0
    last_ind = 0
    maxi = 0
    
    if n == 0:
        return -1
    
    for i in range(n):
    # This logic will work according to the explanation, This will give the max element for sure  
        if count == 0:
            count += 1
            ind = A[i]
            last_ind = i
        else:
            count -= 1
    # we got to find whether the given element is greater than half the array length
    for i in range(n):
        if A[i] == ind:
            maxi += 1
            #last_ind = i
            
    #if float(max) > n/2.0:
    if maxi > n//2:
        return last_ind
    else:
        return -1
    """ 
    """
    # 50 percent on all param 
    ### Throwing the last index
    n = len(A)
    ind = 0
    max = 0
    count = [0 for i in range(n)]
    if n == 0:
        return -1
    for i in range(n):
        count[A[i]] += 1
        if count[A[i]] > max:
            max = count[A[i]]
            ind = i
    if float(max) > n/2.0:
        return ind
    else:
        return -1
    """
    
    """
    ### Passes for 75 to 80 percent on all params
    # Dictionary method
    n = len(A)
    count = {}
    max = 0
    if n == 0:
        return -1
    for i in range(n):
        if A[i] not in count:
            count[A[i]] = [0,[]]
        count[A[i]][0] += 1
        count[A[i]][1].append(i)
        if count[A[i]][0] > max:
            max = A[i]
    #print(count[max][0],n/2)
    if float(count[max][0]) > n/2.0:
        return count[max][1][0]
    else:
        return -1
    """    
