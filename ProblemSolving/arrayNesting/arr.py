class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Optimized Logic - 
        # * Remove the List operation/lookup of temp
        # * Arrive at j = nums[j] in a different fashion by sub and add
        maxi = 0
        n = len(nums)
        for i in range(n):
            temp = 0
            j = i
            while nums[j] >= 0:
                temp += 1
                nums[j] -= n
                j = nums[j] + n
            if temp > maxi:
                maxi = temp
        return maxi
        
        """
        # Direct List Logic
        # Correct Logic but Time Limit Exceeded
        # All pass except performance cases
        maxi = 0
        n = len(nums)
        for i in range(n):
            temp = []
            temp.append(nums[i])
            while nums[temp[-1]] not in temp and nums[temp[-1]] in nums:
                temp.append(nums[temp[-1]])
            if len(temp) > maxi:
                maxi = len(temp)
        return maxi
        """
    
            
