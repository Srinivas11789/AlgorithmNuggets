#!/bin/python

import sys

def toys(w):
    # Complete this function
    # Timeout Failure > O(N)
    """
    n = len(w)
    w = sorted(w)
    result = []
    count = 0
    for i in range(n):
        # 1+4=5
        if w[i] not in result:
            max = w[i] + 4
            count += 1
            # 1 2 3
            for j in range(i,n):
                if w[j] <= max: 
                    result.append(w[j])
    return count

    # Perfect solution
    """
    w = sorted(w)
    n = len(w)
    max = 0
    count = 0
    for i in range(n):
        if w[i] > max:
            max = 0
        if max == 0:
            max = w[i]+4
            count += 1
            #print max
            #print w[i]
    return count
        
        
                
            
if __name__ == "__main__":
    n = int(raw_input().strip())
    w = map(int, raw_input().strip().split(' '))
    result = toys(w)
    print result

