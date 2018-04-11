"""
# Use while for a more control loop than using just for. Deleting the element in the list and simultaneously running a loop will cause errors, prefer to have more control on the loop with While.
# Donot use extra space with an array
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            prev = nums[0]
            i = 1
            while i < len(nums):
                if nums[i] == prev:
                    del nums[i]
                else:
                    prev = nums[i]
                    i = i + 1
        
            return len(nums)
        else:
            return 0
        
        """
        # Hacky
        return set(num)
        """
        
