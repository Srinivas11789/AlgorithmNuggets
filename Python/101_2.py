#typecasting and output

"""
Tip Learnt:
* when using parantheses look at the operation inside, operation with float returns a float but the paranthesis operation could return you an int which could distrupt everything, learn what is inside the paranthesis evaluate and use
* In order to round the value, a direct conversion to int can be done or math.ceil or floor could be used. In addition to that round can also be used. The last test case continuouslt kept failing until round was used. Either know in depth of the function being used or try all the methods once you spot a anamoly like try all types or ways to do it for rounding a number
"""


#!/bin/python

import sys
import math

if __name__ == "__main__":
    meal_cost = float(raw_input().strip())
    tip_percent = int(raw_input().strip())
    tax_percent = int(raw_input().strip())
    
    #  tip = meal_cost * (tip_percent/100) - this evaluates to zero because the paranthesis is evaluated first and they are integer division resulting in 0
    tip = meal_cost * tip_percent/100
    tax = meal_cost * tax_percent/100
    total_cost = meal_cost + tip + tax
    print "The total meal cost is "+str(int(round(total_cost)))+" dollars."


