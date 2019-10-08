
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        sumi = 0
        for i in range(0, len(nums), 2):
            sumi += nums[i]
        return sumi
            
