class Solution:
    def averageValue(self, nums: List[int]) -> int:
        
        total = 0
        count = 0
        
        for i in range(len(nums)):
            if nums[i]%2 == 0 and nums[i]%3 == 0:
                count += 1
                total += nums[i]
        
        if total == 0 or count == 0:
            return 0
        
        return total//count
