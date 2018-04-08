#!/bin/python

import sys

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    result = [0,0,0,0]
    for char in password:
            if char in numbers:
                result[0] += 1
            if char in lower_case:
                result[1] += 1
            if char in upper_case:
                result[2] += 1
            if char in special_characters:
                result[3] += 1
    #print result
    if n + result.count(0) < 6:
            return result.count(0) + (6-n-result.count(0))
    else:
        return result.count(0)
            
if __name__ == "__main__":
    n = int(raw_input().strip())
    password = raw_input().strip()
    answer = minimumNumber(n, password)
    print answer

