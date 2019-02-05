# Logic reference to geekOfGeeks

def heapify(a, n, index):
    largest = index
 
    left = 2*index+1
    right = 2*index+2
  
    if left < n and a[left] > a[largest]:
       largest = left
   
    if right < n and a[right] > a[largest]:
       largest = right

    if largest != index:
       a[index], a[largest] = a[largest], a[index]
       heapify(a, n, largest)

def heapSort(a):
    n = len(a)    

    for i in range(n, -1, -1):
        heapify(a, n, i)
 
    for i in range(n-1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)

def main():
    a = [5,2,6,7,9,3,1,0]
    heapSort(a)
    print a

main()

