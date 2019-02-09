# Pending...

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        
        # Logic 1: Bruteforce with itertools...
        
        # BruteForce with all the combinations for the target sum
        # * Use itertools
        # * add symbols to each integer and then eval() to check for target sum
        
        import itertools
        
        count = 0
        
        if 0 in nums:
            i = 0
            while nums and i < len(nums):
                if nums[i] == 0:
                    del nums[i]
                else:
                    i += 1
        
        if not nums:
            return 0
        
        n = len(nums)    
        
        for combination in itertools.product(["+","-"], repeat=n):
            expression = ""
            for i in range(n):
                expression += combination[i]+str(nums[i])
            if eval(expression) == S:
                count += 1
        return count
