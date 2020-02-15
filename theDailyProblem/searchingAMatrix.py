"""
Given a matrix that is organized such that the numbers will always be sorted left to right, and the first number of each row will always be greater than the last element of the last row (mat[i][0] > mat[i - 1][-1]), search for a specific value in the matrix and return whether it exists.

Here's an example and some starter code.

def searchMatrix(mat, value):
  # Fill this in.
  
mat = [
    [1, 3, 5, 8],
    [10, 11, 15, 16],
    [24, 27, 30, 31],
]

print(searchMatrix(mat, 4))
# False

print(searchMatrix(mat, 10))
# True
"""

# Logic 1: Search is best with binarySearch --> Doing BinarySearch in 2D is the challenge
# the start and end of each row can be a sorted list to do search?
# first, going naive with iteration plus binary search or flatten the matrix and then perform binary search
def binarySearch(array, value):
    print(array)
    n = len(array)
    left = 0
    right = n-1
    while left < right:
        mid = left + (right-left)//2
        print(left, mid, right)
        if array[mid] == value:
           return mid 
        elif array[mid] < value:
           left = mid
        else:
           right = mid
      
        if right-left == 1:
           if array[left] == value:
              return left
           elif array[right] == value:
              return right
           else:
              return -1

# Logic 2: Can you optimize and perform binarySearch in 2D in one go?
        
def searchMatrix(mat, value):
    import itertools
    return binarySearch(list(itertools.chain.from_iterable(mat)), value) 
    

mat = [
    [1, 3, 5, 8],
    [10, 11, 15, 16],
    [24, 27, 30, 31],
]

print(searchMatrix(mat, 4))
# False

print(searchMatrix(mat, 10))
# True
