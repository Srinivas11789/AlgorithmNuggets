# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function

def mergeSort(a):
    if len(a) > 1:
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]
        
        mergeSort(left)
        mergeSort(right)
        
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i = i + 1
            else:
                a[k] = right[j]
                j = j + 1
            k = k + 1
        
        while i < len(left):
            a[k] = left[i]
            i = i + 1
            k = k + 1
        
        while j < len(right):
            a[k] = right[j]
            j = j + 1
            k = k + 1
    return a

n = raw_input()
a = map(int,raw_input().strip().split(' '))
print(mergeSort(a))
