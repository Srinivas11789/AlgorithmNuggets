### Array's
### * Reverse iteration of array

#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
#for item in arr[::-1]:
#    print item,
for i in range(n-1,-1,-1):
    print arr[i],

