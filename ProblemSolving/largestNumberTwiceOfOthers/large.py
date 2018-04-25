class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 100 pass - Pythonic using sorted
        
        # or use max() to get the maximum which is a cleaner solution
        result = nums
        nums =sorted(nums)
        n = len(nums)
        maxi = nums[n-1]
        
        for i in range(n-1):
            if maxi >= 2*nums[i]:
                pass
            else:
                return -1
        return result.index(maxi)
    
        
