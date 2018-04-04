## Merge Sort Sprint

def mergeSort(arr):
   if len(arr) > 1: 
    # Divide and Conquer
    # calulate the length and divide the array 
    n = len(arr)
    mid = n//2

    # Divide the array
    left_array = arr[:mid]
    right_array = arr[mid:]
   
    # Recursive Call
    mergeSort(left_array)
    mergeSort(right_array)
    
    # iterate the subarrays and sort
    i = j = k = 0

    while i < len(left_array) and j < len(right_array):
       if left_array[i] < right_array[j]:
          arr[k] = left_array[i]
          i += 1
       else:
          arr[k] = right_array[j]
          j += 1
       k = k + 1

    
    while i < len(left_array):
       arr[k] = left_array[i]
       i = i + 1
       k = k + 1
          
    while j < len(right_array):
       arr[k] = right_array[j]
       j = j + 1
       k = k + 1

   return arr


def mergeSort1(arr):
 
    if len(arr) > 1:
       n = len(arr)
       mid = n//2
       l = arr[:mid]
       r = arr[mid:]

       mergeSort(l)
       mergeSort(r)
   
       i = j = k = 0

       while i < len(l) and j < len(r):
             if l[i] < r[j]:
                arr[k] = l[i]
                i = i + 1
             else:
                arr[k] = r[j]
                j += 1
             k += 1
         
       while i < len(l):
             arr[k] = l[i]
             i += 1
             k += 1
       
       while j < len(r):
             arr[k] = r[j]
             j += 1
             k += 1
        
    return arr



def main():
    array = [5,6,7,4,3,9,10,123,45,0]
    print mergeSort1(array)

main()
