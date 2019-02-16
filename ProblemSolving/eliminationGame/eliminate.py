class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Interpret the Same condition in another way
        # - Instead of deleting, we add only the respective digits...
        nums = range(1,n+1)
        while len(nums) > 1:
            n = len(nums)
            i = 1
            temp = []
            while i <= n-1:
                temp.append(nums[i])
                i += 2
            nums = temp[::-1]
        return nums[0]  
    
    
        """
        # Literal solve - pseudocode
        
        nums = range(1,n+1)
        
        while len(nums) > 1:
            n = len(nums)
            i = 0
            while i <= n-1:
                nums.pop(i)
                i += 2
            i = len(nums)-1
            while i >= 0:
                nums.pop(i)
                i -= 2
        return nums[0]
        """
            
        
        
