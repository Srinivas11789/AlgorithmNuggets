class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 100 pass - A simple and clear solution from discussion by mzchen
        # Result and length variables
        result = nums[0]
        n = len(nums)
        
        # Two pointers to hold maximum and minimum at each point of time
        maxi = result
        mini = result
        
        # Loop throught the range
        for i in range(1,n):
            
            # Negative numbers handle - swap the numbers when a negative number is seen
            if nums[i] < 0:
                mini, maxi = maxi, mini
                
            print maxi, mini
            
            # Calculating the maximum and minimum as we traverse through the array
            # Why? Maxi - To determine the visited number to be maximum when multiplied
            # Why? Mini - To determine the minimum last visited as we traverse through - this is done
            #             calculate swap when a negative number is visited, as negative number convert 
            #             Big numbers to smallest or small number to biggest when negative
            maxi = max(nums[i], maxi*nums[i])
            mini = min(nums[i], mini*nums[i])
            
            # Extracting the result to the maximum ever seen
            result = max(result, maxi)
            
        return result
        
        """
        # Stumbles with all negative numbers 
        # Finding the longest length of the array without 0 or negative numbers, if every number is positive then the maximum sum of the subarray will be the whole array
        
        n = len(nums)
        maxi = -6000000000
        prod = 1
        anti = 1
        for i in range(n):
            if nums[i] > maxi:
                maxi = nums[i]
            if nums[i] > 0:
                prod *= nums[i]
            else:
                if nums[i] < 0:
                    anti = nums[i] * anti
                    if anti > maxi:
                        maxi = anti
                else:
                    anti = 1
                if maxi > 0 and prod > maxi:
                    maxi = prod
                    prod = 1
            print prod, maxi
        return maxi
        """
        
        
        """
        # Sort and solve
        # Wont work - do not change the order of the array
        nums.sort()
        i = -1
        result = 1
        while nums[i] > 0:
            result *= nums[i]
            i -= 1
        
        return result
        """
        
        """
        # Most Passed but TIME LIMIT EXCEEDED
        def product(x):
            p = 1
            for inte in x:
                p *= inte
            return p
        
        # Naive Brute Force Approach
        maxi = -600000000
        n = len(nums)
        for i in range(n):
            for j in range(1,n+1):
                if i+j <= n:
                    print i ,j
                    value = product(nums[i:i+j]) 
                    if value > maxi:
                        maxi = value
        return maxi
        """
        
