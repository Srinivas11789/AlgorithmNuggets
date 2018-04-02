#!/bin/python

import sys

def lonelyinteger(a):  
    
    # One line method - ref from hr discussion
    # x, y --> first 2 elements and apply formula --> result and the next element
    # Exoring over the list returns the element which occurred only once, as the same element exored is zero x^x = 0
    # Reduce function iterates over the array and returns the result
    answer = reduce((lambda x, y: x^y), a)
    return answer
    
    """
    # Dictionary Method - 100 pass
    n = len(a)
    occur = {}
    for i in range(n):
        if a[i] not in occur:
            occur[a[i]] = 0
        occur[a[i]] += 1
    for key, value in occur.items():
        if value == 1:
            return key
    """
    # List method to hold the count of each index 
    

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
result = lonelyinteger(a)
print(result)

