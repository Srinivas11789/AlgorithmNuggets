# Quick Sort

# Concept: 
"""
Pick an element possibly the last and mark it as pivot, perform an operation called as partitioning where all the elements larger than pivot are on the right hand side and the elements lesser than pivot are on the left hand side. Once the pivot is placed in its final correct position. Apply partitioning and choosing pivot in the left and the right subarray recursively to obtaint he sorted array
"""

# Partition Function
# Pivot and arranging elements

def partition(a, low, high):
    index = low - 1
    pivot = a[high]
    
    for j in range(low, high):
        if a[j] <= pivot:
             index += 1
             a[index],a[j] = a[j],a[index] 
    a[index+1],a[high] = a[high], a[index+1]
    return index+1   


def quickSort(a, low, high):
   
    if low < high:
    	# Select pivot and partitioning
    	n = len(a)
  
    	pivot = partition(a, low, high)
   
    	quickSort(a, low, pivot-1)
        quickSort(a, pivot+1, high)
    

def main():
    array = [5,6,2,1,9,9,6,5,3,1,0,7,5]
    n = len(array)
    quickSort(array, 0, n-1)
    print array

main()
