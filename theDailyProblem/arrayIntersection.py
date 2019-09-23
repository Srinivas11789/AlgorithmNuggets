"""
Given two arrays, write a function to compute their intersection - the intersection means the numbers that are in both arrays.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:
Each element in the result must be unique.
The result can be in any order.

Here's a starting point:

class Solution:
  def intersection(self, nums1, nums2):
    # Fill this in.

print Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4])
# [9, 4]
"""

class Solution:
  def intersection(self, nums1, nums2):
    # Logic 1 - dictonary method
    import collections
    counts = collections.Counter(set(nums1))+collections.Counter(set(nums2))
    result = [k for k,v in counts.items() if v > 1]    
    return result

  def intersection2(self, nums1, nums2):
    # Logic 2 - Set intersection
    return list(set(nums1).intersection(set(nums2)))

  def intersection3(self, nums1, nums2):
    # Logic 3 - Iteration
    result = []
    return result 

print Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4])
print Solution().intersection2([4, 9, 5], [9, 4, 9, 8, 4])
print Solution().intersection3([4, 9, 5], [9, 4, 9, 8, 4])
# [9, 4]
