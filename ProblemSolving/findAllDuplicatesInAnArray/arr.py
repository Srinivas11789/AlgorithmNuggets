class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # similar to disappearing elements finding problem
        
        # Answer to save the value directly rather than the index of the element
        ans = []
        
        # Iterate through the numbers
        for num in nums:
            
            # If the corresponding index is already made negative then it has been already visited
            if nums[abs(num)-1] < 0:
                # Append the value to the result
                ans.append(abs(num)) 
            else:
                # Make the corresponding index negative
                nums[abs(num)-1] = abs(nums[abs(num)-1])*-1
            #print nums
        return ans
        
        """
        # 100 pass using sort
        ans = []
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                ans.append(nums[i])
        return ans
        """ 
        
        """
        # Time Limit Exceeded
        n = len(nums)
        result = []
        for num in nums:
            if num not in result and nums.count(num) > 1:
                result.append(num)
        return result
        """
