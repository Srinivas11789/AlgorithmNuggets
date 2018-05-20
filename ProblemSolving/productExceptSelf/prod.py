class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # 100 pass - Memoize as we dont want to take the product again and again
        
        # Length of nums and the answer list
        n = len(nums)
        answer = []
        
        # Tracking and changing the values as we progress
        taint = 1
        
        # Looping through the array forward using taint
        for i in range(n):
            answer.append(taint)
            taint = taint * nums[i]
            
        print answer
        
        # Looping through the array backward using taint
        taint = 1
        
        for i in range(n-1,-1,-1):
            answer[i] *= taint
            taint = taint * nums[i]
        return answer
            
            
        """
        # 100 pass - Total result and divide results
        # Handle 0 present in the array, with respect to one zero and multiple zeros present
        # If 0 not in nums
        result = 1
        i = 0
        ans = []
        if 0 not in nums:
            while i < len(nums):
                result *= nums[i]
                i += 1
            i = 0
            
            while i < len(nums):
                if nums[i] == 0:
                    ans.append(0)
                else:
                    ans.append(result//nums[i])
                i += 1
        
            return ans
        
        else:
            if nums.count(0) > 1:
                return [0]*len(nums)
            else:
                index = nums.index(0)
                for i in range(len(nums)):
                    if i == index:
                        pass
                    else:
                        result *= nums[i]
                ans = [0]*len(nums)
                ans[index] = result
        return ans
        """
        
            
