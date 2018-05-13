class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Solution: Get the minimum number from the array, find the difference of each element with the minimum and sum them up for the result
        
        select = min(nums)
        answer = 0
        for element in nums:
            answer += element-select
        return answer
        
        """
        ### Thoughts
        # Logic1: sort and continue
        nums = sorted(nums)
        n = len(nums)
        value = nums[n-1] - nums[0]
        if value%2 == 0 and value != 0:
            return nums[n-1]
        else:
            return value
        
        # Logic2: Loop until set(array) is One
        #while set()
        """
        
