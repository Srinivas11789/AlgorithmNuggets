class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        # 100 pass - Dictionary method
        import collections
        dic = collections.Counter(nums)
        for k,v in dic.items():
            if v == 1:
                return k
        """
        
        """
        # Sum method
        total_sum = sum(set(nums))
        return 2*total_sum - sum(nums)
        """
        
        # Binary Search
        n = len(nums)
        low = 0
        high = n-1
        while low < high:
            mid = (low+high)//2
            if nums[mid] == nums[mid^1]:
                low = mid + 1
            else:
                high = mid
        return nums[low]
        
