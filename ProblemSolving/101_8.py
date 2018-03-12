# 101 Challenge -> Binary Challenge
# Lesson: 
#  * Binary number conversion in python is easy with bin() function but it adds a "0b" in the front of the string
#  	* Try to bypass the 0b for proper functionality
#  * Max decision loop => (If max >) should be placed properly for the answer.
#       * Place the decision loop logic so that you could fetch the right output. For instance placing the resp if loop in the beginning of for loop throws wrong ans

#!/bin/python

import sys


n = int(raw_input().strip())

binaryn = bin(n)[2:]
#print binaryn
result = {"0":0, "1":0}
max = 0
#binaryn = str(n)
for char in binaryn:
    if char == "1":
        result["1"] += 1
    if result["1"] > max:
        max = result["1"]
    if char == "0":
        result["0"] += 1
        result["1"] = 0
print max
