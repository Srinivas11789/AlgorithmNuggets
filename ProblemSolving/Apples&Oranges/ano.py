from __future__ import print_function

import os
import sys

#
# Complete the countApplesAndOranges function below.
#
def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    # Apple Score
    
    # s->t is where the house is placed
    # a is the place where tree is located
    
    # apples which are thrown
    app_score = 0
    for throw in apples:
        if a+throw >= s and a+throw <= t:
            app_score += 1
    
    # Orange Score
    # s->t is where the house is placed
    # b is the place where tree is located
    
    # oranges which are thrown
    org_score = 0
    for throw in oranges:
        if b+throw >= s and b+throw <= t:
            org_score += 1
    
    print(app_score)
    print(org_score)
    

if __name__ == '__main__':
    st = raw_input().split()

    s = int(st[0])

    t = int(st[1])

    ab = raw_input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    apple = map(int, raw_input().rstrip().split())

    orange = map(int, raw_input().rstrip().split())

    countApplesAndOranges(s, t, a, b, apple, orange)
