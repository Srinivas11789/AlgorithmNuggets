#!/bin/python

import sys

def marcsCakewalk(calorie):
    # Complete this function
    n = len(calorie)
    # Formula: previous calorie + 2^prev * calorie
    # Idea: to descending order sort the calorie and use so that multiplication stays minimum
    calorie = sorted(calorie, reverse=True)
    psum = 0
    for i in range(n):
        psum += (2**i) * calorie[i]
    return psum

if __name__ == "__main__":
    n = int(raw_input().strip())
    calorie = map(int, raw_input().strip().split(' '))
    result = marcsCakewalk(calorie)
    print result
