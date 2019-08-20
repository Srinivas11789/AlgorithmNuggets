"""
Given a list, find the k-th largest element in the list.
Input: list = [3, 5, 2, 4, 6, 8], k = 3
Output: 5
Here is a starting point:

def findKthLargest(nums, k):
  # Fill this in.

print findKthLargest([3, 5, 2, 4, 6, 8], 3)
# 5
"""

def findKthLargest(nums, k):
    # Write any sorting algo or use inbuilt to sort
    nums.sort()
    # return the index from the reverse 
    return nums[::-1][k-1]

def heapWay(nums, k):
    

print findKthLargest([3, 5, 2, 4, 6, 8], 4)
