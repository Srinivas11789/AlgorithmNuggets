#!/bin/python

import sys

def flippingBits(N):
    # bin wont work as need to convert into 32 bit binary
    #binary = bin(N)[2:]
    # format method 
    binary = list('{:032b}'.format(N))
    for i in range(len(binary)):
        binary[i] = str(int(binary[i])^1)
    return int(''.join(binary),2)

if __name__ == "__main__":
    T = int(raw_input().strip())
    for a0 in xrange(T):
        N = long(raw_input().strip())
        result = flippingBits(N)
        print result


