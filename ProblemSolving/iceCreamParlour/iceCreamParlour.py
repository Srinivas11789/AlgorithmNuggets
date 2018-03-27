#!/bin/python

import sys

def solve(arr, money):
    # Complete this function
    flavours = len(arr)
    hashtable = {}
    # O(N) logic same as below with dictionary to memo and track the values works
    for i in range(flavours):
        value = money - arr[i] # Same logic as I thought of, but the use of dictionary races the speed
        
        # Lookup for a value in the dictionary is faster
        if value in hashtable:
                #print i
                print arr.index(value)+1, i+1
        else:
             hashtable[arr[i]] = value
    
    
    """
    # O(N) almost but still fails - 1 testcase pass, all other timeouts
    for i in range(flavours):
        #if i > 0:
        #    print arr[:i-1]+arr[i+1:]
        #else:
        #    print arr[:i]+arr[i+1:]
        value = money - arr[i]
        if value in arr[i+1:]:
                print i+1, arr[i+1:].index(value)+i+1+1
    """            
    """
        # Thinking on some logic to eliminate redundancy of index in case of (2,2)
        if i > 0:
            if value in arr[:i-1]+arr[i+1:]:
                print str(i+1)+" "+str(arr.index(value))
                break
        else:
            if value in arr[:i]+arr[i+1:]:
                if arr.index(value) == i:
                    
                print str(i+1)+" "+str(arr.index(value))
                break
    """
    """
    # O(N2) - doesnt work
    for i in range(flavours):
        for j in range(i+1,flavours):
            if arr[i] + arr[j] == money:
                print str(i+1)+" "+str(j+1)
                break
    """

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        money = int(raw_input().strip())
        n = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        solve(arr, money)


