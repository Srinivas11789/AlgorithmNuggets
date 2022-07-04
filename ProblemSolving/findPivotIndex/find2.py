class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0
        
        sum_of_array = 0
        for i in nums:
            sum_of_array += i
        
        lsum = 0
        rsum = sum_of_array

        for i in range(len(nums)):
            rsum -= nums[i]
            if lsum == rsum:
                return i
            lsum += nums[i]
            
        return -1
