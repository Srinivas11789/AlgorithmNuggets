#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the pangrams function below.
#
def pangrams(s):
    alp = list('abcdefghijklmnopqrstuvwxyz')
    s = s.lower()
    for char in alp:
        if char not in s:
            return "not pangram"
    return "pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

