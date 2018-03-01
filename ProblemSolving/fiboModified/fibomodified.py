#!/bin/python

import sys
def fibo(n):
    arr = []
    if n == 0:
        arr.append(0)
        return 0
    if n == 1:
        arr.append(1)
        return  1
    if n < len(arr) and arr[n]:
        return arr[n]
    return fibo(n-2) + (fibo(n-1))**2

def fibonacciModified(t1, t2, n):
    """
    arr = []
    if n == t1:
        arr.append(t1)
        return 0
    if n == t2:
        arr.append(t2)
        return  1
    if n < len(arr) and arr[n]:
        return arr[n]
    return fibo((n-2),n-2,n-2) + (fibo(n-1))**2
    """
    #print n
    #return fibo(n-1)
    arr = [t1,t2]
    for i in range(2,n):
        arr.append(arr[i-2] + arr[i-1]**2)
    return arr[len(arr)-1]

if __name__ == "__main__":
    t1, t2, n = raw_input().strip().split(' ')
    t1, t2, n = [int(t1), int(t2), int(n)]
    result = fibonacciModified(t1, t2, n)
    print result

