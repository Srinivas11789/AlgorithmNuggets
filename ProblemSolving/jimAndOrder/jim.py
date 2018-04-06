#!/bin/python

import sys

def jimOrders(orders):
    result = []
    for item in orders:
        result.append(item[0]+item[1])
    s = sorted(result)
    ans = []
    #for i in range(len(s)):
    #    result[result.index(s[i])] = i+1
    #return result
    
    # Fix for same number occurrence
    for item in s:
        i = 1
        while result.index(item)+i in ans:
            i += 1
        ans.append(result.index(item)+i)
    return ans
        

if __name__ == "__main__":
    n = int(raw_input().strip())
    orders = []
    for orders_i in xrange(n):
        orders_temp = map(int,raw_input().strip().split(' '))
        orders.append(orders_temp)
    result = jimOrders(orders)
    print " ".join(map(str, result))



