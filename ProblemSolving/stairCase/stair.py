#!/bin/python

from __future__ import print_function

import os
import sys

def staircase(n):
    
    for i in range(n,0,-1):
        print(" "*(i-1)+"#"*(n-(i-1)))

if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)

