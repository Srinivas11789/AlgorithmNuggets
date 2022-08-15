class Solution:
    def rob(self, nums: List[int]) -> int:
        
        max_steals = {}
        
        def rob(house):
            
            if house in max_steals:
                return max_steals[house]
            if house >= len(nums):
                return 0
            
            max_steals[house] = max(nums[house]+rob(house+2), rob(house+1))
            return max_steals[house]
        
        rob(0)
        return max_steals[0]
