#!/bin/python

import sys

def luckBalance(n, k, contests):
    
    # luck balance problem - 100 pass
    # Add all the 0 priority events first and segregate the 1 prior into a list
    total = 0
    maxi = 0
    prior = []
    for item in contests:
        if item[1] == 0:
            total += item[0]
        else:
            prior.append(item[0])
    # Sort the list to decide on what to be added and what not to be
    prior = sorted(prior)
    # Lose most luck ones to gain the luck and win less luck ones to lose them without much changes
    for i in range(len(prior)):
        if i >= len(prior)-k:
            maxi += prior[i]  
        else:
            maxi -= prior[i]
    maxi += total
    return maxi
    
    """
    # Wrong usage of entries
    luck = []
    prior = []
    total = 0
    maxi = float('-Inf')
    for item in contests:
        luck.append(item[0])
        prior.append(item[1])
        total += item[0]
    luck = sorted(luck)
    for i in range(k):
        value = total - luck[i]*2
        if value > maxi and prior[i]:
            maxi = value
    return maxi
    """ 
        
    
if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    contests = []
    for contests_i in xrange(n):
        contests_temp = map(int,raw_input().strip().split(' '))
        contests.append(contests_temp)
    result = luckBalance(n, k, contests)
    print result

