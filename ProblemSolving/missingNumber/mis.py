class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        # 100 pass
        # 1. sum solution
        n = len(nums)
        return sum(range(n+1)) - sum(nums)
        
        
        """
        # 2. Iteration through n - Time Limit Exceeded
        n = len(nums)
        for i in range(n+1):
            if i not in nums:
                return i
        return -1
        """
        
        """
        # 100 pass
        # 3. Modify 2 to make it optimized - Using SET in python, optimizes a lot because it converts the datastructure to a hashmap and increase the access time
        n = len(nums)
        nums = set(nums)
        for i in range(n+1):
            if i not in nums:
                return i
        return -1
        """
        
        """
        # 3. XOR logic
        # when you exor the total length of the array again and again with (index^value), we end up in the missing number
        a = len(nums)
        for i in range(len(nums)):
            a ^= i^nums[i]
        return a
        """
    
        """
        # 4. sort it and do it
        
        # 5. Use a dictionary
        """
        
