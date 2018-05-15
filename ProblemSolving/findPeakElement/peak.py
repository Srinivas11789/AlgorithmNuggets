class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Naive method
        n = len(nums)
        peak = None
        if n > 2:
            for i in range(1,n-1):
                if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                    #print nums[i], i
                    peak = i
            if not peak:
                return nums.index(max(nums))
            else:
                return peak
        elif n > 1:
            if nums[1] > nums[0]:
                return 1
            else:
                return 0
        else:
            return 0
        
        
        
