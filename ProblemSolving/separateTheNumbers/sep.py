# Pending Task - Yet to complete

#!/bin/python

import sys

def separateNumbers(s):
    
    n = len(s)
    
    
    
    """
    n = len(s)
    if n%2 == 0:
        mid = n//2
    else:
        mid = n//2 + 1
        
    fail = 1
    for k in range(1,mid):
        arr = [s[i:i+k] for i in range(0,len(s),k)]
        for j in range(len(arr)-1):
            if len(arr[j]) < len(str(int(arr[j])+1)):
                value = str(int(arr[j])+1)
                newi = [s[len(arr[j]):][i:i+len(value)] for i in range(0,len(s),len(value))]
                print value, newi
                if value == newi[j]:
                    fail = 0
                else:
                    fail = 1 
            elif int(arr[j]) + 1 != int(arr[j+1]):
                fail = 1
            else:
                fail = 0
    if fail == 0:
        return "YES "
    else:
        return "NO"
        
    """
    
    """
    n = len(s)
    s = list(s)
    mid = n//2
    for i in range(1,n):
        value = "".join(s[:i])
        if value == "0":
            return "NO"
        nexte = str(int(value) + 1)
        #print value, nexte, "".join(s[i:(i)+len(nexte)])
        if "".join(s[i:(i)+len(nexte)]) == nexte:
            newi = int(nexte)+1
            if nexte == "".join(s[:(i)+len(nexte)]):
                return "YES "+value
    return "NO"
    """
    
    """
    # decision logic based on the length of the array
    #s = list(s)
    n = len(s)
    mid = n//2
    
    # from back add string and minus
    i = n-1
    k = 1
    while i >= 0:
        if k <= mid:
            # 1st 4 3
            # 2nd 100 99
            # 3rd
            print s[i:], s[i-k:i]
            if int(s[i:]) - int(s[i-k:i]) == 1:
                return "YES "+ s[:k]
        i -= 1
        k += 1
    return "NO"
    """
    
    """
    # Not working for different length of numbers
    s = list(s)
    for k in range(1,5):
        for i in range(len(s)-1):
            result = s[:k]
            if int(s[i+k]) - int(s[i]) == 1:
                result = s[k:]
            else:
                print "NO"
                break
    print "YES "+ "".join(result)
    """

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        s = raw_input().strip()
        print separateNumbers(s)


