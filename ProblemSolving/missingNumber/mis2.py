class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Logic 1: Sort and Find diff to be consecutive - 44% faster
        
        nums.sort()
        
        # Last integer missing
        if nums and nums[-1] != len(nums):
            return nums[-1]+1
        
        # Starting integer missing
        if nums and nums[0] != 0:
            return 0
        
        # Anything in the middle
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1] == 1:
                continue
            return nums[i]-1
        return -1
        
        
        # Logic 2: 2*O(n), find len(nums) and construct dict/set. Then iterate again for finding missing until len(nums) - 5% faster
        """
        integers = {}
        for i in nums:
            integers[i] = 1
            
        for i in range(len(nums)+1):
            if i not in nums:
                return i
        return -1
        """

        # Logic 3 --> substract sums --> 56% faster
        return sum(range(len(nums)+1)) - sum(nums)
