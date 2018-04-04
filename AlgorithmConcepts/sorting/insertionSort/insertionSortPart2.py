# Traverse both directions once a mismatch is found and sort by shifting
# Assumption: First element is sorted

#!/bin/python
from __future__ import print_function
import sys

def insertionSort2(n, arr):
    # Complete this function
    #!/bin/python
    select = arr[0]
    current = None
    for i in range(1,n):
        if arr[i] > select:
            print(*arr)
            select = arr[i]
        else: 
            current = arr[i]
            arr[i] = select
            arr[i-1] = current
            #print(*arr)
            for j in range(i-2,-1,-1):
                if current < arr[j]:
                    arr[j+1] = arr[j]
                    arr[j] = current
                    #print(*arr)
            print(*arr)
         
                    
                    

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    insertionSort2(n, arr)
