#!/bin/python

import sys

def factorial(n):
    # Complete this function
        fact = []
        if n == 1:
            fact.append(1)
            return 1
        elif n < len(fact):
            return fact[n]
        else:
            num = factorial(n-1) * n
            fact.append(num)
            return num

if __name__ == "__main__":
    n = int(raw_input().strip())
    result = factorial(n)
    print result
