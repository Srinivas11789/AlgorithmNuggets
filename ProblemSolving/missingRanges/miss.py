class Solution:
    
    # Naive iteration logic: 95% faster 100 pass
    
    def constructStrRange(self, l,u):
        if l == u:
            return str(l)
        else:
            return str(l)+"->"+str(u)
            
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        missing_ranges = []
        for i in range(len(nums)):
            # Edge case 1
            if nums[i] < lower or nums[i] > upper:
                continue
                
            # Initial ranges
            if i == 0 and nums[i] > lower:
                missing_ranges.append(self.constructStrRange(lower, nums[i]-1))
            if i == len(nums)-1 and nums[i]+1 <= upper: 
                missing_ranges.append(self.constructStrRange(nums[i]+1, upper))
            
            # Edge case 2
            if i+1 >= len(nums):
                continue
            if nums[i]+1 == nums[i+1]:
                continue
                
            # Add ranges
            l = nums[i]+1
            h = nums[i+1]-1
            missing_ranges.append(self.constructStrRange(l, h))
        
        if not nums:
            missing_ranges.append(self.constructStrRange(lower, upper))
        
        return missing_ranges

