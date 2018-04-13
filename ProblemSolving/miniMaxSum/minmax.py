#!/bin/python

from __future__ import print_function

import os
import sys

def miniMaxSum(arr):
    
    mini = 6000000000
    maxi = -6000000000
    sumi = 0
    for i in range(len(arr)):
        sumi += arr[i]
    for i in range(len(arr)):
        if sumi - arr[i] > maxi:
            maxi = sumi - arr[i]
        if sumi - arr[i] < mini:
            mini = sumi - arr[i]
    print(str(mini)+" "+str(maxi))

if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    miniMaxSum(arr)

