class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        # Wrong logic - doesnt  work for 4 elements
        # Pythonic sort - fails for 112
        nums = sorted(nums)[::-1]
        maxi1 = 0
        maxi2 = 0
        maxi3 = 0
        if len(nums) >= 3:
            for num in nums:
                if max
            return nums[len(nums)-1]
        else:
            return nums[0]
        """
        
        """
        # Tracking the third max - optimize and improvise, still blocked !!!
        maxi1 = -60000000
        maxi2 = -60000000
        maxi3 = -60000000
        for num in sorted(nums)[::-1]:
            if num > maxi1:
                maxi1 = num
            if num > maxi2 and num < maxi1:
                maxi2 = num
            if num > maxi3 and num < maxi1 and num < maxi2:
                maxi3 = num
            else:
                maxi3 = maxi1
        return maxi3
        """
        
        """
        # 100 pass - Have the presence of mind to think properly - Think straight + clear + logical
        # **** Use SET to eliminate duplicates
        # **** Use SORTED to sort the list
        # **** Use MAX to fetch the maximum as well, these were logic you thought off very soon in a clear mind state
        
        # Only unique
        nums = list(set(nums))
        
        # Length calculation
        n = len(nums)
    
        # Length lesser than 2
        if n <=2 :
            return max(nums)
        else:
            # Sorted logic
            nums = sorted(nums)
            return nums[n-3]
        """
        
        ## 100 pass - Hacky Pythonic Max solution
        
        # Eradicate duplicates
        nums = list(set(nums))
        
        # Length Calculation
        n = len(nums)
        
        # Maximum to return when length is lesser than 3
        maximum = max(nums)
        
        # Loop result 
        result = None
        i = 1
        
        if n <= 2:
            return maximum
        
        while i <= 3 and n >= 3:
            print max(nums), nums
            result = nums.pop(nums.index(max(nums)))
            i += 1
        
        return result
            
        
        
        
        
        

        

