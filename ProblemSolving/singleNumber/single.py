class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Try without using a extra memory. 
        
        # 1. Sort it and do it
    
        """
        # 2. pythonic using count - Time limit exceeded
        n = len(nums)
        for i in range(n):
            if nums.count(nums[i]) == 1:
                return nums[i]
        """
        """
        # 3. sum solution
        # Take the sum of the n numbers in a unique list with SET. Twice that list sum would be the scenario where all the elements in the list occur twice. Now sum of the list would be sum of all element twice plus the one element which is left out
        # sum(all element twice) - sum(all element twice + one unique)
        # works 100 but uses sum pythonic
        return 2*sum(set(nums))-sum(nums)
        """
        
        # 4. xor solution
        # Best and works 100 percent 
        # a ^ a = 0
        # a ^ b ^ a = a ^ a ^ b = b
        # Eventually the end would be with the number that occurs only once
        a = 0
        for i in nums:
            a ^= i
        return a
        
        
