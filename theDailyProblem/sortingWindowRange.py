"""
Given a list of numbers, find the smallest window to sort such that the whole list will be sorted. If the list is already sorted return (0, 0). You can assume there will be no duplicate numbers.

Example:
Input: [2, 4, 7, 5, 6, 8, 9]
Output: (2, 4)
Explanation: Sorting the window (2, 4) which is [7, 5, 6] will also means that the whole list is sorted.

def min_window_to_sort(nums):
  # Fill this in.
  
print(min_window_to_sort([2, 4, 7, 5, 6, 8, 9]))
# (2, 4)
"""

def min_window_to_sort(nums):
  
  # Logic O(N) iterate to record the incorrect sort
  left, right = None, None
  for i in range(len(nums)-1):
    if nums[i] > nums[i+1]:
      if not left:
        left = i
      else:
        right = i+1
      nums[i], nums[i+1] = nums[i+1], nums[i]
  if left == None:
    left = 0
  if right == None:
    right = 0
  return (left, right)
      
print(min_window_to_sort([2, 4, 7, 5, 6, 8, 9]))
# (2, 4)
print(min_window_to_sort([2, 3, 7, 5, 4, 6, 8, 9]))
