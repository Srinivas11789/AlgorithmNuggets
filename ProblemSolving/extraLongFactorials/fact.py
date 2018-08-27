#!/bin/python

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.

# Recursive 
def extraLongFactorials(n):
    if n > 0:
        return n * extraLongFactorials(n-1)
    else:
        return 1

# Iterative
def extraLongFactorialsIterative(n):
    result = 1
    while n > 0:
        result = result * (n)
        n -= 1
    return result

if __name__ == '__main__':
    n = int(raw_input())

    print extraLongFactorialsIterative(n)

