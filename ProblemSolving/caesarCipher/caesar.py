#!/bin/python

import sys

def caesarCipher(s, k):
    # Works but fails a number of testcases
    # Analysis - k = 100 fails, as the number always exceeds range of letters - fixed and 100 pass
    string = list(s)
    for i in range(len(string)):
        if ord(string[i]) > 96 and ord(string[i]) < 123:
            value = ord(string[i])+k
            while value > 122:
                sub = value - 122
                value = 96+sub
            string[i] = chr(value)
        if ord(string[i]) > 64 and ord(string[i]) < 91:
            value = ord(string[i])+k
            while value > 90:
                sub = value - 90
                value = 64+sub
            string[i] = chr(value)
    return ''.join(string)

if __name__ == "__main__":
    n = int(raw_input().strip())
    s = raw_input().strip()
    k = int(raw_input().strip())
    result = caesarCipher(s, k)
    print result

