#!/bin/python

import sys

def maximumToys(prices, k):
    # Complete this function
    n = len(prices)
    prices = sorted(prices)
    maxi = 0
    count = 0
    for i in range(n):
        maxi = maxi + prices[i]
        if maxi > k:
            break
        else:
            count += 1
    return count
        
            
        

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    prices = map(int, raw_input().strip().split(' '))
    result = maximumToys(prices, k)
    print result

