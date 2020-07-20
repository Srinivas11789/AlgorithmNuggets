# Logic 1: 2 pointers - 72%
"""
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        j = n # or len(nums)//2
        result = []
        while i < n and j < len(nums):
            result.append(nums[i])
            result.append(nums[j])
            i += 1
            j += 1
        return result
"""

# Logic 2: Same logic above, Reducing to one var 
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        result = []
        while i < n:
            result.append(nums[i])
            result.append(nums[n+i])
            i += 1
        return result
