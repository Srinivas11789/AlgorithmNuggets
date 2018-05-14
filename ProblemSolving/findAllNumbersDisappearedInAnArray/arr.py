class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # 1. Try with O(n) run-time and O(1) space -Pending
        
        
        # 2. 100pass - Most of the helpers have one constant space present to carry out the operation

        # Logic -- referencing index as iteration and converting values such that we know if it was visited or not. Leverage indices vs values logic. Convert all the visited values to corresponding indices in (0-n) form by subtracting 1 and change the corresponding value to negative. Hence for a value 2 present in array, we have array index 2-1=1 a negative value.
        
        # Constant space
        result = []
        
        for num in nums:
            nums[abs(num)-1] = abs(nums[abs(num)-1])*-1

        # Looking for positive values and getting the corresponding index+1 gives the result
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        
        return result
        
        
        """
        # Time Limit Exceeded
        n = len(nums)
        nums.sort()
        for i in range(1,n+1):
            #print nums[0],i,nums
            if len(nums) > 0 and nums[0] == i:
                while len(nums) > 0 and nums[0] == i:
                    del nums[0]
                    #print nums
            else:
                nums.append(i)
        return nums
        """
        
        """
        # Time limit exceeded => Use O(1) space and O(N) runtime
        n = len(nums)
        nums = list(set(nums))
        diff = n-len(nums)
        i = 1
        j = i-1
        while i < n+1:
            #print i, nums[j], nums
            if not nums:
                nums.append(i)
            elif i == nums[j]:
                nums.pop(j)
            else:
                nums.append(i)
            i += 1
        return nums
        """
