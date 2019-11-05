"""
You are given a list of n numbers, where every number is at most k indexes away from its properly sorted index. Write a sorting algorithm (that will be given the number k) for this list that can solve this in O(n log k)

Example:
Input: [3, 2, 6, 5, 4], k=2
Output: [2, 3, 4, 5, 6]
As seen above, every number is at most 2 indexes away from its proper sorted index.

Here's a starting point:

def sort_partially_sorted(nums, k):
  # Fill this in.

print sort_partially_sorted([3, 2, 6, 5, 4], 2)
"""

def sort_partially_sorted(nums, k):
  n = len(nums)
  for i in range(len(nums)):
    time = k
    j = i+1
    mini = float('inf')
    min_ = float('inf')
    while time > 0 and j < len(nums):
      #print(i, j)
      if nums[j] < nums[i] and nums[j] < mini:
        mini = nums[j]
        min_ = j
      j += 1
      time -= 1
    if min_ < len(nums):
      nums[i], nums[min_] = nums[min_], nums[i]
    #print(nums, i, mini)
  return nums  

print sort_partially_sorted([3, 2, 6, 5, 4], 2)
print sort_partially_sorted([2, 3, 0, 1], 2)
