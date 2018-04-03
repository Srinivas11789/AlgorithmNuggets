#!/bin/python

import sys

def solve(a):
    # Complete this function
    
    
    
    # brute force with n one loop else more loops
    # 
    
    
    n = len(a)
    
    if n == 1:
        return "YES"
    
    """
    i = 0
    j = n-1
    sum1 = a[i] # (1,1)
    sum2 = a[j] 
    
    # [1,2,3,1,2]
    # [1,1,3,2,2]
    
    while i != j:
        if sum1 < sum2:
            i = i + 1
            sum1 = sum1 + a[i]
        else:
            j = j - 1
            sum2 = sum2 + a[j]
        #print sum1,sum2
        if sum1 == sum2 and j-i > 1:
            return "YES"
            break
    return "NO"
    """
    
    """
    # Naive Brute Force Solution - O(N) and while loop both sides
    for i in range(n):
        j = i
        sum1 = 0
        while j >= 0:
            sum1 = sum1 + a[j]
            j -= 1
        j = i
        sum2 = 0
        while j < n:
            sum2 = sum2 + a[j]
            j += 1
        if sum1 == sum2:
            return "YES"
    return "NO"
    """
    
    
    ## Naive Brute Force Solution with Memoization
    sum1 = 0
    sum2 = a[0]
    for i in range(1,n-1):
        j = i
        if sum1 == 0:
            while j < n-1:
                j += 1
                sum1 = sum1 + a[j]
        if sum1 == sum2:
            return "YES"
        sum2 = sum2 + a[i]
        sum1 = sum1 - a[i+1]
    return "NO"
    
    
    
    """
    ### Sum logic
    sum = 0
    for i in range(n):
        sum += a[i]
        
    for i in range(n):
        if i > 0 and i < n-1:
            if (sum-a[i])%2 == 0:
                return "YES"
    return "NO"
    """     
        
    
    
    
            

T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    result = solve(a)
    print(result)


