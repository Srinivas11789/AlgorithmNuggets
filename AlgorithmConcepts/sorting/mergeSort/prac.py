def mergeSort(a):
 if len(a) > 1:
    total = len(a)
    mid = total//2
    
    left = a[:mid]
    right = a[mid:]

    m = len(left)
    n = len(right)
 
    mergeSort(left)
    mergeSort(right)

    i=j=k=0
    result = []

    while i < m and j < n:
          if left[i] < right[j]:
             a[k] = left[i]
             i += 1
          else:
             a[k] = right[j]
             j += 1
          k += 1

    while i < m:
          a[k] = left[i]
          i += 1
          k += 1

    while j < n:
          a[k] = right[j]
          j += 1
          k +- 1

    return a

def main():

    a = [4,2,6,3,9,1]
    print mergeSort(a)

main()
