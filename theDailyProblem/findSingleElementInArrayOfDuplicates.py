"""
Given an array of integers, arr, where all numbers occur twice except one number which occurs once, find the number. Your solution should ideally be O(n) time and use constant extra space.
Example:
Input: arr = [7, 3, 5, 5, 4, 3, 4, 8, 8]
Output: 7
class Solution(object):
  def findSingle(self, nums):
    # Fill this in.

nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print(Solution().findSingle(nums))
# 3
"""

class Solution(object):
  def findSingle1(self, nums):
    # Logic 1: Using Data Structure - Hashmap
    import collections
    counts = collections.Counter(nums)
    for ele, count in counts.items():
        if count == 1:
            return ele
    return -1

  def findSingle2(self, nums):
    # Logic 2: Naive O(n) Iteration
    elements = {}
    for i in range(len(nums)):
        if nums[i] in elements:
            del elements[nums[i]]
        else:
           elements[nums[i]] = 1
    return elements.keys()[0]

nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print(Solution().findSingle1(nums))
print(Solution().findSingle2(nums))
# 3
