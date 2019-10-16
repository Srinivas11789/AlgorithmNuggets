class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        nums.sort()
        
        maxi = 1
        count = 1
        
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 1:
                count += 1
            elif nums[i+1]-nums[i]  == 0:
                pass
            else:
                count = 1
            maxi = max(maxi, count)
        return maxi
        
