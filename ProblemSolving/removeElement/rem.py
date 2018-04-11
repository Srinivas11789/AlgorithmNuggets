# Avoid extra space for another array

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        while val in nums:
            del nums[nums.index(val)]
            
        return len(nums)
        
