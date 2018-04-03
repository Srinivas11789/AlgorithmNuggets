#!/bin/python

import sys

def camelcase(s):
    count = 1
    for char in s:
        if ord(char) > 64 and ord(char) < 91:
            count += 1
    return count 

if __name__ == "__main__":
    s = raw_input().strip()
    result = camelcase(s)
    print result

