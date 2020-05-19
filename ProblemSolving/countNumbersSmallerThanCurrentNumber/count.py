class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # Logic 1: Numbers smaller than current number - 100 pass 64% faster
        sortNum = sorted(nums)
        for i in range(len(nums)):
            nums[i] = sortNum.index(nums[i])
        return nums
